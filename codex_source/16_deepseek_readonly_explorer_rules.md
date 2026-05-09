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
- `DEEPSEEK_MODEL=deepseek-v4-flash`
- `DEEPSEEK_ESCALATION_MODEL=deepseek-v4-pro`

模型分工：

- `deepseek-v4-flash` 是默认供料模型，用于常规只读供料：
  - `file_map（文件地图）`
  - `missing_files（缺失文件）`
  - `context_summary（上下文摘要）`
  - 普通 `risk_report（风险报告）`
- `deepseek-v4-pro` 保留为升级模型 / 复杂任务备用模型，用于：
  - 多文件口径冲突
  - 复杂机制判断
  - 长任务审计
  - 多轮供料包合并
  - Flash 多次失败或 fallback 过多
  - Codex 明确标记 `after_read_gap（读完仍有缺口）` 且 fallback 不足

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
- 真实任务必须先控制输入体量；不得默认整文件直塞。
- 默认输入压缩边界：
  - `MAX_CHARS_PER_CONTEXT_FILE = 6000`
  - `MAX_TOTAL_CONTEXT_CHARS = 18000`
- 多文件 / 长文件真实任务默认先走输入裁剪，再走 DeepSeek 调用。
- 脚本必须检查四个顶层 key：
  - `prefetch_context_pack`
  - `must_read_file_map`
  - `risk_and_conflict_report`
  - `candidate_summary`
- JSON Output 返回成功，不等于业务 schema 验证通过。
- 顶层必须是 object。
- 四个顶层 key 的值必须是 object 或 array，不允许是空字符串。
- `must_read_file_map` 在文件型任务里必须能列出文件。
- `candidate_summary` 必须给出 `summary`。
- 缺任一 key，必须写：`context_pack_validation = failed_unexpected_output`。
- 只有四个 key 都存在，才允许写：`context_pack_validation = passed`。
- `timeout`、`empty_content`、`finish_reason = length`、`json_parse_error`、`missing_required_keys`、`schema_validation_failed` 必须进入受控重试。
- 默认最多重试 `3` 次，且每次都要继续缩小输入与输出体量。
- 三次失败后，必须生成 `local fallback（本地兜底资料包）`。
- fallback 只能给 Codex 最小资料，不等于 DeepSeek 结论。
- 切换默认模型到 `deepseek-v4-flash` 不代表 DeepSeek 已稳定供料，也不代表 fallback 问题已彻底解决。
- 只有 DeepSeek 真正输出有效四字段，才允许写 `deepseek_generation_status = passed` 或 `passed_with_retries`。
- 若 DeepSeek 失败但 fallback 成功，必须写：
  - `deepseek_generation_status = failed`
  - `context_pack_validation = fallback_local_only`
  - `fallback_status = used`

不得写：

- `DeepSeek 已进入生产执行`
- `多 agent runtime 已跑通`
- `DeepSeek 已具备写入权限`
- `context_pack_validation = passed` 等于项目事实已验证
- `fallback_local_only` 等于 DeepSeek 已稳定供料

## 5. 一句话规则

**DeepSeek 在《视频工厂》里默认只做只读供料层，默认供料模型为 `deepseek-v4-flash`，`deepseek-v4-pro` 保留为复杂任务升级模型；真实任务要先控输入体量，再做 JSON Output、schema 校验和受控重试，三次失败后回退到 local fallback；即使 `context_pack_validation = passed`，也只证明 readonly explorer 上下文包结构通过，不证明多 agent runtime 已跑通。**

## 6. 与 supply controller 的关系

`已确认` `scripts/deepseek_readonly_explorer.py（DeepSeek 只读探索器脚本）` 是底层单次只读供料器。

`已确认` `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）` 是上层中控入口，负责：

- 判断 `trigger_reason（触发原因）`
- 选择 `action（供料动作）`
- 检查只读路径范围
- 调用 readonly explorer 生成单次上下文包
- 把结果回流到 `dist/deepseek_supply_controller/`
- 写出 `latest_supply_manifest.json（最新供料清单）`

边界：

- explorer 只负责生成单次 `prefetch_context_pack（预读取上下文包）`。
- controller 只负责中控、转换、清单和回流，不负责修改业务规则文件。
- 若 explorer 输出 `fallback_local_only（本地兜底）`，controller 也必须写 `supply_source = fallback_local_only`，不得写成 `deepseek_passed`。
- controller 通过不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
