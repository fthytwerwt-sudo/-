# 上传说明 UPLOAD MANIFEST

## generated_at

`2026-05-15 00:43 CST`

## package_path

`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_flywheel_bridge_thresholds/`

## 本包用途

本包是《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 GPT Project 静态协作包，用于把 2026-05-15 新增的目标驱动数据飞轮、阈值配置、数据目标文案修改闸门、内容结构反馈引擎、单主变量规则和 Codex 动态执行 prompt 同步给 GPT Project。

## 本包包含的新机制

- `goal_driven_data_flywheel_spec_v1（目标驱动数据飞轮规格 V1）`
- `threshold_config_v1（阈值配置 V1）`
- `lead_score_model（客资评分模型）`
- `data_goal_copy_revision_gate（数据目标驱动文案修改闸门）`
- `content_structure_feedback_engine（内容结构反馈引擎）`
- `single_primary_variable_rule（单主变量规则）`
- `next_video_execution_prompt（下一条视频执行 prompt）`
- `data_flywheel_memory（数据飞轮记忆）`

## 本包包含 threshold_config_v1（阈值配置 V1）

`已确认` 本包包含 `threshold_config_v1（阈值配置 V1）`，覆盖：

- `single_video_play_thresholds（单条视频播放阈值）`
- `retention_thresholds（留存阈值）`
- `value_signal_thresholds（价值信号阈值）`
- `lead_signal_thresholds（客资信号阈值）`
- `stage_thresholds（阶段阈值）`
- `metric_decision_rules（指标裁决规则）`

## 本包事实边界

- GitHub / 当前本地 `main` 仓库仍是主事实源。
- 本包只是 GPT Project 静态协作包，不是实时事实库。
- 本包生成不代表用户已上传 GPT Project UI。
- 本包不代表 GPT Project UI 已同步成功。
- 本包不代表内容验证通过。
- 本包不代表 `send_ready = true`。
- 本包不代表 `publish_status（发布状态）` 推进。
- 本包不代表 `voice_validation（声音验证）`、`final_voice_validated（最终声音验证）` 或 `visual_master_locked（视觉母版锁定）` 已通过。
- 本包不代表目标飞轮已真实跑通。
- 本包不代表阈值已经被真实样本验证。
- 本包内阈值全部是当前阶段工作假设，不是行业定论。
- 不得把一次播放高写成方向成立。
- 不得把一次客资高写成商业模式成立。

## 上传后建议

上传本包到 GPT Project 后，下一次 ChatGPT 修改文案前应先读取：

1. `13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
2. 当前 `video_goal_card（视频目标卡）`
3. 当前 `post_publish_review_card（发布后复盘卡）`
4. 当前 `data_flywheel_memory（数据飞轮记忆）`
5. 当前 `content_structure_feedback_card（内容结构反馈卡）`

如果缺 `threshold_config_v1（阈值配置 V1）`、`video_goal_card（视频目标卡）`、`post_publish_review_card（发布后复盘卡）`、`main_bottleneck（主短板）`、`primary_variable（主验证变量）` 或 `next_video_execution_prompt（下一条视频执行 prompt）`，不得声称“根据数据正式改文案”，也不得进入视频执行。

## 文件清单

1. `00_项目总述.md`
2. `01_项目系统提示词.md`
3. `02_术语定义与状态边界.md`
4. `03_总索引与阅读顺序.md`
5. `04_选题与文案规则.md`
6. `05_文案路由规则.md`
7. `06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
8. `07_AI知识类视频价值规则.md`
9. `08_当前正式事实.md`
10. `09_目标态计划.md`
11. `10_OPC一人公司闭环与多AI协作机制.md`
12. `11_项目状态动作总控器_机制推理层.md`
13. `12_参考到执行落地契约_reference_to_execution_contract.md`
14. `13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
15. `14_latest_最新日志.md`
16. `20260515_goal_driven_data_flywheel_copy_execution_loop_thresholds_and_gpt_project_package.md`
17. `15_codex_multi_agent_routing_note_GPT_Project短路由说明.md`
18. `16_current_local_artifact_paths_当前本地产物路径索引.md`
19. `上传说明_UPLOAD_MANIFEST.md`

## 排除项

本包不包含：

- 媒体文件
- `.env`
- API key
- token
- secret
- 大视频文件
- 用户隐私凭据
