# guardrail_check｜短视频自动流 V2.1

## 1. 读取检查

| 检查项 | 状态 | 说明 |
|---|---|---|
| 是否读取项目口径文件 | `passed` | 已读取 `AGENTS.md`、`codex_source/00/01`、`GPT数据源/04/05/06/07` |
| 是否读取素材事实文件 | `passed` | 已读取 PR #41 head 中素材采集、素材清单、细节复采、流程证据 |
| 是否读取 PR #41 失败文件 | `passed` | 已读取 render、assembly、runtime adjustment、redaction、local path 等失败结果 |

## 2. runtime 检查

| 检查项 | 状态 | 说明 |
|---|---|---|
| 是否生成 runtime_script | `passed` | `runtime_script.md` 已作为实际入片口播稿设计 |
| 是否没有把完整稿当 runtime | `passed` | `reference_script.md` 仅 reference；runtime 为压缩稿 |
| runtime 是否只是完整文案照搬 | `passed` | runtime 删除长解释、长工具对比、长 API/Codex/即梦说明 |
| 是否新增素材没有证明的事实 | `passed` | 仅使用素材事实支持的流程证明 |

## 3. timeline 检查

| 检查项 | 状态 | 说明 |
|---|---|---|
| 真实录屏是否承担主体流程推进 | `passed` | 86s 真实录屏，占比 0.819 |
| 卡片是否只做辅助 | `passed` | 19s 卡片，占比 0.181，最长 4s |
| 是否避免 PR #41 长说明片结构 | `passed` | 总时长目标 105s，不使用 60-90s 卡片 |
| 是否写成工具教程 / 软件合集 | `passed` | timeline 以流程证明为主 |

## 4. 状态边界检查

| 检查项 | 状态 | 说明 |
|---|---|---|
| 是否火山 API 已脱敏或 fallback | `passed` | V2.1 默认信息卡 fallback |
| 是否没有把 technical_validation 当 content_validation | `passed` | 本轮只做计划包，不声明内容通过 |
| 是否没有写 content_validation passed | `passed` | 未写内容通过态 |
| 是否没有写 send_ready true | `passed` | 未写可发送真值 |
| 是否允许进入下一轮 render 阶段 | `blocked` | 需要 ChatGPT / 用户先审核计划包 |

## 5. blocked 原因

- `blocked_reason`：计划包尚未经过 ChatGPT / 用户审核。
- `blocked_layer`：`review_gate`
- `已完成什么`：runtime_script、timeline_plan、timeline_manifest、素材/脱敏/口径计划。
- `缺什么`：用户 / ChatGPT 对计划包的审核结论。
- `下一步要补什么`：审核通过后再下发 render 执行单。
