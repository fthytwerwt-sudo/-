# 20260611 Vector Ingestion Blacklist

## 0. purpose

This blacklist prevents a future vector index from reviving stale rules, leaking secrets, indexing private media, or treating generated artifacts as project facts.

This is a design artifact only. It does not delete files.

## 1. hard_do_not_index

| category | examples | reason |
|---|---|---|
| secret files and local runtime config | `.env`, `*.local.*`, runtime auth config, key stores | no secret access or storage in vector DB |
| API key/token/secret values | any actual credential value | forbidden; variable names may be documented, values never |
| raw media | `*.mp4`, `*.mov`, `*.wav`, `*.mp3`, `*.png`, `*.jpg`, `*.jpeg` | large/private/binary; index metadata reports instead |
| generated media folders | `dist/**` media assets, keyframes, contact sheets | use summary/manifest/report metadata only |
| raw screenshots with platform/user data | `review_loop/screenshots/**/*.png` | potential privacy/platform data; use screenshot manifests and extracted records |
| temporary build/runtime output | caches, temp render output, diagnostics media | noisy and unstable |
| local external paths as authority | Desktop/Downloads/tmp/external worktrees | single workspace rule; index only normalized in-repo references |
| untracked unrelated files | current `public/` | not part of this task or committed project facts |

## 2. deprecated_do_not_use_by_default

| item | blacklist_scope | reason |
|---|---|---|
| `gray_test` as current project stage | default retrieval | superseded by `formal_operation_active` |
| `technical_preview` as delivery | default retrieval | only `internal_diagnostic_only` |
| `vertical_9_16 / 1080x1920` as current formal default | default retrieval | superseded by horizontal 16:9 / 1920x1080 for formal-operation delivery |
| old `v3` as default future base | default retrieval | superseded by later baseline/current facts |
| `PR #7 A` as current reaction-card reference | default retrieval | PR #7 B is current reaction route |
| old Qwen/Aliyun B as formal TTS provider | default retrieval | now reference anchor only; MiniMax route/voice lock required |
| MiniMax system voices as old B replacement | default retrieval | forbidden after old B MiniMax voice lock |
| `female-tianmei` as default B voice | default retrieval | explicitly rejected/not allowed unless future user reversal |
| local fallback TTS/macOS say/silent audio as publish candidate | default retrieval | can only be blocked/internal diagnostic |
| `full.mp4 exists` as completion proof | default retrieval | completion truth and preflight required |
| `content_route_card` or `script_to_timeline_map` as delivery | default retrieval | intermediate artifacts only |
| static card pretending to be HyperFrames | default retrieval | violates motion wrapper boundary |

## 3. legacy_demote_only

These may be indexed only when the Router explicitly asks for history, conflict archaeology, or reference lineage.

| source_or_rule | demotion_reason |
|---|---|
| `project_source/` broad historical copies | lower authority than current `GPT数据源/`, `codex_log/latest.md`, and `codex_source/` |
| old GPT Project static upload package notes | static package is not current dynamic repo fact |
| `codex_log/current_gray_test_target.md` | legacy compatibility pointer |
| older `dist/latest_review_pack` media evidence | use current summary/manifest only unless task is v3.1 review archaeology |
| older DeepSeek supply packs | supply evidence only, not project fact authority |
| old reference videos/cards not in current whitelist | reference only and must pass current contract |

## 4. conflict_pending_do_not_auto_promote

| conflict | index_policy |
|---|---|
| `MiniMax formal route` vs old `Qwen/Aliyun B` lineage | index as conflict; current default is MiniMax with old B as reference anchor |
| `formal_operation_active` vs older `gray_test` records | current phase wins; old records retain historical tag |
| `publish_candidate_ready_for_human_review` vs `send_ready` | never merge; send_ready remains false until final confirmation |
| `technical_validation` vs `content_validation` | never merge; technical pass does not imply content pass |
| `HyperFrames runtime found` vs `formal video chain integrated` | runtime proof does not imply full chain stability |
| `current_data_goal_anchor partial_data_recorded` vs ready | partial is not ready |
| `new material added` vs `old material replaced` | default additive; exclusive/replacement requires explicit scope |

## 5. source_path_filters

Default exclude patterns for future ingestion:

```text
**/.env
**/.env.*
**/*secret*
**/*token*
**/*credential*
**/*.mp4
**/*.mov
**/*.wav
**/*.mp3
**/*.png
**/*.jpg
**/*.jpeg
**/*.webp
**/*.psd
**/*.zip
**/*.tar
**/*.gz
dist/**/problem_windows/*.mp4
review_loop/screenshots/**/*.png
codex_log/**/samples/*.mp3
codex_log/**/samples/*.wav
public/**
```

Allowlist exceptions:

- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`
- `review_loop/**/screenshot_manifest.md`
- sanitized diagnostic `.md` / `.json` reports that contain no secret values and no raw private data.

## 6. sensitive_text_filters

If a text file contains the following, chunking must either redact or exclude:

| signal | action |
|---|---|
| actual key assignment | exclude chunk |
| Bearer token-like value | exclude chunk |
| signed URL with credential query | redact URL or exclude |
| local user account/private path beyond in-repo canonical path | redact unless path itself is necessary project evidence |
| platform private message/customer data | index only normalized record fields |
| raw voice sample upload URL | exclude or store only `exists=true` and route metadata |

## 7. anti_noise_rules

Do not index:

- test command output dumps unless they are curated verification reports.
- repeated generated logs that duplicate the same current fact.
- historical failed attempts unless tagged as failure case and demoted.
- shell stdout that includes environment state.
- whole `codex_log/latest.md` as one blob; chunk by date section.
- whole `GPT数据源/05_文案路由规则.md` as one blob; chunk by mechanism heading.

## 8. blacklisted_completion_shortcuts

The future RAG Router must treat these phrases as risk signals, not as completion proof:

- `already generated full.mp4`
- `technical validation passed`
- `script_to_timeline_map exists`
- `tts_prosody_anchor_map exists`
- `review pack generated`
- `HyperFrames rendered`
- `DeepSeek supplied`
- `image looks good`
- `publish_candidate_ready_for_human_review`

Required completion retrieval must include the matching preflight and completion truth evidence.
