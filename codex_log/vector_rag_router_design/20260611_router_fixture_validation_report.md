# 20260611 Router Fixture Validation Report

## 1. validation_status

- `validation_status`: `passed`
- `project_route`: `video_factory`
- `branch`: `feature/vector-rag-router-design-20260611`
- `execution_mode`: `offline_router_fixture_dry_run`
- `external_api_called`: `false`
- `secrets_read_or_printed`: `false`
- `media_generated`: `false`
- `rag_runtime_implemented`: `false`
- `vector_index_created`: `false`
- `skill_registry_runtime_implemented`: `false`

## 2. files_created

| file_path | role |
|---|---|
| `codex_log/vector_rag_router_design/fixtures/README.md` | fixture directory usage note |
| `codex_log/vector_rag_router_design/fixtures/20260611_router_fixtures.json` | three router input fixtures and expected decisions |
| `codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results.json` | generated dry-run result JSON |
| `scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py` | deterministic offline dry-run script |
| `codex_log/vector_rag_router_design/20260611_router_fixture_validation_report.md` | human-readable validation report |

## 3. commands_run

```bash
python3 scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py
python3 -m json.tool codex_log/vector_rag_router_design/fixtures/20260611_router_fixtures.json
python3 -m py_compile scripts/vector_rag_router_design/路由器fixture空跑_router_fixture_dry_run.py
```

## 4. dry_run_summary

| metric | value |
|---|---:|
| fixture_count | 3 |
| passed_count | 3 |
| failed_count | 0 |
| overall_status | `passed` |

## 5. fixture_results

| fixture_id | expected_router_behavior | actual_status |
|---|---|---|
| `new_material_defaults_to_additive_merge` | 新增素材默认 `additive_merge`，必须重建旧候选、锁稿、旧素材、新素材、最新复审问题的完整上下文；不得默认 `exclusive_new_only` | passed |
| `technical_preview_cannot_complete` | `technical_preview` / `full.mp4 exists` / 字段存在不能冒充 `completed`；缺 preflight 与 completion truth 时必须 blocked | passed |
| `old_qwen_b_is_reference_anchor_only` | 旧 Qwen / 阿里 B 声音只能作为 `reference_anchor_only`；当前正式声音锁仍是 MiniMax + `oldBMinimax20260528010200` | passed |

## 6. evidence

Generated result file:

- `codex_log/vector_rag_router_design/fixtures/20260611_router_dry_run_results.json`

Key result fields:

```json
{
  "overall_status": "passed",
  "fixture_count": 3,
  "passed_count": 3,
  "failed_count": 0,
  "external_api_called": false,
  "secrets_read_or_printed": false,
  "media_generated": false
}
```

## 7. limitations

- This is an offline deterministic fixture dry-run, not a real RAG retrieval run.
- This does not create a vector index.
- This does not prove future Router runtime is implemented.
- This does not call Alibaba / DashScope / DashVector APIs.
- This does not generate or modify video, audio, image, subtitle, card, or review-pack media.

## 8. completion_boundary

This validation proves only that the three minimal Router fixture decisions are represented, executable by a local dry-run script, and currently pass their expected outputs. It does not replace the future RAG Router implementation or production retrieval validation.
