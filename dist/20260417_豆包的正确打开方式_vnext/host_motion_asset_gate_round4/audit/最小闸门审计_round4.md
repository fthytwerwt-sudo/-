# 元素娃娃线 round4｜s2v detect 过检优化

## round3_failure_hypothesis

- 候选A 的脸虽然更柔，但五官仍偏简化，眼睛是大块黑色椭圆，嘴部存在过度简写，可能不够像可驱动的人脸。
- 候选B 的脸更方，眉眼嘴仍有明显块面边界，方块切面与发型边缘可能干扰 detect。
- 两张 round3 资产的脸部占比还不够极端，仍然保留较多肩颈和衣服面积，detect 友好优先级不够高。
- 当前 detect 更可能偏好‘更大脸、更正脸、更清楚的眼白/虹膜/鼻孔/嘴唇’，而不是体素味最强的脸。

## asset_candidate_changes

- `候选A_大脸正脸主持娃娃`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `design_goal = 最大化脸部占比、正脸程度和五官可识别度。`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选A_大脸正脸主持娃娃_wan2.7-image-pro_review_1080x1920.png`
- `候选B_弱化方块切面主持娃娃`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `design_goal = 降低脸部方块切面，提升眼口鼻对比度。`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选B_弱化方块切面主持娃娃_wan2.7-image-pro_review_1080x1920.png`
- `候选C_半体素软面部主持娃娃`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `design_goal = 保留 inspired 主持娃娃感，但让脸更接近卡通数字人肖像。`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选C_半体素软面部主持娃娃_wan2.7-image-pro_review_1080x1920.png`
- `候选D_卡通数字人肖像版`
  - `final_status = success`
  - `selected_model = wan2.7-image-pro`
  - `design_goal = 若前三张仍失败，进一步向 detect 友好的卡通数字人肖像靠近。`
  - `review_asset_path = /Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选D_卡通数字人肖像版_wan2.7-image-pro_review_1080x1920.png`

## detect_probe_result

- `候选A_大脸正脸主持娃娃`
  - `status = blocked`
  - `failure_reason = wan_s2v_detect_rejected`
  - `blocked_reason = wan2.2-s2v-detect did not pass.`
- `候选B_弱化方块切面主持娃娃`
  - `status = blocked`
  - `failure_reason = wan_s2v_detect_rejected`
  - `blocked_reason = wan2.2-s2v-detect did not pass.`
- `候选C_半体素软面部主持娃娃`
  - `status = blocked`
  - `failure_reason = wan_s2v_detect_rejected`
  - `blocked_reason = wan2.2-s2v-detect did not pass.`
- `候选D_卡通数字人肖像版`
  - `status = blocked`
  - `failure_reason = wan_s2v_detect_rejected`
  - `blocked_reason = wan2.2-s2v-detect did not pass.`

## optional_s2v_smoke_test

- `status = skipped`
