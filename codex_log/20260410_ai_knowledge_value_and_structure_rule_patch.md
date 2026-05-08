# 20260410_ai_knowledge_value_and_structure_rule_patch

## 本轮目标

- 把两份外部研究稿的核心结论完整收束并落进当前仓库的现有镜像文件
- 不新增 GPT Project 数据源文件
- 不新建新的 `project_source` 主题文件
- 不写成“新增一份研究报告”，而是写成仓库正式规则

## 为什么这轮必须补

当前仓库已经有：

- `project_source/25_ai_knowledge_video_value_rules.md`
  - 有价值底线和四类内容最低价值交付的大方向
- `project_source/21_topic_selection_and_copywriting_rules.md`
  - 有进入文案前的前置判断
- `project_source/22_copy_mode_routing_rules.md`
  - 有文案进入主流程后的路由框架

但还不够完整：

- `25` 还缺：
  - 伪价值内容边界的完整化
  - 强证据 / 弱证据层级的更明确表达
  - 更细的样片前价值闸门
- `21` 还缺：
  - 进入文案前必须锁清“最小收获 / 最关键证据 / 开头类型 / 结尾类型”
- `22` 还缺：
  - 四类内容的结构匹配规则
  - 四类内容的开头匹配规则
  - 四类内容的结尾总结卡匹配规则
  - block 职责细化

如果不补这些，后续执行仍会继续出现：

- 只知道“这条内容有价值”，但不知道该用什么结构
- 进入文案前没有锁清最小收获与关键证据
- 文案写完后才临时决定开头和结尾
- 人物、录屏、PPT 的职责分配没有跟内容类型绑定

## 本轮实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `project_source/25_ai_knowledge_video_value_rules.md`
- `project_source/21_topic_selection_and_copywriting_rules.md`
- `project_source/22_copy_mode_routing_rules.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_log/latest.md`

### 可见的外部研究镜像

- `GPT 数据源/07_AI知识类视频价值规则.md`
- `GPT 数据源/04_选题与文案规则.md`
- `GPT 数据源/05_文案路由规则.md`

## 实际改动文件

- `project_source/25_ai_knowledge_video_value_rules.md`
- `project_source/21_topic_selection_and_copywriting_rules.md`
- `project_source/22_copy_mode_routing_rules.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_log/latest.md`
- `codex_log/20260410_ai_knowledge_value_and_structure_rule_patch.md`

## 这轮怎么对应外部研究稿与仓库现状

### `25` 的补强

从“价值底线粗版”补成：

- 价值底线
- 伪价值内容边界
- 四类内容最低价值交付的更明确解释
- 强证据 / 弱证据层级
- 进入样片前的价值闸门

重点新增的默认理解：

- 只有观点，没有动作
- 只有共鸣，没有帮助
- 只有方法，没有证据
- 只有案例，没有可迁移价值
- 只有总结，没有下一步行动
- 看起来很专业，但用户说不出“我现在先做什么”

这些都属于伪价值内容边界。

### `21` 的补强

把“进入文案阶段前必须先回答的 6 个问题”补得更贴近研究稿，明确进入文案前至少要锁：

- 用户最小收获
- 最关键证据
- 最合适开头类型
- 最合适结尾类型

### `22` 的补强

完整吸收了四类内容的结构 / 开头 / 结尾矩阵：

- AI 项目讲解：
  - 结构：`结论先行 → 过程补充`
  - 开头：`结果先给型`
  - 结尾：`judgment_card + 最小行动`
- AI 方法分享：
  - 结构：`旧方式 → 新方式`
  - 或 `错误点 → 正确动作 → 自检标准`
  - 开头：`问题点破型` / `错误示范型`
  - 结尾：`steps_error_card`
- AI 学习实操：
  - 结构：`问题 → 动作 → 结果`
  - 开头：`直接教一招型`
  - 结尾：`steps_card + 自检句`
- AI 案例拆解：
  - 结构：`提问 → 拆解 → 结论`
  - 开头：`结果先给型` / `问题点破型`
  - 结尾：`judgment_card + 可迁移句`

同时补清了 block 职责细化：

- 人物：
  - 信任
  - 进入感
  - 关键判断
  - 收束
- 用户录制素材：
  - 主体推进
  - 过程证据
  - 现场感
- 少量 PPT / 图片：
  - 关键词显影
  - 结构整理
  - 结尾总结

## bridge 这轮补了什么

在 `codex_source/03_research_findings_bridge.md` 新增了一条 bridge，明确：

- 这两份外部研究稿已经被正式吸收进仓库项目脑
- 当前正式落点是：
  - `project_source/25_ai_knowledge_video_value_rules.md`
  - `project_source/21_topic_selection_and_copywriting_rules.md`
  - `project_source/22_copy_mode_routing_rules.md`

## 本轮边界

- `已确认` 没有改动 `AGENTS.md`
- `已确认` 没有改动 `project_source/16_presentation_routing_rules.md`
- `已确认` 没有改动 `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `已确认` 没有改动任何代码文件
- `已确认` 没有改动任何测试文件
- `已确认` 没有改动任何 config 文件
- `已确认` 没有改动任何 case 文件
- `已确认` 没有改动任何 `dist` 产物
- `已确认` 没有新建任何 `project_source` 新文件
- `已确认` 没有新建任何 GPT Project 数据源文件

## 这轮之后的默认执行变化

- 后续不再只按“价值底线”粗略判断 AI 知识类内容
- 后续会默认按内容类型判断更适合的结构、开头和结尾
- 后续进入文案前必须先锁清最小收获、最关键证据、开头类型和结尾类型
- 后续 block 职责会更明确服从：
  - 人物做关键判断
  - 录屏做主体推进和证据
  - PPT 做结构整理和结尾总结
