# 20260418｜元素娃娃线 round4 s2v detect 过检优化

## read_files

- `已确认` 已读：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`
  - `GPT数据源/01_项目系统提示词.md`
  - `GPT数据源/08_当前正式事实.md`
  - `GPT数据源/09_目标态计划.md`
  - `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md`
  - `codex_log/20260418_元素娃娃线_round3_切换wan2.7与s2v闭环.md`
  - `formal_api_demo_core.py`
  - `scripts/元素娃娃线_round3_切换wan2.7与s2v闭环.py`
  - `~/.config/video-factory/formal_api_demo.local.toml`

## skills_check

- `已确认` 当前仓库本地 `skills/` 目录不存在。
- `已确认` 已回退检查全局 `~/.codex/skills`。
- `已确认` 已检查：
  - `using-superpowers`
  - `context-driven-development`
  - `verification-before-completion`
  - `systematic-debugging`
- `已确认` 本轮实际采用：
  - `using-superpowers`
  - `systematic-debugging`
  - `verification-before-completion`
- `部分成立` `context-driven-development` 已检查，但本轮未进入 `conductor/` 上下文工件维护。

## round3_failure_hypothesis

- `已确认` round3 的失败更像是资产形态问题，而不是接口接入问题。
- `已确认` 当前最可疑的失败原因包括：
  - round3 A 的脸仍偏娃娃化，眼口鼻结构过于简化
  - round3 B 的方块切面和边缘线条仍然太强
  - round3 整体还不够像 detect 友好的“卡通数字人肖像”
  - 当前 detect 更偏好“大脸、强正脸、清楚眼白虹膜鼻孔嘴唇”的人脸化卡通肖像

## asset_candidate_changes

- `已确认` 本轮独立目录已建立：
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/`
- `已确认` 本轮建立了：
  - `assets/`
  - `detect_probe/`
  - `audit/`
- `已确认` 本轮共新生成 4 张资产候选，且都由 `wan2.7-image-pro` 真实成功落出：
  - `候选A_大脸正脸主持娃娃`
    - 强化脸部占比、正脸程度和五官可识别度
  - `候选B_弱化方块切面主持娃娃`
    - 降低脸部方块切面，提高五官对比度
  - `候选C_半体素软面部主持娃娃`
    - 保留 inspired 主持娃娃感，但让脸更接近卡通数字人肖像
  - `候选D_卡通数字人肖像版`
    - 进一步向 detect 友好的卡通数字人肖像靠近
- `已确认` 从人工视觉判断看：
  - `候选C` 是当前最接近可用的一张
  - 原因是脸最平滑、五官最稳定、玩偶感最低
  - 但它仍未过 `wan2.2-s2v-detect`

## detect_probe_result

- `已确认` 本轮 4 张新资产全部真实跑了 `wan2.2-s2v-detect`。
- `已确认` detect 结果如下：
  - `候选A_大脸正脸主持娃娃`：`blocked`
  - `候选B_弱化方块切面主持娃娃`：`blocked`
  - `候选C_半体素软面部主持娃娃`：`blocked`
  - `候选D_卡通数字人肖像版`：`blocked`
- `已确认` 4 张图失败原因一致：
  - `wan2.2-s2v-detect did not pass.`
- `已确认` 因此本轮没有任何一张资产达到“过检资产”。

## optional_s2v_smoke_test

- `已确认` `skipped`
- `已确认` 原因：
  - 没有任何新资产通过 `wan2.2-s2v-detect`
  - 按本轮 stop line，不继续硬跑 `wan2.2-s2v`

## technical_validation

- `已确认` `blocked`
- `已确认` 原因：
  - 新资产真实落出
  - `wan2.7-image-pro` 真实可用
  - 但 `wan2.2-s2v-detect` 对 4 张新资产仍全部未通过

## content_validation

- `已确认` `blocked`
- `已确认` 原因：
  - 本轮没有最小视频
  - 因而没有新的运动结果可回审

## recommended_next_route

- `已确认` 当前不要回退到旧 `wan2.6-image -> liveportrait`。
- `已确认` 当前最上游 blocker 仍是：
  - `wan2.2-s2v-detect` 不接受当前这批主持娃娃资产
- `已确认` 下一步最值路线是继续沿新路线优化资产，而不是换回旧 provider：
  1. 继续向 `候选C` 的脸部方向靠拢
  2. 再进一步减少玩偶感与贴图感
  3. 让脸更像卡通数字人肖像，而不是“可爱摆件 / 娃娃”
  4. 衣服与发型保留 inspired 体素来源感，脸部继续去体素化

## git_commit_and_push_status

- `待验证` 本日志落盘时尚未提交 / 推送。

## reading_branch_sync_status

- `待验证` 本日志落盘时尚未同步回 `codex/user-readable-map`。
