# Latest

## 20260428｜方案 B V3 骚萌表情迭代技术预览

- `已确认` 本轮只改方案 B V3 独立反应片段的角色表情与动作气质；未重做路线，未回退本地绘图，未改正式正片。
- `已确认` 继续显式复用历史成功配置 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`，脱敏 preflight 通过：`provider = aliyun_bailian`，`region = cn-beijing`，key 存在且为 `sk_dashscope_like / 20-39`。
- `已确认` 已生成 2 张骚萌表情候选图：A 版为挑眉 wink + 捂嘴偷笑，B 版为吐舌 + 歪头；候选对比图为 `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌候选对比_contact_sheet.jpg`。
- `已确认` 选中 A 版进入 i2v：A 版更接近贱萌得瑟，且不低幼、不暧昧、胸口无 `AI`；B 版吐舌更强但略偏低幼 / 暧昧。
- `已确认` `wan2.7-i2v` 已生成骚萌独立 reaction clip：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_骚萌_reaction_clip.mp4`，`1.52s / 720x1280`。
- `已确认` 已装配 15 秒骚萌版技术预览：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_scheme_b_standalone_reaction_v3_sassy_cute.mp4`，结构仍为 `round34 录屏片段 A -> 骚萌独立 reaction clip -> round34 录屏片段 B`，不是 overlay compositing。
- `已确认` 本轮未泄露 key、未提交本地私有配置、未本地绘图兜底、未改正式 `full.mp4`、未改 `dist/latest_review_pack/`、未改 `content_validation`、未改 `send_ready`。
- `待验证` 本轮只是 `technical_preview_generated_content_pending`，仍待 ChatGPT / 用户复审“骚萌表情、GIF 感、插入节奏、是否能进入正式方案”；不代表方案 B 最终口径。

## 20260428｜方案 B V3 复用历史配置生成独立反应预览

- `已确认` 本轮显式复用历史成功配置 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`，脱敏 preflight 通过：`provider = aliyun_bailian`，`region = cn-beijing`，key 存在且为 `sk_dashscope_like / 20-39`。
- `已确认` `wan2.7-image-pro` 已成功生成整页 reaction page：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_static_reaction_page.png`。
- `已确认` `wan2.7-i2v` 已成功生成独立 reaction clip，并裁剪为 `1.52s / 720x1280`：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_reaction_clip.mp4`。
- `已确认` 已装配 15 秒技术预览：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_scheme_b_standalone_reaction_v3.mp4`，结构为 `round34 录屏片段 A -> 独立 reaction clip -> round34 录屏片段 B`，不是 overlay compositing。
- `已确认` 已生成 contact sheet 与 before / after contact sheet；已写 `run_summary.json` 与 `方案B独立反应V3说明_preview_report.md`。
- `已确认` 本轮未泄露 key、未提交本地私有配置、未本地绘图兜底、未改正式 `full.mp4`、未改 `dist/latest_review_pack/`、未改 `content_validation`、未改 `send_ready`。
- `待验证` 本轮只是 `technical_preview_generated`，仍待 ChatGPT / 用户复审画质、表情、节奏和是否可进入正式方案；不代表方案 B 最终口径。

## 20260428｜方案 B V3 阿里历史生成链路审计

- `已确认` 本轮只做阿里 / 百炼 / DashScope 图像与视频生成链路审计；未重新生成 V3 图 / 视频。
- `已确认` 历史成功链路存在：正式 API demo 曾用 `wan2.6-image` / `liveportrait` 生成开头、结尾、辅助视觉；元素娃娃 round3 / round4 / round5 曾用 `wan2.7-image-pro` 成功生成主持娃娃图像。
- `已确认` round5 还成功跑通过 `wan2.2-s2v-detect` 与 `wan2.2-s2v` 最短 smoke test。
- `已确认` 历史 round3 / round4 / round5 的成功配置来源指向 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- `已确认` V3 `run_summary.json` 记录的配置来源是 `/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`，并在 `wan2.7-image-pro` / `wan2.7-image` 创建阶段返回 `HTTP401 / InvalidApiKey`。
- `已确认` 当前脱敏复查中，`/Users/fan/.config/video-factory/formal_api_demo.local.toml` 有 `sk-` 形态 DashScope key；`/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml` 当前未呈现为可用 DashScope `auth.api_key`。
- `已确认` 最可能主因不是“用户没配 API”，而是 V3 没有复用历史成功的配置来源 / key 来源，跑到了 legacy config 或 stale key source。
- `已确认` 新增审计报告：
  - `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/历史生成链路审计_history_generation_path_audit.md`
  - `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/history_generation_path_audit_summary.json`
  - `codex_log/20260428_方案B_V3_历史生成链路审计.md`
- `已确认` 本轮未改 key、未生成 V3、未改 `full.mp4`、未改 `dist/latest_review_pack/`、未改 `content_validation`、未改 `send_ready`。
- `待验证` 下一轮若继续 V3，应先显式复用 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`；若仍 401，再补齐支持万相图像 + 图生视频的百炼 / DashScope key。

## 20260427｜中段吐槽插入风格视觉证据补齐

- `已确认` 本轮只是补齐上一轮 reference pack 的轻量视觉证据，用于待 ChatGPT / 用户复审。
- `已确认` 本轮新增 / 同步视觉证据：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_关键帧联系表_keyframes_contact_sheet.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_吐槽三连帧_punchline_triptych.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第一次吐槽前后_context_01.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第二次吐槽前后_context_02.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第三次吐槽前后_context_03.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_GIF式吐槽动态预览_visual_punchline_preview.mp4`
- `已确认` 本轮新增报告：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/画面层保真补充_visual_punchline_report.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据补齐_run_summary.json`
- `待验证` GIF 式吐槽画面层仍待 ChatGPT / 用户复审；本轮不代表最终口径。
- `已确认` 本轮不改视频，不生成新 round，不替换音轨，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不改变 `content_validation（内容验证）`，不改变 `send_ready（可发送状态）`。
- `已确认` 本轮不修改 `GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/08_当前正式事实.md`。
- `已确认` 原始 50MB MP4、完整 `frames/` 目录、音频副本与波形图未提交；本轮只提交筛选后的轻量视觉证据。

## 20260427｜中段吐槽插入风格参考包同步

- `已确认` 本轮只是把上一轮本地“中段吐槽插入风格高保真提取”文本 reference_pack 同步到 `codex/user-readable-map`，用于待 ChatGPT / 用户复审。
- `已确认` 本轮新增 / 同步文本报告路径：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/素材清单_assets_inventory.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio_reference_note.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/scene_index.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/吐槽插入风格_reference_pack.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/给ChatGPT的素材汇报_material_report.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/run_summary.json`
- `已确认` 本轮同步源来自上一轮本地分析包：`/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`。
- `已确认` 上一轮本地分析包生成于 `fix/no-zoom-completeness-layout`，不是主读取分支；本轮已在 `codex/user-readable-map` 重新同步文本报告。
- `已确认` 上一轮存在路径漂移风险：上一轮分支中无空格 `GPT数据源/` 缺失，只读到 `GPT 数据源/`；本轮已在 `codex/user-readable-map` 读取无空格 `GPT数据源/` 当前执行包。
- `待验证` 吐槽插入风格仍待 ChatGPT / 用户复审；本轮不代表最终口径。
- `已确认` 本轮不写入正式风格规则，不改视频，不生成新 round，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不改变 `content_validation`，不改变 `send_ready`。
- `已确认` 本轮未提交二进制证据文件：`keyframes_contact_sheet.jpg`、`audio/reference_audio.m4a`、`audio_waveform.png`、`frames/`；本轮只同步 Markdown / JSON 文本报告。

## 20260427｜文案生产流程与 B 版声音口径固化

- `已确认` 本轮只做《视频工厂》文案生产流程、最终风格锚点、声音 B 版暂定口径的规则落仓库；未生成新音频、新视频，未修改现有样片，未替换全片音轨。
- `已确认` 已在 `GPT数据源/04_选题与文案规则.md（当前文案规则）` 写入后续默认文案生产流程：`Perplexity（外部参考检索 / 研究工具）` 输出 `reference pack（参考包）` 与 `raw feeling draft（原感初稿）` -> 用户录制素材 -> `Codex（执行代理）` 做素材技术检查与细节证据报告 -> `ChatGPT（最终落稿与复审入口）` 写最终落稿 -> `Codex（执行代理）` 按最终稿执行。
- `已确认` 已明确 `Perplexity（外部参考检索 / 研究工具）` 只负责参考包 / 原感初稿，不是最终稿；不得直接进入执行。
- `已确认` 已在 `GPT数据源/05_文案路由规则.md（当前文案路由）` 写入 `Codex（执行代理）` 素材细节汇报标准：不能只报“素材存在 / 技术通过”，必须写清素材里有什么、在哪一秒、发生了什么、能证明什么，并给 `ChatGPT（最终落稿与复审入口）` 可写稿的细节。
- `已确认` 已在 `GPT数据源/07_AI知识类视频价值规则.md（当前价值规则）` 写入最终稿细节标准：最终稿必须尽量具体到真实工具 / 网站、页面、按钮、输入动作、生成结果、前后对比、失败点和下一步怎么做。
- `已确认` 已在 `GPT数据源/04_选题与文案规则.md（当前文案规则）` 写入最终文案风格锚点：用户确认的“用字更自然版长稿” + 20260427 B 版“停顿梗感”试听方向；风格为微反转、说话带梗、自然口语、生活观察起手、轻吐槽、避免 AI 感硬词，不写课程腔 / 广告腔 / 鸡血腔。
- `已确认` 已在 `GPT数据源/08_当前正式事实.md（当前正式事实）` 写入当前声音暂定口径：用户更喜欢 20260427 B 版“停顿梗感”方向；新样本2 `custom voice（自定义音色）` 脱敏标识 `qwen-t...ac19` 可继续作为当前声音底子。
- `已确认` 后续声音主要调 `speech_pacing（语速节奏）`、`pause_timing（停顿位置）`、`copy_fit（文案搭配）`；暂不优先重做 `voice cloning（声音复刻）`，暂不优先换音色。
- `待验证` B 版只是当前优先试听方向，不是最终成片音轨，不能写最终音色已定，不能写 `voice_validation_status（声音验证状态） = 通过`。
- `已确认` 未修改 `GPT 数据源/（GPT Project 协作规则包）`，未把 B 版暂定声音这种动态状态写入静态协作包。
- `已确认` 新增日志：`codex_log/20260427_文案生产流程与B版声音口径固化.md（本轮日期日志）`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260427｜十五秒文案语速停顿试配

- `已确认` 本轮只做《视频工厂》声音文案适配试听；未换音色、未重做 voice cloning、未重新裁剪 / 上传样本、未替换全片音轨。
- `已确认` 用户本轮确认方向已记录：新样本2音色底子可以继续用，后续主要调语速、停顿和文案搭配；偏好“微反转 + 说话带梗 + 自然口语”；需避免类似“下一步从哪打”的 AI 感硬词。
- `已确认` 使用新样本2 custom voice：`qwen-t...ac19`（脱敏）；`model / target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 本轮只通过 custom voice list 解析既有 voice，未重新 `create_custom_voice`；未使用 Serena；未使用上一轮 A / B custom voice。
- `已确认` 新增输出目录：`dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`。
- `已确认` A 版文案为自然节奏，去空白字数 `93`；B 版文案为停顿梗感，去空白字数 `97`；两版均未命中本轮禁用硬词。
- `已确认` 已生成 A / B 两条声音试听：
  - A：`A_15秒文案_自然节奏.wav`，`17.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.9 dB / loudnorm.input_i -23.92 LUFS`
  - B：`B_15秒文案_停顿梗感.wav`，`16.32s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.4 dB / loudnorm.input_i -23.67 LUFS`
- `已确认` A / B 均可被 `ffmpeg` 解码，且时长均在 13-18 秒范围内。
- `已确认` A / B API 原始输出已在目标范围内，本轮未使用 `atempo`。
- `已确认` 脱敏请求、音频验证与运行摘要已落盘：`A_voice_clone_tts_request_debug_sanitized.json`、`B_voice_clone_tts_request_debug_sanitized.json`、`A_ffmpeg_decode_check.txt`、`B_ffmpeg_decode_check.txt`、`A_volumedetect.txt`、`B_volumedetect.txt`、`A_loudnorm_measure.txt`、`B_loudnorm_measure.txt`、`run_summary.json`。
- `已确认` 新增日志：`codex_log/20260427_十五秒文案语速停顿试配.md`。
- `待验证` 本轮只证明 `technical_generation` 通过；A / B 的语速、停顿、轻吐槽和文案搭配是否合适，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜语音样本2复刻与文案风格解析

- `已确认` 本轮重开新语音样本链路，未沿用上一轮 A / B 声音试配结果；上一轮 A / B 只保留为失败参考。
- `已确认` 已定位用户新样本：`/Users/fan/Documents/视频工厂/素材录制/语音样本 2.MP4`，候选数量为 `1`，未回退使用旧样本。
- `已确认` 新样本只读解析：`23.16s / mov,mp4,m4a,3gp,3g2,mj2 / hevc / aac / 44100 Hz / stereo / mean_volume -13.3 dB / loudnorm.input_i -10.26 LUFS`。
- `已确认` 已生成分析副本与复刻输入：
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_分析副本.m4a`
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
- `已确认` 复刻输入样本为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`，从原 MP4 `2.0s` 起连续裁剪。
- `已确认` 已用新样本创建新的测试 custom voice，脱敏标识：`qwen-t...ac19`；`model = qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`，`preferred_name = vfsample20426`。
- `已确认` 已生成 1 条新样本声音复刻试听 trial：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`。
- `已确认` 试听 trial 可被 `ffmpeg` 解码：`13.60s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.8 dB / loudnorm.input_i -23.72 LUFS`。
- `已确认` 已尝试并完成完整 MP4 自动 ASR 转写，模型为 `paraformer-realtime-v2`；转写文件：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写文本_transcript.md`。
- `待验证` 自动转写尚未人工校对，可能存在误识别；文案风格记录只能作为本轮 reference style，不能写成唯一标准风格。
- `已确认` 已新增高保真文案风格记录：`codex_log/20260426_语音样本2_文案风格高保真记录.md`。
- `已确认` 已新增音频参考报告：`codex_log/20260426_语音样本2_audio_reference_report.md`。
- `已确认` 已新增执行日志：`codex_log/20260426_语音样本2复刻与文案风格解析.md`。
- `已确认` 已新增本轮脚本：`scripts/语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis.py`。
- `待验证` 本轮只证明 `technical_generation` 通过；`voice_validation_status` 仍为待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜台湾口语开心降噪声音第二轮试配

- `已确认` 本轮只生成《视频工厂》声音第二轮最小对照 trial；未修改视频、未替换全片音轨、未生成新视频 round。
- `已确认` 用户本轮听感反馈已保真记录：
  1. 情绪上面还不够开心的那种。
  2. 需要把口语改成台湾的口音。
  3. 现在生成的环境音有点吵，需要降噪。
- `已确认` 新增本轮输出目录：`dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`。
- `已确认` A 版沿用当前 custom voice（脱敏：`qwen-t...de43`），使用台湾口语文本 + 开心轻快 instructions 生成，并保留：
  - `A_沿用音色_台湾口语开心_API原始_未节奏校准.wav`
  - `A_沿用音色_台湾口语开心_原始.wav`
  - `A_沿用音色_台湾口语开心_轻降噪.wav`
- `已确认` B 版先对复刻输入样本做轻降噪，再重新创建测试 custom voice（脱敏：`qwen-t...bb3b`），使用同一文本 + 同一 instructions 生成，并保留：
  - `B_复刻输入样本_轻降噪.wav`
  - `B_重建音色_台湾口语开心_API原始_未节奏校准.wav`
  - `B_重建音色_台湾口语开心_原始.wav`
  - `B_重建音色_台湾口语开心_轻降噪.wav`
- `已确认` 因固定文案较长，API 直出分别为 `17.60s` / `16.56s`；本轮保留 API 直出审计文件，同时用 `atempo` 生成 10-15 秒未降噪节奏校准版。
- `已确认` 四个正式对照输出均可被 `ffmpeg` 解码：
  - A 原始：`14.18s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.8 dB / loudnorm.input_i -22.13 LUFS`
  - A 轻降噪：`14.18s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.3 dB / loudnorm.input_i -22.64 LUFS`
  - B 原始：`14.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.4 dB / loudnorm.input_i -22.40 LUFS`
  - B 轻降噪：`14.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.7 dB / loudnorm.input_i -22.65 LUFS`
- `已确认` 脱敏请求与验证记录已落盘：`custom_voice_list_debug_sanitized.json`、`A_voice_clone_tts_request_debug_sanitized.json`、`B_重建音色_create_custom_voice_request_debug_sanitized.json`、`B_voice_clone_tts_request_debug_sanitized.json`、`run_summary.json`。
- `已确认` 新增脚本：`scripts/声音第二轮台湾口语开心降噪_trial_round2.py`。
- `已确认` 新增日志：`codex_log/20260426_台湾口语开心降噪声音试配.md`。
- `待验证` 本轮只证明 `technical_generation` 通过；A / B 是否更开心、是否像台湾口语、降噪后是否仍自然，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜GPT Project 协作规则包更新

- `已确认` 本轮只更新 `GPT 数据源/`，将其定位改为 GPT Project 协作规则包；它只负责告诉 ChatGPT 如何协作、如何读 GitHub、如何处理冲突，不再承载动态当前事实。
- `已确认` 当前项目事实和执行状态的主事实源仍是 GitHub 当前文件；当前 round、`latest_review_pack`、`content_validation`、`send_ready`、声音试配状态都必须从 GitHub 当前文件读取。
- `已确认` 本轮在 `codex/user-readable-map` worktree 中新增并跟踪 `GPT 数据源/` 10 份文件；未修改 `GPT数据源/` 当前 10 份执行包。
- `已确认` `GPT 数据源/08_当前正式事实.md` 未纳入新包；新第 8 份文件为 `GPT 数据源/08_当前事实读取规则.md`，专门记录当前事实读取顺序和冲突裁决。
- `已确认` 本轮未修改视频、音频、图片、原始素材、生成脚本、测试脚本、`dist/latest_review_pack/*` 或 `dist/voice_trials/*`。
- `已确认` 本轮不改变当前视频与声音状态；声音试配和全片内容复审仍以 GitHub 当前文件为准。
- `下一个目标`：后续 ChatGPT 先按 `GPT 数据源/` 协作规则接手，再从 GitHub 当前文件读取项目事实。

## 20260426｜下一个目标与中文英文命名规则补丁

- `已确认` 本轮只做规则补丁，不做目录迁移，不执行 `git mv`，不重命名任何已有文件或文件夹。
- `已确认` 执行位置已校准到主读取分支 worktree：`/private/tmp/视频工厂_user_readable_map_sync`，当前分支为 `codex/user-readable-map`。
- `已确认` 已写入最终汇报和交接口径：最后一栏统一使用“下一个目标”，不再默认使用“下一步行动建议”。
- `已确认` 已写入新增业务文件 / 业务文件夹命名规则：默认使用“中文 + 英文”，推荐格式为 `中文名_english_name`。
- `已确认` 已有文件和已有文件夹本轮不追溯改名；工具链强制英文名保留为例外，且例外不得扩大到普通业务目录和业务文件。
- `已确认` 本轮不修改视频、音频、图片、原始素材、生成脚本或测试脚本。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 提交前本地验证已通过；远端同步状态以本轮收尾的 `git show origin/codex/user-readable-map:路径` 复读验证为准。

## 20260426｜round28 声音复刻试配继续执行

- `已确认` 本轮继续上轮被阿里百炼 `Arrearage` 阻塞的 voice cloning（声音复刻）路线；不重回 `Serena` 系统音色，不修改视频，不替换全片音轨，不生成新视频 round。
- `已确认` 复用上轮合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数仍为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 阿里账户本轮不再返回 `Arrearage`；用户 prompt 指定的 `vf_r28_clone_20260426` 因超过官方 `preferred_name` 16 字符限制返回 `InvalidParameter`，已按官方约束改用 `vfr28clone0426`。
- `已确认` 已创建测试 custom voice，脱敏标识：`qwen-t...de43`；创建模型为 `qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 已使用该 custom voice 生成 1 条 round28 声音复刻 trial：`dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`。
- `已确认` 输出音频验证：`12.96s / wav / pcm_s16le / 24000 Hz / mono / 622124 bytes`，可被 `ffmpeg` 解码；`mean_volume = -23.5 dB`，`loudnorm.input_i = -23.57 LUFS`。
- `已确认` 脱敏请求记录：
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
- `待验证` 本轮只证明 voice cloning trial 已生成；是否明显比上一轮 `Serena` 更接近用户样本，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音复刻最小试配

- `已确认` 用户授权已到位；本轮允许上传裁剪后的合规样本到阿里百炼声音复刻接口，仅用于《视频工厂》最小声音复刻试配。
- `已确认` 已生成合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 本轮实际走的是 `qwen-voice-enrollment -> qwen3-tts-vc-realtime-2026-01-15` 的声音复刻路线，没有回退到 `Serena` 系统音色。
- `已确认` 当前阻塞点发生在 `create_custom_voice` 阶段：阿里百炼返回 `400 / Arrearage`，未创建成功 custom voice，未生成新的声音复刻试配音频。
- `已确认` 脱敏请求记录：`dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`。
- `已确认` 复刻试配日志：`codex_log/20260425_round28_声音复刻最小试配.md`。
- `待验证` 账户恢复后，可直接复用本轮合规裁剪样本继续创建 custom voice；当前声音仍待验证。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音试配失败排查

- `已确认` 用户已听审 `dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`，反馈为：和样本完全不一样，非常生硬，一听就是 AI。
- `已确认` 本轮只做声音路线诊断；未生成新音频，未修改视频 / 图片 / 原始素材 / 当前 trial 音频 / 脚本，未调用 TTS API，未上传用户样本。
- `已确认` 当前 trial 请求体为 `qwen3-tts-instruct-flash-realtime + Serena` 系统音色 + 指令控制；请求体里没有用户样本、custom voice、voice cloning 或 voice design 字段。
- `已确认` 失败主因：用户样本没有实际进入生成链路，当前路线只能做系统音色的风格指令控制，不能复刻用户样本声纹。
- `部分成立` 文案韵律和后处理可能放大生硬 / AI 感，但不是“完全不像样本”的主因。
- `待验证` 下一轮最值路线是：先取得用户明确授权，再走 `voice cloning（声音复刻）` 最小试配；若用户不授权上传样本，则退而走 `voice design（声音设计）`，不要继续盲调 `Serena`。
- `已确认` 诊断日志：`codex_log/20260425_round28_声音试配失败排查.md`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 最小声音试配

- `已确认` 本轮只生成 1 条 10-15 秒声音 trial（试配）音频；未修改任何视频、图片、原始素材、当前成片音轨或视频装配脚本。
- `已确认` 使用 round28 文案来源：`dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/subtitles/round28_完整可读终修.srt`。
- `已确认` 本轮试配文案取自 round28 字幕第 1 段 + 第 5 段首句：
  - `最费时间的，不是做汇报页。是第一行根本写不出来。后来我换上调好的提示词，直接砍掉空转。区别不是豆包，是那段提示词。`
- `已确认` 真实使用 TTS：`aliyun_bailian / aliyun_qwen_realtime_websocket / qwen3-tts-instruct-flash-realtime / Serena`。
- `已确认` 输出音频：`dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`。
- `已确认` 音频基础验证：`13.00s`、`aac (LC)`、`48000 Hz / mono`、`mean_volume = -16.4 dB`、`loudnorm.input_i = -16.25 LUFS`，可被 `ffmpeg` 解码。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 该 trial 只回答声音方向是否接近“低压、清楚、有一点可爱感的女生游戏向导音”；用户 / ChatGPT 听感复审前，不得写成最终音色、最终 TTS 或声音验证通过。

## 20260425｜语音样本只读排查与声音参考锚点

- `已确认` 本轮任务只做语音样本定位、音频基础参数分析、声音参考锚点落地与仓库口径更新；不改视频、不替换旁白、不生成新 round、不做 TTS 试配。
- `已确认` 当前 latest_review_pack 仍指向：`round34_中段双展示提示卡_正反分段提示修复`。
- `已确认` 用户语音样本已通过兜底搜索命中：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`。
- `已确认` 样本用于记录 `可爱女生向导音` 的 reference anchor（参考锚点）；它不等于最终 TTS 方案已确定，也不等于声音内容验证通过。
- `部分成立` `ffmpeg` 可用并已完成分析用音频副本提取、`volumedetect`、`astats`、`silencedetect` 与 `loudnorm` 初步测量；`ffprobe` 未在本机可执行路径中命中，本轮元数据读取降级使用 `ffmpeg` 输入信息。
- `已确认` 音频基础参数报告：`codex_log/20260425_语音样本_audio_reference_report.md`。
- `已确认` 分析文本输出目录：`codex_log/audio_reference/20260425_语音样本/`。
- `已确认` 当前视频状态未改变：
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 下一步声音动作是基于该样本做 10-15 秒最小声音试配，再和当前视频开头 / 结尾主持壳做听感匹配复审；不得直接全片替换。

## 20260425｜round34 中段双展示提示卡正反分段提示修复

- `已确认` 当前视频工作分支为 `codex/doubao-vnext-direct-fix-20260417`；该分支当前由 Git worktree `/private/tmp/视频工厂_round28_complete_readability` 持有。
- `已确认` 本轮新开 `round34_中段双展示提示卡_正反分段提示修复`，只做 `latest_review_pack` 中段局部修复；未重构整条视频。
- `已确认` 用户本轮同步的图二参考图可读取：`/Users/fan/Desktop/截屏2026-04-25 18.11.07.png`，尺寸 `908x492`。
- `已确认` 两张提示卡已按图二粉色樱花柔和展示牌风格重构为 720x1280、9:16 竖屏：
  - 《反面展示》：`先看旧做法：一句糊话，结果怎么变泛`
  - 《正面展示》：`再看工作包后：结果怎么一步步落成`
- `已确认` round34 中段结构为：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
- `已确认` 反面录屏与正面录屏仍由用户真实录屏承担，源时间码与 round33 一致，未裁短、未替换、未重录。
- `已确认` 开头主持壳、回场主持壳、`judgment_card`、Prompt 引用尾卡均未重做；未调用阿里 API，未重新生成元素娃娃，未修改原始录屏素材。
- `已确认` `latest_review_pack` 已更新指向：
  - `round34_中段双展示提示卡_正反分段提示修复`
- `已确认` 当前审片包口径：
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `border_residue_validation = 通过`
  - `jump_cut_validation = 通过`
  - `technical_validation = 通过`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 用户已打开实际可用本地审片包路径：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`。
- `已确认` 用户最新反馈为“现在中段没什么问题了”，仓库口径记录为：round34 中段结构暂定接受，当前不继续修改中段。
- `已确认` 中段暂定接受只代表 `middle_segment_review` 暂定收束，不代表全片 `content_validation` 通过。
- `待验证` round34 内容最终是否过线仍需用户 / ChatGPT 人工复审。
- `禁止误写` 不得把技术扫描通过写成内容最终通过；不得写 `send_ready = yes`；不得把云端剪辑写成稳定跑通。

## 当前最新审片入口

- 当前可打开本地审片包：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/full.mp4`
- `dist/latest_review_pack/middle_preview.mp4`
- `dist/latest_review_pack/before_after.mp4`
- `dist/latest_review_pack/图二参考图.png`
- `dist/latest_review_pack/反面展示提示卡_单帧.png`
- `dist/latest_review_pack/正面展示提示卡_单帧.png`
- `dist/latest_review_pack/正反提示卡_并排对比.png`
- `dist/latest_review_pack/problem_windows/30_32s.mp4`
- `dist/latest_review_pack/cut_contact_sheet.jpg`

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
- `codex_log/20260425_round34_中段暂定通过与本地审片路径修正.md`
