# 20260515｜目标驱动数据飞轮、阈值、文案执行闭环与 GPT Project 静态包同步

## 1. 本轮类型

- `已确认` 本轮是《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制修补 + 项目文件修改 + 字段与函数落地 + GPT Project 静态包同步。
- `已确认` 本轮不是视频成片任务，不生成视频、不生成音频、不生成图片、不 mux、不重做 `full.mp4`、不修当前候选片、不推进发布状态。

## 2. 已新增 / 补强机制

- `已新增` `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`。
- `已写入` `goal_driven_data_flywheel_spec_v1（目标驱动数据飞轮规格 V1）`。
- `已写入` `threshold_config_v1（阈值配置 V1）`。
- `已写入` `lead_score_model（客资评分模型）`。
- `已写入` `data_goal_copy_revision_gate（数据目标驱动文案修改闸门）`。
- `已写入` `content_structure_feedback_engine（内容结构反馈引擎）`。
- `已写入` `single_primary_variable_rule（单主变量规则）`。
- `已写入` `next_video_execution_prompt（下一条视频执行 prompt）` 动态生成机制。
- `已写入` `data_flywheel_memory（数据飞轮记忆）`。

## 3. 已新增阈值

- `single_video_play_thresholds（单条视频播放阈值）`：`< 1000` 触达不及格，`1000-3000` 基础观察，`3000-8000` 正向信号，`8000+` 小爆观察但需先排除泛流量。
- `retention_thresholds（留存阈值）`：3 秒、5 秒、平均观看时长分别对应开头、承接、中段证据 / 结构短板。
- `value_signal_thresholds（价值信号阈值）`：收藏率 `< 1% / 1%-2% / > 2%`，点赞率 `< 2% / 2%-5% / > 5%`，有效评论 `0-2 / 3-5 / > 5`。
- `lead_signal_thresholds（客资信号阈值）`：`lead_score >= 3` 为有效客资，`>= 4` 为高价值客资，`= 5` 为可转化客资；30 天信号分为 fail / baseline / strong / excellent。
- `stage_thresholds（阶段阈值）`：`day_0_30`、`day_31_90`、`day_90_180` 分别写入阶段目标、pass_line、excellent_line、fail_line。
- `metric_decision_rules（指标裁决规则）`：覆盖低播放 + 弱 3 秒留存、小流量高收藏、高播放低价值信号、收藏低、有效客资为 0、高价值客资出现、可转化客资出现等场景。

## 4. 已新增 / 更新字段

- `video_goal_card（视频目标卡）`
- `post_publish_review_card（发布后复盘卡）`
- `data_flywheel_memory（数据飞轮记忆）`
- `content_structure_feedback_card（内容结构反馈卡）`
- `next_video_structure_plan（下一条视频结构计划）`
- `lead_score_model（客资评分模型）`
- `threshold_config_v1（阈值配置 V1）`
- `copy_revision_strategy（文案修改策略）`
- `next_video_execution_prompt（下一条视频执行 prompt）`

## 5. 已新增阻断条件

- `missing_threshold_config_v1`
- `missing_video_goal_card`
- `missing_post_publish_review_card_when_claiming_data_driven`
- `missing_main_bottleneck`
- `missing_primary_variable`
- `too_many_variables_without_major_revision`
- `missing_next_video_execution_prompt`
- `missing_content_structure_feedback_card_when_using_data_to_change_structure`
- `more_than_four_variables_claimed_as_single_variable_experiment`
- `single_high_play_claimed_as_direction_validated`
- `single_high_lead_claimed_as_business_model_validated`
- `threshold_config_written_as_industry_truth`
- `static_gpt_project_package_written_as_live_fact_source`

## 6. 已同步入口和执行规则

- `已同步` GPT Project / ChatGPT 侧入口：`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`。
- `已同步` Codex 执行侧入口：`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`。
- `已同步` 当前事实 / 目标态：`GPT数据源/08_当前正式事实.md`、`GPT数据源/09_目标态计划.md`。

## 7. fixture cases

- `已更新` `codex_source/fixtures/mechanism_inference_function_cases.json`。
- `已新增` 9 个目标飞轮相关 case：
  - `threshold_config_missing_blocked_case`
  - `play_under_1000_opening_or_topic_fail_case`
  - `play_1000_3000_save_rate_strong_case`
  - `play_8000_no_value_signal_case`
  - `copy_revision_without_data_blocked_case`
  - `content_structure_feedback_bridge_drop_case`
  - `single_primary_variable_three_total_ok_case`
  - `too_many_variables_major_revision_case`
  - `too_many_variables_blocked_case`
- `验证` JSON parse 已通过；当前 fixture 总数为 `27`。

## 8. GPT Project 静态上传包

- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_flywheel_bridge_thresholds/`。
- `已生成` 上传说明：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_flywheel_bridge_thresholds/上传说明_UPLOAD_MANIFEST.md`。
- `已更新` `codex_log/current_local_artifact_paths.md` 中的 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）`、manifest 路径、验证时间、包含文件和边界。

## 9. 未做事项与禁止状态检查

- `未生成` 视频、音频、图片、字幕、时间线或媒体产物。
- `未修改` `dist/latest_review_pack/`。
- `未读取` `.env`、`.env.swp`、API key、token、secret。
- `未调用` DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未推进` `content_validation（内容验证）`。
- `未推进` `send_ready（可发送状态）`。
- `未推进` `publish_status（发布状态）`。
- `未推进` `voice_validation（声音验证）`。
- `未推进` `final_voice_validated（最终声音验证）`。
- `未推进` `visual_master_locked（视觉母版锁定）`。

## 10. 状态边界

- `已确认` 机制已写入，阈值已写入，字段已定义，阻断条件已写入，fixture 已补充，GPT Project 静态上传包已生成。
- `待验证` 目标驱动数据飞轮真实效果仍待验证。
- `待验证` 阈值仍是阶段工作假设，不是行业定论，也尚未被真实样本验证。
- `待验证` 下一条真实新片是否能在文案修改前正确读取目标、阈值和数据。
- `待验证` ChatGPT 是否能根据阈值和数据正确诊断主短板。
- `待验证` Codex 是否能按 `next_video_execution_prompt（下一条视频执行 prompt）` 执行剪辑。
- `待验证` 发布后数据是否能验证该机制有效。

## 11. 下一个目标

下一条真实新片进入正式文案修改前，ChatGPT 必须先读取目标、阈值、上一条 / 同类视频数据、复盘结论、主短板和变量计划；改稿后必须生成 `next_video_execution_prompt（下一条视频执行 prompt）`，Codex 才能进入执行。
