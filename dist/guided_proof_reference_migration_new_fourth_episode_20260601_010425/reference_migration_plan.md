# Reference Migration Plan

status: implemented_for_internal_validation_clip
content_validation: pending_user_chatgpt_review

## Reference Quality Points

- `active_evidence_window`: use a restrained focus rectangle to show where the viewer should look.
- `clean_evidence_container`: keep the screen recording as the main evidence, framed consistently.
- `one_claim_one_highlight`: avoid multiple competing callouts in the same beat.
- `voice_and_subtitle_bridge`: subtitle text should bridge narration to evidence.
- `low_density_bridge_card`: side card states the current proof relation in short labels.

## Not To Copy

- No copied person, face, host identity, PiP layout, third-party sticker, logo, or platform-specific visual identity from the reference.
- No forced API-generated human route.
- No replacement of real recording with AI image, PPT card, or decorative proof page.
- No full-video production, publish-candidate claim, `send_ready`, or `content_validation=passed`.

## Screen Language Plan

The after clip uses a stable dark matte, a narrow left bridge rail, and one main evidence container. The real new fourth episode recording remains the center of the frame. Bridge copy is intentionally short so it supports the evidence rather than becoming the content.

## Subtitle Guidance Plan

The subtitle layer is placed outside the evidence window, below the recording container. It rewrites each beat into a viewer-facing proof cue:

- "这一步和手动翻不一样"
- "它是在边看边记录"
- "原来是一张商品卡"
- "商品名、客单价、佣金..."
- "这些东西一进表"

## Highlight Plan

Each line group receives one main highlight state:

- opening claim: source screen stays clean while the bridge rail names the proof mode.
- candidate table beat: focus rectangle moves to the sheet area.
- field-list beat: focus window tracks the table rows and field block.
- final judgment beat: focus returns to the source/product evidence.

## Bridge Card Plan

The bridge card stays in the left rail and uses low-density labels:

- `外部模式`: 浏览商品 / 看一眼 / 凭感觉
- `当前变化`: 记录字段 / 进候选表 / 可核对
- `判断结果`: 不靠感觉 / 逐项核对

It is intentionally smaller than the evidence area and never covers the source recording.

## Split Screen Or Comparison Plan

No hard split-screen was used in this validation clip. The selected material already shows source card and output table in the same recording sequence, so a clean evidence container plus active evidence window is more faithful than a fake before/after split.

## Evidence Window Plan

The active evidence window appears only on beats where attention needs steering. It does not remain permanently on screen, because a constant rectangle would become decorative and reduce readability.

## Expected Viewer Feeling

The viewer should feel that the proof point is easier to follow: the same source recording now explains "what changed" and "where to look" without becoming a lecture slide.

## Deviation Check

- real素材仍是主体证据: passed
- no copied reference identity: passed
- no high-density PPT replacement: passed
- no formal status promotion: passed
- content/aesthetic judgment: pending_user_chatgpt_review
