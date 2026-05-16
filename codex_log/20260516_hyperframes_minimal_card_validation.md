# 20260516 HyperFrames 最小卡片验证

## 1. 任务定位

- `artifact_type`: `hyperframes_minimal_card_validation（HyperFrames 最小卡片验证）`
- `locked_title`: `AI 的正确用法，大家直接冲就行了`
- `internal_diagnostic_only`: true
- `technical_runtime_validation`: passed
- `hyperframes_minimal_artifact`: generated
- `content_validation`: not_advanced
- `send_ready`: false
- `publish_candidate`: false
- `visual_master_locked`: false

本轮只验证 HyperFrames runtime 能否真实生成 1 张 `judgment_card（判断卡）`、1 张 `summary_card（总结卡）` 与最小合并预览，不生成正式视频，不修改已发布视频，不修改 `dist/latest_review_pack/`，不推进任何正式运营内容状态。

## 2. route_decision

```text
route_decision:
  project_route: video_factory
  task_type:
    - hyperframes_runtime_validation
    - minimal_artifact_generation
    - card_motion_baseline_test
  responsibility_layer:
    - execution_layer
    - validation_layer
  large_task_gate:
    triggered: false
    reason: 本轮只做最小产物验证，不做正式视频
    lane_recommendation: standard_lane
    parallel_recommendation: serial_only
  codex_judgment_permission_gate:
    codex_judgment_permission_matrix_read: read_ok
    permission_boundary_violations: none_detected
    copy_change_request_required: false
    blocked_by_permission_boundary: false
  hyperframes_card_motion_gate:
    hyperframes_card_motion_baseline_read: read_ok
    judgment_card_hyperframes_required: true
    summary_card_hyperframes_required: true
    hyperframes_runtime_gate: passed
    hyperframes_runtime_status: found_and_callable
    fallback_static_card_authorized_by_user: false
    blocked_if_hyperframes_required_but_missing: true
  execution_permission: allowed_for_internal_diagnostic_only
```

## 3. impact_check_report

```text
impact_check_report:
  hyperframes_runtime_found: found_via_npx_hyperframes_cli
  hyperframes_skill_found: found_global_plugin_skill_and_hyperframes_cli_skill
  package_dependency_found: false
  script_entry_found: false before this task; true after adding scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py
  can_generate_minimal_artifact: true
  blocked_if_runtime_missing: true
  planned_output_paths:
    - dist/hyperframes_minimal_validation/01_judgment_card/
    - dist/hyperframes_minimal_validation/02_summary_card/
    - dist/hyperframes_minimal_validation/combined_preview.mp4
    - dist/hyperframes_minimal_validation/manifest.json
    - dist/hyperframes_minimal_validation/review_manifest.md
```

## 4. runtime check

- `package_dependency_found`: false；仓库根 `package.json` 只有 `ffmpeg-static`，没有 HyperFrames 依赖。
- `script_entry_found`: 本轮前未发现；本轮新增 `scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py` 作为可复跑的 runtime adapter。
- `skill_found`: true；读取了全局 HyperFrames skill 和 HyperFrames CLI skill。
- `runtime_status`: `found_and_callable`
- `callable`: true
- `runtime_entry`: `npx --yes hyperframes@0.6.12 render`
- `doctor_note`: HyperFrames doctor 显示 CLI、Chrome、FFmpeg、FFprobe 可用；内存低是风险提示，但本轮 draft / single worker 渲染通过。

## 5. generated_artifacts

```text
dist/hyperframes_minimal_validation/
  01_judgment_card/
    judgment_card.mp4
    judgment_card_manifest.json
    judgment_card_preview.png
  02_summary_card/
    summary_card.mp4
    summary_card_manifest.json
    summary_card_preview.png
  combined_preview.mp4
  combined_preview_frame_1.png
  combined_preview_frame_2.png
  DESIGN.md
  index.html
  manifest.json
  review_manifest.md
  runtime_logs/
  source/
```

## 6. validation_result

- `npx --yes hyperframes@0.6.12 lint`: passed for judgment card, summary card, combined preview.
- `npx --yes hyperframes@0.6.12 inspect --samples 8`: passed; 0 layout issues for all three renders.
- `npx --yes hyperframes@0.6.12 render --quality draft --fps 30 --workers 1`: passed for all three renders.
- `npm run check`: passed；HyperFrames lint 0 errors / 0 warnings，validate no console errors 且 70 text elements pass WCAG AA，inspect 0 layout issues。
- `judgment_card.mp4`: 1920x1080, 3.2s, 30fps, h264, decodable, audio_present=false.
- `summary_card.mp4`: 1920x1080, 3.2s, 30fps, h264, decodable, audio_present=false.
- `combined_preview.mp4`: 1920x1080, 6.766667s, 30fps, h264, decodable, audio_present=false.
- `manifest.json`: JSON parse passed.
- `judgment_card_manifest.json`: JSON parse passed.
- `summary_card_manifest.json`: JSON parse passed.
- `git diff --check`: passed.

## 7. copy boundary

- `locked_title`: `AI 的正确用法，大家直接冲就行了`
- `judgment_card_text`: `AI 的正确用法：先判断，再执行`
- `summary_card_text`: `目标说清楚，下一步能验证，就可以冲`
- `title_unchanged`: true
- `card_text_semantic_match`: true
- `allowed_copy_changes_used`: 仅为画面排版拆分短语和轻微标点呈现；未改变原意。
- `forbidden_copy_changes_triggered`: false

## 8. actual output type

- `actual_output_type`: `real_hyperframes_motion`
- `fallback_static_card`: false
- `static_card_only`: false
- `runtime_adapter`: `scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py`

本轮不是“普通静态卡片冒充 HyperFrames”。产物由 HyperFrames CLI 渲染为 mp4，并保留 lint / inspect / render 日志。

## 9. status_boundary

- 未推进 `content_validation（内容验证）`
- 未推进 `send_ready（可发送状态）`
- 未写可发布候选片待复审状态
- 未推进 `voice_validation（声音验证）`
- 未推进 `final_voice_validated（最终声音验证）`
- 未推进 `visual_master_locked（视觉母版锁定）`
- 未写 HyperFrames 长期稳定性结论
- 未修改已发布视频
- 未修改 `dist/latest_review_pack/`

## 10. next_target

下一步如果要进入真实视频执行，需要把本轮最小 runtime adapter 升级为正式视频执行链的一部分，并继续要求：

1. `card_placement_decision（卡片位置判断）` 先选中 `judgment_card / summary_card`；
2. `hyperframes_runtime_status = found_and_callable`；
3. `hyperframes_visual_quality_gate（视觉质量闸门）` 通过；
4. `subtitle_card_overlap_check（字幕卡片重叠检查）` 通过；
5. 不得把内部诊断产物写成正式发布候选片。
