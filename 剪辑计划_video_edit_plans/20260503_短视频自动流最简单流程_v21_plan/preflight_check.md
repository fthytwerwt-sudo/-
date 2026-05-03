# preflight_check｜短视频自动流 V2.1 剪辑计划包

## 1. 任务边界

- `已确认` 本轮只落地剪辑执行计划包。
- `已确认` 本轮不生成视频、不生成音频、不生成图片、不渲染。
- `已确认` 本轮不 commit、不 push、不创建 PR。
- `已确认` PR #41 不合并、不修改远端 PR。
- `已确认` 本计划包只供 ChatGPT / 用户审核；审核通过前不得进入 render。

## 2. 必读文件读取结果

### 主读取分支文件

| 文件 | 状态 | 用途 |
|---|---|---|
| `AGENTS.md` | `found` | 仓库入口、视频工厂路由、单工作区与状态边界 |
| `codex_source/00_codex_readme.md` | `found` | Codex 执行层总入口 |
| `codex_source/01_execution_rules.md` | `found` | 执行规则、视频修改同步与 blocked 边界 |
| `GPT数据源/04_选题与文案规则.md` | `found` | 文案先贴真实素材、用户录制素材硬依据 |
| `GPT数据源/05_文案路由规则.md` | `found` | block/segment 承载、卡片不得替代真实录屏 |
| `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | `found` | API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑主线 |
| `GPT数据源/07_AI知识类视频价值规则.md` | `found` | 真实证据优先级、内容验证边界 |

### PR #41 head 文件

| 文件 | 状态 | 用途 |
|---|---|---|
| `render_report.md` | `found` | PR #41 技术通过但内容待复审、总时长 731.196s |
| `render_summary.json` | `found` | PR #41 渲染摘要 |
| `assembly_plan.md` | `found` | PR #41 卡片 60-90 秒级问题证据 |
| `assembly_manifest.json` | `found` | PR #41 卡片/录屏比例失败证据 |
| `script_runtime_adjustment_report.md` | `found` | PR #41 完整稿直接入片证据 |
| `redaction_report.md` | `found` | 火山引擎 fallback 证据 |
| `local_open_path_report.md` | `found` | 本地路径与状态边界 |
| `scripts/生成短视频自动流样片_generate_short_video_auto_flow_sample.py` | `found` | 失败生成逻辑参考，不作为 V2.1 模板 |
| `素材检查_reports/...vnext_material_intake_report.md` | `found` | 素材事实 |
| `material_inventory.json` | `found` | 素材清单 |
| `素材细节复采报告_material_detail_recapture_report.md` | `found` | 细节复采 |
| `doubao_to_trae_flow_evidence.json` | `found` | 豆包到 Trae 流程证据 |
| `chatgpt_copywriting_input.md` | `found` | 给 ChatGPT 的文案事实输入 |

## 3. PR #41 失败事实

- `已确认` PR #41 生成了 `full_video.mp4`，但不是合格短视频样片。
- `已确认` PR #41 总时长：`731.196s`。
- `已确认` PR #41 `content_validation` 仍为 `pending_user_chatgpt_review`。
- `已确认` PR #41 `send_ready` 仍为 `false`。
- `已确认` PR #41 把完整 `FINAL_SCRIPT_V2` 用作字幕与临时 TTS。
- `已确认` PR #41 多张信息卡持续 60-90 秒级，卡片承担了主叙事。
- `已确认` PR #41 真实录屏没有承担主体流程推进。

## 4. V2.1 计划状态

- `plan_status`：`review_ready_not_render_ready`
- `blocked_items`：`[]`
- `next_gate`：ChatGPT / 用户审核计划包。
