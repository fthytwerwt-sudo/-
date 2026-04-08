# Latest

## 当前主结论

- `已确认` 2026-04-08 已用用户本地 `素材录制/` 下 3 段真实 `.mov` 素材，按固定选题《为什么你明明用了 AI 写汇报，最后还是得自己重写一遍？》跑完一次正式北京区 `OSS + 云剪 cloud-only` 样片。
- `已确认` 本轮新增专用 case：
  - `cases/ai_report_rewrite_trap_50s.md`
- `已确认` 本轮正式云端导出成功：
  - 本地回拉成片：`dist/formal_api_demo/final.mp4`
  - 云端输出：`oss://zvip1-video-beijing/video-factory/final/20260408T134055Z/formal_api_demo.mp4`
  - 视频时长：`50.00s`
  - 分辨率：`1080x1920`
  - 音轨：AAC
- `已确认` 本轮修复了一个 cloud assembly timeline bug：
  - 云剪视觉主轨 clip 不应把全局段落时间写入 `TimelineIn / TimelineOut`
  - 视频 clip 改用 `In / MaxOut` 控制素材内裁剪
  - 图片 clip 改用 `Duration` 控制停留时长
  - 该问题已用回归测试锁住

## 当前素材层判断

- `已确认` 实际检查到的 3 段素材是：
  - `素材录制/1.mov`：约 `39.38s`
  - `素材录制/2.mov`：约 `49.28s`
  - `素材录制/3.mov`：约 `38.20s`
- `已确认` 3 段素材均为 HEVC + AAC、`3366x2180`，且都可被项目内 `ffmpeg-static` 读取。
- `部分成立` 本轮素材全部更像真实屏幕录制 / ChatGPT 工作流录制，不是明显可见真人半身口播。
- `已确认` 本轮路由采用：
  - `hook_human` → `1.mov`
  - `process_self_footage` → `2.mov`
  - `result_card` → 本地生成的结果卡 PNG
  - `close_human` → `3.mov`
- `部分成立` 该路由能跑通正式云端链路，但 hook / close 画面并不满足“可见真人承担信任 / 判断 / 收束”的质量口径，不得写成 90 分水位已通过。

## 当前本地配置状态

- `已确认` 本轮写入的正式本地配置源是：
  - `~/.config/video-factory/formal_api_demo.local.toml`
- `已确认` 本地配置新增 / 更新了：
  - `[footage_inputs.hook_human]`
  - `[footage_inputs.process_self_footage]`
  - `[footage_inputs.result_card]`
  - `[footage_inputs.close_human]`
  - `[tts].speech_rate = 1.0`
- `local_only` 该本地配置包含密钥或本机路径，不进入 GitHub。

## 当前验证结果

- `已确认` 已执行：
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_rewrite_trap_50s.md --out dist/formal_api_demo --dry-run`
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_rewrite_trap_50s.md --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
  - `node_modules/ffmpeg-static/ffmpeg -hide_banner -i dist/formal_api_demo/final.mp4`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_hybrid_master`
- `已确认` 单测结果：
  - `44` tests passed
- `已确认` 回审帧已导出到：
  - `dist/formal_api_demo/review_frames/`

## 当前接手时建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_log/20260408_ai_report_rewrite_trap_50s_real_footage_cloud_sample.md`
5. `cases/ai_report_rewrite_trap_50s.md`
6. `formal_api_demo_cloud_assembly.py`
7. `tests/test_formal_api_demo_pipeline.py`
8. 若继续跑本机样片，再检查 `~/.config/video-factory/formal_api_demo.local.toml`

## 当前工作分支与状态

- 当前工作分支：
  - `codex/provider-auto-rotation`
- 当前状态标签：
  - `task_branch_only`
- 当前必须继续明确：
  - 本轮结果尚未同步回 `codex/user-readable-map`
  - 仓库正式状态仍未更新到主读取分支
  - `dist/formal_api_demo/*` 和本地配置均为 `local_only`
