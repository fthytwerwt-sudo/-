# vNext 最新素材采集汇报 vnext material intake report

## 1. 范围与边界

- `已确认` 本轮工作区：`/Users/fan/Documents/视频工厂`
- `已确认` 本轮分支：`codex/vnext-recorded-material-intake-20260503`
- `已确认` 本轮只扫描用户指定目录：`/Users/fan/Documents/视频工厂/素材录制/最新素材`
- `已确认` 本轮只做素材发现、素材检查、时间码拆解、证据点整理和给 ChatGPT / 后续云端总装验证的素材事实包。
- `已确认` 本轮未调用阿里云 OSS / ICE，未生成云端样片，未剪正式视频，未修改 v3.1 正片，未修改 `dist/latest_review_pack/`。
- `已确认` 本轮未修改 `content_validation` / `send_ready`。

## 2. 读取依据

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md`
- `验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/阿里云剪辑复接验证报告_after_audit_aliyun_editing_reconnect_validation_report.md`
- `codex_log/current_local_artifact_paths.md`
- `video-metadata-probe` global skill：`/Users/fan/.codex/skills/video-metadata-probe/SKILL.md`

`已确认` 仓库本地 `skills/` 目录不存在；相关视频元数据 skill 回退使用全局 `~/.codex/skills/video-metadata-probe`。

## 3. 素材目录检查

- 指定路径存在：`已确认`
- 是否只扫描该路径：`已确认`
- 目录文件数：`7`
- 候选素材数：`6`
- 忽略文件：`.DS_Store`

候选素材：

| 文件 | 类型 | 大小 | 时长 | 分辨率 | 音频 | 解码 |
| --- | --- | ---: | ---: | --- | --- | --- |
| `codex 素材.mp4` | mp4 | 481.87 MiB | 04:04.32 | 3420x2214 / 60fps | AAC | 全片解码通过 |
| `trae 素材.mp4` | mp4 | 269.00 MiB | 02:40.57 | 3420x2214 / 60fps | AAC | 全片解码通过 |
| `创建文件夹.mp4` | mp4 | 13.64 MiB | 00:39.20 | 2830x1654 / 60fps | AAC | 全片解码通过 |
| `豆包素材.mp4` | mp4 | 666.81 MiB | 04:56.17 | 3420x2214 / 60fps | AAC | 全片解码通过 |
| `火山引擎素材.mp4` | mp4 | 214.21 MiB | 01:53.63 | 3420x2214 / 60fps | AAC | 全片解码通过 |
| `录屏2026-04-30 03.25.28.mov` | mov | 6.85 GiB | 106:00.28 | 3420x2214 / 60fps | 无 | 开头 / 中段 / 末段抽样解码通过，未做 106 分钟全片解码 |

## 4. 新素材识别

### 用户新录制素材候选

`已确认` 以下文件修改时间为 2026-05-02 晚间，且在用户指定“最新素材”目录中：

- `codex 素材.mp4`
- `trae 素材.mp4`
- `创建文件夹.mp4`
- `豆包素材.mp4`
- `火山引擎素材.mp4`

### 候选 / 历史参考素材

- `录屏2026-04-30 03.25.28.mov`
  - `部分成立` 它位于最新素材目录，但修改时间是 2026-04-30，文件名也是 2026-04-30 录屏。
  - `已确认` 它是 106 分钟长录屏，无音轨，画面更像历史 ChatGPT / QuickTime 复审场景。
  - `判断` 不默认当成本轮新录制素材，只列为历史 / 参考候选，待用户确认。

## 5. 素材可用性判断

| 文件 | 用户录制素材段 | 卡片段 | 音轨 | 参考 | 关键风险 |
| --- | --- | --- | --- | --- | --- |
| `trae 素材.mp4` | 推荐 | 不适合 | 仅嵌入音频参考 | 可参考 | 可见本机路径和代码，未发现 key/token |
| `豆包素材.mp4` | 可用 | 不适合 | 仅嵌入音频参考 | 可参考 | 可见历史会话标题，未发现 key/token |
| `codex 素材.mp4` | 可用 | 不适合 | 仅嵌入音频参考 | 可参考 | 可见 Git / 文件变更列表，需控制展示边界 |
| `创建文件夹.mp4` | 可作 B-roll | 不适合 | 仅嵌入音频参考 | 可参考 | 可见历史项目目录名 |
| `火山引擎素材.mp4` | 未打码前不建议 | 不适合 | 仅嵌入音频参考 | 仅内部参考 | 出现手机号、短信验证码、API Key 管理页和资源 ID 痕迹 |
| `录屏2026-04-30 03.25.28.mov` | 不推荐 | 不适合 | 不适合 | 历史参考 | 旧长录屏、无音轨、体积过大 |

## 6. 时间码证据摘要

### `豆包素材.mp4`

- `0-8s`：豆包首页，“有什么我能帮你的吗？”以及 `PPT 生成 / 图像生成 / 帮我写作 / 视频生成` 等入口。
- `8-16s`：输入框聚焦，进入参考模式。
- `16-24s`：用户输入并提交“我想用 trae 做一个短视频自动流...”。
- `120-136s`：豆包输出总控智能体、选题 Agent、编剧 Agent、分镜 Agent、视频生成 Agent、后期 Agent、发布 Agent 等短视频自动化方案。
- 能证明：用户真实提出短视频自动化需求，豆包给出结构化方案。
- 不能证明：方案已工程跑通、云剪稳定、内容有效。

### `trae 素材.mp4`

- `0-8s`：Trae / SOLO Coder 打开，右侧文件缺失提示。
- `8-16s`：Markdown 预览标签打开。
- `16-24s`：进入 Builder 协作入口。
- `120-136s`：Trae 生成 `vlog_automation_workflow` 项目结构和 Python 代码，右侧文件树可见 `modules / templates / workflows`。
- 能证明：AI IDE / SOLO Coder 正在执行项目生成任务。
- 不能证明：代码已运行成功、完整链路稳定。

### `codex 素材.mp4`

- `0-8s`：Codex / ChatGPT 类界面处理“录入 V001 24h 截图数据”，文字提到 HyperFrames 透明层。
- `8-16s`：文字提到预合成底片、呼吸框、箭头、小标签。
- `16-24s`：滚动到 MOV 透明层正在渲染、读取 render log。
- `176-188s`：右侧显示分支详情、Git 操作、生成文件列表；正文提到 ffprobe、alpha MOV、透明层导出。
- 能证明：Codex 在执行视频工厂任务，有 Git / 文件变更 / HyperFrames 技术处理痕迹。
- 不能证明：云剪稳定、内容过线、正式片可发。

### `创建文件夹.mp4`

- `0-8s`：Finder 打开“文稿”，可见多个项目文件夹。
- `8-16s`：出现“未命名文件夹”。
- `16-24s`：选中新文件夹并开始重命名。
- 能证明：用户在整理项目文件夹。
- 不能证明：AI 工作流执行或云端总装。

### `火山引擎素材.mp4`

- `0-8s`：火山引擎 ArkClaw 登录页。
- `8-16s`：账号输入框出现手机号。
- `16-24s`：切换手机号登录。
- `60-72s`：火山方舟 API Key 管理页，可见 key 以星号遮挡、资源 ID 和操作按钮。
- 能证明：云平台入口和 API Key 管理页面存在。
- 不能证明：阿里云 OSS / ICE 链路存在，不能证明云剪总装稳定。
- 风险：未打码不得入片。

### `录屏2026-04-30 03.25.28.mov`

- `0-8s`：QuickTime 播放旧竖屏视频，旁边是 ChatGPT 页面，出现 v2_full.mp4、contact sheet、round34 等历史复审信息。
- `8-16s`：继续讨论剪辑 / 放大位置等问题。
- `16-24s`：ChatGPT 页面显示历史复审判断和下一目标。
- 能证明：历史复审过程存在。
- 不能证明：本轮新素材、vNext 云端总装准备完成。

## 7. 推荐给后续云端总装验证的素材组合

`部分成立`：如果后续总装任务允许生成轻量卡片占位和静音占位，则可以进入 vNext 最小云端总装验证；如果要求所有素材都必须来自最新素材目录，则当前缺卡片文件和独立音轨。

### user_recording_segment

- 推荐素材路径：`/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4`
- 推荐截取：`120.0s-136.0s`
- 为什么选它：画面最清楚地展示 AI IDE 正在生成项目结构和代码，隐私风险低，能承接“用户录制素材”。

### card_segment_1

- 推荐素材路径：`待后续任务生成`
- 推荐使用时长：`4s`
- route 类型：`cute_info_card_route`
- 为什么选它：最新目录没有卡片文件；结果差 / 工作流价值信息卡应按 v3.1 规则走 `cute_info_card_route`。

### card_segment_2

- 推荐素材路径：`待后续任务生成`
- 推荐使用时长：`4s`
- route 类型：`sassy_reaction_card_route`
- 为什么选它：若要测试三类卡片兼容，骚萌卡必须走 `sassy_reaction_card_route`，不得套信息卡外壳。

### audio_segment

- 推荐素材路径：`无独立音轨；可使用静音占位`
- 推荐截取：不适用
- 是否可以使用静音占位：`可以，限于最小云端总装技术验证`
- 说明：最新目录没有独立 mp3/wav/aac。若必须测试真实音轨容器，可从 `trae 素材.mp4` 的 `120.0s-136.0s` 抽取嵌入 AAC，但不能写成最终旁白或 TTS 验证通过。

## 8. 风险与补录建议

`部分成立`：用户录制素材足够进入最小总装验证；卡片文件和独立音轨不足。

最多 3 个补录 / 补齐项：

1. 补一个不含隐私的云平台 / 云剪入口短录屏，避免使用 `火山引擎素材.mp4` 的手机号和验证码画面。
2. 补或生成两张轻量卡片素材：一张 `cute_info_card_route`，一张 `sassy_reaction_card_route`。
3. 若后续不接受静音占位，补一条 15-30 秒测试旁白或允许后续任务临时生成静音音轨。

## 9. 状态边界

- `已确认` 本轮未生成可交付视频。
- `已确认` 本轮未生成可交付音频。
- `已确认` 本轮未生成可交付图片；只读检查中使用的临时抽帧不作为交付物，不进入 Git。
- `已确认` 本轮未修改 v3.1 正片。
- `已确认` 本轮未修改 `content_validation` / `send_ready`。
- `已确认` 本轮不提交新录制素材本体，不提交大视频 / 大图片 / 大音频。

## 10. 下一个目标

交给 ChatGPT 判断当前素材是否足够进入 vNext 最小云端总装验证；若足够，再由后续阿里云云端总装验证任务读取：

- `素材检查_reports/20260503_vNext素材采集汇报_vnext_material_intake/recommended_assembly_inputs.json`
