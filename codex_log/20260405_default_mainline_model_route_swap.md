# 本轮目标

把《视频工厂》里已不再继续作为默认主线的两个模型从正式执行口径中移除：

- `wan2.6-t2v`
- `facechain-generation`

并把当前普通视频默认主线改成：

- `wan2.6-image -> wan2.7-i2v`

# 执行前已确认事实

- 用户已明确确认：
  - `wan2.6-t2v` 不再继续作为默认普通视频主线
  - `facechain-generation` 不再继续作为默认依赖
- 真人分支本轮不改模型路线，继续保留：
  - `liveportrait-detect -> liveportrait`
- `wan2.7-videoedit` 只能作为后期修补 / 编辑增强，不能被写成主生成模型
- 当前仓库存在与本轮无关的未提交改动：
  - `project_source/00_project_brief.md`
  - `project_source/03_perplexity_prompt_library.md`

# 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `formal_api_demo_core.py`
- `formal_hybrid_master.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `tests/test_formal_hybrid_master.py`
- 全仓 `rg` 检索：
  - `wan2.6-t2v`
  - `facechain-generation`
  - `wan2.6-image`
  - `qwen-image-edit-plus`
  - `wan2.7-i2v`
  - `wan2.7-videoedit`
  - `liveportrait-detect`
  - `liveportrait`
- 官方文档核对：
  - 阿里百炼 `wan2.7-i2v` 图生视频接口
  - 阿里百炼 `qwen-image-edit-plus` 图像编辑定位
  - 阿里百炼 `wan2.7-videoedit` 视频编辑定位

# 实际改动

- `formal_api_demo_core.py`
  - 默认普通视频模型改为 `wan2.7-i2v`
  - 增加 i2v 首帧输入 payload 构造
  - 普通视频段执行时，若命中 i2v，改为先拿首帧图片再发视频任务
  - 正式说明里明确：
    - 普通视频主线是 `wan2.6-image -> wan2.7-i2v`
    - 人物图 / 人像底图默认走 `wan2.6-image`
    - 修图走 `qwen-image-edit-plus`
    - `wan2.7-videoedit` 不是主生成模型
- `formal_hybrid_master.py`
  - 默认普通视频模型跟随切到 `wan2.7-i2v`
  - hybrid 视觉资产生成增加“先图后视频”的 seed image 链
- `config/formal_api_demo.example.toml`
  - 默认普通视频模型改为 `wan2.7-i2v`
  - 注释里移除 `wan2.6-t2v` 主线口径
  - 注释里明确 `facechain-generation` 不再作为默认修图 / 底图路径
  - 注释里明确 `wan2.7-videoedit` 只做后期编辑
- `codex_source/02_current_execution_context.md`
  - 当前正式执行上下文改为：
    - 普通视频：`wan2.6-image -> wan2.7-i2v`
    - 人物图 / 底图：`wan2.6-image`
    - 修图：`qwen-image-edit-plus`
    - 真人：`liveportrait-detect -> liveportrait`
- `tests/test_formal_api_demo_pipeline.py`
  - 默认主线断言改为 `wan2.7-i2v`
  - 新增 i2v payload 必须带 seed image 的测试
- `tests/test_formal_hybrid_master.py`
  - 默认主线断言改为 `wan2.7-i2v`
  - 新增 hybrid 视觉资产必须先图后视频的测试

# 实际执行

- 先改测试，让旧默认值红灯：
  - `test_normalize_generation_models_fills_blank_defaults`
  - `test_generate_dry_run_outputs_manifest_and_result_summary`
  - `test_generate_visual_assets_uses_seed_image_before_i2v`
  - `test_execute_aliyun_wan_video_generation_uses_seed_image_for_i2v`
- 再改实现与执行口径：
  - 普通视频默认模型
  - i2v 输入链
  - 配置与上下文说明
- 额外做了只读复核：
  - 核对当前 diff、默认模型常量、示例配置与执行上下文
  - 确认 `wan2.7-videoedit` 只停留在“后期编辑增强”口径

# 当前结果

- 当前项目里已不再把 `wan2.6-t2v` 写成默认普通视频主线
- 当前项目里已不再把 `facechain-generation` 写成默认依赖
- 普通视频主线现在已写成：
  - `wan2.6-image -> wan2.7-i2v`
- 人物图 / 人像底图默认现在已写成：
  - `wan2.6-image`
- 需要修图时现在已明确：
  - `qwen-image-edit-plus`
- 真人分支仍保留为：
  - `liveportrait-detect -> liveportrait`
- `wan2.7-videoedit` 现在已明确为：
  - 后期修补 / 编辑增强
  - 不是主生成模型

# 实际验证

- 已运行：
  - `python3 -m unittest tests.test_formal_hybrid_master tests.test_formal_api_demo_pipeline`
- 输出：
  - `Ran 35 tests in 2.653s`
  - `OK`
- 已额外检索确认：
  - 非历史日志范围内不再残留把 `wan2.6-t2v` 当默认主线的口径
  - `facechain-generation` 仅保留“已停用默认依赖”的说明，不再作为默认调用

# 当前结果状态

- 当前工作分支：
  - `codex/round1`
- 当前状态分类（提交前）：
  - 待 commit / push，暂不能写成 `task_branch_only`

# 下一步建议

- 提交并 push 当前任务分支
- 若本轮结果需要成为仓库正式接手口径，再同步回：
  - `codex/user-readable-map`
- 若后续要把真人分支真正切成默认 production 主线，再单独处理：
  - `liveportrait-detect -> liveportrait` 的真实 provider implementation
