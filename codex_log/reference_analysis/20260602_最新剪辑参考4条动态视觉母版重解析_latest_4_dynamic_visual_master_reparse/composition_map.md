# Composition Map

status_boundary:
- `scope = dynamic_visual_master_parse`
- `prior_parse = diagnostic_reference_only`
- `not_a_video_execution = true`

## confirmed_global_pattern

1. `platform_shell_not_migration_target`: 四条源视频外层都有竖屏短视频平台壳，包括顶部搜索/状态区、右侧互动栏、底部字幕/评论区。这是来源环境，不是《视频工厂》应复制的视觉母版。
2. `black_stage_as_internal_canvas`: 可迁移的是平台壳内部的黑底/深灰舞台。黑底用于承托白色证据窗口、黄绿高亮、主持人和手机框。
3. `host_reset_zone`: 主持人通常在紫黑舞台中居中，或缩成左下/左侧小 PIP。作用是 reset、陪读、桥接，不是必须复制真人。
4. `evidence_window_zone`: 白色网页、手机聊天页、文档或结果窗口一般位于中部或中右，面积从内容区 40% 到 75% 不等。窗口越密，越需要黄色/绿色读线。
5. `badge_near_target`: 标签贴近目标证据，不脱离窗口漂浮。标签位置通常在窗口角、旁边或上方。

## per_reference

| reference | composition role | must preserve | must not copy |
| --- | --- | --- | --- |
| `reference_01` | host + black stage + comparison/evidence boards + cinematic examples | 证据板前后有主持人/标题 reset；多窗口只在比较关系成立时使用 | Seedance logo、平台 UI、真人与样例片段 |
| `reference_02` | phone-frame packaging + green keyword badges | 手机框与左侧讲解/PIP的双栏关系；绿色 badge 绑定目标框 | 把横屏项目做成全片小手机框；平台互动栏 |
| `reference_03` | teaching visual master: concept cards -> steps -> document evidence | 黄绿短标签、概念图、文档高亮、主持人复位 | Agent Skills/Coze UI、厨师角色、原课程资产 |
| `reference_04` | long text evidence window + yellow reading line + host reset | 长文本证据必须有动态黄线/高亮和低密度 reset | 聊天内容、头像、平台壳、原记忆主题素材 |

## horizontal_16_9_translation

- 横屏中不要复制竖屏平台外壳；应重建为 `left_host_or_caption_zone + center_evidence_window + right_annotation_or_badge_zone`。
- 主证据窗口宽度建议占横屏 55%-70%；小 PIP 不超过主窗口宽度 18%-22%。
- 字幕独立放在底部安全带，不能和证据窗口、小标签、OCR 文字形成三层拥堵。
