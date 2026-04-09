# 20260410_segment_level_carrier_routing_rule_patch

## 本轮目标

- 把当前项目里的“block 级承载路由”正式升级成“block 下继续拆 `segment` 的承载路由”
- 把这条升级同时写进：
  - 项目层正式规则
  - 执行层 bridge
  - 默认接手日志
- 不改代码
- 不改测试
- 不改 config
- 不改 case
- 不动 `dist`

## 为什么这轮必须补

当前仓库已经有：

- `project_source/16_presentation_routing_rules.md`
  - 定义了展示路由执行单位是 `block`
- `project_source/22_copy_mode_routing_rules.md`
  - 定义了文案先拆到 block
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
  - 定义了当前主线与人物 1 次 / 2 次判断
- `project_source/08_quality_baseline_and_90_score_rules.md`
  - 定义了 demo 感 / 说明书感 / PPT 过重等验收口径

但还缺一层关键规则：

- block 不是最后一级
- 执行时还要继续拆 `segment`
- 先按功能判定：
  - 判断节点
  - 证据节点
  - 整理节点
  - 转场节点
- 再决定这小段更适合：
  - `API生成真人`
  - `用户录制素材`
  - `少量PPT / 总结卡`
- 最后才根据字数 / 动作量 / 可读性反推时长

如果不补这层，默认执行还会继续出现：

- 先定人物次数
- 先定结尾时长
- 先定录屏时长
- 再倒推文案和承载

这正是 demo 感、说明书感、课件感、节奏失真的高频来源。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `project_source/16_presentation_routing_rules.md`
- `project_source/22_copy_mode_routing_rules.md`
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_log/latest.md`

## skills

- `已确认` 仓库内没有本地 `skills/` 目录
- 实际使用全局 skills：
  - `using-superpowers`
  - `verification-before-completion`
  - `brainstorming`

## 实际改动文件

- `project_source/16_presentation_routing_rules.md`
- `project_source/22_copy_mode_routing_rules.md`
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_log/latest.md`
- `codex_log/20260410_segment_level_carrier_routing_rule_patch.md`

## 每个文件补了什么

### `project_source/16_presentation_routing_rules.md`

- 把正式判断顺序从“拆到 block”升级成：
  1. 先判内容类型
  2. 再判整条主价值
  3. 再拆 block
  4. 再拆 `segment`
  5. 先判 `segment` 功能
  6. 再判 `segment` 承载
  7. 最后反推时长
- 明确：
  - `block` 是上层路由单位
  - `segment` 是执行判断单位
- 写入核心一句：
  - **先判这一小段在干什么，再判这段字有多少、观众来不来得及看。功能决定承载，字数决定时长。**

### `project_source/22_copy_mode_routing_rules.md`

- 新增 `segment` 级文案路由规则
- 明确：
  - 判断节点 → `API生成真人`
  - 证据节点 → `用户录制素材`
  - 整理节点 → `少量PPT / 总结卡`
  - 转场节点 → 看它更像判断还是整理
- 明确禁止：
  - 先定人物次数，再硬塞文案
- 写入项目默认经验值，并标明：
  - 这是项目经验值，不是行业硬标准
- 新增 50 秒职场判断类最小示例

### `project_source/24_human_self_footage_light_ppt_routing_rules.md`

- 把主线锚点细化到“人物 / 录屏 / 总结卡按节点分发”
- 明确：
  - 人物出现次数由判断节点数决定
  - 录屏段由证据节点数决定
  - 总结卡由整理节点数决定
  - 50 秒内容默认人物 `1–2` 段
  - 只有出现额外判断拐点时，才允许升到第 `2` 次或第 `3` 次
- 补了简短示例，说明为什么不是每段都用人物，也不是每段都用总结卡

### `project_source/08_quality_baseline_and_90_score_rules.md`

- 在质量验收里显式补入：
  - 人物段越权
  - 录屏段失职
  - 总结卡越权
  - 因先定固定时长而导致节奏失真
  - 因 `segment` 路由错误而形成 demo 感 / 说明书感 / 课件感
- 同时把质量判断顺序补成：
  - 先看 block
  - 再看 `segment`
  - 再看职责分配
  - 再看节奏和信息密度

### `codex_source/03_research_findings_bridge.md`

- 新增 bridge：
  - 当前项目已经从“block 级路由”升级为“segment 级执行判断”
  - 后续执行时先看功能，再定承载，再反推时长

### `codex_log/latest.md`

- 改写为这轮“segment 级承载路由规则补丁”的默认接手摘要
- 明确：
  - 以后默认不再先定人物次数
  - 以后默认不再先定固定结尾时长

## 本轮正式落下的核心规则

- block 不是最后一级，执行时还要继续拆 `segment`
- `segment` 先判功能，再判承载
- 判断节点默认优先给 `API生成真人`
- 证据节点默认优先给 `用户录制素材`
- 整理节点默认优先给 `少量PPT / 总结卡`
- 转场节点看它更像判断还是整理，不单独乱加人物
- 人物出现次数不是先固定，而是由判断节点数决定
- 总结卡时长不是先固定，而是根据文字量和读速反推
- 录屏段时长不是按字数，而是按“至少看清一个完整动作或明确变化”判断
- 50 秒内容里，人物默认 `1–2` 段，只有出现额外判断拐点时才允许升到第 `2` 次或第 `3` 次

## 项目默认经验值

下面这些只作为项目默认经验值，不冒充行业统一标准：

- 人物段时长 ≈ 口播字数 ÷ `4.5–5.5` + `0.2–0.4` 秒缓冲
- 总结卡时长 ≈ 屏幕总字数 ÷ `5.5–6.5` + `0.4–0.8` 秒缓冲
- 单模块最短不要低于 `1.4` 秒
- 人物单段若超过 `22–26` 字，默认先怀疑过长，优先拆成“人物判断 + 录屏 / 卡片”
- 录屏段不按字数，而按“至少看清一个完整动作或明确变化”判断时长

## 本轮边界

- `已确认` 没有改动任何代码文件
- `已确认` 没有改动任何测试文件
- `已确认` 没有改动任何 config 文件
- `已确认` 没有改动任何 case 文件
- `已确认` 没有改动任何 `dist` 产物
- `已确认` 没有改动 `AGENTS.md`
- `已确认` 没有改动其他 `codex_source/*`

## 这轮之后的默认执行变化

- 默认不再只按 block 分发
- 默认先拆 `segment`
- 默认先判功能，再定承载，再反推时长
- 默认不再先定人物次数或固定结尾时长
- 质量验收会显式检查人物越权、录屏失职、总结卡越权和固定时长先行的节奏失真
