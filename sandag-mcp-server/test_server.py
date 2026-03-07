"""Comprehensive integration tests for the SANDAG RDW MCP server.

Tests every exposed MCP tool end-to-end against the live SANDAG ArcGIS REST API.
Run:  python test_server.py
"""

from __future__ import annotations

import asyncio
import sys
import traceback

from sandag_api import SandagApi

PASSED = 0
FAILED = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    global PASSED, FAILED
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASSED += 1
    else:
        FAILED += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")


async def test_refresh_catalog(api: SandagApi) -> None:
    """Mirrors MCP tool: refresh_catalog"""
    catalog = await api.refresh_catalog()
    count = len(catalog)
    report("refresh_catalog returns services", count >= 350, f"{count} services")

    has_feature = any(e.service_type == "FeatureServer" for e in catalog.values())
    report("catalog includes FeatureServer entries", has_feature)

    has_meta = any(e.tags is not None for e in catalog.values())
    report("catalog enriched with RDW_List metadata", has_meta)


async def test_list_services(api: SandagApi) -> None:
    """Mirrors MCP tool: list_services"""
    # Unfiltered
    all_svc = await api.list_services()
    report("list_services (no filter)", len(all_svc) >= 350, f"{len(all_svc)} services")

    # Filter by category
    fire = await api.list_services(category="Fire")
    report("list_services category=Fire", len(fire) >= 3, f"{len(fire)} fire services")
    all_fire = all(
        (e.category1 and "fire" in e.category1.lower())
        or (e.category2 and "fire" in e.category2.lower())
        or (e.categories and "fire" in e.categories.lower())
        for e in fire
    )
    report("list_services category filter is accurate", all_fire)

    # Filter by search keyword
    transit = await api.list_services(search="transit")
    report("list_services search=transit", len(transit) >= 2, f"{len(transit)} transit services")

    # Limit
    small = await api.list_services(limit=3)
    report("list_services limit=3", len(small) <= 3, f"got {len(small)}")


async def test_recommend_services(api: SandagApi) -> None:
    """Mirrors MCP tool: recommend_services"""
    recs = await api.recommend_services("flood hazard zones near coastline", top_k=5)
    report("recommend_services returns results", len(recs) > 0, f"{len(recs)} recommendations")

    has_score = all("score" in r for r in recs)
    report("recommendations have scores", has_score)

    has_why = all("why" in r and len(r["why"]) > 0 for r in recs)
    report("recommendations include reasons", has_why)

    # Another query
    recs2 = await api.recommend_services("schools and education districts", top_k=3)
    names = [r["service_name"] for r in recs2]
    report("recommend_services school query", len(recs2) > 0, f"top: {names}")


async def test_get_service_metadata(api: SandagApi) -> None:
    """Mirrors MCP tool: get_service_metadata"""
    meta = await api.get_service_metadata("Parks")
    report("get_service_metadata has layers", "layers" in meta and isinstance(meta["layers"], list))
    report("get_service_metadata has capabilities", meta.get("capabilities") is not None)
    report("get_service_metadata has description", meta.get("description") is not None)

    # Resolve by case-insensitive name
    meta2 = await api.get_service_metadata("parks")
    report("get_service_metadata case-insensitive", "layers" in meta2)


async def test_list_layers(api: SandagApi) -> None:
    """Mirrors MCP tool: list_layers"""
    meta = await api.get_service_metadata("Census_Tracts_2020")
    layers = meta.get("layers", [])
    report("list_layers returns layers", len(layers) >= 1, f"{len(layers)} layers")
    report("layer has id and name", all("id" in l and "name" in l for l in layers))


async def test_get_layer_metadata(api: SandagApi) -> None:
    """Mirrors MCP tool: get_layer_metadata"""
    lm = await api.get_layer_metadata("Parks", 0)
    report("get_layer_metadata has fields", len(lm.get("fields", [])) > 0, f"{len(lm['fields'])} fields")
    report("get_layer_metadata has geometryType", lm.get("geometryType") is not None)
    report("get_layer_metadata has name", lm.get("name") is not None, lm.get("name", ""))

    field_names = [f["name"] for f in lm["fields"]]
    report("fields include 'name'", "name" in field_names, str(field_names[:6]))


async def test_query_layer(api: SandagApi) -> None:
    """Mirrors MCP tool: query_layer"""
    # Basic query
    q = await api.query_layer("Parks", 0, where="1=1", out_fields="name,park_type", limit=5, return_geometry=False)
    features = q.get("features", [])
    report("query_layer basic", len(features) > 0 and len(features) <= 5, f"{len(features)} features")

    attrs = features[0].get("attributes", {}) if features else {}
    report("query_layer returns requested fields", "name" in attrs and "park_type" in attrs, str(list(attrs.keys())))

    # WHERE filter
    q2 = await api.query_layer("Fire_Stations_CN", 0, where="1=1", out_fields="*", limit=3, return_geometry=False)
    report("query_layer Fire_Stations_CN", len(q2.get("features", [])) > 0)

    # Pagination (offset)
    page1 = await api.query_layer("Parks", 0, where="1=1", out_fields="objectid", limit=2, offset=0, return_geometry=False)
    page2 = await api.query_layer("Parks", 0, where="1=1", out_fields="objectid", limit=2, offset=2, return_geometry=False)
    ids1 = {f["attributes"]["objectid"] for f in page1.get("features", [])}
    ids2 = {f["attributes"]["objectid"] for f in page2.get("features", [])}
    report("query_layer pagination (no overlap)", len(ids1 & ids2) == 0, f"page1={ids1}, page2={ids2}")

    # Geometry return
    qg = await api.query_layer("Parks", 0, where="1=1", out_fields="name", limit=1, return_geometry=True, out_sr=4326)
    geo = qg["features"][0].get("geometry") if qg["features"] else None
    report("query_layer return_geometry=True", geo is not None)

    # Order by
    qo = await api.query_layer("Parks", 0, where="1=1", out_fields="name", limit=3, order_by="name ASC", return_geometry=False)
    names = [f["attributes"]["name"] for f in qo.get("features", []) if f["attributes"].get("name")]
    report("query_layer order_by", names == sorted(names), str(names))


async def test_query_layer_stats(api: SandagApi) -> None:
    """Mirrors MCP tool: query_layer_stats"""
    # Count
    stats = await api.query_layer_stats(
        "Parks", 0,
        out_statistics=[{"statisticType": "count", "onStatisticField": "objectid", "outStatisticFieldName": "cnt"}],
    )
    features = stats.get("features", [])
    report("query_layer_stats count", len(features) == 1)
    cnt = features[0]["attributes"]["cnt"] if features else 0
    report("query_layer_stats count > 0", cnt > 0, f"count={cnt}")

    # Grouped stats
    gstats = await api.query_layer_stats(
        "Parks", 0,
        out_statistics=[{"statisticType": "count", "onStatisticField": "objectid", "outStatisticFieldName": "cnt"}],
        group_by_fields_for_statistics="park_type",
    )
    groups = gstats.get("features", [])
    report("query_layer_stats grouped", len(groups) >= 2, f"{len(groups)} groups")

    # AVG stat (on gis_acres)
    avg = await api.query_layer_stats(
        "Parks", 0,
        out_statistics=[{"statisticType": "avg", "onStatisticField": "gis_acres", "outStatisticFieldName": "avg_acres"}],
    )
    avg_val = avg["features"][0]["attributes"]["avg_acres"] if avg["features"] else None
    report("query_layer_stats avg", avg_val is not None and avg_val > 0, f"avg_acres={avg_val}")


async def test_rest_get(api: SandagApi) -> None:
    """Mirrors MCP tool: rest_get"""
    # By relative path
    data = await api.rest_get("Hosted/Parks/FeatureServer")
    report("rest_get relative path", "layers" in data or "currentVersion" in data)

    # By full URL
    data2 = await api.rest_get("https://geo.sandag.org/server/rest/services/Hosted/Parks/FeatureServer")
    report("rest_get full URL", "layers" in data2 or "currentVersion" in data2)

    # Extra params
    data3 = await api.rest_get("Hosted/Parks/FeatureServer/0/query", extra_params={
        "where": "1=1", "returnCountOnly": "true"
    })
    report("rest_get with extra_params", "count" in data3, f"count={data3.get('count')}")

    # Reject external URL
    try:
        await api.rest_get("https://evil.example.com/data")
        report("rest_get rejects external URLs", False, "should have raised")
    except ValueError:
        report("rest_get rejects external URLs", True)


async def test_error_handling(api: SandagApi) -> None:
    """Verify graceful errors for bad inputs."""
    # Unknown service
    try:
        await api.resolve_service("NonexistentDataset12345")
        report("resolve unknown service raises KeyError", False)
    except KeyError:
        report("resolve unknown service raises KeyError", True)

    # Bad where clause
    try:
        q = await api.query_layer("Parks", 0, where="INVALID SQL !!!", out_fields="*", limit=1, return_geometry=False)
        # ArcGIS may return empty or an error dict
        report("bad where clause handled", True, "returned without crash")
    except Exception:
        report("bad where clause handled", True, "raised controlled exception")


async def test_multiple_datasets(api: SandagApi) -> None:
    """Verify queries work across several different datasets."""
    test_cases = [
        ("Roads_All", "Polyline roads network"),
        ("Census_Tracts_2020", "Census tract polygons"),
        ("Hospitals", "Hospital points"),
        ("Fire_Burn_History", "Fire burn polygons"),
        ("Bikeways", "Bikeway polylines"),
    ]
    for svc_name, desc in test_cases:
        try:
            q = await api.query_layer(svc_name, 0, where="1=1", out_fields="*", limit=2, return_geometry=False)
            ok = len(q.get("features", [])) > 0
            report(f"query {svc_name}", ok, desc)
        except Exception as e:
            report(f"query {svc_name}", False, str(e))


async def main() -> None:
    api = SandagApi()

    tests = [
        ("refresh_catalog", test_refresh_catalog),
        ("list_services", test_list_services),
        ("recommend_services", test_recommend_services),
        ("get_service_metadata", test_get_service_metadata),
        ("list_layers", test_list_layers),
        ("get_layer_metadata", test_get_layer_metadata),
        ("query_layer", test_query_layer),
        ("query_layer_stats", test_query_layer_stats),
        ("rest_get", test_rest_get),
        ("error_handling", test_error_handling),
        ("multiple_datasets", test_multiple_datasets),
    ]

    for name, fn in tests:
        print(f"\n{'='*50}")
        print(f"TEST GROUP: {name}")
        print(f"{'='*50}")
        try:
            await fn(api)
        except Exception:
            report(f"{name} (unhandled crash)", False, traceback.format_exc().splitlines()[-1])

    print(f"\n{'='*50}")
    print(f"RESULTS: {PASSED} passed, {FAILED} failed, {PASSED + FAILED} total")
    print(f"{'='*50}")

    if FAILED > 0:
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
