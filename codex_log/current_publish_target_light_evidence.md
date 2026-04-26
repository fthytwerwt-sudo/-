# Current Publish Target Light Evidence

## 对应对象

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`round34_中段双展示提示卡_正反分段提示修复`
- 当前完整正片：`dist/latest_review_pack/full.mp4`
- 当前中段预览：`dist/latest_review_pack/middle_preview.mp4`
- 当前审片入口：`dist/latest_review_pack/review_manifest.md`

## 历史对象

- 历史待发对象：`dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 历史云端正式输出：`oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`
- 当前解释：该对象只代表 20260412 当时口径下的历史通过样片，不再是当前最新复审 target。

## Git 可追踪轻量证据包

1. `dist/latest_review_pack/review_manifest.md`
   - 当前 ChatGPT / 用户复审入口。
   - 明确复审顺序：先看正反提示卡关键帧，再看 `middle_preview.mp4`、切点联系表和 full。
2. `dist/latest_review_pack/summary.json`
   - 当前 round34 验证状态摘要。
   - 可直接确认：
     - `border_residue_validation = 通过`
     - `jump_cut_validation = 通过`
     - `technical_validation = 通过`
     - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
     - `content_validation = 待用户 / ChatGPT 最终复审`
     - `full_content_validation = 待用户 / ChatGPT 最终复审`
     - `send_ready = false`
3. `dist/latest_review_pack/timeline.json`
   - 当前 segment / shot 时间轴与承载方式。
   - 可直接确认中段顺序：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
4. `dist/latest_review_pack/cut_map.md`
   - 当前逐镜头承载说明。
   - 可直接确认反面 / 正面录屏源时间码保持不变。
5. `dist/latest_review_pack/图二参考图.png`
   - 用户本轮同步的图二参考图副本，尺寸 `908x492`。
6. `dist/latest_review_pack/反面展示提示卡_单帧.png`
   - 反面展示提示卡 9:16 单帧，尺寸 `720x1280`。
7. `dist/latest_review_pack/正面展示提示卡_单帧.png`
   - 正面展示提示卡 9:16 单帧，尺寸 `720x1280`。
8. `dist/latest_review_pack/正反提示卡_并排对比.png`
   - 正反提示卡统一风格对比图。
9. `dist/latest_review_pack/middle_preview.mp4`
   - 中段快速复审视频。
10. `dist/latest_review_pack/full.mp4`
   - round34 完整正片。
11. `dist/latest_review_pack/before_after.mp4`
   - round33 与 round34 中段对比视频。
12. `dist/latest_review_pack/cut_contact_sheet.jpg`
   - round34 全片切点联系表。
13. `dist/latest_review_pack/problem_windows/30_32s.mp4`
   - 当前保留的 30-32 秒问题窗口。
   - 该窗口仍落在正面真实录屏内部。
14. `dist/latest_review_pack/problem_windows/30_32s_frames.jpg`
   - 30-32 秒高频抽帧联系表。
15. `dist/latest_review_pack/audit/full_border_residue_report.md`
   - round34 全片边框残留报告。
16. `dist/latest_review_pack/audit/full_jump_cut_report.md`
   - round34 全片跳切连续性报告。
17. `dist/latest_review_pack/audit/border_residue_contact_sheet.jpg`
   - round34 全片边框残留抽帧联系表。
18. `dist/latest_review_pack/audit/jump_cut_contact_sheet.jpg`
   - round34 全片跳切抽帧联系表。
19. `scripts/元素娃娃线_round34_中段双展示提示卡_正反分段提示修复.py`
   - round34 局部修复生成脚本。
20. `scripts/视频全片边框与跳切审计.py`
   - 本轮继续使用的边框残留与跳切审计脚本。
21. `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
   - round34 生成、修复、验证与口径同步日志。
22. `codex_log/20260425_语音样本_audio_reference_report.md`
   - 用户语音样本 reference anchor 的基础参数报告。
   - 记录样本路径、文件名、容器 / 编码 / 时长 / 采样率 / 声道 / 音量 / 静音段等客观参数。
   - 只能证明“样本已找到并已做基础参数分析”，不能证明声音已通过内容验证。
23. `codex_log/audio_reference/20260425_语音样本/`
   - 本轮音频分析文本输出目录。
   - `语音样本_分析副本.m4a` 为本地分析副本，不代表最终 TTS 产物，不直接替换当前视频音轨。
24. `dist/voice_trials/20260425_round28_10s_voice_trial/README.md`
   - round28 最小声音 trial 说明。
   - 记录使用文案、TTS 工具 / 模型 / 音色 / 参数、输出路径、时长与响度基础信息。
   - 只能证明 trial 已生成；当前已收到用户失败反馈，不能证明声音已通过。
25. `dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`
   - 本轮唯一声音试配音频。
   - 时长 `13.00s`，用于复审“低压、清楚、有一点可爱感的女生游戏向导音”是否接近目标。
   - 不替换当前视频音轨，不改变 `latest_review_pack`。
26. `codex_log/20260425_round28_最小声音试配.md`
   - 本轮声音 trial 执行日志。
27. `codex_log/20260425_round28_声音试配失败排查.md`
   - 本轮声音 trial 失败排查日志。
   - 记录用户反馈、请求体核对、模型能力层判断、样本未进入生成链路、仓库旧规则冲突与下一轮最小路线。
   - 只能证明失败排查完成，不能证明声音已通过。
28. `dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`
   - 已裁出的合规声音复刻输入样本。
   - 参数为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
   - 只能证明输入样本已准备好，不能证明 custom voice 已创建。
29. `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
   - 本轮声音复刻创建请求的脱敏记录。
   - 记录 `qwen-voice-enrollment -> qwen3-tts-vc-realtime-2026-01-15` 实际调用。
   - 本轮账户不再返回 `Arrearage`；用户 prompt 指定的 `preferred_name` 超长后，已按官方限制改用 `vfr28clone0426` 并创建成功。
30. `dist/voice_trials/20260425_round28_voice_clone_trial/README.md`
   - 本轮声音复刻最小试配说明。
   - 记录用户授权、复刻输入样本参数、API 路线、custom voice 脱敏标识和输出音频验证结果。
31. `codex_log/20260425_round28_声音复刻最小试配.md`
   - 本轮声音复刻执行日志。
32. `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
   - 本轮声音复刻合成请求的脱敏记录。
   - 可直接确认本轮使用的是 custom voice，`uses_custom_voice = true`，`uses_serena = false`。
33. `dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`
   - 本轮唯一声音复刻 trial 音频。
   - 时长 `12.96s`，格式 `wav / pcm_s16le / 24000 Hz / mono`。
   - 不替换当前视频音轨，不改变 `latest_review_pack`。
34. `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_ffmpeg_decode_check.txt`
   - 本轮复刻 trial 的 `ffmpeg` 解码验证日志。
35. `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_volumedetect.txt`
   - 本轮复刻 trial 的基础音量分析日志。
36. `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_loudnorm_measure.txt`
   - 本轮复刻 trial 的响度初测日志。
37. `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/README.md`
   - 本轮声音第二轮 A / B 对照 trial 说明。
   - 记录用户反馈原文、台湾口语文本、开心轻快 instructions、A / B 差异、模型、音色脱敏标识、降噪处理和验证结果。
38. `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav`
   - A 版沿用当前 custom voice 的未降噪节奏校准输出。
   - 时长 `14.18s`，格式 `wav / pcm_s16le / 24000 Hz / mono`。
39. `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav`
   - A 版沿用当前 custom voice 的输出后轻降噪版本。
   - 时长 `14.18s`，格式 `wav / pcm_s16le / 24000 Hz / mono`。
40. `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav`
   - B 版基于轻降噪输入样本重建 custom voice 的未降噪节奏校准输出。
   - 时长 `14.20s`，格式 `wav / pcm_s16le / 24000 Hz / mono`。
41. `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav`
   - B 版基于轻降噪输入样本重建 custom voice 的输出后轻降噪版本。
   - 时长 `14.20s`，格式 `wav / pcm_s16le / 24000 Hz / mono`。
42. `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/run_summary.json`
   - 本轮 A / B 技术生成、API 原始直出、节奏校准、降噪与音频验证的结构化摘要。
43. `codex_log/20260426_台湾口语开心降噪声音试配.md`
   - 本轮声音第二轮试配执行日志。
44. `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/README.md`
   - 本轮新样本 voice cloning 与文案风格解析入口说明。
   - 记录新样本定位、声音解析结果、custom voice 脱敏标识、试听 trial、转写与验证结果。
45. `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
   - 基于用户新样本重新创建测试 custom voice 后生成的声音复刻试听 trial。
   - 时长 `13.60s`，格式 `wav / pcm_s16le / 24000 Hz / mono`。
   - 不替换当前视频音轨，不改变 `latest_review_pack`。
46. `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
   - 从新样本裁出的 voice cloning 输入样本。
   - 参数为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
47. `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写文本_transcript.md`
   - 完整 MP4 音频的自动 ASR 转写文本。
   - 使用 `paraformer-realtime-v2`，仍待人工校对。
48. `codex_log/20260426_语音样本2_audio_reference_report.md`
   - 新样本基础音频参数报告。
49. `codex_log/20260426_语音样本2_文案风格高保真记录.md`
   - 新样本文案 reference style 高保真记录。
   - 包含 Source Anchor、Language Texture、Sentence Rhythm、Narrative Move、Emotion / Persona、Copywriting Reuse Rules、Prohibited Distortion。
50. `codex_log/20260426_语音样本2复刻与文案风格解析.md`
   - 本轮新样本复刻与文案风格解析执行日志。

## 这些轻量证据共同证明什么

- 当前最新复审对象是谁：
  - `dist/latest_review_pack/`
- 当前审片包指向哪一轮：
  - `round34_中段双展示提示卡_正反分段提示修复`
- 当前中段结构是什么：
  - 反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡
- 当前中段复审状态是什么：
  - 用户已确认 round34 中段“暂时就这样”，仓库口径为 `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
- 当前技术状态是什么：
  - `technical_validation（技术验证）`：`通过`
  - `border_residue_validation（边框残留验证）`：`通过`
  - `jump_cut_validation（跳切连续性验证）`：`通过`
- 当前内容状态是什么：
  - `content_validation（内容验证）`：`待用户 / ChatGPT 最终复审`
  - `full_content_validation（全片内容验证）`：`待用户 / ChatGPT 最终复审`
  - `send_ready（可直接发送）`：`no`
- 当前声音参考状态是什么：
  - `voice_reference_anchor`：用户样本已提供，待听感复审与试配
  - `voice_trial_status`：上一轮 round28 10-15 秒最小 trial 已生成，但用户反馈为不像样本、非常生硬、AI 感明显；当前系统音色 trial 不通过听感目标
  - `voice_clone_trial_status`：用户授权已记录；上一轮台湾口语开心降噪 A / B 对照 trial 已被用户判定完全不合格，仅保留失败参考；20260426 已基于新样本 `语音样本 2.MP4` 重新创建测试 custom voice，并生成 13.60s 复刻试听 trial，待用户 / ChatGPT 听感复审
  - `copy_style_status`：语音样本2完整 MP4 自动转写已生成，文案 reference style 已高保真记录；自动转写仍待人工校对，不能写成“文案风格已完全掌握”
  - `voice_validation_status`：待验证
  - `tts_vendor_status`：待验证
  - `next_voice_step`：先听审语音样本2新复刻试听 trial，判断是否比上一轮 A / B 更接近新样本；听感复审通过前，不直接全片替换
- 当前证据链原则是什么：
  - 中段主体仍由用户真实录屏承担。
  - 卡片 / PPT / 图片只允许辅助解释，不允许替代证据。
  - 新增 / 重构提示卡不能替代正面或反面真实录屏。
- 当前不能证明什么：
  - 不能证明 round34 已经可直接发送。
  - 不能证明 `content_validation` 已通过。
  - 不能证明 `云端剪辑` runtime 已稳定跑通。
  - 不能证明最终 TTS 供应商已确定。
  - 不能证明用户语音样本已经通过项目听感验证。
  - 不能证明本轮声音 trial 已经通过听感复审。
  - 不能证明 custom voice 已经是最终音色。
  - 不能证明新的 voice cloning trial 已经通过听感复审。
  - 不能证明台湾口音、开心情绪和降噪听感已经通过人工验证。
  - 不能证明单个约 23 秒样本足以作为完整 voice cloning 训练集。

## 当前本地审片包

- `/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- `dist/latest_review_pack/`

## 为什么仍保留历史 20260412 证据

- 20260412 是当时口径下的历史通过样片。
- 历史日志不删除，继续用于追溯旧判断。
- 当前复审 target 已切到 round34，不得再用 20260412 冒充当前最新可发样片。

## 当前一句话

- 当前最新复审对象是 `dist/latest_review_pack/`，指向 `round34_中段双展示提示卡_正反分段提示修复`；用户已暂定接受中段并要求当前不继续修改中段；技术扫描通过与中段暂定接受都不等于全片内容最终过线，`content_validation = 待用户 / ChatGPT 最终复审`，`send_ready = no`；上一轮 A / B 声音试配已被用户判定完全不合格，只保留失败参考；当前声音路线已基于新样本 `语音样本 2.MP4` 生成 13.60s 复刻试听 trial，并已高保真记录样本文案 reference style，但声音与文案风格仍待用户 / ChatGPT 复审，不能写成最终音色、声音验证通过或文案风格已完全掌握。
