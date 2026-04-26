# Current Publish Target

## 当前口径

- `已确认` 本文件记录《视频工厂》当前复审 / publish target 入口。
- `已确认` 20260412 旧样片只保留为历史通过样片，不再代表当前最新复审对象。
- `已确认` 当前用户最终人工确认前，`send_ready` 必须保持 `no`。

## 历史 target

- 历史待发对象：`dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 历史云端输出：`oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`
- 历史状态：
  - `technical_validation`：`通过`
  - `content_validation`：`通过`
  - `user_acceptance`：`通过`
  - `send_ready`：`是`
- 当前解释：上述状态只代表 20260412 当时口径下的历史 target，不代表当前 vNext / round34 可直接发送。

## 当前复审 target

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`round34_中段双展示提示卡_正反分段提示修复`
- 当前完整正片：`dist/latest_review_pack/full.mp4`
- 当前中段预览：`dist/latest_review_pack/middle_preview.mp4`
- 当前 before / after：`dist/latest_review_pack/before_after.mp4`
- 当前复审入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`

## 当前正式状态

- `technical_validation`：`通过`
- `border_residue_validation`：`通过`
- `jump_cut_validation`：`通过`
- `middle_segment_review`：`用户暂定通过 / 暂不继续修改中段`
- `content_validation`：`待用户 / ChatGPT 最终复审`
- `full_content_validation`：`待用户 / ChatGPT 最终复审`
- `send_ready`：`no`
- 当前判断：`round34 中段结构已获用户暂定接受，当前不继续修改中段；全片内容最终过线与可发送状态仍待用户 / ChatGPT 复审`

## 当前唯一最高优先级 blocker

- `用户 / ChatGPT 尚未对 round34 完整正片做最终内容复审`
- `声音路线已新增用户语音样本 reference anchor；上一轮台湾口语开心降噪 A / B 对照 trial 被用户明确判定完全不合格，只保留为失败参考；20260426 已基于新样本“语音样本 2.MP4”重新创建测试 custom voice 并生成 13.60s 复刻试听 trial，同时已记录样本文案 reference style，但声音和文案风格仍待用户 / ChatGPT 复审`
- 当前不能写：
  - `content_validation = 通过`
  - `send_ready = yes`
  - `最终 TTS 已选定`
  - `声音路线已完成验证`
  - `云端剪辑已稳定跑通`

## 本轮结构变化

- 读取到的 round33 中段结构：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
- round34 中段结构：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
- round34 本轮实际变化是：基于用户本轮图二参考图，重构《反面展示》《正面展示》两张 720x1280、9:16 粉色樱花柔和展示牌提示卡，并保留录屏证据时间码不变。
- 用户最新复审反馈：round34 中段“现在中段没什么问题了”，仓库口径记为中段暂定接受，当前不继续修改中段。
- 注意：中段暂定接受不等于全片内容验证通过。
- 两张提示卡时长均为 `1.6s`。
- 中段主要切点使用 `0.16s` 轻 crossfade；结果差卡回主持壳使用 `0.22s` 轻 crossfade。
- 反面录屏与正面录屏仍是中段主体证据，卡片只承担段落标识。

## 现在最该看的入口

1. `dist/latest_review_pack/review_manifest.md`
2. `dist/latest_review_pack/正反提示卡_并排对比.png`
3. `dist/latest_review_pack/反面展示提示卡_单帧.png`
4. `dist/latest_review_pack/正面展示提示卡_单帧.png`
5. `dist/latest_review_pack/middle_preview.mp4`
6. `dist/latest_review_pack/cut_contact_sheet.jpg`
7. `dist/latest_review_pack/full.mp4`

## 当前已追踪证据

- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/timeline.json`
- `dist/latest_review_pack/cut_map.md`
- `dist/latest_review_pack/cut_contact_sheet.jpg`
- `dist/latest_review_pack/图二参考图.png`
- `dist/latest_review_pack/反面展示提示卡_单帧.png`
- `dist/latest_review_pack/正面展示提示卡_单帧.png`
- `dist/latest_review_pack/正反提示卡_并排对比.png`
- `dist/latest_review_pack/problem_windows/30_32s.mp4`
- `dist/latest_review_pack/problem_windows/30_32s_frames.jpg`
- `dist/latest_review_pack/audit/full_border_residue_report.md`
- `dist/latest_review_pack/audit/full_jump_cut_report.md`
- `dist/latest_review_pack/audit/border_residue_contact_sheet.jpg`
- `dist/latest_review_pack/audit/jump_cut_contact_sheet.jpg`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/20260425_语音样本_audio_reference_report.md`
- `codex_log/20260425_语音样本只读排查与声音参考锚点.md`
- `dist/voice_trials/20260425_round28_10s_voice_trial/README.md`
- `dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`
- `codex_log/20260425_round28_最小声音试配.md`
- `codex_log/20260425_round28_声音试配失败排查.md`
- `codex_log/20260425_round28_声音复刻最小试配.md`
- `dist/voice_trials/20260425_round28_voice_clone_trial/README.md`
- `dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`
- `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
- `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
- `dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`
- `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_ffmpeg_decode_check.txt`
- `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_volumedetect.txt`
- `dist/voice_trials/20260425_round28_voice_clone_trial/复刻输出_loudnorm_measure.txt`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/README.md`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav`
- `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/run_summary.json`
- `codex_log/20260426_台湾口语开心降噪声音试配.md`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/README.md`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写文本_transcript.md`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/run_summary.json`
- `codex_log/20260426_语音样本2_audio_reference_report.md`
- `codex_log/20260426_语音样本2_文案风格高保真记录.md`
- `codex_log/20260426_语音样本2复刻与文案风格解析.md`

## 当前 `local_review_pack` 证据

- `/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- `dist/latest_review_pack/`

## `lane_recommendation`

- `serial_review_only`

## `lane_reason`

- 当前对象已收束到 round34 审片包。
- 当前动作是按 review_manifest 进行全片最终人工复审；中段已暂定收束，当前不继续修改中段。
- 用户最终确认前，不得把技术验证通过升级成内容通过。

## `lane_invalid_if`

- 用户要求新开 round 或继续修视频内容。
- 用户人工确认 round34 内容通过并允许更新 `send_ready`。
- `dist/latest_review_pack/summary.json` 指向发生变化。

## `parallel_recommendation`

- `serial_only`

## `parallel_reason`

- 当前只需要围绕同一套审片包做最终判断。
- 并发写同一状态文件容易造成 `technical_validation` 与 `content_validation` 混写。

## `parallel_invalid_if`

- 下一轮任务拆成互不写同一文件的独立审计项。

## 当前同步状态

- 状态分类：`task_branch_round34_review_pack_ready`
- 当前工作分支：`codex/doubao-vnext-direct-fix-20260417`
- 当前主读目录：`GPT数据源/`
- 当前复审 target：`dist/latest_review_pack/`
- 当前可打开本地审片包：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- 本轮同步要求：必须 push 当前视频工作分支，并同步默认主读取分支 `codex/user-readable-map`
- 未同步事项：用户 / ChatGPT 全片最终内容复审结论尚未产生；语音样本2复刻试听 trial 已生成但尚未完成听感复审，不能写成最终音色或声音验证通过；语音样本2文案风格记录已生成但 ASR 自动转写仍待人工校对

## 最后更新时间

- `2026-04-26 CST`

## 对应 dated log 路径

- `codex_log/20260412_豆包素材正式样片执行与过线结论.md`
- `codex_log/20260413_口径压平补丁_过线与升级空间拆层.md`
- `codex_log/20260424_round32_全片边框残留与跳切连续性修复.md`
- `codex_log/20260425_全仓口径审计第一批修正.md`
- `codex_log/20260425_round33_正反展示提示卡补齐与风格统一.md`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
- `codex_log/20260425_round34_中段暂定通过与本地审片路径修正.md`
- `codex_log/20260425_语音样本只读排查与声音参考锚点.md`
- `codex_log/20260425_语音样本_audio_reference_report.md`
- `codex_log/20260425_round28_最小声音试配.md`
- `codex_log/20260425_round28_声音试配失败排查.md`
- `codex_log/20260425_round28_声音复刻最小试配.md`
- `codex_log/20260426_台湾口语开心降噪声音试配.md`
- `codex_log/20260426_语音样本2_audio_reference_report.md`
- `codex_log/20260426_语音样本2_文案风格高保真记录.md`
- `codex_log/20260426_语音样本2复刻与文案风格解析.md`
