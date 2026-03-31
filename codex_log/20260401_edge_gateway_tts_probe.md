# 20260401 Edge Gateway TTS Probe

## 本轮目标

- 默认先试 `edge_gateway_openai_compatible` 这条 TTS 正式入口
- 用本地私有配置执行一次真实 non-dry-run TTS probe
- 把结果压实到 `success / failed / blocked`
- 不把 TTS 子线结果夸大成整条正式视频链路已跑通

## 执行前已确认事实

- formal_api_demo 骨架已完成 TTS route family split
- 当前显式支持：
  - `ark_openai_compatible`
  - `edge_gateway_openai_compatible`
  - `doubao_openspeech_v3`
- Ark 更适合作为 404 对照路径
- Doubao OpenSpeech 当前仍是 gate-only，这轮不切去跑它

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260401_tts_route_fix.md`
- `codex_log/20260401_tts_route_family_split.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- 本地 `config/formal_api_demo.local.toml`（只做本地读取，不回显真实值）

## 本地最小字段复核结果

- `auth.api_key`：通过
- `tts.api_route_family`：初始为 Ark，已本地切到 Edge Gateway
- `tts.model`：未通过
- `tts.voice`：通过

## 实际执行

- 本地仅修改：
  - `config/formal_api_demo.local.toml`
  - 新增 `tts.api_route_family = "edge_gateway_openai_compatible"`
- 真实执行：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 状态核对：
  - `generation_gate.status`
  - `manifest.current_status`
  - `manifest.generation.status`
  - `manifest.generation.tts_probe.status`
  - `result_summary.overall_status`

## 验证结果

- 本轮真实 non-dry-run 结果：`blocked`
- 当前唯一缺失项：`tts_model`
- 三份结果文件状态一致：
  - `generation_gate.status = blocked`
  - `manifest.current_status = blocked`
  - `manifest.generation.status = blocked`
  - `manifest.generation.tts_probe.status = blocked`
  - `result_summary.overall_status = blocked`
- 当前 `api_route_family` 已确认进入 `edge_gateway_openai_compatible`
- 当前没有落出真实音频文件

## 当前结果

- 这轮已经把 Edge Gateway probe 的阻塞点压缩到最小层：
  - 不是 API Key 层
  - 不是 voice 层
  - 不是路由 404 层
  - 而是 `tts.model` 仍未就位
- 当前只能写：
  - Edge Gateway TTS probe 已真实执行，结果为 `blocked`
- 当前不能写：
  - TTS 子线已接通成功
  - 正式版整条视频链路已跑通

## 下一步建议

- 下一步只需在本地 `config/formal_api_demo.local.toml` 里补上真实可用的 `tts.model`
- 然后继续跑：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 只有当真实音频文件落出时，才能把结论推进为“formal 骨架中的 TTS probe 已接通”
