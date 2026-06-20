# GPT Project 上传说明｜20260620 工程线协作闸门

## 1. 本包用途

本包用于把《视频工厂》GPT Project / ChatGPT / Codex 协作机制升级到 `engineering_line_collaboration_gate（工程线协作闸门）`。

上传后，GPT Project 在复杂任务、机制修补、自动化、多节点任务或 Codex 下发前，默认先判断：

- `engineering_worth_question（值不值得工程化的入口问题）`
- `engineering_depth_router（工程深度路由器）`
- `decision_authority_matrix（决策权矩阵）`
- `per_file_detail_plan_gate（单文件细节方案闸门）`
- `execution_budget_gate（执行预算闸门）`
- `collaboration_effectiveness_check（协作有效性检查）`

## 2. 推荐上传目录

- `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）`:
  `/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260620_工程线协作闸门_engineering_line_collaboration_gate/`
- `upload_manifest_path（上传说明路径）`:
  `/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260620_工程线协作闸门_engineering_line_collaboration_gate/上传说明_UPLOAD_MANIFEST.md`

## 3. 上传方式

把本目录整体上传 / 更新到 GPT Project 资料源。

不要只上传单个新增机制文件；本包同时包含项目入口、索引、总控器、Codex 执行入口、状态边界和本轮报告，缺任一层都可能导致新聊天接手不完整。

## 4. 上传文件清单

完整清单见：

- `文件清单_FILE_MANIFEST.md`
- `路径索引_PATH_INDEX.md`
- `变更摘要_CHANGE_SUMMARY.md`

关键入口包括：

- `project_entry/AGENTS.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/16_工程线协作闸门_engineering_line_collaboration_gate.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/engineering_line_collaboration/20260620_工程线协作闸门_engineering_line_collaboration_gate_report.md`

## 5. 状态边界

- 本地同步包已生成，不代表用户已上传 GPT Project UI。
- 本地同步包已生成，不代表 GPT Project UI 已更新成功。
- GitHub `main` 仍是当前事实源。
- 本包不包含视频、图片、音频、源素材、`dist/latest_review_pack/`、secret、API key、token、无关 `public/` 文件或大量历史日志。
- 本包不调用 TTS、视频生成、图像生成、阿里、MiniMax、DashVector 或 DeepSeek API。
- 本包不推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证）`、`final_voice_validated（最终声音验证）`、`visual_master_locked（视觉母版锁定）` 或 `production_readiness（生产可用状态）`。
