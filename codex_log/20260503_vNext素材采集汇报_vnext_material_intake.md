# 20260503 vNext 最新素材采集汇报

## 1. 本轮范围

- `已确认` 本轮工作区：`/Users/fan/Documents/视频工厂`
- `已确认` 本轮分支：`codex/vnext-recorded-material-intake-20260503`
- `已确认` 本轮只扫描：`/Users/fan/Documents/视频工厂/素材录制/最新素材`
- `已确认` 本轮只做素材采集汇报，不剪视频、不生成样片、不调用阿里云、不改 v3.1 正片。

## 2. 读取与工具

- `已确认` 已读取 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_log/latest.md`、`GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`、HyperFrames 卡片边界报告、阿里云剪辑复接验证报告和 `codex_log/current_local_artifact_paths.md`。
- `已确认` 仓库本地 `skills/` 不存在。
- `已确认` 已使用全局 `video-metadata-probe` skill。

## 3. 素材发现结果

- `已确认` 指定目录存在。
- `已确认` 目录下共 7 个文件，其中 6 个候选素材，`.DS_Store` 已忽略。
- `已确认` 5 个 2026-05-02 晚间修改的 mp4 文件可作为本轮新录制素材候选：
  - `codex 素材.mp4`
  - `trae 素材.mp4`
  - `创建文件夹.mp4`
  - `豆包素材.mp4`
  - `火山引擎素材.mp4`
- `部分成立` `录屏2026-04-30 03.25.28.mov` 位于最新素材目录，但修改时间较旧、时长 106 分钟且无音轨，默认只列为历史 / 参考候选，待用户确认。

## 4. 技术检查

- `已确认` 5 个 mp4 均通过 ffprobe 元数据读取和 ffmpeg 全片解码检查。
- `部分成立` 106 分钟 `.mov` 已通过开头 / 中段 / 末段抽样解码，未做全片完整解码；报告中不得写成完整全片技术验证通过。
- `已确认` 最新目录未发现独立 mp3 / wav / aac 音轨文件。
- `已确认` 最新目录未发现可直接当卡片素材的 png / jpg / json / srt 文件。

## 5. 推荐组合

- `user_recording_segment`：推荐 `trae 素材.mp4` 的 `120.0s-136.0s`。
- `card_segment_1`：最新目录缺卡片文件；后续若允许生成占位卡，建议 `cute_info_card_route`，4 秒。
- `card_segment_2`：最新目录缺骚萌卡文件；后续若允许生成占位卡，建议 `sassy_reaction_card_route`，4 秒。
- `audio_segment`：最新目录缺独立音轨；可用静音占位做最小云剪总装技术验证。

## 6. 风险

- `已确认` `火山引擎素材.mp4` 出现手机号、短信验证码、API Key 管理页和资源 ID 痕迹；未打码不得入片。
- `已确认` `codex 素材.mp4` 可见 Git / 文件变更列表，正式使用前需控制内部路径和文件名展示边界。
- `已确认` 本轮素材检查不能写成内容验证通过，不能写成云端总装链路稳定。

## 7. 输出文件

- `素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/vNext素材采集汇报_vnext_material_intake_report.md`
- `素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/material_inventory.json`
- `素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/recommended_assembly_inputs.json`
- `素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/chatgpt_review_input.md`

## 8. 状态边界

- `已确认` 未生成可交付视频 / 音频 / 图片。
- `已确认` 未修改 v3.1 正片。
- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改 `content_validation` / `send_ready`。
- `已确认` 不提交新录制素材本体、大视频、大图片、大音频。

## 9. 下一个目标

交给 ChatGPT 判断素材是否足够进入 vNext 最小云端总装验证；如果足够，再由后续阿里云云端总装验证任务读取 `recommended_assembly_inputs.json`。
