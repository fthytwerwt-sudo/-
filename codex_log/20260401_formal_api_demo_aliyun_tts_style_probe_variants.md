# 20260401 Formal API Demo Aliyun TTS Style Probe Variants

## 本轮目标

- 不再泛泛调声音，而是把 `formal_api_demo` 当前阿里 TTS 子线按“声音目标稿 v1”压成可执行结果
- 只推进阿里 TTS 风格控制
- 不推进视频生成，不推进 assembly

## 执行前已确认事实

- 阿里百炼 TTS 已接通，且此前已落出真实音频文件
- 当前正式版 generation 仍只做到 TTS probe，不代表整条正式视频链路成功
- 用户要求先判断风格稿是否真实进入请求体，再决定是否生成 A / B / C 三版

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- 本地 `config/formal_api_demo.local.toml`（只读，不回显真实值）

## 关键判断

- 代码修改前，阿里 TTS 请求体只发送：
  - `model`
  - `input.text`
  - `input.voice`
  - `input.format`
- 因此“声音目标稿 v1”当时并没有真实进入阿里请求体
- 当前最小缺口不是模型或音色，而是：
  - 阿里 CosyVoice HTTP 请求体没有桥接 `instruction`
  - 也没有桥接语速、音高、音量参数
  - 仓库里没有固定 A / B / C 风格对照入口

## 实际改动

- 修改了 `formal_api_demo_core.py`
  - 为阿里 CosyVoice HTTP 请求新增风格桥接：
    - `input.instruction`
    - `input.rate`
    - `input.pitch`
    - `input.volume`
  - 新增运行期 TTS override 解析：
    - `instruction`
    - `speech_rate`
    - `pitch_rate`
    - `volume`
  - 新增 `run_aliyun_tts_style_probe_variants(...)`
  - 新增固定测试文案与 A / B / C 默认参数
  - 新增阿里 request debug 字段，确认风格稿是否真实进请求体
- 修改了 `config/formal_api_demo.example.toml`
  - 新增通用阿里风格参数示例：
    - `tts.instruction`
    - `tts.speech_rate`
    - `tts.pitch_rate`
    - `tts.volume`
  - 新增固定测试文案：
    - `[tts_style_probe]`
  - 新增三版默认参数：
    - `[tts_style_probe_variant_A]`
    - `[tts_style_probe_variant_B]`
    - `[tts_style_probe_variant_C]`
- 修改了 `tests/test_formal_api_demo_pipeline.py`
  - 新增 A / B / C 三版真实落文件测试
  - 校验阿里请求体确实包含：
    - `input.instruction`
    - `input.rate`
    - `input.pitch`
    - `input.volume`

## 固定测试文案

- 当前三版统一使用同一段 3 句测试文案：
  - 表面参数很多，但关键上限只看供电、火控和协同链路
  - 前两项还能补，第三项掉队后新壳子也只是好看
  - 结论带一点锋利感：不是没亮点，而是关键战力没站住

## 三版设计

- A 稳定版
  - 目标：冷静利落，优先保住稳定判断感
  - `instruction = neutral`
  - `speech_rate = 1.18`
  - `pitch_rate = 0.92`
  - `volume = 46`
- B 判断感更强版
  - 目标：保持克制，同时把锋利感再往前推一点
  - `instruction = disgusted`
  - `speech_rate = 1.24`
  - `pitch_rate = 0.9`
  - `volume = 48`
- C 更克制版
  - 目标：进一步压低情绪起伏，保住冷静和收束
  - `instruction = neutral`
  - `speech_rate = 1.08`
  - `pitch_rate = 0.9`
  - `volume = 44`

## 实际执行

- 单测：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_run_aliyun_tts_style_probe_variants_writes_three_named_audio_files`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 语法检查：
  - `python3 -m py_compile formal_api_demo_core.py tests/test_formal_api_demo_pipeline.py`
- 真实生成：
  - 通过 `python3` 内联脚本调用 `run_aliyun_tts_style_probe_variants(...)`
  - 读取：
    - `cases/formal_api_demo.md`
    - `config/formal_api_demo.example.toml`
    - 本地 `config/formal_api_demo.local.toml`
  - 输出目录：
    - `dist/formal_api_demo`

## 执行结果

- 单测通过：
  - `Ran 18 tests in 0.037s`
  - `OK`
- 真实生成结果：
  - `overall_status = success`
  - `style_draft_in_request = true`
  - `recommended_variant_id = A`
- 三版真实音频已落出：
  - `dist/formal_api_demo/tts/voice_probe_A.mp3`
  - `dist/formal_api_demo/tts/voice_probe_B.mp3`
  - `dist/formal_api_demo/tts/voice_probe_C.mp3`
- 三版 request debug 已确认风格稿真实进入请求体：
  - `request_input_keys = [text, voice, format, instruction, rate, pitch, volume]`
  - A / B / C 均为 `instruction_present = true`
- 结构化结果文件：
  - `dist/formal_api_demo/tts_style_probe_variants.json`

## 当前结论

- 这轮已经可以明确说：
  - “声音目标稿 v1”不再只是描述，已经桥接进阿里 CosyVoice 的真实请求体
  - 当前同文案三版风格音频已生成，具备复审条件
- 这轮还不能冒充说：
  - 三版听感已经明确满足“不能像客服播报 / 新闻播音 / 广告配音”
- 原因不是代码没接通，而是：
  - 这些判断仍需要人工试听

## 当前最值的下一步

- 先人工试听 A / B / C 三版
- 若三版整体方向对，但还不够“军事鉴定 / 装备拆解 / 判断型解说”：
  - 先改 `instruction` 写法
  - 不要先切模型族
  - 只有确认 `longanyang + cosyvoice-v3-flash` 承载不住时，再考虑换 voice
