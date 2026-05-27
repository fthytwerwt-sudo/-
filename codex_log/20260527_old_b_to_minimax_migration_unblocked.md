# 20260527｜旧 B 到 MiniMax 迁移上传授权解阻检查

## 任务结果

```text
task_result.status: blocked
video_generated: false
audio_generated: false
tts_api_called: false
copy_changed: false
current_video_modified: false
```

## 路线裁决

```text
old_qwen_role: reference_anchor_only
minimax_role: final_generation_provider
selected_route: route_b_migrate_old_b_to_minimax
system_voice_candidates_allowed: false
old_qwen_formal_route_allowed: false
```

本轮按用户最新授权处理：允许上传两条旧 B 参考音频，仅用于 MiniMax voice clone / reference 短样本；但不恢复旧 Qwen / 阿里正式路线，不使用 MiniMax 系统音色候选。

## 关键结论

- `已确认` 两条旧 B 参考音频均存在且可解码：
  - `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`
- `已确认` MiniMax 官方 voice clone 当前要求先调用 `/v1/files/upload` 获取 `file_id`，再调用 `/v1/voice_clone` 创建 cloned `voice_id`。
- `已确认` 当前本地环境没有 `MINIMAX_API_KEY`，因此不能进行 MiniMax 官方 file upload，也不能生成 `generated_minimax_voice_id`。
- `已确认` 用户可控 OSS 字段可用，但当前 MiniMax 官方 clone 链路需要 `file_id`；只上传到 OSS 不能生成 cloned `voice_id`，所以本轮未做无效上传。
- `已确认` 本轮没有生成 V1 / V2 / V3 迁移样本。

## 产物

```text
diagnostics_dir: codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125
report_json: codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125/old_b_to_minimax_migration_unblocked_report.json
report_md: codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125/old_b_to_minimax_migration_unblocked_report.md
review_table: codex_log/diagnostics/old_b_to_minimax_migration_unblocked_20260527_234125/voice_candidate_review_table_old_b_minimax.md
deepseek_supply_request: codex_log/supply_requests/20260527_old_b_to_minimax_migration_unblocked_pre_supply_request.json
deepseek_supply_output: codex_log/deepseek_supply/20260527_old_b_to_minimax_migration_unblocked_pre_supply
deepseek_post_risk_review_request: codex_log/supply_requests/20260527_old_b_to_minimax_migration_unblocked_post_risk_review_request.json
deepseek_post_risk_review_output: codex_log/deepseek_supply/20260527_old_b_to_minimax_migration_unblocked_post_risk_review
```

## 状态边界

- 未上传参考音频。
- 未生成音频。
- 未生成视频。
- 未重生成全片旁白。
- 未替换当前视频音轨。
- 未改文案。
- 未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。

## 下一步

下一轮只需在安全运行环境提供 `MINIMAX_API_KEY`，复跑：

```bash
python3 scripts/旧B到MiniMax迁移解阻样本生成_old_b_to_minimax_migration_unblocked.py <timestamp>
```

随后才允许上传这两条旧 B 参考音频到 MiniMax 官方 `/v1/files/upload`，获取 `file_id`，创建 cloned `voice_id`，并生成 V1 / V2 / V3 三条迁移短样本。
