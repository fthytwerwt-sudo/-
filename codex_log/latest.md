# Latest

## 当前主结论

- `已确认` 本轮完成的是 **segment 级承载路由规则补丁**，不是代码实现任务。
- `已确认` 当前项目的展示 / 文案路由，不再只停在 `block` 级。
- `已确认` 当前正式默认已升级为：
  - 先拆 `block`
  - 再把每个 `block` 继续拆成 `segment`
  - 先判 `segment` 在干什么
  - 再判这段更适合谁承载
  - 最后才按字数 / 动作量 / 读速反推时长
- `已确认` 当前项目必须按这句理解：

**先判这一小段在干什么，再判这段字有多少、观众来不来得及看。功能决定承载，字数决定时长。**

- `已确认` 以后默认不再先定人物次数，也不再先定固定结尾时长。
- `已确认` 人物、录屏、总结卡的默认分发正式改成：
  - 判断节点 → `API生成真人`
  - 证据节点 → `用户录制素材`
  - 整理节点 → `少量PPT / 总结卡`
  - 转场节点 → 看它更像判断还是整理

## 当前接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `project_source/16_presentation_routing_rules.md`
5. `project_source/22_copy_mode_routing_rules.md`
6. `project_source/24_human_self_footage_light_ppt_routing_rules.md`
7. `project_source/08_quality_baseline_and_90_score_rules.md`
8. `codex_source/03_research_findings_bridge.md`
9. `codex_log/20260410_segment_level_carrier_routing_rule_patch.md`

## 本轮状态

- 当前任务性质：
  - 项目规则补丁
  - 路由机制修补
  - 执行层 bridge 更新
- 当前影响范围：
  - 展示路由
  - 文案路由
  - 主线锚点
  - 质量验收
  - 执行层 bridge

## 当前默认行为变化

- 过去容易出现：
  - 只按 block 分配承载
  - 先定人物次数，再倒推文案
  - 先定结尾卡时长，再往里塞文字
  - 录屏段按字数裁，而不是按动作与变化裁
- 当前正式默认改成：
  - block 不是最后一级，执行时还要继续拆 `segment`
  - 判断节点默认优先给 `API生成真人`
  - 证据节点默认优先给 `用户录制素材`
  - 整理节点默认优先给 `少量PPT / 总结卡`
  - 人物出现次数由判断节点数决定
  - 总结卡时长按文字量和读速反推
  - 录屏段时长按“至少看清一个完整动作或明确变化”判断

## 当前仍需明确

- 本轮修的是项目规则和执行层 bridge，不是代码实现
- 本轮没有改动任何代码 / 测试 / config / case / dist
- 本轮没有改动 `AGENTS.md`
- 当前 reading branch 应以这轮 segment 级路由补丁后的口径为准
