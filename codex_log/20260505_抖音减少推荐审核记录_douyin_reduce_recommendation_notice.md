# 20260505 抖音减少推荐审核记录 douyin reduce recommendation notice

## route_decision（路由判断）

- project_route（项目路由）：video_factory（视频工厂）
- task_type（任务类型）：data_review_loop（数据记录 / 灰度复盘） + review_diagnosis_audit（复盘 / 诊断 / 审核） + external_research_bridge（外部规则桥接） + project_file_change（项目文件局部新增 / 更新）
- responsibility_layer（责任层级）：validation_layer（验收复审层） + sync_layer（同步回写层）
- large_task_gate（大任务闸门）：triggered
- large_task_gate.reason：本轮读取 / 检查超过 3 个仓库文件，并涉及记录、截图证据目录、复盘输入、执行日志、latest 最小同步。
- lane_recommendation：standard_lane
- lane_reason：目标和边界已锁定，但需要正常读取、记录、验证、日志回写和 Git 同步。
- lane_invalid_if：发现已有同名视频记录、video_id 无法判断、需要修改禁止范围、需要把平台减推写成内容成败结论。
- parallel_recommendation：serial_only
- parallel_reason：写入对象集中在单条视频记录和日志，单点整合可避免误写 V001 或 v3.1 状态。
- parallel_invalid_if：写入范围扩大到 `dist/latest_review_pack/`、`current_publish_target`、`GPT数据源/` 或当前视频产物。
- write_owner：Codex 当前执行器
- read_only_lanes：none
- integration_owner：Codex 当前执行器
- execution_permission：allowed_after_read_check（读取确认后允许执行）

## read_status（读取状态）

| file（文件） | read_status（读取状态） | purpose（用途） |
| --- | --- | --- |
| `AGENTS.md` | read_ok | 仓库入口规则、路由闸门、单工作区规则、禁止项 |
| `codex_source/00_codex_readme.md` | read_ok | Codex 执行层入口、review_loop 读取顺序、主读取分支 |
| `codex_log/latest.md` | read_ok | 当前最新摘要与 v3.1 状态边界 |
| `review_loop/00_review_loop_readme.md` | read_ok | 发布后复盘执行层总说明 |
| `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md` | read_ok | 截图优先录入、分桶、来源状态规则 |
| `review_loop/02_video_record_template.md` | read_ok | 单条视频记录模板 |
| `review_loop/03_result_dashboard_template.md` | read_ok | 检查是否需要更新看板；本轮未新增看板，以免异常样本混入聚合判断 |
| `codex_source/13_execution_lane_and_parallel_rules.md` | read_ok | large_task_gate 后的 lane / parallel 判断 |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | read_ok | large_task_gate 后的 GPT Project 并发路由说明 |
| `codex_log/current_gray_test_target.md` | read_ok | 当前灰度目标与禁止判断 |
| `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md` | read_ok | 指标口径与 6000 播放门槛边界 |
| `project_source/14_content_review_and_loop_governance_rules.md` | read_ok | 异常样本、规律沉淀、排除样本规则 |

## impact_check（影响面检查）

- `已确认` 当前工作区：`/Users/fan/Documents/视频工厂`
- `已确认` 当前分支：`codex/user-readable-map`
- `已确认` `review_loop/records/` 下仅有 `V001_v31_AI做PPT踩坑_gray_test/`，未发现《自动流的最简单流程》既有记录。
- `已确认` `review_loop/screenshots/` 下仅有 `V001_v31_AI做PPT踩坑/`，未发现 V002 既有截图目录。
- `已确认` 当前最大 video_id 为 V001，因此本轮分配 V002。
- `已确认` 未更新 result dashboard；当前只有模板文件，且 V002 是平台减推异常样本，暂不混入聚合看板。
- `已确认` `codex_log/latest.md` 需要最小追加摘要，因为本轮结果会影响新会话默认接手判断。
- `已确认` 本轮未触碰 `current_publish_target`、`dist/latest_review_pack/`、`GPT 数据源/` 或 `GPT数据源/`。

## created_files（新建文件）

- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_视频上下文_video_context.md`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_抖音审核通知字段提取_report_douyin_notice_extract.md`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_发布后复盘记录_post_publish_review_record.md`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_给ChatGPT复盘输入_chatgpt_review_input.md`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_缺失与待人工确认_missing_and_uncertain_fields.md`
- `review_loop/screenshots/V002_自动流的最简单流程/V002_截图清单_screenshot_manifest.md`
- `codex_log/20260505_抖音减少推荐审核记录_douyin_reduce_recommendation_notice.md`

## created_dirs（新建目录）

- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/`
- `review_loop/screenshots/V002_自动流的最简单流程/`
- `review_loop/screenshots/V002_自动流的最简单流程/审核通知_policy_notice/`
- `review_loop/screenshots/V002_自动流的最简单流程/人工补充数据_manual_metrics/`

## updated_files（修改文件）

- `codex_log/latest.md`：仅顶部追加最小摘要，不改变当前 v3.1 状态。

## extracted_fields（已记录截图字段）

- video_title（视频标题）：自动流的最简单流程
- publish_time（发布时间）：2026-05-04 17:00:08
- platform（平台）：抖音
- notice_type（通知类型）：作品审核通知
- review_result（审核结果）：减少作品推荐
- violation_reason（违规原因）：引导至风险不可控渠道
- reason_surface（触发位置）：画面
- platform_reason_text（平台原因原文）：引导用户脱离平台至其他渠道交易，或引导下载/使用第三方软件，平台无法保证双方权益，易造成人身/财产安全风险。
- platform_modification_advice（平台修改建议）：为保障双方权益，请勿发布脱离平台至其他渠道交易、或引导下载/使用第三方软件的内容。
- appeal_entry（申诉入口）：截图可见“查看申诉”
- ai_label_status（AI 标识状态）：第二张截图可见“作者声明：内容由 AI 生成”
- visible_video_context（画面可识别内容）：已在 V002 审核字段提取报告中逐项记录。

## user_confirmed_metrics（用户确认数据）

- play_count（播放量）：39
- like_count（点赞数）：5
- favorite_count（收藏数）：8

## calculated_metrics（计算字段）

- like_rate（点赞率）：5 / 39 = 12.82%
- favorite_rate（收藏率）：8 / 39 = 20.51%
- like_plus_favorite_action_rate（点赞 + 收藏动作率，非去重）：13 / 39 = 33.33%

## distribution_status（分发状态标记）

- policy_distribution_limited（平台审核减推 / 分发受限）
- abnormal_distribution_sample（异常分发样本）
- policy_limited_but_interest_signal_strong（平台减推污染样本，但兴趣信号强）
- external_channel_or_third_party_software_risk（外部渠道 / 第三方软件风险）

## external_rule_check（外部规则核实）

- `已确认` 已读取国家网信办《人工智能生成合成内容标识办法》页面，确认视频生成合成内容显式标识、用户主动声明和平台标识功能相关要求。
- `已确认` 已读取抖音 AI 内容标识公告转述页，确认 AIGC 辅助创作本身不违规，发布 AI 生成视频、图像、文本、音频等内容需要主动添加标识。
- `已确认` 已读取抖音“AI 起号”专项治理转述页，确认其治理对象包括 AI 视频账号售卖教程、AI 账号秘籍传授、引导规避平台 AI 标注、转让销售 AI 虚拟账号等。
- `部分成立` 抖音社区自律公约页面可打开但本地工具未提取到正文；本轮主要采用用户提供的抖音审核通知原文记录外部渠道 / 第三方软件风险桶。

## sample_interpretation（样本解释）

- `已确认` 该视频处于平台审核减推 / 分发受限状态，播放量不能作为正常自然流量样本判断。
- `已确认` 39 播放样本太小，不能沉淀为稳定规律。
- `部分成立` 点赞率 12.82%、收藏率 20.51% 属于小样本高兴趣信号。
- `部分成立` 收藏数高于点赞数，初步说明有工具价值 / 可复用价值信号。
- `已确认` 本轮不把该条写成“内容失败”或“自然流量差”。

## forbidden_changes_check（禁止项检查）

- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改当前 v3.1 视频产物、正片、样片或复审包。
- `已确认` 未修改 `codex_log/current_publish_target.md`。
- `已确认` 未修改 `content_validation（内容验证）`。
- `已确认` 未修改 `send_ready（可发送状态）`。
- `已确认` 未修改 `GPT 数据源/`。
- `已确认` 未修改 `GPT数据源/`。
- `已确认` 未新建外部工作区、fresh clone、worktree 或临时 clone。

## blocked_items（阻断项）

- none

## next_target（下一个目标）

ChatGPT / 用户基于 V002 复盘输入判断该样本最终归为 `排除样本` 还是 `可参考异常样本`，并拍板下一轮唯一优先改点是否锁定为发布包装 / 风险表达 / 画面触发点。

