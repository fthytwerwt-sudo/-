# 20260409｜GPT 数据源信息层同步到仓库

## 任务性质

- 仓库信息层同步任务
- 不是代码实现任务
- 不是 provider / runtime 验证任务
- 不是样片执行任务

## 本轮源事实

本轮唯一上游源事实为：

- `GPT 数据源/` 当前 25 份中文文件

本轮同步目标为：

1. 用这 25 份文件重写 `project_source/`
2. 再用同步后的 `project_source/` 反写 `codex_source/`
3. 更新 `codex_log/latest.md`
4. 同步 `codex/user-readable-map`

## 本轮主要改动

### 一、project_source

- 新增：
  - `project_source/02_term_definitions_and_state_boundaries.md`
  - `project_source/07_current_formal_facts.md`
  - `project_source/09_target_state_plan.md`
  - `project_source/11_result_diagnosis_map.md`
  - `project_source/12_review_role_split_and_workflow.md`
  - `project_source/15_distribution_and_commercialization_rules.md`
  - `project_source/19_ai_capability_boundary_rules.md`
  - `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
  - `project_source/23_scene_and_failure_experience_material_bank.md`
- 重写：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/02_scene_mode_templates.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/05_psychology_execution_rules.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/10_video_review_record_template.md`
  - `project_source/13_stage_and_acceptance_gates.md`
  - `project_source/14_content_review_and_loop_governance_rules.md`
  - `project_source/16_presentation_routing_rules.md`
  - `project_source/18_visual_motion_and_information_density_rules.md`
  - `project_source/21_topic_selection_and_copywriting_rules.md`
  - `project_source/22_copy_mode_routing_rules.md`
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - `project_source/25_ai_knowledge_video_value_rules.md`
- 删除旧口径文件：
  - `project_source/07_user_readable_repo_map.md`
  - `project_source/09_tts_voice_target_v1.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `project_source/17_white_collar_ppt_style_rules.md`
  - `project_source/19_human_self_footage_hybrid_mainline_rules.md`

### 二、codex_source

- 更新：
  - `codex_source/00_codex_readme.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_source/05_runtime_and_artifact_rules.md`
  - `codex_source/07_formal_api_demo_target_plan.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - `codex_source/12_codex_known_state_three_layer_rules.md`

### 三、日志

- 重写：
  - `codex_log/latest.md`
- 新增：
  - `codex_log/20260409_gpt_data_source_info_sync_to_repo_layers.md`

## 本轮明确替换掉的旧仓库口径

- 旧“人物 / 用户本地录制素材 / 少量 PPT”的默认主线表述
- 旧“cloud-only 更像当前已跑通事实”的表述
- 旧“当前正式事实 / 目标态计划 / 历史说明”混写
- 旧“信息同步完成 ≈ 代码已跑通 / 样片已验证”的误读

## 当前仍待验证的事项

- `待验证` `云端剪辑 / cloud-only` 的 runtime 与 provider 真实可用性
- `待验证` `API 生成真人` 的具体 provider / 模型执行链路
- `待验证` TTS / provider 配额与真实 generation
- `待验证` 样片质量是否真实过线

## 本轮状态

- 仓库状态：
  - 信息层已同步
- 非本轮完成项：
  - 代码实现验证
  - provider 验证
  - runtime 验证
  - 样片验证
