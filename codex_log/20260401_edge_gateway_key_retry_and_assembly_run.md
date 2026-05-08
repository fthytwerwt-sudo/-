# 20260401 Edge Gateway Key Retry And Assembly Run

## 本轮目标

- 用当前本地私有配置再次重跑 `edge_gateway_openai_compatible` 的真实 non-dry-run TTS probe
- 若 TTS 成功则立即推进 assembly
- 若 TTS 仍失败，则把失败点继续压到最小层后收口

## 执行前已确认事实

- 当前默认优先 TTS family 是 `edge_gateway_openai_compatible`
- 上一轮 TTS 结果已是 `failed`，不是 `blocked`
- 当前最小硬阻塞曾压到：
  - HTTP `401`
  - 远端错误：`AI Gateway API Key invalid`
- 上一轮没有真实音频文件落出，因此 assembly 未执行是合理停止

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260401_edge_gateway_tts_and_assembly_run.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- 本地 `config/formal_api_demo.local.toml`
- `dist/formal_api_demo/manifest.json`
- `dist/formal_api_demo/generation_gate.json`
- `dist/formal_api_demo/result_summary.json`

## 本地最小字段复核结果

### TTS 阶段

- `auth.api_key`：通过
- `tts.api_route_family`：通过
- `tts.model`：通过
- `tts.voice`：通过

### Assembly 阶段

- 本轮未进入真实 assembly 执行前提复核
- 原因：TTS 未成功，没有可用音频资产进入组装

## TTS 阶段实际执行

- 执行：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 状态核对：
  - `generation_gate.status = success`
  - `manifest.current_status = failed`
  - `manifest.generation.status = failed`
  - `manifest.generation.tts_probe.status = failed`
  - `result_summary.overall_status = failed`

## TTS 阶段结果

- 本轮 TTS 结果：`failed`
- 当前没有落出真实音频文件
- 当前失败点继续稳定压缩在最小层：
  - route family：`edge_gateway_openai_compatible`
  - `base_url = https://ai-gateway.vei.volces.com/v1`
  - `relative_path = /audio/speech`
  - `model_identifier_source = model`
  - `voice_location = payload.voice`
  - HTTP `401`
  - provider 响应层明示：AI Gateway API Key invalid

## Assembly 阶段实际执行

- 本轮未执行真实 assembly
- 原因：
  - TTS 未成功
  - 当前没有可用音频文件
  - 若继续强行执行，只会命中 `generation_assets_not_ready`

## Assembly 阶段结果

- `未执行`

## 当前结果

- 本轮已经再次用当前本地配置把 TTS 推到不能再前推的位置
- 当前最小硬阻塞仍然不是代码 bug，而是：
  - Edge Gateway 访问密钥有效性层
- 在这一步未解决前，不应继续推进 assembly

## 下一步建议

- 下一步不建议继续改代码
- 先把本地 `auth.api_key` 换成真实有效的 AI Gateway 访问密钥
- 然后继续重跑：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 只有真实音频文件落出后，才进入 assembly 的真实执行
