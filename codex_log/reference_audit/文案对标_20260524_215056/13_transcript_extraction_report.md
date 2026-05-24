# 13 Transcript Extraction Report｜逐字稿提取状态报告

## transcript_status

```text
transcript_status = blocked_local_asr_missing
partial_visible_text_available = true
audio_extract_status = passed
full_transcript_generated = false
full_transcript_commit_allowed = false
full_transcript_committed = false
external_api_called = false
```

## Source And Previous Audit

- reference_video: `/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`
- previous_reference_audit_dir: `codex_log/reference_audit/文案对标_20260524_215056/`
- previous_transcript_confidence: `partial`
- current_goal: 尽可能提取逐字稿，并补充话语口味 / 逐字表达方式分析。

## Audio Extract Status

- audio_output_local_only: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/reference_audio.wav`
- audio_duration_seconds: `416.750313`
- audio_codec: `pcm_s16le`
- audio_sample_rate: `16000`
- audio_channels: `1`
- audio_committed_to_git: `false`

## ASR / OCR Tool Status

| tool | status |
| --- | --- |
| `whisper` CLI | missing |
| `whisper-cpp` CLI | missing |
| `whisper.cpp main` | missing / not detected |
| `python whisper` | missing |
| `python faster_whisper` | missing |
| `python mlx_whisper` | missing |
| `python funasr / vosk / speech_recognition` | missing |
| `tesseract / pytesseract / cv2` | missing |
| `PIL` | available, but not OCR |

## Full Transcript Boundary

- `FULL_TRANSCRIPT_COMMIT_ALLOWED = false`
- 完整逐字稿本轮未生成。
- 即使后续生成完整逐字稿，默认也只能存入 local-only 目录，不能提交 GitHub；除非用户明确确认 reference 视频为自有或已授权。
- 本轮仓库只提交：转写状态、短引用片段、话语机制分析、改稿建议和 ChatGPT handoff。

## Local-only Outputs

- audio_extract_report: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/audio_extract_report.md`
- asr_tool_report: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/asr_tool_report.md`
- transcript_blocked_report: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/transcript_blocked_report.md`
- visible_text_crosscheck: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/visible_text_crosscheck.md`
- partial_visible_text_segments: `/Users/fan/Documents/视频工厂/本地仅分析_local_only/reference_transcripts/文案对标_20260524_221353/partial_visible_text_segments.json`

## Visible Text Crosscheck Summary

| timestamp | visible text / card | function | ASR crosscheck |
| --- | --- | --- | --- |
| 00:00-00:08 | 朋友们 / 0门槛拥有自己的高级AI军师 | opening_hook | `not_available_no_local_asr` |
| 00:25-00:45 | 问题一：买房方案 | problem_card | `not_available_no_local_asr` |
| 00:45-01:25 | 快速模式 / 思考模式 / 专家模式 | mode_comparison | `not_available_no_local_asr` |
| 02:05-02:55 | 快速 / 思考 / 专家；先搜一圈 / 把利弊讲清楚 | judgment_comparison | `not_available_no_local_asr` |
| 02:55-03:35 | 问题二：装修方案；预算表 / 清单表 | result_table | `not_available_no_local_asr` |
| 04:35-05:15 | 问题三：论文研究 | scope_expansion | `not_available_no_local_asr` |
| 05:45-06:20 | 不只是程序员专属 / 生活工作都能用 | boundary | `not_available_no_local_asr` |

## Main Uncertain Parts

- 全片口播逐字内容无法本地自动转写。
- 主播衔接句、语气词、停顿、笑点和细微转折无法做逐字级校验。
- 音效与口播的精确对齐只能基于上一轮视觉 / 音频节奏分析，不能写成逐帧声画对齐结论。

## Confidence

- audio_extraction_confidence: `high`
- full_transcript_confidence: `blocked_not_generated`
- visible_text_confidence: `medium`
- copy_taste_analysis_confidence: `medium`，来自可见文本、上一轮时间线和同目录文案口味样本。
