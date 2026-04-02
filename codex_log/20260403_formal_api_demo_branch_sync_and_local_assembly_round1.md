# 2026-04-03 formal_api_demo 主读取分支同步 + local assembly round1

## 本轮目标

- 把 `codex/formal-api-demo-wan-provider-impl` 已完成并已 push 的结果，真实同步回主读取分支 `codex/user-readable-map`
- 在仓库里补最小可执行的主读取分支 / 任务分支回流规则
- 在主读取分支上继续推进 `formal_api_demo` 的正式 local assembly implementation
- 不继续修 preview 画面
- 不继续做真人开口分支
- 不扩 cloud assembly

## skill 检查结果

- 仓库本地 `skills/`：
  - 未找到
- 全局 `~/.codex/skills`：
  - 已检查
  - 本轮实际纳入：
    - `using-superpowers`
    - `git-advanced-workflows`
    - `using-git-worktrees`
    - `test-driven-development`
    - `verification-before-completion`
- 说明：
  - `brainstorming` / `writing-plans` 已检查到
  - 但本轮用户已经给出明确文件边界、执行顺序和完成标准，因此没有再单独展开新的设计文档回合

## 分支核对与同步

### 核对结果

- 主读取分支：
  - `codex/user-readable-map`
- 任务分支：
  - `codex/formal-api-demo-wan-provider-impl`
- 任务分支相对主读取分支多出的最小提交集合：
  - `07ff6a1 Implement formal_api_demo wan visual providers`
  - `5aab536 docs: verify formal_api_demo wan provider status`
- 最小同步方式：
  - `cherry-pick`

### 为什么没有直接在当前工作区切分支

- 当前原工作区存在无关 `project_source/*` 脏改动
- 为避免碰到这些文件，本轮在隔离 worktree 中挂载 `codex/user-readable-map`

### 实际同步动作

- worktree：
  - `/private/tmp/video-factory-user-readable-map.oh1UeA`
- 已执行：
  - `git worktree add /private/tmp/video-factory-user-readable-map.oh1UeA codex/user-readable-map`
  - `git cherry-pick 07ff6a1 5aab536`
  - `git push origin codex/user-readable-map`
- `cherry-pick` 后在主读取分支上的提交：
  - `668bab1 Implement formal_api_demo wan visual providers`
  - `a65325c docs: verify formal_api_demo wan provider status`

### 实际同步到主读取分支的文件

- `formal_api_demo_core.py`
- `tests/test_formal_api_demo_pipeline.py`
- `codex_source/02_current_execution_context.md`
- `codex_log/latest.md`
- `codex_log/20260403_formal_api_demo_wan_provider_impl_round1.md`
- `codex_log/20260403_formal_api_demo_wan_provider_impl_verification.md`

## 分支同步规则补齐

### 更新文件

- `codex_source/02_current_execution_context.md`
  - 明确当前默认主读取分支是 `codex/user-readable-map`
  - 明确任务分支结果只有回流主读取分支并更新 `latest` 后，才算仓库正式状态
  - 新会话若涉及主读取分支 / 回流规则，补读 `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - 新增最小规则文档
  - 写清主读取分支、任务分支回流、收尾 4 个同步锚点、`latest.md` 的使用规则

### 收尾必须回报的 4 个同步锚点

- 当前工作分支
- 最新提交 SHA
- 是否已 push
- 是否已同步回主读取分支 `codex/user-readable-map`

## local assembly 本轮实现

### 已完成

- `formal_api_demo_core.py`
  - `run_assembly_pipeline(...)` 不再把 local assembly 固定写成“实现未接入”
  - 新增正式 local assembly 执行路径：
    - 从 manifest 读取真实本地视觉素材
    - 每段判断该用本地图片还是本地视频
    - 用 ffmpeg 先把每段素材标准化为本地 segment mp4
    - 拼接为正式 visual track
    - 再合入真实 voiceover 音频与字幕，输出 `dist/formal_api_demo/final.mp4`
  - 正式输出路径会回写到：
    - `manifest["assembly"]["delivery_video_path"]`
    - `result_summary["artifact_paths"]["final_video"]`
  - preview 继续只保留为辅助产物
- 失败口径已分开：
  - 缺素材 / 缺路径 / 缺 ffmpeg => `blocked`
  - ffmpeg 真实执行失败 / 输出文件缺失 => `failed`

### 本轮没有做

- preview 画面优化
- `seg02` 修图
- cloud assembly 扩写
- `liveportrait-detect -> liveportrait`

## 测试改动

### 新增 / 改写

- `test_assemble_non_dry_run_outputs_formal_local_mp4_when_visual_assets_ready`
  - 锁住 formal local assembly 成功路径
- `test_assemble_non_dry_run_blocks_when_manifest_visual_path_missing_even_if_preview_succeeds`
  - 锁住 preview 成功但 formal assembly 仍 blocked 的情况
- `test_assemble_non_dry_run_marks_failed_when_local_ffmpeg_assembly_fails`
  - 锁住 ffmpeg 真实失败时必须诚实 `failed`
- 保留：
  - `test_assemble_non_dry_run_keeps_preview_auxiliary_when_formal_local_assembly_not_ready`
  - 继续锁住 preview 不能冒充 formal assembly

## 验证命令与结果

- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_outputs_formal_local_mp4_when_visual_assets_ready tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_blocks_when_manifest_visual_path_missing_even_if_preview_succeeds tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_marks_failed_when_local_ffmpeg_assembly_fails`
  - 结果：`Ran 3 tests ... OK`
- `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_dry_run_reads_manifest_and_outputs_result_summary tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_keeps_preview_auxiliary_when_formal_local_assembly_not_ready tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_outputs_formal_local_mp4_when_visual_assets_ready tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_blocks_when_manifest_visual_path_missing_even_if_preview_succeeds tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_marks_failed_when_local_ffmpeg_assembly_fails`
  - 结果：`Ran 5 tests ... OK`
- `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`
  - 结果：通过
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：`Ran 28 tests ... OK`

## 当前真实状态

- TTS API：`success`
- 图片 API：`success`
- 通用视频 API：`success`
- 真人开口分支：`blocked`
- local assembly：`success`
- overall：`blocked`

## 当前剩余最高优先级 blocker

- `liveportrait-detect -> liveportrait`

## 结论

- “结果完整同步到 GitHub”：
  - 已解决
- “Codex 任务分支与主读取分支不同步”：
  - 已补最小执行规则，并已把这轮结果真实回流到 `codex/user-readable-map`
- “下一轮正式执行入口”：
  - 已解决
  - 新会话默认从主读取分支读取 `latest.md`、`02_current_execution_context.md`、`08_branch_sync_and_reading_branch_rules.md`，即可直接接着推进真人开口分支
