# Review Manifest

review_pack_status: ready_for_user_chatgpt_review
technical_validation: passed_for_internal_reference_migration_clip
content_validation: pending_user_chatgpt_review
send_ready: false
publish_candidate: false

## Review Pack

- output_dir: `dist/guided_proof_reference_migration_new_fourth_episode_20260601_010425/`
- before_original_segment: `before_original_segment.mp4`
- after_reference_migration_segment: `after_reference_migration_segment.mp4`
- before_after_contact_sheet: `before_after_contact_sheet.jpg`
- segment_selection_report: `segment_selection_report.md`
- reference_migration_plan: `reference_migration_plan.md`
- technical_validation_report: `technical_validation_report.json`
- content_review_notes: `content_review_notes.md`
- media_probe: `media_probe.json`
- frame_samples: `frame_samples/`

## Source

- source_video: `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/full.mp4`
- source_narration: `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/narration.wav`
- source_captions: `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/captions.srt`
- selected_timecode: `00:03:40.988-00:04:22.060`

## Mechanisms Migrated

- `active_evidence_window`: passed
- `clean_evidence_container`: passed
- `one_claim_one_highlight`: passed
- `voice_and_subtitle_bridge`: passed
- `low_density_bridge_card`: passed
- `split_screen_or_comparison`: intentionally_not_used_for_this_segment

## Verification Summary

- toolchain_check: passed
- remotion_render: passed
- ffprobe_before: passed
- ffprobe_after: passed
- decode_before: passed
- decode_after: passed
- after_duration: `41.130667s`
- after_resolution: `1920x1080`
- after_aspect_ratio: `16:9`
- after_audio: present
- source_overwrite_check: passed_no_output_written_to_source_path

## Review Boundary

The review pack is an internal reference-migration validation clip only. It does not change formal project status and does not promote `content_validation`, `send_ready`, `publish_candidate`, `voice_validation`, or `visual_master_locked`.
