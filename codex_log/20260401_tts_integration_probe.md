# 20260401 TTS Integration Probe

## 本轮目标

- 只接正式版骨架里的 TTS
- 把方舟 API Key + 已开通的豆包语音合成模型入口接进 generation pipeline
- 让正式版骨架第一次具备真实 TTS probe 能力
- 若真实前提不足，明确 blocked，不假装 success

## 执行前已确认事实

- 当前仓库已落正式版最小骨架，但还未通过“接 API 前验收”
- 当前已确认跑通的真实链路仍是本地 demo，不是正式版云端链路
- 用户说明当前已有方舟 API Key 和“豆包语音合成模型 2.0”开通状态
- 但仓库里原本不存在 `config/formal_api_demo.local.toml`
- 本轮边界明确：
  - 只接 TTS
  - 不接视觉
  - 不接云端组装
  - 不接 `space_name / template_id`

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `codex_log/latest.md`
- `config/formal_api_demo.local.toml` 检查结果：不存在

## 实际改动

- `formal_api_demo_core.py`
  - generation pipeline 从“泛 generation 骨架”收窄为“TTS probe 主路径”
  - generation_gate 改为围绕 `api_key / tts model-or-endpoint / voice / region` 判断
  - 新增真实 TTS probe 执行逻辑
  - 新增 TTS probe 结果写回 manifest / result_summary
  - 将 blocked / failed / success 清楚区分
- `scripts/generate_formal_api_demo.py`
  - 文案改为当前阶段只接 TTS probe
- `tests/test_formal_api_demo_pipeline.py`
  - 补齐缺 API Key blocked
  - 缺 model / endpoint blocked
  - TTS probe failed
  - TTS probe success
- `config/formal_api_demo.example.toml`
  - 最小补充 `auth.api_key`
  - 最小补充 `tts.endpoint_id`
  - 最小补充 `tts.response_format`
- `config/formal_api_demo.local.toml`
  - 本地新建，仅作为私有配置模板
  - 已加中文注释
  - 不进入 git

## 实际执行

- 检查本地是否已有 `config/formal_api_demo.local.toml`
- 发现不存在后，本地新建 local 配置模板
- 优先将 generation 前提从 `access_key_id / secret_access_key / space_name` 收缩为当前 TTS 真正需要的最小项
- 基于方舟兼容调用路径实现 TTS probe 入口
- 用单测覆盖 blocked / failed / success 路径
- 用当前 local 模板执行一次非 dry-run probe，验证 blocked 是否真实成立

## 验证结果

- 测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：通过，`Ran 9 tests`
- dry-run：
  - `python3 scripts/generate_formal_api_demo.py --dry-run --out /tmp/formal_api_demo_tts_dry_run`
  - 结果：`planned`
  - 当前最少缺失项：`api_key`、`tts_model_or_endpoint`、`tts_voice`
- 非 dry-run：
  - `python3 scripts/generate_formal_api_demo.py --out /tmp/formal_api_demo_tts_probe`
  - 结果：`blocked`
  - blocked 原因：`缺少 TTS probe 前提：api_key、tts_model_or_endpoint、tts_voice`
- 当前没有真实音频产物，因为 local 配置仍是空模板，未填真实值

## 当前结果

- 正式版骨架现在已经具备“真实 TTS probe 能力”
- 但本轮没有把 TTS 写成已接通成功，因为当前本地私有配置还没填入真实值
- 当前真实状态是：
  - TTS probe 代码路径已就位
  - TTS gate 已就位
  - 测试已通过
  - 实际执行结果为 blocked

## 下一步建议

- 下一轮优先在本地 `config/formal_api_demo.local.toml` 中填入：
  - `auth.api_key`
  - `tts.endpoint_id` 或 `tts.model`
  - `tts.voice`
- 填完后重新运行一次非 dry-run TTS probe
- 只有当真实音频成功落出后，才能写“正式版骨架的 TTS 调用已接通”；即使如此，也仍不能写成“整条正式视频链路已跑通”
