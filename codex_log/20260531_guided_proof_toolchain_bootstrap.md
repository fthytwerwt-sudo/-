# 20260531 Guided Proof Video 剪辑工具链补齐

- `task_result.status = completed_toolchain_bootstrap_synced`
- `target_delivery = remotion_minimal_project + python_visual_toolchain + self_check_script + still_render + 5s_render + toolchain_status_json`
- `已确认` 本轮只补本地工具链和生成内部验证产物，不修改当前正片、不生成正式发布候选片、不调用阿里 / 图片 / 视频 / TTS 外部 API、不读取 `.env`、API key、token 或 secret。
- `已确认` macOS / Node 满足 Remotion 当前官方最低要求：`macOS 26.2`、`node v25.6.1`、`npm 11.9.0`；`pnpm` 仍缺失但不阻断 npm 路线。
- `已安装` Node 依赖：`@remotion/cli / @remotion/captions / @remotion/media / @remotion/renderer / remotion = 4.0.469`，`react / react-dom = 19.2.6`。
- `已保留` 既有 `ffmpeg-static` 依赖和 `check` script；`package.json` 本轮只做最小增量。
- `已安装` Python 视觉依赖：`numpy 2.0.2`、`opencv-python 4.13.0.92`、`pysubs2 1.8.1`、`cairosvg 2.8.2`、`pillow 11.3.0`；另通过 Homebrew 安装 `cairo 1.18.4` 供 CairoSVG runtime 使用。
- `已新增` Remotion 最小 composition：`remotion/index.tsx`、`remotion/Root.tsx`、`remotion/GuidedProofToolchain.tsx`，覆盖 `dark_or_neutral_matte / clean_evidence_container / subtitle_safe_zone / one_claim_one_highlight / split_screen_placeholder / low_density_bridge_card`。
- `已新增` 自检入口：`scripts/视频剪辑工具链自检_check_guided_proof_toolchain.py`；重复安装入口：`scripts/视频剪辑工具链安装_bootstrap_guided_proof_toolchain.sh`。
- `验证通过` `npm run vf:remotion:still`，输出 `dist/toolchain_validation/remotion_still.png`。
- `验证通过` `npm run vf:remotion:render5s`，输出 `dist/toolchain_validation/remotion_5s.mp4`。
- `验证通过` `npm run vf:toolchain:check`，输出 `dist/toolchain_validation/toolchain_status.json`，其中 `minimum_guided_proof_ready = true`、`remotion_ready = true`、`ffmpeg_ready = true`、`python_visual_ready = true`。
- `ASS 边界`：`ass_ready = false`；当前 FFmpeg 未检测到 `libass`、`ass` 或 `subtitles` filter；本轮明确写为 `fallback_only_not_primary`，不阻断 Remotion caption layer 主路线。
- `ffprobe` 5 秒片段通过：`1920x1080 / 30fps / h264 / aac / duration 5.056s`。
- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`。
- `报告`：`codex_log/toolchain_bootstrap/20260531_guided_proof_toolchain_bootstrap_report.md`
- `验证产物`：`dist/toolchain_validation/remotion_still.png`、`dist/toolchain_validation/remotion_5s.mp4`、`dist/toolchain_validation/toolchain_status.json`
