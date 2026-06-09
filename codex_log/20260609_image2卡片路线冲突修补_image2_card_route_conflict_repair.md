# 20260609 image2 卡片路线冲突修补

## 本轮定位

- `project_route = video_factory`
- `task_type = mechanism_or_route_fix + project_file_change + fixture_test_sync`
- `task_result.status = image2_card_route_conflict_repair_completed_pending_git_sync`
- `scope = card_visual_route_mechanism_only`
- `no_image_generated = true`
- `no_video_generated = true`
- `dist_latest_review_pack_modified = false`

## 修补原因

只读冲突审计确认旧机制仍把 `judgment_card / summary_card` 与 HyperFrames 无条件强绑定，导致 image2 即使作为主视觉底图候选，也可能因 HyperFrames runtime 缺失被误阻断。

用户已人工查看本轮 image2 样张，并反馈：审美上能过关。本反馈只支持 image2 进入 `primary_visual_route_candidate（主视觉路线候选）`，不支持写成长期稳定通过。

## 路线修补

```text
card_route_layers:
  visual_base_route:
    preferred_candidate: image2_visual_base_route_candidate
    responsibility: 主视觉 / 底图 / 构图 / 质感 / 社交编辑感
    status: partial
  text_authority_route:
    primary: codex_post_overlay_locked_copy
    exact_text_fallback: HTML/CSS/PIL_exact_text_layer
    responsibility: 准确 locked copy 文字层
  motion_wrapper_route:
    default: none
    optional: HyperFrames_motion_wrapper
    runtime_gate_required_when: motion_wrapper_route = HyperFrames_motion_wrapper
```

## 状态边界

```text
image2_visual_probe_user_aesthetic_passed = true
image2_primary_visual_route_candidate = partial
hyperframes_primary_visual_route = downgraded
hyperframes_motion_wrapper = active
image2_long_term_stable_passed = false
content_validation = not_advanced
send_ready = false
visual_master_locked = false
```

## 新增阻断

- `image2_text_semantic_mismatch_unfixable`
- `generated_fake_data_or_claim`
- `evidence_window_covered`
- `third_party_asset_detected`
- `social_editorial_card_v1_deviation`
- `post_overlay_readability_check_missing`
- `hyperframes_motion_wrapper_selected_but_runtime_missing`

## 保留项

- `social_editorial_card_v1`
- 横屏 `16:9 / 1920x1080`
- `card_budget_gate`
- `cluster_merge_rule`
- `card_placement_decision`
- `evidence_window_protection`
- `locked copy` 语义保护
- 卡片不能替代真实录屏证据
- 卡片不能新增素材里没有的数据、指标或结论

## 本轮修改文件

- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/21_codex_judgment_permission_matrix.md`
- `codex_source/00_codex_readme.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/20_reference_to_execution_contract.md`
- `codex_source/01_execution_rules.md`
- `codex_source/fixtures/codex_judgment_permission_matrix_cases.json`
- `codex_source/fixtures/mechanism_inference_function_cases.json`
- `scripts/卡片判断闸门_card_decision_gate.py`
- `tests/test_card_decision_gate.py`

## 未推进

- 未修改 `dist/latest_review_pack/`
- 未修改 `public/`
- 未生成图片
- 未生成视频
- 未替换现有机制产物
- 未推进 `content_validation / send_ready / visual_master_locked`
