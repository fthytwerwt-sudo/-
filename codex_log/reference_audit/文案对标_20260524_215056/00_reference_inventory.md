# 00 Reference Inventory｜文案对标

- generated_at: `2026-05-24T21:50:56`
- requested_path: `/Users/fan/Documents/视频工厂/文案库/文案对标`
- resolved_path: `/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`
- source_root: `/Users/fan/Documents/视频工厂/文案库`
- primary_reference_video: `/Users/fan/Documents/视频工厂/文案库/文案对标.MP4`
- reference_file_count: `3`
- skill_used: `skills/视频素材解析_video_material_audit/SKILL.md` + `video-metadata-probe`
- boundary: 原始视频 / 文案库源文件只读，不提交。

## inventory

| file_id | relative_path | file_type | size_bytes | duration_seconds | modified_time | primary_candidate | deep_audit | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R001 | 文案库/文案对标.MP4 | video/mp4 | 373998641 | 416.740114 | 2026-05-24T21:12:50 | True | True | 唯一名称包含“文案对标”的视频文件；位于文案库；体积最大且时长最长；进入深度解析。 |
| R002 | 文案库/喜欢 txt.txt | text/plain | 65688 |  | 2026-04-13T22:13:21 | False | False | 同目录文案喜好文本，作为 secondary reference context；不当作主视频 transcript。 |
| R003 | 文案库/不喜欢.txt | text/plain | 16272 |  | 2026-04-13T23:36:19 | False | False | 同目录文案喜好文本，作为 secondary reference context；不当作主视频 transcript。 |

## secondary text context

- `喜欢 txt.txt`: `10` 条喜欢样本文案，作为文案口味和结构偏好参考，不等于本 MP4 的完整 transcript。
- `不喜欢.txt`: `10` 条不喜欢样本文案，作为风险和反例参考。

## impact check

- `已确认` 本轮输出影响 reference pack、Reference-to-Execution Contract、ChatGPT 后续新第四期长文案、Codex 后续视频执行前参考规则。
- `已确认` 本轮不影响当前成片状态、数据目标锚点 ready、内容验证状态、发送状态。
- `已确认` 当前工作区有 unrelated dirty changes；提交必须 path-limited。
- `已确认` 对标视频只能提取结构、节奏、机制、风格原则，不能复用原始画面、人物、音频、BGM、音效、logo、字体或特定资产。
