# 当前本地产物路径索引 current_local_artifact_paths

## 1. 文件定位

本文件记录 Codex 已在本机验证真实存在的《视频工厂》本地产物路径。

`已确认` 本轮已执行 `single_workspace_rule（单工作区硬规则）`：

- 《视频工厂》唯一正式工作区是 `/Users/fan/Documents/视频工厂`。
- `canonical_local_path（首选本地路径）` 只能指向 `/Users/fan/Documents/视频工厂` 内部。
- `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*`、`/Users/fan/Documents/视频工厂-worktrees`、`/private/tmp`、`/Users/fan/Desktop`、`/Users/fan/Downloads` 不得作为最终交付路径。
- 旧外部路径只能作为 `historical_source_path（历史来源路径）` 或 `fallback_path（备选路径）` 记录，不得作为默认执行路径。
- 如果路径超过 24 小时未重新验证，必须标记为 `stale_pending_recheck（已过期，待重新检查）`。
- `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径，只能作为线索，不能直接当真实路径。

## 2. 当前路径优先级

路径优先级：

1. `project_internal_stable_path（唯一正式工作区内部稳定路径）`
2. `project_internal_latest_review_pack（唯一正式工作区内部 latest_review_pack）`
3. `historical_source_path（历史来源路径，仅说明来源，不作为默认执行路径）`
4. `fallback_path（备选路径，仅在本轮重新验证后可输出）`

## 3. 当前已验证路径表

字段：

| artifact_id（产物编号） | 中文名称 | purpose（用途） | canonical_local_path（首选本地路径） | path_exists（路径是否存在） | fallback_paths（备选路径） | verified_at（验证时间） | source_record（来源记录） | notes（备注） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `round34_middle_preview` | round34 中段预览样片 | 中段放大剪辑尺度 / 中段结构 reference whitelist | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/middle_preview.mp4` | `true` | 旧大包路径：`/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1508_中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4` | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正；Git tracked latest_review_pack evidence | 旧 817M 本地大包未恢复；当前恢复 / 保留的是 `dist/latest_review_pack` 中仍存在的最小中段参考证据。它不是当前固定素材锚点，但属于中段剪辑 / 证据窗口 `reference_whitelist`。 |
| `round34_problem_window_30_32` | round34 30-32 秒问题窗口 | 中段证据窗口 reference whitelist | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/problem_windows/30_32s.mp4` | `true` | 旧大包路径：`/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1511_30_32s.mp4` | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正；Git tracked latest_review_pack evidence | 旧 817M 本地大包未恢复；当前保留的是 latest_review_pack 中仍存在的问题窗口最小证据。它不是固定素材锚点，但可用于中段证据窗口复核。 |
| `round34_problem_window_30_32_frames` | round34 30-32 秒抽帧联系表 | 中段证据窗口抽帧 reference whitelist | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/problem_windows/30_32s_frames.jpg` | `true` | 旧大包路径：`/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/01_主候选_1080P_images/1382_30_32s_frames.jpg` | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正；Git tracked latest_review_pack evidence | 旧 817M 本地大包未恢复；当前保留的是 latest_review_pack 中仍存在的问题窗口抽帧证据。它不是固定素材锚点，但可用于中段证据窗口复核。 |
| `round34_cut_contact_sheet` | round34 切点联系表 | cut points / 中段结构 reference whitelist | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/cut_contact_sheet.jpg` | `true` | 旧大包路径：`/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/01_主候选_1080P_images/1675_cut_contact_sheet.jpg` | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正；Git tracked latest_review_pack evidence | 旧 817M 本地大包未恢复；当前恢复 / 保留的是 `dist/latest_review_pack` 中仍存在的切点联系表。它不是当前固定素材锚点，但属于中段结构 `reference_whitelist`。 |
| `round34_full_video` | round34 完整正片 | 历史 round34 完整片记录 | `/Users/fan/Documents/视频工厂/视频工厂_元素娃娃1080P复审包_20260428/02_主候选_1080P_videos/1521_主持壳正式正片_round34_中段双展示提示卡_正反分段提示修复.mp4` | `false` | 无 | `2026-05-04 CST` | `deleted_in_pre_upgrade_cleanup_20260504` | 旧 round34 本地复审包已删除；不得作为用户可打开路径或当前 reference 输出。 |
| `v31_full_video_current_baseline` | AI 做 PPT 踩坑 v3.1 当前基线片 | 当前最新视频基线；后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基础 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4` | `true` | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/full.mp4` | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | `historical_source_path` 曾为 `/Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502/...` 与 `/Users/fan/Documents/视频工厂_v31_visual_route_fix/...`，外部 worktree 已安全移除；`send_ready = false`、`content_validation = gray_testing_not_final_passed` 保持不变。 |
| `v31_element_doll_opening_anchor` | v3.1 元素娃娃开头锚点 | 当前唯一固定素材锚点；只承担 v3.1 开头入口 | `/Users/fan/Documents/视频工厂/素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | `true` | 无 | `2026-05-04 CST` | `test -f` 已通过；`opening_reference_element_doll_no_text_locked_20260428` 路径补登记 | 只保留开头价值；不代表元素娃娃继续做全片主持；不代表元素娃娃替代录屏主体；不代表元素娃娃替代真人判断段。 |
| `v31_element_doll_opening_preview` | v3.1 元素娃娃开头预览 | 当前 v3.1 复审包中的开头预览证据 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4` | `true` | 无 | `2026-05-04 CST` | `test -f` 已通过；`dist/latest_review_pack/summary.json` artifacts.opening_preview 线索本地复核 | 只保留开头预览价值；不代表元素娃娃继续做全片主持；不代表元素娃娃替代录屏主体；不代表元素娃娃替代真人判断段；不改变 `content_validation` 或 `send_ready`。 |
| `v3_full_video_review_candidate` | AI 做 PPT 踩坑 v3 完整候选片 | v3 历史候选 / 对照记录 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/AI做PPT踩坑_成品候选_v3_full.mp4` | `false` | 无 | `2026-05-04 CST` | `deleted_in_pre_upgrade_cleanup_20260504` | v3 复审包已在项目升级前清库中删除；v3 只保留历史口径，不再作为可打开路径或后续默认基础。 |
| `pr7_b_sassy_reference` | PR #7 B 骚萌卡视觉参考 | 后续骚萌卡执行参考 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 读不到该文件必须 `blocked`，不得回退 PR #7 A；外部 worktree 旧路径已降级为历史来源。 |
| `cute_prompt_card_negative_reference` | 可爱反面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_反面展示提示卡.png` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 外部 worktree 旧路径已降级为历史来源。 |
| `cute_prompt_card_positive_reference` | 可爱正面展示提示卡参考 | `cute_prompt_card_route` 证据 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/round34_正面展示提示卡.png` | `true` | 无 | `2026-05-03 CST` | `test -f` 已通过；单工作区治理重新验证 | 外部 worktree 旧路径已降级为历史来源。 |
| `tts_15s_b_pacing_locked_20260427` | 20260427 B 版 15 秒停顿梗感 TTS 节奏参考 | TTS pacing reference whitelist | `/Users/fan/Documents/视频工厂/dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav` | `true` | 无 | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正 | 锁定的是 TTS 节奏参考，不是最终音色，不代表 `voice_validation = final`，不得写成最终声音通过。 |
| `voice_sample2_cute_guide_voice_candidate_20260426` | 语音样本 2 可爱向导音候选参考 | TTS voice reference whitelist；语音 / 音色候选参考 | `/Users/fan/Documents/视频工厂/dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav` | `true` | `dist/latest_review_pack/summary.json` 中 `custom_voice.voice_masked = qwen-t...ac19`; `target_model = qwen3-tts-vc-realtime-2026-01-15` | `2026-05-04 CST` | `test -f` 已通过；PR #48 TTS voice reference 补充；`dist/latest_review_pack/summary.json` 已记录 candidate reference / custom voice | 这是语音 / 音色候选参考，不是 locked final voice；custom voice 只允许使用脱敏标识 `qwen-t...ac19`；`voice_validation = pending_user_chatgpt_review`，`final_voice_validated = false`，不得写成最终声音通过。 |
| `v31_visual_route_map` | v3.1 视觉路由表 | visual route structure / reference whitelist | `/Users/fan/Documents/视频工厂/dist/latest_review_pack/visual_route_map.json` | `true` | 无 | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正 | 结构地图必须保留；用于区分 cute prompt card、cute info card、sassy reaction card 和真实录屏主体。 |
| `locked_reference_registry` | 锁定参考登记表 | reference whitelist registry | `/Users/fan/Documents/视频工厂/codex_source/locked_reference_registry.md` | `true` | 无 | `2026-05-04 CST` | `test -f` 已通过；PR #48 清库口径修正 | 后续 reference 继承必须读取本 registry；不得把 fixed material anchor 误写成唯一 reference。 |
| `no_zoom_1x_review_frames` | 不放大完整可读 1x 默认视图复审图 | 历史 no_zoom_completeness 1x 默认视图复审图 | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png` | `false` | 无 | `2026-05-03 CST` | `test -f` 未命中；单工作区治理重新验证 | `stale_pending_recheck`：当前唯一正式工作区内未找到该 PNG；不得作为用户可打开路径输出。 |
| `no_zoom_layout_metrics` | 不放大完整可读布局指标 | 历史 no_zoom_completeness 布局指标 JSON | `/Users/fan/Documents/视频工厂/dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json` | `false` | 无 | `2026-05-03 CST` | `test -f` 未命中；单工作区治理重新验证 | `stale_pending_recheck`：当前唯一正式工作区内未找到该 JSON；不得作为用户可打开路径输出。 |

## 4. 20260504 项目升级前清库结果

- `已确认` PR #47 已合入主读取分支，v3.1 元素娃娃开头锚点与开头预览已补入本索引。
- `已确认` 本轮项目升级前清库后，当前唯一固定素材锚点是 `v31_element_doll_opening_anchor`。
- `已确认` `v31_element_doll_opening_preview` 只作为开头预览证据保留。
- `已确认` `fixed_material_anchor（固定素材锚点）` 只有 v3.1 元素娃娃开头；但元素娃娃不是唯一 reference。
- `已确认` round34 旧 817M 本地大包路径已删除；但 `dist/latest_review_pack` 中仍存在的 `round34_middle_preview`、`round34_cut_contact_sheet`、30-32s 问题窗口已恢复为 `path_exists = true`，作为中段剪辑 / 证据窗口 `reference_whitelist`。
- `已确认` PR #7 B、cute card、round34 中段剪辑、TTS 节奏参考、TTS 语音 / 音色候选参考、visual route / registry 仍属于 `reference_whitelist（参考白名单）`；本索引不得把它们误写为废弃，也不得把它们输出成当前固定素材锚点。
- `已确认` TTS reference whitelist 必须拆分：`tts_15s_b_pacing_locked_20260427` 是 pacing reference；`voice_sample2_cute_guide_voice_candidate_20260426` + 脱敏 custom voice `qwen-t...ac19` + `target_model = qwen3-tts-vc-realtime-2026-01-15` 是 voice reference candidate。后者仍为 `pending_user_chatgpt_review`，`final_voice_validated = false`。
- `已确认` PR #46 保留为未来流程 / 教学 / 操作拆解升级方向资料，不作为当前 reference。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 本轮冻结不动。

## 5. 本轮单工作区治理结果

- `已确认` `/Users/fan/Documents` 顶层执行 `find /Users/fan/Documents -maxdepth 1 -name '*视频工厂*' -print` 后，只剩 `/Users/fan/Documents/视频工厂`。
- `已确认` 2026-05-02 的外部目录回收曾先落到：`/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260502/`。
- `已确认` 2026-05-08 起，archive/delete payload 已按用户授权进一步外移到 archive-only 外部目录：`/Users/fan/Documents/视频工厂归档+删除/待用户确认_user_confirmation_required/本地归档_local_archive/`；该路径不是执行工作区，不作为默认读取入口。
- `已确认` 已将非 Git 散目录 / 损坏临时 worktree 残留移入：`/Users/fan/Documents/视频工厂/本地隔离区_local_quarantine/外部散目录待确认_external_dirs_pending_delete_20260502/`。
- `已确认` 本轮未永久删除任何未回收文件；干净 Git worktree 只在无未提交、无未跟踪、无未推送且回收校验通过后执行 `git worktree remove`。
- `待验证` `git worktree list` 仍保留两个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree，因为它们有未跟踪文件，按安全规则保留并等待用户下一轮确认。

## 6. 历史外部来源降权清单

以下路径只作为 `historical_source_path（历史来源路径）` 说明，不再作为 `canonical_local_path` 或默认执行路径：

- `/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430`
- `/Users/fan/Documents/视频工厂_v31_current_baseline_sync_20260502`
- `/Users/fan/Documents/视频工厂_repo_cleanup_old_context_20260502`
- `/Users/fan/Documents/视频工厂_v3_milestone_reference_locks_20260501`
- `/Users/fan/Documents/视频工厂_v31_visual_route_fix`
- `/Users/fan/Documents/视频工厂_v2_candidate_worktree`
- `/Users/fan/Documents/视频工厂_sassy-card-structure-budget-20260428`
- `/Users/fan/Documents/视频工厂_locked_reference_inheritance_20260430`
- `/Users/fan/Documents/视频工厂归档+删除`
- `/Users/fan/Documents/视频工厂-worktrees`
- `/private/tmp/视频工厂_opening_anchor_20260428`
- `/private/tmp/视频工厂_real_ai_experience_mainline_20260428`
- `/private/tmp/视频工厂_scheme_b_v3_diagnostics`
- `/private/tmp/视频工厂_user_readable_map_sync`

## 7. PR #46 降权说明

- `已确认` PR #46：`Record blocked formal short-video auto-flow TTS retry` 当前仍为 `open / draft / not merged`。
- `已确认` PR #46 暂时不作为当前 reference（参考资产），不进入当前主读取分支正式状态。
- `已确认` PR #46 仅保留为 `parallel_future_flow_teaching_asset（未来流程 / 教学 / 操作拆解类视频升级方向资料）`。
- `已确认` PR #46 local fix v3 不写成内容通过，不写成 `send_ready = true`。

## 8. GPT Project 静态包冻结说明

- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 是未追踪静态包文件，本轮冻结不动。
- 本轮不纳入、不删除、不移动、不改名；后续另起 GPT Project 静态包整理任务。

## 9. GPT Project 上传包路径

- `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_latest_video_data_intake/`
- `gpt_project_upload_package_path_exists（路径是否存在）`：`true`
- `gpt_project_upload_package_manifest_path（上传说明清单路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_latest_video_data_intake/上传说明_UPLOAD_MANIFEST.md`
- `gpt_project_upload_package_manifest_exists（上传说明清单是否存在）`：`true`
- `gpt_project_upload_package_verified_at（验证时间）`：`2026-05-15 21:18 CST`
- `gpt_project_upload_package_status（上传包状态）`：`current_latest_static_upload_package`
- `gpt_project_upload_package_contains（本包包含）`：
  - `GPT数据源/00_项目总述.md`
  - `GPT数据源/01_项目系统提示词.md`
  - `GPT数据源/03_总索引与阅读顺序.md`
  - `GPT数据源/08_当前正式事实.md`
  - `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
  - `GPT数据源/11_项目状态动作总控器_机制推理层.md`
  - `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
  - `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
  - `codex_log/current_gray_test_target.md`
  - `codex_log/current_data_goal_anchor.md`
  - `codex_log/latest.md（最新日志）`
  - `codex_log/20260515_latest_video_data_intake.md`
  - `codex_log/supply_requests/20260515_最新视频数据录入_DeepSeek执行前供料_latest_video_data_intake_pre_supply_request.json`
  - `codex_log/supply_requests/20260515_最新视频数据录入_DeepSeek后置风险复核_latest_video_data_intake_post_risk_review_request.json`
  - `review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/`
  - `review_loop/screenshots/V003_本地文件优化实用分享_latest_practical_video_20260514/`
  - `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/pre_supply/latest_supply_pack.md`
  - `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/pre_supply/latest_supply_pack.json`
  - `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/pre_supply/latest_supply_manifest.json`
  - `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/post_risk_review/latest_supply_pack.md`
  - `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/post_risk_review/latest_supply_pack.json`
  - `dist/deepseek_runtime_validation/20260515_latest_video_data_intake/post_risk_review/latest_supply_manifest.json`
  - `dist/deepseek_readonly_explorer/latest_prefetch_context_pack.md`
  - 本文件的当前路径索引副本
- `previous_gpt_project_upload_package_path（上一版 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_deepseek_runtime_provider/`
- `previous_gpt_project_upload_package_path_exists（上一版路径是否存在）`：`true`
- `previous_gpt_project_upload_package_status（上一版状态）`：`historical_previous_package_not_latest`
- `previous_gpt_project_upload_package_note（上一版说明）`：
  20260515 DeepSeek runtime provider 包已降级为 `historical_previous_package_not_latest`，不再是当前推荐上传目录。
- `older_current_data_goal_anchor_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_current_data_goal_anchor/`
- `older_current_data_goal_anchor_package_path_exists（更早路径是否存在）`：`true`
- `older_current_data_goal_anchor_package_status（更早路径状态）`：`historical_previous_package_not_latest`
- `older_current_data_goal_anchor_previous_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_deepseek_safe_loader_data_goal_anchor/`
- `older_current_data_goal_anchor_previous_package_path_exists（更早路径是否存在）`：`true`
- `older_current_data_goal_anchor_previous_package_status（更早路径状态）`：`historical_previous_package_not_latest`
- `older0_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_goal_execution_bus/`
- `older0_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `older0_gpt_project_upload_package_status（更早路径状态）`：`historical_previous_package_not_latest`
- `older1_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_mandatory_deepseek_supply_loop/`
- `older1_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `older1_gpt_project_upload_package_status（更早路径状态）`：`historical_previous_package_not_latest`
- `older_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260515_data_flywheel_bridge_thresholds/`
- `older_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `older_gpt_project_upload_package_status（更早路径状态）`：`historical_previous_package_not_latest`
- `older2_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_state_router/`
- `older2_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `older3_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512/`
- `older3_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `older4_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_reference_contract/`
- `older4_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `oldest_gpt_project_upload_package_path（更早 GPT Project 上传包路径）`：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260509/`
- `oldest_gpt_project_upload_package_path_exists（更早路径是否存在）`：`true`
- `old_static_package_path（旧静态包路径）`：
  `/Users/fan/Documents/视频工厂/GPT 数据源/`
- `old_static_package_path_exists（旧静态包路径是否存在）`：`true`
- `dynamic_repo_fact_package_path（GitHub 动态事实目录）`：
  `/Users/fan/Documents/视频工厂/GPT数据源/`
- `dynamic_repo_fact_package_path_exists（动态事实目录是否存在）`：`true`
- `upload_policy（上传策略）`：
  20260515 latest video data intake 包是当前推荐上传目录；20260515 DeepSeek runtime provider 包、current data goal anchor 包、DeepSeek safe loader + data goal anchor 包、data goal execution bus 包、mandatory DeepSeek 包、数据飞轮包与旧 20260512 / 20260509 上传包只作为 historical / previous package；旧静态包不是本轮推荐上传目录；动态事实目录不是 GPT Project 上传目录；用户上传时只使用 `gpt_project_upload_package_canonical_path`。
- `address_rule（地址规则）`：
  以后 GPT Project 上传包地址必须由 Codex 本地审计或 `current_local_artifact_paths.md` 给出，ChatGPT 不得凭记忆口头给本地地址。
- `boundary（边界）`：
  本路径只证明本地静态上传包已生成且路径存在，不代表用户已经上传到 GPT Project UI，也不代表 GPT Project UI 已同步成功；GitHub main 仍是主事实源；本包不代表当前视频内容验证通过，不代表 `send_ready = true`，不代表 `publish_status` 成功推进，不代表 `voice_validation`、`final_voice_validated` 或 `visual_master_locked` 已通过。本包记录 V003 早期截图数据已录入，DeepSeek 执行前供料与执行后风险复核均为 `deepseek_passed`、`fallback_count = 0`、`blocked_count = 0`；但不代表最终发布后复盘完成，也不代表下一条正式文案已决定。

## 10. DeepSeek runtime provider 验证产物

- `artifact_id（产物编号）`: `deepseek_runtime_provider_validation`
- `中文名称`: `DeepSeek runtime provider 多任务真实供料验证`
- `purpose（用途）`: `验证 provider 自动加载、子进程 env 注入、runtime doctor、单任务与多任务真实 DeepSeek 供料`
- `canonical_local_path（首选本地路径）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/`
- `path_exists（路径是否存在）`: `true`
- `runtime_doctor_report_json`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/runtime_doctor_report.json`
- `runtime_doctor_report_md`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/runtime_doctor_report.md`
- `combined_participation_report_json`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/latest_combined_participation_report.json`
- `combined_participation_report_md`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/latest_combined_participation_report.md`
- `task_A_report`: `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/deepseek_runtime_validation_task_A_file_map/participation_report.json`
- `task_B_report`: `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/deepseek_runtime_validation_task_B_data_goal_anchor/participation_report.json`
- `task_C_report`: `/Users/fan/Documents/视频工厂/dist/deepseek_runtime_validation/deepseek_runtime_validation_task_C_risk_review/participation_report.json`
- `verified_at（验证时间）`: `2026-05-15 20:30 CST`
- `runtime_doctor_status`: `ready`
- `key_source`: `project_env`
- `key_git_tracked`: `false`
- `can_call_deepseek`: `true`
- `deepseek_passed_count`: `3`
- `fallback_count`: `0`
- `blocked_count`: `0`
- `status（状态）`: `local_validation_artifact_not_gpt_project_truth`
- `boundary（边界）`: 本路径证明本地 runtime provider 技术验证通过；不代表长期多轮真实任务稳定，也不代表多 agent runtime 已跑通。
- `secret_policy（密钥策略）`: key 来源只记录为 `.env` 文件名；key 值未打印、未写入、未提交；controller / explorer 侧 `env_file_read = false`。

## 11. DeepSeek 真实参与活体测试产物

- `artifact_id（产物编号）`: `deepseek_live_participation_smoke_test`
- `中文名称`: `DeepSeek 真实参与活体测试供料输出`
- `purpose（用途）`: `验证 DeepSeek API 是否真实调用、是否 deepseek_passed、是否不是 fallback_local_only`
- `canonical_local_path（首选本地路径）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_supply_controller/live_smoke_test_20260515/`
- `path_exists（路径是否存在）`: `true`
- `latest_supply_pack_md（供料包 Markdown）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_supply_controller/live_smoke_test_20260515/latest_supply_pack.md`
- `latest_supply_pack_json（供料包 JSON）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_supply_controller/live_smoke_test_20260515/latest_supply_pack.json`
- `latest_supply_manifest_json（供料清单 JSON）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_supply_controller/live_smoke_test_20260515/latest_supply_manifest.json`
- `request_file（测试请求文件）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_supply_controller/deepseek_live_participation_smoke_test_request.json`
- `runner_file（安全加载 runner）`:
  `/Users/fan/Documents/视频工厂/dist/deepseek_supply_controller/run_live_smoke_with_safe_env_loader.py`
- `verified_at（验证时间）`: `2026-05-15 02:27 CST`
- `deepseek_actual_participation`: `deepseek_passed`
- `supply_source`: `deepseek_passed`
- `fallback_status`: `not_used`
- `api_validation`: `passed`
- `context_pack_validation`: `passed`
- `token_usage_expected`: `true`
- `token_usage_should_decrease`: `true`
- `status（状态）`: `local_validation_artifact_not_gpt_project_package`
- `boundary（边界）`: 本路径只是本地 DeepSeek 活体测试产物，不是 GPT Project 上传包；不代表 `multi-agent runtime（多 agent 运行时）` 已稳定跑通，不代表当前视频内容验证通过，不代表可发送状态已通过，不代表发布状态推进。
- `secret_policy（密钥策略）`: key 来源仅记录为 `.env` 文件名；key 值未打印、未写入、未提交；controller / explorer 侧 `env_file_read = false`。

## 12. 最后更新时间

- `2026-05-15 20:35 CST`
