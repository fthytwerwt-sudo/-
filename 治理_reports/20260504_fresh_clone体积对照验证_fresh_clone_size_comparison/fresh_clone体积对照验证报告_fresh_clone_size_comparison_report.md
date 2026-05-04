# fresh clone体积对照验证报告 fresh_clone_size_comparison_report

## 1. 本轮结论

- PR #48 是否已合并：`已确认` 是。
- PR #48 merge commit：`d2df313920e1d7e4f720db279964d6a2324b06a1`
- PR #49 是否已合并：`已确认` 是。
- PR #49 merge commit：`a1981935e404a78377e121b0643601cad01e483a`
- fresh clone 是否完成：`已确认` 是。
- fresh clone 目录：`/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504`
- 是否替换正式工作区：`已确认` 否。
- 是否删除正式工作区：`已确认` 否。
- 是否执行 Git GC / prune / repack：`已确认` 否。
- 是否执行历史重写：`已确认` 否。
- 是否执行 Git LFS 迁移：`已确认` 否。
- 是否修改当前发布状态：`已确认` 否。

## 2. PR #48 合并验证

- fixed_material_anchor / reference_whitelist 是否已区分：`已确认` 是。`v31_element_doll_opening_anchor` 是唯一固定素材锚点，但不是唯一 reference。
- TTS pacing / TTS voice 是否已区分：`已确认` 是。`tts_15s_b_pacing_locked_20260427` 是 pacing reference；`voice_sample2_cute_guide_voice_candidate_20260426` + 脱敏 custom voice `qwen-t...ac19` + `target_model = qwen3-tts-vc-realtime-2026-01-15` 是 voice reference candidate。
- round34 中段最小参考是否保留：`已确认` 是，`dist/latest_review_pack/middle_preview.mp4` 与 `dist/latest_review_pack/cut_contact_sheet.jpg` 存在，路径索引为 `path_exists = true`。
- PR #7 B 是否保留：`已确认` 是，`复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` 存在。
- cute card 是否保留：`已确认` 是，正反提示卡参考文件存在。
- TTS pacing 是否保留：`已确认` 是，`dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav` 存在。
- TTS voice candidate 是否保留：`已确认` 是，`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav` 存在。
- GPT 静态包是否未动：`已确认` 是，`GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 仍为 `untracked / frozen / untouched`。
- 当前发布状态是否未变：`已确认` 是，`codex_log/current_publish_target.md` 与 `codex_log/current_publish_target_light_evidence.md` 无 diff。

## 3. PR #49 合并验证

- 是否只读审计：`已确认` 是，PR #49 只新增 Git 历史大文件审计 dated log、治理报告，并更新 `codex_log/latest.md`。
- 是否未执行 Git 清理：`已确认` 是，未执行 `git gc`、`git prune`、`git repack`、`git lfs migrate`、`filter-repo`、`filter-branch`、BFG 或 force push。
- `.git` 主因是否写清：`已确认` 是。
- `tmp_pack_*` garbage 是否写清：`已确认` 是，正式工作区 `tmp_pack_*` 约 `15.49 GiB`。
- 下一步 fresh clone 对照是否写清：`已确认` 是。

## 4. fresh clone 体积对照

| 项目 | 正式工作区 | fresh clone | 差异 |
| --- | ---: | ---: | ---: |
| 总目录大小 | `33G` | `980M` | fresh clone 约少 `32G` |
| `.git` | `21G` | `896M` | fresh clone 约少 `20G` |
| `.git/objects` | `21G` | `896M` | fresh clone 约少 `20G` |
| `.git/objects/pack` | `19G` | `896M` | fresh clone 约少 `18G` |
| 当前工作树 | `12.18 GiB` | `0.08 GiB` | fresh clone 约少 `12.1 GiB` |

补充指标：

| 指标 | 正式工作区 | fresh clone |
| --- | ---: | ---: |
| `.git/objects/pack/tmp_pack_*` 数量 | `28` | `0` |
| `.git/objects/pack/tmp_pack_*` 体积 | `15.49 GiB` | `0` |
| `git count-objects -vH` garbage | `67` | `0` |
| `git count-objects -vH` size-garbage | `15.51 GiB` | `0 bytes` |
| `素材录制/` | `11G` | fresh clone 不含该本地原始素材目录 |

## 5. 结论判断

- `.git 21G` 是否主要来自当前本地 tmp_pack garbage：`已确认` 是。正式工作区有 `28` 个 `tmp_pack_*`，约 `15.49 GiB`；fresh clone 为 `0`。
- fresh clone 是否显著变小：`已确认` 是。fresh clone `.git` 为 `896M`，远低于正式工作区 `.git` 的 `21G`。
- 是否建议迁移到 fresh clone：`部分成立`。从体积角度建议下一轮以 fresh clone 作为 clean workspace 候选；但迁移前必须确认冻结未追踪文件、用户录制素材、未纳入 Git 的本地必要资产和当前分支 / PR 状态。
- 是否仍需要 Git LFS / history rewrite：`当前不建议直接做`。fresh clone 已证明远端当前主线可降到 `896M` 级别；除非后续仍需压缩远端历史或多分支历史，否则不应先做高风险 history rewrite。
- 是否需要先处理 `素材录制/`：`待用户确认`。正式工作区仍有 `素材录制/` 约 `11G`，这是用户录制原始素材，不应默认删除或移动。

## 6. 风险与建议

主路线：
- 动作：下一轮做“clean clone 工作区迁移确认”，以 `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504` 为候选，核对冻结文件、本地素材、路径索引和必要本地资产后，再决定是否切换正式工作区。
- 为什么：fresh clone 已把 `.git` 从 `21G` 降到 `896M`，且不需要 Git 历史重写。
- 做到哪算完：新 clean workspace 能满足主读取分支、reference whitelist、本地路径索引和冻结 GPT Project 静态包处理要求；旧正式工作区在用户确认前仍保留。
- 风险：如果直接迁移，可能遗漏未跟踪但有价值的本地素材或冻结静态包；必须先做迁移清单。

备选路线：
- 动作：仅当 fresh clone 迁移后仍因远端历史过大或协作政策需要，才另起 Git LFS / history rewrite 设计任务。
- 触发条件：clean clone `.git` 仍不可接受，或 GitHub 远端需要长期治理大文件历史。

## 7. 本轮未执行动作确认

- 未删除正式工作区
- 未替换正式工作区
- 未执行 Git GC
- 未执行 Git prune
- 未执行 Git repack
- 未执行 Git LFS migrate
- 未执行 filter-repo / filter-branch / BFG
- 未 force push
- 未修改当前发布状态

## 8. Git 同步

- commit SHA：`8510711f9eb4003a765757e250d3fcc903ecd48b`（PR #50 fresh clone 对照报告初始提交）
- 是否已 push：已 push
- PR 链接：`https://github.com/fthytwerwt-sudo/-/pull/50`
- 是否已同步到 `codex/user-readable-map`：待本轮合并 PR #50 后同步；合并后以 merge commit 为准

## 9. 下一个目标

用户 / ChatGPT 复审 fresh clone 对照报告，再决定是否迁移到 fresh clone 工作区，或继续处理 `素材录制/` 原始素材。
