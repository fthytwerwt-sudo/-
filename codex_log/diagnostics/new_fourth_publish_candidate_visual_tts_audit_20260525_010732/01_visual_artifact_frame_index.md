# 视觉异常抽帧索引

## 抽帧方式

- inspected_video: `/Users/fan/Documents/视频工厂/dist/new_fourth_episode_selection_publish_candidate_20260525_001803/full.mp4`
- local_only_frame_dir: `/tmp/new_fourth_visual_tts_audit_20260525_005746`
- local_only_contact_sheet: `/tmp/new_fourth_visual_tts_audit_20260525_005746/full_contact_sheet_local_only.jpg`
- local_only_comparison_sheet: `/tmp/new_fourth_visual_tts_audit_20260525_005746/final_vs_intermediate_contact_sheet_local_only.jpg`
- commit_policy: 不提交截图 / contact sheet / 媒体文件，只提交时间码与诊断结果。

## 异常时间码概览

- whiteout / washout affected_timecodes: `5s, 15s, 25s, 32s, 42s, 55s, 68s, 78s, 88s, 96s, 106s, 120s, 132s, 145s, 155s, 170s, 184s, 198s, 215s, 230s, 245s`
- right_top_black_block affected_timecodes: `5s, 15s, 25s, 32s, 42s, 55s, 68s, 78s, 88s, 96s, 120s, 132s, 145s, 155s, 170s, 184s, 198s, 215s, 230s, 245s`
- gray_border_or_band affected_timecodes: `5s, 15s, 25s, 32s, 42s, 55s, 68s, 78s, 88s, 96s, 106s, 120s, 132s, 145s, 155s, 170s, 184s, 198s, 215s, 230s, 245s`

## 帧级指标表

说明：`center_bright` / `grid_bright` 越接近 1，越接近白屏 / 洗白；`right_top_dark` 越高，右上角黑块越明显。

| timecode | symptom | center_bright | grid_bright | right_top_dark | origin_judgment |
| --- | --- | --- | --- | --- | --- |
| 005.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.863 | 0.985 | 0.454 | render pipeline added issue; see intermediate/source comparison |
| 015.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.932 | 0.985 | 0.454 | render pipeline added issue; see intermediate/source comparison |
| 025.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.933 | 0.984 | 0.454 | render pipeline added issue; see intermediate/source comparison |
| 032.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.883 | 0.958 | 0.205 | render pipeline added issue; see intermediate/source comparison |
| 042.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.933 | 0.984 | 0.454 | render pipeline added issue; see intermediate/source comparison |
| 055.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.932 | 0.985 | 0.454 | render pipeline added issue; see intermediate/source comparison |
| 068.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.934 | 0.985 | 0.199 | render pipeline added issue; see intermediate/source comparison |
| 078.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.863 | 0.986 | 0.454 | render pipeline added issue; see intermediate/source comparison |
| 088.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.874 | 0.983 | 0.160 | render pipeline added issue; see intermediate/source comparison |
| 096.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.881 | 0.912 | 0.550 | render pipeline added issue; see intermediate/source comparison |
| 106.00s | whiteout / washout, gray_edge_or_band | 0.920 | 0.749 | 0.759 | render pipeline added issue; see intermediate/source comparison |
| 120.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.986 | 0.973 | 0.124 | render pipeline added issue; see intermediate/source comparison |
| 132.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.904 | 0.948 | 0.215 | render pipeline added issue; see intermediate/source comparison |
| 145.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.974 | 0.933 | 0.229 | render pipeline added issue; see intermediate/source comparison |
| 155.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.903 | 0.987 | 0.170 | render pipeline added issue; see intermediate/source comparison |
| 170.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.990 | 0.987 | 0.124 | render pipeline added issue; see intermediate/source comparison |
| 184.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.988 | 0.987 | 0.159 | render pipeline added issue; see intermediate/source comparison |
| 198.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.936 | 0.984 | 0.200 | render pipeline added issue; see intermediate/source comparison |
| 215.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.893 | 0.929 | 0.232 | render pipeline added issue; see intermediate/source comparison |
| 230.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.990 | 0.980 | 0.124 | render pipeline added issue; see intermediate/source comparison |
| 245.00s | whiteout / washout, right_top_black_block, gray_edge_or_band | 0.955 | 0.712 | 0.124 | render pipeline added issue; see intermediate/source comparison |


## 人眼复核重点

- 5s / 15s / 25s / 42s / 55s：商品卡区域明显洗白，商品图和字段不可读。
- 96s / 106s / 120s：表格 / 页面主体被大面积白层覆盖，右上角黑块明显。
- 155s / 170s / 184s / 215s / 245s：结果表 / 复查表段继续出现过度遮挡。
