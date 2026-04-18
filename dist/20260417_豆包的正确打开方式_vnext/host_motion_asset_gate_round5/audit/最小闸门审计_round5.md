# 元素娃娃线 round5｜s2v detect 过检优化

## round4_delta_direction

- 继续沿候选C方向走，但脸更像卡通数字人肖像，而不是玩偶 / 娃娃。
- 继续放大脸部占比，减少肩颈和衣服面积，让 detect 更聚焦脸。
- 继续增强眼白、虹膜、鼻孔、唇形可识别度。
- 继续减少脸部方块切面和硬边，但把体素来源感保留在发型与服装上。

## asset_candidate_changes

- `候选A_round5_软脸主持肖像`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `design_goal = 沿候选C继续降玩偶感，做更稳定的卡通数字人脸。`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/assets/候选A_round5_软脸主持肖像_wan2.7-image-pro_review_1080x1920.png`

## detect_probe_result

- `候选A_round5_软脸主持肖像`
  - `status = success`
  - `failure_reason = `
  - `blocked_reason = `

## optional_s2v_smoke_test

- `status = success`
  - `video_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/s2v_probe/visual/候选A_round5_软脸主持肖像_video.mp4`
  - `contact_sheet = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/audit/s2v_smoke_contact_sheet.jpg`
