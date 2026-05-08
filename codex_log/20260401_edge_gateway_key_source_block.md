# 20260401 Edge Gateway Key Source Block

## 本轮目标

- 直接解决 `formal_api_demo` 当前 `edge_gateway_openai_compatible` 路线下的 `401 / AI Gateway API Key invalid`
- 若能在本地拿到真实有效的 AI Gateway 访问密钥与目标模型，则重跑真实 non-dry-run TTS probe
- 若仍不能成功，则把失败点继续压到最小层，并明确为什么当前无法继续推进

## 执行前已确认事实

- 当前默认优先 TTS family 是 `edge_gateway_openai_compatible`
- 当前不是字段缺失问题：
  - `auth.api_key`
  - `tts.api_route_family`
  - `tts.model`
  - `tts.voice`
  都已存在
- 上一轮真实结果已是 `failed`，不是 `blocked`
- 上一轮最小硬阻塞已经压到：
  - HTTP `401`
  - provider 返回：`AI Gateway API Key invalid`
- 当前没有真实音频文件落出，因此 assembly 不能继续推进

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

- `auth.api_key`：通过
- `tts.api_route_family`：通过
- `tts.model`：通过
- `tts.voice`：通过

## 本地来源复核结果

- 当前本地私有配置中，没有第二个可直接替换的 Edge Gateway 访问密钥候选
- 注释区没有额外真实候选值
- 当前 shell 环境中，也没有可直接回填的相关网关密钥变量
- 这说明本轮无法在“当前工作区本地已知信息”内继续替换到另一把真实网关密钥

## 实际执行

- 执行真实 non-dry-run：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

## 验证结果

- `generation_gate.status = success`
- `manifest.current_status = failed`
- `manifest.generation.status = failed`
- `manifest.generation.tts_probe.status = failed`
- `manifest.assembly.status = not_started`
- `result_summary.overall_status = failed`
- 当前没有真实音频文件落出

## 当前失败点

- 当前失败点继续稳定压缩在同一 provider 响应层：
  - route family：`edge_gateway_openai_compatible`
  - `base_url = https://ai-gateway.vei.volces.com/v1`
  - `relative_path = /audio/speech`
  - `model_identifier_source = model`
  - `voice_location = payload.voice`
  - HTTP `401`
  - provider 响应：`AI Gateway API Key invalid`
- 这说明当前问题已经不在：
  - route family 选择层
  - 字段缺失层
  - 代码 blocked / failed 分类层
- 当前最小硬阻塞是：
  - 本地没有真实有效的 AI Gateway 访问密钥来源可替换

## 当前结果

- 本轮没有改代码
- 本轮没有落出真实音频文件
- 本轮没有进入 assembly
- 当前 formal_api_demo 主线仍停在 Edge Gateway TTS 的真实远端 `401` 硬阻塞

## 下一步建议

- 下一步不应先改代码
- 先从 AI Gateway 控制台“查看密钥 / 查看代码”拿到真实有效的网关访问密钥
- 同时核对该密钥支持的真实目标模型标识
- 然后继续重跑：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 只有真实音频文件落出后，才继续推进 assembly
