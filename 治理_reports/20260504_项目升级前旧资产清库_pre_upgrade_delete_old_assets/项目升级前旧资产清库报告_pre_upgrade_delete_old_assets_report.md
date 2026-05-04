# 项目升级前旧资产清库报告 pre_upgrade_delete_old_assets_report

## 1. 本轮定位

- `已确认` 本轮目标是项目升级前清库，不生成视频，不继续审片，不重写 Git 历史，不 force push。
- `已确认` PR #47 已先合入 `codex/user-readable-map`，合并提交为 `20d9419e0a9ad048075a2138c610472df93051be`。
- `已确认` 本轮清库分支：`codex/pre-upgrade-delete-old-assets-20260504`。
- `已确认` 当前唯一固定素材锚点：`v31_element_doll_opening_anchor`。
- `已确认` v3.1 开头预览：`v31_element_doll_opening_preview`。
- `已确认` PR #46 只保留为未来流程 / 教学 / 操作拆解升级方向资料，不作为当前 reference。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 与整个 `GPT 数据源/` 本轮冻结不动。

## 2. 清理前体积审计

| 对象 | 清理前体积 | 说明 |
| --- | ---: | --- |
| `/Users/fan/Documents/视频工厂` | `36G` | 工作区总量 |
| `.git/` | `21G` | Git 系统目录，绝对不动 |
| `素材录制/` | `11G` | 用户录制原始素材，列入 blocked_unknown |
| `dist/` | `2.6G` | 旧视频产物与历史样片主清理对象 |
| `视频工厂_元素娃娃1080P复审包_20260428/` | `817M` | 旧 round / 旧复审包，本轮删除 |
| `本地归档_local_archive/` | `217M` | 外部工作区回收物，本轮删除 |
| `本地隔离区_local_quarantine/` | `194M` | 旧隔离区，本轮删除 |
| `复审包_review_packs/` | `89M` | 仅删除旧 v1 / v2 / v3 本地复审包；保留 v3.1 开头预览所在包 |
| `node_modules/` | `45M` | 依赖缓存，本轮删除 |
| `临时产物_staging/` | `41M` | 临时产物，本轮删除 |

## 3. cleanup_plan 清理计划

### 3.1 keep_absolute 绝对保留

| 路径 / 对象 | 中文说明 | 保留原因 |
| --- | --- | --- |
| `素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | v3.1 元素娃娃开头锚点 | 当前唯一固定素材锚点 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4` | v3.1 元素娃娃开头预览 | 开头预览证据 |
| `AGENTS.md` | 仓库入口规则 | 多项目路由入口 |
| `codex_source/00_codex_readme.md` | Codex 执行入口 | 执行层最小入口 |
| `codex_source/01_execution_rules.md` | 执行规则 | 执行边界 |
| `codex_log/latest.md` | 最新摘要 | 新会话最小事实入口 |
| `codex_log/current_local_artifact_paths.md` | 当前本地产物路径索引 | 本地路径真实性入口 |
| `GPT 数据源/` | GPT Project 静态协作包 | 本轮冻结不动 |
| `.git/` / `.github/` | Git / GitHub 系统目录 | 禁止删除 |
| `scripts/` / `config/` / `tests/` / 核心源码文件 | 必要源码 / 脚本 / 配置 / 测试 | 后续项目升级仍可能需要 |

### 3.2 delete_local_large_old_assets 删除本地旧大素材

| 路径 | 清理前体积 | 删除原因 | 二次引用检查结果 |
| --- | ---: | --- | --- |
| `视频工厂_元素娃娃1080P复审包_20260428/` | `817M` | 旧 round / 旧复审包；当前固定素材锚点已在 `素材库_assets/` 内 | 仅作为旧 round / 历史路径被引用；路径索引同步降权为已删除 |
| `本地归档_local_archive/` | `217M` | 外部 worktree 回收物；本轮进入最终清库 | 旧治理报告引用保留为历史记录，不再作为可打开路径 |
| `本地隔离区_local_quarantine/` | `194M` | 旧隔离区；用户本轮授权清理旧 worktree 回收物 | 旧治理报告引用保留为历史记录，不再作为可打开路径 |
| `临时产物_staging/` | `41M` | 临时中间产物 | 未作为当前路径索引 / 当前复审包入口 |
| `node_modules/` | `45M` | 可重新安装依赖缓存 | 未被 Git 跟踪 |
| `HyperFrames测试_hyperframes_result_card_component_20260502/` | `800K` | 旧测试输出 | 未作为当前入口 |
| `HyperFrames测试_hyperframes_screencast_annotation_20260502/` | `56M` | 旧测试输出 | 未作为当前入口 |
| `dist/视频样片_video_samples/` | `396M` | 旧样片缓存 | 未被 Git 跟踪；不是当前路径索引 |
| `复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/` | `19M` | 旧 v1 复审包 | 当前不再作为基线 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/` | `33M` | 旧 v2 复审包 | 当前不再作为基线 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/` | `10M` | 旧 v3 复审包 | 路径索引同步标记已删除 |

### 3.3 git_rm_old_noise 从 GitHub 当前树移除旧噪音

| 路径 | 类型 | 删除方式 | 删除原因 |
| --- | --- | --- | --- |
| `dist/20260414_豆包高效用法_cartoon_ip_formal/` | 旧视频产物 | `git rm -r` | 20260414 旧样片，不是当前事实入口 |
| `dist/20260417_豆包的正确打开方式_vnext/` | 旧 round / 旧视频产物 | `git rm -r` | 已被当前元素娃娃开头锚点口径覆盖 |
| `dist/formal_api_demo*/` | 旧 demo 产物 | `git rm -r` | 历史 demo，不应拖慢默认读取 |
| `dist/demo/` | 旧 demo 产物 | `git rm -r` | 历史 demo，不是当前入口 |
| `dist/latest_contact/` | 旧 latest 指针 | `git rm -r` | 旧产物索引，易误导 |
| `dist/latest_first_min/` | 旧 latest 指针 | `git rm -r` | 旧产物索引，易误导 |
| `dist/latest_min2_3/` | 旧 latest 指针 | `git rm -r` | 旧产物索引，易误导 |
| `dist/验证样片_validation_samples/` | 旧验证样片 | `git rm -r` | 非当前入口 |
| `dist/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/` | 旧 v3 dist 产物 | `git rm -r` | v3 不再作为后续默认基础 |

### 3.4 keep_but_downgrade 保留但降权

| 路径 / 对象 | 当前处理 | 后续用途 |
| --- | --- | --- |
| PR #46 | 未合并、未关闭、未删除；保持 draft / open | 未来流程 / 教学 / 操作拆解升级方向资料 |
| `dist/latest_review_pack/` | 保留 | 当前发布 / 灰度状态轻量证据，避免 `current_publish_target` 出现坏引用 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/` | 保留 | v3.1 开头预览所在包；非当前固定素材全集 |
| `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/` | 保留但降权 | 历史样本说明；不作为当前固定素材锚点 |
| `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/` | 保留但降权 | 历史样本说明；不作为当前固定素材锚点 |
| `codex_source/locked_reference_registry.md` | 保留但加清库后口径 | 旧 reference 仅作历史机制资料；当前固定锚点以元素娃娃开头为准 |

### 3.5 blocked_unknown 不确定，禁止动

| 路径 / 对象 | 不确定原因 | 后续需要用户确认什么 |
| --- | --- | --- |
| `素材录制/` | 11G，含用户录制原始素材，可能有唯一证据价值 | 是否另起原始素材归档 / 外置 / 删除任务 |
| `.git/` | 21G，Git 系统目录 | 如需瘦身只能另起 Git LFS / history 方案；本轮不重写历史 |
| `dist/完整成片_full_videos/` | 含 PR #46 本地流程教学产物线索 | 是否另轮归档 PR #46 本地大产物 |
| `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | GPT Project 静态包未追踪文件 | 后续另起 GPT Project 静态包整理任务 |

## 4. 实际执行清单

### 4.1 实际删除

| 路径 | 大小 | 类型 | 删除原因 | 引用检查结果 |
| --- | ---: | --- | --- | --- |
| `视频工厂_元素娃娃1080P复审包_20260428/` | `817M` | 本地旧复审包 | 旧 round / 旧元素娃娃大包，不是当前固定锚点所在目录 | `current_local_artifact_paths.md` 已将 round34 相关项改为 `path_exists=false` |
| `本地归档_local_archive/` | `217M` | 本地旧归档 | 外部工作区回收物，本轮用户授权清理旧 worktree 回收物 | 旧治理报告保留文字记录，不作为可打开路径 |
| `本地隔离区_local_quarantine/` | `194M` | 本地旧隔离区 | 旧散目录隔离区，本轮用户授权清理 | 旧治理报告保留文字记录，不作为可打开路径 |
| `临时产物_staging/` | `41M` | 临时产物 | 中间缓存，无当前继承价值 | 未命中当前路径索引 |
| `node_modules/` | `45M` | 依赖缓存 | 可重新安装缓存 | 未被 Git 跟踪 |
| `HyperFrames测试_hyperframes_result_card_component_20260502/` | `800K` | 旧测试输出 | 非当前入口 | 未命中当前路径索引 |
| `HyperFrames测试_hyperframes_screencast_annotation_20260502/` | `56M` | 旧测试输出 | 非当前入口 | 未命中当前路径索引 |
| `dist/视频样片_video_samples/` | `396M` | 本地旧样片缓存 | 旧样片缓存，不是当前固定锚点 | 未被 Git 跟踪 |
| `复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/` | `19M` | 旧复审包 | v1 历史包 | 非当前基线 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/` | `33M` | 旧复审包 | v2 历史包 | 非当前基线 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/` | `10M` | 旧复审包 | v3 历史包 | 路径索引已标记 `path_exists=false` |

### 4.2 GitHub 当前树删除

| 路径 | 类型 | 删除方式 | 删除原因 |
| --- | --- | --- | --- |
| `dist/20260414_豆包高效用法_cartoon_ip_formal/` | 旧视频产物 | `git rm -r` | 20260414 旧样片，不是当前事实入口 |
| `dist/20260417_豆包的正确打开方式_vnext/` | 旧 round / 旧视频产物 | `git rm -r` | 已被当前元素娃娃开头锚点口径覆盖 |
| `dist/formal_api_demo*/` | 旧 demo 产物 | `git rm -r` | 历史 demo，不应拖慢默认读取 |
| `dist/demo/` | 旧 demo 产物 | `git rm -r` | 历史 demo，不是当前入口 |
| `dist/latest_contact/` | 旧 latest 指针 | `git rm -r` | 旧产物索引，易误导 |
| `dist/latest_first_min/` | 旧 latest 指针 | `git rm -r` | 旧产物索引，易误导 |
| `dist/latest_min2_3/` | 旧 latest 指针 | `git rm -r` | 旧产物索引，易误导 |
| `dist/验证样片_validation_samples/` | 旧验证样片 | `git rm -r` | 非当前入口 |
| `dist/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/` | 旧 v3 dist 产物 | `git rm -r` | v3 不再作为后续默认基础 |

### 4.3 清理后体积

| 对象 | 清理后体积 | 说明 |
| --- | ---: | --- |
| `/Users/fan/Documents/视频工厂` | `33G` | 释放约 `3G` |
| `.git/` | `21G` | 未动 |
| `素材录制/` | `11G` | blocked_unknown，未动 |
| `dist/` | `1.3G` | 已删除旧噪音，保留 latest / PR46 blocked 等 |
| `复审包_review_packs/` | `27M` | 保留 v3.1 开头预览所在包和少量降权历史说明 |

## 5. 状态字段保护

- `content_validation`：保持未通过 / 灰度测试中，不写成 `passed`。
- `send_ready`：保持 `false`，不写成 `true`。
- `voice_validation`：不写成 `final`。
- 当前发布 / 灰度状态：不改写为内容通过。
