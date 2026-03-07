"""MCP server exposing all SANDAG Regional Data Warehouse ArcGIS REST endpoints."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from sandag_api import SandagApi

mcp = FastMCP(
    name="sandag-rdw",
    instructions=(
        "This server provides comprehensive access to SANDAG Regional Data Warehouse ArcGIS REST endpoints. "
        "Use list_services to discover datasets, recommend_services when unsure which dataset matches a task, "
        "get_service_metadata and get_layer_metadata to understand schema/capabilities, and query_layer or "
        "query_layer_stats for data retrieval and analysis. Use rest_get for advanced ArcGIS operations not "
        "directly wrapped by other tools."
    ),
)

api = SandagApi()


@mcp.tool(description="Refresh and return the full live catalog of exposed Hosted services/endpoints.")
async def refresh_catalog() -> dict[str, Any]:
    catalog = await api.refresh_catalog()
    return {
        "service_count": len(catalog),
        "services": [entry.__dict__ for entry in sorted(catalog.values(), key=lambda e: e.service_name.lower())],
    }


@mcp.tool(description="List services with optional filtering by type, category, and free-text search.")
async def list_services(
    service_type: str | None = None,
    category: str | None = None,
    search: str | None = None,
    limit: int = 200,
) -> dict[str, Any]:
    services = await api.list_services(service_type=service_type, category=category, search=search, limit=limit)
    return {
        "count": len(services),
        "services": [s.__dict__ for s in services],
    }


@mcp.tool(
    description=(
        "Recommend likely datasets/endpoints for a user question. "
        "Use this first when uncertain which endpoint to call."
    )
)
async def recommend_services(user_task: str, top_k: int = 10) -> dict[str, Any]:
    return {
        "task": user_task,
        "recommendations": await api.recommend_services(user_task=user_task, top_k=top_k),
        "next_step_guidance": [
            "For each recommendation: call get_service_metadata",
            "Then call list_layers/get_layer_metadata",
            "Then call query_layer with explicit where and out_fields",
            "For aggregates, call query_layer_stats",
        ],
    }


@mcp.tool(description="Get metadata and capabilities for a specific service by name (e.g. 'Parks') or service URL.")
async def get_service_metadata(service: str) -> dict[str, Any]:
    return await api.get_service_metadata(service=service)


@mcp.tool(description="List layer/table IDs and names for a specific service.")
async def list_layers(service: str) -> dict[str, Any]:
    meta = await api.get_service_metadata(service=service)
    return {
        "service": meta["service"],
        "layers": meta.get("layers", []),
        "tables": meta.get("tables", []),
    }


@mcp.tool(description="Get full schema/capabilities metadata for a specific layer ID in a service.")
async def get_layer_metadata(service: str, layer_id: int = 0) -> dict[str, Any]:
    return await api.get_layer_metadata(service=service, layer_id=layer_id)


@mcp.tool(
    description=(
        "Query features from a layer/table. Typical flow: find service -> inspect fields -> query with where/out_fields. "
        "Supports pagination with limit/offset."
    )
)
async def query_layer(
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
    return await api.query_layer(
        service=service,
        layer_id=layer_id,
        where=where,
        out_fields=out_fields,
        limit=limit,
        offset=offset,
        order_by=order_by,
        return_geometry=return_geometry,
        out_sr=out_sr,
    )


@mcp.tool(
    description=(
        "Run ArcGIS outStatistics queries (count/sum/avg/min/max/stddev/var/etc). "
        "Pass out_statistics as ArcGIS JSON objects."
    )
)
async def query_layer_stats(
    service: str,
    layer_id: int,
    out_statistics: list[dict[str, Any]],
    where: str = "1=1",
    group_by_fields_for_statistics: str | None = None,
) -> dict[str, Any]:
    return await api.query_layer_stats(
        service=service,
        layer_id=layer_id,
        out_statistics=out_statistics,
        where=where,
        group_by_fields_for_statistics=group_by_fields_for_statistics,
    )


@mcp.tool(
    description=(
        "Raw read-only ArcGIS REST GET for any endpoint under https://geo.sandag.org/server/rest/services. "
        "Use for advanced operations not covered by wrapper tools (e.g., specific export/query params)."
    )
)
async def rest_get(path_or_url: str, extra_params: dict[str, Any] | None = None) -> dict[str, Any]:
    return await api.rest_get(path_or_url=path_or_url, extra_params=extra_params)


if __name__ == "__main__":
    mcp.run(transport="stdio")
