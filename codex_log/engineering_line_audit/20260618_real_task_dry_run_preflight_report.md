# 20260618 Real Task Dry Run Preflight Report

## route_decision（路由判断）

```yaml
project_route（项目路由）: video_factory（视频工厂）
task_type（任务类型）:
  - framework_dry_run_validation（框架干跑验证）
  - real_task_preflight_simulation（真实任务执行前模拟）
  - rag_default_route_probe_by_real_task（用真实任务探测 RAG 默认路线）
  - decision_gate_validation（决策闸门验证）
workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
execution_permission（执行权限）: dry_run_fixture_probe_report_only（仅允许干跑 fixture / probe / report / latest / index）
```

本轮只验证新框架是否能对一个真实《视频工厂》产出前任务做执行前判断。它不是视频生成，不是正式文案产出，不是真实 RAG（检索增强生成）调用，不启用 runtime（运行时），不启动 service（服务）。

## input_task（本轮输入任务）

```text
用户想用《视频工厂》的新整体框架，开始进入真实内容产出流程。
目标是：为一条后续正式运营视频任务做执行前判断，确认新框架能否自动判断 RAG、文案权限、卡片判断、素材证据、工具权限、失败回退和人工确认边界。
本轮只验证框架，不生成媒体。
```

这是一个真实产出前 dry run（干跑），不是抽象流程图。通过标准是框架能明确给出能做什么、不能做什么、需要谁确认、下一步缺什么。

## framework_routing（新框架如何路由）

```yaml
route_decision（路由判断）:
  project_route（项目路由）: video_factory（视频工厂）
  workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
  task_type（任务类型）: real_task_preflight_simulation（真实任务执行前模拟）
  is_video_generation（是否视频生成）: false（否）
  is_formal_copywriting（是否正式文案产出）: false（否）
  is_preflight_check（是否执行前检查）: true（是）
```

归位到 `mechanism_repair_flow（机制修补流）` 的原因是：本轮修的是框架进入真实产出前的判断能力，不是内容生产本身。若未来把 `preflight_validation_flow（执行前验证流）` 设为正式 workflow（工作流），必须另行经过用户 / ChatGPT 确认，不能在本轮直接启用。

## engineering_state_map_check（工程状态地图检查）

```yaml
current_status（当前状态）:
  framework_status（框架状态）: probe_only_safe_framework（仅限安全框架探测）
  runtime_status（运行时状态）: not_enabled（未启用）
  rag_runtime_status（RAG 运行时状态）: not_enabled（未启用）
  media_status（媒体状态）: not_generated（未生成）
allowed_statuses_applied（已应用允许状态）:
  - formal（正式）
  - candidate（候选）
  - probe_only（仅探测）
  - documented_only（仅文档）
  - missing（缺失）
  - conflict（冲突）
  - blocked（阻断）
```

本轮结论是：新框架的执行前判断能力通过本地 fixture / probe 验证，但仍属于 `probe_only_safe_framework（仅限安全框架探测）`，不能写成 runtime 已启用、service 已启动、真实 RAG 已接入或媒体链路已可用。

## rag_default_decision（RAG 默认判断）

```yaml
rag_default_entered（RAG 是否进入默认判断链）: true（是）
retrieval_manifest_requirement（检索清单要求）: required（必须）
source_path_required（是否必须来源路径）: true（是）
chunk_id_required（是否必须分块编号）: true（是）
readback_required（是否必须原文回读）: true（是）
real_dashvector_call_allowed（是否允许真实调用 DashVector）: false（否）
real_chroma_ingestion_allowed（是否允许 Chroma 入库）: false（否）
repo_fact_priority（仓库事实优先）: true（是）
```

RAG（检索增强生成）默认进入判断链，意思是：后续真实任务默认要准备检索清单、来源路径、分块编号和原文回读。它不表示本轮真实调用 DashVector（阿里向量数据库）或 Chroma（本地向量库），也不表示向量结果可以覆盖 GitHub / main 当前仓库事实。

## why_no_external_call（为什么没有真实外部调用）

本轮的验证对象是框架判断能力，不是外部工具能力。真实调用 DashVector、运行 Chroma ingestion、调用 TTS、调用外部 API、启动服务或生成媒体都会改变权限、成本、隐私或执行边界，必须先触发 `human_decision_gate（人工决策闸门）`。

因此本轮只允许本地 YAML fixture（测试样例）和 Python probe（探测脚本）验证，不打开端口，不联网，不读取真实媒体。

## allowed_actions（当前允许做什么）

- `route_task（路由任务）`: 判断项目、任务类型、workflow 和责任层。
- `run_preflight_dry_run（执行前干跑）`: 用真实任务输入模拟执行前检查。
- `create_fixture（创建测试样例）`: 新增 passing / blocked fixture。
- `create_local_probe（创建本地探测脚本）`: 新增只读 YAML probe。
- `create_report（创建报告）`: 写明输入、判断、缺口、验证和下一步。
- `update_schema_index（更新结构契约索引）`: 把本轮新增 fixture / probe 登记进索引。
- `update_latest（更新最新日志）`: 顶部记录本轮状态边界。
- `run_local_readonly_probe（运行本地只读探测）`: 只跑本地检查，不外呼。

## forbidden_actions（当前禁止做什么）

- 禁止生成视频、音频、字幕、卡片图片。
- 禁止生成正式文案。
- 禁止调用 TTS（语音合成）。
- 禁止真实调用 DashVector。
- 禁止运行 Chroma ingestion（Chroma 入库）。
- 禁止调用 external API（外部接口）。
- 禁止启动 runtime（运行时）或 service（服务）。
- 禁止读取真实媒体。
- 禁止修改 `.env*` 或 `GPT数据源/**`。
- 禁止把 dry run（干跑）写成真实产出完成。
- 禁止把 preflight（执行前检查）写成内容验证推进。
- 禁止使用 `git add .`。

## missing_for_real_production（不能直接产出的缺失项）

如果下一步要真正开始产出视频，还缺：

- `target_or_topic（目标或选题）`: 这条正式运营视频到底做什么。
- `locked_copy_or_copy_draft（锁定文案或文案草稿）`: Codex 不能自行定稿或改语义。
- `material_path_or_gap（素材路径或素材缺口）`: 素材路径、时间码、证据强度或明确缺口。
- `real_rag_authorization（真实 RAG 授权）`: 是否允许真实调用 DashVector 或运行 Chroma。
- `tts_api_media_authorization（TTS / API / 媒体生成授权）`: 是否允许调用 TTS、外部 API 或生成媒体。
- `card_aesthetic_boundary（卡片审美边界）`: 如需改变视觉方向，必须用户确认。
- `status_promotion_boundary（状态推进边界）`: 内容验证、可发送状态、生产可用状态都不能自动推进。

## human_confirmation_required（必须用户确认的情况）

```yaml
human_decision_gate（人工决策闸门）:
  required_for（需要人工确认的事项）:
    - real_rag_call（真实 RAG 调用）
    - external_api_call（外部 API 调用）
    - tts_call（TTS 调用）
    - media_generation（媒体生成）
    - runtime_enablement（运行时启用）
    - copy_semantic_change（文案语义修改）
    - aesthetic_direction_change（审美方向变化）
    - status_promotion（状态推进）
  auto_pass_allowed_when_required（需要人工时是否允许自动通过）: false（否）
```

用户只需要拍关键决策，不负责内部排障。Codex 负责把缺口、阻断、证据和下一步整理清楚。

## user_chatgpt_codex_next_inputs（下一步分别准备什么）

用户 / ChatGPT 需要准备：

- 真实视频任务目标或选题。
- 锁定文案或文案草稿。
- 是否允许 Codex 只做格式、断句、字幕分句和执行层处理。
- 素材路径、素材清单，或明确素材缺口。
- 是否授权真实 RAG、TTS、外部 API、媒体生成。
- 审美方向变化是否允许。

Codex 下一步可以做：

- 对真实任务跑正式 preflight（执行前检查）。
- 生成 `material_evidence_contract（素材证据契约）`。
- 生成 `copy_change_request（文案修改请求）` 或 `locked_copy_contract（锁定文案契约）` 的检查报告。
- 在授权后进入 production candidate（候选产出）或继续 blocked（阻断）。

## validation_result（验证结果）

```yaml
real_task_dry_run_preflight_probe（真实任务干跑探测）: passed（通过）
engineering_state_map_probe（工程状态地图探测）: passed（通过）
rag_default_decision_probe（RAG 默认判断探测）: passed（通过）
evaluator_failure_guardrail_probe（评估失败护栏探测）: passed（通过）
report_trace_log_validator（报告追踪日志校验）: passed（通过）
py_compile（Python 编译检查）: passed（通过；原始命令在受控提权后通过，沙盒内也用 /private/tmp pycache 前缀通过）
git_diff_check（Git 差异检查）: passed（通过）
forbidden_status_promotion_scan（禁止状态推进扫描）: passed（通过）
secret_scan（密钥扫描）: passed（通过；扫描本轮新增 / 修改片段，未发现凭证样式内容）
forbidden_path_scan（禁止路径扫描）: passed（通过；仅 6 个本轮允许文件，public 下无关未跟踪媒体未暂存）
```

已运行命令：

```text
python3 codex_source/schema_contracts/probes/real_task_dry_run_preflight_probe.py
python3 codex_source/schema_contracts/probes/engineering_state_map_probe.py
python3 codex_source/schema_contracts/probes/rag_default_decision_probe.py
python3 codex_source/schema_contracts/probes/evaluator_failure_guardrail_probe.py
python3 codex_source/schema_contracts/probes/report_trace_log_validator.py
PYTHONPYCACHEPREFIX=/private/tmp/video_factory_pycache python3 -m py_compile codex_source/schema_contracts/probes/real_task_dry_run_preflight_probe.py
python3 -m py_compile codex_source/schema_contracts/probes/real_task_dry_run_preflight_probe.py
git diff --check
```

补充检查：

- `forbidden_status_promotion_scan（禁止状态推进扫描）`: scoped scan（本轮新增 / 修改片段）通过。
- `secret_scan（密钥扫描）`: scoped scan（本轮新增 / 修改片段）通过；仓库历史 `latest.md` 中存在旧任务的 `API_KEY` 字段名记录，但本轮新增片段没有凭证样式内容。
- `forbidden_path_scan（禁止路径扫描）`: 通过；只识别到本轮 6 个允许文件，`public/reference_migration_20260601_010425/source_segment.mp4` 保持无关未跟踪状态，不会暂存。

## status_not_promoted（未推进状态）

```yaml
runtime_enabled（运行时启用）: false（未启用）
service_started（服务启动）: false（未启动）
external_api_called（外部 API 调用）: false（未调用）
tts_called（TTS 调用）: false（未调用）
dashvector_real_call（DashVector 真实调用）: false（未调用）
chroma_ingestion_run（Chroma 入库）: false（未运行）
rag_runtime_enabled（RAG 运行时启用）: false（未启用）
media_generated（媒体生成）: false（未生成）
content_validation（内容验证）: not_promoted（未推进）
send_ready（可发送状态）: false（未开启）
production_readiness（生产可用状态）: not_claimed（未声称）
```

## files_created_or_modified（新增或修改文件）

```yaml
files_created_or_modified（新增或修改文件）:
  - path（路径）: codex_source/schema_contracts/fixtures/passing/real_task_dry_run_preflight.passing.yaml
    purpose（用途）: 真实任务干跑执行前检查通过样例
  - path（路径）: codex_source/schema_contracts/fixtures/blocked/real_task_dry_run_preflight.blocked.yaml
    purpose（用途）: 真实任务干跑执行前检查阻断样例
  - path（路径）: codex_source/schema_contracts/probes/real_task_dry_run_preflight_probe.py
    purpose（用途）: 本地 YAML fixture 探测脚本
  - path（路径）: codex_log/engineering_line_audit/20260618_real_task_dry_run_preflight_report.md
    purpose（用途）: 本轮干跑报告
  - path（路径）: codex_source/schema_contracts/00_schema_contracts_index.md
    purpose（用途）: 登记新增 fixture / probe 家族
  - path（路径）: codex_log/latest.md
    purpose（用途）: 顶部更新本轮状态摘要
```

## next_safe_step（下一步安全动作）

如果用户要最快开始真实产出，下一步不是继续写策略，而是选择一个真实视频任务输入，补齐：

1. 目标 / 选题。
2. 锁定文案或文案草稿。
3. 素材路径或素材缺口。
4. 是否允许真实 RAG。
5. 是否允许 TTS / API / 媒体生成。

补齐后再进入正式 preflight（执行前检查）或 production candidate（候选产出）任务。
