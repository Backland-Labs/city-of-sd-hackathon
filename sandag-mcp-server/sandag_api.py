"""Core API client for SANDAG Regional Data Warehouse ArcGIS REST services."""

from __future__ import annotations

import time
import json
from dataclasses import dataclass
from typing import Any

import httpx

BASE_REST = "https://geo.sandag.org/server/rest/services"
HOSTED_JSON = f"{BASE_REST}/Hosted"
RDW_LIST_QUERY_URL = f"{BASE_REST}/Hosted/RDW_List/FeatureServer/0/query"
RDW_LIST_QUERY_PARAMS = {
    "where": "1=1",
    "outFields": "dataset_name,category1,category2,categories,tags,shape_type,rest_url",
    "resultRecordCount": 2000,
}


@dataclass(frozen=True)
class ServiceEntry:
    service_name: str
    service_type: str
    service_url: str
    dataset_name: str | None
    category1: str | None
    category2: str | None
    categories: str | None
    shape_type: str | None
    tags: str | None


class SandagApi:
    """Client and cache for SANDAG ArcGIS REST API."""

    def __init__(self, timeout_seconds: float = 30.0, cache_ttl_seconds: int = 600) -> None:
        self.timeout_seconds = timeout_seconds
        self.cache_ttl_seconds = cache_ttl_seconds
        self._catalog_ts: float = 0.0
        self._catalog: dict[str, ServiceEntry] = {}

    async def _get_json(self, url: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        query = {"f": "json"}
        if params:
            for key, value in params.items():
                if isinstance(value, (dict, list)):
                    query[key] = json.dumps(value)
                else:
                    query[key] = value
        async with httpx.AsyncClient(timeout=self.timeout_seconds, follow_redirects=True) as client:
            response = await client.get(url, params=query)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, dict) and "error" in data:
                raise ValueError(f"ArcGIS REST error: {data['error']}")
            return data

    async def refresh_catalog(self) -> dict[str, ServiceEntry]:
        hosted = await self._get_json(HOSTED_JSON)
        services = hosted.get("services", [])

        rdw = await self._get_json(RDW_LIST_QUERY_URL, params=RDW_LIST_QUERY_PARAMS)
        rows = rdw.get("features", [])
        meta_by_rest_url: dict[str, dict[str, Any]] = {}
        meta_by_name: dict[str, dict[str, Any]] = {}

        for row in rows:
            attrs = row.get("attributes", {})
            rest_url = (attrs.get("rest_url") or "").strip()
            dataset_name = (attrs.get("dataset_name") or "").strip()
            if rest_url:
                meta_by_rest_url[rest_url.lower()] = attrs
            if dataset_name:
                meta_by_name[dataset_name.lower()] = attrs

        catalog: dict[str, ServiceEntry] = {}
        for svc in services:
            full_name = svc.get("name", "")
            svc_type = svc.get("type", "")
            service_url = f"{BASE_REST}/{full_name}/{svc_type}"
            dataset_name = full_name.split("/", 1)[-1] if "/" in full_name else full_name

            attrs = meta_by_rest_url.get(service_url.lower()) or meta_by_name.get(dataset_name.lower()) or {}

            entry = ServiceEntry(
                service_name=dataset_name,
                service_type=svc_type,
                service_url=service_url,
                dataset_name=attrs.get("dataset_name") or dataset_name,
                category1=attrs.get("category1"),
                category2=attrs.get("category2"),
                categories=attrs.get("categories"),
                shape_type=attrs.get("shape_type"),
                tags=attrs.get("tags"),
            )
            catalog[dataset_name.lower()] = entry

        self._catalog = catalog
        self._catalog_ts = time.time()
        return catalog

    async def get_catalog(self, force_refresh: bool = False) -> dict[str, ServiceEntry]:
        if force_refresh or not self._catalog or (time.time() - self._catalog_ts) > self.cache_ttl_seconds:
            return await self.refresh_catalog()
        return self._catalog

    async def resolve_service(self, service: str) -> ServiceEntry:
        catalog = await self.get_catalog()
        key = service.strip().lower()

        if key in catalog:
            return catalog[key]

        # URL input support
        for entry in catalog.values():
            if entry.service_url.lower() == key:
                return entry

        raise KeyError(f"Unknown service: {service}")

    async def list_services(
        self,
        service_type: str | None = None,
        category: str | None = None,
        search: str | None = None,
        limit: int = 500,
    ) -> list[ServiceEntry]:
        catalog = await self.get_catalog()
        results = list(catalog.values())

        if service_type:
            st = service_type.lower()
            results = [r for r in results if r.service_type.lower() == st]

        if category:
            c = category.lower()
            results = [
                r for r in results
                if (r.category1 and c in r.category1.lower())
                or (r.category2 and c in r.category2.lower())
                or (r.categories and c in r.categories.lower())
            ]

        if search:
            q = search.lower()
            results = [
                r for r in results
                if q in r.service_name.lower()
                or (r.tags and q in r.tags.lower())
                or (r.dataset_name and q in r.dataset_name.lower())
            ]

        results.sort(key=lambda r: r.service_name.lower())
        return results[: max(1, min(limit, 2000))]

    async def get_service_metadata(self, service: str) -> dict[str, Any]:
        entry = await self.resolve_service(service)
        data = await self._get_json(entry.service_url)
        return {
            "service": entry.__dict__,
            "capabilities": data.get("capabilities"),
            "description": data.get("description"),
            "copyrightText": data.get("copyrightText"),
            "layers": data.get("layers", []),
            "tables": data.get("tables", []),
            "supportedQueryFormats": data.get("supportedQueryFormats"),
            "supportedExportFormats": data.get("supportedExportFormats"),
            "maxRecordCount": data.get("maxRecordCount"),
            "raw": data,
        }

    async def get_layer_metadata(self, service: str, layer_id: int = 0) -> dict[str, Any]:
        entry = await self.resolve_service(service)
        layer_url = f"{entry.service_url}/{layer_id}"
        data = await self._get_json(layer_url)
        return {
            "service": entry.__dict__,
            "layerId": layer_id,
            "layerUrl": layer_url,
            "name": data.get("name"),
            "type": data.get("type"),
            "geometryType": data.get("geometryType"),
            "description": data.get("description"),
            "fields": data.get("fields", []),
            "capabilities": data.get("capabilities"),
            "maxRecordCount": data.get("maxRecordCount"),
            "supportedQueryFormats": data.get("supportedQueryFormats"),
            "supportedSpatialRelationships": data.get("supportedSpatialRelationships", []),
            "raw": data,
        }

    async def query_layer(
        self,
        service: str,
        layer_id: int = 0,
        where: str = "1=1",
        out_fields: str = "*",
        limit: int = 100,
        offset: int = 0,
        order_by: str | None = None,
        return_geometry: bool = False,
        out_sr: int | None = 4326,
    ) -> dict[str, Any]:
        entry = await self.resolve_service(service)
        layer_url = f"{entry.service_url}/{layer_id}/query"

        params: dict[str, Any] = {
            "where": where,
            "outFields": out_fields,
            "resultRecordCount": max(1, min(limit, 2000)),
            "resultOffset": max(0, offset),
            "returnGeometry": str(return_geometry).lower(),
        }
        if order_by:
            params["orderByFields"] = order_by
        if out_sr is not None:
            params["outSR"] = out_sr

        data = await self._get_json(layer_url, params=params)
        return {
            "service": entry.__dict__,
            "layerId": layer_id,
            "query": params,
            "featureCount": len(data.get("features", [])),
            "exceededTransferLimit": data.get("exceededTransferLimit", False),
            "fields": data.get("fields", []),
            "features": data.get("features", []),
            "objectIdFieldName": data.get("objectIdFieldName"),
            "geometryType": data.get("geometryType"),
            "spatialReference": data.get("spatialReference"),
        }

    async def query_layer_stats(
        self,
        service: str,
        layer_id: int,
        out_statistics: list[dict[str, Any]],
        where: str = "1=1",
        group_by_fields_for_statistics: str | None = None,
    ) -> dict[str, Any]:
        entry = await self.resolve_service(service)
        layer_url = f"{entry.service_url}/{layer_id}/query"

        params: dict[str, Any] = {
            "where": where,
            "outStatistics": out_statistics,
            "returnGeometry": "false",
        }
        if group_by_fields_for_statistics:
            params["groupByFieldsForStatistics"] = group_by_fields_for_statistics

        data = await self._get_json(layer_url, params=params)
        return {
            "service": entry.__dict__,
            "layerId": layer_id,
            "query": params,
            "fields": data.get("fields", []),
            "features": data.get("features", []),
        }

    async def rest_get(self, path_or_url: str, extra_params: dict[str, Any] | None = None) -> dict[str, Any]:
        target = path_or_url.strip()
        if target.startswith("http://") or target.startswith("https://"):
            if not target.startswith(BASE_REST):
                raise ValueError("Only SANDAG ArcGIS REST URLs under /server/rest/services are allowed")
            url = target
        else:
            if target.startswith("/"):
                target = target[1:]
            url = f"{BASE_REST}/{target}"

        params = extra_params or {}
        return await self._get_json(url, params=params)

    async def recommend_services(self, user_task: str, top_k: int = 10) -> list[dict[str, Any]]:
        catalog = await self.get_catalog()
        terms = [t.strip().lower() for t in user_task.replace("/", " ").replace(",", " ").split() if t.strip()]
        scored: list[tuple[int, ServiceEntry, list[str]]] = []

        for entry in catalog.values():
            score = 0
            reasons: list[str] = []
            haystacks = {
                "name": (entry.service_name or "").lower(),
                "tags": (entry.tags or "").lower(),
                "category": " ".join(
                    [x for x in [entry.category1, entry.category2, entry.categories] if x]
                ).lower(),
                "shape_type": (entry.shape_type or "").lower(),
            }

            for term in terms:
                if len(term) < 3:
                    continue
                if term in haystacks["name"]:
                    score += 5
                    reasons.append(f"name matches '{term}'")
                if term in haystacks["tags"]:
                    score += 3
                    reasons.append(f"tags mention '{term}'")
                if term in haystacks["category"]:
                    score += 2
                    reasons.append(f"category relates to '{term}'")
                if term in haystacks["shape_type"]:
                    score += 1
                    reasons.append(f"shape type mentions '{term}'")

            if score > 0:
                scored.append((score, entry, reasons))

        scored.sort(key=lambda x: (-x[0], x[1].service_name.lower()))
        top = scored[: max(1, min(top_k, 50))]

        return [
            {
                "score": score,
                "service_name": entry.service_name,
                "service_type": entry.service_type,
                "service_url": entry.service_url,
                "category1": entry.category1,
                "category2": entry.category2,
                "shape_type": entry.shape_type,
                "tags": entry.tags,
                "why": reasons[:5],
                "recommended_next_calls": [
                    "get_service_metadata",
                    "list_layers",
                    "get_layer_metadata",
                    "query_layer",
                ],
            }
            for score, entry, reasons in top
        ]
