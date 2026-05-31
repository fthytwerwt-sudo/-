# Guided Proof Video 剪辑工具链补齐报告

## 1. toolchain_bootstrap_report

```yaml
task_id: 20260531_guided_proof_toolchain_bootstrap
project_route: video_factory
status: completed_toolchain_bootstrap_synced
not_publish_candidate: true
video_generated: internal_toolchain_validation_only
current_video_modified: false
external_api_called: false
secret_read: false
status_promoted: false
minimum_guided_proof_ready: true
```

## 2. runtime_audit

| item | result |
| --- | --- |
| `macos_version` | `macOS 26.2 / Build 25C56` |
| `node_version` | `v25.6.1` |
| `npm_version` | `11.9.0` |
| `pnpm_status` | `missing` |
| `remotion_system_requirement_risk` | `passed`，当前环境满足 Remotion 官方 Node 16+ / macOS 15+ 最低要求 |

## 3. installed_dependencies

### npm_dependencies

| package | version |
| --- | --- |
| `@remotion/cli` | `4.0.469` |
| `@remotion/captions` | `4.0.469` |
| `@remotion/media` | `4.0.469` |
| `@remotion/renderer` | `4.0.469` |
| `remotion` | `4.0.469` |
| `react` | `19.2.6` |
| `react-dom` | `19.2.6` |
| `ffmpeg-static` | 保留既有依赖 |

### python_dependencies

| package | version / status |
| --- | --- |
| `numpy` | `2.0.2` |
| `opencv-python` | `4.13.0.92` |
| `pysubs2` | `1.8.1` |
| `cairosvg` | `2.8.2` |
| `pillow` | `11.3.0` |
| `cairo` system library | Homebrew `cairo 1.18.4` installed for CairoSVG runtime |

## 4. modified_files

| path | change |
| --- | --- |
| `package.json` | preserved existing `check` script and added Remotion scripts / dependencies |
| `package-lock.json` | locked Node dependency tree |
| `requirements-video-toolchain.txt` | added Python visual dependency list |
| `remotion/index.tsx` | added Remotion entrypoint |
| `remotion/Root.tsx` | added still + 5s composition registry |
| `remotion/GuidedProofToolchain.tsx` | added minimal guided proof test composition |
| `scripts/视频剪辑工具链自检_check_guided_proof_toolchain.py` | added one-command self-check and JSON status writer |
| `scripts/视频剪辑工具链安装_bootstrap_guided_proof_toolchain.sh` | added repeatable bootstrap runner |
| `dist/toolchain_validation/*` | added validation outputs |
| `codex_log/latest.md` | added latest handoff entry |

## 5. generated_outputs

| output | status |
| --- | --- |
| `dist/toolchain_validation/remotion_still.png` | generated, `1920x1080 PNG` |
| `dist/toolchain_validation/remotion_5s.mp4` | generated, `1920x1080 / 30fps / 5.056s / h264 + aac` |
| `dist/toolchain_validation/toolchain_status.json` | generated, `minimum_guided_proof_ready = true` |

## 6. remotion_validation

- `npx --no-install remotion versions` passed.
- `npm run vf:remotion:still` passed.
- `npm run vf:remotion:render5s` passed.
- Still visual readback passed: nonblank 16:9 frame with `low_density_bridge_card / clean_evidence_container / subtitle_safe_zone / one_claim_one_highlight / split_screen_placeholder`.

## 7. ffmpeg_validation

- `ffmpeg -version` passed: `ffmpeg 8.1`.
- `ffprobe -version` passed: `ffprobe 8.1`.
- `ffprobe` on `dist/toolchain_validation/remotion_5s.mp4` passed:
  - video: `h264 / 1920x1080 / 30fps / 150 frames / 5.000s`
  - audio: `aac / stereo / 5.056s`
  - container: `mov,mp4,m4a,3gp,3g2,mj2`

## 8. ass_validation

`ass_ready = false`。

当前 Homebrew FFmpeg 未暴露 `ass` / `subtitles` filter，也未显示 `--enable-libass`。这不阻断本轮 Remotion 主路线，当前字幕主策略为：

```yaml
remotion_caption_layer_primary: true
ass_role: fallback_only_not_primary
ass_ready: false
```

## 9. python_validation

Python 视觉 import check passed through the self-check runtime path:

| module | status |
| --- | --- |
| `cv2` | ok |
| `numpy` | ok |
| `pysubs2` | ok |
| `cairosvg` | ok |
| `PIL` | ok |

说明：系统 `python3` 需要在进程内设置 `/opt/homebrew/lib` 供 CairoSVG 找到 Homebrew `cairo` dylib；自检脚本已内置该处理，不读取 `.env` 或 secret。

## 10. minimum_guided_proof_ready

```yaml
remotion_ready: true
ffmpeg_ready: true
ass_ready: false
python_visual_ready: true
minimum_guided_proof_ready: true
blocked_if: []
```

## 11. remaining_risks

- `ASS burn-in` 未就绪；若未来必须走 FFmpeg/ASS 压字幕，需要另换带 `--enable-libass` 的 FFmpeg build。
- `pnpm` 仍未安装；当前项目以 `npm` 为可用包管理器。
- 本轮只验证工具链最小承载能力，不代表下一条 30-45 秒真实证据片段已经审美通过。
- 本轮生成的是 `internal_toolchain_validation_only`，不是正式发布候选片。

## 12. future_usage

后续 Codex 进入剪辑前，先跑：

```bash
npm run vf:toolchain:check
```

如需重建最小工具链，可跑：

```bash
scripts/视频剪辑工具链安装_bootstrap_guided_proof_toolchain.sh
```

如需只验证 Remotion：

```bash
npm run vf:remotion:still
npm run vf:remotion:render5s
```

下一步可以进入 `30-45s guided proof validation`，但必须先有 `locked_copy_contract / material_parse_pack / script_to_timeline_map / current_data_goal_anchor / visual_style_decision / active_evidence_window_map`。
