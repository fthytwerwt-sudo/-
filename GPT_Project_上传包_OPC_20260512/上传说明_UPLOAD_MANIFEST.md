# 上传说明 UPLOAD MANIFEST

## 1. 本包生成时间

- `generated_at`: `2026-05-12 02:52 CST`
- `package_path`: `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512/`

## 2. 本包用途

本包用于 GPT Project 静态资料同步，让 GPT Project 侧资料对齐 GitHub 当前 `main（主读取分支）` 已写入的《视频工厂｜OPC 一人公司 AI 闭环验证系统》机制、配合规则和项目残缺审计结果。

## 3. 本包事实边界

- GitHub 当前 `main` 仍是主事实源。
- 本包只是静态协作包，不是实时事实库。
- 本包生成只代表本地资料包已准备好，不代表用户已经上传到 GPT Project UI。
- 本包生成不代表 GPT Project UI 已同步成功。
- 本包是 GPT Project 静态上传版；包内副本已去除密钥类字面标识，不包含媒体文件或真实凭据。

## 4. 本包包含的新机制与新结果

- `Completion Relay Gate（补全接力闸门）`
- `项目残缺审计 project_gap_audit`
- 最新 `latest.md（最新日志）`
- 当前 `current_local_artifact_paths.md（当前本地产物路径索引）` 中的新上传包路径

## 5. 本包不代表

- 不代表当前视频内容已通过。
- 不代表 `send_ready（可发送状态）` 已变成 true。
- 不代表 DeepSeek 长期稳定真实供料。
- 不代表多 agent runtime 已跑通。
- 不代表 v3.1 灰度测试已完成。
- 不代表目标态计划已经变成当前正式事实。

## 6. 上传后建议

1. 用户将本目录内全部文件上传到 GPT Project。
2. 上传完成后，新聊天仍优先读取 GitHub 当前 `main` 的最新仓库文件。
3. 如果 GPT Project 侧和 GitHub `main` 冲突，以 GitHub `main` 为准，再由 Codex 重新生成上传包。

## 7. 文件清单

| 包内文件名 | 来源仓库路径 | 用途 | 是否必传 |
| --- | --- | --- | --- |
| `00_项目总述.md` | `GPT数据源/00_项目总述.md` | 项目总述、上位身份和主线定位 | 是 |
| `01_项目系统提示词.md` | `GPT数据源/01_项目系统提示词.md` | GPT Project 侧系统提示词与 GPT -> Codex 补全接力规则 | 是 |
| `02_术语定义与状态边界.md` | `GPT数据源/02_术语定义与状态边界.md` | 术语定义、状态边界和目标态 / 当前事实区分 | 是 |
| `03_总索引与阅读顺序.md` | `GPT数据源/03_总索引与阅读顺序.md` | GPT Project 资料读取顺序与旧口径降权 | 是 |
| `04_选题与文案规则.md` | `GPT数据源/04_选题与文案规则.md` | 选题和文案规则 | 是 |
| `05_文案路由规则.md` | `GPT数据源/05_文案路由规则.md` | 文案路由、执行链路和供料边界 | 是 |
| `06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | 当前四件套主线锚点 | 是 |
| `07_AI知识类视频价值规则.md` | `GPT数据源/07_AI知识类视频价值规则.md` | AI 知识类视频价值、内容验证和产品化边界 | 是 |
| `08_当前正式事实.md` | `GPT数据源/08_当前正式事实.md` | 当前正式事实，防止目标态冒充事实 | 是 |
| `09_目标态计划.md` | `GPT数据源/09_目标态计划.md` | 目标态计划，只作为未来方向 | 是 |
| `10_OPC一人公司闭环与多AI协作机制.md` | `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` | OPC 多 AI 协作机制、ChatGPT / Codex / DeepSeek / Perplexity 分工 | 是 |
| `11_latest_最新日志.md` | `codex_log/latest.md` | 最新执行日志，含 2026-05-12 上传包生成记录 | 是 |
| `12_completion_relay_gate_补全接力闸门机制修补.md` | `codex_log/20260512_补全接力闸门机制修补.md` | Completion Relay Gate 机制修补记录 | 是 |
| `13_project_gap_audit_项目残缺审计.md` | `codex_log/20260512_项目残缺审计_project_gap_audit.md` | 项目残缺审计报告，含 P0 / P1 / P2 / P3 缺口 | 是 |
| `14_codex_multi_agent_routing_note_GPT_Project短路由说明.md` | `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | GPT Project 给 Codex 下发任务时的 lane / parallel / Completion Relay 短路由说明 | 是 |
| `15_current_local_artifact_paths_当前本地产物路径索引.md` | `codex_log/current_local_artifact_paths.md` | 当前本地真实路径索引，含 20260512 新上传包路径 | 是 |

## 8. 一句话上传规则

用户上传 GPT Project 时，只上传这个目录内的文件：

`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512/`
