# reference_01 Dynamic Visual Timeline

status_boundary:
- `task_result.status = dynamic_visual_master_parse`
- `source_video_read = true`
- `prior_parse_trust = failed_prior_parse / low_trust_reference_summary / diagnostic_reference_only`
- `content_validation = not_applicable`
- `send_ready = false`
- `new_fourth_episode_modified = false`
- `formal_mechanism_updated = false`

evidence:
- `5s_contact_sheets = dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/contact_sheet_5s_page_*.jpg`
- `scene_contact_sheet = dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/contact_sheet_scene_candidates.jpg`
- `dynamic_1s_clips = dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/dynamic_1s_clips/`

## segment_01

- `time_range`: `00:00-00:20`
- `representative_frame_path`: `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0000s.jpg`
- `visual_state`:
  - `layout_composition`: 竖屏平台壳内的上半区为紫黑主持人舞台，人物占画面中上部约 45%-55% 宽度；下方平台字幕/评论区占约 25%-30%，右侧互动栏固定悬浮。本段的视觉重点不是满屏资料，而是先让人看到真人/主持人和大标题钩子。
  - `main_subject_position`: 主持人居中偏上，双手手势有开场招呼感，身体在紫色灯光背景前形成最亮主体；持续 2-5 秒后切到标题/拼贴。
  - `evidence_window_position`: 开头证据窗口较少，主要以小卡片/拼贴闪现，通常在主持人旁侧或中部短暂出现，不承担细读。
  - `pip_or_host_position`: 主持人是主画面而非 PIP；切到拼贴时偶尔出现小头像/平台头像，但不可迁移为项目资产。
  - `subtitle_position`: 平台原生字幕在画面下半部，靠近互动/评论区，和主视频内容保持分层；迁移时应转换为横屏安全下三分之一字幕，不复制平台壳。
  - `typography_style`: 大标题为高对比白/浅色粗体，局部加紫粉或黄绿色强调，字重重、行数少。
  - `highlight_style`: 高亮更像开场爆点字，而不是文档荧光笔；出现方式是随硬切/弹出出现，停留短。
  - `keyword_badge_style`: 少量短词贴在标题或拼贴边缘，功能是抓眼而非解释。
  - `icon_or_motif`: 平台头像、应用图标、短视频互动符号出现，但本轮只读其注意力功能，不可复制。
  - `background_layer`: 紫黑舞台 + 平台黑底 UI；背景低亮度，方便脸和标题跳出来。
  - `depth_and_space`: 人物在前景，标题/拼贴在中景，平台 UI 在最外层；层级清楚但不复杂。
  - `color_weight`: 紫/黑为底，白字和肤色最亮，黄色/粉色作瞬时强调。
  - `information_density`: 中等，开场不是资料堆叠，主要完成识别和兴趣建立。
  - `motion_behavior`: 主持人手势 + 标题/拼贴硬切，视觉运动来自切换和手势，不靠复杂镜头运动。
  - `transition_behavior`: 0-5 秒内硬切到标题或样例，10-20 秒出现拼贴/对比框，节奏直接。
  - `pacing_feel`: 快起势、低停顿、2-5 秒一视觉状态。
  - `attention_path`: 脸部手势 -> 大标题 -> 拼贴/样例 -> 回到底部字幕。
  - `viewer_first_impression`: 像一个有主持人带入的 AI 视频工具讲解，不是纯录屏或 PPT。
  - `why_it_feels_like_reference`: 主持人先建立人感，再快速把注意力交给 AI 视频样例，这个交接是参考感来源。
  - `what_must_not_be_copied`: 不得复制真人身份、平台 UI、互动栏、头像、具体标题字样和 Seedance 相关品牌资产。

## segment_02

- `time_range`: `00:20-01:00`
- `representative_frame_path`: `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0025s.jpg`
- `visual_state`:
  - `layout_composition`: 黑底舞台中部出现双栏或多栏对比板，白色/深色样例框被放在视觉中心；顶部留出黑场，底部仍是平台字幕区。
  - `main_subject_position`: 主角从主持人切换为样例框，人物只在小 PIP 或前后桥接中出现。
  - `evidence_window_position`: 证据窗口多在中上部，约占视频内部区域 45%-65% 宽度，左右并排时每格约半宽；出现 3-8 秒后换下一组。
  - `pip_or_host_position`: 小主持人/PIP 常在左下或框边，承担指路，不覆盖样例主体。
  - `subtitle_position`: 字幕位于视频内容下方，不能压住对比格标题和生成结果。
  - `typography_style`: 标签短、粗、白字，比较关系用小标签或角标说明。
  - `highlight_style`: 黄/浅色小块用于标出 reference/generated 或重点样例，不大面积刷屏。
  - `keyword_badge_style`: 关键词贴近对应样例，而不是统一放在屏幕角落。
  - `icon_or_motif`: 工具图标、手机样例、电影感素材作为证明对象出现。
  - `background_layer`: 黑底弱化平台壳，样例窗口形成亮面。
  - `depth_and_space`: 多窗口形成前景卡片层，黑底是深层，PIP 是最前层。
  - `color_weight`: 黑底 + 白框 + 局部黄色，样例画面颜色本身承担视觉变化。
  - `information_density`: 高，但每次只让 1-2 个窗口成为主读区。
  - `motion_behavior`: 窗口内容换帧、样例视频内部运动、PIP 轻变化；窗口本身多为硬切替换。
  - `transition_behavior`: 密集 hard cut，不用长转场；对比关系靠相邻窗口而不是过渡特效解释。
  - `pacing_feel`: 密集证明段，约 3-6 秒换一类证据。
  - `attention_path`: 对比标签 -> 左右样例 -> 小 PIP -> 字幕。
  - `viewer_first_impression`: 像被带着看“工具能做什么”的证据墙。
  - `why_it_feels_like_reference`: 关键是黑底承载可读证据窗口 + 小标签引导，不是简单拼屏。
  - `what_must_not_be_copied`: 不得复制样例视频、产品 logo、平台原 UI；横屏迁移时要重做证据窗口比例。

## segment_03

- `time_range`: `01:00-01:45`
- `representative_frame_path`: `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0065s.jpg`
- `visual_state`:
  - `layout_composition`: 主持人复位与白色网页/产品页交替；白色证据窗口居中或偏上，小头像/PIP贴边。
  - `main_subject_position`: 主持人短暂回到中心，随后让位给网页证据；主读对象从脸切到白页。
  - `evidence_window_position`: 白色网页窗口占内容区中部约 55%-70% 宽度，停留 5-10 秒，常带轻微裁切聚焦。
  - `pip_or_host_position`: PIP 在左下或窗口边缘，尺寸小于证据窗口 1/5，作用是陪读。
  - `subtitle_position`: 字幕继续在低区，和网页底边有距离，避免覆盖按钮/表格。
  - `typography_style`: 白页内原文小字不可直接依赖；外层只用短词说明当前读哪里。
  - `highlight_style`: 旧参考高亮较少，更多靠窗口裁切和短标签；迁移时应增加项目自己的 active evidence window。
  - `keyword_badge_style`: 黑底上的白/黄短标签，靠近窗口顶角。
  - `icon_or_motif`: 工具 logo/音乐符号/产品图标用于语义识别，不复制。
  - `background_layer`: 黑底让白页成为唯一亮面。
  - `depth_and_space`: 白页像浮在黑幕前，PIP贴前景，平台壳在最外层。
  - `color_weight`: 白页亮度最高，黄色标签次之，紫色主持人作为复位点。
  - `information_density`: 中高，文字多但真正可读区域少。
  - `motion_behavior`: 主要是硬切到网页、轻微裁切、再回主持人。
  - `transition_behavior`: 密集证据后使用主持人画面做低密度 reset。
  - `pacing_feel`: 证明段和解释段交替，观众有喘息。
  - `attention_path`: 主持人解释 -> 白页窗口 -> 标签/按钮 -> 字幕。
  - `viewer_first_impression`: 不是单纯展示网页，而是有人把网页端出来给你看。
  - `why_it_feels_like_reference`: 证据窗口的亮面和主持人复位构成节奏呼吸。
  - `what_must_not_be_copied`: 不得把整页小字原样塞进横屏；必须重构可读裁切。

## segment_04

- `time_range`: `01:45-02:50`
- `representative_frame_path`: `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0125s.jpg`
- `visual_state`:
  - `layout_composition`: 多窗口比较板成为主画面，手机框、样例图、视频画面在中部排布，黄色角标贴在窗口上方或侧边。
  - `main_subject_position`: 主对象是比较板中的结果样例，不是主持人。
  - `evidence_window_position`: 2-4 个窗口并列，整体占内部内容区 60%-75%；每个小窗口持续短，重要窗口会被放大或居中。
  - `pip_or_host_position`: PIP 通常在左下，像讲解者的锚点；不能遮挡比较标签。
  - `subtitle_position`: 平台字幕和画内标签分离；横屏迁移时字幕必须放在证据窗口下方安全区。
  - `typography_style`: 小标签短、功能性强，避免长句；章节/能力词用粗体。
  - `highlight_style`: 黄色边角标提示读哪一格，绿色/亮色用于结果或能力点。
  - `keyword_badge_style`: 贴在对应窗口边缘，保持语义绑定。
  - `icon_or_motif`: 手机框、工具图标、视频缩略图作为动态示例容器。
  - `background_layer`: 黑底 + 多卡片；证据窗口像浮层。
  - `depth_and_space`: 卡片层较多，但主窗口仍明显大于装饰元素。
  - `color_weight`: 窗口画面色彩变化大，黑底维持统一。
  - `information_density`: 高，必须靠高亮和窗口尺寸控制阅读顺序。
  - `motion_behavior`: 窗口内容快速换、偶尔放大/替换；观众感到是在翻一组例子。
  - `transition_behavior`: hard cut + board replacement，几乎没有慢转场。
  - `pacing_feel`: 例证轰炸，但每组有角标定位，不完全乱。
  - `attention_path`: 黄色角标 -> 被标窗口 -> 相邻对照窗口 -> PIP。
  - `viewer_first_impression`: 工具能力被做成连续证据板，而不是单个截图。
  - `why_it_feels_like_reference`: 多窗口不是装饰，是比较/能力证明的容器。
  - `what_must_not_be_copied`: 没有真实比较关系时，不得强行做并排板；不得复制第三方视频缩略图。

## segment_05

- `time_range`: `02:50-04:20`
- `representative_frame_path`: `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0195s.jpg`
- `visual_state`:
  - `layout_composition`: 从多窗口转向电影感样例和黑底章节卡；中部大画面占主导，章节卡穿插。
  - `main_subject_position`: 主对象是生成视频片段或章节大字，主持人只做段落重置。
  - `evidence_window_position`: 大视频窗口居中，约占内容区 55%-70%；章节卡常为整块黑底大字。
  - `pip_or_host_position`: PIP 缩到角落或消失，避免抢动作画面。
  - `subtitle_position`: 字幕在低区，动作画面下方保留安全边。
  - `typography_style`: 章节文字粗而短，中心对齐或略偏中，字距紧凑。
  - `highlight_style`: 章节卡用单点黄/白强调；视频画面不加过多高亮。
  - `keyword_badge_style`: 能力词是段落标题，不再像小贴纸。
  - `icon_or_motif`: 动作片、人物、场景切换承担视觉能量。
  - `background_layer`: 黑底保持统一，亮视频片段像嵌入窗口。
  - `depth_and_space`: 大视频窗口前景化，其他 UI 退后。
  - `color_weight`: 高动态样例自带冷暖变化，黑底控场。
  - `information_density`: 中，文本减少，用画面运动维持兴趣。
  - `motion_behavior`: 动作片段内部运动明显，剪辑外层仍硬切。
  - `transition_behavior`: dense examples 后插入黑底章节卡/主持人 reset。
  - `pacing_feel`: 视觉能量高，但文字负担下降。
  - `attention_path`: 章节大字 -> 动作画面中心 -> 字幕。
  - `viewer_first_impression`: 从讲功能转为看结果，观众被结果画面拉住。
  - `why_it_feels_like_reference`: 用低文字密度的动态样例给密集证据段降压。
  - `what_must_not_be_copied`: 不得复制电影片段或把无关炫技视频当项目证据。

## segment_06

- `time_range`: `04:20-05:46`
- `representative_frame_path`: `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0300s.jpg`
- `visual_state`:
  - `layout_composition`: 尾段在动作样例、白页证据和主持人/标题卡之间收束；最后回到主持人或品牌标题。
  - `main_subject_position`: 收尾主对象回到主持人或最终工具/主题名。
  - `evidence_window_position`: 证据窗口减少，出现时多为单窗口居中，不再多格铺开。
  - `pip_or_host_position`: 主持人恢复为主画面，PIP退场。
  - `subtitle_position`: 字幕仍固定在低区，结尾标题不被字幕盖住。
  - `typography_style`: 结尾用短标题/工具名，白字为主。
  - `highlight_style`: 高亮收敛，不再新增复杂标记。
  - `keyword_badge_style`: 尾段只有总结性词，不做多标签堆叠。
  - `icon_or_motif`: 工具名/最终样例作为记忆点。
  - `background_layer`: 紫黑舞台或黑底标题卡。
  - `depth_and_space`: 层级变浅，减少窗口数量。
  - `color_weight`: 回到紫黑 + 白字，视觉闭环。
  - `information_density`: 中低，主要收束。
  - `motion_behavior`: 主持人手势和少量样例硬切。
  - `transition_behavior`: 由证据段 hard cut 回主持人/标题。
  - `pacing_feel`: 从高密证明降到稳态结尾。
  - `attention_path`: 最后样例 -> 主持人 -> 标题/CTA。
  - `viewer_first_impression`: 完整度来自“主持人开合 + 证据中段 + 标题收束”。
  - `why_it_feels_like_reference`: 不是只会拼窗口，而是有进入、证明、复位、收尾。
  - `what_must_not_be_copied`: 不得把第三方工具名当《视频工厂》自己的结尾品牌。
