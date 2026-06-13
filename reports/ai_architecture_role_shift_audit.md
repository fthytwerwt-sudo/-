# AI Architecture Role Shift Audit（AI 执行架构换位审计）

## 1. audit status

- `audit_date`: `2026-06-13`
- `project_route`: `video_factory`
- `task_type`: `review_diagnosis_audit + mechanism_or_route_fix + project_file_change`
- `large_task_gate`: `triggered`
- `deepseek_participation`: `fallback_local_only`
- `not_deepseek_conclusion`: `true`
- `external_api_called`: `false`
- `secrets_read_or_printed`: `false`

## 2. scanned scope

已扫描：

- `AGENTS.md`
- `GPT数据源/00/01/03/06/08/10/11/12/13/14`
- `codex_source/00/13/16/17/18/19/20`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_log/latest.md`
- `codex_log/vector_rag_router_design/`
- `scripts/deepseek_*`
- `scripts/DeepSeek*`
- `scripts/vector_sync/`
- `scripts/probe_dashscope_embedding_dimension.py`
- `config/`

本轮未读取 `.env*`，未调用 DeepSeek / 阿里 / OpenAI API。

## 3. current layer inventory

| layer | current evidence | status |
|---|---|---|
| 资料层 | `GPT数据源/`、`codex_source/`、`codex_log/`、`review_loop/` | `已确认` |
| 切块层 | `scripts/vector_sync/向量同步空跑_vector_sync_dry_run.py`、20260611 chunk policy | `部分成立` |
| 向量化层 | `scripts/probe_dashscope_embedding_dimension.py`、`text-embedding-v4` 1024 记录 | `部分成立` |
| 向量库 / 索引层 | DashVector `video_factory_docs_test` 最小链路报告 | `部分成立` |
| 检索层 | 20260613 5 query retrieval readback report | `部分成立` |
| LLM 推理层 | DeepSeek scripts、Qwen/阿里/TTS 相关脚本、GPT 规则 | `已确认` |
| Codex 执行层 | `codex_source/`、scripts、tests、preflight suites | `已确认` |
| 验收 / 测试层 | `tests/`、preflight scripts、readback reports | `已确认` |
| 状态记录层 | `codex_log/latest.md`、`current_data_goal_anchor.md`、本轮 `CURRENT_STATUS.md` | `已确认` |

## 4. findings

### 4.1 responsibilities are partially misplaced

`部分成立`：项目已经有 20260611 的正确 RAG / DeepSeek 边界策略，明确 RAG 负责项目内检索、DeepSeek 负责外部深供料和风险复核。

审计前正式入口仍保留旧口径：

- `AGENTS.md` 要求每轮默认创建 supply_request 并尝试 DeepSeek。
- `GPT数据源/01` 写了 DeepSeek deep file supply mode 是默认升级口径。
- `codex_source/17/18` 写了 mandatory deepseek loop 和 deep_file_prefetch。
- 审计前 `project_source/20` 写了 DeepSeek 不是可选项，而是每轮默认只读供料层。

本轮已把当前正式入口改为 RAG-first 供料仲裁；历史日志和旧 fixtures 中的旧表述只按历史证据理解，不作为当前默认执行口径。

### 4.2 RAG exists, but is not yet the default execution layer

`部分成立`：

- 20260613 已记录 minimal ingestion `chunks_written=261`。
- retrieval readback 已通过，且包含 `chunk id / source_file_path / content_hash / readback`。
- `scripts/vector_sync` 仍强调 dry-run 与安全边界。

`待验证`：

- 正式入口是否已经默认先走 RAG retrieval manifest。
- 是否已有 chunk metadata validator。
- 是否已有 retrieval quality fixtures。
- 是否把 DeepSeek 从每轮默认资料供料降为 RAG fallback / risk review。

### 4.3 prompt stuffing risk remains

`已确认`：DeepSeek deep file supply 机制允许把相关文件内容、exact snippet、dependency map 传给模型。虽然有大小上限与禁止路径，但它仍容易复用“把一堆上下文塞给模型”的旧模式。

### 4.4 Codex responsibility is mostly clear but overloaded

`部分成立`：Codex 执行层、验证、日志、Git 边界很清楚；但当前规则还让 Codex同时承担路由、DeepSeek 供料、原文件复核、RAG 设计、执行和状态同步，容易过重。新链路应让 RAG 先承担资料召回，DeepSeek 只在冲突/风险处补位。

## 5. correct role split

| role | responsibility |
|---|---|
| 用户 | 方向、业务判断、最终验收 |
| GPT | 目标拆解、阶段规划、Codex 下发单、结果复盘 |
| Codex | 代码/文档执行、测试、报告落库、状态维护 |
| DeepSeek | 推理、总结、改写、判断、复盘、风险二次意见 |
| embedding | 资料向量化 |
| vector database | 存储 chunk、metadata、source、版本、召回结果 |
| RAG | 根据任务召回资料并输出证据路径 |
| Qwen / 主 LLM | 基于召回内容生成、分析、执行文本任务 |
| 人工兜底 | 检索不准、模型冲突、验收失败时介入 |

## 6. recommended execution chain

```text
资料进入
-> 清洗
-> 切块
-> metadata 标注
-> embedding
-> 写入向量库
-> 任务触发
-> RAG 召回
-> LLM 判断 / 生成
-> Codex 执行
-> 测试验证
-> 报告落库
-> CURRENT_STATUS.md / codex_log/latest.md 更新
-> 用户验收
```

失败降级：

- RAG 召回为空：扩大检索或进入 DeepSeek risk/reasoning。
- RAG 召回冲突：Router 仲裁，未裁决则 blocked。
- DeepSeek 不可用：`fallback_local_only / not_deepseek_conclusion=true`。
- Codex 无法回读原文件：blocked。
- 测试失败：继续修或 blocked，不写 completed。

## 7. files modified

本轮新增：

- `docs/AI_ROLE_MAP.md`
- `docs/RAG_EXECUTION_ARCHITECTURE.md`
- `docs/DEEPSEEK_POSITIONING.md`
- `docs/VECTOR_RETRIEVAL_PLAN.md`
- `docs/CODEX_EXECUTION_RULES.md`
- `reports/ai_architecture_role_shift_audit.md`
- `CURRENT_STATUS.md`
- `codex_log/supply_requests/20260613_ai_architecture_role_shift_audit_pre_supply_request.json`

本轮最小补丁：

- `AGENTS.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`
- `codex_source/17_deepseek_supply_controller_protocol.md`
- `codex_source/18_deepseek_supply_request_schema.md`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_log/latest.md`

## 8. risks

- `待验证` RAG runtime 是否已接入所有 Codex 任务。
- `待验证` 最小入库集是否覆盖真实执行所需资料。
- `待验证` DeepSeek 相关脚本仍保留读取文本 context 的能力，需后续按 RAG-first 模式加 healthcheck。
- `部分成立` 现有文档已开始纠偏，但历史 `codex_log/` 和旧 GPT Project 上传包仍会保留旧表述，后续只能降权，不建议批量改历史。

## 9. next Codex Goal

建议下一个目标：

`建立 RAG-first execution healthcheck（RAG 优先执行健康检查）`：输入一个任务 query，输出 retrieval manifest、readback proof、source arbitration、DeepSeek trigger decision，并验证 DeepSeek 只在 RAG 不足/冲突/风险复核时触发。

不建议现在做：

- 直接全仓入库。
- 直接改 DeepSeek controller 运行逻辑。
- 直接接新 provider 或真实 API。
- 批量重写历史日志。
