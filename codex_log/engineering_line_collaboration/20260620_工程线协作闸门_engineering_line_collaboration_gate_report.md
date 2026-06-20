# 20260620｜工程线协作闸门升级与 GPT Project 资料同步包报告

## 1. task_result（任务结果）

```yaml
task_result（任务结果）:
  status（状态）: package_generated_validation_passed_git_synced（同步包已生成、验证通过且 Git 提交推送和远端回读已完成）
  project_route（项目路由）: video_factory（视频工厂）
  task_type（任务类型）:
    - mechanism_repair（机制修补）
    - collaboration_mechanism_upgrade（协作机制升级）
    - GPT_Project_sync_package_generation（GPT Project 资料同步包生成）
    - no_media_generation（不生成媒体）
    - no_external_api_call（不调用外部 API）
  workflow_route_decision（工作流归位判断）: mechanism_repair_flow（机制修补流）
  no_media_generation（不生成媒体）: true（是）
  no_external_api_call（不调用外部 API）: true（是）
```

## 2. route_decision（路由判断）

```yaml
route_decision（路由判断）:
  project_route（项目路由）: video_factory（视频工厂）
  task_type（任务类型）:
    - mechanism_or_route_fix（机制修补 / 路由修补）
    - project_file_change（项目文件修改）
    - local_file_governance（本地文件治理 / 同步包生成）
    - GPT_Project_sync_package_generation（GPT Project 资料同步包生成）
  responsibility_layer（责任层级）:
    - project_judgment_layer（项目判断层）
    - mechanism_fix_layer（机制修补层）
    - execution_layer（执行落地层）
    - validation_layer（验收复审层）
    - sync_layer（同步回写层）
  large_task_gate（大任务闸门）:
    triggered（是否触发）: true（是）
    lane_recommendation（车道建议）: audit_lane_then_standard_lane（先审计后标准执行）
    parallel_recommendation（并发建议）: serial_only（串行执行）
    reason（理由）: 核心机制文件、Codex 执行入口、日志和同步包由同一整合者写入，避免并发写冲突。
  supply_source_arbitration（供料来源裁决）:
    retrieval_manifest（检索清单）: local_repo_readback_only（仅仓库原文件回读）
    source_readback_status（事实源回读状态）: read_ok（已读取）
    deepseek_trigger_decision（DeepSeek 触发判断）: false（否）
    not_deepseek_conclusion（是否不是 DeepSeek 结论）: true（是）
    reason（理由）: 用户本轮禁止外部 API；仓库原文件足够，无 DeepSeek 条件触发。
```

## 3. state_action_router（项目状态动作总控器）

```yaml
state_action_router（项目状态动作总控器）:
  input_signal（输入信号）:
    - 用户确认长期协作原则从 prompt stuffing（把规则塞进提示词）升级为 engineering_line_collaboration（工程线协作）
    - 需要生成 GPT Project 资料同步包
  current_project_state（当前项目状态）:
    - formal_operation_active（正式运营中）
    - mechanism_repair_needed（需要机制修补）
    - gpt_project_sync_needed（需要 GPT Project 同步）
  inferred_state（推断状态）:
    - engineering_line_collaboration_gate_needed（需要工程线协作闸门）
    - engineering_depth_router_required（需要工程深度路由器）
    - per_file_detail_plan_required（需要单文件细节方案）
    - execution_budget_gate_required（需要执行预算闸门）
    - collaboration_effectiveness_check_required（需要协作有效性检查）
    - GPT_Project_sync_needed（需要 GPT Project 静态包同步）
  selected_action（选择动作）:
    - 新增 `GPT数据源/16_工程线协作闸门_engineering_line_collaboration_gate.md`
    - 更新 `GPT数据源/03_总索引与阅读顺序.md`
    - 更新 `GPT数据源/11_项目状态动作总控器_机制推理层.md`
    - 更新 `codex_source/00_codex_readme.md`
    - 更新 `codex_source/01_execution_rules.md`
    - 更新 `codex_source/19_project_state_action_router.md`
    - 生成 GPT Project 资料同步包
  done_when（完成标准）:
    - 工程深度路由器、决策权矩阵、单文件细节方案闸门、执行预算闸门、协作有效性检查已写入并被入口引用
    - 同步包包含上传说明、清单、路径索引、变更摘要和本轮更新报告
    - 验证通过
    - path-limited commit / push / remote HEAD readback 完成
  blocked_if（阻断条件）:
    - 关键必读文件缺失
    - 同步包无上传说明
    - 验证失败且无法修复
    - secret scan 失败
    - push 或 remote HEAD readback 失败
```

## 4. mechanism_update_summary（机制更新摘要）

```yaml
mechanism_update_summary（机制更新摘要）:
  engineering_depth_router（工程深度路由器）: added（已加入）
  decision_authority_matrix（决策权矩阵）: added（已加入）
  per_file_detail_plan_gate（单文件细节方案闸门）: added（已加入）
  execution_budget_gate（执行预算闸门）: added（已加入）
  collaboration_effectiveness_check（协作有效性检查）: added（已加入）
  engineering_worth_question（值不值得工程化）: added（已加入）
```

## 5. per_file_detail_plan（单文件细节方案）

| file（文件） | purpose（用途） | layer（所属层级） | inputs（输入） | outputs（输出） | validation（验证方式） | user_review_points（用户复审点） |
| --- | --- | --- | --- | --- | --- | --- |
| `GPT数据源/16_工程线协作闸门_engineering_line_collaboration_gate.md` | 承载完整工程线协作闸门 | 目标 / 状态 / 节点 / 工具 / 评估 / 失败路由 / 记录 | 用户本轮锁定锚点、既有工程线审计口径 | 13 层、五问法、第六问、L0-L3、权限矩阵、预算闸门、协作检查 | 关键词和结构字段检查 | L0-L3 是否符合“简单任务保持简单” |
| `GPT数据源/03_总索引与阅读顺序.md` | 把 16 号机制纳入默认读取和触发词 | 资料召回 / 状态记录 | 现有索引、16 号文件 | 新读取顺序和触发词 | 索引引用检查 | 新入口是否会过度增加日常任务负担 |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | 把工程线协作纳入 state_action_router | 状态 / 路由 / 失败路由 | 现有状态表、16 号机制 | 新 state、动作规则、blocked_if | 总控器引用检查 | 需要人工兜底的判断是否保留 |
| `codex_source/19_project_state_action_router.md` | 给 Codex 执行层新增状态动作策略 | 执行节点 / 失败路由 | 11 号总控器、16 号机制 | `engineering_line_collaboration_gate_needed`、`per_file_detail_plan_required`、`engineering_overdesign_risk` | Codex 入口引用检查 | Codex 是否先判深度再动文件 |
| `codex_source/00_codex_readme.md` | 更新 Codex 总入口接手规则 | 执行入口 / 人工兜底 | 16 号机制、现有 readme | 工程线协作闸门入口 | 关键词检查 | 用户/ChatGPT/Codex 权限是否清楚 |
| `codex_source/01_execution_rules.md` | 更新完成标准 | 评估 / 完成真实性 | 16 号机制、现有完成闸门 | L2 / L3 completed 禁止条件 | 完成字段检查 | L3 缺契约/评估/失败路由/trace 时是否禁止完成 |
| `AGENTS.md` | 仓库入口引用工程线闸门 | 入口路由 | 现有多项目入口规则 | 《视频工厂》命中后的补读规则 | 路由引用检查 | 是否未改仓库身份 / 分流事实 |
| `codex_log/current_local_artifact_paths.md` | 更新 GPT Project 同步包规范路径 | 状态记录 / 路径索引 | 旧 canonical path、生成包路径 | 新同步包 canonical path 和边界 | 路径存在检查 | 同步包生成是否不等于 UI 上传 |
| `codex_log/latest.md` | 记录本轮机制升级和状态边界 | 状态记录 | 本轮 diff、验证结果 | latest 顶部摘要 | latest 关键词检查 | 未推进内容 / 发送 / 发布 / 生产状态 |

## 6. gpt_project_sync_package（GPT Project 资料同步包）

```yaml
gpt_project_sync_package（GPT Project 资料同步包）:
  package_path（同步包路径）: /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260620_工程线协作闸门_engineering_line_collaboration_gate/
  upload_manifest（上传说明）: /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260620_工程线协作闸门_engineering_line_collaboration_gate/上传说明_UPLOAD_MANIFEST.md
  canonical_path_status（规范路径状态）: updated_this_round_from_existing_rule（按既有规范路径规则本轮更新）
  status_boundary（状态边界）:
    - 只表示本地同步包已生成
    - 不表示用户已上传 GPT Project UI
    - 不表示 GPT Project 已更新成功
    - 不表示 GitHub main 之外的静态包高于仓库事实
```

## 7. status_boundary（状态边界）

```yaml
status_boundary（状态边界）:
  media_generated（媒体生成）: false（未生成）
  audio_generated（音频生成）: false（未生成）
  tts_called（TTS 调用）: false（未调用）
  external_api_called（外部 API 调用）: false（未调用）
  deepseek_called（DeepSeek 调用）: false（未调用）
  dashvector_called（DashVector 调用）: false（未调用）
  content_validation（内容验证）: not_promoted（未推进）
  send_ready（可发送状态）: false（未开启）
  publish_status（发布状态）: not_promoted（未推进）
  voice_validation（声音验证）: not_promoted（未推进）
  final_voice_validated（最终声音验证）: false（未通过）
  visual_master_locked（视觉母版锁定）: false（未锁定）
  production_readiness（生产可用状态）: not_claimed（未声称）
  long_term_mechanism_stability（长期机制稳定性）: pending_real_task_validation（待真实任务验证）
```

## 8. validation_plan（验证计划）

```yaml
validation_result（验证结果）:
  markdown_structure_check（Markdown 结构检查）: passed_basic_structure_check（基础结构检查通过；本地未安装 markdownlint）
  chinese_annotation_check（中文备注检查）: passed（通过，新增英文 key / status 已配中文解释）
  index_reference_check（索引引用检查）: passed（通过，03 总索引已引用 16 号机制）
  controller_reference_check（总控器引用检查）: passed（通过，11 总控器已引用工程线协作状态）
  codex_entry_reference_check（Codex 入口引用检查）: passed（通过，00 / 01 / 19 已引用）
  sync_package_check（同步包检查）: passed（通过，上传说明 / 清单 / 路径索引 / 变更摘要存在）
  latest_boundary_check（latest 边界检查）: passed（通过，未推进内容 / 发送 / 发布 / 生产状态）
  media_exclusion_check（媒体排除检查）: passed（通过，同步包不含视频 / 音频 / 图片 / zip）
  secret_scan（密钥扫描）: passed_staged_diff_scan（通过，staged diff 扫描通过）
```

## 9. next_safe_step（下一步安全动作）

```yaml
next_safe_step（下一步安全动作）:
  before_completion（完成前）:
    - 生成同步包清单和上传说明
    - 更新 current_local_artifact_paths.md
    - 更新 latest.md
    - 运行验证和 secret scan
    - path-limited stage / commit / push / remote HEAD readback
  user_review_points（用户复审点）:
    - L0 / L1 / L2 / L3 分档是否符合你的协作习惯
    - 用户 / ChatGPT / Codex 权限边界是否正确
    - “值不值得工程化”是否能防止过度工程化
```
