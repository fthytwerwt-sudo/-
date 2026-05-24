# 03 Copy Transcript And Structure｜文案 / 字幕 / 口播结构

## transcript_status

- `audio_present = true`
- `subtitle_track_present = false`
- `local_asr_available = false`
- `local_ocr_available = false`
- `transcript_confidence = partial`
- `fallback_method = visible subtitles / visible cards / 同目录喜欢和不喜欢文案库口味文本 / scene timeline`

## structure summary

1. 0-3 秒：用巨大标题字 + 主播表情/手势制造停留，先给“这事很重要”的情绪信号。
2. 3-8 秒：补出具体利益点，暗示“普通人也能拥有高级 AI 军师”。
3. 8-25 秒：快速预览多个结果画面，先让观众看到屏幕成果，再解释。
4. 中段：按“问题一 / 问题二 / 问题三”推进，每个问题都用卡片定题，再用真实页面/表格/资料高亮承接。
5. 判断句：常放在问题卡、模式对比卡和主持人回脸处，不让复杂表格单独承担判断。
6. 高光句：绑定高亮字段、表格结果、三模式对比。
7. 结尾：低压 CTA，核心不是强卖，而是把能力边界拉回“生活工作都能用”。

## copy_structure_table

| line_or_segment_id | timestamp | text | function | granularity_type | detail_density | rhythm_note | visual_dependency | why_effective | transferable_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 00:00-00:08 | 可见字幕: 朋友们；大字标题抓眼 | opening_hook | smooth_line + visual_hook | high visual / low transcript | big-word punch, fast promise | host + title words | 先抓情绪，再落具体利益 | 新第四期开头先抛“别问AI哪个品能爆，先看能否进复查表”这类问题，不直接讲工具 |
| C02 | 00:25-00:45 | 可见卡: 问题一：买房方案 | problem_setup | judgment_boundary_line | medium | 从生活问题切入 | problem card | 把能力放进具体问题，观众知道接下来要看什么 | 新第四期用“问题一：怎么从一堆商品卡筛到4个复查对象” |
| C03 | 00:45-01:25 | 可见标签: 快速模式 / 思考模式 / 专家模式；文档高亮 | proof_structure | material_granularity_line | high visual | 三层对比 + 高亮证据 | document/table screen | 不是说AI强，而是展示强在哪里 | 新第四期用手动翻卡 / Codex初筛 / 人工复查三层结构 |
| C04 | 02:05-02:55 | 可见卡: 体谅 / 思考 / 专家；结果差异 | judgment | judgment_boundary_line | medium-high | 对比卡节奏 | mode cards | 判断句有可视化载体 | 把“AI只做初筛，不做最终上架判断”放进判断卡 |
| C05 | 02:55-03:35 | 可见卡: 问题二：装修方案；表格/清单 | result_change | material_granularity_line | high visual | 表格出现时节奏放慢 | spreadsheet | 结果变化由表格证明 | 新第四期候选表/云盘表格必须局部放大 |
| C06 | 04:35-05:15 | 可见卡: 问题三：论文研究 | transition | smooth_line | medium | 第三案例扩展能力边界 | section card + b-roll | 防止只停留在一个例子 | 新第四期可扩展到“下一步核什么”，但别变成万能AI |
| C07 | 05:45-06:20 | 可见字幕: 不只是程序员专属 / 生活工作都能用 | boundary | judgment_boundary_line | medium | 人话收束 | host + subtitle | 把能力边界拉回普通用户 | 新第四期结尾说清 AI 初筛不是商业验证，只是复查动作 |

## liked / disliked text context

- `喜欢 txt.txt` 提供 `10` 条正向文案样本，主要偏好：具体场景、亲身体验、动作步骤、强例子、最后给行动。
- `不喜欢.txt` 提供 `10` 条反向样本，主要风险：夸大自动化、泛资讯堆砌、收益承诺、没有真实动作、教程过密但缺结果边界。
- 本报告不把上述文本直接当作主视频 transcript；只用于辅助提炼文案口味边界。

## key copy lesson

对《视频工厂》最有价值的是：开头要顺口抓人，但中段高光必须落到真实页面、字段、表格、结果变化和聊天框回传结论；普通连接句可以人话，证明句必须有素材颗粒度。
