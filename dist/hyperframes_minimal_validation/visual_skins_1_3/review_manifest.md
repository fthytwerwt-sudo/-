# HyperFrames 最小卡片视觉皮肤预览包 review_manifest

- `title`: AI 的正确用法，大家直接冲就行了
- `artifact_type`: `hyperframes_minimal_card_visual_skin_review`
- `internal_diagnostic_only`: true
- `user_visual_review`: passed
- `reviewer`: user
- `review_basis`: user watched combined_preview and approved
- `hyperframes_minimal_style_baseline`: locked_for_judgment_and_summary_cards
- `allowed_hyperframes_visual_skins`: clean_soft, cute_ai_guide
- `not_selected_visual_skin`: sharp_judgment
- `actual_output_type`: real_hyperframes_motion
- `fallback_static_card`: false
- `content_validation`: not_advanced
- `send_ready`: false
- `publish_candidate`: false
- `visual_master_locked`: false

## Skin Results

### clean_soft / 干净柔和
- `locked_status`: `allowed_minimal_skin`
- `combined_preview`: `dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/combined_clean_soft.mp4`
- `validation_status`: `passed`
- `judgment_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/judgment_card_clean_soft.mp4` / `passed`
- `summary_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/clean_soft/summary_card_clean_soft.mp4` / `passed`

### cute_ai_guide / 可爱 AI 向导
- `locked_status`: `allowed_minimal_skin`
- `combined_preview`: `dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/combined_cute_ai_guide.mp4`
- `validation_status`: `passed`
- `judgment_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/judgment_card_cute_ai_guide.mp4` / `passed`
- `summary_card`: `dist/hyperframes_minimal_validation/visual_skins_1_3/cute_ai_guide/summary_card_cute_ai_guide.mp4` / `passed`

## Combined Skin Review
- `output_path`: `dist/hyperframes_minimal_validation/visual_skins_1_3/combined_skin_review.mp4`
- `validation_status`: `passed`

## Sharp Judgment Boundary

- `sharp_judgment`: not_selected_this_round
- 不生成默认预览，不写入 allowed locked skins，不作为判断卡 / 总结卡默认皮肤。

## Status Boundary

- 本包不是正式视频。
- 本包不是正式发布候选片。
- 本包不推进 `content_validation`。
- 本包不推进 `send_ready`。
- 本包不锁定视觉母版。
