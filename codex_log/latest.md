# Latest

## 当前主结论

- `已确认` 当前正式对象仍是：
  - `《豆包的正确打开方式》vNext`
  - 输出目录：`dist/20260417_豆包的正确打开方式_vnext/`
- `已确认` 当前最新 C 线独立能力验证已推进到：
  - `host_motion_asset_gate_round5`
- `已确认` 本轮最新新增结论是：
  - 已修正 round3 / round4 自定义 detect 逻辑误读 `output.pass` 的问题，当前按 `output.check_pass` 判定
  - `wan2.7-image-pro` 本轮继续真实可用
  - round5 首张新资产已通过 `wan2.2-s2v-detect`
  - 可选最短 `wan2.2-s2v` smoke test 已真实成功落出最小 `mp4`
  - 这只代表：`detect gate + smoke route` 已成立，不代表主线可替换或正式样片已成立
- `已确认` `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4` 现只作为：`历史通过样片 / 历史口径`
- `已确认` 当前主线状态仍是：
  - `technical_validation = passed`
  - `content_validation = blocked`
- `已确认` 当前不要进入最终样片组装。

## 当前主线 blocker

1. `待补录` A 线反面原句级证据仍未补齐

## 当前 B 线

- `已确认` 当前正式 B 线暂定定版仍固定为：
  - `E1`
- `已确认` 备选：
  - `E2`
- `已确认` 淘汰对照：
  - `E3`

## 当前 C 线

- `已确认` 当前项目 / 当前已接模型 **仍不具备** 直接产出“高质量视频级元素娃娃样片”的能力。
- `已确认` 本轮已按既定路线进入：
  - `host_motion_asset_gate_round5`
- `已确认` 当前 C 线已停止继续沿：
  - `wan2.6-image -> liveportrait`
- `已确认` 当前 C 线当前最小主路线已切到：
  - `wan2.7-image-pro / wan2.7-image -> wan2.2-s2v`
- `已确认` 本轮真实已成立：
  - `wan2.7-image-pro` 可用
  - 已真实落出新主持娃娃资产
  - 已锁定当前过检资产：`候选A_round5_软脸主持肖像`
- `已确认` 因此本轮结果是：
  - `wan2.2-s2v-detect` 已对当前 round5 资产返回 `success`
  - 最短 `wan2.2-s2v` smoke test 已成功产出最小 `mp4`
- `已确认` 当前 C 线新增最高优先级 blocker 为：
  - 已从“detect 过检”推进到“生成结果质量判断”
  - 当前还没有证明已摆脱 `gif` 感或达到主持壳最低可用线
  - 因而当前仍不能写成主线可用

## 本轮新增产出

1. `codex_log/20260418_视频工厂_GPT_Project配合机制修补.md`
2. `codex_log/20260418_视频工厂_Project指令补丁_账号层硬执行.md`
3. `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md`
4. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round2/audit/asset_gate_summary.json`
5. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round2/audit/最小闸门审计_round2.md`
6. `scripts/元素娃娃线_round2_资产与detect闸门验证.py`
7. `codex_log/20260418_元素娃娃线_round2_资产与detect闸门验证.md`
8. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/audit/round3_switch_summary.json`
9. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/audit/最小闸门审计_round3.md`
10. `scripts/元素娃娃线_round3_切换wan2.7与s2v闭环.py`
11. `codex_log/20260418_元素娃娃线_round3_切换wan2.7与s2v闭环.md`
12. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/audit/round4_detect_summary.json`
13. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/audit/最小闸门审计_round4.md`
14. `scripts/元素娃娃线_round4_s2v_detect过检优化.py`
15. `codex_log/20260418_元素娃娃线_round4_s2v_detect过检优化.md`
16. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/audit/round5_detect_summary.json`
17. `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/audit/最小闸门审计_round5.md`
18. `scripts/元素娃娃线_round5_s2v_detect过检优化.py`
19. `codex_log/20260418_元素娃娃线_round5_s2v_detect过检优化.md`

## 下一轮唯一建议

- `已确认` 主线仍先补 A 线反面原句级证据，不进入最终样片组装
- `已确认` C 线本轮已跨过新路线的 `s2v detect` 闸门
- `已确认` 下一步不该回退到旧 `wan2.6-image -> liveportrait`
- `通用建议` 下一步应转到“最小视频质量审查”：
  - 判断 smoke test 是否仍像 `gif / 图片动起来`
  - 判断口型 / 头部 / 动作是否达到主持壳最低可用线
  - 若不过线，再继续在新路线里修资产和参数，而不是回退旧 provider

## 当前默认接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_log/20260418_视频工厂_GPT_Project配合机制修补.md`
5. `codex_log/20260418_视频工厂_Project指令补丁_账号层硬执行.md`
6. `GPT数据源/01_项目系统提示词.md`
7. `GPT数据源/08_当前正式事实.md`
8. `GPT数据源/09_目标态计划.md`
9. `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md`
10. `codex_log/20260418_元素娃娃线_round2_资产与detect闸门验证.md`
11. `codex_log/20260418_元素娃娃线_round3_切换wan2.7与s2v闭环.md`
12. `codex_log/20260418_元素娃娃线_round4_s2v_detect过检优化.md`
13. `codex_log/20260418_元素娃娃线_round5_s2v_detect过检优化.md`
