# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- `formal_api_demo` 目前仍只推进到 TTS 子线：
  - 阿里百炼 TTS 已接通
  - 本轮新增了“声音目标稿 v1”的最小可执行桥接
  - 本轮没有推进视频生成，也没有推进 assembly
- 当前阿里默认技术路线保持为：
  - `provider.name = aliyun_bailian`
  - `tts.api_route_family = aliyun_bailian_cosyvoice`
  - `tts.model = cosyvoice-v3-flash`
  - `tts.voice = longanyang`

## 最近一次完成了什么

- 已确认此前阿里 TTS 真实音频链路可用的基础上，补上了阿里 CosyVoice 的风格参数桥接：
  - `tts.instruction`
  - `tts.speech_rate`
  - `tts.pitch_rate`
  - `tts.volume`
- 已把固定风格测试文案和 A/B/C 三版参数落入可维护位置：
  - `config/formal_api_demo.example.toml`
  - `formal_api_demo_core.py`
- 已新增三版风格对照执行入口：
  - `run_aliyun_tts_style_probe_variants(...)`
- 已执行真实阿里三版风格音频生成，结果为：
  - `overall_status = success`
  - `style_draft_in_request = true`
  - `recommended_variant_id = A`
- 当前已落出真实音频文件：
  - `dist/formal_api_demo/tts/voice_probe_A.mp3`
  - `dist/formal_api_demo/tts/voice_probe_B.mp3`
  - `dist/formal_api_demo/tts/voice_probe_C.mp3`
- 当前 summary 文件：
  - `dist/formal_api_demo/tts_style_probe_variants.json`

## 当前结论边界

- 现在可以明确写：
  - “声音目标稿 v1”已经真实接入阿里请求体
  - 当前已生成同文案 A / B / C 三版真实音频，供复审
- 现在还不能写：
  - “三版听感已经明确达到最终定稿水位”
  - 因为是否像客服腔 / 播音腔 / 广告腔，仍需要人工试听确认

## 当前最关键的下一步

- 先人工试听：
  - `dist/formal_api_demo/tts/voice_probe_A.mp3`
  - `dist/formal_api_demo/tts/voice_probe_B.mp3`
  - `dist/formal_api_demo/tts/voice_probe_C.mp3`
- 若三版整体方向对，但仍不够“军事鉴定 / 装备拆解 / 判断型解说”：
  - 先改 `instruction` 写法
  - 不要先切模型族
  - 只有在确认 `longanyang + cosyvoice-v3-flash` 的承载力不足时，再考虑换 voice

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- 若继续推进阿里 TTS 风格复审：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
  - `dist/formal_api_demo/tts_style_probe_variants.json`
