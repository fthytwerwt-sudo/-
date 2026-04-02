# 2026-04-03 formal_api_demo 普通图片 / 视频主线 provider implementation round1

## 本轮目标

- 基于当前仓库已确认的阿里免费优先模型路线，真实补上 `formal_api_demo` 的普通图片 / 视频主线 provider implementation
- 本轮只做：
  - `wan2.6-image`
  - `wan2.6-t2v`
- 本轮不做：
  - preview 画面 round2
  - `seg02` 视觉表达优化
  - cloud assembly 扩写
  - `liveportrait-detect -> liveportrait` 真实 provider implementation

## 已读取文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/05_execution_deviation_and_reality_sync.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_mainline_realign.md`
- `codex_log/20260403_formal_api_demo_free_model_route.md`
- `config/formal_api_demo.example.toml`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `tests/test_formal_api_demo_pipeline.py`

## skill 检查结果

- 仓库本地 `skills/`：
  - 未找到
- 全局 `~/.codex/skills` 已检查并纳入：
  - `using-superpowers`
  - `brainstorming`
  - `test-driven-development`
  - `verification-before-completion`
- 本轮没有找到仓库内额外更贴切的本地 skill

## 执行前缺口审计

### 普通图片主线 `wan2.6-image`

- 缺异步创建任务请求
- 缺 `task_id` 轮询
- 缺成功结果 URL 提取
- 缺本地文件下载
- 缺 manifest / result_summary / segment outputs 的本地路径回写
- 缺超时 / 结果 URL 缺失 / 下载失败的真实失败口径

### 通用视频主线 `wan2.6-t2v`

- 缺异步创建任务请求
- 缺 `task_id` 轮询
- 缺成功 `video_url` 提取
- 缺本地视频下载
- 缺 manifest / result_summary / segment outputs 的本地路径回写
- 缺下载失败与任务失败口径

### 真人开口分支 `liveportrait-detect -> liveportrait`

- 路线与配置语义已定
- 当前仍缺足够明确且安全的实现依据
- 本轮继续保持 `blocked`

## 实际改动

### 1. `formal_api_demo_core.py`

- 真实补上阿里 DashScope 普通图片 / 视频 provider implementation：
  - 图片创建任务：
    - `POST /api/v1/services/aigc/image-generation/generation`
  - 视频创建任务：
    - `POST /api/v1/services/aigc/video-generation/video-synthesis`
  - 统一轮询：
    - `GET /api/v1/tasks/{task_id}`
  - 成功后下载临时 URL 到本地 `dist/formal_api_demo/visual/`
- `build_visual_generation_plan` 不再固定只落 `visual plan / preview storyboard`
  - gate 不通过时继续诚实 `blocked`
  - gate 通过时真实执行 create / poll / download
- manifest / result_summary 已同步补齐：
  - `segments[*].task_slots.image_task_id`
  - `segments[*].task_slots.video_task_id`
  - `segments[*].output_slots.visual_uri`
  - `generation.visual_generation.segment_assets[*].image_asset_path`
  - `generation.visual_generation.segment_assets[*].video_asset_path`
  - `result_summary.artifact_paths.visual_assets`
- 保持真人开口分支诚实 blocked：
  - `portrait_detect`
  - `portrait_video_generation`
- 最小同步执行层入口：
  - `codex_source/02_current_execution_context.md` 现在明确“普通图片 / 视频主线已接，liveportrait 仍 blocked”

### 2. `tests/test_formal_api_demo_pipeline.py`

- 先补红灯，再回绿
- 新增 / 改写的关键测试包括：
  - `wan2.6-image + wan2.6-t2v` 成功创建任务、轮询成功并下载本地素材
  - 轮询超时 => `blocked`
  - 图片结果 URL 缺失 => `failed`
  - 视频下载失败 => `failed`
  - liveportrait 分支继续 `blocked`
- 旧的“阿里 visual provider 未接入”断言已按新仓库事实改写

### 3. `codex_log/latest.md`

- 当前状态从“普通图片 / 视频 provider 未接入”改成：
  - 普通图片 / 视频主线已接
  - `liveportrait` 仍 blocked
  - `local assembly` 仍 blocked

## 真实验证

### 红灯阶段

- 执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_aliyun_bailian_downloads_local_visual_assets ...`
- 初始结果：
  - `FAIL`
- 失败原因：
  - 代码仍停在 `provider implementation 尚未接入` 旧状态

### 绿灯阶段

- 执行：
  - 同一批新增/修改测试
- 结果：
  - `OK`

### 全量验证

- 执行：
  - `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 结果：
  - 全部通过

## 当前 formal_api_demo 真实状态

- TTS API：`success`
- 图片 API：`success`
  - `wan2.6-image` provider implementation 已接入
- 通用视频 API：`success`
  - `wan2.6-t2v` provider implementation 已接入
- 真人开口分支：`blocked`
  - `liveportrait-detect -> liveportrait` 仍未接入
- local assembly：`blocked`
  - 当前只有辅助 preview，正式本地素材拼接实现仍未接入
- overall：`blocked`
  - generation 主线已通
  - 但正式交付仍卡在 local assembly；真人开口分支也仍未接入

## 仓库事实同步

- 当前执行现实已不再是“普通图片 / 视频 provider 未接入”
- 这属于会影响后续默认接手的长期前提变化，因此本轮已同步更新：
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`

## 下一步

- 第一优先级：
  - 正式本地 assembly implementation
- 第二优先级：
  - `liveportrait-detect -> liveportrait`
- 当前不要回退到：
  - 继续修 preview 画面
  - 把 preview 冒充 generation / assembly success
  - 把 liveportrait 写成已接通
