# formal_api_demo 免费优先模型路线收口

## 本轮目标

- 把 `formal_api_demo` 当前阿里路线先收成“免费优先版”
- 明确区分：
  - 通用图片 / 视频主线
  - 真人开口分支
- 不伪造 provider 已真实接通
- 不继续推进 preview 画面 round2

## 执行前确认

- 当前仓库已完成上一轮 `mainline realign`：
  - `generation success = 配音 API success + 图片 / 视频 API success`
  - `preview` 不再冒充 generation success
- 但 `config/formal_api_demo.example.toml` 仍未写明免费优先模型路线
- `formal_api_demo_core.py` 仍未把通用视频与真人开口分支彻底拆开
- 仓库本地 `skills/` 目录未命中相关 skill
- 本轮实际纳入的全局 skill：
  - `using-superpowers`
  - `test-driven-development`
  - `verification-before-completion`
  - `python-configuration`

## 实际改动

- 更新 [config/formal_api_demo.example.toml](/Users/fan/Documents/视频工厂/config/formal_api_demo.example.toml)
  - `image_generation.model = "wan2.6-image"`
  - `video_generation.model = "wan2.6-t2v"`
  - 新增 `[portrait_detect]`
  - 新增 `[portrait_video_generation]`
- 更新 [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - 补充免费优先模型常量
  - 新增视觉模型路由构建逻辑
  - 在 gate / manifest / visual plan 中拆出：
    - `general_video_generation`
    - `portrait_detect`
    - `portrait_video_generation`
  - 明确 `liveportrait` 必须先过 `liveportrait-detect`
  - provider implementation 未接通时继续诚实 `blocked`
- 更新 [codex_source/02_current_execution_context.md](/Users/fan/Documents/视频工厂/codex_source/02_current_execution_context.md)
  - 把免费优先模型路线写入执行层入口
- 更新 [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
  - 把当前最高优先级切到真实 provider implementation

## 验证

- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`

## 当前真实状态

- TTS API：`success`
- 图片 API：`blocked`
  - 模型路线已定为 `wan2.6-image`
  - provider implementation 未接入
- 通用视频 API：`blocked`
  - 模型路线已定为 `wan2.6-t2v`
  - provider implementation 未接入
- 真人开口分支：`blocked`
  - 路线已定为 `liveportrait-detect -> liveportrait`
  - 前置检测与开口视频 provider implementation 未接入
- local assembly：`blocked`
  - 当前仍只有辅助 preview

## 结论

- 本轮完成的是“免费优先模型路线与语义收口”
- 本轮没有把 provider 假装成已接通
- 当前最高优先级 blocker 已明确回到真实 provider implementation，而不是继续修 preview 画面
