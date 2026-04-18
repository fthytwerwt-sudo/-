# 元素娃娃线 round3｜切换 wan2.7 与 s2v 最小闭环

## provider_switch_result

- `已确认` 当前正式配置入口：`/Users/fan/.config/video-factory/formal_api_demo.local.toml`
- `已确认` round3 主路线已改为：`wan2.7-image-pro / wan2.7-image -> wan2.2-s2v`
- `已确认` 官方文档参考：`wan2.7-image-pro / wan2.7-image` 图像生成 API 与 `wan2.2-s2v` 数字人对口型 API。

## asset_generation_result

- `候选A_正脸主持娃娃_v2`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选A_正脸主持娃娃_v2_wan2.7-image-pro_review_1080x1920.png`
- `候选B_软体素主持娃娃_v2`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选B_软体素主持娃娃_v2_wan2.7-image-pro_review_1080x1920.png`

## s2v_min_run_result

- `status = blocked`
- `video_path = None`
- `contact_sheet = `

## s2v_attempts

- `候选A_正脸主持娃娃_v2`
  - `status = blocked`
  - `failure_reason = wan_s2v_detect_rejected`
  - `blocked_reason = wan2.2-s2v-detect did not pass.`
- `候选B_软体素主持娃娃_v2`
  - `status = blocked`
  - `failure_reason = wan_s2v_detect_rejected`
  - `blocked_reason = wan2.2-s2v-detect did not pass.`

## route_note

- `待验证` 本文件只记录自动闭环结果；‘是否摆脱 gif 感’需结合导出视频与抽帧做人工判读。
