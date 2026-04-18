# 主持壳方向验证 round6｜正式质量审计

## route_audit

- `已确认` 路线 A（本地程序化 / 分层 / 时间线 / ffmpeg）更适合本轮目标。
- `已确认` 原因：它最能保证全身存在、身体承担动作、镜头不滑向大头特写。
- `已确认` 路线 B（I2V）在当前阶段更容易再次滑回特写人像或 talking head，因此本轮不优先。

## implementation_choice

- `已确认` 本轮选用：路线 A
- `已确认` 形式：全身 `Chibi Voxel Mascot Doll` 静音 `idle loop` 验证

## new_asset_definition

- `已确认` 目标对象：`Chibi Voxel Mascot Doll`
- `已确认` 头身比：约 `1:2.2`
- `已确认` 镜头：全身中景，第一帧即完整见身
- `已确认` 风格：`Minecraft-inspired` 原创体素方块风 + 更柔的 2.5D 主持娃娃
- `已确认` 动作：身体主导的 `idle loop`，含重心起伏、手臂摆动、腿部交替承重

## minimum_quality_gate_check

- 第一帧是否完整全身：`已确认`
- 头身比是否接近 `1:2`：`部分成立`
- 脸部占比是否 `<= 35%`：`已确认`
- 是否仍像大头特写：`已确认` 否
- 是否仍像 `talking head`：`已确认` 否
- 身体是否真的承担主要动作：`已确认` 是
- 是否像游戏角色自由活动：`部分成立`
- 是否像 `gif / 图片动起来`：`部分成立`
- 是否达到“主持壳最低可用线”：`待验证`

## high_fidelity_direction_check

- `角色保真`：`部分成立`。当前更像体素主持娃娃，不像软脸 talking head，但角色细节仍偏简化。
- `镜头保真`：`已确认`。当前已守住全身 / 中景，没有滑向头肩特写。
- `动作保真`：`部分成立`。当前动作由身体承担，不是只动脸，但动作词汇仍偏少。
- `风格保真`：`部分成立`。当前保留了几何体素感和玩具人偶感，但离高保真终版仍有差距。
- `收敛判断`：`partially_converging`。当前开始朝高保真体素主持娃娃方向收敛，但还不是可替换主线的形态。

## summary

- `technical_validation = passed_for_probe`
- `content_validation = blocked`
- `high_fidelity_direction = partially_converging`
- `current_gap_to_high_fidelity = 角色细节层次、动作语言丰富度、镜头稳定性与游戏角色感仍不足`
- `remaining_blockers = 当前结果虽已脱离 talking head，但仍带明显程序化循环感，距离“高保真主持壳最低可用线”仍差一步`
