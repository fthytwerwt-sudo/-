# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-03 本轮已完成“formal_api_demo 主线语义纠偏 / mainline realign”：
  - `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 本轮已把仓库口径拉回正式主线：
  - `generation success = 配音 API 真实成功 + 图片 / 视频 API 真实成功`
  - `visual plan / preview / skipped` 不再允许冒充 `generation success`
  - `local assembly` 被收回为“拼接真实生成素材”的职责
  - `preview` 只保留为辅助产物，不再冒充正式 assembly success

## 当前真实状态

- TTS API：
  - `success`
  - 当前已有真实请求实现与测试覆盖
- 图片 API：
  - `blocked`
  - 原因不是模型字段被取消，而是 `provider implementation` 仍未真实接入
- 视频 API：
  - `blocked`
  - 原因同上，当前仓库仍缺足够明确的 provider 实现
- local assembly：
  - `blocked`
  - 当前只能生成辅助 `preview`，正式本地素材拼接 implementation 仍未接入
- overall：
  - `blocked`

## 最近一次真正完成了什么

- 审计并分类了 formal_api_demo 当前跑偏点：
  - 描述层
  - 状态层
  - 测试层
  - 日志层
- 修正了：
  - [scripts/generate_formal_api_demo.py](/Users/fan/Documents/视频工厂/scripts/generate_formal_api_demo.py)
  - [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - [tests/test_formal_api_demo_pipeline.py](/Users/fan/Documents/视频工厂/tests/test_formal_api_demo_pipeline.py)
  - [codex_source/02_current_execution_context.md](/Users/fan/Documents/视频工厂/codex_source/02_current_execution_context.md)
  - 本日志入口
- 本轮没有继续做 preview 画面 round2，也没有继续修 `seg02` 视觉表达

## 当前最关键下一步

- 当前最高优先级已切回主线：
  - 先补图片 / 视频 API provider 的真实接口合同与实现依据
- 在这一步成立前：
  - 不要再把 `visual plan / preview` 写成 generation success
  - 不要再把“继续修 preview 画面”写成当前最高优先级

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_mainline_realign.md`
- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
