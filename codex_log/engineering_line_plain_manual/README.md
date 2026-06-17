# 工程线人话版手册 README

## 本目录用途

本目录把上一轮 `engineering_line_audit（工程线审计）` 的技术报告，翻译成用户、ChatGPT（总控脑）和 Codex（写入执行器）都能复审的人话版手册。

它解决的是“先把方案讲清楚”，不是“工程改造已经做完”。本目录不证明 `runtime（运行时）` 已启用，不证明 `service（服务）` 已启动，不证明 `RAG（检索增强生成）` 已接入正式运行链，也不证明 `production_readiness（生产可用状态）` 已成立。

## 推荐阅读顺序

1. `00_先读这个_工程线人话版总览.md`：先看现在项目到底处在哪。
2. `01_工程线人话版施工图.md`：再看工程线后续准备怎么接。
3. `02_常见场景决策手册.md`：遇到冲突、卡片、RAG（检索增强生成）、文案、素材、人工确认时按场景查。
4. `03_以后修改下发模板.md`：用户以后要改项目时，把模板复制给 ChatGPT（总控脑），再由 ChatGPT（总控脑）补成 Codex（写入执行器）执行单。
5. `05_项目总规则_用户决策版.md`：用户判断哪些事必须自己拍板、哪些事 AI（人工智能）默认处理、失败后应该回到哪一层。

`05_项目总规则_用户决策版.md` 已追加 `## 10. 当前 8 个关键决策｜已确认版`，后续工程融合任务应先读取这一节，再判断是否进入 schema（结构契约）、fixture（测试样例）、probe（探测脚本）或 runtime hardening（运行时加固）。

## 哪些文件给用户看

- `00_先读这个_工程线人话版总览.md`
- `01_工程线人话版施工图.md`
- `02_常见场景决策手册.md`
- `05_项目总规则_用户决策版.md`

这四份主要用于用户理解：现在是什么、为什么不能直接做、哪些关键事必须由用户拍板、下一步先修哪一层、遇到问题怎么停。

## 哪些文件给 ChatGPT / Codex 下发前参考

- `02_常见场景决策手册.md`
- `03_以后修改下发模板.md`
- `05_项目总规则_用户决策版.md`

ChatGPT（总控脑）后续补执行单时，应该先用项目总规则判断是否需要用户拍板，再用场景手册判断需求属于哪一层，最后用下发模板把任务边界、允许文件、禁止文件、完成标准和 `blocked（阻断）` 条件写清楚。

## 状态边界

```yaml
status_boundary（状态边界）:
  document_type（文档类型）: plain_language_manual（人话版手册）
  runtime_enabled（运行时启用）: false（未启用）
  service_started（服务启动）: false（未启动）
  rag_runtime_enabled（RAG 运行时启用）: false（未启用）
  external_api_called（外部 API 调用）: false（未调用）
  media_generated（媒体生成）: false（未生成）
  content_validation（内容验证）: not_promoted（未推进）
  send_ready（可发送状态）: false（未开启）
  production_readiness（生产可用状态）: not_claimed（未声称）
```

本目录是方案手册，不是执行完成证据。方案确认后，后续仍要按 `Task Slice（任务切片）` 一片一片执行、验证、提交、推送。

## 20260618 安全工程融合入口

本轮新增的 `engineering_state_map（工程状态地图）`、`acceptance_contract（验收契约）`、State / Node / Edge（状态 / 节点 / 边）、RAG / Tool Registry / Retriever / Vector Store（检索增强生成 / 工具注册表 / 检索器 / 向量库）、Evaluator / Failure Route / Human-in-the-loop / Guardrails（评估器 / 失败路由 / 人工介入 / 护栏）、Report / Trace / Log（报告 / 追踪 / 日志）仍属于 no-service / fixture-first（无服务 / 测试样例优先）框架。

这代表后续任务有了可验证入口，不代表 `runtime（运行时）` 已启用，不代表 `service（服务）` 已启动，不代表真实 RAG（检索增强生成）外部调用已授权，也不代表媒体生成或内容验证已推进。
