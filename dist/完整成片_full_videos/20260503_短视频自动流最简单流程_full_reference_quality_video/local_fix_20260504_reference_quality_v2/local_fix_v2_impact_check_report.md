# local_fix_v2_impact_check_report

## 基本判断

- `current_final_video_path`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/full_video.mp4`
- `current_local_fix_video_path`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/full_video_local_fix.mp4`
- `v2_output_dir`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality_v2`
- `current_local_fix_resolution`：`1080x1920`
- `current_local_fix_duration_seconds`：`776.640`
- `current_local_fix_decodable`：`true`

## 中段来源与左右晃判断

- `current_middle_source_mode`：`prepared_intermediate_clips`
- `raw_middle_sources_available`：`true`
- `raw_middle_sources`：
  - `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4`
  - `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4`
  - `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4`
- `current_middle_segments_to_recut`：`seg02`, `seg04`, `seg06`, `seg07`, `seg08`, `seg14`
- `current_dynamic_crop_location`：历史 formal 核心 `formal_api_demo_core.py` 仍包含 `middle_reference_zoom` 动态横向裁切；v1 本地脚本不走该 formal 动态 zoom，但 v1 中段复用了已准备的中间片段，不满足本轮“从原始素材重新剪”的要求。
- `current_v1_script_cos_sin_note`：v1 本地脚本中的 `math.cos / math.sin` 只用于静态骚萌卡冲击线绘制，不是中段横向移动；v2 脚本将避免在中段和本地装配 timeline 中出现周期性横移表达式。
- `v2_required_fix`：从原始素材重新生成中段，固定证据窗口，禁止持续 `crop_x`、周期性横向扫描、`cos / sin` 驱动的中段移动。

## 画布 / 粉色背景判断

- `target_canvas`：`1080x1920`
- `current_canvas`：`1080x1920`
- `reported_problem`：用户反馈后段出现粉色背景不对称 / 画布偏移。
- `likely_root_cause`：v1 中录屏段使用粉色遮挡块和局部裁切时，视觉上形成单侧粉色厚边；部分卡片 / MOV / 录屏层虽然最终编码为 `1080x1920`，但画面内容层没有统一以同一 full-bleed canvas 和居中证据窗口组织。
- `v2_required_fix`：所有 segment 统一进入 `1080x1920`；背景 full bleed；录屏中段使用同尺寸背景层 + 居中固定证据窗口；卡片、骚萌卡、HyperFrames 总结卡全部按同一 9:16 画布输出。

## 元素娃娃判断

- `element_doll_keep_segment`：`seg01` 开头约 `2.0s`
- `element_doll_dialogue`：`大家好`
- `element_doll_reference`：`opening_reference_element_doll_no_text_locked_20260428`
- `element_doll_after_intro_allowed`：`false`
- `element_doll_segments_to_replace`：`seg01_after_intro`, `seg05`, `seg10`, `seg12`, `seg17`

## 骚萌卡替换判断

- `sassy_reference`：`PR7_B_骚萌反应页.png`
- `sassy_locked_reference`：`sassy_card_pr7_b_visual_locked_20260501`
- `legacy_pr7_a_allowed`：`false`
- `required_replacement_strategy`：原元素娃娃位置全部改为骚萌卡；每张必须属于同一角色体系但不能完全一样。
- `planned_sassy_cards`：
  - `seg01_after_intro`：问题钩子骚萌卡，`一键生成？先别急着抽卡`
  - `seg05`：判断转折骚萌卡，`先拆流程，工具才有位置`
  - `seg10`：API 工位转折骚萌卡，`API 是工位，不是主角`
  - `seg12`：装配台转折骚萌卡，`装配台别抢方向盘`
  - `seg14`：执行检查骚萌卡，`半成品别装完成`
  - `seg17`：收束反应骚萌卡，`流程在，工具才好换`

## HyperFrames 判断

- `summary_segment`：`seg17`
- `summary_card_core_sentence`：`顺序对了，自动化才有地方落脚。`
- `current_v1_hyperframes_used`：`true`
- `v2_hyperframes_required`：`true`
- `allowed_role`：`card_motion_layer`
- `entered_middle_screen_recording_allowed`：`false`

## TTS 判断

- `target_model`：`qwen3-tts-vc-realtime-2026-01-15`
- `custom_voice_reference`：`qwen-t...ac19`
- `tts_reference_read`：`tts_15s_b_pacing_locked_20260427`
- `current_v1_voiceover`：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/local_fix_20260504_reference_quality/声音_v31_ac19_b_pacing_tts/tts/formal_voiceover.mp3`
- `current_v1_voiceover_duration_seconds`：`776.640`
- `v2_voiceover_plan`：继续走阿里 realtime voice clone 链路，优先使用可用的 `qwen-t...ac19` 生成开头 `大家好`，并将完整主体旁白合成为 v2 最终音轨；不得使用 macOS `say`，不得回退旧 TTS 基线。

## 局部修复可行性

- `can_recut_middle_only`：`true`
- `can_fix_canvas_without_full_rebuild_from_zero`：`true`
- `can_reuse_non_middle_assets`：`true`
- `must_reassemble_full_local_video`：`true`
- `full_rebuild_from_scratch_required`：`false`
- `cloud_assembly_required`：`false`
- `true_blocker`：`none_at_impact_check`

## Impact Check 结论

`已确认` 本轮可以在 PR #46 当前分支上做本地参考修正版 v2：不整片从零重做，不走阿里云剪辑；从原始录屏素材重剪中段，统一 9:16 画布，保留 v3.1 参考 TTS / HyperFrames / 骚萌卡机制，再重新本地总装完整片。
