# HyperFrames 最小卡片验证 review_manifest

- `title`: AI 的正确用法，大家直接冲就行了
- `artifact_type`: `hyperframes_minimal_card_validation`
- `internal_diagnostic_only`: true
- `technical_runtime_validation`: `passed`
- `hyperframes_runtime_status`: `found_and_callable`
- `runtime_entry`: `npx --yes hyperframes@0.6.12 render`
- `fallback_static_card`: false
- `content_validation`: not_advanced
- `send_ready`: false
- `publish_candidate`: false
- `visual_master_locked`: false

## Cards

### judgment_card
- `text`: AI 的正确用法：先判断，再执行
- `motion_type`: judgment_card_motion
- `output_path`: `dist/hyperframes_minimal_validation/01_judgment_card/judgment_card.mp4`
- `validation_status`: `passed`

### summary_card
- `text`: 目标说清楚，下一步能验证，就可以冲
- `motion_type`: summary_card_motion
- `output_path`: `dist/hyperframes_minimal_validation/02_summary_card/summary_card.mp4`
- `validation_status`: `passed`

## Combined Preview
- `output_path`: `dist/hyperframes_minimal_validation/combined_preview.mp4`
- `validation_status`: `passed`

## Runtime Checks
- `judgment_lint`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/judgment_card_lint.log`
- `judgment_inspect`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/judgment_card_inspect.log`
- `judgment_render`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/judgment_card_render.log`
- `summary_lint`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/summary_card_lint.log`
- `summary_inspect`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/summary_card_inspect.log`
- `summary_render`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/summary_card_render.log`
- `combined_lint`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/combined_preview_lint.log`
- `combined_inspect`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/combined_preview_inspect.log`
- `combined_render`: exit_code=0, log=`dist/hyperframes_minimal_validation/runtime_logs/combined_preview_render.log`

## Status Boundary

- 本产物不是正式视频。
- 本产物不是正式发布候选片。
- 本产物不推进 `content_validation`。
- 本产物不推进 `send_ready`。
- 本产物不锁定视觉母版。

## User Visual Review And Minimal Style Lock

- `user_visual_review`: passed
- `reviewer`: user
- `review_basis`: user watched combined_preview and approved
- `hyperframes_minimal_style_baseline`: locked_for_judgment_and_summary_cards
- `judgment_card_motion_minimal_baseline`: locked
- `summary_card_motion_minimal_baseline`: locked
- `allowed_hyperframes_visual_skins`: clean_soft, cute_ai_guide
- `not_selected_visual_skin`: sharp_judgment
- `visual_skin_preview_pack`: `dist/hyperframes_minimal_validation/visual_skins_1_3/`

## Still Not Advanced

- `content_validation`: not_advanced
- `send_ready`: false
- `publish_candidate`: false
- `visual_master_locked`: false
- `real_video_execution_chain_integration`: pending
- `long_term_runtime_stability`: pending
