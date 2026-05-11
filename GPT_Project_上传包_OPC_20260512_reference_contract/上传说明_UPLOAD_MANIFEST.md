# GPT Project 上传说明 UPLOAD_MANIFEST

## 1. 本包定位

本目录是《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 GPT Project 静态上传包。

包路径：

```text
/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_reference_contract/
```

本包用于把 GitHub / 本地 `main` 当前机制同步给 GPT Project，不是实时事实库。

## 2. 事实源边界

- `GitHub main` / 本地 `main` 仓库文件仍是主事实源。
- 本包只是 GPT Project 静态资料包。
- 本包包含 `Project State Action Router（项目状态动作总控器）`。
- 本包包含 `Reference-to-Execution Contract（参考到执行落地契约）`。
- 本包不代表 GPT Project UI 已上传成功。
- 本包不代表 GPT Project UI 已同步成功。
- 本包不代表内容验证通过。
- 本包不代表 `send_ready = true`。
- 本包不代表声音、视觉母版或发布复盘已最终通过。

## 3. 本包包含文件

| file | purpose |
| --- | --- |
| `00_项目总述.md` | 项目总述 |
| `01_项目系统提示词.md` | GPT Project 系统提示词 |
| `02_术语定义与状态边界.md` | 术语与状态边界 |
| `03_总索引与阅读顺序.md` | 读取顺序与索引 |
| `04_选题与文案规则.md` | 选题与文案规则 |
| `05_文案路由规则.md` | 文案路由规则 |
| `06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | 当前主线锚点 |
| `07_AI知识类视频价值规则.md` | AI 知识类视频价值规则 |
| `08_当前正式事实.md` | 当前正式事实 |
| `09_目标态计划.md` | 目标态计划 |
| `10_OPC一人公司闭环与多AI协作机制.md` | OPC 上位机制与多 AI 协作 |
| `11_项目状态动作总控器_机制推理层.md` | Project State Action Router |
| `12_参考到执行落地契约_reference_to_execution_contract.md` | Reference-to-Execution Contract |
| `latest.md` | 最新 Codex 日志摘要 |
| `20260512_参考到执行落地契约落地.md` | 本轮 dated log |
| `current_local_artifact_paths.md` | 当前本地产物路径索引 |
| `20_codex_multi_agent_routing_note_for_gpt_project.md` | GPT Project 短路由说明 |
| `上传说明_UPLOAD_MANIFEST.md` | 本上传说明 |

## 4. 上传后代表什么

上传本包后，GPT Project 可以读到以下当前机制：

1. `Project State Action Router（项目状态动作总控器）`
2. `Completion Relay Gate（补全接力闸门）`
3. `Reference-to-Execution Contract（参考到执行落地契约）`
4. `DeepSeek（只读供料层 / Explorer）` 与 `Codex（唯一写入执行层 / Integrator）` 的边界
5. GPT Project 上传包路径必须由 Codex 本地索引确认的规则

## 5. 上传后仍不代表什么

上传本包仍不代表：

- 用户已经在 GPT Project UI 完成上传。
- GPT Project UI 已经重新索引成功。
- v3.1 灰度测试完成。
- 当前视频内容验证通过。
- 任何视频、图片、音频、时间线、字幕产物已被修改。
- DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API 已被调用。
- reference 机制已经在后续真实视频任务里长期稳定验证。

## 6. 推荐上传方式

用户上传 GPT Project 时，只使用本目录：

```text
/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_reference_contract/
```

旧上传包只作历史包，不作为本轮推荐上传目录。
