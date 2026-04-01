# 20260401 Formal API Demo Aliyun TTS Success

## 本轮目标

- 在本地 `config/formal_api_demo.local.toml` 已填入阿里百炼 API Key 的前提下
- 不再让用户手动挑模型和音色
- 直接按当前项目最稳默认值补齐本地 TTS 配置并重跑真实 generation
- 只验证阿里 TTS，不推进 assembly，不推进视频生成

## 执行前已确认事实

- 当前 formal_api_demo 已具备阿里百炼 TTS provider：
  - `aliyun_bailian_cosyvoice`
- 上一轮真实失败已压缩在阿里远端认证层 `401 InvalidApiKey`
- 当前仓库 working tree 中仍存在用户未提交的 `project_source/*` 变更，本轮不得碰这些文件
- 当前本轮目标只包括：
  - 本地 TTS 默认值补齐
  - 真实 non-dry-run
  - 结果核对
  - 日志落仓库

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260401_formal_api_demo_aliyun_tts_switch.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- 本地 `config/formal_api_demo.local.toml`（只读检查，不回显真实值）

## 实际改动

- 修改了本地 `config/formal_api_demo.local.toml` 的以下字段：
  - `provider.name = aliyun_bailian`
  - `provider.region = cn-beijing`
  - `tts.api_route_family = aliyun_bailian_cosyvoice`
  - `tts.model = cosyvoice-v3-flash`
  - `tts.voice = longanyang`
- 更新了：
  - `codex_log/latest.md`
- 新增了：
  - `codex_log/20260401_formal_api_demo_aliyun_tts_success.md`

## 实际执行

- 本地字段复核：
  - `provider.name` 匹配默认值
  - `provider.region` 匹配默认值
  - `tts.api_route_family` 匹配默认值
  - `tts.model` 匹配默认值
  - `tts.voice` 匹配默认值
- 真实执行命令：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 结果核对：
  - `dist/formal_api_demo/generation_gate.json`
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/result_summary.json`

## 当前结果

- 当前真实 TTS 已成功接通：
  - `generation_gate.status = success`
  - `manifest.current_status = success`
  - `manifest.generation.tts_probe.status = success`
  - `result_summary.overall_status = success`
- 当前已落出真实音频文件：
  - `dist/formal_api_demo/tts/voice_probe.mp3`
- 当前 request_debug 已确认：
  - `api_route_family = aliyun_bailian_cosyvoice`
  - `provider = aliyun_bailian`
  - `base_url = https://dashscope.aliyuncs.com/api/v1`
  - `relative_path = /services/audio/tts/SpeechSynthesizer`
  - `model_identifier_source = model`

## 下一步建议

- 先试听 `dist/formal_api_demo/tts/voice_probe.mp3`，判断当前默认音色是否达到正式版复审入口水位。
- 在试听和质量复审前，不要先推进 assembly。
- 后续若继续 formal_api_demo 主线，应把“阿里 TTS 已接通”作为已确认事实，但不要扩写成整条正式视频链路已跑通。
