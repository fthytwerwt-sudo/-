# V002 抖音审核通知字段提取 report douyin notice extract

## 记录原则

- 本报告记录用户本轮提供的抖音审核通知截图可识别字段。
- 用户未向 Codex 提供截图原图，因此不编造截图路径。
- 直接审核原因只记录为平台通知中的 `violation_reason（违规原因）`，不扩写成“AI 教程违规已确认”或“未标注 AI 导致已确认”。
- 对可能触发点只写 `preliminary_judgment（初步判断）` 或 `推测`，不得写成确定触发帧。

## 截图文件状态

| field（字段） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| screenshot_file_status（截图原图状态） | missing_user_not_provided（截图原图未提供给 Codex） | missing_user_not_provided |
| screenshot_path（截图路径） | missing_user_not_provided（未提供，未编造路径） | missing_user_not_provided |

## 平台审核通知字段

| field（字段） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| video_title（视频标题） | 自动流的最简单流程 | extracted_from_screenshot |
| publish_time（发布时间） | 2026-05-04 17:00:08 | extracted_from_screenshot |
| platform（平台） | 抖音 | extracted_from_screenshot |
| notice_type（通知类型） | 作品审核通知 | extracted_from_screenshot |
| review_result（审核结果） | 减少作品推荐 | extracted_from_screenshot |
| violation_reason（违规原因） | 引导至风险不可控渠道 | extracted_from_screenshot |
| reason_surface（触发位置） | 画面 | extracted_from_screenshot |
| platform_reason_text（平台原因原文） | 引导用户脱离平台至其他渠道交易，或引导下载/使用第三方软件，平台无法保证双方权益，易造成人身/财产安全风险。 | extracted_from_screenshot |
| platform_modification_advice（平台修改建议） | 为保障双方权益，请勿发布脱离平台至其他渠道交易、或引导下载/使用第三方软件的内容。 | extracted_from_screenshot |
| appeal_entry（申诉入口） | 截图可见“查看申诉” | extracted_from_screenshot |
| ai_label_status（AI 标识状态） | 第二张截图可见“作者声明：内容由 AI 生成” | extracted_from_screenshot |
| ai_label_record_status（AI 标识记录状态） | extracted_from_screenshot（已从截图提取） | extracted_from_screenshot |

## 平台举例字段

| item（项） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| platform_example_1（平台举例 1） | 在作品或个人主页中，引导至第三方平台、线下等渠道完成交易。 | extracted_from_screenshot |
| platform_example_2（平台举例 2） | 引导用户下载或前往使用其他应用程序、小程序、网站等。 | extracted_from_screenshot |

## 画面可识别内容

| field（字段） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| visible_video_context_01（画面内容 01） | 视频页显示“SOLO Coder” | extracted_from_screenshot |
| visible_video_context_02（画面内容 02） | 画面中出现“视频 vlog” | extracted_from_screenshot |
| visible_video_context_03（画面内容 03） | 画面中出现“vlog_automation_workflow” | extracted_from_screenshot |
| visible_video_context_04（画面内容 04） | 画面中出现命令片段：mkdir -p | extracted_from_screenshot |
| visible_video_context_05（画面内容 05） | 画面中出现任务列表：0/11 已完成 | extracted_from_screenshot |
| visible_video_context_06（画面内容 06） | 画面中出现“创建Vlog自动化生产流的核心项目结构和配置文件” | extracted_from_screenshot |
| visible_video_context_07（画面内容 07） | 画面中出现“实现全局人设锚定模块” | extracted_from_screenshot |
| visible_video_context_08（画面内容 08） | 画面中出现“实现Vlog选题与叙事线生成模块” | extracted_from_screenshot |
| visible_video_context_09（画面内容 09） | 画面中出现“实现Vlog分镜与标准化脚本生成模块” | extracted_from_screenshot |
| visible_video_context_10（画面内容 10） | 画面中出现“实现素材智能匹配与调度模块” | extracted_from_screenshot |
| visible_video_context_11（画面内容 11） | 画面中出现“实现Vlog专属自动化后期模块” | extracted_from_screenshot |
| visible_video_context_12（画面内容 12） | 画面中出现“实现成片与运营物料导出模块” | extracted_from_screenshot |
| visible_video_context_13（画面内容 13） | 画面下方可见“公开” | extracted_from_screenshot |
| visible_video_context_14（画面内容 14） | 画面下方可见“减少作品推荐” | extracted_from_screenshot |

## 用户补充数据与计算字段

| field（字段） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| play_count（播放量） | 39 | user_provided |
| like_count（点赞数） | 5 | user_provided |
| favorite_count（收藏数） | 8 | user_provided |
| like_rate（点赞率） | 12.82% | calculated_from_fields |
| favorite_rate（收藏率） | 20.51% | calculated_from_fields |
| like_plus_favorite_action_rate（点赞 + 收藏动作率，非去重） | 33.33% | calculated_from_fields |

## 外部规则桥接摘要

| field（字段） | value（值） | source_status（来源状态） |
| --- | --- | --- |
| external_rule_ai_label（AI 内容标识规则） | 使用 AIGC 辅助创作本身不违规，但发布 AI 生成视频、图像、文本、音频等内容需要主动添加标识。 | external_source_checked |
| external_rule_aigc_label_method（国家 AIGC 标识规则） | 视频生成合成内容应在起始画面和播放周边适当位置添加显著标识，用户发布生成合成内容应主动声明并使用标识功能。 | external_source_checked |
| external_rule_external_channel（外部渠道规则） | 平台通知文本指向“引导至风险不可控渠道 / 第三方软件 / 脱离平台交易”风险桶。 | extracted_from_screenshot |
| external_rule_ai_account_governance（AI 起号治理） | 抖音曾专项治理 AI 视频账号售卖教程、AI 账号秘籍传授、引导规避平台 AI 标注、转让销售 AI 虚拟账号等行为。 | external_source_checked |

## 初步判断记录

- `部分成立` 本次直接审核原因应优先记录为 `external_channel_or_third_party_software_risk（外部渠道 / 第三方软件风险）` + `policy_distribution_limited（平台审核减推 / 分发受限）`。
- `已确认` 截图可见 AI 标识，因此不得优先写成“未标注 AI 导致”。
- `待验证` 可能触发点来自画面中的第三方工具界面、自动化生产流、命令行、项目结构、工具名称或平台对“引导下载 / 使用第三方软件”的误判。
- `待验证` 具体触发帧未确认，不能写成已确认事实。

## 外部来源

- 抖音关于升级 AI 内容标识功能的公告转述页：`https://finance.sina.com.cn/roll/2025-09-01/doc-infnyqek9773468.shtml`
- 人工智能生成合成内容标识办法：`https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm`
- 抖音社区自律公约：`https://www.douyin.com/rule/policy`
- 抖音“AI 起号”专项治理转述页：`https://finance.sina.com.cn/jjxw/2025-05-19/doc-inexavha2311135.shtml`

