# 20260531 Remotion / FFmpeg / ASS / 阿里 API 剪辑工具链审计

- `task_result.status = toolchain_audit_completed_no_video_no_api`
- `target_delivery = local_toolchain_audit + tool_routing_decision + installation_recommendation + next_30_to_45s_validation_plan`
- `已确认` 本轮只审计本地 / 仓库工具链，不生成视频、不修改当前正片、不调用阿里 / 图片 / 视频 / TTS / 外部 API，不读取 `.env`、API key、token 或 secret，不安装依赖。
- `已确认` Remotion 当前未安装、不可直接运行：`node = v25.6.1`、`npm = 11.9.0`、`pnpm = missing`、`node_modules = missing`、`npm list remotion = empty`、`npm list '@remotion/*' = empty`、`npx --no-install remotion --version` 失败。
- `已确认` 仓库根 `package.json` 当前只声明 `ffmpeg-static`；未发现 `remotion.config.*`、根 `src/`、根 `remotion/` 或 `scripts/*remotion*`。
- `已确认` FFmpeg / FFprobe 本机可用：`/opt/homebrew/bin/ffmpeg`、`/opt/homebrew/bin/ffprobe`，版本均为 `8.1`。
- `部分成立` FFmpeg 可用于 probe、抽帧、裁剪、转码、重封装、mux；但当前未发现 `libass`、`ass` filter 或 `subtitles` filter，ASS burn-in 不可写成可用。
- `已确认` Python 为 `3.9.6`；`Pillow 11.3.0` 可用；`cv2 / numpy / pysubs2 / cairosvg` 缺失。
- `工具路由判断`：下一轮 `guided proof video` 首选 Remotion 做 16:9 composition、evidence container、labels、highlights、split screen、bridge card 和字幕安全区；FFmpeg 做媒体 probe / mux / trim / transcode；ASS 暂不作为首选，除非先补 libass；Python 需补视觉库后再做帧级辅助。
- `阿里 API 素材判断`：只允许做开头 / 转场 / 结尾的非证据辅助素材、小向导、背景、图标或氛围图；不得替代用户录屏、Prompt / 表格 / 按钮 / 聊天证据或真实平台数据。
- `下一步建议`：用户确认安装后，先补 Remotion 最小栈并跑 still / 5 秒片段验证，再进入 30-45 秒 `guided proof` 片段；若要 ASS burn-in，先切换带 `--enable-libass` 的 FFmpeg 并复验 filter。
- `状态边界`：未推进 `content_validation / send_ready / publish_status / voice_validation / final_voice_validated / visual_master_locked`；未生成视频、未改音频、未改素材、未改当前 review pack。
- `报告`：`codex_log/toolchain_audit/20260531_Remotion_FFmpeg_ASS_阿里API剪辑工具链审计_remotion_ffmpeg_ass_aliyun_toolchain_audit/toolchain_audit_report.md`
- `manifest`：`codex_log/toolchain_audit/20260531_Remotion_FFmpeg_ASS_阿里API剪辑工具链审计_remotion_ffmpeg_ass_aliyun_toolchain_audit/audit_manifest.json`
- `供料任务卡`：`codex_log/supply_requests/20260531_remotion_ffmpeg_ass_aliyun_toolchain_audit_pre_supply_request.json`
