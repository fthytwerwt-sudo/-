# 元素娃娃线 round2｜资产与 detect 闸门验证

## connected_provider_recheck

- `已确认` 正式本地配置：`/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- `已确认` `image_generation.model = wan2.6-image`
- `已确认` `video_generation.model = wan2.7-i2v`
- `已确认` `portrait_detect.model = liveportrait-detect`
- `已确认` `portrait_video_generation.model = liveportrait`

## asset_candidates

- `候选A_正脸主持娃娃`
  - `image_generation.status = failed`
  - `review_asset_path = missing`
- `候选B_软体素主持娃娃`
  - `image_generation.status = failed`
  - `review_asset_path = missing`

## detect_results


## liveportrait_probe

- `status = skipped`
- `result_path = skipped`
- `contact_sheet = not_generated`

## stop_line

- `ability_gate = blocked`
- `stop_line_triggered = image_generation_unavailable_or_failed`

## note

- `待验证` 本文件只记录自动执行结果；是否摆脱“图片动起来 / gif 感”，仍需基于导出视频与预览帧做人工判读。
