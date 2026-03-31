# 20260401 TTS Route Fix

## 本轮目标

- 排查 formal_api_demo 骨架里的 TTS 真实调用为什么返回 404
- 修正 `blocked / failed / success` 的分类
- 重新跑一次真实 non-dry-run TTS probe，并把失败点压缩到最小可判断层

## 执行前已确认事实

- 本地最少关键字段已齐：`auth.api_key`、`tts.endpoint_id` 或 `tts.model`、`tts.voice`
- 当前不是配置缺失问题
- 当前真实请求已经发出
- 当前接口返回的是 404
- 本轮只围绕 TTS，不扩到视觉、组装和整条正式视频链路

## 当前 404 的判断

- 当前代码实际调用的是：
  - `POST https://ark.cn-beijing.volces.com/api/v3/audio/speech`
  - SDK 调用方式：`client.audio.speech.with_streaming_response.create`
  - `model` 参数当前取自 `endpoint_id`
  - `voice` 放在 payload 内
- 当前请求结构的脱敏结论：
  - `endpoint_id` 形状是纯数字 10 位
  - `model` 当前为空
  - `voice` 已存在，并放在 payload 的 `voice` 字段
- 404 的最小真实原因判断为：
  - 当前 provider 路由与 TTS HTTP 接口不匹配
  - 官方火山方舟 API 列表当前没有 `audio/speech` 这条 HTTP 路由，常规在线推理文档主要暴露的是 `responses` / `chat` / 图片 / 视频等接口
  - 官方 OpenAI 兼容 TTS `/v1/audio/speech` 文档属于边缘大模型网关，不是当前 Ark `https://ark.<region>.volces.com/api/v3` 这条路由族
  - 同时，当前 `endpoint_id` 被直接当作 `model` 发送，而它的形状也不像文档中的 Ark Endpoint ID 示例格式
- 结论：
  - 这次 404 已压缩到“Ark 路由 / 接入标识匹配层”，不是本地字段缺失

## 实际改动

- 修改了 `formal_api_demo_core.py`
  - 新增脱敏 `request_debug`，把 base URL、相对路径、`model_identifier_source`、`voice` 位置等写入 `tts_probe`
  - 调整 `_classify_tts_exception`：
    - 前提不足才是 `blocked`
    - 请求已发出且收到 4xx / 5xx 默认记 `failed`
    - 404 单独归为 `ark_tts_route_or_identifier_not_found`
  - 调整 generation `next_action_hint`，让 404 明确指向“请求路由 / 接入标识匹配层”
- 修改了 `tests/test_formal_api_demo_pipeline.py`
  - 新增“远端 404 应记 failed，不应记 blocked”的测试

## 实际执行

- 先补了一个失败测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_marks_failed_when_remote_returns_404`
  - 初始结果：失败，证明旧逻辑会把远端 404 记成 `blocked`
- 修正实现后重新执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：`Ran 10 tests`，通过
- 重新跑真实 non-dry-run：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`

## 验证结果

- 修正后的真实 non-dry-run probe 结果：`failed`
- 当前真实状态：
  - `generation_gate.status = success`
  - `manifest.current_status = failed`
  - `manifest.generation.tts_probe.status = failed`
  - `result_summary.overall_status = failed`
- 当前失败原因：
  - `failure_reason = ark_tts_route_or_identifier_not_found`
  - `http_status_code = 404`
- 当前没有真实音频文件落出

## 当前结果

- 这轮已经完成两件关键事：
  - 404 的失败点已压缩到最小可判断层：`Ark /audio/speech` 路由 / `endpoint_id-model` 匹配层
  - “请求已发出但远端 404” 现在会被正确记为 `failed`，不再误记为 `blocked`
- 当前仍不能写成：
  - TTS 已接通成功
  - 正式版整条视频链路已跑通

## 下一步建议

- 下一步不是继续补本地字段，而是确认当前火山入口到底该走哪条 TTS 正式调用路由：
  - 如果继续走 Ark，需要确认 Ark 是否真的支持这条 HTTP TTS 路由，以及 `endpoint_id/model` 的正确传法
  - 如果当前能力实际属于边缘大模型网关或豆包语音服务，则需要切换到对应产品的正式请求入口
- 在这个 provider 路由问题确认前，继续重跑只会稳定得到 `failed` 404
