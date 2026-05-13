# material_03 Codex 工作流深审报告

生成时间：2026-05-14  
素材对象：`/Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 03-06-26.mp4`  
用途：给 ChatGPT 修改《今天就说一个事，AI 到底赚不赚钱》文案提供素材证据边界。  
状态：`completed（已完成）`

---

## 1. scope（本轮范围）

本轮只解析指定单段素材：

```text
material_id: material_03_single_deep_audit
file_name: 内建视网膜显示器 2026-05-14 03-06-26.mp4
file_path: /Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 03-06-26.mp4
```

本轮不解析另外两段素材，不写最终文案，不生成视频，不剪辑，不修改原始素材，不调用外部 API，不读取 `.env` / `.env.swp` / secret，不推进任何动态状态。

本轮生成的审看辅助文件：

```text
codex_log/20260514_material_03深审关键帧_material_03_deep_audit_keyframes/material_03_contact_sheet_3s.jpg
codex_log/20260514_material_03深审关键帧_material_03_deep_audit_keyframes/frame_001.jpg ... frame_011.jpg
codex_log/20260514_material_03深审关键帧_material_03_deep_audit_keyframes/crop_001_demo_order.jpg
codex_log/20260514_material_03深审关键帧_material_03_deep_audit_keyframes/crop_006_focusee_order.jpg
codex_log/20260514_material_03深审关键帧_material_03_deep_audit_keyframes/crop_009_focusee_status.jpg
```

---

## 2. route_decision（路由判断）

```text
route_decision:
  project_route: video_factory
  task_type:
    - material_audit_needed
    - video_sample_or_assembly_read_only
    - copywriting_bridge
  responsibility_layer:
    - project_judgment_layer
    - validation_layer
    - sync_layer
  large_task_gate:
    triggered: false
    reason: 本轮只解析单一指定素材，不做多素材总审计
    lane_recommendation: audit_lane
    parallel_recommendation: serial_only
  completion_relay_gate:
    triggered: true
    reason: 不能只读取素材参数，必须输出给 ChatGPT 改文案用的证据判断
  execution_permission: allowed_after_material_found_and_readable
```

read_status:

```text
AGENTS.md: read_ok
codex_source/00_codex_readme.md: read_ok
codex_source/01_execution_rules.md: read_ok
codex_log/latest.md: read_ok
GPT数据源/05_文案路由规则.md: read_ok
GPT数据源/11_项目状态动作总控器_机制推理层.md: read_ok
codex_source/19_project_state_action_router.md: read_ok
codex_log/20260514_AI到底赚不赚钱三段素材细节报告_ai_money_three_materials_detail_report.md: read_ok
指定素材: read_ok, validation_status=passed
~/.codex/skills/video-metadata-probe/SKILL.md: read_ok
```

---

## 3. state_action_router（项目状态动作总控器）

```text
state_action_router:
  input_signal: 用户要求专门解析 material_03，确认它是否能证明 Codex 同时执行两个任务，以及如何支撑 AI 赚钱文案
  current_project_state:
    - material_audit_needed
    - copy_production_ready_after_material_report
  fact_source_arbitration:
    primary_source: 指定素材真实画面 + 上一轮三段素材报告
    secondary_sources:
      - 当前文案路由规则
      - 当前状态动作总控器
  conflict_detected:
    - 用户想表达“同时推进两个任务”，但上一轮报告没有明确证明“Codex 并发执行两个任务”
  conflict_resolution:
    - 只按画面直接证据判断能说到什么程度；能证明多任务线就写多任务线，不能证明并发就不能写并发
  inferred_state:
    - single_material_deep_audit_needed
    - final_copy_claim_needs_evidence_boundary
  confidence: high_after_frame_review
  trigger_mechanism:
    - material_audit
    - copy_support_check
    - content_route_card V2
    - Completion Relay Gate
  selected_action:
    - 对指定素材做更细时间码解析
    - 判断能支撑哪些文案句子
    - 输出可写 / 不可写 / 需降级表达
  forbidden_action:
    - 不写最终文案
    - 不生成视频
    - 不修改媒体
    - 不推进动态状态
  blocked_if:
    - 素材不存在
    - 素材无法打开
    - 画面内容无法判断
  current_blocker: none
```

---

## 4. material_inventory（素材基础参数）

```text
file_path: /Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 03-06-26.mp4
modified_time: 2026-05-14 03:07:57
file_size_bytes: 38238203
duration: 33.133333s
width: 2498
height: 1874
aspect_ratio: 1.3330, near 4:3
fps: 30.000
video_codec: h264
has_audio: false
audio_codec: none
audio_channels: 0
can_open: true
decodable: true
ffprobe_available: true
ffmpeg_available: true
metadata_validation: passed
technical_validation: passed
content_validation: not_evaluated_as_project_status
```

technical note:

- `video-metadata-probe（视频元数据检查）` 证明本文件存在、可读取 metadata、可解码。
- `audio_present=false（没有音轨）`，所以本段不能证明任何 TTS 配音结果。
- 技术验证通过不等于内容验证通过。

basic_quality:

```text
是否模糊: partially, FocuSee/录屏运动中局部文字有运动模糊，但关键大字和主要任务标题可读
是否黑屏: false, blackdetect 未发现明显黑屏段
是否卡顿: not_observed_in_keyframes, 但未做逐帧播放流畅性评分
是否遮挡: partially, 鼠标和窗口运动会遮挡局部文字
是否有明显水印: false, 未见明显平台水印
```

---

## 5. detailed_timecode_analysis（更细时间码分析）

### 00:00-00:03

```text
visible_content: ChatGPT 网页界面，左侧项目列表可见，当前对话标题为“生成厕所清洁剂图文视频demo”。
user_action: 画面停留在对话内容区，鼠标位于执行单正文附近。
page_or_scene: ChatGPT 项目 / Codex 执行单。
readable_text:
  - “# Codex 执行单：为‘厕所清洁剂’生成 3 图拼接 + TTS 的图文视频 demo”
  - “## Goal（目标）”
  - “生成一个可复制的图文拼接视频 demo”
task_context: 直播工厂 / 商品 demo 相关执行单，不是当前视频工厂素材审计。
evidence_value: 能证明 ChatGPT/Codex 里存在明确执行单、目标和项目化任务，不是普通聊天。
copywriting_use: 可支撑“我不是只开一个 AI 对话框闲聊，而是在用执行单让 AI 做项目任务”。
claim_boundary: 不能证明 demo 已生成成功；不能证明 Codex 正在并发执行另一个任务。
```

### 00:03-00:06

```text
visible_content: 同一“厕所清洁剂图文视频 demo”执行单继续显示。
user_action: 页面基本停留，开始出现处理进度区域。
page_or_scene: ChatGPT 项目 / Codex 执行单处理中。
readable_text:
  - “3 张静态图片 -> 拼接成短视频 -> 接入 TTS 配音 -> 合成 mp4 -> 生成验收记录”
  - “本轮不是只写脚本说明，不是只生成 Markdown 测试包，不是只输出内容文案”
  - “本轮必须真实产出”
task_context: 任务要求从素材到视频再到验收记录的执行闭环。
evidence_value: 能证明执行单有“目标、产物、验收”意识。
copywriting_use: 可写“AI 被放进项目流程里，目标、产物、验收都写清楚”。
claim_boundary: 不能证明素材、TTS、mp4 已全部产出；画面只显示任务要求和处理中状态。
```

### 00:06-00:09

```text
visible_content: 执行单下方出现处理状态，文本提到先做仓库确认。
user_action: 等待 ChatGPT/Codex 继续处理。
page_or_scene: Codex 执行过程 / 项目文件检查前置。
readable_text:
  - “已处理 9s”
  - “我会先做两件底层确认：确认当前目录确实落在指定 Git 仓库里，同时快速回读项目记忆和本地约束，避免把旧‘直播前台’分支误当当前主线”
task_context: Codex 在开始执行前先确认 repo / 项目记忆 / 本地约束。
evidence_value: 能证明 Codex 工作流有项目边界意识和上下文防串线机制。
copywriting_use: 可写“它会先核对项目边界，避免把不同项目搞混”。
claim_boundary: 不能证明两个任务并发，只证明单个执行单内部在做前置校验。
```

### 00:09-00:12

```text
visible_content: 同一对话继续显示“正在搜索 MEMORY.md 文件夹中的文件”。
user_action: 无明显新输入，画面处于等待执行状态。
page_or_scene: Codex 执行过程 / memory 与规则读取。
readable_text:
  - “正在搜索 MEMORY.md 文件夹中的文件”
task_context: Codex 正在检索项目记忆 / 约束文件。
evidence_value: 能证明执行层不是单纯生成一句回答，而是在检索上下文后再执行。
copywriting_use: 可支撑“AI 帮我整理项目上下文和约束”。
claim_boundary: 不能写成“AI 已完成视频生成”，也不能写成“两个任务同时在跑”。
```

### 00:12-00:15

```text
visible_content: 左侧项目列表可见多个项目/任务；当前仍在“生成厕所清洁剂图文视频demo”。画面出现 FocuSee 式放大/倾斜运动。
user_action: 鼠标靠近左侧项目列表，准备切换。
page_or_scene: ChatGPT 项目列表 + 当前执行单。
readable_text:
  - 左侧可见“直播工厂”“视频工厂”
  - 直播工厂下可见“生成厕所清洁剂图文视频demo”“迁移90分内容质量标准”“补齐单商品执行闭环”等
  - 视频工厂下可见“修正 FocuSee 中段剪辑口径”“落地三大推理函数”“落地参考到执行契约”等
task_context: 多个项目与任务线在 ChatGPT 项目空间里存在。
evidence_value: 能证明“多任务线 / 多项目记录可见”。
copywriting_use: 可写“我把不同项目拆成不同任务线管理”。
claim_boundary: 只能证明多个项目/任务条目存在；不能证明它们此刻由 Codex 并发执行。
```

### 00:15-00:18

```text
visible_content: 画面切换到“修正 FocuSee 中段剪辑口径”对话，属于“视频工厂”项目。
user_action: 点击/切换到视频工厂中的 FocuSee 相关任务。
page_or_scene: ChatGPT 项目 / 视频工厂 / FocuSee 中段剪辑口径。
readable_text:
  - “修正 FocuSee 中段剪辑口径”
  - “保留 4:3 素材原始画面信息”
  - “不再投 9:16 竖屏幕布预制 / 填充或套旧模板”
  - “不默认二次放大 / crop / 重新运镜”
  - “不推进内容验证状态”
  - “不把技术装配成功写成内容过线”
task_context: 视频工厂中关于 FocuSee 屏录素材和剪辑口径的规则修正。
evidence_value: 强证明视频项目有素材比例、剪辑策略、内容状态边界。
copywriting_use: 可支撑“Codex / ChatGPT 帮我把视频项目里的素材规则和验收边界写清楚”。
claim_boundary: 不能证明电商选品线；不能证明并发执行。
```

### 00:18-00:21

```text
visible_content: 同一视频工厂对话继续，出现“已处理 1m30s”和执行说明。
user_action: 停留查看执行说明。
page_or_scene: Codex 执行说明 / 技术装配修正。
readable_text:
  - “我会按这轮当成‘技术装配修正’来跑”
  - “先锁当前目标和 4:3 素材路径”
  - “再决定能不能动装配链路”
  - “这里会用 video-metadata-probe 做素材宽高核验”
  - “用 executing-plans 接你的执行单收口”
task_context: Codex 正在说明本轮执行策略，涉及素材路径、比例核验、执行单收口。
evidence_value: 强证明 Codex 本地执行系统存在，并且会按素材路径、4:3、metadata、执行计划做检查。
copywriting_use: 可写“我把 Codex 接进本地项目，让它帮我查路径、查比例、查验收条件”。
claim_boundary: 不能写成“已经完成所有验证”；画面显示的是执行过程和计划，不是最终验收结果。
```

### 00:21-00:24

```text
visible_content: 同一对话继续显示只读锁定说明。
user_action: 无明显新输入。
page_or_scene: Codex 执行说明 / 只读锁定。
readable_text:
  - “我先做只读锁定”
  - “当前目标、复审包、装配脚本和素材路径都要从仓库里实证找到”
  - “如果目标或素材路径断掉，就按你的阻断条件停，不硬猜”
task_context: Codex 在执行前强调从仓库实证确认，而非凭口径猜测。
evidence_value: 能证明 AI/Codex 在项目中承担“路径确认、证据读取、阻断条件判断”角色。
copywriting_use: 可支撑“AI 帮我检查项目执行，而不是只陪我聊天”。
claim_boundary: 不能证明视频已经剪完或状态通过；只能证明执行前检查机制。
```

### 00:24-00:27

```text
visible_content: 文本继续显示对象锁定结果。
user_action: 页面停留。
page_or_scene: Codex 执行说明 / 对象与素材验证。
readable_text:
  - “当前对象已经锁到 v3.1 复审包”
  - “现有成片还是 720x1280 竖屏”
  - “下一步我在装配链路和时间线里找原素材路径”
  - “因为你要求必须验证‘素材本身 4:3’，不能只信口径”
task_context: 视频工厂 v3.1 复审包、竖屏成片、原素材路径、4:3 素材验证。
evidence_value: 强证明 Codex 会区分成片比例和素材原始比例，并会做路径/时间线核验。
copywriting_use: 可支撑“我让 AI 帮我检查视频项目里的素材、比例和验收问题”。
claim_boundary: 不能证明“内容验证 passed”；也不能证明“AI 自动把视频做好了”。
```

### 00:27-00:30

```text
visible_content: 画面仍在视频工厂 FocuSee 任务，底部显示“正在自动压缩上下文”。
user_action: 等待执行。
page_or_scene: ChatGPT/Codex 执行中状态。
readable_text:
  - “正在自动压缩上下文”
  - 底部可见“本地模式”“main”
task_context: Codex / ChatGPT 项目执行上下文处理。
evidence_value: 能证明存在本地模式和主分支上下文，但画面没有终端命令完整输出。
copywriting_use: 可作为“本地项目工作流”辅助镜头。
claim_boundary: 不能写成远端已提交、已发布或已通过。
```

### 00:30-00:33

```text
visible_content: 同一视频工厂任务停留在 FocuSee 规则与 4:3 素材验证说明。
user_action: 无明显新操作。
page_or_scene: 视频工厂执行记录结束段。
readable_text:
  - “video-metadata-probe”
  - “executing-plans”
  - “v3.1 复审包”
  - “720x1280 竖屏”
  - “素材本身 4:3”
task_context: 素材验证和执行计划仍是主内容。
evidence_value: 最适合用作“Codex 本地执行系统 / 项目验收机制”的证据镜头。
copywriting_use: 建议放在文案中段或后段，用于承接“AI 的价值是把执行、检查、验收接进系统”。
claim_boundary: 不能用来证明电商选品、收入、成本、同时并发执行。
```

---

## 6. parallel_or_multi_task_claim_check（并发 / 多任务判断）

```text
parallel_or_multi_task_claim_check:
  can_claim_codex_parallel_execution: false
  can_claim_multiple_task_lines_visible: true
  can_claim_user_is_advancing_video_and_ecommerce_lines: unclear
  can_claim_codex_local_execution_system_exists: true
  evidence:
    - 00:00-00:15 可见“直播工厂”下的“生成厕所清洁剂图文视频demo”执行单。
    - 00:12-00:15 左侧可见“直播工厂”和“视频工厂”两个项目，以及多个任务条目。
    - 00:15-00:33 切换到“视频工厂”下“修正 FocuSee 中段剪辑口径”任务。
    - 00:18-00:33 可见 “video-metadata-probe”“executing-plans”“4:3 素材路径”“v3.1 复审包”等 Codex 执行检查内容。
  cannot_claim:
    - 不能写“Codex 正在并发执行两个任务”。
    - 不能写“Codex 同屏同时跑两个任务”。
    - 不能只凭 material_03 写“视频项目和电商选品同时推进”；material_03 未显示电商选品/成本倒推画面。
    - 不能写“厕所清洁剂 demo 已生成成功”或“FocuSee 修正已完成发布”。
  safest_copywriting_phrase: “我现在不是只开一个 AI 对话框，而是把不同项目拆成任务线：有的让它生成执行单，有的让它查素材路径、比例和验收条件；至于电商选品这条线，需要结合前一段成本倒推素材一起看。”
```

判断结论：

- `已确认`：material_03 能证明 ChatGPT/Codex 项目里存在多个任务线和多个项目记录。
- `已确认`：material_03 能证明视频工厂里存在 Codex 本地执行检查流程，包括路径、素材比例、metadata、执行计划和验收边界。
- `部分成立`：可以说“我同时在推进不同任务线 / 多项目执行系统”，但这里的“同时”应理解为同一工作系统内多任务线并行管理，不是同一秒钟并发执行。
- `不成立`：不能说“Codex 同时执行两个任务”。
- `待验证`：material_03 单独不能证明“电商选品线”；需要结合 material_01 的成本倒推 / 选品研究画面。

---

## 7. copy_support_check（文案支撑等级）

### claim 1｜“我不是只用 AI 聊天。”

```text
support_status: directly_supported
evidence: 执行单包含目标、产物、验收记录；FocuSee 任务包含路径、比例、metadata、执行计划。
safe_rewrite: “我不是只拿 AI 聊天，我是把它接进项目流程里，让它按目标、路径和验收条件做事。”
```

### claim 2｜“我把 Codex 接进了本地项目。”

```text
support_status: directly_supported
evidence: 画面出现“本地模式”“main”“从仓库里实证找到”“video-metadata-probe”“executing-plans”等内容。
safe_rewrite: “我把 Codex 放进本地项目里，让它先查仓库、查路径、查素材参数，再决定能不能继续。”
```

### claim 3｜“Codex 帮我做视频项目的路径、素材、比例和验收。”

```text
support_status: directly_supported
evidence: 00:18-00:33 明确出现“4:3 素材路径”“素材宽高核验”“v3.1 复审包”“720x1280 竖屏”“不能只信口径”。
safe_rewrite: “视频项目里，它会帮我查素材路径、查 4:3 比例、核对复审包和验收边界。”
```

### claim 4｜“我同时在推进视频项目和电商选品。”

```text
support_status: unclear
evidence: material_03 显示视频工厂和直播工厂/商品 demo 任务，不显示电商选品/成本倒推画面；电商选品证据在上一轮 material_01 中。
safe_rewrite: “这一段能证明我在项目系统里管理不同任务线；电商选品那条线要结合前面成本倒推那段素材一起看。”
```

### claim 5｜“Codex 同时执行两个任务。”

```text
support_status: unsupported
evidence: 画面是先看一个执行单，再切换到另一个项目任务；没有同屏或连续明确显示两个 Codex 任务同时运行。
safe_rewrite: “我把任务拆成不同项目线管理，但这段画面不能写成 Codex 正在并发执行两个任务。”
```

### claim 6｜“AI 帮我写文案、整理素材、复盘数据。”

```text
support_status: partially_supported
evidence: material_03 能证明整理素材路径、检查比例、执行单和验收；没有直接显示写最终文案或复盘平台数据。
safe_rewrite: “它能帮我整理素材路径、执行单和验收边界；文案和数据复盘要结合其他素材一起说。”
```

### claim 7｜“AI 是一个执行系统，不只是聊天工具。”

```text
support_status: directly_supported
evidence: 执行单、项目边界、仓库确认、metadata 检查、4:3 素材验证、执行计划收口均可见。
safe_rewrite: “对我来说，AI 不只是聊天工具，它已经变成项目里的执行和检查系统。”
```

### claim 8｜“AI 能把项目拆成多个执行任务。”

```text
support_status: partially_supported
evidence: 左侧可见多个项目和任务条目，当前画面有不同执行单；但拆分过程本身没有完整展示。
safe_rewrite: “我会把项目拆成一条条任务线，再让 AI 分别处理目标、素材、路径和验收。”
```

---

## 8. safe_copywriting_expression（给 ChatGPT 的安全表达建议）

```text
strong_version_if_directly_supported:
  - “我不是只拿 AI 聊天，我把 Codex 接进本地项目，让它查仓库、查素材路径、查 4:3 比例，还要按验收条件收口。”
  - “这就是我说的执行系统：不是给我一句漂亮答案，而是帮我把项目里的目标、素材、路径和验收拆清楚。”

medium_version_if_partially_supported:
  - “我现在不是只做一个 AI 对话，而是在不同项目里推进不同任务线：有视频项目、有商品 demo、有素材验证和执行单收口。”
  - “电商选品和成本倒推那条线，要结合前面那段成本表素材一起看；这一段主要证明 Codex 的本地执行流程。”

safe_version_if_unclear:
  - “这段画面只能证明多个任务线在项目里被管理，不能证明 Codex 正在并发跑两个任务。”
  - “如果要说‘同时推进视频和电商’，最好写成‘我把不同任务线放进同一套 AI 工作流里推进’，不要写成‘Codex 同时执行两个任务’。”
```

lines_to_avoid_or_downgrade:

```text
avoid:
  - “Codex 同时执行两个任务。”
  - “画面里可以看到视频项目和电商选品同时在跑。”
  - “AI 已经把厕所清洁剂 demo 生成完了。”
  - “AI 已经验证内容通过 / 可以发布。”
downgrade_to:
  - “画面里能看到多个任务线和项目记录。”
  - “这一段主要证明 Codex 被接进本地视频项目，负责路径、素材比例和验收检查。”
  - “电商选品需要结合另一段成本倒推素材作为证据。”
```

---

## 9. content_route_card_v2_update_from_material_03（内容路由卡 V2 更新草案）

```text
content_route_card_v2_update_from_material_03:
  evidence_plan:
    core_evidence:
      - Codex 执行单：厕所清洁剂 3 图拼接 + TTS 图文视频 demo
      - 视频工厂 FocuSee 任务：4:3 素材路径、video-metadata-probe、executing-plans、v3.1 复审包
    evidence_type:
      - workflow_screen_recording
      - local_execution_system_evidence
      - project_boundary_and_validation_evidence
    evidence_missing_or_unclear:
      - 没有同屏证明 Codex 并发执行两个任务
      - 没有 material_03 内部的电商选品/成本倒推证据
      - 没有最终 demo 产物或发布结果
  middle_carrier_decision:
    material_03_role: Codex 本地执行系统证据，不作为成本/收入证明
    best_timecodes:
      - 00:00-00:06: Codex 执行单、目标、产物、验收要求
      - 00:12-00:18: 多项目/多任务线可见，切换到视频工厂
      - 00:18-00:33: video-metadata-probe、executing-plans、4:3、v3.1 复审包、素材路径核验
    should_use_for:
      - “不是只聊天，而是项目执行系统”
      - “Codex 帮我查路径、查比例、查验收”
      - “多任务线在项目里被管理”
    should_not_use_for:
      - “Codex 并发执行两个任务”
      - “电商选品与视频项目同屏同时推进”
      - “AI 自动生成结果已成功”
      - “内容验证通过 / 可发布”
  card_placement_decision:
    recommended_card: “不是聊天框，是执行系统”
    reason: 这段画面最强证据是执行单、路径核验、素材比例和验收边界，不是收益或生成结果。
  copy_support_boundary:
    - 这段只负责证明 Codex 工作流和项目执行机制。
    - 电商成本倒推用 material_01 支撑。
    - 粽子 / 婚纱样片展示用 material_02 支撑。
    - 并发执行 claim 必须删除或降级。
```

---

## 10. final_handoff_to_chatgpt（给 ChatGPT 的最终交接）

```text
final_handoff_to_chatgpt:
  material_03_best_use: 用作“ChatGPT / Codex 已经进入项目执行系统”的证据，不用作收益、成本、并发执行或最终成果证明。
  strongest_supported_lines:
    - “我不是只用 AI 聊天，我把 Codex 接进本地项目，让它帮我查仓库、查素材路径、查 4:3 比例和验收条件。”
    - “这就是 AI 真正值钱的地方：它不是自动赚钱按钮，而是把执行、检查和复盘变成一套流程。”
    - “我会把项目拆成不同任务线，让 AI 分别处理目标、素材、路径和验收。”
  lines_to_avoid_or_downgrade:
    - 避免写“Codex 同时执行两个任务”。
    - 避免写“这段画面证明视频项目和电商选品同时在跑”。
    - 避免写“厕所清洁剂 demo 已完成生成”。
    - 避免写“内容验证通过 / 可以发布”。
  recommended_script_insertion_point: 放在中后段。先用 material_02 展示真实素材/样片，再用 material_01 讲成本倒推和选品逻辑，最后用 material_03 收束到“AI 是执行系统，不只是聊天工具”。
  safe_wording_for_multi_task_claim: “这段画面能看到多个项目和任务线在同一套 AI 工作流里被管理，但不能写成 Codex 正在并发执行两个任务。更安全的说法是：我把视频项目、商品 demo、素材验证这些任务拆成不同任务线，让 AI 帮我逐条推进。”
```

---

## 11. forbidden_status_check（禁止动作核验）

```text
parsed_only_target_material: true
parsed_other_two_materials: false
source_media_modified: false
video_generated: false
video_edited: false
audio_replaced: false
external_api_called: false
deepseek_called: false
aliyun_called: false
tts_or_voice_cloning_called: false
image_or_video_generation_called: false
secret_read: false
env_read: false
env_swp_read: false
content_validation_promoted: false
send_ready_promoted: false
publish_status_promoted: false
voice_validation_promoted: false
final_voice_validated_promoted: false
visual_master_locked_promoted: false
```

---

## 12. validation_check（完成前验证）

```text
specified_material_exists: passed
specified_material_can_open: passed
metadata_collected: passed
contact_sheet_or_keyframes_extracted: passed
detailed_timecode_analysis_written: passed
codex_parallel_execution_claim_checked: passed
safe_copywriting_expression_written: passed
final_handoff_to_chatgpt_written: passed
source_media_unchanged: passed
video_generated: false
dynamic_status_promoted: false
```

---

## 13. final_completion_status（本轮完成状态）

```text
status: completed
completed_items:
  - 已专门解析指定素材
  - 已完成 3-5 秒粒度时间码分析
  - 已明确判断：不能说 Codex 同时执行两个任务
  - 已明确判断：可以说多任务线 / 多项目记录可见
  - 已明确判断：可以说 Codex 是本地执行系统的一部分
  - 已输出可写、不可写、需降级表达
  - 已生成 material_03 深审报告
remaining_unclear_points:
  - 电商选品线不能由 material_03 单独证明，需要结合 material_01
  - demo 是否最终生成成功不能由 material_03 单独证明
```

---

## 14. next_target（下一个目标）

让 ChatGPT 基于 material_03 的证据边界，把“同时推进两个任务 / Codex 执行系统”相关文案改成保守可证明表达：保留“多任务线管理”和“本地项目执行检查”，删除或降级“Codex 并发执行两个任务”。
