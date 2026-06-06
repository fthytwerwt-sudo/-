# 20260606 完整 GPT Project 同步包

## 任务目标

重新生成一份最新、完整、可直接整包上传到 GPT Project 的资料同步包，修复上一版包缺少关键入口文件的问题。

## 上一版包缺口审计

- `previous_package_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/`
- `missing_files`:
  - `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
  - `GPT数据源/15_对标文案学习与说人话判断标准_copy_reference_learning_and_plain_language_standard.md`
- `present_files`:
  - `codex_log/latest.md`
  - `codex_log/current_local_artifact_paths.md`

## 新包路径

- `gpt_project_upload_package_canonical_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_完整GPTProject同步包_full_project_sync_package/`
- `upload_manifest_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_完整GPTProject同步包_full_project_sync_package/上传说明_UPLOAD_MANIFEST.md`
- `package_source_commit = 6d9fd8a6f2838c56d74f770456d683a80a17698b`
- `ready_for_user_upload = true_after_manifest_and_path_verification`

## 新包文件清单

- `project_entry/AGENTS.md`
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
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`
- `codex_log/current_operation_target.md`
- `codex_log/current_data_goal_anchor.md`
- `review_loop/operation_records_index.md`
- `codex_source/00_codex_readme.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/20_reference_to_execution_contract.md`
- `codex_source/21_codex_judgment_permission_matrix.md`

## 完整性验证

- `GPT数据源/00-15 = passed`
- `required_logs_and_indexes = passed`
- `upload_manifest_exists = passed`
- `requirement_alignment_grep = passed`
- `secret_scan = passed`
- `media_exclusion_check = passed`
- `git_diff_check = passed`

## Git 状态

- `branch = main`
- `commit_sha = pending_final_report`
- `pushed = pending_final_report`
- `remote_head_verified = pending_final_report`
- `unrelated_dirty_files = public/reference_migration_20260601_010425/source_segment.mp4`

## 未推进项

- 不生成视频。
- 不生成正式文案。
- 不生成下一条视频执行 prompt。
- 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。
- 不把本地同步包生成写成用户已上传 GPT Project UI。
