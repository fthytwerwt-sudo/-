# 20260429｜文案样本视频节奏提取

## 本轮目标

- `已确认` 本轮只做本地 `文案样本` 视频的保真提取与节奏报告。
- `已确认` 不写新文案、不剪视频、不生成新 round。

## 执行前已确认事实

- `已确认` 当前项目仍按《视频工厂》内容质量、结构稳定、可复用执行阶段处理。
- `已确认` 用户要求优先检查 `/Users/fan/Documents/视频工厂/素材录制/文案样本/` 及同义路径。
- `已确认` 用户指定报告输出目录为 `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `GPT 数据源/04_选题与文案规则.md`
- `GPT 数据源/05_文案路由规则.md`
- `GPT 数据源/07_AI知识类视频价值规则.md`
- `project_source/06_project_index.md`
- `/Users/fan/.codex/skills/copywriting-cn/SKILL.md`
- `/Users/fan/.codex/skills/verification-before-completion/SKILL.md`

## 实际改动

- 新增报告目录：
  - `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
- 新增交付文件：
  - `文案样本节奏报告_copy_sample_rhythm_report.md`
  - `文案样本转写_transcript.md`
  - `文案样本结构_segments.json`
  - `run_summary.json`
- 新增中间证据：
  - `intermediate/文案样本_audio_16k_mono.wav`
  - `intermediate/文案样本_contact_sheet_10s_labeled.jpg`
  - `intermediate/frames/`

## 实际执行

- `已确认` 找到视频：`/Users/fan/Documents/视频工厂/素材录制/文案样本.MP4`
- `已确认` 媒体信息：`00:03:40.94`、`1180x2556`、HEVC 视频、AAC 音频。
- `已确认` PATH 中无 `ffmpeg` / `ffprobe`，但仓库 `node_modules/ffmpeg-static/ffmpeg` 可用。
- `已确认` 已抽取音频并生成关键帧 / 联系表。
- `已确认` 未找到可用本地 ASR；macOS `SFSpeechRecognizer` 因 TCC 隐私权限中断。
- `已确认` `segments.json` 和 `run_summary.json` 已通过 `jq` 解析验证。

## 当前结果

- `sample_video_found（样本视频已找到）`
- `blocked_no_asr_available（阻塞：缺少可用转写工具）`
- `sample_structure_extracted（样本结构已提取）`

报告仅基于可见字幕和画面节奏做结构提取，不冒充全量口播转写。

## 状态边界

- `已确认` 未生成新视频。
- `已确认` 未修改原视频。
- `已确认` 未修改 `dist/latest_review_pack`。
- `已确认` 未修改 `content_validation`。
- `已确认` 未修改 `send_ready`。
- `已确认` 未生成最终文案。

## 下一步建议

ChatGPT 可基于本轮报告，把样本的“先结果、再方法词、再案例细节、再低压边界”迁移到《AI 做 PPT 踩坑》正式文案初稿，但必须继续保留“不是最终验收稿、不可直接发布”的边界。
