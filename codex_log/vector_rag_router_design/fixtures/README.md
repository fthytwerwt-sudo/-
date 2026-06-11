# Router Fixture Dry-Run Fixtures

## Purpose

This directory contains the minimal offline validation fixtures for the future 《视频工厂》 RAG Router.

These fixtures do not implement RAG, do not build a vector index, do not call Alibaba / DashScope / DashVector APIs, and do not generate media. They only verify that three high-risk routing decisions can be represented and checked with deterministic local rules.

## Files

| file | role |
|---|---|
| `20260611_router_fixtures.json` | Input fixtures and expected router decisions |
| `20260611_router_dry_run_results.json` | Generated dry-run results from the local script |
| `../20260611_router_fixture_validation_report.md` | Human-readable validation summary |

## Fixture Coverage

1. `new_material_defaults_to_additive_merge`: new material should default to `additive_merge`, not `exclusive_new_only`.
2. `technical_preview_cannot_complete`: `technical_preview` and partial artifacts must not become `completed`.
3. `old_qwen_b_is_reference_anchor_only`: old Qwen / Aliyun B voice can only be a `reference_anchor`; current formal voice lock remains MiniMax + `oldBMinimax20260528010200`.

## Dry Run

```bash
python3 scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py
```

Expected result:

- `overall_status = passed`
- every fixture has `actual_decision_matches_expected = true`
- no external API call
- no secret read
- no media generation
