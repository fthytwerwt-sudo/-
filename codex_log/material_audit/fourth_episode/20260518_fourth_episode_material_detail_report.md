# 第四期素材内容审计报告

```text
skill_used = skills/视频素材解析_video_material_audit/SKILL.md
```

## 1. 本轮结论

`已确认` 第四期素材目录已命中：`/Users/fan/Documents/视频工厂/素材录制/第四期`。

`已确认` 目录内共有 4 个 `.mp4` 素材，均可用 `ffprobe（媒体信息检查工具）` 读取，均可用 `ffmpeg（媒体处理工具）` 解码，均为 H.264、30fps、无音轨。该结论只代表 `technical_validation（技术验证）`，不代表 `content_validation（内容验证）`。

`部分成立` 这 4 个素材能支撑下一条内容从“数据复盘能力”转向“真实 AI 工作流实验”。最稳表达不是“我已经做出一个自动化视频系统”，而是：

- 先把一个模糊想法拆成可执行任务。
- 再把任务拆成字段、模板、报告、验收标准和下一步。
- 最后再决定文案和视频怎么写。

`待验证` 这批素材还不能完整证明“AI 已经进入真实执行并产出最终成品”。画面主要是 ChatGPT / Markdown / GitHub 页面和执行单，不是完整的 Codex 终端执行过程，也没有展示最终文件生成闭环。因此如果公开视频写“AI 已经把整条视频自动做完”，证据不足。

`建议` 如果只做一条 60-90 秒视频，主线可以是：

> 我发现我用 AI 做视频，第一步不能是“帮我写文案”，而是先把一句糊话拆成任务单。拆清楚以后，AI 才知道要生成什么、检查什么、什么时候该阻断。

## 2. 素材清单

| material_id | file_name | duration | role_guess |
| --- | --- | ---: | --- |
| `material_01` | `内建视网膜显示器 2026-05-17 23-59-42.mp4` | 91.50s | 四样本方向复盘与下一轮变量决策说明 |
| `material_02` | `内建视网膜显示器 2026-05-18 00-08-22.mp4` | 122.80s | 把一个复盘 prompt 拆成通用配置、字段、模板、报告和 Definition of Done |
| `material_03` | `内建视网膜显示器 2026-05-18 00-12-15.mp4` | 59.47s | V003 数据回填执行单与 Codex 边界说明 |
| `material_04` | `内建视网膜显示器 2026-05-18 00-17-06.mp4` | 114.20s | 从 V002/V004 文案数据到新方向判断：一句糊话变执行单 |

审计辅助图：

- `dist/material_audit/fourth_episode/material_01_contact_sheet_labeled.jpg`
- `dist/material_audit/fourth_episode/material_02_contact_sheet_labeled.jpg`
- `dist/material_audit/fourth_episode/material_03_contact_sheet_labeled.jpg`
- `dist/material_audit/fourth_episode/material_04_contact_sheet_labeled.jpg`

说明：contact sheet 仅作本地审计辅助，不作为正式视频产物；源视频不提交 Git。

## 3. 媒体基础信息

| material_id | size | resolution | aspect_ratio | fps | codec | audio | decodable | technical_status |
| --- | ---: | --- | --- | ---: | --- | --- | --- | --- |
| `material_01` | 152.72 MiB | 2870x1676 | 1.71:1 | 30.000 | h264 | false | true | `metadata_validation_passed_decodable_no_audio` |
| `material_02` | 162.70 MiB | 2872x1646 | 1.74:1 | 30.000 | h264 | false | true | `metadata_validation_passed_decodable_no_audio` |
| `material_03` | 122.12 MiB | 2882x1726 | 1.67:1 | 30.000 | h264 | false | true | `metadata_validation_passed_decodable_no_audio` |
| `material_04` | 215.12 MiB | 2906x1646 | 1.77:1 | 30.000 | h264 | false | true | `metadata_validation_passed_decodable_no_audio` |

基础异常检查：

- `blackdetect（黑屏检测）`：未观察到 2 秒以上明显黑屏事件。
- `freezedetect（静帧检测）`：4 个素材都有少量静帧段，主要对应用户停留阅读 ChatGPT / Markdown 页面，不等同于素材损坏。
- `audio_present = false`：这批素材不能证明口播、TTS、声音质量或音色状态。
- `OCR（文字识别）`：本轮未使用 OCR 工具，画面文字来自 contact sheet 和关键帧人工可读观察；读不清处已标记不确定。

## 4. 四个素材逐条时间码解析

### material_01

```yaml
material_id: material_01
file_name: 内建视网膜显示器 2026-05-17 23-59-42.mp4
duration: 91.50s
role_guess: 四样本方向复盘与下一轮变量决策说明
```

| timecode | visible_content | user_action | readable_text | possible_copy_value | evidence_strength | platform_risk | privacy_risk | uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:16 | ChatGPT 页面，用户追问“现在视频复盘到底应该重点要看什么” | 停留阅读 | 可见 `review_loop`、`latest.md`、`current_data_goal_anchor` 等入口词 | 可作为“先找系统入口，不是先写稿”的背景 | medium | low | low | 画面远景，小字需人工复核 |
| 00:16-00:32 | ChatGPT 展开“下一轮变量决策前”的数据录入复盘 | 滚动阅读 | 数据来源、判断时间窗、截图归档、字段提取、缺失标记、写入记录和 JSON；强调“这个流程不负责下结论” | 支撑“AI 工作流先拆数据/字段/记录，不急着写文案” | high | low | medium | 可见平台/仓库字段，需避免公开视频里过长停留 |
| 00:32-00:48 | 文案迭代复盘与样本分类 | 滚动阅读 | V002/V003/V004、`copy_iteration_decision_system.py`、`opening_packaging`、`bridge_3_8s` | 可说明“下一步不是凭感觉改文案，而是先看样本类别和问题层” | high | medium | medium | V002 平台异常样本不能被写成正常样本 |
| 00:48-01:04 | 素材 / 证据盘说明 | 停留阅读 | “不只是视频文件存在，而是要判断能证明什么、不能证明什么、可做开头/中段/证据、隐私风险/平台风险、是否需要补录” | 非常适合做本期审计的元说明，解释为什么要先审计素材 | high | medium | medium | 不直接证明第四期素材内容，只证明审计方法 |
| 01:04-01:20 | 下一轮变量复盘 | 滚动阅读 | “不是马上写下一条视频，而是先决定：改开头、改选题、改平台风险表达、改证据呈现、改账号价值点，还是继续等数据” | 支撑“第一步不是写稿，而是判断变量”的过渡 | high | low | low | 不能写成最终变量已确定 |
| 01:20-01:31 | 四样本方向复盘目标 | 停留阅读 | V002 异常信号、V003 当前目标、V004 最新早期样本；输出三个东西：最强价值信号、最大风险、下一条验证主变量 | 可作为结尾判断：下一条先做方向层复盘 | medium-high | low | low | 不能替代 ChatGPT/用户最终方向判断 |

material_01:

- `can_support`: 证明当前系统不是直接写文案，而是先做数据、文案、素材、平台风险和变量复盘。
- `cannot_support`: 不能证明“真实 AI 执行已经产出成片”，也不能证明下一条正式变量已锁定。
- `best_use`: 开场前的背景铺垫或结尾判断卡素材。
- `not_allowed_use`: 不要把 V002/V003/V004 的数据画面写成最新正式结论。
- `needs_reshoot`: 如果要公开视频，建议补录更干净的“复盘盘点总览”画面，减少仓库字段和历史样本细节停留。

### material_02

```yaml
material_id: material_02
file_name: 内建视网膜显示器 2026-05-18 00-08-22.mp4
duration: 122.80s
role_guess: 把一个复盘 prompt 拆成通用配置、字段、模板、报告和 Definition of Done
```

| timecode | visible_content | user_action | readable_text | possible_copy_value | evidence_strength | platform_risk | privacy_risk | uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:15 | 用户提出要一个可复用 prompt，别人能复制视频复盘流程并可定制 | 停留阅读 | “给我一个 prompt，可以让别人直接用 trace...但是需要通用的，而且用户可以自己方便的去定制” | 最适合做开头反差：不是让 AI 写一段文案，而是让 AI 先拆一个可复用系统 | high | medium | low | “直接复制”公开视频表达需弱化 |
| 00:15-00:30 | ChatGPT 重新定义任务边界 | 停留 / 滚动 | “不是短视频脚本机器”，而是短视频复盘机制；一条视频后判断下一条只改一个主变量 | 支撑“先定义系统目标和使用场景” | high | low | low | 不能写成所有账号通用效果已验证 |
| 00:30-00:50 | 用户可定制区与 YAML 配置 | 滚动阅读 | `review_config.yaml`、平台、账号阶段、metrics、problem_layers 等 | 支撑“拆成配置字段，而不是一句话出文案” | high | low | low | 代码 / YAML 长时间展示需配解释卡，避免观众看不懂 |
| 00:50-01:10 | 协作边界与目录结构 | 滚动阅读 | 需要创建的目录、数据入口、文案版本记录、诊断模板、下一轮建议模板；强调边界 | 可做中段主体证据：AI 把需求拆成多个交付件 | high | medium | low | 不能说这些文件已全部在第四期任务中生成 |
| 01:10-01:30 | 数据口径和文案记录机制 | 滚动阅读 | 播放量不是最终目标、点赞不是需求、收藏是可复用价值信号但不能直接等于成功、私信要分层 | 可说明“先把判断口径拆清楚，才知道怎么写” | high | low | low | 这些是机制建议，不能写成平台普适真理 |
| 01:30-01:50 | 变量复盘和报告结构 | 滚动阅读 | 问题层、变量层、内容层、互动层、转化层；一行结论、当前数据状态、分层诊断、问题判断、单变量建议 | 可作为“AI 从判断到报告结构”的核心证据 | high | low | low | 小字多，成片要放大或做卡片 |
| 01:50-02:03 | Definition of Done 与命令 | 停留阅读 | 目录结构、配置文件、模板、诊断系统、README、运行一次后生成 Markdown 复盘报告 | 证明“拆任务”的终点是验收标准，不是漂亮回答 | high | medium | low | 不要公开视频里强调可运行命令细节过久 |

material_02:

- `can_support`: 最强支撑“第一步不是写文案，而是拆任务”。它清楚展示从一个模糊 prompt 到配置、字段、目录、报告、验收标准的过程。
- `cannot_support`: 不能证明完整工具已经产品化，也不能证明别人复制后一定有效。
- `best_use`: 主素材和中段主体证据。
- `not_allowed_use`: 不要写“一键复制整个复盘系统”“自动生成爆款视频”“任何账号都适用且保证有效”。
- `needs_reshoot`: 如果想更像公开视频，建议补录一个干净版，只展示需求拆解、字段、模板和 DoD，不展示太长 YAML。

### material_03

```yaml
material_id: material_03
file_name: 内建视网膜显示器 2026-05-18 00-12-15.mp4
duration: 59.47s
role_guess: V003 数据回填执行单与 Codex 边界说明
```

| timecode | visible_content | user_action | readable_text | possible_copy_value | evidence_strength | platform_risk | privacy_risk | uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:10 | ChatGPT 页面和 GitHub 侧栏，显示 V003 数据回填任务 | 停留 / 放大 | 运营数据录入、项目文件修改、系统重跑；不生成新视频、不推进状态 | 可证明“AI 先收到任务类型和边界” | medium-high | medium | high | 侧栏和仓库信息不适合直接公开 |
| 00:10-00:20 | 代码块 / 执行单，包含 forbidden action 和 DeepSeek supply gate | 滚动阅读 | `next_formal_video_execution_prompt / content_validation / send_ready` forbidden；DeepSeek gate | 支撑“任务拆解包含禁止项，不是只列要做什么” | high | medium | high | 代码画面可读性低，公开视频需解释 |
| 00:20-00:30 | 数据快照和状态写入说明 | 滚动阅读 | `post_72h_pre_7d_snapshot`、V003 current operation；不是 7d final | 可作为“正确记录数据窗口”的辅助证据 | medium-high | low | medium | 不能作为第四期新方向的主证明 |
| 00:30-00:45 | 截图文件、路径、账号诊断和 JSON 任务 | 滚动阅读 | 可见截图路径、文件名、账号诊断、归档路径 | 不建议作为公开视频主体；只可内部证明执行单颗粒度 | medium | medium | high | 高隐私风险，需裁切/打码 |
| 00:45-00:55 | V003 结构化数据和 GitHub 侧栏 | 停留 / 切换 | 播放 143、平均 20 秒、2s 跳出 48.81%、5s 28.57%、完播 4.05%、收藏 3/2.10% | 可低置信度说明“数据被结构化”，但不是下一条主题主证据 | medium | low | high | 不要写成最新 7d final 或方向结论 |
| 00:55-00:59 | 路由 / 状态动作字段被选中 | 鼠标选择 | `operation_data_intake + account_diagnostic_intake`、forbidden action | 可证明“状态边界被锁住” | medium | low | high | 画面可读性不足 |

material_03:

- `can_support`: 辅助证明 AI 任务会先拆成任务类型、禁止项、数据窗口、文件和验证，而不是直接让 Codex 写文案。
- `cannot_support`: 不能证明第四期新选题已经可执行，也不能证明 Codex 已完成本轮第四期审计前的产物。
- `best_use`: 内部报告证据，或公开视频中短暂裁切放大“forbidden action / not generate video”片段。
- `not_allowed_use`: 未打码前不建议公开；不能展示本地路径、截图文件名、GitHub 侧栏、账号诊断细节。
- `needs_reshoot`: 建议补录一段干净的 Codex 接收任务画面，只保留任务清单和状态边界，隐藏路径和账号侧栏。

### material_04

```yaml
material_id: material_04
file_name: 内建视网膜显示器 2026-05-18 00-17-06.mp4
duration: 114.20s
role_guess: 从 V002/V004 文案数据到新方向判断：一句糊话变执行单
```

| timecode | visible_content | user_action | readable_text | possible_copy_value | evidence_strength | platform_risk | privacy_risk | uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00-00:20 | 用户补充 V002 文案 / 数据，ChatGPT 区分异常样本和补录边界 | 停留 / 滚动 | V002 56 播放、6 赞、9 收藏；V002 是平台审核减推异常样本，不是正常自然分发样本 | 可作为“不是先写方向，先分清样本类别”的证据 | medium-high | medium | medium | 数据为用户补充，缺截图复核 |
| 00:20-00:40 | V002 补录字段和文件清单 | 滚动阅读 | `user_provided_in_chat / no_screenshot_yet`、不覆盖历史、不设 current target、py_compile 命令 | 支撑“任务拆成文件/字段/验证” | medium | medium | medium | 代码/命令画面不宜长停留 |
| 00:40-00:55 | V002 raw copy 片段与用户新提问 | 滚动 / 停留 | 用户说文案和数据基本齐全，要求分析方向，不清楚去仓库看 | 可做开头转折：“我不是让 AI 直接写稿，而是让它先回仓库判断” | high | low | medium | raw copy 若含平台风险词需谨慎 |
| 00:55-01:10 | ChatGPT 先确认两个事实，再做方向判断 | 停留阅读 | 要先确认 V002/V004 是否已入库、系统是否可以做方向判断；当前断点不是内容角度，而是前端包装和风险表达 | 非常适合开头证据：AI 没有急着写文案，先锁事实和判断权限 | high | low | low | 仍是 ChatGPT 判断，不是用户最终拍板 |
| 01:10-01:30 | 两条方向：自动制作流程 vs 一句话变执行单 | 滚动阅读 | “自动流 / 自动制作方式”风险更高；“一句糊话变执行单”更安全；前台表达不是“我做了一个自动流”，而是“为什么你用 AI 总是废话，因为你给的是一句糊话，不是任务单” | 最强开头/中段方向证据，直接命中本轮新方向 | high | high | low | “自动流 / 全自动”属于平台风险表达，必须改写 |
| 01:30-01:50 | 当前账号价值和具体表达 | 滚动阅读 | “不秀结果，而是拆给你看为什么”；“不是为了涨粉，是为了验证一人公司的闭环”；“我在测试一个人能不能靠 AI 跑通内容、产品、复盘和服务闭环” | 支撑账号价值从方法论复盘转向真实工作流实验 | high | medium | low | 不要写成商业闭环已成立 |
| 01:50-01:54 | 下一步判断 | 停留阅读 | 先整理两个版本：公开制作流程方向、一句话变执行单；做到判断后再做文案/剪辑 | 结尾边界：本轮只到写稿判断，不到执行 prompt | high | low | low | 不直接生成最终稿 |

material_04:

- `can_support`: 最适合做开头和方向切换证据，直接说明为什么“先拆任务”比“直接写文案 / 公开自动流”更稳。
- `cannot_support`: 不能证明最终脚本已确认，也不能证明自动制作流程可安全公开。
- `best_use`: 开头证据、方向判断卡、结尾“先判断后写稿”的边界。
- `not_allowed_use`: 不要沿用“全自动 / 自动流 / 公开制作方式”作为标题核心，存在平台风险。
- `needs_reshoot`: 若要公开视频，建议补录同一段判断的干净版，保留“一句糊话变执行单”，删去或弱化“全自动 / 自动流”。

## 5. 哪些素材能支撑当前新方向

当前新方向：

```text
我用 AI 做视频，第一步不是写文案，而是拆任务
```

| proof_point | 支撑素材 | 判断 |
| --- | --- | --- |
| 从一句模糊想法开始 | `material_02 00:00-00:15`, `material_04 00:40-00:55` | `high` |
| AI 一开始给的是建议，不是执行 | `material_04 00:55-01:10`, `material_01 01:04-01:20` | `high` |
| 用户 / ChatGPT 如何把想法拆成任务 | `material_02 00:15-01:50`, `material_04 01:10-01:50` | `high` |
| 是否出现任务列表 / 字段 / 模板 | `material_02 00:30-02:03`, `material_03 00:10-00:30` | `high` |
| 是否出现项目结构 | `material_02 00:50-01:20`, `material_03 00:20-00:45` | `medium-high` |
| 是否出现素材计划 | `material_01 00:48-01:04` | `medium` |
| 是否出现执行单 / prompt | `material_03 00:05-00:25`, `material_04 00:20-00:40` | `medium-high` |
| 是否出现 Codex 接收任务 | `material_03 00:05-00:25` | `medium`，只看到执行单/仓库侧栏，不是完整终端运行 |
| 是否出现系统真实产物 | `material_02 01:50-02:03` 只出现 Definition of Done；`material_03` 出现字段/文件路径 | `medium-low`，不足以证明产物已完成 |
| 是否能证明“不是先写文案，而是先拆任务” | `material_02`, `material_04` | `high` |
| 是否能证明“非技术人也能判断 AI 有没有开始干活” | `material_02 01:50-02:03`, `material_03 00:10-00:25` | `medium-high` |

结论：

- `material_02` 是最适合作为主素材的素材。
- `material_04 00:55-01:30` 是最适合作为开头证据的片段。
- `material_02 00:30-01:50` 是最适合作为中段主体证据的片段。
- `material_03 00:30-00:55` 是最不建议公开视频使用的片段，隐私风险最高。

## 6. 可支撑的具体文案点

可以写进口播或字幕的点：

- “我发现我以前用 AI 做视频，第一步太容易让它写文案。”
- “但真正卡住的不是文案，是我没有先把任务拆清楚。”
- “比如我只说：给我一个复盘 prompt。AI 如果不拆任务，就只能给我一段漂亮话。”
- “这次我让它先拆：配置、数据字段、样本分类、文案记录、报告模板、验收标准。”
- “拆到这一步，我才知道下一条视频到底该拍什么，而不是凭感觉重写一版。”
- “AI 真正有用的地方不是替我拍板，而是帮我把一个模糊想法压成可执行清单。”
- “先判断风险，再决定表达。‘全自动’这种词看起来爽，但对平台可能很危险。”

适合做卡片 / 字幕的点：

- `第一步不是写文案，是拆任务`
- `一句糊话 -> 任务单 -> 素材清单 -> 验收标准`
- `播放量只是入口，不是最终目标`
- `素材存在 != 内容通过`
- `自动流这个词要谨慎，公开表达要换成真实工作流复盘`

## 7. 不能证明 / 禁止写入的内容

`not_allowed_claims（禁止写入文案的主张）`：

- 不得写“AI 已经自动做完整条视频”。
- 不得写“全自动制作方式已经跑通并可复制”。
- 不得写“只要复制这个 prompt，就能复刻整个账号系统”。
- 不得写“V002/V004 已经证明方向成立”。
- 不得写“V002 是正常自然流量样本”。
- 不得写“V004 已经完成 24h / 72h / 7d 数据验证”。
- 不得写“商业闭环已经成立”。
- 不得写“已有私信、咨询、客户或成交”。
- 不得把 `ffprobe / ffmpeg` 技术检查通过写成内容通过。
- 不得把 `material_03` 中的执行单画面写成 Codex 已完整执行完成，除非另有仓库运行证据。

## 8. 平台风险与隐私风险

### 平台风险

| material_id | timecode | risk_level | risk_type | note | recommended_action |
| --- | --- | --- | --- | --- | --- |
| `material_01` | 00:32-00:48 | medium | V002 异常样本 / 平台风险表达 | 画面讨论 V002 平台减推和 `policy_limited_abnormal_operation_sample` | 只作为内部判断，不直接放大平台审核细节 |
| `material_02` | 00:00-00:15 | medium | “直接复制 / prompt”表达 | 容易被理解成复制账号流程或模板化生产 | 改成“复用复盘框架”，不要写“复制整个视频复盘” |
| `material_02` | 01:50-02:03 | medium | 命令 / 模板 / report | 长时间展示命令、模板、report 可能被误判为工具引导 | 加卡片解释“这是内部验收清单”，不引导下载工具 |
| `material_03` | 00:10-00:25 | medium | DeepSeek / 命令 / 仓库执行单 | 工具链画面过长，观众可能看不懂用途 | 只取 1-2 秒关键字段，配旁白解释“先锁禁止项” |
| `material_04` | 01:10-01:30 | high | “全自动 / 自动流 / 公开制作方式” | 命中已有平台风险词，容易触发自动化生产/工具导流误判 | 公开表达改成“一句话拆任务执行单”或“真实工作流复盘” |

### 隐私风险

| material_id | timecode | risk_level | risk_type | recommended_action |
| --- | --- | --- | --- | --- |
| `material_01` | 00:16-00:56 | medium | 仓库文件名、项目状态字段 | 可公开视频前裁切，只保留关键句，不展示完整仓库路径和字段 |
| `material_02` | 全段 | low | 主要是通用配置 / 模板，无明显个人敏感信息 | 公开视频时仍建议隐藏浏览器侧栏和账号头像 |
| `material_03` | 00:00-00:59 | high | GitHub 侧栏、仓库/分支、截图文件名、可能的本地路径与账号诊断信息 | 未打码前不建议公开；若使用，只裁切中间执行单字段 |
| `material_04` | 00:20-00:40 | medium | raw copy、数据补录、命令和文件列表 | 公开视频前裁切代码块和侧栏，避免长时间展示文件清单 |

本轮未观察到明确 `API key`、`token`、手机号、邮箱或客户信息，但 `material_03` 的路径/侧栏/截图信息足以构成高隐私风险。

## 9. 和 V002 / V003 / V004 数据复盘的关系

这批素材不是替 V002/V003/V004 下内容结论，而是解释“为什么下一条内容不应该继续只是讲数据复盘”。

- `V002`: 作为平台风险和异常样本提醒出现。不能写成正常自然分发成功或失败。
- `V003`: 作为当前 operation target 和数据结构化样本出现。不能写成 7d final 或正式复盘完成。
- `V004`: 作为最新早期样本和 raw copy 记录出现。不能写成 24h / 72h / 7d final。
- 第四期素材的真正价值：把账号证明方式从“我讲一个判断”转成“我展示一个真实拆任务过程”。

## 10. 是否需要补录

`需要补录`，但不是因为当前素材完全不可用，而是因为公开视频需要更干净、更低风险的证据窗口。

最小补录建议：

1. 补录一段干净画面：一行模糊想法，例如“我想做一条 AI 视频，但不知道先干嘛”。
2. 展示 AI 把它拆成任务清单：目标、素材、字段、时间线、报告、验收标准。
3. 展示 Codex 接收任务或生成文件的干净片段，只保留任务清单和产物路径，隐藏侧栏、用户名、桌面、截图文件名。
4. 补录一个最终报告/索引的静态结果页，证明“拆任务后能落成文件”，不要展示 API、key、token、私密路径。
5. 如果坚持用现有素材，优先用 `material_04 + material_02`，少用 `material_03`。

## 11. 给 ChatGPT 的写稿建议

建议 ChatGPT 后续不要直接写“全自动制作方式公开”。

更稳的文案方向：

- 主题：`我用 AI 做视频，第一步不是写文案，而是拆任务`
- 口径：从一次真实需求出发，展示 AI 如何把模糊想法拆成可执行任务、字段、报告和验收标准。
- 账号价值：非技术人也能判断 AI 有没有开始干活，不是看回答多漂亮，而是看它有没有把下一步拆清楚。
- 平台安全表达：少说“全自动 / 自动流 / 一键复制”，多说“真实工作流复盘 / 减少重复步骤 / 拆任务执行单”。
- 证据边界：这批素材证明“拆任务过程”，不证明“自动成片能力已经成熟”。

如果只做 60-90 秒视频，建议用 3 个片段：

1. `material_04 00:55-01:30`：AI 先确认事实和方向，不是直接写稿。
2. `material_02 00:20-01:50`：从 prompt 拆成配置、字段、模板、报告、变量和 DoD。
3. `material_01 01:04-01:28` 或 `material_04 01:30-01:50`：收束到“先判断下一步，再做文案/剪辑”。

## 12. 下一步建议

`已确认` 本轮可以把第四期素材交给 ChatGPT 做下一轮写稿判断。

`待验证` 进入正式视频执行前，还需要 ChatGPT / 用户确认：

- 是否采用“第一步不是写文案，而是拆任务”作为主标题方向。
- 是否允许弱化或删除“全自动 / 自动流 / 公开制作方式”等高风险词。
- 是否补录干净的任务拆解窗口。
- 是否把 `material_03` 完全排除出公开视频，只作为内部证据。

本轮不生成最终文案，不生成视频，不生成正式下一条视频执行 prompt。

## ChatGPT 快速写稿输入包

### 推荐主标题方向

`我用 AI 做视频，第一步不是写文案，而是拆任务`

备选：

- `为什么你用 AI 总是废话？因为你给的是一句糊话，不是任务单`
- `我让 AI 写文案之前，先让它把任务拆清楚`

### 推荐开头证据

优先用 `material_04 00:55-01:30`：

- AI 没有直接写文案，而是先确认 V002/V004 是否入库、系统是否能做方向判断。
- 明确“自动流 / 全自动”风险更高，“一句糊话变执行单”更安全。

### 推荐中段证据

优先用 `material_02 00:20-01:50`：

- 从用户一个 prompt，拆成用户可定制区、数据字段、目录结构、文案记录机制、变量复盘和报告结构。
- 这段最能证明“拆任务”不是抽象口号。

### 推荐结尾判断

用 `material_01 01:04-01:28` 或 `material_04 01:50-01:54`：

- 下一步不是马上写一条新文案，而是先决定验证哪个主变量。
- 本轮素材已经足够支持 ChatGPT 写一版候选脚本，但还不等于正式执行 ready。

### 不能写的内容

- 不能写“AI 已经自动做完整条视频”。
- 不能写“全自动制作方式已安全公开”。
- 不能写“复制这个 prompt 就能复刻账号系统”。
- 不能写“V002/V004 证明方向成立”。
- 不能写“有私信 / 咨询 / 客资 / 成交”。

### 需要用户确认的内容

- 是否保留“全自动”相关说法，还是统一改成“真实工作流复盘 / 一句话拆任务执行单”。
- 是否补录一段更干净的“模糊想法 -> 任务清单 -> 产物验收”窗口。
- 是否公开视频中完全避开 `material_03`。

## 状态边界

```yaml
new_video_generated: false
published_video_modified: false
final_copy_written: false
formal_next_video_prompt_generated: false
content_validation_advanced: false
send_ready_advanced: false
publish_candidate_advanced: false
current_data_goal_anchor_ready_advanced: false
source_media_committed: false
skill_used: "skills/视频素材解析_video_material_audit/SKILL.md"
```
