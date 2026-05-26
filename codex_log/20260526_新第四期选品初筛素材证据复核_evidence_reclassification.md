# 20260526｜新第四期选品初筛素材证据复核

- `task_result.status = completed`
- `video_generated = false`
- `tts_called = false`
- `copy_changed = false`
- `review_pack_path = dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604`
- `evidence_reclassification_report = dist/new_fourth_episode_selection_locked_script_publish_candidate_20260526_171604/evidence_reclassification_report.json`

## 复核结论

- `codex_atlas_operation.status = direct_evidence_present`
- `product_card_processing.status = screenshot_based_product_card_processing_present`
- `sku_evidence.status = table_evidence_passed`
- `candidate/detail/review_table_readability = high_res_source_present_edit_zoom_required_not_missing_material`
- `previous_blockers.resolved = 28`
- `previous_blockers.still_blocked = 0`
- `can_continue_to_publish_candidate_generation = true`
- `next_step = rerun publish candidate generation with existing locked script`

## 证据重新归类

1. `Codex 操作我的电脑`：V001 `00:00-00:12` 与 `01:27-01:33` 可见 ChatGPT Atlas、`已使用 Computer Use`、`已运行命令`、页面已进入选品广场、关键词/搜索框处理和可见样本获取。上一轮把证据标准限定为“Codex 必须全自动逐页翻商品卡”过窄。
2. `进入选品页面 / 输入品类词 / 一张张翻商品卡`：归类为 `screenshot_based_product_card_processing`。V001 有商品卡页面，V003/V004 有商品字段进入候选表、明细表和复查表。`live_browser_page_turning_missing` 不是 blocker。
3. `SKU 复杂度`：V004 `00:27-00:39` 可见 `SKU 数量`、`买错/不适配差评`、`配列 / 轴体 / 兼容`，可作为表格截图证据。
4. `候选表 / 明细表 / 复查表`：原始素材有高分辨率源画面，后续剪辑需要裁切、放大、遮挡隐私并做字幕/卡片避让；这属于执行要求，不再是补素材 blocker。

## 状态边界

- 未修改 `locked_final_script`
- 未修改 `narration_text`
- 未修改 `subtitle_text`
- 未生成 `full.mp4`
- 未生成 `narration.wav`
- 未生成 `captions.srt`
- 未调用 TTS / MiniMax
- 未推进 `send_ready`
- 未推进 `content_validation`
- 未推进 `voice_validation`
- 未推进 `final_voice_validated`
- 未推进 `visual_master_locked`

## 后续生成要求

- 使用现有锁稿重跑正片候选生成。
- 正式声音仍必须走 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd`。
- V003/V004 表格必须裁切/放大，不得全屏小字硬上。
- 账号、路径和敏感商品信息必须遮挡。
- 字幕/卡片不得遮挡核心证据。
- 重跑完整 publish candidate preflight suite。
