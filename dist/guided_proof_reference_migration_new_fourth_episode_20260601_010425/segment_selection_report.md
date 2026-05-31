# Segment Selection Report

status: selected
task_scope: internal_reference_migration_validation_clip
content_validation: pending_user_chatgpt_review

## Selected Segment

- source_material: `dist/new_fourth_episode_selection_publish_candidate_rerun_20260526_231105/full.mp4`
- selected_timecode: `00:03:40.988-00:04:22.060`
- selected_duration_seconds: `41.072`
- caption_range: `captions.srt` entries `76-93`
- before_output: `before_original_segment.mp4`
- after_output: `after_reference_migration_segment.mp4`

## Why This Segment

This section is the clearest internal proof point for reference-migration testing because the narration moves from manual browsing to structured Codex-assisted evaluation:

- manual browsing: "边看边想"
- Codex behavior: "边看边记录"
- visible transition: product cards become a candidate table
- evaluation layer: price, commission, sales signal, store score, product score, return risk, content feasibility

It has enough real screen evidence to support guided proof editing without replacing the evidence with PPT cards or AI-generated visuals.

## Source Captions Covered

```text
00:03:40,988 --> 00:03:43,764
我自己看的时候，是边看边想。

00:03:43,764 --> 00:03:47,046
Codex 做的时候，是边看边记录。

00:03:47,046 --> 00:03:50,327
它会把这些商品先整理成一张候选表。

00:03:50,447 --> 00:03:57,403
原来在页面上，它们只是一张张商品卡。
到了表格里，就变成了一行一行可以判断的记录。

00:03:57,403 --> 00:04:13,326
商品名、客单价、佣金空间、销量信号、店铺分、商品分、
退货风险、内容能不能拍、为什么留下、为什么不能直接上。

00:04:15,103 --> 00:04:22,060
这些东西一进表，选品这件事就不再是靠感觉了。
它变成了一个可以逐项核对的判断过程。
```

## Original Segment Problems

- Core evidence exists, but the viewer has to infer the current proof point from the full screen.
- The transition from product card to table is visible but not guided enough.
- The original subtitle layer records speech but does not actively direct attention.
- Evidence changes happen quickly, so the important table fields can feel flat or easy to miss.

## Reference Mechanisms To Migrate

- `active_evidence_window`: moving focus window over the evidence area.
- `clean_evidence_container`: stable screen container that keeps the recording readable.
- `one_claim_one_highlight`: one primary visual emphasis per line group.
- `voice_and_subtitle_bridge`: subtitle line summarizes the current proof point, not just transcription.
- `low_density_bridge_card`: small side card only names the current proof relation.

## Selection Verdict

selected_for_internal_clip: true
blocked_reason: none
publish_candidate_status: not_publish_candidate
