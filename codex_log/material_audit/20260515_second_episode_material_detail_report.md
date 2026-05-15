# 20260515 第二期素材细节审计报告

## 1. route_decision（路由判断）

- `project_route`: `video_factory`
- `task_type`: `review_diagnosis_audit + data_review_loop + material_audit_report_only`
- `current_stage`: `formal_operation_active`
- `current_operation_target`: `V003`
- `current_data_goal_anchor_status`: `partial_data_recorded`
- `execution_permission`: 只允许本地只读素材审计、抽帧、OCR、写审计报告。
- `forbidden_status_promoted`: 无。未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked`。
- `deepseek_supply_gate`: `fallback_local_only`。本轮用户只授权本地素材审计；未调用外部 API；本报告不是 DeepSeek 结论。

## 2. 必读文件读取状态

### read_ok

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_source/01_execution_rules.md`
4. `codex_log/latest.md`
5. `codex_log/current_operation_target.md`
6. `review_loop/operation_records_index.md`
7. `codex_log/current_data_goal_anchor.md`
8. `GPT数据源/04_选题与文案规则.md`
9. `GPT数据源/05_文案路由规则.md`
10. `GPT数据源/13_目标驱动数据飞轮与文案执行闭环_goal_driven_data_flywheel_and_copy_execution_loop.md`
11. `GPT数据源/14_数据目标执行总线_data_goal_execution_bus.md`
12. `codex_source/13_execution_lane_and_parallel_rules.md`
13. `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
14. `codex_source/19_project_state_action_router.md`
15. `GPT数据源/11_项目状态动作总控器_机制推理层.md`
16. `~/.codex/skills/video-metadata-probe/SKILL.md`

### missing

- 仓库本地 `skills/` 目录未发现可用本地 skill；已回退使用全局 `video-metadata-probe`。

### 是否影响本轮素材审计

- 不影响。关键边界已确认：当前只是素材审计和 ChatGPT 写稿供料；不得生成正式文案、不得生成下一条视频执行 prompt、不得推进任何发布 / 内容 / 声音 / 视觉母版状态。

## 3. 素材路径解析

```text
material_path_resolution:
  resolved_path: /Users/fan/Documents/视频工厂/素材录制/第二期
  checked_paths:
    - /Users/fan/Documents/视频工厂/素材录制/第二期: found
    - /Users/fan/Documents/视频工厂/视频工厂-素材录制-第二期: missing
    - /Users/fan/Documents/视频工厂-素材录制-第二期: missing
  video_count: 2
  video_files:
    - /Users/fan/Documents/视频工厂/素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4
    - /Users/fan/Documents/视频工厂/素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4
```

审计副产物：

- 抽帧目录：`dist/material_audit/second_episode/`
- OCR 原始表：`dist/material_audit/second_episode/ocr_raw.tsv`
- 联系表：`video_1_contact_sheet_part1-5.jpg`、`video_2_contact_sheet_part1-5.jpg`

## 4. video_file_metadata（视频文件信息）

### video_1

```text
filename: 目标录制   2026-05-14 22-17-06.mp4
absolute_path: /Users/fan/Documents/视频工厂/素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4
relative_path_if_inside_repo: 素材录制/第二期/目标录制   2026-05-14 22-17-06.mp4
file_size: 169,956,091 bytes
duration: 102.50s
resolution: 3338x1644
fps: 30
video_codec: h264
audio_exists: false
audio_codec: none
can_open: true
decodable: true
visible_quality: 屏幕录制清晰，关键大字和高亮段可读；部分缩放后的长段小字需结合 OCR，仍有少量 unclear。
obvious_issues: 无音轨；没有真人、没有外部软件执行画面；主体是 ChatGPT / Pro 生成 prompt 与用户追问过程。
sha256: af27135d6666e67cd2618b7ed57238c3cd539b1959ee67dc1964cded77b2db6c
```

### video_2

```text
filename: 内建视网膜显示器 2026-05-14 22-44-29.mp4
absolute_path: /Users/fan/Documents/视频工厂/素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4
relative_path_if_inside_repo: 素材录制/第二期/内建视网膜显示器 2026-05-14 22-44-29.mp4
file_size: 194,136,706 bytes
duration: 119.03s
resolution: 3248x1626
fps: 30
video_codec: h264
audio_exists: false
audio_codec: none
can_open: true
decodable: true
visible_quality: 屏幕录制清晰，多个局部放大能读；长表格局部文字仍需标记为 partially readable。
obvious_issues: 无音轨；后半段 `video_goal_card` 模板只露出开头，完整模板没有录完；没有显示真实发布后台或平台数据页面。
sha256: 56fde4194677ec611b290bfdd6d1942390a1ec0dab8c8f49daafd7a518ef0b5d
```

## 5. timecoded_material_report（逐时间码素材报告）

### video_1：目标录制

#### segment_v1_01

```text
start_time: 00:00
end_time: 00:08
visual_summary: ChatGPT / Pro 页面。顶部黄色用户输入要求给《视频工厂》一个 pro prompt，用来定义项目目标，包含客资、点赞、播放等。
visible_page_or_app: ChatGPT web / Pro 对话页
visible_text:
  - "目前我觉得项目缺少的是目标..."
  - "一个最合适项目的目标，包括客资，点赞，播放..."
  - "项目缺的不是播放目标本身，而是目标分层..."
user_action: 鼠标停留与轻微移动，页面停在 AI 回复起始区域。
ai_action_or_output: AI 先指出不能只要播放 KPI，要做项目目标重判。
result_or_change: 从用户的糊目标请求，被改写成“项目目标重判”方向。
evidence_strength: strong
can_prove: 素材里存在“原始糊话 / 模糊目标输入”和 AI 初步纠偏。
cannot_prove: 不能证明最终目标机制已落库，也不能证明下一条视频可执行。
writing_use: narration + proof_visual
risk_or_unclear_point: 部分原始输入小字需要 OCR 辅助；不能把这段写成最终文案已经完成。
```

#### segment_v1_02

```text
start_time: 00:08
end_time: 00:22
visual_summary: 页面显示 AI 输出的 Markdown prompt，包含项目背景、OPC 上位身份、当前中心价值与视频主线。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "《视频工厂｜OPC 一人公司 AI 闭环验证系统》"
  - "真实 AI 使用经验 + 工作提效实录"
  - "API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑"
  - "但这只是内容化输出载体，不是项目最终目标"
user_action: 滚动查看 AI 生成内容。
ai_action_or_output: 输出一版更结构化的 prompt 背景。
result_or_change: 把项目身份、内容出口、反馈入口放进 prompt。
evidence_strength: strong
can_prove: 可证明“结构化 prompt 过程”存在，且包含项目事实约束。
cannot_prove: 不能证明这些规则就是当前仓库最新事实；最终仍应以仓库文件为准。
writing_use: subtitle + proof_visual + narration
risk_or_unclear_point: 可以写“画面里 AI 把目标拆成背景和机制”，不能写“系统已正式执行目标飞轮”。
```

#### segment_v1_03

```text
start_time: 00:22
end_time: 00:36
visual_summary: 继续展示第一版 prompt 的需求列表，要求北极星目标、0-30 / 31-90 / 90-180 天目标、指标树、有效客资定义、单条视频目标卡、发布后复盘目标卡。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "不要把所有私信都算客资"
  - "请给播放、点赞、客资的合理阶段目标"
  - "请把播放、点赞、收藏、评论、关注、私信、客资、成交放进一棵树里"
  - "有效客资定义表"
  - "单条视频目标卡模板"
user_action: 滚动并局部放大阅读。
ai_action_or_output: 第一版 prompt 已经把散指标拆成多个可回答模块。
result_or_change: 从散指标转成目标 / 阶段 / 指标树 / 客资定义 / 复盘卡的需求清单。
evidence_strength: strong
can_prove: 素材支持“普通问法被结构化成目标系统需求”。
cannot_prove: 不能证明各阈值已正确、也不能证明用户已经接受第一版。
writing_use: proof_visual + subtitle + card
risk_or_unclear_point: 这仍是 prompt 生成过程，不是最终项目机制落库证据。
```

#### segment_v1_04

```text
start_time: 00:36
end_time: 00:44
visual_summary: 用户指出当前 prompt 仍有问题，希望项目能根据目标驱动，每一期视频发布和复盘后加速数据飞轮，再让 AI 补一个 prompt。
visible_page_or_app: ChatGPT 对话页
visible_text:
  - "我觉得现在这个 prompt 有问题..."
  - "项目可以根据目标来进行驱动..."
  - "每一期我发出去，然后复盘之后..."
  - "加速我数据飞轮，再给我一个 prompt，并且帮我补全"
user_action: 继续追问并要求改方向。
ai_action_or_output: AI 解释上一版更像 KPI，用户真正要的是“目标 -> 发布 -> 数据 -> 复盘 -> 下一期变量”的轮转。
result_or_change: 第一版 prompt 被用户否定并触发第二版“目标驱动数据飞轮机制”。
evidence_strength: strong
can_prove: 有明确 before/after 缺口：第一版不够，原因是没有把数据反馈驱动下一期变量讲透。
cannot_prove: 不能证明后续视频一定要讲“数据飞轮”全套，只能证明素材中有这个迭代过程。
writing_use: narration + proof_visual
risk_or_unclear_point: 这一段适合做“普通 prompt 不够用”的转折，不适合写成产品能力已经稳定。
```

#### segment_v1_05

```text
start_time: 00:44
end_time: 01:04
visual_summary: AI 输出第二版 prompt，标题方向变成“目标驱动的数据飞轮机制”，重新定义项目背景、当前问题和真正想验证的内容。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "目标驱动的数据飞轮机制"
  - "项目可以被目标驱动"
  - "每一期视频发布后，系统能根据播放、留存、点赞、收藏、评论、私信、客资、转化等反馈..."
  - "把真实问题变成内容，把内容发布到平台验证，再通过数据反馈沉淀出产品、服务、工作包..."
user_action: 滚动查看并放大第二版 prompt。
ai_action_or_output: 第二版输出将项目目标、数据反馈和产品 / 服务沉淀串起来。
result_or_change: prompt 从静态 KPI 表升级为数据飞轮机制。
evidence_strength: strong
can_prove: 可证明“改 prompt 过程”和“更好的结构化结果”。
cannot_prove: 不能证明数据飞轮真实跑通，也不能证明已产生客资。
writing_use: proof_visual + card + narration
risk_or_unclear_point: 必须保留“机制设计 / prompt 结果”，不能写成现实运营结果。
```

#### segment_v1_06

```text
start_time: 01:04
end_time: 01:22
visual_summary: 第二版 prompt 继续展开：项目到底应该被什么目标驱动、四圈飞轮、只改一个变量、自动补全指标体系、有效客资定义。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "请你设计一套数据飞轮机制"
  - "第一圈飞轮 / 第二圈飞轮 / 第三圈飞轮 / 第四圈飞轮"
  - "只改一个变量"
  - "自动补全指标体系"
  - "有效客资"
user_action: 滚动浏览。
ai_action_or_output: 输出可被 ChatGPT 后续借用的结构化模块名。
result_or_change: 从“目标”扩展到“每轮变量选择”和“指标体系”。
evidence_strength: medium
can_prove: 有结构化拆解过程。
cannot_prove: 不能证明四圈飞轮每项都已可执行。
writing_use: subtitle + card + background_only
risk_or_unclear_point: 部分文字小，适合抽成字幕 / 卡片，不适合逐字口播。
```

#### segment_v1_07

```text
start_time: 01:22
end_time: 01:42.5
visual_summary: 结尾部分展示数据飞轮记忆、阶段数字只是保守假设、回答要求和最终区别。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "data_flywheel_memory（数据飞轮记忆）"
  - "video_id / topic / target_user / hypothesis / main_variable..."
  - "这些数字只是阶段工作假设，不是行业定论"
  - "这一版是在问：目标怎么驱动每一期内容，并用数据反推下一期怎么改"
user_action: 滚动到结尾。
ai_action_or_output: 输出记忆结构和最终说明。
result_or_change: 形成可交给 Pro / ChatGPT 的更完整 prompt 方向。
evidence_strength: medium
can_prove: 第二版比第一版更接近“数据目标驱动”。
cannot_prove: 不能证明已生成可执行视频 prompt；也不能证明数据目标 anchor 已 ready。
writing_use: card + narration + proof_visual
risk_or_unclear_point: 结尾是 prompt 说明，不是执行完成状态。
```

### video_2：内建视网膜显示器

#### segment_v2_01

```text
start_time: 00:00
end_time: 00:12
visual_summary: 第二个视频直接显示 AI 回答结果，包含“一句话主判断”和“项目北极星目标”。
visible_page_or_app: ChatGPT / Pro 回答页
visible_text:
  - "不是先追播放，不是先追成交，而是先验证..."
  - "不是看我能不能做视频，而是看这些视频能不能持续帮我找到真实有需求的人。"
  - "3-6个月内，通过连续发布和复盘，验证《视频工厂》能否稳定产生高质量需求信号..."
user_action: 滚动和局部放大阅读。
ai_action_or_output: 输出项目判断和北极星目标。
result_or_change: 第二段承接 video_1 的第二版 prompt，展示更完整的 AI 结果。
evidence_strength: strong
can_prove: 有“改 prompt 后得到更具体判断”的结果画面。
cannot_prove: 不能证明目标已经被用户 / ChatGPT 最终采纳。
writing_use: proof_visual + narration + subtitle
risk_or_unclear_point: 不要写成正式项目目标已经通过，只能写成素材中的 AI 输出候选。
```

#### segment_v2_02

```text
start_time: 00:12
end_time: 00:22
visual_summary: 展示“为什么不是单纯追播放 / 点赞 / 客资”以及四圈飞轮。
visible_page_or_app: ChatGPT / Pro 回答页
visible_text:
  - "不是单纯追播放"
  - "不是单纯追点赞"
  - "不是一开始追成交"
  - "客资重要，但不该一开始当唯一主目标"
  - "第一圈：内容飞轮 / 第二圈：需求飞轮 / 第三圈：客资飞轮 / 第四圈：产品化飞轮"
user_action: 滚动。
ai_action_or_output: 解释指标和飞轮层级。
result_or_change: 将目标拆成内容、需求、客资、产品化四层。
evidence_strength: strong
can_prove: 可证明输出不是简单 KPI，而是层级判断。
cannot_prove: 不能证明四圈飞轮在项目中真实运转。
writing_use: card + subtitle + narration
risk_or_unclear_point: 可写“AI 把指标从散点整理成层级”，不能写“项目已形成稳定商业飞轮”。
```

#### segment_v2_03

```text
start_time: 00:22
end_time: 00:46
visual_summary: 展示指标分层表，包含触达层、认可层、互动层、需求层、客资层、商业验证层，以及每层代表什么和不能代表什么。
visible_page_or_app: ChatGPT 表格
visible_text:
  - "触达层：播放量、推荐流量、3秒留存、5秒留存、完播率、平均观看时长"
  - "认可层：点赞、收藏、转发、关注、主页访问"
  - "互动层：评论数、评论质量、复述痛点、追问细节"
  - "需求层：私信数、有效私信数、问工具 / 流程 / 模板 / 服务的人数"
  - "商业验证层：付费咨询、定制化视频、AI工作流搭建、工作包需求、复购可能"
user_action: 滚动并放大表格。
ai_action_or_output: 输出指标层级表。
result_or_change: 把播放 / 点赞 / 收藏 / 评论 / 私信 / 客资拆成不同证明层。
evidence_strength: strong
can_prove: 有清楚的指标分层结果，可作为中段强证据。
cannot_prove: 表格不是平台真实数据；只是目标判断框架。
writing_use: proof_visual + card
risk_or_unclear_point: 表格内容多，若用于视频需要局部放大或截取重点，不适合一次塞满。
```

#### segment_v2_04

```text
start_time: 00:46
end_time: 01:04
visual_summary: 展示“有效客资 0-5 分表”，把无效私信、泛泛好奇、弱需求、明确问题、明确场景与结果请求、明确预算 / 时间 / 决策意愿拆开。
visible_page_or_app: ChatGPT 表格
visible_text:
  - "有效客资 0-5 分表"
  - "0分：无效私信"
  - "1分：泛泛好奇"
  - "2分：弱需求"
  - "3分：明确问题"
  - "4分：明确场景 + 结果请求"
  - "5分：明确场景 + 预算 / 时间 / 决策意愿"
user_action: 滚动和局部放大。
ai_action_or_output: 输出客资评分框架。
result_or_change: 把“私信”从总数拆成质量评分。
evidence_strength: strong
can_prove: 可证明素材里有“客资不等于所有私信”的具体分层。
cannot_prove: 不能证明当前账号已经有 3-5 分客资。
writing_use: proof_visual + card + subtitle
risk_or_unclear_point: 可写“它开始区分私信质量”，不能写“已经验证有效客资”。
```

#### segment_v2_05

```text
start_time: 01:04
end_time: 01:24
visual_summary: 展示目标状态阶梯：content_discovery、content_validation、demand_signal_validation、lead_quality_validation、offer_validation、scale_or_reposition。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "content_discovery（内容探索）"
  - "content_validation（内容验证）"
  - "demand_signal_validation（需求信号验证）"
  - "lead_quality_validation（客资质量验证）"
  - "offer_validation（产品 / 服务验证）"
  - "scale_or_reposition（放大或重判）"
user_action: 继续滚动。
ai_action_or_output: 输出阶段验证路径。
result_or_change: 从指标表继续细化到阶段判断路径。
evidence_strength: strong
can_prove: 有“阶段化判断”结果。
cannot_prove: 不能把当前项目状态写成已进入 `content_validation` 或更高阶段。
writing_use: subtitle + card + narration
risk_or_unclear_point: `content_validation` 在画面里只是阶段名，不是本轮状态推进。
```

#### segment_v2_06

```text
start_time: 01:24
end_time: 01:44
visual_summary: 展示 0-30 天目标与默认保守数字，包含基础播放门槛、较好播放、小爆观察、收藏率、有效评论、有效私信等。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "0-30 天目标"
  - "找到能引发真实反馈的选题"
  - "单条基础播放门槛：1000-3000"
  - "较好播放：3000-8000"
  - "小爆观察：8000+"
  - "收藏率参考：>1% 可观察，>2% 值得复盘"
  - "有效评论：每条 ≥3 条可观察"
user_action: 滚动查看。
ai_action_or_output: 输出阶段假设和阈值。
result_or_change: 目标机制开始落到阶段数字，但画面也强调数字是保守假设。
evidence_strength: medium
can_prove: 可以证明素材里有阶段阈值候选。
cannot_prove: 不能证明这些阈值是行业定论或已由真实样本验证。
writing_use: card + proof_visual
risk_or_unclear_point: 文案必须写“候选 / 阶段假设”，不能写“标准答案”。
```

#### segment_v2_07

```text
start_time: 01:44
end_time: 01:59
visual_summary: 展示 31-90 / 90-180 天目标、失败后重判方式、成功后放大方式，并露出 `video_goal_card` 模板开头。
visible_page_or_app: ChatGPT Markdown 输出
visible_text:
  - "31-90 天目标"
  - "90-180 天目标"
  - "如果有客资无成交：重判承接方式和服务边界"
  - "如果需求分散：缩小目标用户"
  - "video_goal_card"
  - "video_id / title / target_user / funnel_stage..."
user_action: 滚动到尾部，视频在模板刚开始处结束。
ai_action_or_output: 输出后续阶段和目标卡模板开头。
result_or_change: 结果进一步接近可执行卡片，但没有完整录完。
evidence_strength: medium
can_prove: 可证明 AI 输出到了目标卡模板入口。
cannot_prove: 不能证明完整 `video_goal_card` 模板已可见；不能证明发布后复盘卡完整展示。
writing_use: background_only + subtitle
risk_or_unclear_point: 若后续写稿要讲“目标卡模板”，必须说明素材只录到模板开头，完整字段需要补录或另找文字源。
```

## 6. 两个视频之间的关系

```text
sequence:
  video_1: 从原始模糊目标 -> 第一版项目目标 prompt -> 用户指出不够 -> 第二版目标驱动数据飞轮 prompt。
  video_2: 承接第二版 prompt 的结果输出 -> 北极星目标、四圈飞轮、指标分层、有效客资评分、阶段目标、goal card 模板入口。
dependency:
  video_2 依赖 video_1 的第二版 prompt 背景；单独看 video_2 也能理解结果，但缺少“为什么要重写 prompt”的前因。
```

## 7. 素材叙事功能图

```text
material_function_map:
  video_1:
    possible_role:
      - raw_problem_input
      - ordinary_ai_bad_output
      - structured_prompt_process
      - before_after_comparison
      - project_process_evidence
    reason: 有原始糊话输入、有第一版 prompt、有用户指出第一版不对、有第二版 prompt 的生成过程。
  video_2:
    possible_role:
      - improved_result
      - structured_prompt_process
      - project_process_evidence
      - before_after_comparison
    reason: 主要展示第二版 prompt 产出的结构化结果，包括目标、指标、客资、阶段与模板入口。
  combined_storyline:
    possible_structure: "一句糊话问目标 -> AI 先给 KPI 式结构 -> 用户追问目标驱动和数据飞轮 -> AI 输出可复盘、可评分、可分阶段的机制候选。"
    missing_link: 缺真实平台后台数据页面、缺最终落库画面、缺完整目标卡模板尾部、缺使用这个机制后产生的下一条视频结果。
```

## 8. 四段核心素材检查

```text
four_core_material_check:
  raw_problem_input:
    exists: true
    evidence: video_1 00:00-00:08，用户原始输入要求给项目目标，包含客资、点赞、播放，表达较泛。
    timecode: video_1 00:00-00:08
  ordinary_or_bad_output:
    exists: partial
    evidence: video_1 00:22-00:44，第一版 prompt 已结构化，但用户指出“这个 prompt 有问题”；AI 随后承认上一版更像定 KPI。
    timecode: video_1 00:22-00:44
  structured_process:
    exists: true
    evidence: video_1 00:44-01:42，第二版 prompt 从目标驱动、数据反馈、单变量、指标体系、数据飞轮记忆展开。
    timecode: video_1 00:44-01:42
  before_after_result_diff:
    exists: true
    evidence: video_2 00:00-01:59 展示改后结果：北极星目标、四圈飞轮、指标分层、有效客资评分、阶段目标和 goal card 入口。
    timecode: video_2 00:00-01:59
  missing_or_weak_parts:
    - 缺真实发布后台数据和 V003 实际复盘画面。
    - 缺“使用这个目标机制后，下一期内容真的怎么变”的实际执行结果。
    - video_2 尾部的 `video_goal_card` 模板没有完整录完。
    - 两个视频均无音轨，不能直接做同期声证明。
  recommended_reshoot_if_any:
    - 补录完整 `video_goal_card` / `post_publish_review_card` 模板尾部。
    - 如果要讲“数据驱动下一条”，补录一个真实 V003 数据锚点或平台后台指标画面，但当前数据不完整时只能标 `partial_data_recorded`。
    - 补录最终把这份结果保存 / 回填到项目文件前的确认画面，若后续 ChatGPT 判断需要落库证据。
```

## 9. 选题支持判断

```text
topic_support_check:
  strongest_supported_topic:
    title_draft: "为什么你问 AI 要目标，它只会给你 KPI；真正有用的是数据飞轮"
    reason: 两个视频有完整证据链：糊目标输入 -> 第一版不够 -> 追问数据飞轮 -> 输出指标分层和客资评分。
    supporting_timecodes:
      - video_1 00:00-00:08
      - video_1 00:36-00:44
      - video_1 00:44-01:22
      - video_2 00:00-01:04
    unsupported_claims_to_avoid:
      - 不能说数据飞轮已跑通。
      - 不能说项目已经验证出高质量客资。
      - 不能说 V003 数据已经支持下一条正式改稿。
  backup_topic_1:
    title_draft: "别把播放、点赞、私信混成一个目标：AI 项目要先分层"
    reason: video_2 的指标分层表和有效客资 0-5 分表很强。
    supporting_timecodes:
      - video_2 00:22-01:04
  backup_topic_2:
    title_draft: "一条好 prompt，不是让 AI 给答案，而是让它帮你设计判断系统"
    reason: video_1 展示 prompt 从泛问法迭代到机制设计，video_2 展示机制化结果。
    supporting_timecodes:
      - video_1 00:00-01:42
      - video_2 00:00-01:24
  not_suitable_topics:
    - "AI 自动赚钱"：素材不支持，也与项目边界冲突。
    - "用数据证明第二期选题成功"：没有真实发布数据。
    - "V003 已经复盘完成"：当前锚点仍 `partial_data_recorded`。
    - "完整目标卡模板演示"：video_2 只录到模板开头。
```

## 10. 给 ChatGPT 的写稿供料包

```text
chatgpt_material_supply_pack:
  material_summary:
    这组素材不是成片执行素材，而是一组“ChatGPT / Pro 如何把模糊项目目标请求，拆成目标驱动数据飞轮机制”的屏幕录制。video_1 负责过程：原始糊话、第一版 prompt、用户指出不够、第二版数据飞轮 prompt；video_2 负责结果：北极星目标、四圈飞轮、指标分层、有效客资评分、阶段目标和 goal card 模板入口。
  strongest_evidence:
    video_1 00:36-00:44 用户明确说第一版 prompt 有问题，想要目标驱动和复盘后加速数据飞轮；video_2 00:22-01:04 显示指标分层和有效客资评分表。
  strongest_before_after_gap:
    before: 原始输入只说项目缺目标，想要客资 / 点赞 / 播放等目标。
    after: AI 输出变成“北极星目标 + 四圈飞轮 + 指标分层 + 客资评分 + 阶段目标 + goal card”的判断系统。
  best_opening_candidate:
    素材支持“你问 AI 要播放目标，它会给 KPI；但真正有用的是让它帮你判断项目该被什么目标驱动”。适合 `screen_first_opening` 或直接问题标题卡，不适合说成最终运营复盘。
  best_middle_evidence:
    video_2 00:22-00:46 指标分层表；video_2 00:46-01:04 有效客资 0-5 分表；video_1 00:36-00:44 用户二次追问。
  best_result_diff:
    第一版停在“阶段目标 / 指标树 / 客资定义”的列表；第二版把“每条视频发布后按数据选择下一期只改一个变量”写进 prompt，并在 video_2 生成目标飞轮结果。
  possible_summary_card_content:
    - 播放是入口，不是目标。
    - 点赞 / 收藏是认可，不等于需求。
    - 私信要评分，不是每条都算客资。
    - 每条视频只改一个主变量，才能让复盘有用。
  possible_prompt_tail_card_material:
    可以引用素材中的 prompt 方向："帮我为《视频工厂》设计一套目标驱动的数据飞轮机制；每期视频发布后，根据播放、留存、收藏、评论、私信、客资等反馈，判断下一期只改哪个变量。"
  human_feel_notes:
    这组素材有真实“卡住 -> 改问法 -> 结果变具体”的过程，适合讲“不是不会用 AI，是你没让它进入判断系统”。但画面是长文档滚动，后续剪辑需要大量局部放大、字幕和少量卡片辅助。
  platform_risk_notes:
    避免写“AI 自动赚钱”“保证客资”“数据飞轮已跑通”。建议写“判断系统”“阶段假设”“候选机制”，不要写成商业成功。
  must_not_write:
    - 不得写 V003 已经完成 72h / 7d 复盘。
    - 不得写当前已有有效客资或成交。
    - 不得写视频里出现了真实平台后台数据。
    - 不得写 goal card 完整字段已经录全。
    - 不得写 content_validation / send_ready / publish_status_success 已推进。
    - 不得写 DeepSeek 参与了本轮素材判断。
  missing_material:
    - 完整 goal card / post-publish review card 尾部。
    - 真实平台数据画面。
    - 使用该机制后生成下一条内容的实际结果。
    - 口播音频或可直接用的叙述音轨。
  recommended_next_decision_for_chatgpt:
    先判断这组素材是否适合做“AI 目标判断 / 数据飞轮 / 有效客资分层”方向，而不是直接进入正式稿；若选这个方向，建议围绕“从 KPI 到判断系统”的前后差来写，且保守标注为素材候选，不写成运营结论。
```

## 11. forbidden_status_check（禁止状态检查）与禁止误写清单

1. 不得把素材存在写成素材适配完成。
2. 不得把 prompt 结果写成项目正式事实已经落库。
3. 不得把 `content_validation` 写成已通过。
4. 不得把 `send_ready` 写成 true。
5. 不得把 `publish_status_success` 写成已推进。
6. 不得把 `voice_validation`、`final_voice_validated`、`visual_master_locked` 推进。
7. 不得说 DeepSeek 参与了本轮判断。
8. 不得说平台数据、客资、成交、真实后台验证已在素材里出现。
9. 不得说两个视频有音频。
10. 不得把 video_2 尾部未录完的模板写成“完整模板已展示”。

## 12. 技术验证

```text
technical_validation:
  material_directory_found: true
  exact_two_videos_found: true
  metadata_read: true
  decodable: true
  frame_extraction_done: true
  local_ocr_done: true
  timecoded_report_done: true
  report_file_created: true
  source_material_unchanged: true
```

## 13. 内容验证

```text
content_validation:
  status: not_advanced
  reason: 本轮只做素材审计和 ChatGPT 写稿供料，不做最终文案、内容验证、成片判断或发布判断。
```

## 14. 下一个目标

把本轮素材审计报告贴回 ChatGPT，由 ChatGPT 判断这 2 个视频素材是否足够支撑下一条候选内容、应走哪种开头路线、是否需要补录，以及是否可以进入正式文案准备。
