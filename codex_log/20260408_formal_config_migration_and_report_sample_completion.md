# 20260408_formal_config_migration_and_report_sample_completion

## 本轮目标

- 读取当前 resolver 真正认的正式 local config 本体
- 完成“旧配置 -> 新资源池结构”的真实迁移
- 用迁移后的正式 config 直接重跑 `ai_report_fluff_trap_45s`
- 尽量把这轮从 `local preview only` 推进到正式完整片
- 若不能完成，必须把 blocker 收到只剩一个

## 当前工作分支

- `codex/provider-auto-rotation`

## 执行前已确认事实

- `已确认`
  - 当前仓库本地 `skills/` 目录不存在
  - 本轮已检查并实际采用的全局 skill：
    - `brainstorming`
    - `systematic-debugging`
    - `test-driven-development`
    - `verification-before-completion`
- `已确认`
  - 当前 `formal_api_demo` 代码已经具备资源池与 fallback 结构
- `部分成立`
  - repo 内 `config/formal_api_demo.local.toml` 仍是 placeholder
  - 但这不自动等于“当前机器没有真实 formal config”

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `formal_api_demo_core.py`
- `formal_api_demo_cloud_assembly.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`
- `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- `/Users/fan/.config/superpowers/worktrees/视频工厂/codex-formal-api-demo-quality-liveportrait-round1/config/formal_api_demo.local.toml`
- `cases/ai_report_fluff_trap_45s.md`
- `tests/test_formal_api_demo_pipeline.py`
- `tests/test_formal_hybrid_master.py`

## 正式 config 真正路径与现实结论

- `已确认`
  - 当前 resolver 默认正式路径已切到：
    - `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- `已确认`
  - repo 内 legacy 副本：
    - `/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`
  - 当前仍是 placeholder
  - 它不是当前默认正式读取源
- `已确认`
  - 当前 global 官方 config 中存在真实：
    - `auth.api_key`
    - `tts.voice`
    - `tts.model`
    - `tts.api_route_family`
- `已确认`
  - 上一轮“primary 被解析成 placeholder”的根因，不是 parser 本身读不到，而是：
    - 默认路径指到了 repo 内 legacy 占位副本
    - 没有优先使用官方全局 config 源

## 旧配置如何迁移成新结构

- `已确认`
  - 已把正式 local config 迁成：
    - base primary 继续可直接运行
    - 同时补入 pool 结构
- 当前真实迁移结果：
  - `tts_pool.primary`
  - `image_generation_pool.primary`
  - `video_generation_pool.primary`
  - `video_generation_pool.legacy_t2v`
- `已确认`
  - 没有为 TTS / 图片硬造 backup
  - 因为当前真实旧来源里没有第二个可确认的 TTS key / voice，也没有第二个可确认的图片 key / model
- `已确认`
  - 已把旧配置里误开的 portrait 分支关闭：
    - `portrait_detect.enabled = false`
    - `portrait_video_generation.enabled = false`
  - 这样当前样片 generation 不再被未实现真人链路误阻塞

## 迁移后当前 primary / backup

- TTS
  - primary：
    - `Aliyun CosyVoice Primary`
  - backup：
    - `0`
- 图片
  - primary：
    - `Aliyun Image Primary`
  - backup：
    - `0`
- 视频
  - primary：
    - `Aliyun Video Primary`
  - backup：
    - `Legacy T2V Backup`

## 自动轮转当前是否真实可用

- `已确认`
  - 代码层：
    - `可用`
- `部分成立`
  - 当前机器资源层：
    - 只对视频存在真实 backup
    - TTS / 图片还没有真实 backup
- 因此当前准确口径是：
  - `自动轮转机制已真实生效`
  - 但当前机器的资源冗余还不完整

## 实际执行

### 1. config 迁移与 preflight

- 已执行：
  - 读取并比对 repo placeholder config、旧 worktree config、官方 global config
  - 修改 resolver 默认正式路径
  - 修改官方 global config 为新资源池结构
  - 重跑 gate / dry-run 审计

### 2. 正式 generation

- 已执行：
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_fluff_trap_45s.md --out dist/formal_api_demo_ai_report_fluff_trap_45s`
- 实际结果：
  - `generation = success`
  - 真实落出：
    - `manifest.json`
    - `script.txt`
    - `captions.srt`
    - `timeline.json`
    - `visual_generation_plan.json`
    - `tts/formal_voiceover.mp3`
    - `visual/seg01_image.png`
    - `visual/seg02_image.png`
    - `visual/seg03_image.png`
    - `visual/seg04_image.png`

### 3. 正式 assembly

- 已执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo_ai_report_fluff_trap_45s/manifest.json --out dist/formal_api_demo_ai_report_fluff_trap_45s`
- 实际结果：
  - `assembly = success`
  - 真实云端导出信息：
    - `project_id = a139456cf3334509b20192f3203d75bc`
    - `job_id = 010de21131904aedbe8ac582fdad9424`
    - `output_url = oss://zvip1-video-beijing/video-factory/final/20260407T194328Z/formal_api_demo.mp4`

### 4. 正式成片下载与 review_frames

- 已执行：
  - 用当前机器上的 OSS AccessKey 生成签名下载链接
  - 将正式成片下载回本地：
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/final.mp4`
  - 导出正式回审帧：
    - `dist/formal_api_demo_ai_report_fluff_trap_45s/review_frames/*`

## 实际验证

- 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_hybrid_master`
  - `python3 scripts/generate_formal_api_demo.py --input cases/formal_api_demo.md --out dist/_provider_rotation_probe --dry-run`
  - `python3 scripts/generate_formal_api_demo.py --input cases/formal_api_demo.md --out dist/_provider_rotation_realcheck`
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_fluff_trap_45s.md --out dist/formal_api_demo_ai_report_fluff_trap_45s`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo_ai_report_fluff_trap_45s/manifest.json --out dist/formal_api_demo_ai_report_fluff_trap_45s`
  - `node_modules/ffmpeg-static/ffmpeg -i dist/formal_api_demo_ai_report_fluff_trap_45s/final.mp4`
- 验证结果：
  - `已确认`
    - `41` 项测试全部通过
  - `已确认`
    - 当前正式成片本地存在
    - 时长约 `45.00s`
    - 音轨存在
  - `已确认`
    - 当前正式样片不是 local preview 顶替，而是真正 cloud assembly 成片回拉

## 当前结果

- `已确认`
  - 正式 config 迁移已完成
  - 当前 primary 不再被解析成 placeholder
  - `ai_report_fluff_trap_45s` 已补成正式完整片
- `部分成立`
  - 当前代码与当前机器都已能跑通这条样片
  - 但 TTS / 图片 backup 资源池仍为空

## 当前唯一剩余短板

- `已确认`
  - 当前唯一剩余短板不是 sample blocker，而是资源冗余不足：
    - TTS backup = 0
    - 图片 backup = 0
- 这不阻塞当前样片完成
- 但会影响未来“主 key / 主 voice 失效时是否还能自动接着跑”

## 下一步建议

- 若下一轮目标是把当前机器推进到更接近 fully auto-rotation：
  - 只需补真实可用的：
    - `tts_pool.backup_*`
    - `image_generation_pool.backup_*`
- 当前不需要再改样片结构，不需要再回退 local preview
