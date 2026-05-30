# Remotion / FFmpeg / ASS / 阿里 API 剪辑工具链审计报告 Toolchain Audit Report

## 1. route_decision

```yaml
route_decision:
  project_route: video_factory
  task_type:
    - review_diagnosis_audit
    - local_file_governance
    - video_sample_or_assembly_preflight
  responsibility_layer:
    - entry_routing_layer
    - validation_layer
    - sync_layer
  large_task_gate:
    triggered: true
    reason:
      - 本轮同时涉及 Remotion / FFmpeg / ASS / Python / API 素材边界 / 日志同步
      - 本轮只做审计与决策，不生成视频
    lane_recommendation: explore_plus_integrate
    write_owner: Codex
    read_only_lanes:
      - local_toolchain_probe
      - repo_structure_scan
      - reference_decision_pack_review
    integration_owner: Codex
  deepseek_supply_gate:
    supply_request_created: true
    deepseek_actual_participation: not_attempted_policy_constraint
    fallback_status: fallback_local_only
    not_deepseek_conclusion: true
    reason: 用户本轮禁止外部 API 调用、secret 读取和大任务重执行
  execution_permission: granted_for_readonly_audit_and_log_sync_only
```

### read_status

| file | status | use |
| --- | --- | --- |
| `AGENTS.md` | read_ok | 多项目路由、route_decision、日志 / Git 同步边界 |
| `codex_source/00_codex_readme.md` | read_ok | 当前正式接手口径 |
| `codex_log/latest.md` | read_ok | 最新剪辑参考解析状态 |
| `GPT数据源/08_当前正式事实.md` | read_ok | 正式运营边界、不可推进状态字段 |
| `GPT数据源/05_文案路由规则.md` | read_ok | `script_to_timeline_map`、卡片、API 素材和剪辑决策链 |
| `GPT数据源/07_AI知识类视频价值规则.md` | read_ok | 真实证据、字幕 / 卡片遮挡、API 图边界 |
| `GPT数据源/11_项目状态动作总控器_机制推理层.md` | read_ok | 状态动作与同步规则 |
| `codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/deep_reference_reparse_report.md` | read_ok | `guided proof video` 目标语言 |
| `codex_log/reference_analysis/20260531_剪辑参考深度重解析_deep_editing_reference_reparse/editing_decision_pack_for_next_round.md` | read_ok | 下一轮 30-45 秒验证输入与阻断条件 |
| `Remotion skill rules/subtitles.md` | read_ok | Remotion 字幕数据结构为 JSON Caption |
| `Remotion skill rules/ffmpeg.md` | read_ok | Remotion 内部 FFmpeg/FFprobe 与裁剪建议 |

## 2. remotion_audit

### 已确认

| check | result |
| --- | --- |
| `node -v` | `v25.6.1` |
| `npm -v` | `11.9.0` |
| `pnpm -v` | missing: `command not found: pnpm` |
| `npx --no-install remotion --version` | failed: `npm error could not determine executable to run` |
| `npm list remotion --depth=0` | empty |
| `npm list '@remotion/*' --depth=0` | empty |
| `node_modules` | missing |
| root `package.json` | only declares `ffmpeg-static` |
| `remotion.config.*` | not found |
| root `src/` or `remotion/` app dir | not found |
| `scripts/*remotion*` | not found |
| repo reference | `dist/reference_analysis_vlog_20260527/combined/remotion_feasibility_matrix.md` exists as historical analysis |

### readiness

`Remotion` 当前是 `not_installed_not_runnable`。本机 Node/npm 可用，但仓库没有 Remotion project scaffold、没有 Remotion 依赖、没有 local CLI、没有 `node_modules`。因此下一轮不能直接承诺 Remotion 渲染；必须先安装依赖或建立最小 Remotion composition，再做 `still / short clip` 验证。

## 3. ffmpeg_ass_audit

### 已确认

| check | result |
| --- | --- |
| `which ffmpeg` | `/opt/homebrew/bin/ffmpeg` |
| `ffmpeg -version` | `ffmpeg version 8.1` |
| `which ffprobe` | `/opt/homebrew/bin/ffprobe` |
| `ffprobe -version` | `ffprobe version 8.1` |
| `ffmpeg -hide_banner -filters | rg '(ass|subtitles)'` | no match |
| `ffmpeg -hide_banner -buildconf | rg 'libass'` | no match |

### decision

`FFmpeg / FFprobe` 可用于 probe、抽帧、裁剪、转码、重封装、音视频 mux 和最终基础媒体校验。
`ASS / subtitles burn-in` 当前为 `not_ready`：现有 Homebrew FFmpeg 未显示 `--enable-libass`，也未暴露 `ass` / `subtitles` filter。若下一轮要用 ASS 作为最终字幕层，必须先换成带 `libass` 的 FFmpeg build 并复验 filter。

## 4. python_visual_tool_audit

### 已确认

| check | result |
| --- | --- |
| `python3 --version` | `Python 3.9.6` |
| `Pillow` | installed `11.3.0` |
| `OpenCV / cv2` | missing |
| `numpy` | missing |
| `pysubs2` | missing |
| `CairoSVG` | missing |

### readiness

Python 当前只能承担轻量静态图处理、contact sheet、简单占位图或 JSON/报告类工作。
需要帧级视觉检测、区域裁剪、运动/清晰度检测、字幕格式转换或 SVG 渲染时，应先补 `numpy / opencv-python / pysubs2 / cairosvg`，并在项目内固定版本和验证命令。

## 5. aliyun_api_asset_decision

### 已确认

本轮未调用阿里 / 百炼 / 图片 / 视频 / TTS 外部 API，未读取 `.env`、API key、token 或 secret。

### decision

`阿里 API / API 生成素材` 只能作为辅助表达层，不作为真实证据层：

- 可用：开头 / 转场 / 结尾的 `api_generated_human`，小向导、背景、图标、氛围图、非证据桥接素材。
- 不可用：中段核心证据、用户录屏替代、真实平台数据替代、Prompt / 表格 / 按钮 / 聊天证据替代。
- 中文可读文字默认由后期卡片 / Remotion / ASS / subtitle layer 生成，不交给图片模型直接生成。
- 真实证据不足时，默认路线是删改文案、补录、降级为信息卡或 blocked，不用 API 图补证据缺口。

## 6. tool_routing_decision

| layer | primary tool | current decision |
| --- | --- | --- |
| `guided proof video` 画面编排 | Remotion | 推荐主栈，但当前未安装；负责 16:9 composition、evidence container、labels、highlights、split screen、bridge card、caption safe zone |
| 字幕注意力引导 | Remotion JSON captions first | 当前优先做 Remotion caption layer；ASS 作为兼容 / fallback，不作为当前可用主线 |
| ASS 字幕压制 | FFmpeg + libass | 当前不可用；需补带 libass 的 FFmpeg 后再选 |
| 媒体 probe / mux / trim / transcode | FFmpeg / FFprobe | 当前可用 |
| 帧级分析 / 截图 / 图片预处理 | Python | Pillow 可用；OpenCV/numpy 缺失，复杂视觉判断未就绪 |
| API 生成素材 | Aliyun API | 只可做非证据辅助素材；本轮不调用 |

短结论：下一轮应先补 Remotion 最小可渲染链路；FFmpeg 保留为媒体处理和 mux；ASS 不作为首选，除非先修 libass；Python 只在补齐视觉库后承担帧级辅助。

## 7. installation_recommendation

### priority_1_remotion_minimal_stack

目的：验证 `guided proof video` 的屏幕语言，而不是先做最终成片。

建议在用户确认安装后补：

```bash
npm install react react-dom remotion @remotion/media @remotion/captions @remotion/renderer
```

然后建立最小 16:9 composition，先跑 still / 5 秒片段，不直接改当前正片。

### priority_2_ffmpeg_libass_or_keep_remotion_captions

如果字幕最终要 ASS burn-in，则需要安装或切换到带 `--enable-libass` 的 FFmpeg，并复验：

```bash
ffmpeg -hide_banner -filters | rg '(^|\\s)(ass|subtitles)(\\s|$)'
ffmpeg -hide_banner -buildconf | rg 'libass'
```

如果下一轮先用 Remotion caption layer 渲染字幕，则可以暂缓 ASS。

### priority_3_python_visual_helpers

建议后续用项目内 venv 固定：

```bash
python3 -m pip install pillow numpy opencv-python pysubs2 cairosvg
```

当前 Pillow 已有；其余缺失。安装后必须跑 import check 和一个最小图像读写 / subtitle parse 验证。

### optional_pnpm

`pnpm` 当前缺失，但 `npm` 可用。除非项目决定统一包管理器，否则不是第一优先级。

## 8. next_validation_plan

下一轮 30-45 秒验证建议：

1. 锁输入：`locked_copy_contract / material_parse_pack / script_to_timeline_map / current_data_goal_anchor / visual_style_decision / active_evidence_window_map`。
2. 安装并验证 Remotion 最小栈：本地 CLI 可运行、composition 可加载、`still` 可渲染。
3. 做 30-45 秒 `guided proof` 片段：`active_evidence_window + subtitle_safe_zone + one_claim_one_highlight + context_bridge_card`。
4. 产出 review pack：before/after 对比、字幕/卡片遮挡报告、split readability、evidence safety、FFprobe 结果。
5. 人审通过后再决定是否扩展到整片；未通过则只修视觉语言，不推进 `content_validation / send_ready`。

## 9. status_boundary

- `video_generated = false`
- `current_video_modified = false`
- `external_api_called = false`
- `secret_read = false`
- `dependency_installed = false`
- `content_validation_changed = false`
- `send_ready_changed = false`
- `publish_status_changed = false`
- `voice_validation_changed = false`
- `visual_master_locked_changed = false`
- `status_label = local_toolchain_audit_ready_for_git_sync`

## 10. git_sync

本报告写入时的 Git 同步状态由本轮最终回报给出。
本轮允许同步文件限于：本报告、manifest、供料任务卡、日期日志与 `codex_log/latest.md`。
