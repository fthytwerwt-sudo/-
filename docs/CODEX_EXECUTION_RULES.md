# Codex Execution Rules（Codex 执行规则）

## 1. status

- `document_status`: `active_architecture_guidance`
- `created_at`: `2026-06-13`
- `project_route`: `video_factory`

## 2. Codex responsibility

Codex 的正确职责：

1. 读取仓库事实和 RAG 召回证据。
2. 回读关键原文件。
3. 修改代码、文档、schema、fixture、报告或状态文件。
4. 运行测试、lint、dry-run、secret scan。
5. 维护 `codex_log/latest.md`、`CURRENT_STATUS.md` 和审计报告。
6. path-limited stage、commit、push、remote readback。

Codex 不负责：

- 拍板用户方向。
- 替代 GPT/用户做最终业务验收。
- 把技术验证写成内容验证。
- 把 RAG 或 DeepSeek 输出当正式事实。
- 把 local-only / fallback / internal diagnostic 写成 completed。

## 3. execution chain after role shift

```text
route_decision
-> source_arbitration
-> RAG retrieval manifest if available
-> original file readback
-> optional DeepSeek risk/reasoning if RAG insufficient or conflict exists
-> child_task_graph
-> scoped file edits
-> verification
-> status/log/report update
-> git sync
```

## 4. blocked conditions

Codex 必须 blocked 或标 `待验证`：

- 项目路由不清。
- RAG 召回缺 source path / chunk id / content_hash。
- 关键原文件无法回读。
- DeepSeek 输出和仓库文件冲突且 Router 未仲裁。
- 任务需要真实 API key 才能判断。
- 修改会推进 `content_validation / send_ready / publish_status / voice_validation` 但没有用户授权。
- 只能产出技术预览或局部报告却被要求写完成。

## 5. fallback hierarchy

1. 先用仓库原文件。
2. 再用 RAG 召回和 readback。
3. RAG 不足时，用 DeepSeek 做推理/风险复核/冲突二次意见。
4. DeepSeek 不可用时，标 `fallback_local_only / not_deepseek_conclusion=true`。
5. 仍无法判断时，blocked 给 GPT/用户裁决。
