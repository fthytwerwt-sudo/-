#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path("/Users/fan/Documents/视频工厂")
LOG_DIR = ROOT / "codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse"
DIST_DIR = ROOT / "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse"
SUMMARY_PATH = LOG_DIR / "media_probe_and_sampling_summary.json"

FIELDS = [
    "layout_composition",
    "main_subject_position",
    "evidence_window_position",
    "pip_or_host_position",
    "subtitle_position",
    "typography_style",
    "highlight_style",
    "keyword_badge_style",
    "icon_or_motif",
    "background_layer",
    "depth_and_space",
    "color_weight",
    "information_density",
    "motion_behavior",
    "transition_behavior",
    "pacing_feel",
    "attention_path",
    "viewer_first_impression",
    "why_it_feels_like_reference",
    "what_must_not_be_copied",
]


TIMELINES = {
    "reference_01": [
        {
            "time_range": "00:00-00:20",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0000s.jpg",
            "visual_state": {
                "layout_composition": "竖屏平台壳内的上半区为紫黑主持人舞台，人物占画面中上部约 45%-55% 宽度；下方平台字幕/评论区占约 25%-30%，右侧互动栏固定悬浮。本段的视觉重点不是满屏资料，而是先让人看到真人/主持人和大标题钩子。",
                "main_subject_position": "主持人居中偏上，双手手势有开场招呼感，身体在紫色灯光背景前形成最亮主体；持续 2-5 秒后切到标题/拼贴。",
                "evidence_window_position": "开头证据窗口较少，主要以小卡片/拼贴闪现，通常在主持人旁侧或中部短暂出现，不承担细读。",
                "pip_or_host_position": "主持人是主画面而非 PIP；切到拼贴时偶尔出现小头像/平台头像，但不可迁移为项目资产。",
                "subtitle_position": "平台原生字幕在画面下半部，靠近互动/评论区，和主视频内容保持分层；迁移时应转换为横屏安全下三分之一字幕，不复制平台壳。",
                "typography_style": "大标题为高对比白/浅色粗体，局部加紫粉或黄绿色强调，字重重、行数少。",
                "highlight_style": "高亮更像开场爆点字，而不是文档荧光笔；出现方式是随硬切/弹出出现，停留短。",
                "keyword_badge_style": "少量短词贴在标题或拼贴边缘，功能是抓眼而非解释。",
                "icon_or_motif": "平台头像、应用图标、短视频互动符号出现，但本轮只读其注意力功能，不可复制。",
                "background_layer": "紫黑舞台 + 平台黑底 UI；背景低亮度，方便脸和标题跳出来。",
                "depth_and_space": "人物在前景，标题/拼贴在中景，平台 UI 在最外层；层级清楚但不复杂。",
                "color_weight": "紫/黑为底，白字和肤色最亮，黄色/粉色作瞬时强调。",
                "information_density": "中等，开场不是资料堆叠，主要完成识别和兴趣建立。",
                "motion_behavior": "主持人手势 + 标题/拼贴硬切，视觉运动来自切换和手势，不靠复杂镜头运动。",
                "transition_behavior": "0-5 秒内硬切到标题或样例，10-20 秒出现拼贴/对比框，节奏直接。",
                "pacing_feel": "快起势、低停顿、2-5 秒一视觉状态。",
                "attention_path": "脸部手势 -> 大标题 -> 拼贴/样例 -> 回到底部字幕。",
                "viewer_first_impression": "像一个有主持人带入的 AI 视频工具讲解，不是纯录屏或 PPT。",
                "why_it_feels_like_reference": "主持人先建立人感，再快速把注意力交给 AI 视频样例，这个交接是参考感来源。",
                "what_must_not_be_copied": "不得复制真人身份、平台 UI、互动栏、头像、具体标题字样和 Seedance 相关品牌资产。",
            },
        },
        {
            "time_range": "00:20-01:00",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0025s.jpg",
            "visual_state": {
                "layout_composition": "黑底舞台中部出现双栏或多栏对比板，白色/深色样例框被放在视觉中心；顶部留出黑场，底部仍是平台字幕区。",
                "main_subject_position": "主角从主持人切换为样例框，人物只在小 PIP 或前后桥接中出现。",
                "evidence_window_position": "证据窗口多在中上部，约占视频内部区域 45%-65% 宽度，左右并排时每格约半宽；出现 3-8 秒后换下一组。",
                "pip_or_host_position": "小主持人/PIP 常在左下或框边，承担指路，不覆盖样例主体。",
                "subtitle_position": "字幕位于视频内容下方，不能压住对比格标题和生成结果。",
                "typography_style": "标签短、粗、白字，比较关系用小标签或角标说明。",
                "highlight_style": "黄/浅色小块用于标出 reference/generated 或重点样例，不大面积刷屏。",
                "keyword_badge_style": "关键词贴近对应样例，而不是统一放在屏幕角落。",
                "icon_or_motif": "工具图标、手机样例、电影感素材作为证明对象出现。",
                "background_layer": "黑底弱化平台壳，样例窗口形成亮面。",
                "depth_and_space": "多窗口形成前景卡片层，黑底是深层，PIP 是最前层。",
                "color_weight": "黑底 + 白框 + 局部黄色，样例画面颜色本身承担视觉变化。",
                "information_density": "高，但每次只让 1-2 个窗口成为主读区。",
                "motion_behavior": "窗口内容换帧、样例视频内部运动、PIP 轻变化；窗口本身多为硬切替换。",
                "transition_behavior": "密集 hard cut，不用长转场；对比关系靠相邻窗口而不是过渡特效解释。",
                "pacing_feel": "密集证明段，约 3-6 秒换一类证据。",
                "attention_path": "对比标签 -> 左右样例 -> 小 PIP -> 字幕。",
                "viewer_first_impression": "像被带着看“工具能做什么”的证据墙。",
                "why_it_feels_like_reference": "关键是黑底承载可读证据窗口 + 小标签引导，不是简单拼屏。",
                "what_must_not_be_copied": "不得复制样例视频、产品 logo、平台原 UI；横屏迁移时要重做证据窗口比例。",
            },
        },
        {
            "time_range": "01:00-01:45",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0065s.jpg",
            "visual_state": {
                "layout_composition": "主持人复位与白色网页/产品页交替；白色证据窗口居中或偏上，小头像/PIP贴边。",
                "main_subject_position": "主持人短暂回到中心，随后让位给网页证据；主读对象从脸切到白页。",
                "evidence_window_position": "白色网页窗口占内容区中部约 55%-70% 宽度，停留 5-10 秒，常带轻微裁切聚焦。",
                "pip_or_host_position": "PIP 在左下或窗口边缘，尺寸小于证据窗口 1/5，作用是陪读。",
                "subtitle_position": "字幕继续在低区，和网页底边有距离，避免覆盖按钮/表格。",
                "typography_style": "白页内原文小字不可直接依赖；外层只用短词说明当前读哪里。",
                "highlight_style": "旧参考高亮较少，更多靠窗口裁切和短标签；迁移时应增加项目自己的 active evidence window。",
                "keyword_badge_style": "黑底上的白/黄短标签，靠近窗口顶角。",
                "icon_or_motif": "工具 logo/音乐符号/产品图标用于语义识别，不复制。",
                "background_layer": "黑底让白页成为唯一亮面。",
                "depth_and_space": "白页像浮在黑幕前，PIP贴前景，平台壳在最外层。",
                "color_weight": "白页亮度最高，黄色标签次之，紫色主持人作为复位点。",
                "information_density": "中高，文字多但真正可读区域少。",
                "motion_behavior": "主要是硬切到网页、轻微裁切、再回主持人。",
                "transition_behavior": "密集证据后使用主持人画面做低密度 reset。",
                "pacing_feel": "证明段和解释段交替，观众有喘息。",
                "attention_path": "主持人解释 -> 白页窗口 -> 标签/按钮 -> 字幕。",
                "viewer_first_impression": "不是单纯展示网页，而是有人把网页端出来给你看。",
                "why_it_feels_like_reference": "证据窗口的亮面和主持人复位构成节奏呼吸。",
                "what_must_not_be_copied": "不得把整页小字原样塞进横屏；必须重构可读裁切。",
            },
        },
        {
            "time_range": "01:45-02:50",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0125s.jpg",
            "visual_state": {
                "layout_composition": "多窗口比较板成为主画面，手机框、样例图、视频画面在中部排布，黄色角标贴在窗口上方或侧边。",
                "main_subject_position": "主对象是比较板中的结果样例，不是主持人。",
                "evidence_window_position": "2-4 个窗口并列，整体占内部内容区 60%-75%；每个小窗口持续短，重要窗口会被放大或居中。",
                "pip_or_host_position": "PIP 通常在左下，像讲解者的锚点；不能遮挡比较标签。",
                "subtitle_position": "平台字幕和画内标签分离；横屏迁移时字幕必须放在证据窗口下方安全区。",
                "typography_style": "小标签短、功能性强，避免长句；章节/能力词用粗体。",
                "highlight_style": "黄色边角标提示读哪一格，绿色/亮色用于结果或能力点。",
                "keyword_badge_style": "贴在对应窗口边缘，保持语义绑定。",
                "icon_or_motif": "手机框、工具图标、视频缩略图作为动态示例容器。",
                "background_layer": "黑底 + 多卡片；证据窗口像浮层。",
                "depth_and_space": "卡片层较多，但主窗口仍明显大于装饰元素。",
                "color_weight": "窗口画面色彩变化大，黑底维持统一。",
                "information_density": "高，必须靠高亮和窗口尺寸控制阅读顺序。",
                "motion_behavior": "窗口内容快速换、偶尔放大/替换；观众感到是在翻一组例子。",
                "transition_behavior": "hard cut + board replacement，几乎没有慢转场。",
                "pacing_feel": "例证轰炸，但每组有角标定位，不完全乱。",
                "attention_path": "黄色角标 -> 被标窗口 -> 相邻对照窗口 -> PIP。",
                "viewer_first_impression": "工具能力被做成连续证据板，而不是单个截图。",
                "why_it_feels_like_reference": "多窗口不是装饰，是比较/能力证明的容器。",
                "what_must_not_be_copied": "没有真实比较关系时，不得强行做并排板；不得复制第三方视频缩略图。",
            },
        },
        {
            "time_range": "02:50-04:20",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0195s.jpg",
            "visual_state": {
                "layout_composition": "从多窗口转向电影感样例和黑底章节卡；中部大画面占主导，章节卡穿插。",
                "main_subject_position": "主对象是生成视频片段或章节大字，主持人只做段落重置。",
                "evidence_window_position": "大视频窗口居中，约占内容区 55%-70%；章节卡常为整块黑底大字。",
                "pip_or_host_position": "PIP 缩到角落或消失，避免抢动作画面。",
                "subtitle_position": "字幕在低区，动作画面下方保留安全边。",
                "typography_style": "章节文字粗而短，中心对齐或略偏中，字距紧凑。",
                "highlight_style": "章节卡用单点黄/白强调；视频画面不加过多高亮。",
                "keyword_badge_style": "能力词是段落标题，不再像小贴纸。",
                "icon_or_motif": "动作片、人物、场景切换承担视觉能量。",
                "background_layer": "黑底保持统一，亮视频片段像嵌入窗口。",
                "depth_and_space": "大视频窗口前景化，其他 UI 退后。",
                "color_weight": "高动态样例自带冷暖变化，黑底控场。",
                "information_density": "中，文本减少，用画面运动维持兴趣。",
                "motion_behavior": "动作片段内部运动明显，剪辑外层仍硬切。",
                "transition_behavior": "dense examples 后插入黑底章节卡/主持人 reset。",
                "pacing_feel": "视觉能量高，但文字负担下降。",
                "attention_path": "章节大字 -> 动作画面中心 -> 字幕。",
                "viewer_first_impression": "从讲功能转为看结果，观众被结果画面拉住。",
                "why_it_feels_like_reference": "用低文字密度的动态样例给密集证据段降压。",
                "what_must_not_be_copied": "不得复制电影片段或把无关炫技视频当项目证据。",
            },
        },
        {
            "time_range": "04:20-05:46",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/frames_5s/t0300s.jpg",
            "visual_state": {
                "layout_composition": "尾段在动作样例、白页证据和主持人/标题卡之间收束；最后回到主持人或品牌标题。",
                "main_subject_position": "收尾主对象回到主持人或最终工具/主题名。",
                "evidence_window_position": "证据窗口减少，出现时多为单窗口居中，不再多格铺开。",
                "pip_or_host_position": "主持人恢复为主画面，PIP退场。",
                "subtitle_position": "字幕仍固定在低区，结尾标题不被字幕盖住。",
                "typography_style": "结尾用短标题/工具名，白字为主。",
                "highlight_style": "高亮收敛，不再新增复杂标记。",
                "keyword_badge_style": "尾段只有总结性词，不做多标签堆叠。",
                "icon_or_motif": "工具名/最终样例作为记忆点。",
                "background_layer": "紫黑舞台或黑底标题卡。",
                "depth_and_space": "层级变浅，减少窗口数量。",
                "color_weight": "回到紫黑 + 白字，视觉闭环。",
                "information_density": "中低，主要收束。",
                "motion_behavior": "主持人手势和少量样例硬切。",
                "transition_behavior": "由证据段 hard cut 回主持人/标题。",
                "pacing_feel": "从高密证明降到稳态结尾。",
                "attention_path": "最后样例 -> 主持人 -> 标题/CTA。",
                "viewer_first_impression": "完整度来自“主持人开合 + 证据中段 + 标题收束”。",
                "why_it_feels_like_reference": "不是只会拼窗口，而是有进入、证明、复位、收尾。",
                "what_must_not_be_copied": "不得把第三方工具名当《视频工厂》自己的结尾品牌。",
            },
        },
    ],
    "reference_02": [
        {
            "time_range": "00:00-00:18",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/frames_5s/t0000s.jpg",
            "visual_state": {
                "layout_composition": "主持人紫黑舞台开场，随后转成左侧主持人小窗 + 右侧竖向手机结果框；整体仍包在短视频平台壳里。",
                "main_subject_position": "0 秒主持人居中，5 秒后手机框成为主对象，主持人缩到左侧陪读。",
                "evidence_window_position": "手机框垂直居中偏右，宽度约为内部内容区 30%-40%，持续多秒；证据更像结果预览而非文档证明。",
                "pip_or_host_position": "左侧小主持人/PIP与手机框平行，形成双栏阅读。",
                "subtitle_position": "底部平台字幕固定，横屏迁移时应移到手机框下缘外，不盖手机画面。",
                "typography_style": "开场大字短、颜色亮；手机旁绿色短词为高可见标签。",
                "highlight_style": "绿色块和 check 式标记从右侧贴近手机框出现，像动态注释。",
                "keyword_badge_style": "绿色 badge 小而硬，绑定结果框，不脱离证据漂浮。",
                "icon_or_motif": "手机框是核心 motif，平台互动栏不可复制。",
                "background_layer": "深灰/黑底弱化空间，手机框发亮。",
                "depth_and_space": "主持人和手机框并排同层，绿色标签在最前层。",
                "color_weight": "紫黑 + 绿色关键词 + 手机内容色彩。",
                "information_density": "中，证据窗口小但标签清楚。",
                "motion_behavior": "手机内容/人物样例快速替换，绿色标签弹入。",
                "transition_behavior": "硬切从主持人转手机双栏，变化直接。",
                "pacing_feel": "短促、包装感强。",
                "attention_path": "主持人 -> 手机框 -> 绿色标签 -> 字幕。",
                "viewer_first_impression": "像一条讲 AI 视频结果的手机框包装片。",
                "why_it_feels_like_reference": "手机框和绿色标签一起出现，形成“看这里”的视觉指令。",
                "what_must_not_be_copied": "不得复制平台壳、具体人物脸、手机内第三方素材。",
            },
        },
        {
            "time_range": "00:18-00:50",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/frames_5s/t0025s.jpg",
            "visual_state": {
                "layout_composition": "左侧 PIP + 右侧手机竖屏结果形成稳定双栏；中间留黑，右侧互动栏在平台壳外固定。",
                "main_subject_position": "手机结果为主，主持人小窗提供语境。",
                "evidence_window_position": "手机框居中偏右，尺寸稳定，内容每几秒更换。",
                "pip_or_host_position": "PIP在左侧中部或偏下，和手机等高关系清晰。",
                "subtitle_position": "字幕在平台底部，不参与手机内容层级。",
                "typography_style": "小白字/绿色块，文字少。",
                "highlight_style": "绿色高亮/check 标注短促出现，指向手机结果。",
                "keyword_badge_style": "标签多贴右上或右侧，不覆盖手机中心主体。",
                "icon_or_motif": "手机框、头像、小贴纸承担平台感。",
                "background_layer": "暗灰黑底，大面积留空。",
                "depth_and_space": "手机框是亮前景，PIP次前景，暗底为后景。",
                "color_weight": "暗底中绿色最刺眼。",
                "information_density": "中低，适合讲结果，不适合讲长流程。",
                "motion_behavior": "内容换帧为主，外框少动。",
                "transition_behavior": "硬切替换手机内素材或切到新手机框。",
                "pacing_feel": "稳定双栏，节奏靠内容轮播。",
                "attention_path": "手机屏幕中心 -> 绿色标签 -> PIP。",
                "viewer_first_impression": "手机结果被包装得清楚，但证明深度有限。",
                "why_it_feels_like_reference": "固定双栏让观众知道左边讲解、右边看结果。",
                "what_must_not_be_copied": "不得把横屏项目全片做成小手机框，证据可读性会不足。",
            },
        },
        {
            "time_range": "00:50-01:20",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/frames_5s/t0060s.jpg",
            "visual_state": {
                "layout_composition": "进入多结果轮播，手机框/竖屏样例在中央，绿色标签有时贴右侧，有时消失。",
                "main_subject_position": "竖屏样例人物或结果画面成为中心。",
                "evidence_window_position": "证据窗口仍小，约内容区 30%-45%，可看结果但难细读文字。",
                "pip_or_host_position": "PIP有时左侧，有时退场，主持功能弱化。",
                "subtitle_position": "底部字幕保留，迁移时要避免和小手机框同时挤压。",
                "typography_style": "标签短句，平台小字不可作为迁移对象。",
                "highlight_style": "绿色标签作为瞬时注意力锚点，不做长文本高亮。",
                "keyword_badge_style": "badge 适合标“结果 / 效果 / 关键词”，不适合承载解释。",
                "icon_or_motif": "手机框继续是视觉锚点。",
                "background_layer": "深灰背景，留空大。",
                "depth_and_space": "结果窗口单层突出。",
                "color_weight": "内容色彩变化来自样例，整体仍暗。",
                "information_density": "中，更多是示例展示。",
                "motion_behavior": "样例视频内部运动 + 外部硬切。",
                "transition_behavior": "一屏一结果切换，少复杂转场。",
                "pacing_feel": "结果流，偏快。",
                "attention_path": "手机结果 -> 绿色短词 -> 下方字幕。",
                "viewer_first_impression": "轻量、直接、有移动端感。",
                "why_it_feels_like_reference": "小框结果持续替换，形成短视频工具展示节奏。",
                "what_must_not_be_copied": "不得迁移其平台滤镜和第三方人物素材。",
            },
        },
        {
            "time_range": "01:20-02:05",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/frames_5s/t0090s.jpg",
            "visual_state": {
                "layout_composition": "主持人复位穿插全屏/单窗口视频样例，双栏关系不再持续。",
                "main_subject_position": "主持人和样例交替成为主画面。",
                "evidence_window_position": "样例窗口居中，大小不一，部分直接全宽内嵌。",
                "pip_or_host_position": "主持人回到中心时承担解释；在样例中常消失。",
                "subtitle_position": "下方字幕持续提供语义线。",
                "typography_style": "外层文字减少，靠口播字幕推进。",
                "highlight_style": "绿色标签减少，偶尔用于结果点。",
                "keyword_badge_style": "badge 变成间歇性提醒。",
                "icon_or_motif": "人物/舞台/手机示例混合。",
                "background_layer": "紫黑主持舞台和暗底样例交替。",
                "depth_and_space": "层级变浅，更多是单主体。",
                "color_weight": "主持人紫色稳定，样例色彩变化大。",
                "information_density": "中低。",
                "motion_behavior": "主持人手势 reset，样例内部运动。",
                "transition_behavior": "hard cut 回主持人，形成呼吸。",
                "pacing_feel": "比前段稍慢，给观众重新对齐。",
                "attention_path": "样例 -> 主持人 -> 字幕。",
                "viewer_first_impression": "包装从结果轮播回到人讲。",
                "why_it_feels_like_reference": "短视频节奏里用主持人打断纯素材轮播。",
                "what_must_not_be_copied": "不要把主持人真人身份或服装当模板。",
            },
        },
        {
            "time_range": "02:05-03:20",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/frames_5s/t0170s.jpg",
            "visual_state": {
                "layout_composition": "尾段在主持人、暗底工具标题和手机样例之间切换；出现带工具名/版本字样的中心标题。",
                "main_subject_position": "主持人与工具标题交替为主。",
                "evidence_window_position": "证据窗口减少，更多是记忆点和样例结束。",
                "pip_or_host_position": "主持人回到大画面收束，PIP不再是主结构。",
                "subtitle_position": "字幕仍在平台底部，尾卡中要留出避免冲突。",
                "typography_style": "大字标题/工具名居中，短而醒目。",
                "highlight_style": "绿色/亮色作为最后标记，不展开解释。",
                "keyword_badge_style": "尾部 badge 是点题，不承担证明。",
                "icon_or_motif": "工具 logo/手机框/主持人。",
                "background_layer": "暗底与紫色舞台回环。",
                "depth_and_space": "单层收尾。",
                "color_weight": "暗底中标题最亮。",
                "information_density": "低到中。",
                "motion_behavior": "硬切、主持手势、标题弹出。",
                "transition_behavior": "结果窗口 -> 主持人 -> 工具名。",
                "pacing_feel": "收束但仍快。",
                "attention_path": "工具名 -> 主持人 -> 最后样例。",
                "viewer_first_impression": "这是手机包装/关键词包装的辅助参考，而不是完整证据母版。",
                "why_it_feels_like_reference": "绿色 badge + 手机结果框构成可迁移语言。",
                "what_must_not_be_copied": "不能把它当作新第四期主视觉模板，尤其不能复制平台 UI。",
            },
        },
    ],
    "reference_03": [
        {
            "time_range": "00:00-00:20",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/frames_5s/t0005s.jpg",
            "visual_state": {
                "layout_composition": "主持人紫黑舞台开场后迅速切到大标题卡，标题占内部画面中部大面积，主持人有时与标题并置。",
                "main_subject_position": "主持人先居中，然后标题成为主对象。",
                "evidence_window_position": "无深证据窗口，只有概念入口和主题定位。",
                "pip_or_host_position": "主持人是主画面，不是角落 PIP。",
                "subtitle_position": "底部字幕在平台区，和标题分开。",
                "typography_style": "大标题中英文混用，白字/黄绿重点词，粗体醒目。",
                "highlight_style": "标题词本身被黄绿块或亮色强调。",
                "keyword_badge_style": "关键词像课程标题，不像装饰贴纸。",
                "icon_or_motif": "Agent/Skills/AI 词汇成为视觉 motif。",
                "background_layer": "紫黑主持舞台 + 黑底标题。",
                "depth_and_space": "低层级，先建立主题。",
                "color_weight": "黑紫底 + 黄绿重点词。",
                "information_density": "低到中。",
                "motion_behavior": "主持手势，标题硬切/弹出。",
                "transition_behavior": "0-6 秒完成主持人到大标题的切换。",
                "pacing_feel": "开头利落，像课程入口。",
                "attention_path": "脸 -> 大标题 -> 关键词。",
                "viewer_first_impression": "像一条结构化 AI 教学视频，主题很快被钉住。",
                "why_it_feels_like_reference": "主题词被做成可读的大视觉对象，而不是藏在字幕里。",
                "what_must_not_be_copied": "不得复制 Agent Skills 具体品牌/课程标题。",
            },
        },
        {
            "time_range": "00:20-01:15",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/frames_5s/t0030s.jpg",
            "visual_state": {
                "layout_composition": "黑底解释舞台，厨师/小人/AI 图标/短词卡组成概念图；多个小块按横向或网格排列。",
                "main_subject_position": "中心是概念图中的角色或关键词，不是主持人。",
                "evidence_window_position": "这一段不是实证窗口，而是概念模型窗口，占内容区中部约 50%-65%。",
                "pip_or_host_position": "主持人多退场或只在边缘作为小头像。",
                "subtitle_position": "底部字幕不干扰概念图。",
                "typography_style": "短词卡、黄绿标签、白色解释词；每屏字数少。",
                "highlight_style": "黄绿块贴在关键词附近，帮助观众读顺序。",
                "keyword_badge_style": "badge 绑定角色/图标，如“炒菜/AI/步骤”这类类比词。",
                "icon_or_motif": "厨师、小人、AI 圆标、步骤卡是概念比喻 motif。",
                "background_layer": "黑底，概念元素浮在中心。",
                "depth_and_space": "图标/标签形成前景，背景简洁。",
                "color_weight": "黑底 + 黄绿 + 白字，信息非常清爽。",
                "information_density": "中，概念多但每屏少字。",
                "motion_behavior": "元素通过硬切/分步出现，像搭积木。",
                "transition_behavior": "概念块之间快速替换，每个停留约 3-8 秒。",
                "pacing_feel": "教学式、可跟上。",
                "attention_path": "关键词 badge -> 图标 -> 相邻解释词。",
                "viewer_first_impression": "复杂概念被视觉化成小游戏/类比图。",
                "why_it_feels_like_reference": "它不是展示素材，而是把抽象机制拆成一眼能读的视觉语法。",
                "what_must_not_be_copied": "厨师角色、具体 Coze/Agent UI、图标造型不可直接复制。",
            },
        },
        {
            "time_range": "01:15-02:30",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/frames_5s/t0135s.jpg",
            "visual_state": {
                "layout_composition": "黑底中心出现黄色步骤/定义卡，随后主持人复位；卡片是横向短条或几行堆叠。",
                "main_subject_position": "步骤卡或定义词在中心偏上；主持人复位时回到中心。",
                "evidence_window_position": "无长文档证据，先用结构卡过渡到下一段。",
                "pip_or_host_position": "主持人作为 reset，而不是一直在角落小讲。",
                "subtitle_position": "底部平台字幕独立，结构卡不压字幕。",
                "typography_style": "黄底黑字/白字短标签，边框硬朗。",
                "highlight_style": "整块黄卡就是高亮，信息量克制。",
                "keyword_badge_style": "多个黄绿短词排列成结构层级。",
                "icon_or_motif": "小人/AI icon 间歇出现。",
                "background_layer": "纯黑让黄色卡片突出。",
                "depth_and_space": "少量卡片前景，空间开阔。",
                "color_weight": "黄色高亮权重最高。",
                "information_density": "中低，适合做桥接。",
                "motion_behavior": "卡片硬切或逐步增加，主持人 cut-in reset。",
                "transition_behavior": "概念图 -> 黄卡 -> 主持人 -> 文档证据。",
                "pacing_feel": "段落边界明确。",
                "attention_path": "黄卡标题 -> 次级卡 -> 主持人。",
                "viewer_first_impression": "像有章节小黑板，不是乱切素材。",
                "why_it_feels_like_reference": "黄卡承担“现在讲哪一层”的导航功能。",
                "what_must_not_be_copied": "不要把所有句子都做成黄卡；只给结构节点用。",
            },
        },
        {
            "time_range": "02:30-03:25",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/frames_5s/t0170s.jpg",
            "visual_state": {
                "layout_composition": "白色文档/网页窗口开始成为主证据，窗口横向居中或偏右，左下角保留小头像/PIP。",
                "main_subject_position": "主对象为文档窗口中的高亮行或界面区域。",
                "evidence_window_position": "白色窗口占内容区约 60%-75%，高亮行位于窗口中部，持续 5-15 秒。",
                "pip_or_host_position": "小头像/PIP 在左下，尺寸很小，只做讲解来源标记。",
                "subtitle_position": "字幕在低区，和白色窗口底边隔开。",
                "typography_style": "文档小字很多，但外层只允许提取少量可读重点。",
                "highlight_style": "紫/黄/绿荧光笔式高亮行，直接落在文档内部。",
                "keyword_badge_style": "右侧或窗口旁有小型黄绿标签，说明读哪段。",
                "icon_or_motif": "文档窗口、网页工具栏、AI 小标识。",
                "background_layer": "黑底衬白窗。",
                "depth_and_space": "白窗前景很强，PIP贴前，平台壳退后。",
                "color_weight": "白窗最大，黄绿高亮导视。",
                "information_density": "高；若不高亮会难读。",
                "motion_behavior": "文档窗口硬切/轻微移动，高亮区域切换。",
                "transition_behavior": "结构卡进入证据窗，证明开始落地。",
                "pacing_feel": "从讲概念进入看资料，节奏变稳。",
                "attention_path": "高亮行 -> 窗口标题/边缘标签 -> PIP。",
                "viewer_first_impression": "这是有文档支撑的讲解，不是空讲。",
                "why_it_feels_like_reference": "高亮行让长文档变成可读证据窗口。",
                "what_must_not_be_copied": "不能把第三方文档原文当项目内容；不可让小字成为唯一证据。",
            },
        },
        {
            "time_range": "03:25-04:55",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/frames_5s/t0240s.jpg",
            "visual_state": {
                "layout_composition": "工作流/技能商店/设置页等界面窗口连续出现，有时右侧叠黑色说明栏或绿色小标签。",
                "main_subject_position": "主对象为界面中的被高亮区域，通常在白页中上或右侧。",
                "evidence_window_position": "证据窗口最大化为中心白页，约占内容区 70%；右侧说明栏约 25%。",
                "pip_or_host_position": "小头像保持在左下，或主持人短暂复位。",
                "subtitle_position": "字幕仍低区，避免压住界面底部按钮。",
                "typography_style": "界面原字 + 外层短标签混合；外层字必须少。",
                "highlight_style": "黄/绿框、荧光笔、局部块状标签指向具体按钮或列表。",
                "keyword_badge_style": "贴近界面中的目标区域，不独立漂浮。",
                "icon_or_motif": "网页窗口、技能列表、AI 图标。",
                "background_layer": "黑底框住白页，平台壳仍在外。",
                "depth_and_space": "证据窗口前景，注释层更前，PIP最前但很小。",
                "color_weight": "白页 + 黄绿注释，黑底控噪。",
                "information_density": "高到很高，必须分屏读。",
                "motion_behavior": "窗口内容切换、局部高亮移动、说明栏替换。",
                "transition_behavior": "同类界面之间 hard cut，保持阅读位置相似。",
                "pacing_feel": "持续教学证明段，节奏稳但密。",
                "attention_path": "标签 -> 高亮区域 -> 界面上下文 -> PIP。",
                "viewer_first_impression": "像认真讲工具流程，有证据也有导航。",
                "why_it_feels_like_reference": "它把复杂界面做成“可读局部”，不是一整页扔给观众。",
                "what_must_not_be_copied": "不得复制 Coze/Agent Skills 界面作为项目品牌；横屏应重做裁切和注释。",
            },
        },
        {
            "time_range": "04:55-06:03",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/frames_5s/t0355s.jpg",
            "visual_state": {
                "layout_composition": "后段在文档窗口、主持人复位和结尾标题之间收束，信息密度逐步下降。",
                "main_subject_position": "主持人或最终文档页交替成为主对象。",
                "evidence_window_position": "白页证据仍出现，但不再多层叠加。",
                "pip_or_host_position": "主持人回到中心，PIP减少。",
                "subtitle_position": "低区字幕稳定。",
                "typography_style": "收尾标题短，文档高亮少。",
                "highlight_style": "只保留关键黄绿标记。",
                "keyword_badge_style": "尾段 badge 用于总结，不再开新概念。",
                "icon_or_motif": "AI/技能/文档。",
                "background_layer": "紫黑舞台和黑底证据窗互切。",
                "depth_and_space": "层级收敛。",
                "color_weight": "回到主持人紫黑色。",
                "information_density": "中低。",
                "motion_behavior": "硬切回主持人，动作降低。",
                "transition_behavior": "证据窗 -> 主持人 -> 结尾状态。",
                "pacing_feel": "收束明确。",
                "attention_path": "最后高亮 -> 主持人 -> 结尾词。",
                "viewer_first_impression": "完整教学闭环。",
                "why_it_feels_like_reference": "高密证据之后用人像和短词降噪。",
                "what_must_not_be_copied": "不要把课程品牌和人物形象迁移。",
            },
        },
    ],
    "reference_04": [
        {
            "time_range": "00:00-00:35",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/frames_5s/t0000s.jpg",
            "visual_state": {
                "layout_composition": "紫黑主持人舞台开场，大标题悬在人物上方或旁侧，随后切到黑底标题卡。",
                "main_subject_position": "主持人居中偏上，标题在中上部，形成强钩子。",
                "evidence_window_position": "开头证据很少，主要是话题锁定。",
                "pip_or_host_position": "主持人是主画面，非 PIP。",
                "subtitle_position": "底部字幕位于平台下半区。",
                "typography_style": "大白字/紫粉字，主题词粗体，行数少。",
                "highlight_style": "用标题颜色强调“记忆/AI”类核心词。",
                "keyword_badge_style": "开头 badge 少，后续才转为证据高亮。",
                "icon_or_motif": "AI、记忆、黑底标题是 motif。",
                "background_layer": "紫黑舞台，外层平台 UI。",
                "depth_and_space": "人物前景、标题中景、平台壳外层。",
                "color_weight": "紫黑 + 白字最强。",
                "information_density": "低到中。",
                "motion_behavior": "主持人手势、标题硬切。",
                "transition_behavior": "主持人 -> 黑底标题卡 -> 证据前置。",
                "pacing_feel": "开题快，情绪更轻一点。",
                "attention_path": "脸 -> 大标题 -> 字幕。",
                "viewer_first_impression": "像一个人带你进入 AI 长期记忆主题。",
                "why_it_feels_like_reference": "强标题和主持人先把抽象能力人格化。",
                "what_must_not_be_copied": "不得复制真人、平台搜索栏、互动栏和原主题包装。",
            },
        },
        {
            "time_range": "00:35-01:10",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/frames_5s/t0035s.jpg",
            "visual_state": {
                "layout_composition": "黑底中出现白色/黑色信息卡、AI 长期记忆标题和小列表；局部蓝/紫条做路径感。",
                "main_subject_position": "信息卡居中，主持人退到小 PIP 或暂时消失。",
                "evidence_window_position": "信息卡不是原始证据，像概念导图，约占内容区 55%-65%。",
                "pip_or_host_position": "小头像/PIP在左下或边缘，不遮挡列表。",
                "subtitle_position": "底部字幕和信息卡保持垂直距离。",
                "typography_style": "大标题短，列表行距紧但可扫读。",
                "highlight_style": "白字 + 蓝紫/黄绿小条突出流程项。",
                "keyword_badge_style": "标签贴在列表侧边或标题旁，像章节锚点。",
                "icon_or_motif": "AI 字样、记忆节点、路径线。",
                "background_layer": "纯黑控场。",
                "depth_and_space": "卡片浮在黑底前，PIP次级。",
                "color_weight": "白字最高，蓝紫条给技术感。",
                "information_density": "中。",
                "motion_behavior": "卡片硬切出现，列表逐项变化感。",
                "transition_behavior": "标题卡进入概念卡，随后回主持人。",
                "pacing_feel": "解释节奏，不急。",
                "attention_path": "标题 -> 列表首项 -> 彩色条 -> PIP。",
                "viewer_first_impression": "抽象能力被整理成清单。",
                "why_it_feels_like_reference": "它先建结构，再进长文本证据。",
                "what_must_not_be_copied": "不要复制具体 UI 或原文；只学清单化入口。",
            },
        },
        {
            "time_range": "01:10-02:05",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/frames_5s/t0085s.jpg",
            "visual_state": {
                "layout_composition": "手机聊天/长文本窗口居中偏右，左侧小头像/PIP或小卡片做讲解，黑底留空。",
                "main_subject_position": "长文本窗口里的高亮段是主读对象。",
                "evidence_window_position": "手机/白页证据窗口约占内容区 45%-60%，垂直长条，持续 10-30 秒，内部黄色高亮随段落变化。",
                "pip_or_host_position": "PIP在左侧，约证据窗口 1/5 宽，承担陪读。",
                "subtitle_position": "底部平台字幕不应覆盖手机底部文字；横屏迁移需单独设字幕安全带。",
                "typography_style": "长文本本身密，外层只加短标签；不能让观众读整页。",
                "highlight_style": "黄色荧光笔横条直接盖在长文本重点句上，是本条最核心视觉语言。",
                "keyword_badge_style": "小白/黄标签在手机框顶部或左侧说明当前证据功能。",
                "icon_or_motif": "手机聊天页、头像、记忆库/聊天气泡。",
                "background_layer": "黑底 + 白色手机窗口。",
                "depth_and_space": "手机窗口前景，PIP/标签更前，平台 UI外层。",
                "color_weight": "白页 + 黄色高亮最亮，紫色主持人较少。",
                "information_density": "高，但高亮把主句压出来。",
                "motion_behavior": "窗口内容硬切，黄线位置变化，PIP偶尔变化。",
                "transition_behavior": "主持人 reset 后进入长文本证据，证据持续比其他参考更久。",
                "pacing_feel": "慢一点，像陪读长文。",
                "attention_path": "黄色高亮 -> 当前文本段 -> PIP -> 字幕。",
                "viewer_first_impression": "有人在替你读一大段 AI 记忆证据。",
                "why_it_feels_like_reference": "核心是黄色高亮在长文本里移动，形成真实阅读路径。",
                "what_must_not_be_copied": "不得复制聊天内容、头像、平台 UI；不要把整页字缩小到不可读。",
            },
        },
        {
            "time_range": "02:05-03:45",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/frames_5s/t0140s.jpg",
            "visual_state": {
                "layout_composition": "长文本证据窗口反复出现，黄色高亮越来越密；主持人每隔一段回到中心做复位。",
                "main_subject_position": "主对象持续为证据窗口高亮句组。",
                "evidence_window_position": "证据窗口居中偏右或居中，长期稳定；每次停留 10-20 秒，适合逐段讲。",
                "pip_or_host_position": "PIP在左侧，主持人复位时变成全主画面。",
                "subtitle_position": "底部字幕必须远离证据窗口，避免三层文字同时挤压。",
                "typography_style": "长文本 + 黄色高亮 + 少量白色外层标签。",
                "highlight_style": "黄线/黄色块是阅读主指针，必须贴真实证据，不做装饰。",
                "keyword_badge_style": "badge 用于标证据类型，如记忆/步骤/方法，不要逐词乱贴。",
                "icon_or_motif": "手机文本、聊天头像、记忆节点。",
                "background_layer": "黑底稳定，降低长文压力。",
                "depth_and_space": "证据窗口主前景，标签和 PIP在前。",
                "color_weight": "黄色高亮在白页上最抓眼。",
                "information_density": "高，但有读线。",
                "motion_behavior": "高亮位置变化和窗口替换是主要动态；主持人 reset 降低疲劳。",
                "transition_behavior": "证据窗 -> 主持人 -> 新证据窗循环。",
                "pacing_feel": "中速陪读，密但不乱。",
                "attention_path": "黄线 -> 证据窗口 -> 主持人表情/手势 -> 下一黄线。",
                "viewer_first_impression": "长文本被导演成可读证据。",
                "why_it_feels_like_reference": "动态高亮和主持人复位共同解决长文本疲劳。",
                "what_must_not_be_copied": "不能在无真实文本证据时假造高亮；不能让字幕压住高亮句。",
            },
        },
        {
            "time_range": "03:45-04:25",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/frames_5s/t0255s.jpg",
            "visual_state": {
                "layout_composition": "主持人复位、彩条/梗图式断点、列表卡和小标签穿插，视觉密度明显降低。",
                "main_subject_position": "主持人重新成为主对象，或中心列表卡成为主对象。",
                "evidence_window_position": "证据窗口暂时退场，转为情绪/章节桥接。",
                "pip_or_host_position": "主持人居中，PIP减少。",
                "subtitle_position": "底部字幕继续承接语义。",
                "typography_style": "短句、列表、少量英文/符号，字号较大。",
                "highlight_style": "高亮从长文本黄线变成标题/列表强调。",
                "keyword_badge_style": "badge 做转场提示，不做证据读线。",
                "icon_or_motif": "彩条、列表、提示词/章节符号。",
                "background_layer": "黑底或紫黑主持舞台。",
                "depth_and_space": "层级简单，给观众休息。",
                "color_weight": "短时高饱和彩条作为视觉重置。",
                "information_density": "低到中。",
                "motion_behavior": "硬切到彩条/列表，形成醒目的情绪断点。",
                "transition_behavior": "长证据段后的 reset bridge。",
                "pacing_feel": "呼吸点，轻松一点。",
                "attention_path": "主持人 -> 短标题/列表 -> 下一段。",
                "viewer_first_impression": "长文讲完后被主动降噪。",
                "why_it_feels_like_reference": "它知道什么时候不能继续塞长文本。",
                "what_must_not_be_copied": "彩条/梗图只可作节奏参考，不可照搬素材。",
            },
        },
        {
            "time_range": "04:25-04:54",
            "representative_frame_path": "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/frames_5s/t0280s.jpg",
            "visual_state": {
                "layout_composition": "尾段出现 B-roll/浅色标题页/黑底 hashtag 卡，主持人短暂回收。",
                "main_subject_position": "最终标题或 B-roll 画面成为主对象。",
                "evidence_window_position": "证据窗口基本退场。",
                "pip_or_host_position": "主持人不再持续占屏，收尾更轻。",
                "subtitle_position": "字幕仍在平台低区。",
                "typography_style": "结尾短句、hashtag、白字。",
                "highlight_style": "高亮减少，回到记忆点。",
                "keyword_badge_style": "尾部 hashtag/短标签作记忆锚。",
                "icon_or_motif": "城市/情绪 B-roll、黑底结尾字。",
                "background_layer": "黑底或浅色 B-roll。",
                "depth_and_space": "单主体，层级收敛。",
                "color_weight": "比中段更轻，少黄色。",
                "information_density": "低。",
                "motion_behavior": "B-roll 或硬切结尾卡。",
                "transition_behavior": "证据密度降为情绪收束。",
                "pacing_feel": "柔和收尾。",
                "attention_path": "结尾短句 -> B-roll/主持人 -> hashtag。",
                "viewer_first_impression": "从工具证据回到情绪记忆点。",
                "why_it_feels_like_reference": "长文本证据后用轻画面收束，避免沉重。",
                "what_must_not_be_copied": "不要复制 B-roll 或原 hashtag；只学降密度收尾功能。",
            },
        },
    ],
}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def read_summary() -> dict:
    return json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))


def timeline_markdown(ref_id: str, segments: list[dict]) -> str:
    lines = [
        f"# {ref_id} Dynamic Visual Timeline",
        "",
        "status_boundary:",
        "- `task_result.status = dynamic_visual_master_parse`",
        "- `source_video_read = true`",
        "- `prior_parse_trust = failed_prior_parse / low_trust_reference_summary / diagnostic_reference_only`",
        "- `content_validation = not_applicable`",
        "- `send_ready = false`",
        "- `new_fourth_episode_modified = false`",
        "- `formal_mechanism_updated = false`",
        "",
        "evidence:",
        f"- `5s_contact_sheets = {DIST_DIR.relative_to(ROOT)}/{ref_id}/contact_sheet_5s_page_*.jpg`",
        f"- `scene_contact_sheet = {DIST_DIR.relative_to(ROOT)}/{ref_id}/contact_sheet_scene_candidates.jpg`",
        f"- `dynamic_1s_clips = {DIST_DIR.relative_to(ROOT)}/{ref_id}/dynamic_1s_clips/`",
        "",
    ]
    for idx, segment in enumerate(segments, start=1):
        lines.extend(
            [
                f"## segment_{idx:02d}",
                "",
                f"- `time_range`: `{segment['time_range']}`",
                f"- `representative_frame_path`: `{segment['representative_frame_path']}`",
                "- `visual_state`:",
            ]
        )
        for field in FIELDS:
            lines.append(f"  - `{field}`: {segment['visual_state'][field]}")
        lines.append("")
    return "\n".join(lines)


def write_timelines() -> None:
    for ref_id, segments in TIMELINES.items():
        write(LOG_DIR / f"{ref_id}_dynamic_visual_timeline.md", timeline_markdown(ref_id, segments))


def write_route_and_boundary(summary: dict) -> None:
    source_rows = []
    for ref_id, item in summary["references"].items():
        meta = item["metadata"]
        source_rows.append(
            f"| `{ref_id}` | `{item['source_path']}` | `{meta['duration_seconds']:.3f}s` | `{meta['width']}x{meta['height']}` | `{meta['fps']:.3f}` | `{item['ffmpeg_smoke']['status']}` | `{item['sampling']['opencv']['opencv_opened']}` |"
        )
    content = f"""
# Route And Status Boundary

## route_decision

- `project_route = video_factory`
- `task_type = review_diagnosis_audit + reference_analysis_only + local_file_governance + project_file_change`
- `selected_state = dynamic_visual_master_parse`
- `responsibility_layer = project_judgment_layer + validation_layer + sync_layer`
- `why_not_video_task = user prompt explicitly forbids generating video, validation clip, full candidate, or modifying new fourth episode; this round only reparses source reference videos`
- `execution_permission = allowed_after_route_read_and_source_video_count_confirmed`

## state_action_router

- `input_signal = latest editing reference videos + prior parse rejected as insufficient visual standard`
- `current_project_state = reference_contract_needed + ambiguous_reference_goal_resolved_by_user_as_visual_look_dynamic_master + deepseek_supply_required + mandatory_commit_push_required`
- `fact_source_arbitration.primary_source = source videos under 素材录制/剪辑参考/最新剪辑参考`
- `fact_source_arbitration.prior_parse = diagnostic_reference_only`
- `trigger_mechanism = Reference-to-Execution Contract + dynamic visual master parse`
- `selected_action = generate frame evidence, timelines, visual maps, failure report, contract draft, migration notes, latest update`
- `forbidden_action = generate new video, edit source videos, update formal mechanisms, touch dist/latest_review_pack, promote validation/send states`
- `done_when = 4/4 probe + extraction passed, required reports exist, validation passes, path-limited commit/push/readback done`

## large_task_gate

- `large_task_gate.triggered = true`
- `large_task_gate.reason = 4 reference videos, each longer than 180 seconds or near it, with frame extraction, scene candidates, timelines, maps, validation, commit/push`
- `lane_recommendation = audit_lane -> standard_lane after source video evidence generated`
- `parallel_recommendation = serial_only`
- `parallel_reason = outputs share one report package and final judgment must integrate visual observations consistently`
- `write_owner = Codex integrator`
- `read_only_lanes = DeepSeek pre-supply attempted; source videos read-only; prior parse read via git show only`
- `integration_owner = Codex`

## deepseek_supply_gate

- `supply_request = codex_log/supply_requests/20260602_最新剪辑参考4条动态视觉母版重解析_pre_supply_request.json`
- `runner_output = codex_log/deepseek_supply/20260602_latest_4_dynamic_visual_master_reparse_pre_supply/latest_supply_pack.md`
- `deepseek_participation_report = blocked_invalid_context_pack`
- `fallback_status = fallback_local_only`
- `not_deepseek_conclusion = true`
- `token_usage_expectation_check = token_decrement_expected_if_real_call_succeeds / not_observable_by_codex`
- `api_key_printed = false`
- `api_key_written = false`

## source_videos

| reference | source_path | duration | resolution | fps | ffmpeg_smoke | opencv_open |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(source_rows)}

## allowed_changes

- `codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/`
- `scripts/最新剪辑参考动态视觉母版重解析_generate_dynamic_visual_evidence.py`
- `scripts/最新剪辑参考动态视觉母版重解析_write_reports.py`
- `codex_log/supply_requests/20260602_最新剪辑参考4条动态视觉母版重解析_pre_supply_request.json`
- `codex_log/deepseek_supply/20260602_latest_4_dynamic_visual_master_reparse_pre_supply/`
- `codex_log/latest.md`

## forbidden_changes

- 不生成新第四期视频、验证片、完整候选片。
- 不修改 `/Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考` 源视频。
- 不修改 `GPT数据源/` 正式机制、`codex_source/` 正式规则、`dist/latest_review_pack/`。
- 不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。
- 不把旧解析报告当正式视觉标准。

## actual_read_files

- `AGENTS.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/00_codex_readme.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/20_reference_to_execution_contract.md`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_log/latest.md`
- `git show 191f02f431f424af42979830c3194305fb7b5e93:codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/...`
- `/Users/fan/.codex/skills/video-metadata-probe/SKILL.md`

## status_boundary_check

- `video_rendered = false`
- `source_videos_modified = false`
- `new_fourth_episode_modified = false`
- `formal_mechanism_updated = false`
- `dist_latest_review_pack_modified = false`
- `content_validation = not_applicable`
- `send_ready = false`
- `visual_master_locked = false`
"""
    write(LOG_DIR / "route_and_status_boundary.md", content)


def write_maps() -> None:
    write(
        LOG_DIR / "composition_map.md",
        """
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
""",
    )

    write(
        LOG_DIR / "typography_subtitle_highlight_map.md",
        """
# Typography Subtitle Highlight Map

## typography

- 大标题：短词、粗体、高对比，常见白字 + 黄绿/紫粉关键词。它用于开头或章节，不承担长解释。
- 结构卡：黄底黑字或绿底黑字，单屏少词，位置靠近对应概念/步骤。
- 证据页：原 UI 小字不可靠，必须用外层高亮、裁切或重新排版让关键句可读。

## subtitle

- 源视频字幕属于平台壳低区，和画内证据天然分离。
- 横屏迁移必须建立 `subtitle_safe_zone`，字幕不得压住白页证据、黄线高亮、按钮、表格、手机框底部。
- 字幕是语义节奏，不是视觉主角；主视觉仍应由证据窗口 / 主持人 / 标题卡承担。

## highlight

| highlight type | source references | use | warning |
| --- | --- | --- | --- |
| `yellow_reading_line` | `reference_03`, `reference_04` | 长文本、文档、聊天页证据读线 | 只可贴真实证据，不可作装饰 |
| `green_keyword_badge` | `reference_02`, `reference_03` | 标功能词、结果词、步骤词 | 不要每个词都贴，必须绑定目标 |
| `large_title_emphasis` | all | 开头钩子、章节重置 | 不要让大标题代替证据 |
| `corner_label` | `reference_01` | 对比格、结果窗口标注 | 无比较关系时不要硬做 |
""",
    )

    write(
        LOG_DIR / "motion_transition_map.md",
        """
# Motion Transition Map

## confirmed_motion_language

- 主转场是 `hard_cut`，不是花哨转场。参考感来自切换对象和注意力路径，不是动效复杂度。
- 高频动态包括：主持人手势、标题弹出、证据窗口硬切、手机内容替换、黄线位置变化、PIP 出现/退场。
- 密集证据段必须插入 `host_reset`、`title_reset` 或 `low_density_bridge`，否则会变成小字堆叠。

## one_second_dynamic_clips

每条参考已抽 8 个 1 秒证据 clips，覆盖 opening、large change、highlight/evidence/bridge/density/late section：

- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/dynamic_1s_clips/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/dynamic_1s_clips/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/dynamic_1s_clips/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/dynamic_1s_clips/`

## motion rules

1. `host_to_evidence_cut`: 主持人提出判断后 1-3 秒内切入证据窗口。
2. `evidence_window_replace`: 同类证据窗口可以硬切替换，保持位置稳定，降低学习成本。
3. `highlight_move`: 长文本只移动高亮或换高亮行，不让整页乱跳。
4. `density_reset`: 高密证据段结束必须回到主持人/标题/低字数卡。
5. `split_only_if_relation`: 分屏只在 before/after、source/output、reference/result、步骤对照成立时出现。
""",
    )

    write(
        LOG_DIR / "density_hierarchy_map.md",
        """
# Density Hierarchy Map

## density levels

| level | visual state | reference examples | migration note |
| --- | --- | --- | --- |
| `low_density_hook` | 主持人 + 大标题 + 少量关键词 | ref01/02/03/04 opening | 建立第一眼，不要上来塞全页资料 |
| `medium_structure` | 黄绿结构卡、概念图、1-3 个短标签 | ref03 00:20-01:15, ref04 00:35-01:10 | 用来解释抽象关系 |
| `high_evidence` | 白色文档/手机/网页窗口 + 高亮 | ref03/ref04 middle | 必须有读线和字幕安全区 |
| `high_montage` | 多窗口比较板或结果轮播 | ref01, ref02 | 只用于真实比较/结果展示 |
| `reset_bridge` | 主持人、黑底短标题、低字数卡 | all | 每个高密段后必须出现 |

## hierarchy rules

- 主信息：主持人或大标题先锁问题。
- 证据：白页/手机/网页/结果窗口承载证明。
- 导视：黄线、绿 badge、角标只指读哪里。
- 字幕：解释语义，不抢证据区。
- 装饰：图标、头像、平台元素必须降权，不能抢主证据。
""",
    )

    write(
        LOG_DIR / "pacing_map.md",
        """
# Pacing Map

## pacing by reference

| reference | opening cadence | proof cadence | reset cadence | useful for |
| --- | --- | --- | --- | --- |
| `reference_01` | 0-20s 快速主持人/标题/拼贴 | 3-6s 一次样例或窗口替换 | 30-60s 插主持人/章节卡 | 综合工具展示、比较板、结果 montage |
| `reference_02` | 0-18s 从主持人切手机框 | 手机内容 3-8s 替换 | 主持人间歇复位 | 手机框和关键词包装 |
| `reference_03` | 0-20s 主持人 + 大标题 | 概念卡 5-10s，文档证据 10-20s | 结构卡/主持人复位 | 教学解释、流程拆解 |
| `reference_04` | 0-35s 主持人 + 主题卡 | 长文本证据 10-30s 持续陪读 | 主持人/列表/轻 B-roll reset | 长文本证据、记忆/方法类讲解 |

## pacing rules

- 开头 3 秒必须有明确第一眼主对象。
- 高密证据不可连续超过 30-45 秒不 reset。
- 结果 montage 可以快，但文档/表格/聊天页必须慢一点并提供高亮。
- 若横屏素材是用户录屏，优先采用 ref03/ref04 的稳态证据节奏，而不是 ref01 的电影结果轰炸。
""",
    )

    write(
        LOG_DIR / "attention_path_map.md",
        """
# Attention Path Map

## common path

`host face / title -> target evidence window -> highlight or badge -> subtitle -> host reset`

## per_reference_attention

- `reference_01`: 脸和标题先抓眼，随后看对比标签，再看左右样例；适合结果差和能力展示。
- `reference_02`: 手机框是第一主读区，绿色 badge 是第二主读区，主持人 PIP 是第三层；适合轻量移动端包装。
- `reference_03`: 关键词卡/概念图先定义关系，再进入文档高亮；适合把抽象流程讲清。
- `reference_04`: 黄色高亮线是阅读光标，主持人复位负责防止长文疲劳；适合长文本/聊天证据。

## deviation checks

- 观众第一眼如果先看到平台 UI、互动栏、头像或装饰，而不是主题/证据，即偏离。
- 证据窗口如果没有高亮/裁切，观众需要自己扫整页，即偏离。
- badge 如果离目标窗口太远，变成漂浮贴纸，即偏离。
- 字幕如果和证据文字抢同一位置，即偏离。
""",
    )


def write_classification_contract_failure_and_templates() -> None:
    write(
        LOG_DIR / "reference_visual_role_classification.md",
        """
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
""",
    )

    write(
        LOG_DIR / "visual_reference_contract_draft.md",
        """
# Visual Reference Contract Draft

## reference_anchor

- `reference_id = latest_4_dynamic_visual_master_reparse_20260602`
- `reference_type = dynamic_visual_master + editing_reference + evidence_window_reference + typography_highlight_reference`
- `source_layer = user_provided_local_source_videos`
- `exact_reference_available = true`
- `source_dir = /Users/fan/Documents/视频工厂/素材录制/剪辑参考/最新剪辑参考`
- `primary_reference_video = reference_03 + reference_04`
- `support_reference_video = reference_01 + reference_02`

## effect_targets

- `viewer_first_impression`: 第一眼知道有人在带着看一个 AI 工具/机制/证据，不是随手拼屏。
- `information_hierarchy`: 主持人或标题先定题，证据窗口承载证明，高亮/badge 指读哪里，字幕解释语义。
- `visual_weight`: 证据窗口 > 主持人 reset > 高亮/badge > 字幕 > 装饰。
- `pacing`: 高密证据段必须与低密 reset 交替。
- `evidence_clarity`: 文档、手机、聊天、网页等证据必须有可读裁切或高亮读线。

## function_fields

| field | value |
| --- | --- |
| `input_signal` | 用户要求重解析最新四条剪辑参考的视频源 |
| `evidence_role` | 动态视觉母版，不是正式项目机制 |
| `importance_type` | `must_preserve_visual_language / must_not_copy_assets` |
| `target_area` | composition, typography, subtitle, highlight, motion, transition, density, attention path |
| `selected_action` | 生成动态视觉时间线、视觉地图、偏离检查模板和迁移说明 |
| `validation_rule` | 每条 reference 必须回指源视频、frame/contact sheet/dynamic clip 证据 |
| `blocked_if` | 只写机制名、无关键帧、无第一眼描述、复制平台 UI 或第三方资产、推进状态 |

## must_preserve

- 黑底/深灰舞台承载证据窗口。
- 主持人/标题 reset 与证据窗口交替。
- 证据窗口必须有位置、大小、持续时间、出现/消失方式和遮挡关系。
- 黄/绿高亮必须绑定真实证据位置。
- 分屏只在关系成立时使用。

## can_vary

- 颜色皮肤、字体、角色、项目品牌、横屏布局、证据素材、卡片形态。

## must_not_copy

- 真人脸、平台 UI、互动栏、头像、logo、第三方视频/图片、原 app UI、原字幕/标题文案、平台水印或商业标识。

## done_when

- 4 条源视频技术探针通过。
- 每条有动态视觉时间线。
- 组合地图、角色分类、偏离检查模板、迁移说明完成。
- 不修改新第四期、不推进正式状态。
""",
    )

    write(
        LOG_DIR / "previous_parse_failure_report.md",
        """
# Previous Parse Failure Report

## prior_parse_status

- `prior_parse_path = codex_log/reference_analysis/20260602_最新剪辑参考4条深度解析_latest_4_editing_references_deep_parse/`
- `prior_commit = 191f02f431f424af42979830c3194305fb7b5e93`
- `availability_on_main = missing_from_worktree`
- `access_method = git show 191f02f431f424af42979830c3194305fb7b5e93:<path>`
- `new_status = failed_prior_parse / low_trust_reference_summary / diagnostic_reference_only`

## failure_reason

1. `mechanism_name_over_visual_language`: 旧报告大量使用 split_screen、keyword、screen_packaging、rhythm 等机制词，但没有充分说明第一眼画面怎么组成、主对象在哪里、窗口多大、持续多久、如何出现/消失。
2. `insufficient_dynamic_state`: 旧时间线按 40-60 秒大段描述，缺少动态关系：主持人何时变 PIP、证据窗口何时上来、黄线怎么换、reset 如何降密度。
3. `classification_too_early`: 旧分类把 reference_01 写成 main_style_reference，但从源视频重看，reference_03/04 对“教学/证据窗口视觉母版”更直接，reference_01 更适合作为结果 montage 与比较板支持。
4. `side_by_side_missing`: 旧包没有把未来候选片与参考并排检查所需的字段模板落清楚。
5. `visual_first_impression_missing`: 旧报告没有把用户要的“第一眼像不像”拆成构图、重心、密度、颜色权重和注意力路径。

## retained_value

- 旧包的 ffprobe、5s 抽帧、scene 候选和 contact sheet 思路有参考价值。
- 旧包的“不可复制平台 UI / 真人 / logo”边界仍成立。
- 旧包可作为失败样本和诊断材料，不作为本轮主判断。

## replacement_standard

本轮以 `dynamic_visual_master_parse` 替代旧 `deep_parse`：每条 timeline 必须包含 `layout_composition / main_subject_position / evidence_window_position / pip_or_host_position / subtitle_position / typography_style / highlight_style / keyword_badge_style / icon_or_motif / background_layer / depth_and_space / color_weight / information_density / motion_behavior / transition_behavior / pacing_feel / attention_path / viewer_first_impression / why_it_feels_like_reference / what_must_not_be_copied`。
""",
    )

    write(
        LOG_DIR / "side_by_side_deviation_check_template.md",
        """
# Side By Side Deviation Check Template

status_boundary:
- `template_only = true`
- `new_fourth_episode_modified = false`
- `content_validation = not_applicable`

## usage

未来只有在用户要求修改/重做新第四期或下一条视频时，才能用本模板对照候选片。当前本轮不对新第四期做修改，也不声称它已符合参考。

| check_id | reference_anchor | expected_dynamic_visual | candidate_frame_path | candidate_observation | deviation_level | repair_if_needed | pass_condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `first_impression` | ref03/ref04 opening | 3 秒内出现主持人/标题/核心对象，第一眼清楚主题 |  |  | `none/minor/major/blocking` | 重做 opening hierarchy | 观众第一眼不先看平台壳或装饰 |
| `evidence_window` | ref03/ref04 middle | 主证据窗口占 55%-70% 横屏宽，有裁切/高亮 |  |  |  | 调整窗口尺寸、位置、裁切 | 关键证据可读 |
| `highlight_binding` | ref03/ref04 yellow/green highlighter | 高亮贴真实证据，不漂浮 |  |  |  | 重新绑定高亮位置 | 高亮能回答“看哪里” |
| `host_reset` | all | 高密证据后有主持人/标题/低密度卡 reset |  |  |  | 插入 reset bridge | 高密段不连续疲劳 |
| `split_relation` | ref01 comparison board | 分屏只用于真实比较关系 |  |  |  | 去掉装饰分屏或补足比较关系 | 分屏左右有语义关系 |
| `subtitle_safe_zone` | all | 字幕不压证据窗口/OCR/高亮 |  |  |  | 重排字幕或证据窗口 | 无 high severity overlap |
| `asset_copy_risk` | all | 无平台 UI/真人/logo/第三方素材复制 |  |  |  | 替换为项目原创资产 | 无侵权/误导性复制 |

## blocking_deviation

- 只有大标题页，没有证据窗口。
- 证据窗口小到不可读。
- 黄/绿标签离目标太远，变成装饰。
- 分屏没有比较关系。
- 字幕、卡片、OCR 三层文字互相遮挡。
- 复制平台 UI、真人、logo 或第三方素材。
""",
    )

    write(
        LOG_DIR / "migration_notes_for_new_fourth_episode_dynamic_visual_only.md",
        """
# Migration Notes For New Fourth Episode Dynamic Visual Only

status_boundary:
- `not_video_task = true`
- `new_fourth_episode_modified = false`
- `candidate_generated = false`
- `content_validation = not_applicable`
- `send_ready = false`

## current_round_scope

本轮只完成动态视觉母版重解析，不回炉新第四期，不改任何新第四期素材、剪辑、声音、字幕、review_pack 或 `dist/latest_review_pack/`。

## future_migration_priority

1. `primary`: 用 `reference_03` 处理“教学/流程/工具机制怎么讲清楚”。
2. `primary`: 用 `reference_04` 处理“长文本/聊天/文档证据怎么被高亮带读”。
3. `support`: 用 `reference_01` 处理“结果差/能力样例/比较板/章节 reset”。
4. `support`: 用 `reference_02` 处理“手机框和绿色关键词包装”，不要把它当整片主视觉。

## future_execution_notes

- 新第四期若继续使用用户录屏/文档/表格证据，应优先迁移 ref03/ref04 的证据窗口和高亮读线，而不是复制竖屏平台壳。
- 若句组没有 before/after、source/output、reference/result 关系，不应强行使用 ref01 多窗口分屏。
- 若需要手机框，只作为局部证据容器，不能让手机框小到看不清。
- 字幕必须与证据窗口分离；动态高亮不能被字幕覆盖。
- 所有角色、图标、标签、品牌和背景必须重做为《视频工厂》原创视觉语言。

## blocked_if_future_video_task

- 缺 locked copy contract。
- 缺 line_group 级 script_to_timeline_map。
- 缺 evidence window plan。
- 缺 subtitle_card_overlap_check。
- 缺 side-by-side deviation check。
- 试图复制平台 UI / 真人 / logo / 第三方样例。
""",
    )


def write_manifest(summary: dict) -> None:
    required_files = [
        "route_and_status_boundary.md",
        "reference_01_dynamic_visual_timeline.md",
        "reference_02_dynamic_visual_timeline.md",
        "reference_03_dynamic_visual_timeline.md",
        "reference_04_dynamic_visual_timeline.md",
        "composition_map.md",
        "typography_subtitle_highlight_map.md",
        "motion_transition_map.md",
        "density_hierarchy_map.md",
        "pacing_map.md",
        "attention_path_map.md",
        "reference_visual_role_classification.md",
        "visual_reference_contract_draft.md",
        "previous_parse_failure_report.md",
        "side_by_side_deviation_check_template.md",
        "migration_notes_for_new_fourth_episode_dynamic_visual_only.md",
        "reference_video_inventory.md",
        "media_probe_and_sampling_summary.json",
    ]
    manifest = {
        "analysis_id": "20260602_latest_4_dynamic_visual_master_reparse",
        "status": "dynamic_visual_master_parse_completed_pending_user_chatgpt_review",
        "source_video_count": summary["reference_count"],
        "prior_parse_handling": "failed_prior_parse / low_trust_reference_summary / diagnostic_reference_only",
        "content_validation": "not_applicable",
        "send_ready": False,
        "visual_master_locked": False,
        "new_fourth_episode_modified": False,
        "formal_mechanism_updated": False,
        "required_files": required_files,
        "required_files_exist": {name: (LOG_DIR / name).exists() for name in required_files},
        "media_evidence_dir": str(DIST_DIR.relative_to(ROOT)),
        "source_videos": {ref_id: item["source_path"] for ref_id, item in summary["references"].items()},
    }
    write(LOG_DIR / "analysis_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))


def main() -> None:
    summary = read_summary()
    write_timelines()
    write_route_and_boundary(summary)
    write_maps()
    write_classification_contract_failure_and_templates()
    write_manifest(summary)
    print(json.dumps({"status": "ok", "log_dir": str(LOG_DIR.relative_to(ROOT))}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
