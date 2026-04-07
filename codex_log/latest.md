# Latest

## 当前主结论

- 2026-04-08 已把 `formal_api_demo` 的 provider / key / voice 治理升级成“资源池 + 自动切换”结构：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
- 当前正式 local config 已被正确读到：
  - `has_local_config = true`
- 但按当前代码真实读取结果，本机 formal local config 当前只读到：
  - `tts_candidate_total = 1`
  - `tts_candidate_available = 0`
  - `image_candidate_total = 1`
  - `image_candidate_available = 0`
  - `video_candidate_total = 1`
  - `video_candidate_available = 0`
- 当前最关键的现实结论不是“代码读不到 config”，而是：
  - 当前 formal local config 里没有任何 `tts_pool / image_generation_pool / video_generation_pool` 备用候选
  - 当前 primary TTS 候选仍被解析成 placeholder：
    - `auth.api_key`
    - `tts.voice`
- 这与“本地正式 config 已经填好”的口头预期存在冲突；执行层必须以当前文件真实读取结果为准

## 现有自动切换逻辑的真实审计结论

- `已确认`
  - 旧逻辑已存在的只有：
    - TTS `route family` 选择
    - TTS style probe 候选
    - 普通图片 / 视频 provider implementation 路由
  - 旧逻辑缺少的关键部分包括：
    - 真正的运行时 key / voice / provider 候选池
    - 失败后自动切换到备用项
    - 候选链 preflight
    - 自动切换事件日志
- `已确认`
  - 真人分支目前仍只有：
    - `liveportrait-detect -> liveportrait` 路线语义
  - 真实 provider implementation 仍未接入
  - 因此本轮没有把“真人自动切换”伪装成已完成能力

## 本轮新增 / 修正的 fallback 机制

- `已确认`
  - parser 已支持 dotted section：
    - `[tts_pool.<candidate_id>]`
    - `[image_generation_pool.<candidate_id>]`
    - `[video_generation_pool.<candidate_id>]`
- `已确认`
  - preflight / gate 已升级为候选链检查，不再只看单个 primary
- `已确认`
  - TTS 已支持真实运行时 fallback：
    - auth failed
    - quota exhausted / 429
    - voice unavailable
    - timeout / upstream unavailable
    - model / endpoint / resource invalid
- `已确认`
  - 图片生成已支持真实运行时 fallback：
    - auth failed
    - quota exhausted / 429
    - timeout / upstream unavailable
    - candidate invalid
- `已确认`
  - 视频生成已接入同一套候选池与 fallback 执行器
- `已确认`
  - 自动切换痕迹已回写到：
    - `manifest.json`
    - `visual_generation_plan.json`
    - `result_summary.json`

## 当前本机真实状态

- 代码能力状态：
  - `partial_auto_rotation`
- 当前本机资源状态：
  - `blocked_by_no_backup_resources`
- 原因：
  - 代码已经能轮转已有资源池
  - 但当前本机 formal local config 里没有任何备用候选
  - 且 primary TTS 候选本身仍不可用
- 必须明确：
  - 系统现在可以“自动轮转已有资源”
  - 但不能“凭空自动获得新 key”

## 当前下一步

- 若要让这台机器真正进入接近 `auto_rotation_ready` 的状态，最小动作不是再改代码，而是：
  - 在 `config/formal_api_demo.local.toml` 中补至少 1 组真实可用的候补资源池
  - 例如：
    - `tts_pool.backup_*`
    - `image_generation_pool.backup_*`
    - `video_generation_pool.backup_*`
- 当前 example config 已写入新结构说明：
  - `config/formal_api_demo.example.toml`

## 当前工作分支与状态

- 当前工作分支：
  - `codex/provider-auto-rotation`
- 当前状态标签：
  - `task_branch_only`
- 当前必须继续明确：
  - 本轮结果尚未同步回 `codex/user-readable-map`
  - 仓库正式状态仍未更新到主读取分支
