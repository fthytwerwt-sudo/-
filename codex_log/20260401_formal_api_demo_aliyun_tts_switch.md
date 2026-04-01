# 20260401 Formal API Demo Aliyun TTS Switch

## 本轮目标

- 把 `formal_api_demo` 当前卡住的 TTS provider 从火山 Edge Gateway 切到阿里百炼
- 只先完成 TTS provider 接入与真实音频探测
- 不推进视频生成，不推进 assembly，不夸大成整条正式链路成功

## 执行前已确认事实

- 当前 formal_api_demo 已有：
  - `generation_gate`
  - `manifest`
  - `result_summary`
- 上一轮已确认 Edge Gateway 路径的最小失败层是外部凭证来源，不再值得继续消耗
- 当前 formal_api_demo 仍只做 TTS probe，不做视觉生成和 assembly
- 当前仓库 working tree 中存在用户未提交的 `project_source/*` 变更，本轮不得碰这些文件

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- 本地 `config/formal_api_demo.local.toml`（只读检查，不回显真实值）

## 实际改动

- 修改了 `formal_api_demo_core.py`
  - 新增阿里百炼 TTS route family：`aliyun_bailian_cosyvoice`
  - 保留原有火山 family：
    - `ark_openai_compatible`
    - `edge_gateway_openai_compatible`
    - `doubao_openspeech_v3`
  - 新增阿里百炼最小 HTTP probe：
    - `POST https://dashscope.aliyuncs.com/api/v1/services/audio/tts/SpeechSynthesizer`
    - 成功时解析 `output.audio.url`
    - 再真实下载音频文件到本地
  - 新增阿里 provider 解析与 request_debug 字段：
    - `api_route_family`
    - `provider`
    - `base_url`
    - `relative_path`
    - `model_identifier_source`
  - 成功判定继续收紧：
    - 只有真实音频文件落盘才记 `success`
    - 远端 4xx / 5xx 一律记 `failed`
    - 前提不足继续记 `blocked`
- 修改了 `config/formal_api_demo.example.toml`
  - route family 注释新增 `aliyun_bailian_cosyvoice`
  - 示例默认 TTS route family 切到阿里百炼
  - 示例 `tts.model` 改为 `cosyvoice-v3-flash`
  - `tts.voice` 继续要求在 local 配置显式填写
- 修改了 `tests/test_formal_api_demo_pipeline.py`
  - 新增阿里 family 缺 API Key = `blocked`
  - 新增阿里 family 缺 model = `blocked`
  - 新增阿里 family mock success = `success` 且真实写出音频文件
  - 新增阿里 family 远端 403 = `failed`
  - 保留 dry-run 路径与现有火山 family 测试

## 实际执行

- `git status --short --branch`
- `git switch -c codex/aliyun-bailian-tts`
- 本地配置只读检查：
  - `auth.api_key` 非空
  - `tts.model` 非空
  - `tts.voice` 非空
  - 当前 local config 的 route family 还不是阿里
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
- 真实 non-dry-run：
  - 未修改本地 `config/formal_api_demo.local.toml`
  - 使用一次性临时 overlay config，把 `provider.name` 和 `tts.api_route_family` 切到阿里百炼
  - 执行 `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo --local-config <temp_overlay>`
- 结果核对：
  - `dist/formal_api_demo/manifest.json`
  - `dist/formal_api_demo/generation_gate.json`
  - `dist/formal_api_demo/result_summary.json`

## 当前结果

- 代码层结果：
  - 阿里百炼 TTS provider 已接入
  - 单测通过
  - 语法检查通过
- 真实执行结果：
  - `generation_gate.status = success`
  - `manifest.current_status = failed`
  - `manifest.generation.tts_probe.status = failed`
  - `result_summary.overall_status = failed`
  - `request_debug.api_route_family = aliyun_bailian_cosyvoice`
  - `request_debug.provider = aliyun_bailian`
  - `request_debug.base_url = https://dashscope.aliyuncs.com/api/v1`
  - `request_debug.relative_path = /services/audio/tts/SpeechSynthesizer`
  - `request_debug.model_identifier_source = model`
- 当前未落出真实音频文件

## 最小失败层级

- 当前失败不是 `blocked`
- 当前失败也不是 assembly 或视频生成问题
- 当前已压缩到阿里百炼远端认证层：
  - HTTP `401`
  - 远端返回：`InvalidApiKey`
- 因此本轮最小失败层是：
  - `auth.api_key / provider 认证有效性`

## 下一步建议

- 先修正本地阿里百炼 API Key，再重跑同一条 non-dry-run。
- 在 API Key 修正之前：
  - 不要继续推进 assembly
  - 不要把问题误判成 model / voice / 地域 / 组装问题
- 若 API Key 修正后仍失败，再继续把失败压缩到：
  - `tts.model`
  - `tts.voice`
  - 地域 / 权限
  - 或其他远端接口响应层
