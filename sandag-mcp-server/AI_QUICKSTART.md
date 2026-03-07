# SANDAG RDW MCP: AI Quickstart

Use this server to discover and query SANDAG ArcGIS REST datasets.

## Tool Order (Default)
1. `recommend_services(user_task)` when the user request is vague.
2. `get_service_metadata(service)` to confirm service capabilities.
3. `list_layers(service)` and `get_layer_metadata(service, layer_id)` to inspect schema.
4. `query_layer(...)` for records.
5. `query_layer_stats(...)` for aggregates.
6. `rest_get(...)` only for advanced ArcGIS endpoints not covered above.

## Which Tool to Use
- `recommend_services`: user asks domain questions like "flood risk", "parks", "zoning", "voting".
- `list_services`: user already knows category/type/search terms.
- `query_layer`: row-level data retrieval with `where`, `out_fields`, `limit`, `offset`.
- `query_layer_stats`: counts, sums, averages, grouped statistics.
- `rest_get`: power-user ArcGIS operations (read-only) under `/server/rest/services`.

## Minimal Examples

### 1) Find likely datasets
```json
{"user_task":"Find parks and open space in San Diego", "top_k": 5}
```
Call: `recommend_services`

### 2) Inspect schema before querying
```json
{"service":"Parks", "layer_id":0}
```
Call: `get_layer_metadata`

### 3) Fetch records
```json
{
  "service":"Parks",
  "layer_id":0,
  "where":"1=1",
  "out_fields":"name,park_type,ownership",
  "limit":50,
  "order_by":"name ASC",
  "return_geometry":false
}
```
Call: `query_layer`

### 4) Aggregate stats
```json
{
  "service":"Parks",
  "layer_id":0,
  "where":"1=1",
  "out_statistics":[
    {
      "statisticType":"count",
      "onStatisticField":"objectid",
      "outStatisticFieldName":"feature_count"
    }
  ]
}
```
Call: `query_layer_stats`

## Good AI Behavior
- Always inspect layer fields before writing strict `where` clauses.
- Keep `limit` small first, then paginate with `offset`.
- Use `out_fields` instead of `*` when possible.
- If no results, verify field names and case via `get_layer_metadata`.
- For unknown dataset names, never guess: use `recommend_services` first.
