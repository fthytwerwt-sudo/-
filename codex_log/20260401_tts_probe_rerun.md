# 20260401 TTS Probe Rerun

## 本轮目标

- 使用本地已存在的 `config/formal_api_demo.local.toml`
- 重跑一次真实 non-dry-run TTS probe
- 明确正式版骨架里的 TTS 当前到底是 `success`、`blocked` 还是 `failed`

## 执行前已确认事实

- formal 骨架里的 TTS probe 路径已经接好
- generation gate 已能判断 `planned / blocked / failed / success`
- 上一轮没有真实成功，是因为 local 文件当时还是空模板
- 本轮用户说明 local 文件已填好，因此需要用真实 local 配置直接重跑
- 当前边界仍然只围绕 TTS，不扩到视觉、组装和整条正式视频链路

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`（仅本地读取，不回显真实值）
- `tests/test_formal_api_demo_pipeline.py`
- `codex_log/latest.md`
- `codex_log/20260401_tts_integration_probe.md`

## 实际执行

- 先做本地配置最小字段校验，只看“键是否存在、值是否为空”，不回显任何真实内容
- 结果确认：
  - `provider.name`、`provider.region`、`tts.style` 有值
  - `auth.api_key` 当前为空
  - `tts.model` 当前为空
  - `tts.endpoint_id` 当前为空
  - `tts.voice` 当前为空
- 在此基础上执行一次真实 non-dry-run probe：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

## 验证结果

- 真实 non-dry-run probe 已执行
- 当前真实结果：`blocked`
- blocked 原因：
  - `api_key`
  - `tts_model_or_endpoint`
  - `tts_voice`
- 结果文件已更新：
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/generation_gate.json`
  - `dist/formal_api_demo/result_summary.json`
- 当前状态一致：
  - `manifest.current_status = blocked`
  - `manifest.generation.status = blocked`
  - `manifest.generation.tts_probe.status = blocked`
  - `result_summary.overall_status = blocked`
- 本轮没有真实音频文件落出
- 额外回归：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：通过，`Ran 9 tests`

## 当前结果

- 这次 rerun 已经明确证明：
  - 当前 formal 骨架的 TTS probe 入口能真实执行
  - 但当前本地私有配置最小字段并未填齐，所以真实状态是 `blocked`
- 本轮不能写成：
  - TTS 已接通成功
  - 正式版整条视频链路已跑通

## 下一步建议

- 下一步只需要补 3 个最小真实前提：
  - `auth.api_key`
  - `tts.endpoint_id` 或 `tts.model`
  - `tts.voice`
- 这 3 个字段补齐后，再重跑一次 non-dry-run TTS probe
- 只有当真实音频落出后，才能把结论推进为“正式版骨架的 TTS 已接通”；即便如此，也仍不能写成“整条正式视频链路已跑通”
