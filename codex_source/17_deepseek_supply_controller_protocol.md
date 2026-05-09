# DeepSeek supply controller 协议

## 1. 文件定位

本文件定义《视频工厂》的 `DeepSeek supply controller（DeepSeek 供料中控）` 最小机制。

它负责：
- 规定 Codex 什么时候触发 DeepSeek 供料
- 规定每次供料只能做什么小动作
- 规定 DeepSeek 允许读取和禁止读取的范围
- 规定供料包如何回流给 Codex

它不负责：
- 启动后台常驻服务
- 证明 `multi-agent runtime（多 agent 运行时）` 已跑通
- 让 DeepSeek 写文件
- 让 DeepSeek 拍板项目事实
- 修改视频、声音、发布状态

## 2. trigger mechanism（触发机制）

Codex 在以下情况必须优先触发 `DeepSeek supply controller`：

1. `missing_context（缺上下文）`
   - 任务涉及多个规则文件，但 Codex 不确定该读哪些。
2. `rule_conflict（规则冲突）`
   - `latest.md（最新摘要）`、`08_当前正式事实.md（当前正式事实）`、机制文件之间说法可能冲突。
3. `stale_context_risk（旧口径污染风险）`
   - 任务可能被旧 SOP、旧 reference、旧日志带偏。
4. `large_context（上下文过大）`
   - 文件太多或太长，Codex 需要压缩包。
5. `before_write_gate（写入前依据不足）`
   - Codex 准备修改机制文件、执行规则、视频状态相关文件前，依据不足。
6. `after_read_gap（读完仍有缺口）`
   - Codex 读完首批文件后，仍不知道该信哪个文件或还缺关键文件。
7. `user_explicit_deepseek（用户明确要求 DeepSeek 参与）`
   - 用户明确说让 DeepSeek 供料、预读、补读或参与 agent 配合。

触发 controller 不等于自动通过 DeepSeek 生成；controller 必须如实记录供料来源。

## 3. action mechanism（行动机制）

DeepSeek 每次只做一个小动作，不能一次吞掉完整项目任务。

controller 当前支持 5 个 action：

1. `file_map（文件地图）`
   - 输出本轮应该读哪些文件，为什么读。
2. `risk_report（风险报告）`
   - 输出旧口径、冲突、误写、越权风险。
3. `context_summary（上下文摘要）`
   - 把已读文件压缩成 Codex 可用摘要。
4. `missing_files（缺失文件）`
   - 判断还缺哪些文件，下一轮应该补读什么。
5. `auto（自动）`
   - 只能在上述 4 个 action 中选择，不允许生成自由任务。

Codex 后续执行仍必须复核原文件；供料包只是输入，不是最终判断。

## 4. scope mechanism（范围机制）

DeepSeek / controller 只读范围默认允许：

- `AGENTS.md（仓库入口规则）`
- `codex_source/*.md（Codex 执行规则）`
- `codex_log/latest.md（最新摘要）`
- `codex_log/current_*.md（当前状态日志）`
- `GPT数据源/*.md（GPT 数据源规则包）`
- `review_loop/*.md（复盘闭环规则）`
- `scripts/*.py（脚本）`
- 用户显式指定的文本类文件

默认禁止读取：

- `.env（真实环境变量文件）`
- `.env.*（环境变量衍生文件）`
- `.env.swp（本地交换文件）`
- 密钥文件
- token 文件
- 任何二进制媒体文件
- 视频文件
- 音频文件
- 图片文件
- `dist/latest_review_pack/（最新审片包）` 中的大媒体文件
- archive-only 外部目录
- Git 内部文件
- `.git/`

DeepSeek 禁止：

- 写文件
- 改文件
- 删除文件
- commit
- push
- 修改项目事实
- 修改 `content_validation`
- 修改 `send_ready`
- 拍板最终判断

## 5. return mechanism（回流机制）

供料结果固定写入：

- `dist/deepseek_supply_controller/latest_supply_pack.md`
- `dist/deepseek_supply_controller/latest_supply_pack.json`
- `dist/deepseek_supply_controller/latest_supply_manifest.json`

输出必须包含：

- `supply_id（供料编号）`
- `task_type（任务类型）`
- `trigger_reason（触发原因）`
- `action（供料动作）`
- `supply_source（供料来源）`
  - `deepseek_passed`
  - `fallback_local_only`
  - `blocked`
- `context_pack_validation（上下文包验证）`
- `files_considered（已考虑文件）`
- `files_recommended（建议读取文件）`
- `risks（风险）`
- `missing_files（缺失文件）`
- `codex_next_input（给 Codex 的下一步输入）`
- `not_allowed（禁止事项）`

Codex 后续执行必须读取：

- `dist/deepseek_supply_controller/latest_supply_pack.md`
- 或 `dist/deepseek_supply_controller/latest_supply_pack.json`

供料结果不能只躺在日志里。

## 6. 状态表达规则

允许写：

- `DeepSeek supply controller 最小机制已落地`
- `supply_source = deepseek_passed`
- `supply_source = fallback_local_only`
- `supply_source = blocked`
- `pipeline_status = usable_with_fallback`

禁止写：

- DeepSeek 已稳定供料
- DeepSeek 已替代 Codex
- DeepSeek 已能拍板项目事实
- `fallback_local_only` 等于 DeepSeek 结论
- `multi-agent runtime` 已跑通
- 完整 agent 协作闭环已完成

## 7. supply request schema（供料请求任务卡）

controller 支持两种运行方式：

1. 旧 CLI 参数方式
   - 用于兼容测试和临时低风险任务。
2. `--request-file（供料请求文件）` 方式
   - 推荐作为后续默认方式。
   - 示例：

```bash
python3 scripts/deepseek_supply_controller.py \
  --request-file codex_source/fixtures/deepseek_supply_request_file_map_example.json
```

`supply_request（供料请求任务卡）` 是 DeepSeek 每次“知道当前任务”的唯一正式输入。

硬规则：

- DeepSeek 不靠长期记忆理解当前任务。
- DeepSeek 不靠猜测理解当前任务。
- DeepSeek 不默认读取全仓库。
- Codex / controller 必须每次显式传入任务卡。
- 任务卡必须写清当前目标、当前步骤、已知上下文、缺失上下文、候选文件、禁止路径、期望输出、停止条件和回流路径。
- request validation 失败时必须 `blocked`，并写 `latest_supply_manifest.json`。

任务卡结构说明见：

- `codex_source/18_deepseek_supply_request_schema.md`
- `codex_source/schemas/deepseek_supply_request.schema.json`

## 7A. execution observation loop（执行观察循环）

DeepSeek / fallback 参与机制升级时，默认允许至少两次供料观察：

1. 执行前：`trigger_reason = before_write_gate`
   - 用于检查旧口径、规则冲突、文件缺口、固定 SOP 化风险和 forbidden 修改风险。
2. 执行后：`trigger_reason = after_read_gap`
   - 用于复核本轮改动是否存在越权、状态误写、fallback 误写、死 SOP 化或遗漏供料来源记录。

如果 Codex 执行中发现读完首批文件后仍有缺口，也可以生成第二张或 follow-up `supply_request（供料请求任务卡）`：

- `trigger_reason = after_read_gap`
- `action = risk_report` / `missing_files` / `context_summary`
- `current_step` 必须写清是执行中补读还是执行后风险复核

每次供料必须记录：

- `supply_source（供料来源）`
- `request_validation_status（请求校验状态）`
- `fallback_status（兜底状态）`
- `not_deepseek_conclusion（是否不是 DeepSeek 结论）`
- `codex_next_input（给 Codex 的下一步输入）`

如果连续两次都是 `fallback_local_only（本地兜底）`，仍可继续低风险文档机制任务，但必须记录：

- `deepseek_generation_unstable = true`
- 本轮结论来自 Codex 原文件复核，不来自 DeepSeek 拍板
- 下轮应继续收紧 request 输入范围、上下文长度或输出约束

供料结果不能替代原文件复核。Codex 改文件前仍必须回读允许修改的原文件；改完后仍必须执行 diff、状态字段、forbidden path 和日志检查。

## 8. 一句话规则

`DeepSeek supply controller` 是 Codex 可按需触发的只读供料入口：它把缺上下文、规则冲突、旧口径风险和大上下文压缩成小型供料任务，并把结果回流到固定供料包；DeepSeek 失败时可以使用 `fallback_local_only`，但 fallback 必须明确标记为本地兜底，不得写成 DeepSeek 结论。
