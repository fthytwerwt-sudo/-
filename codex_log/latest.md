# Latest

## 当前 formal_api_demo 执行状态

- 当前正式主路径已收口为：
  - 文本需求 → 脚本 → 配音 API → 图片 / 视频生成 API → 本地 assembly → 本地 mp4 → 人工上传
- `formal_api_demo` 当前真实口径：
  - generation 继续接 API，TTS / 图片 / 视频仍属于正式 generation 主链
  - local assembly / 本地 mp4 是当前默认交付路径
  - cloud assembly 属于后续增强项；缺 `storage.space_name` / `assembly.template_id` 时，当前记为 `skipped`
  - 缺 `image_generation.model` / `video_generation.model` 时，generation 会被真实拦截，不能再写成 success
- 当前整体状态判定：
  - `overall_status` 以 generation + local assembly 为准
  - generation 成功且 local assembly 成功时，即使 cloud assembly 是 `skipped`，整体仍是 success
  - cloud assembly 当前不再是整体成功与否的硬前置

## 最近一次真正完成了什么

- `formal_api_demo` 这一轮核心修复已经把代码、测试、配置注释统一到同一口径：
  - 视频 API 继续接
  - local assembly 默认交付
  - cloud assembly optional / skipped
  - 缺视觉模型时 generation 真实 blocked
- 对新会话最重要的结论不是执行机制桥接文件，而是：
  - `formal_api_demo` 当前主链已经按“generation 继续接 + 本地 assembly 默认交付”收口
  - `config/formal_api_demo.example.toml`、`formal_api_demo_core.py`、`tests/test_formal_api_demo_pipeline.py` 现在彼此一致

## 当前最关键下一步

- 不再继续补 `latest.md`
- 不再继续扩机制文件
- 下一步应回到视频主线任务推进：
  - 优先继续推进真实图片 / 视频 provider implementation，或直接复审本地 mp4 成片质量

## 新会话建议先读

- `AGENTS.md`
- `codex_log/latest.md`
- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
- `config/formal_api_demo.example.toml`
