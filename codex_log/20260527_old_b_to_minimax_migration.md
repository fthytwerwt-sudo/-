# 20260527｜旧 B 到 MiniMax 声音迁移审计

## 任务结果

```text
task_result.status: blocked_need_reference_audio_url
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

本轮按用户最新指令处理：不是恢复旧 Qwen / 阿里正式路线，而是用 MiniMax 参考音频 / voice clone 迁移旧 B 声音。

## 读取与能力检查

- 已读取 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`、`codex_log/latest.md`、`GPT数据源/08_当前正式事实.md`。
- 已读取旧 B 恢复审计报告：`codex_log/diagnostics/old_aliyun_b_voice_restoration_audit_20260527_222316/old_b_voice_restoration_audit_report.json`。
- 已读取 TTS 声音审计 JSON 与 MiniMax B 声音重审报告。
- 已探测旧 B 两条参考音频：`B_15秒文案_停顿梗感.wav` 与 `语音样本2_声音复刻试听_15秒.wav` 均存在且可读。
- 已搜索 MiniMax voice clone / reference_audio / audio_url / voice_id / qwen-t...ac19 / B_15秒文案_停顿梗感。

## 关键结论

- MiniMax 官方 voice clone 支持上传参考音频获取 `file_id`，再 clone 出 `voice_id`。
- 仓库当前百炼代理到 MiniMax 的历史诊断记录为：reference audio / voice clone 需要公网 `audio_url`。
- 本轮没有旧 B 参考音频公网 `audio_url`，也没有用户授权上传参考音频。
- 因此本轮没有调用 MiniMax TTS / clone API，没有生成迁移样本。
- 禁止退回 MiniMax 系统音色候选；女声、男声或中性系统候选均不能替代旧 B。

## 机制回写

- 更新 `scripts/正片候选TTS路线_publish_candidate_tts_route.py`：新增 `old_b_to_minimax_voice_lock` 校验，阻断缺 `audio_url / upload authorization`、缺 `generated_minimax_voice_id`、系统音色替代、旧 Qwen 正式路线恢复、未用户试听确认。
- 更新测试：覆盖旧 Qwen reference-only、系统男声不能替代旧 B、缺参考音频 URL 阻断、生成 MiniMax clone voice 并用户确认后才可通过。
- 更新 `codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/19_project_state_action_router.md`、`codex_source/21_codex_judgment_permission_matrix.md`、`GPT数据源/08_当前正式事实.md`、`codex_log/latest.md`。

## 产物

```text
diagnostics_dir: codex_log/diagnostics/old_b_to_minimax_migration_20260527_224840
report_json: codex_log/diagnostics/old_b_to_minimax_migration_20260527_224840/old_b_to_minimax_migration_report.json
report_md: codex_log/diagnostics/old_b_to_minimax_migration_20260527_224840/old_b_to_minimax_migration_report.md
deepseek_supply_request: codex_log/supply_requests/20260527_old_b_to_minimax_migration_pre_supply_request.json
deepseek_supply_output: codex_log/deepseek_supply/20260527_old_b_to_minimax_migration_pre_supply
```

## 状态边界

- 未生成音频。
- 未生成视频。
- 未重生成全片旁白。
- 未替换当前视频音轨。
- 未改文案。
- 未推进 `voice_validation / final_voice_validated / content_validation / send_ready / visual_master_locked`。

## 下一步

用户授权参考音频上传或提供可访问 `audio_url` 后，下一轮只生成三条 MiniMax 迁移短样本：

```text
V1_identity_match
V2_prosody_optimized
V3_emotion_rich
```
