# DeepSeek readonly explorer 规则

## 1. 文件定位

本文件用于定义《视频工厂》里的 `DeepSeek readonly explorer（DeepSeek 只读探索器）` 最小配置与验证边界。

它负责：

- 约束 DeepSeek 的只读角色
- 约束默认模型名与 `base_url`
- 约束最小 API 验证结果如何表述
- 约束允许输出与禁止输出

它不负责：

- 替代 `AGENTS.md`
- 替代项目正式事实
- 替代多 agent runtime
- 允许 DeepSeek 写仓库文件

## 2. 默认配置

当前默认配置：

- `DEEPSEEK_BASE_URL=https://api.deepseek.com`
- `DEEPSEEK_MODEL=deepseek-v4-pro`

硬规则：

- 不再使用旧模型名 `deepseek-chat`
- 不再使用旧模型名 `deepseek-reasoner`
- DeepSeek API key 只从本地 `.env` 读取
- 不打印真实 `DEEPSEEK_API_KEY`

## 3. 只读边界

DeepSeek 只允许输出：

- `prefetch_context_pack（预读取上下文包）`
- `must_read_file_map（必读文件地图）`
- `risk_and_conflict_report（风险与冲突报告）`
- `candidate_summary（候选摘要）`

DeepSeek 不得：

- 修改仓库文件
- 拍板项目事实
- 推进发布状态
- 推进 `content_validation`
- 推进 `send_ready`
- 推进 `publish_status`
- 推进 `voice_validation`
- 推进 `final_voice_validated`

## 4. 最小 API 验证口径

允许写：

- `DeepSeek readonly explorer API validation passed`
- `DeepSeek readonly explorer API validation blocked`
- `context_pack_validation = passed`
- `context_pack_validation = failed_unexpected_output`

结构规则：

- DeepSeek readonly explorer 默认使用 `JSON Output`。
- 请求体必须使用 `response_format={"type":"json_object"}`。
- prompt 必须明确要求 JSON，不允许 Markdown 或 JSON 外解释文字。
- 脚本必须检查四个顶层 key：
  - `prefetch_context_pack`
  - `must_read_file_map`
  - `risk_and_conflict_report`
  - `candidate_summary`
- 缺任一 key，必须写：`context_pack_validation = failed_unexpected_output`。
- 只有四个 key 都存在，才允许写：`context_pack_validation = passed`。

不得写：

- `DeepSeek 已进入生产执行`
- `多 agent runtime 已跑通`
- `DeepSeek 已具备写入权限`
- `context_pack_validation = passed` 等于项目事实已验证

## 5. 一句话规则

**DeepSeek 在《视频工厂》里默认只做只读供料层，模型默认锁为 `deepseek-v4-pro`，输出默认走 JSON Output 并校验四个顶层 key；即使 `context_pack_validation = passed`，也只证明 readonly explorer 上下文包结构通过，不证明多 agent runtime 已跑通。**
