# 2026-04-03 formal_api_demo 质量审核 round1 + liveportrait round1

## 本轮目标

- A 线：
  - 对已成立的普通主线做第一轮正式质量审核
  - 先收口问题，不做大面积质量修补
- B 线：
  - 推进 `liveportrait-detect -> liveportrait`
  - 优先补齐官方契约、provider implementation round1、测试与 blocker 收口

## skill 检查结果

- 仓库本地 `skills/`：
  - 未找到
- 全局 `~/.codex/skills`：
  - 已检查
  - 本轮实际纳入：
    - `using-superpowers`
    - `systematic-debugging`
    - `test-driven-development`
    - `verification-before-completion`
- 说明：
  - 本轮用户已给出明确边界、文件列表和完成标准
  - 因此未再额外展开 `writing-plans` / `brainstorming`

## A 线：普通主线质量审核 round1

### 实际审核了哪些产物

- 需求与结构锚点：
  - `cases/formal_api_demo.md`
- generation 产物：
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/visual_generation_plan.json`
  - `dist/formal_api_demo/visual/seg01_image.png`
  - `dist/formal_api_demo/visual/seg02_image.png`
  - `dist/formal_api_demo/visual/seg02_video.mp4`
  - `dist/formal_api_demo/visual/seg03_image.png`
- assembly 产物：
  - `dist/formal_api_demo/final.mp4`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  - `dist/formal_api_demo/assembly/preview_manifest.json`
  - `dist/formal_api_demo/assembly_plan.json`
  - `dist/formal_api_demo/manifest.json`

### A 线主结论

- 当前普通主线已经具备“正式可审产物”
- 但当前只到“可继续复审水位”，还没到“质量过线可交付”

### 一票否决项

- 画面 demo / PPT 感仍然过重
- 15 秒里有 9 秒仍靠静态图承载
- `seg02` 虽然已有真实视频素材，但整支视频的“散乱 -> SOP”结果变化仍不够可见

### 当前最关键的 2 个质量问题

1. 中段推进还偏“方法说明书”
   - 脚本是“先把目标、输入、输出压成 SOP，再让生成和组装按流程跑”
   - 信息正确，但更像流程说明，不像内容推进
2. 结果变化没有真正被看见
   - Hook、结尾都成立
   - 但核心变化主要停留在文字层和意图层，观众未必能直观看到“从散乱到收束”的过程

### 问题分层

- “中段仍像说明书”：
  - `输入层`
- “画面 demo 感重、变化不可视”：
  - `generation 层`

### 其他审核结论

- 开头 3 秒 hook：
  - 成立
  - “AI 项目卡住，不是没思路，是流程还没拉齐。”有明确问题抓手
- 结尾落点：
  - 成立
  - “先稳住样片，再把质量逐轮压到正式水位。”是清楚收束
- 音画协调：
  - 结构级没有明显冲突
  - `formal_voiceover.mp3` 时长约 14.06 秒，`final.mp4` 为 15 秒
  - 但本轮未做真人听感验收，不把听感写成已验证
- 字幕理解性：
  - 成立
  - 单句切分清楚，没有明显过密

### A 线下一轮只该改什么

- 只改 2 点：
  - 把 `seg02` 做成更强的“散乱 -> SOP”视觉转化
  - 把中段文案从抽象说明改成更具体的推进表达
- 本轮没有继续做：
  - preview 画面 round2
  - 大面积视觉返工
  - wan provider 重做

## B 线：真人开口分支 round1

### 先审计到的缺口

- `portrait_detect`
- `portrait_video_generation`
- create task
- poll task
- detect 结果写回
- 口型视频结果写回
- 本地素材下载
- manifest / result_summary / segment outputs 写回
- 错误处理 / blocked_reason / failure_reason

### 官方依据核对

- 已核对阿里官方文档：
  - `LivePortrait图像检测API参考`
  - `LivePortrait视频生成 API参考`
  - `如何上传本地文件至临时存储空间并获取文件 URL`
- 本轮据此补齐了：
  - `face-detect` 请求结构
  - `video-synthesis/` 异步任务创建
  - `/api/v1/tasks/{task_id}` 轮询
  - 本地文件上传到临时存储空间的最小 multipart form-data 提交
  - `oss://...` 资源写回

### 本轮实际推进了什么

- `formal_api_demo_core.py`
  - `visual_generation_gate` 不再把阿里 provider 下的 `portrait_detect` / `portrait_video_generation` 固定视为“implementation missing”
  - 新增：
    - `_execute_aliyun_liveportrait_detect(...)`
    - `_execute_aliyun_liveportrait_video_generation(...)`
    - `_upload_file_to_aliyun_temp_storage(...)`
    - `_build_multipart_form_data(...)`
    - `_normalize_timeout_blocked_reason(...)`
  - `build_visual_generation_plan(...)` 已能在开启 portrait 分支时：
    - 先生成底图
    - 上传底图 / 音频
    - 做 detect
    - create liveportrait task
    - poll task
    - download 本地 mp4
    - 回写 `segment_assets[*].video_asset_path`
    - 回写 `segments[*].task_slots.video_task_id`
    - 回写 `visual_generation.portrait_detect / portrait_video_generation`
- `config/formal_api_demo.example.toml`
  - 把 portrait 分支注释从“路线已定但未实现”改成“当前已支持代码 / 契约层接入”

### 当前最具体 blocker

- 代码与测试层已补到位
- 当前没有 `config/formal_api_demo.local.toml`
- 因而不能在这个 worktree 做带真实 API Key 的线上 detect / liveportrait 实调
- 所以：
  - 不把 `liveportrait-detect` 写成已线上验证 `success`
  - 不把 `liveportrait` 写成已线上验证 `success`

### B 线测试改动

- `test_generate_non_dry_run_liveportrait_branch_downloads_local_video_when_detect_passes`
- `test_generate_non_dry_run_liveportrait_blocks_when_detect_rejects_image`
- `test_generate_non_dry_run_liveportrait_blocks_when_detect_times_out`
- `test_generate_non_dry_run_liveportrait_marks_failed_when_remote_task_fails`
- `test_generate_non_dry_run_liveportrait_blocks_when_task_poll_times_out`
- `test_generate_non_dry_run_liveportrait_marks_failed_when_local_video_file_is_missing`

### B 线验证结果

- 上述 6 个 liveportrait round1 测试：
  - 全部通过
- 覆盖到的状态：
  - detect success
  - detect reject
  - detect timeout
  - liveportrait success
  - liveportrait remote task failed
  - liveportrait task poll timeout
  - 本地结果文件缺失

## 本轮更新的文件

- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
- `config/formal_api_demo.example.toml`
- `codex_source/02_current_execution_context.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_quality_review_and_liveportrait_round1.md`

## 验证命令与结果

- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_branch_downloads_local_video_when_detect_passes`
  - `OK`
- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_blocks_when_detect_rejects_image tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_blocks_when_detect_times_out tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_marks_failed_when_remote_task_fails tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_blocks_when_task_poll_times_out tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_liveportrait_marks_failed_when_local_video_file_is_missing`
  - `OK`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `Ran 34 tests ... OK`
- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - 通过

## 当前状态收口

- TTS API：`success`
- 图片 API：`success`
- 通用视频 API：`success`
- 真人开口分支：`blocked`
  - 原因已从“provider implementation missing”收口为“缺本地正式配置，无法做真实线上实调”
- local assembly：`success`
- overall：`blocked`
  - 主要原因仍是真人开口分支缺真实线上验证
  - 普通主线质量 round1 也已明确还没过线

## 下一轮最关键一步

1. 补 `config/formal_api_demo.local.toml`
2. 跑一次带真实 API Key 的 `liveportrait-detect -> liveportrait` 实调
3. 若 B 线实调通过，再只改 A 线的 `seg02` 变化可视化与中段说明书感
