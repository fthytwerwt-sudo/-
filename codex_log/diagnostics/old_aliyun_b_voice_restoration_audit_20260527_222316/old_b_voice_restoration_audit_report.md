# 旧阿里 B 方案声音恢复审计报告

## 结论

- `task_result.status = completed_old_b_voice_audit`
- 本轮未调用 TTS API，未生成音频，未生成视频，未改文案，未替换当前视频音轨。
- 旧 B 方案声音证据链成立：仓库里的旧 B 声音底子是阿里 / 百炼 Qwen custom voice 路线，脱敏声音标识为 `qwen-t...ac19`，模型为 `qwen3-tts-vc-realtime-2026-01-15`。
- `qwen-t...ac19` 不是 MiniMax `voice_id`；MiniMax 系统女声、男声或中性候选都不能自动替代旧 B。
- 当前冲突已明确：仓库近期把正片候选默认 TTS 切到 MiniMax，但用户当前最新指令要求恢复旧阿里 / Qwen B 方案声音。下一轮唯一修复路线应走 `route_a_restore_old_qwen_b`。

## 旧 B 声音事实

| 字段 | 结论 |
| --- | --- |
| old_b_voice_exists | true |
| old_b_voice_model | `qwen3-tts-vc-realtime-2026-01-15` |
| old_b_voice_masked_id | `qwen-t...ac19` |
| provider | `aliyun_bailian` |
| route | `aliyun_qwen_realtime_websocket_voice_clone` |
| request_method | `WEBSOCKET` |
| create_model | `qwen-voice-enrollment` |
| 20260427 是否重新 create custom voice | false，使用已有 custom voice 列表按 suffix `ac19` 命中 |
| confidence | 历史路线身份高；当前可调用状态需下一轮 runtime smoke |

## 参考音频

- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`
  - 角色：B 版停顿梗感参考
  - `duration = 16.32s`
  - `codec = pcm_s16le`
  - `sample_rate = 24000`
  - `channels = 1`
- `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
  - 角色：历史声音底子参考
  - `duration = 13.6s`
  - `codec = pcm_s16le`
  - `sample_rate = 24000`
  - `channels = 1`

## 核心证据路径

- `codex_log/20260427_十五秒文案语速停顿试配.md`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/run_summary.json`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_voice_clone_tts_request_debug_sanitized.json`
- `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/custom_voice_list_debug_sanitized.json`
- `scripts/语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis.py`
- `scripts/生成新第四期选品初筛源比例无遮挡B语音修复候选片_generate_new_fourth_selection_source_ratio_no_mask_b_voice_fix_candidate.py`
- `codex_log/20260525_visual_no_mask_source_ratio_and_voice_b_fix.md`
- `dist/new_fourth_episode_selection_publish_candidate_visual_voice_fix_20260525_012938/summary.json`

## 路线冲突

| 项 | 结论 |
| --- | --- |
| conflict_exists | true |
| current_minimax_default | 当前正片候选默认要求 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd` |
| user_requested_old_aliyun_b | 用户当前要求恢复旧阿里 / Qwen B 方案声音 |
| can_old_b_voice_run_on_minimax_directly | false |
| can_minimax_clone_old_b_with_reference_audio | 能力上可能，但不是本轮路线，也必须用户确认 |
| can_qwen_old_b_route_be_restored_for_publish_candidate | 可以恢复，但下一轮必须先做 runtime smoke，本轮不推进通过 |
| safest_next_path | `route_a_restore_old_qwen_b` |

## 运行时检查

- `existing_script_found = true`
- `existing_runtime_config_found = historical_logs_show_authorized_runtime_config; current_secret_file_not_read`
- `likely_callable_without_code_change = false`
- 原因：当前旧 B 修复候选脚本内存在 `LEGACY_B_VOICE_ROUTE_BLOCKED_FOR_PUBLISH_CANDIDATE = True`，下一轮需要显式恢复旧 Qwen / 阿里 B 路线并做最小 runtime smoke。

## 禁止替代规则

以下声音不能替代旧 B：

- `female-tianmei`
- `female-shaonv`
- `female-shaonv-jingpin`
- `female-yujie`
- `male-qn-qingse`
- `male-qn-daxuesheng`
- `Chinese (Mandarin)_Gentleman`
- `Chinese (Mandarin)_Gentle_Youth`
- `Chinese (Mandarin)_Sincere_Adult`

规则：男声候选也不能自动等于旧 B。只有恢复旧 Qwen / 阿里 B 路线，或用旧 B 参考音频克隆并经用户确认，才能成为新 B。

## 下一轮唯一路线

`selected_route = route_a_restore_old_qwen_b`

下一轮应只做：

1. 显式恢复旧 Qwen / 阿里 B 路线。
2. 在用户允许调用 TTS API 时，先做最小 runtime smoke。
3. smoke 通过后，再决定是否只重生成全片旁白并替换音轨。
4. 仍不得改文案、画面或推进 `voice_validation = passed`，除非用户试听确认。

## DeepSeek 供料状态

- 已创建供料任务卡。
- safe runner 确认 runtime provider ready，key 未打印、未写入。
- controller 返回 `blocked_invalid_context_pack`。
- `deepseek_actual_participation = not_attempted_policy_violation`
- `not_deepseek_conclusion = true`

本报告结论来自 Codex 本地复核仓库证据，不写成 DeepSeek 结论。
