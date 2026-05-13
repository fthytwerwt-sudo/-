# 20260514｜《AI 到底赚不赚钱》三段素材细节报告

## 0. scope（本轮范围）

- `已确认` 本轮只做用户最新 3 段素材的只读审计、基础参数读取、时间码细节整理、证据映射和给 ChatGPT 的文案桥接。
- `已确认` 不写最终文案，不生成视频，不剪辑，不修改原始素材，不调用 DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `已确认` 本轮没有推进 `content_validation`、`send_ready`、`publish_status`、`voice_validation`、`final_voice_validated`、`visual_master_locked`。
- `已确认` 素材目录命中：`/Users/fan/Documents/视频工厂/素材录制`
- `已确认` 用户口头路径 `文稿-视频工厂-素材录制` 不是当前精确目录名；当前正式工作区内实际命中目录为 `素材录制`。

## 1. route_decision（路由判断）

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
    triggered: true
    reason: 本轮涉及 3 段素材查找、读取、时间码分析、证据判断和文案桥接报告
    lane_recommendation: audit_lane
    lane_reason: 素材路径来自口头描述，需先本地查找与审计
    lane_invalid_if: 找不到唯一 3 段素材、素材不可读、证据点无法判断
    parallel_recommendation: serial_only
    parallel_reason: 最终判断和报告写入只有一个 owner，避免时间码与证据结论冲突
    write_owner: Codex integrator
    read_only_lanes:
      - 本地素材目录查找
      - ffprobe / ffmpeg 技术读取
      - 关键帧 / 画面内容只读分析
    integration_owner: Codex integrator
  completion_relay_gate:
    triggered: true
    reason: 不能只找到文件就结束，必须输出完整素材细节报告
  execution_permission: allowed_after_must_read_and_material_path_found
```

## 2. state_action_router（项目状态动作总控器）

```text
state_action_router:
  input_signal: 用户提供 3 段最新素材路径线索，要求 Codex 解析素材并交给 ChatGPT 修改文案
  current_project_state:
    - material_audit_needed
    - copy_production_ready_after_material_report
  fact_source_arbitration:
    primary_source: 用户本轮路径线索 + 本地真实文件读取结果
    secondary_sources:
      - GPT数据源/05_文案路由规则.md
      - GPT数据源/11_项目状态动作总控器_机制推理层.md
      - GPT数据源/08_当前正式事实.md
    conflict_detected:
      - 用户口头路径可能不是精确文件系统路径
    conflict_resolution:
      - 以实际找到的本地文件路径、素材参数和画面内容为准
  inferred_state:
    - latest_materials_need_audit
    - final_copy_should_wait_for_material_detail_report
  confidence: high_after_path_found
  trigger_mechanism:
    - material_audit
    - content_route_card V2
    - Completion Relay Gate
  selected_action:
    - 查找 3 段最新素材
    - 读取基础参数
    - 输出时间码细节、证据判断和文案修改建议
  forbidden_action:
    - 不写最终文案
    - 不生成视频
    - 不修改媒体
    - 不推进动态状态
  blocked_if:
    - 找不到素材目录
    - 找不到 3 段素材
    - 素材无法打开
    - 素材内容无法判断
```

## 3. actual_read_files（实际读取文件）

```text
read_status:
  AGENTS.md: read_ok
  codex_source/00_codex_readme.md: read_ok
  codex_source/01_execution_rules.md: read_ok
  codex_log/latest.md: read_ok
  GPT数据源/05_文案路由规则.md: read_ok
  GPT数据源/11_项目状态动作总控器_机制推理层.md: read_ok
  codex_source/19_project_state_action_router.md: read_ok
  GPT数据源/08_当前正式事实.md: read_ok
  codex_source/13_execution_lane_and_parallel_rules.md: read_ok
  project_source/20_codex_multi_agent_routing_note_for_gpt_project.md: read_ok
  ~/.codex/skills/video-metadata-probe/SKILL.md: read_ok
  codex_source/fixtures/mechanism_inference_function_cases.json: read_ok_partial_relevant_lines
```

## 4. material_search_result（素材查找结果）

```text
tried_paths:
  /Users/fan/Documents/视频工厂/素材录制: exists
  /Users/fan/Documents/视频工厂/文稿: missing
  /Users/fan/Documents/视频工厂/文稿-视频工厂-素材录制: missing
  /Users/fan/Documents/视频工厂/文稿/视频工厂/素材录制: missing

matched_material_directory:
  /Users/fan/Documents/视频工厂/素材录制

selection_rule:
  - 当前命中目录内刚好 3 段 mp4
  - 文件修改时间集中在 2026-05-14 02:59-03:07
  - 与用户“里面有 3 段素材”描述一致

analysis_frames:
  - /Users/fan/Documents/视频工厂/codex_log/20260514_AI赚钱素材关键帧_ai_money_material_keyframes/material_01_contact_sheet.jpg
  - /Users/fan/Documents/视频工厂/codex_log/20260514_AI赚钱素材关键帧_ai_money_material_keyframes/material_02_contact_sheet.jpg
  - /Users/fan/Documents/视频工厂/codex_log/20260514_AI赚钱素材关键帧_ai_money_material_keyframes/material_03_contact_sheet.jpg
```

## 5. material_inventory（素材清单）

### material_01

```text
material_id: material_01
file_name: 内建视网膜显示器 2026-05-14 02-45-29.mp4
file_path: /Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 02-45-29.mp4
modified_time: 2026-05-14 02:59:12
file_size_bytes: 93670463
duration: 67.433333s
width: 2180
height: 1634
aspect_ratio: 1.3341, near 4:3
fps: 30.000
video_codec: h264
has_audio: false
can_open: true
decodable: true
metadata_validation: passed
basic_quality:
  - 是否模糊: 局部 FocuSee 运镜时有轻微运动模糊；主要文字在近景段可读
  - 是否黑屏: 未发现黑屏
  - 是否卡顿: 抽帧未见明显卡顿；仅做视觉抽检
  - 是否遮挡: 鼠标指针偶尔覆盖文字；不遮挡核心表格
  - 是否有明显水印: 未见明显平台水印
```

### material_02

```text
material_id: material_02
file_name: 内建视网膜显示器 2026-05-14 02-59-28.mp4
file_path: /Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 02-59-28.mp4
modified_time: 2026-05-14 03:02:54
file_size_bytes: 206936407
duration: 91.800000s
width: 2614
height: 1960
aspect_ratio: 1.3337, near 4:3
fps: 30.000
video_codec: h264
has_audio: false
can_open: true
decodable: true
metadata_validation: passed
basic_quality:
  - 是否模糊: FocuSee 3D 运镜 / 放大移动时边缘有运动模糊；婚纱、粽子预览主体可辨认
  - 是否黑屏: 未发现黑屏
  - 是否卡顿: 抽帧未见明显卡顿；仅做视觉抽检
  - 是否遮挡: Finder / Quick Look 窗口遮住部分 ChatGPT 文案，但不影响素材文件和预览判断
  - 是否有明显水印: 未见明显水印
```

### material_03

```text
material_id: material_03
file_name: 内建视网膜显示器 2026-05-14 03-06-26.mp4
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
can_open: true
decodable: true
metadata_validation: passed
basic_quality:
  - 是否模糊: 中后段运镜放大导致部分文字偏糊；大标题和核心字段可辨认
  - 是否黑屏: 未发现黑屏
  - 是否卡顿: 抽帧未见明显卡顿；仅做视觉抽检
  - 是否遮挡: 鼠标指针和窗口移动会遮挡局部文字
  - 是否有明显水印: 未见明显水印
```

## 6. timecode_detail（时间码细节）

### material_01｜Perplexity / ChatGPT 研究与选品成本逻辑

```text
00:00-00:08:
  visible_content: ChatGPT / 深度研究页面，用户提问要求根据成本和项目情况研究抖音精选商品；页面显示将 prompt 补成给 Perplexity / Deep Research 用。
  user_action: 页面停留并向下滚动。
  page_or_scene: ChatGPT research / deep research prompt 页面。
  readable_text: “不是找几个高佣商品，而是按你的月成本和自然流量能力倒推出什么价格带、佣金率、内容难度、履约风险的商品才值得测”；“成本基线是 9500 元/月”。
  evidence_value: 能证明用户正在把选品问题转成结构化研究问题。
  copywriting_use: 可用于“AI 不是自动赚钱按钮，而是帮你把业务问题拆成可测试条件”。

00:08-00:20:
  visible_content: Markdown prompt / 研究任务，标题为“基于 9500 元/月成本，倒推抖音精选联盟选品、分佣与内容测试逻辑”。
  user_action: 继续滚动查看研究目标和约束。
  page_or_scene: ChatGPT 生成的研究 prompt。
  readable_text: “AI 电商项目筛选工厂”；“基于抖音精选 / 抖音精选联盟商品，通过自然流量内容测试，找到值得继续投入的商品方向”。
  evidence_value: 能证明当前研究对象是电商选品 / 佣金 / 内容测试，不是泛泛 AI 赚钱鸡血。
  copywriting_use: 适合做中段证据：“赚钱不是问 AI 选什么，而是先把成本、流量、佣金、转化变量拆开。”

00:20-00:32:
  visible_content: Deep Research 结果卡，标题仍是“基于 9500 元月成本的抖音精选联盟选品、分佣与内容测试逻辑”，显示研究完成情况。
  user_action: 滚动查看结论和成本表。
  page_or_scene: ChatGPT / Deep Research 结果页。
  readable_text: “研究完成情况：1h 5m · 13 次引用 · 270 个搜索”；“一句话结论”；“内容 3 秒能讲清”；“售后与合规不会把利润吃掉”。
  evidence_value: 能证明 AI 研究工具已经生成结构化报告；能显示研究耗时 1h5m，但不能证明最终商业结果。
  copywriting_use: 可用于“AI 帮我把一个模糊问题变成筛选规则”。

00:32-00:44:
  visible_content: 表格显示不同内容量下覆盖 9500 元成本所需的最低佣金 / 单。
  user_action: 继续滚动表格。
  page_or_scene: Deep Research 报告表格。
  readable_text: “30 条/月 82.8 元”“60 条/月 41.4 元”“80 条/月 31.0 元”“100 条/月 24.8 元”“120 条/月 20.7 元”；有效单佣金表中有 10 / 15 / 20 / 25 / 30 / 35 元等行。
  evidence_value: 能证明素材里出现了成本倒推、内容量、佣金门槛等具体数字。
  copywriting_use: 可用于“成本不是口号，是可以被拆成每月内容量和有效单佣金”。

00:44-00:56:
  visible_content: 报告继续展示不同价格带和佣金组合，如 50-79、80-129、130-199、200+ 的代表组合。
  user_action: 滚动回到上方结果段落。
  page_or_scene: Deep Research 报告。
  readable_text: “真正值得你重点扫货的是 80-129 和 130-199 两个价格带”；表格含“覆盖 9500 需商品点击数”“需内容播放量”“约需内容条数”。
  evidence_value: 能证明素材里有“选品不是凭感觉，而是按成本和转化倒推”的画面。
  copywriting_use: 适合支撑“AI 是成本 / 执行系统，不是直接给钱”。

00:56-01:07:
  visible_content: 回到 ChatGPT 结果卡与用户继续提问区域，用户输入关于“家庭清洁工具 / 清洁耗材 / 厕所清洁剂”的图文拼接视频需求。
  user_action: 页面停留在下一轮 prompt。
  page_or_scene: ChatGPT 对话页。
  readable_text: 用户要求根据报告中的候选商品，输出图文拼接 demo 视频 prompt。
  evidence_value: 能证明研究结果被继续转成素材 / demo 生产需求。
  copywriting_use: 可作为“从研究到执行”的桥接画面，但不能证明该 demo 已生成或赚钱。
```

### material_02｜婚纱样片、粽子视频样片与当前文案草稿同屏

```text
00:00-00:08:
  visible_content: Finder 下载目录，选中 `wedding_demo_30s_benchmark_v6.MP4`；右侧预览显示婚纱竖屏视频封面。背景左侧可见 ChatGPT 当前文案草稿标题“AI 到底能不能赚钱？”。
  user_action: 鼠标指向并选中婚纱视频文件。
  page_or_scene: macOS Finder + ChatGPT 页面背景。
  readable_text: 文件名 `wedding_demo_30s_benchmark_v6.MP4`；背景文案含“AI 本身不赚钱，会用 AI 降成本、放大执行”。
  evidence_value: 能证明本地存在婚纱视频样片文件，并和本条文案主题同屏。
  copywriting_use: 可用于“我不是只讲观点，电脑里有实际做过的样片”。

00:08-00:24:
  visible_content: Quick Look 播放 / 预览婚纱视频片段，画面包括白色捧花、婚纱裙摆、室内婚纱照氛围。
  user_action: 打开视频预览，画面随播放变化。
  page_or_scene: Quick Look 视频预览。
  readable_text: 文件标题栏显示 `wedding_demo_30...`；画面本身无可读文案。
  evidence_value: 能证明婚纱样片不只是文件名，确实可打开且有婚纱视觉内容。
  copywriting_use: 可作为“AI 可以先跑出能看的初稿 / 视觉样片”的画面。

00:24-00:36:
  visible_content: Finder / Quick Look 打开婚纱相关 JPEG；画面出现婚礼场景中的新人，随后切回婚纱输出图。
  user_action: 切换或点选婚纱参考 / 输出图片。
  page_or_scene: Finder 图片预览。
  readable_text: 文件名局部可见 `d9fc24b44...JPEG`、`reference_style_02_korean_cafe_wedding.jpeg`。
  evidence_value: 能证明素材中有婚纱图片 / reference 风格图 / 输出图一类素材。
  copywriting_use: 可写“婚纱视频这类视觉样片也能先用 AI 跑样子”，但不能写成“由生活照参考生成”已经被画面完整证明。

00:36-00:52:
  visible_content: Finder 回到最近使用 / 下载目录，背景 ChatGPT 文案更清楚，写到“以前一套视频加图片，从沟通、找素材、剪辑、修图，基本一天就没了；现在给一张生活照做参考，AI 半小时能跑出一套能看的初稿，成本也是二十多。”
  user_action: 在 Finder 中选中 / 切换婚纱文件。
  page_or_scene: Finder + ChatGPT 文案草稿背景。
  readable_text: “AI 不是一个自动赚钱按钮，它是一个成本压缩器”；“现在给一张生活照做参考，AI 半小时能跑出一套能看的初稿，成本也是二十多”。
  evidence_value: 这段是文案草稿可见，不是独立证据；它能告诉 ChatGPT 用户想表达什么，但不能当作事实证明。
  copywriting_use: 可保留为用户经验表达，必须用“我这次的经验是 / 我现在的感受是”降级，不可写成画面证明。

00:52-01:08:
  visible_content: Finder 选中 `01_20秒初版样片.MP4`，Quick Look 预览出现粽子视频画面：手拿粽子、糯米特写、筷子夹粽子。
  user_action: 打开并播放粽子视频样片。
  page_or_scene: Finder + Quick Look 视频预览。
  readable_text: 文件名 `01_20秒初版样片.MP4`；右侧信息显示 MPEG-4 影片，约 5.2MB。
  evidence_value: 能证明素材里有粽子 / 食品类视频样片，且可以打开预览。
  copywriting_use: 可用于“粽子 / 食品电商视频已经有一版样片”，但不能证明它一定由 AI 生成，也不能证明生成耗时或成本。

01:08-01:20:
  visible_content: Finder 重新选中婚纱视频或婚纱相关素材，显示多张婚纱视频 / 图片 / 截图混排。
  user_action: 切换文件，展示同一批本地素材资产。
  page_or_scene: Finder 最近使用 / 下载目录。
  readable_text: 多个 `wedding_demo_30s...` 文件、`01_20秒初版样片.MP4`、`IMG_1264.jpg`、截图文件。
  evidence_value: 能证明本地已经沉淀了多种 AI / 视频项目样片资产。
  copywriting_use: 可作为“不是只研究，也有本地样片资产”的过渡。

01:20-01:31:
  visible_content: Finder 继续浏览目录和素材缩略图，背景仍是当前 AI 赚钱文案草稿。
  user_action: 目录浏览。
  page_or_scene: Finder + ChatGPT。
  readable_text: 背景文案仍可见“真正值钱的不是用了哪个 AI 工具，而是你能不能把自己的业务问题讲清楚”。
  evidence_value: 支撑“素材资产 + 业务问题拆解”这个表达方向。
  copywriting_use: 适合做结尾前的归纳画面，但不是金额 / 时间 / 转化证明。
```

### material_03｜ChatGPT / Codex 工作流与项目执行记录

```text
00:00-00:06:
  visible_content: ChatGPT 项目对话 `生成厕所清洁剂图文视频demo`，页面展示 Codex 执行单。
  user_action: 页面停留在执行单顶部。
  page_or_scene: ChatGPT 项目 / Codex 执行单。
  readable_text: “为‘厕所清洁剂’生成 3 图拼接 + TTS 的图文视频 demo”；“3 张静态图片 -> 拼接成短视频 -> 接入 TTS 配音 -> 合成 mp4 -> 生成验收记录”。
  evidence_value: 能证明项目存在“从素材到 demo 视频再到验收记录”的执行流程。
  copywriting_use: 可用于“我把 AI 接进项目流程，不只是拿它聊天”。

00:06-00:12:
  visible_content: ChatGPT 处理执行单，提示会先确认当前目录、素材路径等底层条件。
  user_action: 页面等待 / 自动思考。
  page_or_scene: ChatGPT 项目。
  readable_text: “我会先做两件底层确认：确认当前目录确实……”等文字局部可见。
  evidence_value: 能证明流程里有执行前确认，而不是直接瞎跑。
  copywriting_use: 可用于“AI 工作流真正值钱的是把执行前提先检查清楚”。

00:12-00:21:
  visible_content: 窗口切到另一个 ChatGPT / Codex 相关对话，左侧项目列表包含 `视频工厂`，当前对话与 `FocuSee`、4:3 素材验证、`video-metadata-probe`、`executing-plans` 相关。
  user_action: 通过侧栏切换项目 / 对话。
  page_or_scene: ChatGPT 项目列表 + Codex 执行说明。
  readable_text: 局部可读“先锁当前目标和 4:3 素材路径”“必须用 video-metadata-probe 做素材宽高校验，用 executing-plans 接你的执行单收口”。
  evidence_value: 能证明 Codex 工作流有项目边界、素材验证、执行计划等机制。
  copywriting_use: 可作为“Codex 本地工作流 / 执行系统”的证据。

00:21-00:33:
  visible_content: 同一执行记录继续显示，提到 v3.1 复审包、720x1280 竖屏、当前对象已找到、仍需验证素材本身 4:3、不能只信口径。
  user_action: 页面停留 / 自动压缩上下文。
  page_or_scene: ChatGPT / Codex 执行记录。
  readable_text: “当前对象已经找回 v3.1 复审包，现有成片还是 720x1280 竖屏”；“下一步我在装配链路和时间线里找原素材路径”；“不能只信口径”。
  evidence_value: 能证明项目里存在技术验证 / 复审包 / 素材路径核查，但文字略糊，需要配口播解释。
  copywriting_use: 可写“我现在把 Codex 接进本地项目，让它检查素材、路径、比例和验收”，不宜写成“所有自动化已稳定跑通”。
```

## 7. evidence_mapping（证据映射）

### material_01

```text
can_prove:
  - AI / Deep Research 可把电商选品问题拆成成本、佣金、内容量、转化、履约风险等变量。
  - 画面中出现 9500 元/月成本基线、不同内容量对应单佣金门槛、商品价格带与内容测试逻辑。
  - 这段能支撑“AI 帮我把业务问题结构化”的表达。
cannot_prove:
  - 不能证明某个商品已经赚钱。
  - 不能证明用户真实投流 / 成交 / 转化数据。
  - 不能证明 AI 自动选品就能盈利。
  - 不能证明粽子视频 10 分钟生成或成本 22 元。
best_used_for:
  - 中段真实证据
  - 数据复盘 / 选品 / 文案系统展示
  - AI 是成本压缩器 / 执行系统
needs_rerecording_if:
  - 想证明真实成交、佣金、点击率、转化率，需要补录平台后台或订单 / 数据截图。
```

### material_02

```text
can_prove:
  - 本地存在婚纱视频 / 图片样片，可打开预览，画面内容是婚纱照 / 婚礼氛围。
  - 本地存在粽子 / 食品视频样片 `01_20秒初版样片.MP4`，可打开预览，画面确实是粽子食品镜头。
  - 当前文案草稿里出现“AI 不是自动赚钱按钮 / 成本压缩器 / 半小时 / 二十多”等表达。
cannot_prove:
  - 不能直接证明婚纱视频 / 图片是由生活照参考生成。
  - 不能直接证明粽子视频由 AI 生成。
  - 不能直接证明“10 分钟左右出效果”或“成本 22 左右”。
  - 不能证明以前拍摄成本高，只能看到用户草稿表达。
best_used_for:
  - 开头钩子
  - 中段真实证据
  - 粽子视频成本对比（只能作为样片存在证据，成本需口述降级）
  - 婚纱视频成本对比（只能作为样片存在证据，成本需口述降级）
needs_rerecording_if:
  - 要证明“由生活照参考生成”，需补录生活照参考 -> AI 生成结果的过程或目录对应关系。
  - 要证明“10 分钟 / 22 元”，需补录计时、账单、API 控制台、生成任务记录或成本明细。
```

### material_03

```text
can_prove:
  - ChatGPT / Codex 项目里存在明确执行单、目标、输出要求和验收记录意识。
  - Codex 工作流会检查当前目录、素材路径、4:3 素材、v3.1 复审包等。
  - 能支撑“我不是只用 AI 做一句话，而是把它接进本地项目执行流程”。
cannot_prove:
  - 不能证明厕所清洁剂 demo 已经生成成功。
  - 不能证明 TTS / 视频合成 / manifest 全部已完成。
  - 不能证明 Codex 工作流长期稳定或已完全自动化。
best_used_for:
  - Codex 本地工作流展示
  - 数据复盘 / 选品 / 文案系统展示中的“执行系统”段落
  - 中段真实证据补充
needs_rerecording_if:
  - 要证明 demo 真实生成完成，需要补录终端输出、生成目录、成品预览、manifest 或验收记录。
```

## 8. copy_support_check（文案支撑检查）

```text
claim: AI 是否真的展示了粽子 / 电商视频相关素材
support_status: partially_supported
supporting_material:
  - material_01: 电商选品 / 佣金 / 内容测试研究报告
  - material_02: `01_20秒初版样片.MP4` 粽子视频预览
evidence_note: 能证明有粽子食品视频样片和电商选品研究画面；不能证明粽子样片由 AI 生成。
copy_action: rewrite

claim: 是否能证明“以前拍摄成本高”
support_status: not_supported
supporting_material:
  - material_02 only shows draft text, not hard proof
evidence_note: 画面只有文案草稿口述“以前一套视频加图片，从沟通、找素材、剪辑、修图，基本一天就没了”，没有历史账单、拍摄报价、排期记录或人工成本证据。
copy_action: downgrade

claim: 是否能证明“现在 AI 10 分钟左右出效果”
support_status: not_supported
supporting_material:
  - material_02 visible draft text and sample file name only
evidence_note: 素材未显示计时、生成任务日志或工具记录；`01_20秒初版样片.MP4` 文件名能证明有 20 秒初版样片，不能证明 10 分钟生成。
copy_action: downgrade

claim: 是否能证明“成本 22 左右”
support_status: not_supported
supporting_material:
  - material_02 visible draft text only
evidence_note: 素材未显示账单、API 消耗、支付记录或成本明细。
copy_action: downgrade

claim: 是否能证明婚纱视频 / 图片由生活照参考生成
support_status: partially_supported
supporting_material:
  - material_02
evidence_note: 能证明有婚纱视频 / 图片输出样片；不能证明源头是生活照，也不能证明从生活照到婚纱图的生成链路。
copy_action: rewrite

claim: 是否能证明 Codex 本地工作流
support_status: partially_supported
supporting_material:
  - material_03
evidence_note: 画面显示 Codex 执行单、素材路径确认、video-metadata-probe、4:3 验证、v3.1 复审包等项目流程；但未显示终端命令完整输出或最终文件结果。
copy_action: keep_with_precision

claim: 是否能证明文案、数据复盘、选品这些功能
support_status: partially_supported
supporting_material:
  - material_01
  - material_03
evidence_note: material_01 支撑选品 / 成本倒推 / 研究，material_03 支撑执行单 / 验证流程；没有真实平台数据复盘截图。
copy_action: rewrite

claim: 是否能支撑“AI 是成本压缩器 / 执行系统”这个核心判断
support_status: partially_supported
supporting_material:
  - material_01
  - material_02
  - material_03
evidence_note: 三段合起来能支撑“AI 帮用户把研究、样片、执行流程前置化 / 结构化”；但不能直接证明赚钱结果、成本数额和时间数额。
copy_action: keep_but_frame_as_user_experience
```

必须保留的边界句：

```text
成本 / 时间数据来自用户口述，素材未直接证明；文案可保留为用户经验陈述，但不能写成素材画面已证明。
```

## 9. suggested_copy_revision_for_chatgpt（给 ChatGPT 的文案修改建议）

```text
strongest_material_points:
  - material_02 最强：婚纱样片和粽子视频样片确实存在，可作为“AI 先跑样子”的直观画面。
  - material_01 最强：9500 元/月成本倒推、佣金门槛、内容条数和价格带，适合支撑“赚钱要拆业务问题”。
  - material_03 最强：ChatGPT / Codex 执行单和素材验证流程，适合支撑“AI 接进工作流 / 执行系统”。

weak_or_unsupported_points:
  - “10 分钟左右”没有计时证据。
  - “成本 22 左右”没有账单 / API 消耗 / 支付记录证据。
  - “以前拍摄成本很高”没有旧流程报价 / 时间记录证据。
  - “婚纱由生活照参考生成”没有源图 -> 结果图的同屏链路。
  - “粽子视频由 AI 生成”没有生成工具 / 任务记录 / prompt 过程。

recommended_script_order:
  - 先用问题句开头：AI 到底能不能赚钱？
  - 先给结论：AI 本身不直接赚钱；它更像成本压缩器 / 执行放大器。
  - 切 material_02：先给婚纱 / 粽子样片，证明“我确实有跑出来的样子”。
  - 切 material_01：说明真正关键是把 9500 元月成本、佣金、内容量、转化变量拆清楚。
  - 切 material_03：说明 Codex / ChatGPT 是怎么被接进本地项目流程里，负责检查、生成、验收。
  - 收束：AI 不替你赚钱，但能让你更快、更便宜地试错；赚钱仍取决于你有没有讲清业务问题。

recommended_opening_route:
  - 首选 direct_question_title_card：直接打出“AI 到底能不能赚钱？”
  - 可选 screen_first_opening：直接从 material_02 的样片预览切入。
  - 不建议当前直接用 meme_gif_opening_hook，除非另有已授权梗图 / GIF 资产；当前 3 段素材没有 meme 资产。

recommended_middle_structure:
  - 第一层：样片可见，证明“AI 能先跑样子”。
  - 第二层：成本倒推可见，证明“真正要算的是业务模型”。
  - 第三层：Codex 工作流可见，证明“执行系统能减少反复沟通和手动检查”。

recommended_card_placement:
  - 开头卡：问题句 + 一句话结论。
  - 中段不强插大卡，优先保留 FocuSee 自带运镜和真实录屏。
  - 在 material_01 成本表之后插一张轻总结卡：“成本不是感觉，是公式。”
  - 在 material_02 样片之后插一张降级说明卡：“样片能证明有结果，成本 / 时间仍是经验口述。”

recommended_lines_to_keep:
  - “AI 本身不赚钱，会用 AI 降成本、放大执行。”
  - “AI 不是一个自动赚钱按钮，它是一个成本压缩器。”
  - “真正值钱的不是用了哪个 AI 工具，而是你能不能把自己的业务问题讲清楚。”

recommended_lines_to_rewrite:
  - “10 分钟左右出效果”改成“我这轮的经验是，很快就能先跑出一版能看的样子；具体时间别写死，除非补录计时证据。”
  - “成本也是二十多”改成“这次的成本在我的口述经验里是二十多，但画面没有账单，不能写成画面证明。”
  - “生活照参考生成婚纱”改成“素材里能看到婚纱样片；如果要写生活照参考生成，最好补一句‘这部分来自我的项目记录 / 需要补源图画面’。”

recommended_lines_to_delete_or_downgrade:
  - 删除或降级任何“AI 自动赚钱”的暗示。
  - 降级“以前一天 / 现在半小时”的绝对对比，除非补旧流程证据。
  - 降级“10 分钟 / 22 元”成用户经验，不做画面已证。
```

## 10. content_route_card_v2_draft（内容路由卡 V2 草案）

```text
content_route_card_v2:
  meta:
    content_type: AI 问题点破 + 真实工作流证据
    validation_goal: 验证“AI 不是直接赚钱工具，而是成本压缩器 / 执行放大器”的表达是否有真实素材支撑
    route_confidence: medium_high_for_core_judgment, low_for_exact_cost_and_time_claims

  opening_route_decision:
    selected_opening_route: direct_question_title_card
    route_reason: 当前 3 段素材没有独立 meme / GIF 资产；最稳路线是用问题句直接立论，再快速切到样片和成本表

  evidence_plan:
    core_evidence:
      - material_02: 婚纱样片 + 粽子视频样片可见
      - material_01: 9500 元/月成本倒推与选品研究表可见
      - material_03: ChatGPT / Codex 执行单与素材验证流程可见
    evidence_type:
      - user_recording
      - step_screenshot
      - result_screenshot
    evidence_missing_or_unclear:
      - 10 分钟生成计时
      - 22 元成本账单
      - 生活照源图到婚纱结果的生成链路
      - 真实成交 / 播放 / 转化数据

  middle_carrier_decision:
    middle_carrier: user_recording_screen_capture
    source_material_list:
      - material_01
      - material_02
      - material_03
    focusee_middle_editing_decision:
      recording_layer_motion_baked_in: true_for_observed_motion
      selected_editing_policy:
        - keep_original_focusee_motion
        - direct_cut_by_script
        - trim_dead_time_only
      no_secondary_zoom_by_default: true
      blocked_if_key_evidence_unclear: true

  card_placement_decision:
    summary_card_usage: optional_after_material_01_cost_table
    reversal_card_usage: optional_after_opening_conclusion, only if ChatGPT writes a clear reversal
    result_diff_card_usage: use_with_caution; result_diff is mostly user experience, not hard data
    prompt_tail_card_usage: not_recommended_by_default_for_this_video

  api_human_usage:
    usage_count: not_required_for_this_material_report
    usage_role: none_currently
    route_reason: 当前强证据来自录屏和样片，不需要强插 API 生成真人

  ppt_usage:
    usage_type: optional_keyword_card_only
    density_line: 少量卡片辅助，不替代素材证据

  blocked_if:
    - ChatGPT 想写死“10 分钟 / 22 元”但用户不补计时或账单
    - ChatGPT 想写“生活照参考生成婚纱”但不补源图到结果图链路
    - ChatGPT 想写“AI 已经赚钱 / 商品已验证盈利”但没有平台数据
```

## 11. final_handoff_to_chatgpt（给 ChatGPT 的最终交接）

```text
给 ChatGPT：

我已读取 3 段素材。请基于以下素材事实修改《今天就说一个事，AI 到底赚不赚钱》的文案。注意只能写素材能支撑的内容，用户口述成本 / 时间可作为个人经验表达，不能冒充素材画面证明。

素材事实：
1. material_01 是 ChatGPT / Deep Research 研究画面，主题是基于 9500 元/月成本，倒推抖音精选联盟选品、佣金、内容量、点击 / 转化和履约风险。它能支撑“AI 帮我把赚钱问题拆成业务变量”，不能证明真实成交或赚钱。
2. material_02 是 Finder + Quick Look 预览。它能看到婚纱视频 / 图片样片，也能看到 `01_20秒初版样片.MP4` 粽子视频样片。它能支撑“我确实有跑出样片”，但不能证明粽子视频由 AI 生成、不能证明 10 分钟、不能证明成本 22、也不能完整证明婚纱由生活照参考生成。
3. material_03 是 ChatGPT / Codex 工作流画面，能看到 Codex 执行单、素材路径确认、video-metadata-probe、4:3 素材验证、v3.1 复审包等项目执行机制。它能支撑“我把 AI 接进本地项目流程”，不能证明 demo 已全部生成成功或自动化长期稳定。

建议文案结构：
开头直接问“AI 到底能不能赚钱？”；然后立结论“AI 本身不直接赚钱，它更像成本压缩器 / 执行放大器”。中段先放 material_02 的婚纱 / 粽子样片，证明能先跑样子；再放 material_01 的 9500 成本倒推表，解释赚钱不是靠工具名，而是拆成本、佣金、内容量和转化；最后放 material_03 的 Codex 工作流，说明 AI 真正值钱的是把执行、检查、验收接进系统。

必须降级的点：
“10 分钟左右”“成本 22 左右”“以前一天 / 现在半小时”“生活照参考生成婚纱”目前都没有完整画面证据。可以写成“我的经验 / 我这次的感受 / 这轮项目里我看到的是”，不要写成画面已经证明。

必须避免：
不要写 AI 自动赚钱，不要写商品已盈利，不要写平台数据已验证，不要把样片存在写成商业结果成立。
```

## 12. forbidden_status_check（禁止状态检查）

```text
original_media_modified: false
video_generated: false
video_edited: false
audio_replaced: false
external_api_called: false
secret_read: false
content_validation_promoted: false
send_ready_promoted: false
publish_status_promoted: false
voice_validation_promoted: false
final_voice_validated_promoted: false
visual_master_locked_promoted: false
```

## 13. validation_check（完成前验证）

```text
3_materials_found: passed
3_materials_openable: passed
basic_metadata_recorded: passed
timecode_detail_written: passed
evidence_mapping_written: passed
copy_support_check_written: passed
content_route_card_v2_draft_written: passed
final_handoff_to_chatgpt_written: passed
original_media_unchanged: passed
no_video_generation: passed
no_dynamic_status_promotion: passed
```

## 14. final_completion_status（本轮完成状态）

`completed（已完成）`：本轮已找到并解析 3 段素材，输出给 ChatGPT 修改文案用的素材细节报告。报告只证明素材审计与文案桥接完成，不代表最终文案已完成，不代表内容验证通过，不代表可发布。

## 15. next_target（下一个目标）

让 ChatGPT 基于本报告重写《今天就说一个事，AI 到底赚不赚钱》的最终文案，并把所有成本 / 时间 / 生成链路表述降级到素材能支撑的范围内。
