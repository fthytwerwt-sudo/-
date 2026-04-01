# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续默认走功能分支，不直接改 `main`。
- 当前项目仍处于“正式版目标态搭建阶段”：
  - `formal_api_demo` 的 generation 仍只收敛到 TTS probe
  - 本轮没有推进视频生成，也没有推进 assembly
  - 当前不能把正式版整条云端视频链路写成已跑通
- formal_api_demo 的 TTS 当前已新增阿里百炼 route family：
  - `aliyun_bailian_cosyvoice`
  - 火山现有 family 仍保留：
    - `ark_openai_compatible`
    - `edge_gateway_openai_compatible`
    - `doubao_openspeech_v3`
- 当前 request_debug 已可明确看到：
  - `api_route_family`
  - `provider`
  - `base_url`
  - `relative_path`
  - `model_identifier_source`

## 最近一次完成了什么

- 已修改：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
- 已接入阿里百炼 CosyVoice 的最小 HTTP TTS probe：
  - `POST https://dashscope.aliyuncs.com/api/v1/services/audio/tts/SpeechSynthesizer`
  - 使用普通百炼 API Key
  - 复用现有 `tts.model / tts.voice / tts.response_format`
  - 成功时先拿 `output.audio.url`，再真实下载音频文件落盘
- 已把状态继续收紧为：
  - 前提不足 = `blocked`
  - 远端 4xx / 5xx = `failed`
  - 真实音频文件落出 = `success`
- 已补阿里路径单测并通过：
  - 缺 API Key = `blocked`
  - 缺 model = `blocked`
  - mock success = `success` 且真实写出音频文件
  - 远端 403 = `failed`
  - dry-run 路径未破坏
- 已执行：
  - `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 真实 non-dry-run：通过临时 overlay config 把 route family 切到阿里后执行 `scripts/generate_formal_api_demo.py`
- 当前真实 non-dry-run 的最新已确认结果：
  - `generation_gate.status = success`
  - `manifest.current_status = failed`
  - `manifest.generation.tts_probe.status = failed`
  - `result_summary.overall_status = failed`
  - 未落出真实音频文件
- 当前失败点已压缩到最小层：
  - 已真正打到阿里百炼接口
  - HTTP `401`
  - 远端返回 `InvalidApiKey`
  - 说明当前不是本地前提不足、不是 assembly、也还没进入模型 / voice 层

## 当前最关键的下一步

- 先把本地用于阿里百炼的真实 API Key 换成有效值，再重跑同一条 non-dry-run。
- 在 API Key 修正前，不需要继续推进 assembly，也不要把问题误判成模型或视频链路问题。
- 若 API Key 修正后再次失败，再继续把失败压到：
  - `model`
  - `voice`
  - 接口权限 / 地域
  - 或其他远端响应层

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
