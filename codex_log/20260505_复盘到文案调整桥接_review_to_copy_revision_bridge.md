# 20260505 复盘到文案调整桥接 review to copy revision bridge

## route_decision（路由判断）

- project_route（项目路由）：video_factory（视频工厂）
- task_type（任务类型）：mechanism_or_route_fix（机制修补 / 路由修补） + review_diagnosis_audit（复盘 / 诊断 / 审核） + copywriting（文案写作 / 改写） + project_file_change（项目文件修改）
- responsibility_layer（责任层级）：mechanism_fix_layer（机制修补层） + validation_layer（验收复审层） + sync_layer（同步回写层）
- large_task_gate（大任务闸门）：triggered（已触发）
- large_task_gate.reason（触发原因）：本轮写入 / 检查超过 3 个仓库文件，同时涉及规则文件、入口文件、V002 记录、日志与 Git 同步。
- lane_recommendation：standard_lane（标准执行车道）
- lane_reason：目标、允许范围和禁止范围已锁定，但仍需要多文件写入、日志回写、禁止项核验与 push。
- lane_invalid_if：读到的 V002 事实与 latest 冲突；或继续需要修改禁止范围。
- parallel_recommendation：serial_only（串行执行）
- parallel_reason：多个目标文件属于同一复盘闭环入口，写入需要单点整合。
- write_owner：Codex 主执行者。
- integration_owner：Codex 主执行者。
- execution_permission（执行许可）：allowed（允许执行）

## read_status（读取状态）

| file（文件） | status（状态） | purpose（用途） |
| --- | --- | --- |
| `AGENTS.md` | read_ok（已读取） | 仓库入口、route_decision 与禁止范围规则 |
| `codex_source/00_codex_readme.md` | read_ok（已读取） | Codex 执行层总入口 |
| `codex_log/latest.md` | read_ok（已读取） | 当前摘要与 V002 / 风险检查口径 |
| `review_loop/00_review_loop_readme.md` | read_ok（已读取） | 发布后复盘执行层总说明 |
| `review_loop/04_diagnosis_template.md` | read_ok（已读取） | 诊断层输出边界 |
| `review_loop/05_dual_review_handoff_template.md` | read_ok（已读取） | Codex 初检与 ChatGPT 拍板分工 |
| `review_loop/06_next_round_task_template.md` | read_ok（已读取） | 现有下轮执行单模板边界 |
| `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md` | read_ok（已读取） | V002 平台风险检查与发布许可规则 |
| `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_发布后复盘记录_post_publish_review_record.md` | read_ok（已读取） | V002 原始复盘事实 |
| `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_给ChatGPT复盘输入_chatgpt_review_input.md` | read_ok（已读取） | 给 ChatGPT 的 V002 复盘边界 |
| `GPT数据源/04_选题与文案规则.md` | read_ok（已读取） | 选题与文案前置边界 |
| `GPT数据源/05_文案路由规则.md` | read_ok（已读取） | 文案交付包与 block / segment 承载规则 |
| `GPT数据源/07_AI知识类视频价值规则.md` | read_ok（已读取） | AI 知识类视频价值与真实证据要求 |
| `project_source/14_content_review_and_loop_governance_rules.md` | read_ok（已读取） | 内容复盘治理、异常样本和循环规则 |
| `codex_source/13_execution_lane_and_parallel_rules.md` | read_ok（已读取） | large_task_gate 后的 lane / parallel 规则 |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | read_ok（已读取） | GPT Project 侧多执行器路由说明 |

## gap_audit（闭环缺口审计）

- current_loop_gap（当前闭环缺口）：复盘结论没有稳定转成文案结构改版包。
- missing_between_review_and_revision（复盘到改版之间缺失什么）：缺少样本判断、问题层判断、文案结构状态、修订目标、安全文案包、发布前检查要求和下一轮执行包之间的桥接文件。
- why_existing_templates_are_not_enough（为什么现有模板不够）：`review_loop/06_next_round_task_template.md（下轮视频执行单草稿模板）` 只负责“下一轮只改一个变量”，不足以承接标题、开头、block、segment 承载、录屏要求、风险词替换、结尾动作和发布前风险检查。
- target_fix_scope（本轮修复范围）：只补复盘到文案结构改版的桥接层，不生成视频，不写最终正式脚本，不修改 V002 原始数据，不修改当前发布状态。

## created_files（新建文件）

- `review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md`
- `review_loop/10_文案结构改版包模板_copy_revision_package_template.md`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_复盘到文案调整桥接_review_to_copy_revision_bridge.md`
- `codex_log/20260505_复盘到文案调整桥接_review_to_copy_revision_bridge.md`

## updated_files（修改文件）

- `review_loop/00_review_loop_readme.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`

## V002_bridge_summary（V002 桥接摘要）

- sample_decision = reference_abnormal_sample（可参考异常样本）
- main_problem_layer = platform_risk + publish_packaging（平台风险 + 发布包装）
- secondary_problem_layer = copy_structure + footage_carrier（文案结构 + 录屏承载）
- copy_structure_status = not_locked（文案结构未锁定）
- revision_target = publish_packaging_and_copy_structure（发布包装 + 文案结构）
- V002b 当前状态：draft_pending_chatgpt_user_confirmation（草案，待 ChatGPT / 用户确认）

## forbidden_changes_check（禁止项检查）

- `dist/latest_review_pack/`：未修改。
- 当前 v3.1 视频产物：未修改。
- `codex_log/current_publish_target.md`：未修改。
- `content_validation（内容验证）`：未修改。
- `send_ready（可发送状态）`：未修改。
- `GPT 数据源/`：未修改。
- `GPT数据源/`：未修改。
- V002 原始数据字段：未修改；仅在新桥接记录中引用 39 播放、5 点赞、8 收藏。
- `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`：未修改。
- V002 已有记录文件：未删除、未移动、未重命名。

## commit_and_push_status（提交与同步状态）

- commit_status：pending_before_git_step（本日志随本轮提交进入 Git）
- push_status：pending_before_git_step（最终 push 状态以本轮最终回报为准）
- target_branch：codex/user-readable-map（默认主读取分支）

## next_target（下一个目标）

V002b 进入 ChatGPT / 用户确认状态：先确认安全版文案结构是否采用，再决定是否进入录制 / 剪辑 / 发布前风险检查；当前不生成视频、不写最终正式脚本。
