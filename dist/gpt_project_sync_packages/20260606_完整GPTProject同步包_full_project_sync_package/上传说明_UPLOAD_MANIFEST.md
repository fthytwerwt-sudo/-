# GPT Project 完整资料同步包上传说明

## 1. 本包用途

本目录是《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 GPT Project 完整资料同步包，用于修复上一版同步包缺少关键入口文件的问题。

本包只用于 GPT Project 资料同步，不生成视频、不生成正式文案、不生成下一条视频执行 prompt，不推进任何动态状态。

## 2. 生成信息

- `generated_at`: `2026-06-06 20:57 CST`
- `package_source_commit`: `6d9fd8a6f2838c56d74f770456d683a80a17698b`
- `package_task`: `full_gpt_project_sync_package`
- `project_route`: `video_factory`
- `project_identity`: `OPC 一人公司 AI 闭环验证系统`
- `project_phase`: `formal_operation_active`

## 3. 用户上传目录

请直接上传整个目录：

`/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_完整GPTProject同步包_full_project_sync_package/`

不要只上传散文件。上传后，GPT Project UI 是否完成同步仍需用户在 UI 侧确认；本包只证明本地可上传目录已生成。

## 4. 上一版包缺口审计

上一版同步包：

`/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/`

审计结果：

- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`: missing
- `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`: missing
- `codex_log/latest.md`: present
- `codex_log/current_local_artifact_paths.md`: present

本轮新包已补齐 `GPT数据源/00-15` 全套入口文件，并保留 `latest`、路径索引、当前运营入口、当前数据目标锚点和运营记录索引。

## 5. 本包文件清单

### project_entry

- `project_entry/AGENTS.md`

### GPT数据源

- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/02_术语定义与状态边界.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/09_目标态计划.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
- `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`

### codex_log

- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/current_operation_target.md`
- `codex_log/current_data_goal_anchor.md`
- `codex_log/20260606_完整GPTProject同步包_full_project_sync_package.md`

### review_loop

- `review_loop/operation_records_index.md`

### codex_source

- `codex_source/00_codex_readme.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/20_reference_to_execution_contract.md`
- `codex_source/21_codex_judgment_permission_matrix.md`

## 6. 完整性检查结果

- `GPT数据源/00-15`: passed
- `GPT数据源/06`: passed
- `GPT数据源/15`: passed
- `codex_log/latest.md`: passed
- `codex_log/current_local_artifact_paths.md`: passed
- `codex_log/current_operation_target.md`: passed
- `codex_log/current_data_goal_anchor.md`: passed
- `review_loop/operation_records_index.md`: passed
- `上传说明_UPLOAD_MANIFEST.md`: passed

## 7. 不包含内容

本包不包含：

- `.env`
- API key / token / secret
- 视频、音频、图片、源素材、大型媒体文件
- `public/`
- `dist/latest_review_pack/`
- `review_loop/records/`
- `review_loop/screenshots/`

## 8. 状态边界

- 本包生成不代表用户已上传 GPT Project UI。
- 本包生成不代表 GPT Project UI 已同步成功。
- GitHub `main` 仍是当前主事实源。
- 本包不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。
