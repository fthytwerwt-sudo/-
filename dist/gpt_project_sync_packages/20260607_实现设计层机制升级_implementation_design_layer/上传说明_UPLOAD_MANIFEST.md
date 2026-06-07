# GPT Project 上传说明｜20260607 实现设计层机制升级

## 1. 本包用途

本包用于把《视频工厂》GPT Project / ChatGPT -> Codex 协作机制升级到 `implementation_design_layer（实现设计层）`。

上传后，GPT Project 在把任务交给 Codex 前，默认必须先补齐：

- `target_effect（目标效果）`
- `codex_capability_boundary（Codex 能力边界）`
- `confirmed_capabilities（已确认能力）`
- `unverified_capabilities（待验证能力）`
- `preferred_execution_route（首选执行路线）`
- `fallback_routes（替代路线）`
- `capability_probe_tasks（能力探测任务）`
- `done_when（完成标准）`
- `blocked_if（阻断条件）`

## 2. 推荐上传目录

- `gpt_project_upload_package_canonical_path`:
  `/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260607_实现设计层机制升级_implementation_design_layer/`
- `upload_manifest_path`:
  `/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260607_实现设计层机制升级_implementation_design_layer/上传说明_UPLOAD_MANIFEST.md`

## 3. 上传文件清单

- `project_entry/AGENTS.md`
- `同步说明_SYNC_SUMMARY.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/00_codex_readme.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/20_reference_to_execution_contract.md`
- `codex_source/21_codex_judgment_permission_matrix.md`
- `codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md`
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/current_operation_target.md`
- `codex_log/current_data_goal_anchor.md`
- `codex_log/20260607_实现设计层机制升级_implementation_design_layer.md`
- `review_loop/operation_records_index.md`

## 4. 上传后默认行为

上传后，命中视觉、卡片、动效、声音、剪辑、自动化、数据脚本、机制修改或任何需要 Codex 落地的任务时，GPT Project 必须先输出 `implementation_design_layer（实现设计层）`，再生成 Codex prompt。

缺少实现设计层时，Codex 侧应返回 `blocked_need_implementation_design_layer` 或 `implementation_design_request（实现设计请求）`，不得凭经验猜测执行路线。

## 5. 状态边界

- 本地同步包已生成，不代表用户已上传 GPT Project UI。
- GitHub `main` 仍是当前事实源。
- 本包不包含视频、图片、音频、源素材、`dist/latest_review_pack/`、secret、API key、token、无关 `public/` 文件或大量历史日志。
- 本包不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。
- `HyperFrames` 不能仅凭最小 runtime 可用写成卡片审美能力稳定可用。
- `image2 / 图片生成能力` 不能写成已确认可用，除非未来本地真实探测通过并有证据。
