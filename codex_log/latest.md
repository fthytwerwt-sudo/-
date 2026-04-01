# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续默认走功能分支，不直接改 `main`。
- 当前项目仍处于“正式版目标态搭建阶段”：
  - `formal_api_demo` 的 generation 当前仍只收敛到 TTS probe
  - 本轮没有推进视频生成，也没有推进 assembly
  - 当前不能把正式版整条云端视频链路写成已跑通
- 当前阿里百炼 TTS 路线已接通：
  - `provider.name = aliyun_bailian`
  - `tts.api_route_family = aliyun_bailian_cosyvoice`
  - 当前默认模型为 `cosyvoice-v3-flash`
  - 当前默认音色为 `longanyang`

## 最近一次完成了什么

- 已只读检查本地 `config/formal_api_demo.local.toml`，并把本地 TTS 字段补齐到当前项目最稳默认值：
  - `provider.name`
  - `provider.region`
  - `tts.api_route_family`
  - `tts.model`
  - `tts.voice`
- 已执行真实 non-dry-run：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 当前已确认结果：
  - `generation_gate.status = success`
  - `manifest.current_status = success`
  - `manifest.generation.tts_probe.status = success`
  - `result_summary.overall_status = success`
- 当前已落出真实音频文件：
  - `dist/formal_api_demo/tts/voice_probe.mp3`
- 当前 request_debug 已证明阿里路径真实生效：
  - `api_route_family = aliyun_bailian_cosyvoice`
  - `provider = aliyun_bailian`
  - `base_url = https://dashscope.aliyuncs.com/api/v1`
  - `relative_path = /services/audio/tts/SpeechSynthesizer`
  - `model_identifier_source = model`
- 当前结论必须收紧为：
  - 仅能写“阿里 TTS 已接通并落出真实音频”
  - 不能写“正式版整条视频链路已跑通”

## 当前最关键的下一步

- 先试听 `dist/formal_api_demo/tts/voice_probe.mp3`，确认当前默认音色是否达到正式版复审入口水位。
- 在未进入人工试听前，不要先推进 assembly，也不要扩到视频生成。
- 若后续继续推进，只应在“当前 TTS 已接通”基础上进入音质复审和下一阶段素材链路。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- 若继续接 formal_api_demo 的阿里 TTS：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/generation_gate.json`
  - `dist/formal_api_demo/result_summary.json`
