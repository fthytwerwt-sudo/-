# Reference Visual Role Classification

status_boundary:
- `basis = dynamic_visual_timeline + source_video_evidence`
- `prior_classification = diagnostic_reference_only`
- `content_validation = not_applicable`
- `visual_master_locked = false`

| reference | visual role | confidence | reason from dynamic timeline | migrate | do not migrate |
| --- | --- | --- | --- | --- | --- |
| `reference_03` | `primary_teaching_dynamic_visual_master` | high | 最完整的教学视觉链路：主持人/标题开题 -> 黑底概念卡 -> 黄绿步骤标签 -> 白色文档证据窗口 -> 高亮行 -> 主持人 reset。 | 抽象概念解释、流程拆解、文档证据带读 | Agent Skills/Coze 资产、厨师角色、具体 UI |
| `reference_04` | `primary_long_text_evidence_window_master` | high | 长文本/聊天证据窗口持续时间长，黄色高亮承担阅读光标，主持人 reset 控制疲劳。 | 长文本证据、聊天/文档逐段带读、黄线阅读路径 | 聊天内容、头像、平台壳、原 AI 记忆主题包装 |
| `reference_01` | `support_result_montage_and_comparison_master` | medium_high | 黑底多窗口比较板、电影/结果样例和章节 reset 强，但具体资产不可复制。 | 结果差、reference/result、before/after、能力样例 montage | Seedance logo、电影素材、平台 UI、真人身份 |
| `reference_02` | `support_phone_keyword_badge_packaging` | medium | 手机框 + 绿色 badge 清楚，但证据窗口小、证明深度不足，不适合做主母版。 | 手机框包装、绿色关键词、轻量结果轮播 | 全片小手机框、平台互动栏、第三方人物素材 |
