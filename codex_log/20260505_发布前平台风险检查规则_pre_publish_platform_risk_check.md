# 20260505 发布前平台风险检查规则 pre publish platform risk check

## route_decision（路由判断）

- project_route（项目路由）：video_factory（视频工厂）
- task_type（任务类型）：mechanism_or_route_fix（机制修补 / 路由修补） + data_review_loop（数据记录 / 灰度复盘） + project_file_change（项目文件修改）
- responsibility_layer（责任层级）：mechanism_fix_layer（机制修补层） + validation_layer（验收复审层） + sync_layer（同步回写层）
- large_task_gate（大任务闸门）：triggered
- large_task_gate.reason：本轮读取 / 检查超过 3 个仓库文件，并新增规则、补入口引用、写日志、更新 latest、commit / push。
- lane_recommendation：standard_lane
- lane_reason：目标和边界已锁定，但需要正常读取、机制落地、入口回写、验证和 Git 同步。
- lane_invalid_if：V002 记录缺失、需要修改禁止范围、需要把 V002 改写成内容成败结论。
- parallel_recommendation：serial_only
- parallel_reason：写入范围集中在规则文件、入口文件和日志，单点整合可避免机制重复或入口混乱。
- parallel_invalid_if：写入范围扩大到 `dist/latest_review_pack/`、`current_publish_target`、`GPT数据源/`、`GPT 数据源/` 或 V002 原始数据字段。
- write_owner：Codex 当前执行器
- read_only_lanes：none
- integration_owner：Codex 当前执行器
- execution_permission：allowed_after_read_check（读取确认后允许执行）

## read_status（读取状态）

| file（文件） | read_status（读取状态） | purpose（用途） |
| --- | --- | --- |
| `AGENTS.md` | read_ok | 仓库入口规则、路由闸门、禁止项 |
| `codex_source/00_codex_readme.md` | read_ok | Codex 执行层总入口、发布前触发引用位置 |
| `codex_log/latest.md` | read_ok | 当前最新摘要与 V002 / v3.1 状态边界 |
| `codex_log/20260505_抖音减少推荐审核记录_douyin_reduce_recommendation_notice.md` | read_ok | V002 执行日志与样本解释 |
| `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_发布后复盘记录_post_publish_review_record.md` | read_ok | V002 发布后复盘记录 |
| `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_给ChatGPT复盘输入_chatgpt_review_input.md` | read_ok | V002 给 ChatGPT 的复盘输入 |
| `review_loop/00_review_loop_readme.md` | read_ok | review_loop 入口引用位置 |
| `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md` | read_ok | 截图 / 数据记录边界，确认本轮不是再次录入数据 |
| `review_loop/06_next_round_task_template.md` | read_ok | 下一轮草稿边界，确认本轮只补防再犯机制 |
| `codex_source/01_execution_rules.md` | read_ok | 执行规则、route_decision、机制修补必读映射 |
| `codex_source/13_execution_lane_and_parallel_rules.md` | read_ok | large_task_gate 后的 lane / parallel 判断 |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | read_ok | large_task_gate 后的并发路由说明 |

## V002_record_check（V002 记录复核）

- `已确认` V002 记录存在。
- `已确认` V002 标记为 `policy_distribution_limited（平台审核减推 / 分发受限）`。
- `已确认` V002 标记为 `abnormal_distribution_sample（异常分发样本）`。
- `已确认` V002 标记为 `policy_limited_but_interest_signal_strong（平台减推污染样本，但兴趣信号强）`。
- `已确认` V002 未混入 V001。
- `已确认` V002 不作为正常自然流量样本。
- `已确认` 本轮未修改 V002 原始数据字段：播放量 39、点赞 5、收藏 8。

## created_files（新建文件）

- `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`
- `codex_log/20260505_发布前平台风险检查规则_pre_publish_platform_risk_check.md`

## updated_files（修改文件）

- `review_loop/00_review_loop_readme.md`：追加发布前平台风险检查入口引用。
- `codex_source/00_codex_readme.md`：追加发布前检查触发读取提示。
- `codex_log/latest.md`：顶部追加本轮最小摘要。

## risk_rule_summary（风险规则摘要）

- `已确认` 新规则文件用于发布前平台风险检查，不是数据记录文件，不是内容质量最终判断文件，不替代平台规则原文。
- `已确认` 新规则要求 AI 工作流 / AI 教程 / 自动化流程 / 工具演示 / 命令行或 IDE 画面展示类视频发布前必须检查平台风险表达。
- `已确认` 必查对象包括标题、封面、字幕、画面文字、工具界面、命令行、代码注释、项目文件名、结尾动作、简介、评论区引导、私信 / 资料领取话术。
- `已确认` 风险分级包括 `hard_block`、`rewrite_required`、`caution`。
- `已确认` V002 已作为第一条发布前风险样本写入规则。

## forbidden_changes_check（禁止项检查）

- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改当前 v3.1 视频产物。
- `已确认` 未修改 `codex_log/current_publish_target.md`。
- `已确认` 未修改 `content_validation（内容验证）`。
- `已确认` 未修改 `send_ready（可发送状态）`。
- `已确认` 未修改 `GPT 数据源/`。
- `已确认` 未修改 `GPT数据源/`。
- `已确认` 未修改 V002 原始数据字段。
- `已确认` 未删除或移动 V002 记录文件。

## blocked_items（阻断项）

- none

## next_target（下一个目标）

后续发布 AI 工作流 / 自动化流程 / 工具演示类视频前，先执行 `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`，输出风险等级、命中词、命中位置、改写项、AI 标识检查和发布许可。

