# Previous Parse Failure Report

## prior_parse_status

- `prior_parse_path = codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/`
- `prior_commit = 191f02f431f424af42979830c3194305fb7b5e93`
- `availability_on_main = missing_from_worktree`
- `access_method = git show 191f02f431f424af42979830c3194305fb7b5e93:<path>`
- `new_status = failed_prior_parse / low_trust_reference_summary / diagnostic_reference_only`

## failure_reason

1. `mechanism_name_over_visual_language`: 旧报告大量使用 split_screen、keyword、screen_packaging、rhythm 等机制词，但没有充分说明第一眼画面怎么组成、主对象在哪里、窗口多大、持续多久、如何出现/消失。
2. `insufficient_dynamic_state`: 旧时间线按 40-60 秒大段描述，缺少动态关系：主持人何时变 PIP、证据窗口何时上来、黄线怎么换、reset 如何降密度。
3. `classification_too_early`: 旧分类把 reference_01 写成 main_style_reference，但从源视频重看，reference_03/04 对“教学/证据窗口视觉母版”更直接，reference_01 更适合作为结果 montage 与比较板支持。
4. `side_by_side_missing`: 旧包没有把未来候选片与参考并排检查所需的字段模板落清楚。
5. `visual_first_impression_missing`: 旧报告没有把用户要的“第一眼像不像”拆成构图、重心、密度、颜色权重和注意力路径。

## retained_value

- 旧包的 ffprobe、5s 抽帧、scene 候选和 contact sheet 思路有参考价值。
- 旧包的“不可复制平台 UI / 真人 / logo”边界仍成立。
- 旧包可作为失败样本和诊断材料，不作为本轮主判断。

## replacement_standard

本轮以 `dynamic_visual_master_parse` 替代旧 `deep_parse`：每条 timeline 必须包含 `layout_composition / main_subject_position / evidence_window_position / pip_or_host_position / subtitle_position / typography_style / highlight_style / keyword_badge_style / icon_or_motif / background_layer / depth_and_space / color_weight / information_density / motion_behavior / transition_behavior / pacing_feel / attention_path / viewer_first_impression / why_it_feels_like_reference / what_must_not_be_copied`。
