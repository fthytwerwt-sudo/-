# 20260401 TTS Route Family Split

## 本轮目标

- 把 formal_api_demo 的 TTS probe 从“默认全走 Ark”改成“显式 route family”
- 保留当前 Ark 路由的失败分类与调试信息
- 新增 Edge Gateway OpenAI 兼容 TTS probe 路径
- 把 Doubao OpenSpeech v3 显式拆成独立 family 与独立 Gate，不再混在 Ark 里猜

## 执行前已确认事实

- 当前正式版骨架已经具备 TTS probe 基础能力
- 上一轮真实 TTS 最新状态是 `failed(404)`，不是 `blocked`
- 当前 404 已压缩到 Ark 路由 / endpoint-model 接入标识匹配层
- 这轮不扩到视觉、云端组装或整条正式视频链路

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260401_tts_route_fix.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- 本地 `config/formal_api_demo.local.toml`（只做本地读取，不回显真实值）

## 当前 404 的判断

- 当前 Ark probe 的脱敏请求结构仍是：
  - `POST https://ark.<region>.volces.com/api/v3/audio/speech`
  - SDK 调用：`client.audio.speech.with_streaming_response.create`
  - 当前 `model` 参数优先取 `endpoint_id`
  - `voice` 放在 payload 内
- 本轮继续保留这个调试结构，但不再把它默认套用到所有 TTS family。
- 当前 404 的最小真实原因仍是：
  - Ark 路由与当前 TTS HTTP 接口不匹配，或
  - Ark 下 `endpoint_id/model` 的接入标识用法不匹配

## 实际改动

- 修改了 `formal_api_demo_core.py`
  - 新增显式 TTS route family：
    - `ark_openai_compatible`
    - `edge_gateway_openai_compatible`
    - `doubao_openspeech_v3`
  - 新增 family 读取与 family-specific gate 判断
  - Ark 继续走原有 OpenAI SDK probe
  - Edge Gateway 新增最小 OpenAI 兼容 probe：
    - `base_url = https://ai-gateway.vei.volces.com/v1`
    - `model` 只取 `tts.model`
  - Doubao OpenSpeech v3 只拆出 family / gate，本轮不强行实装真实请求
  - `request_debug` 新增：
    - `api_route_family`
    - `base_url`
    - `relative_path`
    - `model_identifier_source`
    - `voice_location`
    - 并保留 `provider_route_family` 兼容字段
  - `blocked / failed` 分类继续收紧：
    - 前提不足或实现未接入才 `blocked`
    - 已发请求收到远端 4xx / 5xx 记 `failed`
- 修改了 `config/formal_api_demo.example.toml`
  - 新增 `tts.api_route_family`
  - 新增 `tts.resource_id`
  - 注释区分不同 family 的生效字段
- 修改了 `tests/test_formal_api_demo_pipeline.py`
  - 保留远端 404 记 `failed`
  - 新增 Edge Gateway success mock
  - 新增 Doubao OpenSpeech 缺 `app_id/resource_id` 的 blocked
  - 新增 family 切换后 missing prerequisites 的差异测试

## 实际执行

- `python3 -m py_compile formal_api_demo_core.py tests/test_formal_api_demo_pipeline.py`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
- `python3 scripts/generate_formal_api_demo.py --dry-run --out /tmp/formal_api_route_family_split`

## 验证结果

- 语法检查通过
- 单测结果：`Ran 13 tests`，通过
- generate dry-run 正常产出 `manifest.json`、`generation_gate.json`、`result_summary.json`
- 本轮没有把任何未验证成功的 family 假装写成已接通 success

## 当前结果

- 当前 TTS family 已正式拆开，不再默认全走 Ark
- 当前已具备真实 probe 路径的 family：
  - `ark_openai_compatible`
  - `edge_gateway_openai_compatible`
- 当前仍是 gate-only 的 family：
  - `doubao_openspeech_v3`
- 当前仍不能写：
  - TTS 已全部接通成功
  - 正式版整条视频链路已跑通

## 下一步建议

- 下一步默认优先尝试 `edge_gateway_openai_compatible`
  - 这条路已有最小 probe 路径
  - 且更贴近公开的 OpenAI 兼容 TTS 入口
- Ark 路由可以继续保留用于对照和定位 404
- Doubao OpenSpeech 若要继续推进，需要先补真实请求体和返回解析实现，再做本地真实凭证验证
