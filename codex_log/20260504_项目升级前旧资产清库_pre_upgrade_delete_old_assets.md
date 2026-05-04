# 20260504 项目升级前旧资产清库 pre_upgrade_delete_old_assets

## 1. 本轮结论

- `已确认` PR #47 已先合入 `codex/user-readable-map`，合并提交：`20d9419e0a9ad048075a2138c610472df93051be`。
- `已确认` 本轮清库分支：`codex/pre-upgrade-delete-old-assets-20260504`。
- `已确认` 本轮没有生成视频，没有修改当前发布 / 灰度状态，没有把内容验证写成通过。
- `已确认` 当前唯一固定素材锚点是 `v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）`。
- `已确认` `v31_element_doll_opening_preview（v3.1 元素娃娃开头预览）` 只保留开头预览证据。
- `已确认` PR #46 未合并、未关闭、未删除；只作为未来流程 / 教学 / 操作拆解升级方向资料。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 与整个 `GPT 数据源/` 目录未动。

## 2. 体积变化

| 指标 | 数值 |
| --- | ---: |
| 清理前工作区总量 | `36G` |
| 清理后工作区总量 | `33G` |
| 释放空间 | `约 3G` |
| 未动 `.git/` | `21G` |
| 未动 `素材录制/` | `11G` |

## 3. 实际删除

### 3.1 Git 当前树删除

- `dist/20260414_豆包高效用法_cartoon_ip_formal/`
- `dist/20260417_豆包的正确打开方式_vnext/`
- `dist/formal_api_demo*/`
- `dist/demo/`
- `dist/latest_contact/`
- `dist/latest_first_min/`
- `dist/latest_min2_3/`
- `dist/验证样片_validation_samples/`
- `dist/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/`

### 3.2 本地旧大目录 / 缓存删除

- `视频工厂_元素娃娃1080P复审包_20260428/`
- `本地归档_local_archive/`
- `本地隔离区_local_quarantine/`
- `临时产物_staging/`
- `node_modules/`
- `HyperFrames测试_hyperframes_result_card_component_20260502/`
- `HyperFrames测试_hyperframes_screencast_annotation_20260502/`
- `dist/视频样片_video_samples/`
- `复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/`
- `复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/`
- `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/`

## 4. 保留内核

- `素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4`
- `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4`
- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_local_artifact_paths.md`
- `GPT数据源/`
- `GPT 数据源/`
- 必要源码 / 脚本 / 配置 / 测试

## 5. blocked_unknown

- `素材录制/`：用户录制原始素材，体积约 `11G`，可能有唯一证据价值，本轮不动。
- `.git/`：Git 系统目录，体积约 `21G`，本轮不动，不重写历史。
- `dist/完整成片_full_videos/`：含 PR #46 本地流程教学产物线索，需另轮确认是否归档 / 删除。
- `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`：本轮冻结不动，后续另起 GPT Project 静态包整理任务。

## 6. 状态字段保护

- `已确认` `content_validation` 未写成 `passed`。
- `已确认` `send_ready` 未写成 `true`。
- `已确认` `voice_validation` 未写成 `final`。
- `已确认` 当前发布 / 灰度状态未被改成内容通过。

## 7. 下一个目标

用户 / ChatGPT 复审清库 PR，确认没有误删保留内核；通过后再进入项目升级机制收口。
