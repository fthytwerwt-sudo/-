# 阿里云剪辑使用审计报告 aliyun_edit_usage_audit

## 1. 本轮范围

- `已确认` 本轮只做只读审计，不删除、不禁用、不修改任何阿里云相关代码、配置或剪辑链路。
- `已确认` 本轮不生成视频、音频、图片，不修改 v3.1 正片，不修改 `dist/latest_review_pack/` 既有产物。
- `已确认` 本轮结论只回答“当前是否仍有阿里云剪辑实际调用证据”，不写成“历史上从未使用”。

## 2. 搜索范围

本轮使用 `rg` 只读搜索仓库文本、脚本、配置、日志、报告和当前复审包文本文件。排除范围：

- `node_modules/`
- `.git/`
- `本地归档_local_archive/`
- `本地隔离区_local_quarantine/`
- `.mp4 / .mov / .wav / .mp3 / .aac / .png / .jpg / .jpeg / .zip`

重点覆盖：

- `codex_source/`
- `GPT数据源/`
- `project_source/`
- `codex_log/`
- `scripts/`
- `config/`
- `tests/`
- `dist/latest_review_pack/*.json`
- `dist/latest_review_pack/*.md`
- `复审包_review_packs/` 的文本 manifest / summary / report
- `治理_reports/`
- `README.md`
- `package.json`
- `package-lock.json`

## 3. 搜索关键词

中文关键词：

- 阿里云剪辑
- 阿里剪辑
- 阿里云视频剪辑
- 阿里云智能媒体服务
- 智能媒体服务
- 云端剪辑
- 云剪辑
- 剪辑服务
- 媒体处理
- 视频合成
- 视频剪辑

英文 / 技术关键词：

- aliyun
- Aliyun
- Alibaba Cloud
- alibaba
- ice
- ICE
- intelligent media
- media service
- media editing
- cloud editing
- cloud render
- cloud rendering
- video editing
- video production
- video compose
- compose
- timeline
- render API
- vod
- oss

## 4. 关键命中摘要

### 4.1 代码层实际调用能力

| 文件 | 行号 | 命中摘要 | 分类 |
| --- | ---: | --- | --- |
| `formal_api_demo_cloud_assembly.py` | 21-22 | 定义 `ALIYUN_ICE_API_VERSION` 与 `ALIYUN_ICE_ENDPOINT_TEMPLATE` | `active_runtime_dependency` |
| `formal_api_demo_cloud_assembly.py` | 54、353-405、439-440 | 读取 `aliyun_ims.cloud_project_name`，调用 `ListEditingProjects`、`UpdateEditingProject`、`SubmitMediaProducingJob`、`GetMediaProducingJob` | `active_runtime_dependency` |
| `formal_api_demo_cloud_assembly.py` | 471-562、596-630、737、830-831 | 读取 `aliyun_oss` 字段，上传 OSS，签名调用 ICE OpenAPI | `active_runtime_dependency` |
| `formal_api_demo_core.py` | 27、1530-1605、4800-4885、5060-5075 | 引入 cloud assembly，设置 assembly gate，要求北京区 `OSS + 云剪` 字段，提示下一步注入 AccessKey 后执行云端导出验证 | `active_runtime_dependency` |
| `scripts/assemble_formal_api_demo.py` | 25 | 命令入口说明正式 assembly 固定为北京区 `OSS + 云剪 cloud-only` | `active_runtime_dependency` |

判断：`部分成立`。仓库里仍保留可运行的阿里云 ICE / OSS 云端 assembly 代码路径，属于当前代码层实际运行依赖；但本轮没有执行该链路。

### 4.2 配置层

| 文件 | 行号 / 字段 | 命中摘要 | 分类 |
| --- | --- | --- | --- |
| `config/formal_api_demo.example.toml` | 241-300 | 示例配置包含 `[aliyun_oss]`、`[aliyun_ims]`、北京区 OSS endpoint、IMS storage address、cloud project name | `configured_but_unused` |
| `config/formal_api_demo.local.toml` | redacted | 本机存在 local config，已只读确认 `[aliyun_oss]` 与 `[aliyun_ims]` 字段存在；未输出 secret 值 | `configured_but_unused` |

判断：`部分成立`。配置字段存在，但本轮没有执行真实云端导出。

### 4.3 当前 v3.1 latest_review_pack

| 文件 | 行号 | 命中摘要 | 分类 |
| --- | ---: | --- | --- |
| `dist/latest_review_pack/summary.json` | 80-84 | 指向 v3.1 timeline 与 run summary；未发现 `assembly_status`、`cloud_assembly`、`provider`、`generation_provider` 等云剪调用字段 | `not_found` |
| `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_run_summary.json` | 20-21、62-63、126-127 等 | 命中 `provider = aliyun_bailian` 与 `api_route_family = aliyun_qwen_realtime_websocket_voice_clone`，属于 TTS / voice clone，不是阿里云剪辑 / ICE assembly | `historical_reference_only` / `not_found_for_editing` |
| `dist/latest_review_pack/review_manifest.md` | 30-39、80 | 只写声音待复审与 custom voice 入片；未发现阿里云剪辑 / ICE 调用记录 | `not_found` |

判断：`未发现当前实际调用证据`。当前 v3.1 复审包中没有发现阿里云剪辑 / ICE / 云剪 assembly 的实际调用记录；命中的阿里百炼内容是 TTS，不等于剪辑服务。

### 4.4 历史日志

| 文件 | 行号 | 命中摘要 | 分类 |
| --- | ---: | --- | --- |
| `codex_log/20260405_ppt_cloud_only_assembly_route.md` | 6-26、57-87、112-122 | 把 pure PPT / 信息卡主线改为北京区 `OSS + 云剪`，记录 IMS / ICE 状态包和后续真实导出验证目标 | `historical_reference_only` |
| `codex_log/20260406_cloud_assembly_permission_blocker_status_sync.md` | 24-39、62-71、86-89 | 记录 `ListEditingProjects` 权限 blocker 和最小 ICE 权限列表 | `historical_reference_only` |
| `codex_log/20260406_cloud_assembly_rerun_success_after_policy_bind.md` | 55、61、63-66、73 | 记录 `ListEditingProjects`、`UpdateEditingProject`、`SubmitMediaProducingJob`、`GetMediaProducingJob` 与一次 cloud-only assembly 成功 | `historical_reference_only` |
| `codex_log/20260408_ai_report_rewrite_trap_50s_real_footage_cloud_sample.md` | 86、118、160 | 记录云剪 visual clip timeline 修正和北京区 `OSS + 云剪 cloud-only` assembly 成功 | `historical_reference_only` |

判断：`历史参考`。历史日志证明仓库曾做过云剪 / ICE 真实导出或验证，但不直接证明当前 v3.1 最新复审包仍在使用阿里云剪辑。

### 4.5 概念 / 目标方向

| 文件 | 行号 | 命中摘要 | 分类 |
| --- | ---: | --- | --- |
| `GPT数据源/00_项目总述.md` | 22、26 | 当前正式主线包含 `云端剪辑` | `concept_or_target_only` |
| `GPT数据源/01_项目系统提示词.md` | 18、23、111 | 固定主线为 `API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`，并禁止把云端剪辑写成已稳定跑通 | `concept_or_target_only` |
| `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` | 14、41、204 | 把云端剪辑作为正式组装方向 | `concept_or_target_only` |
| `GPT数据源/08_当前正式事实.md` | 18、179 | 当前正式主需求包含云端剪辑；云端剪辑 runtime 是否稳定跑通仍待验证 | `concept_or_target_only` |
| `project_source/02_term_definitions_and_state_boundaries.md` | 18、44-47 | 定义云端剪辑是方向，不等于稳定跑通事实 | `concept_or_target_only` |

判断：`部分成立`。云端剪辑是当前正式方向，但供应商实际调用不能只由方向表述证明。

## 5. 分类结果

| 分类 | 本轮结论 | 证据摘要 |
| --- | --- | --- |
| `active_runtime_dependency` | `部分成立` | `formal_api_demo_cloud_assembly.py`、`formal_api_demo_core.py`、`scripts/assemble_formal_api_demo.py` 保留阿里云 ICE / OSS 云剪 assembly 可运行代码路径 |
| `configured_but_unused` | `部分成立` | `config/formal_api_demo.example.toml` 与本机 `config/formal_api_demo.local.toml` 存在 `aliyun_oss` / `aliyun_ims` 字段；本轮未执行 |
| `historical_reference_only` | `已确认` | 20260405-20260408 多条日志记录 cloud-only / ICE / OSS 云剪验证和历史成功样本 |
| `concept_or_target_only` | `已确认` | GPT 数据源与 project_source 把云端剪辑写为正式方向，同时强调不能写成已稳定跑通 |
| `not_found` | `未发现当前实际调用证据` | 当前 v3.1 `dist/latest_review_pack` 未发现云剪 / ICE assembly 调用记录；仅发现阿里百炼 TTS / voice clone 记录 |

## 6. 当前是否仍在实际使用阿里云剪辑

最终判断：

- `部分成立` 仓库当前仍保留阿里云 ICE / OSS 云端 assembly 代码路径和配置字段，因此阿里云剪辑不是“完全不存在”。
- `未发现当前实际调用证据` 当前 v3.1 `latest_review_pack` 未发现阿里云剪辑 / ICE assembly 的实际调用记录。
- `历史参考` 20260405-20260408 日志证明历史上做过云剪 / ICE 验证和导出样本。
- `待验证` 后续是否继续把阿里云剪辑作为当前 vNext 实际总装运行链路，需要单独跑云端导出或读取新的执行记录，不能由本轮只读审计直接确认。

## 7. 本轮未做事项

- 未删除阿里云相关代码。
- 未禁用任何配置。
- 未修改剪辑链路。
- 未执行阿里云 API。
- 未把“未发现当前调用”写成“从未使用”。
