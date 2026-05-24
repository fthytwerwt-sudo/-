# 02 Scene Timeline Map｜场景时间线地图

- primary_reference_video: `/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`
- analysis_basis: ffprobe metadata + ffmpeg contact sheets + manual visual inspection of keyframes.
- limitations: local OCR / ASR unavailable; onscreen text is partial and marked by visual confidence.
- local_temp_contact_sheets_not_committed: `本地隔离区_local_quarantine/reference_audit_temp_20260524_文案对标/`

| scene_id | start_time | end_time | main_function | visual_summary | onscreen_text | visual_elements | motion_elements | audio_elements | card_or_overlay | why_it_works | transferability | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | 00:00 | 00:08 | hook | host close-up with oversized kinetic title words; Douyin UI visible | 朋友们 / 巨大标题字 / “0门槛拥有自己的高级AI军师”标题信息 | large title typography; presenter face; purple studio light | quick opening title punch; hand gestures | voice + likely light BGM | title word overlay | 用大字先造情绪，再落到“AI军师”具体承诺 | 机制可迁移：大字钩子 + 具体问题；资产不可复制 | 第三方人物/账号/抖音界面不可复用 |
| S02 | 00:08 | 00:25 | pain_point | rapid montage of UI pages / expert-mode examples / secondary character shot | 四屏资料、人物镜头、专家模式头像 | multi-panel UI examples; creator UI chrome | fast cuts preview outcome before explanation | continuous audio | preview panels | 先让观众看到“它真的能做复杂事”，再解释 | 可迁移：先给候选表/聊天框结论预览 | 别复用原画面和平台 UI |
| S03 | 00:25 | 00:45 | pain_point | presenter explains problem; black problem card appears | 复杂问题 / 问题一：买房方案 | black card with bold white/yellow text | card pop-in; subtitle follows speech | voice | problem card | 把抽象AI能力压成具体生活问题 | 可迁移：把“选品初筛”先压成一个具体问题卡 | 不要承诺“自动赚钱/爆品” |
| S04 | 00:45 | 01:25 | demonstration | home-buying solution demo; mode labels; highlighted evidence lines | 快速模式 / 思考模式 / 专家模式；高亮房贷/首付/利率等字段 | left mode tags; document panel; yellow highlights; avatar corner | document scroll/focus; highlighted rows | voice + short pauses | mode labels + highlight overlay | 三层对比让观众看懂“专家模式”比普通回答多了什么 | 可迁移：手动翻卡/Codex初筛/人工复查三层对比 | 不要照搬买房场景/数据 |
| S05 | 01:25 | 02:05 | transition | host returns; abstract point summarized; workflow screen examples | 生活中还有很多 / 不是所有资料都看 | presenter + screen evidence alternation | host-to-screen cut rhythm | voice | subtitle + occasional callout | 用人脸承接复杂资料，降低屏幕疲劳 | 可迁移：每段表格后回人话判断 | 不能让主持人资产成为 reference |
| S06 | 02:05 | 02:55 | judgment | mode comparison and agent/expert model card set | 快速 / 思考 / 专家；先搜一圈 / 把利弊讲清楚 | three-column vertical mode cards; green/yellow emphasis | cards switch; text block appears | voice | comparison card | 把方法差异视觉化，不靠长解释 | 可迁移：手动筛/AI初筛/复查表三列 | 不要照搬字体、卡片皮肤 |
| S07 | 02:55 | 03:35 | proof | problem two renovation plan; table and spreadsheet-like evidence | 问题二：装修方案；预算表/清单表 | black title card, spreadsheet panels, highlighted table cells | table reveal, scroll, zoom/crop | voice; few silence pockets around 03:05 | section card + table overlay | 用真实表格承担“结果变化” | 可迁移：候选商品表/云盘表格必须给局部放大 | 表格小字过密风险 |
| S08 | 03:35 | 04:35 | proof | document-based answer screens with yellow highlights | 长文档/参考资料/高亮句 | white document cards; yellow marker highlights; side avatar | scrolling long answer; key line highlight | voice | highlight overlay | 资料多但只高亮关键字段，避免观众迷失 | 可迁移：只高亮佣金/风险/ready字段 | 不要复制原文字或资料 |
| S09 | 04:35 | 05:15 | judgment | host introduces thesis/research case; problem card appears | 问题三：论文研究 | host close-up; black section card; study/desk b-roll | cut from host to b-roll and document boards | voice | section card | 第三个案例扩展边界，说明能力不只适用于一个场景 | 可迁移：用“第三步：回聊天框结论”说明边界 | 不要过度扩展成万能AI |
| S10 | 05:15 | 05:45 | result | paper/document boards and generated notes; cat/desk b-roll | 文献/PDF/网页内容总结 | multiple document panels; b-roll of reading/writing | document board shifts, b-roll reset | voice | summary card | 用结果卡收束复杂资料 | 可迁移：把4个商品卡复查项做成结果卡 | 第三方图片/素材不可复用 |
| S11 | 05:45 | 06:20 | boundary | more dense document examples; host closing transition | 不只是程序员专属 / 生活工作都能用 | dense text screens + host | slower document hold, then host | voice | boundary subtitle | 把能力边界拉回普通用户 | 可迁移：强调AI初筛不是最终选品 | 别把“万能/自动赚钱”写进去 |
| S12 | 06:20 | 06:56 | CTA | ending and swipes/secondary content appears; expert-mode title again | 专家模式 / 结尾关注或下一集信息 | host, title card, possible next video snippets | short cuts; end-screen rhythm | voice + BGM likely continues | CTA title card | 低压收尾，回到可操作入口 | 可迁移：结尾给“下一步核什么”而不是泛泛关注 | 不要复用原CTA/账号/品牌 |

## scene method note

`ffmpeg` full processing succeeded but emitted non-monotonic DTS warnings. Scene segmentation here uses a conservative 5-10s visual structure pass rather than treating every platform UI redraw as a separate creative scene.
