# Latest

## 当前主结论

- 2026-04-08 已把 `formal_api_demo` 的正式 local config 读取路径从 repo 内 legacy 副本，切到当前机器的官方配置源：
  - `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- 当前 repo 内的：
  - `config/formal_api_demo.local.toml`
  现在只是 legacy 占位副本，不再是默认正式读取源。
- 已基于这份官方 config 完成：
  - 旧配置 -> 新资源池结构迁移
  - `ai_report_fluff_trap_45s` 正式 generation
  - `ai_report_fluff_trap_45s` 正式 cloud assembly
  - 正式成片下载回本地
  - 正式 `review_frames` 导出

## 当前正式 config 真实状态

- `已确认`
  - 当前正式 config 路径：
    - `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- `已确认`
  - 当前 primary 已真实可用：
    - TTS primary：`1`
    - 图片 primary：`1`
    - 视频 primary：`1`
- `已确认`
  - 当前真实 backup 候选：
    - TTS backup：`0`
    - 图片 backup：`0`
    - 视频 backup：`1`
- `已确认`
  - 当前视频 backup 来自旧配置迁移时保留的旧模型：
    - `legacy_t2v`
- 必须明确：
  - 当前代码已经支持自动轮转已有资源池
  - 但当前机器上：
    - TTS 没有 backup
    - 图片没有 backup
  - 所以如果主 TTS / 主图片额度耗尽或不可用，系统会诚实报资源池已耗尽，不会伪造恢复成功

## 当前样片状态

- `已确认`
  - `cases/ai_report_fluff_trap_45s.md` 已完成正式 generation
  - 已完成正式 cloud assembly
  - 已把正式成片下载回本地：
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/final.mp4`
- `已确认`
  - 当前正式云端导出路径：
    - `oss://zvip1-video-beijing/video-factory/final/20260407T194328Z/formal_api_demo.mp4`
- `已确认`
  - 当前正式 review frames：
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/review_frames/contact_sheet.jpg`
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/review_frames/frame_start.jpg`
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/review_frames/frame_middle.jpg`
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/review_frames/frame_end.jpg`

## 当前一句话判断

- 当前这轮已经不再是“sample blocked”；更准确的现状是：
  - 正式 config 迁移已完成
  - 正式样片已完成
  - 自动轮转代码已落成
  - 但当前机器的 TTS / 图片 backup 资源池仍为空

## 当前下一步

- 若下一轮目标是把 auto-rotation 从“代码可用”推进到“资源也真有冗余”，最小动作只有：
  - 在 `/Users/fan/.config/video-factory/formal_api_demo.local.toml` 里补真实可用的：
    - `tts_pool.backup_*`
    - `image_generation_pool.backup_*`
- 当前 example config 已写入新结构示例：
  - `config/formal_api_demo.example.toml`

## 当前工作分支与状态

- 当前工作分支：
  - `codex/provider-auto-rotation`
- 当前状态标签：
  - `task_branch_only`
- 当前必须继续明确：
  - 本轮结果尚未同步回 `codex/user-readable-map`
  - 仓库正式状态仍未更新到主读取分支
