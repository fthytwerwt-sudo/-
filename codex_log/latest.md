# Latest

## 当前主结论

- 2026-04-05 已把《视频工厂》默认普通视频主线从 `wan2.6-t2v` 切到 `wan2.6-image -> wan2.7-i2v`。
- `facechain-generation` 已不再作为当前仓库的默认人物图 / 人像底图依赖。
- 真人分支仍保留为：
  - `liveportrait-detect -> liveportrait`
- `wan2.7-videoedit` 已明确收口为：
  - 后期修补 / 编辑增强
  - 不是主生成模型

## 本轮关键执行事实

- 当前代码里命中的旧默认主线主要在：
  - `formal_api_demo_core.py`
  - `formal_hybrid_master.py`
  - `config/formal_api_demo.example.toml`
  - `codex_source/02_current_execution_context.md`
  - 相关测试
- 当前代码里未发现 `facechain-generation` 的直接默认调用路径；
  - 这次已在正式执行口径中明确写成“不再默认依赖”
  - 普通人物图 / 底图默认转为 `wan2.6-image`
  - 需要修图时明确转为 `qwen-image-edit-plus`
- `wan2.7-i2v` 所需的“先图后视频”链路已补入：
  - 正式主线 `formal_api_demo_core.py`
  - hybrid 视觉资产生成 `formal_hybrid_master.py`

## 本轮实际改动（仓库内）

- 更新默认模型与执行说明：
  - `formal_api_demo_core.py`
  - `formal_hybrid_master.py`
  - `config/formal_api_demo.example.toml`
  - `codex_source/02_current_execution_context.md`
- 更新测试：
  - `tests/test_formal_api_demo_pipeline.py`
  - `tests/test_formal_hybrid_master.py`

## 本轮实际验证

- 已运行：
  - `python3 -m unittest tests.test_formal_hybrid_master tests.test_formal_api_demo_pipeline`
- 结果：
  - `Ran 35 tests in 2.653s`
  - `OK`

## 当前同步状态

- 当前工作分支：
  - `codex/round1`
- `codex_log/latest.md`：
  - 已更新
- 是否已 push：
  - 待本轮提交后确认
- 是否已同步回 `codex/user-readable-map`：
  - 待本轮提交与分支同步后确认
