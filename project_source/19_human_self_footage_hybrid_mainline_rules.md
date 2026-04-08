# 人物 + 自录素材 + 轻 PPT 正式主线规则

## 1. 文件定位

本文件用于把《视频工厂》当前正式默认主线，写成稳定、可执行、可回审的规则。

它解决的是：

- 当前正式默认主线到底是什么
- 人物、自录素材、轻 PPT 分别承担什么职责
- 为什么 AI talking avatar / 数字人口播不再承担默认主承载
- 云端 assembly 如何继续作为正式主路径
- 当前最小可执行入口是什么

它不是：

- pure PPT 次级支路说明
- 动态 PPT 方案
- AI avatar 复活计划

## 2. 当前正式默认主线

当前正式默认主线固定为：

- `人物`
- `用户自己的真实录制素材`
- `少量 PPT / 图片辅助`

当前正式 assembly 主路径继续固定为：

- `北京区 OSS + 云剪 cloud-only`

必须明确：

- 这不是把主线切回 local assembly
- 这不是把 AI avatar 换个 prompt 再继续当默认主承载
- 这也不是把 pure PPT 删除；pure PPT 只降级为次级支路

## 3. 三类承载的职责分工

### A. 人物承担什么

- 开头命中
- 关键判断
- 收束 / 最小行动
- “这是我在对你说”的可信度

默认要求：

- 优先是真人表达，不是 AI avatar 模仿真人
- 语气克制、像真实创作者 / 真实同事在说
- 人物不能只是摆件；如果没有判断感，就不该硬上

### B. 用户自己的真实录制素材承担什么

- 现场感
- 过程感
- 证据感
- 真实操作 / 真实工作片段 / 真实录屏

默认要求：

- 优先让真实录屏、真实桌面操作、真实工作片段承担“看见过程”
- 这类段落优先吃用户真实素材，不默认改写成 AI 生成视频
- 缺真实素材时必须诚实 `blocked` / `待素材注入验证`

### C. 少量 PPT / 图片辅助承担什么

- 关键词显影
- 前后对比
- 结果句 / 数字句收束
- 局部说明

默认要求：

- 只做辅助，不抢主承载
- 不回到整条 pure PPT 主承载
- 只负责把重点打亮，不负责替代人物判断和真实证据

## 4. AI avatar / 数字人口播降级边界

以下问题当前已被正式收口为高风险：

- 口型和语音对不上
- 性别和文案不匹配
- 动作和文案不匹配
- 视觉人物与内容判断不一致

因此当前必须写死：

1. AI talking avatar / 数字人口播不再作为默认主承载
2. 若后续继续保留，只能作为：
   - 可选支线
   - 待验证支线
   - 非默认路线
3. 当前更稳的正式默认主线是：
   - 真人表达 / 自录素材 / 少量 PPT

这次改版的根理由必须固定为：

- 更像真人会发
- 更少 demo 感
- 避免把高风险错配路线顶在默认主承载位置

## 5. formal_api_demo 的最小执行入口

当前最小执行入口固定为：

- case：`cases/formal_api_demo_human_self_footage.md`
- config：`config/formal_api_demo.example.toml` 里的 `[footage_inputs.*]`
- generation：`scripts/generate_formal_api_demo.py`
- assembly：`scripts/assemble_formal_api_demo.py`

当前本地主线要求：

- `hook_human`
- `process_self_footage`
- `result_card`
- `close_human`

这些素材路径默认从本地 config 注入：

- 有真实文件：进入 manifest / route_plan / cloud assembly
- 缺真实文件：诚实 `blocked`

## 6. pure PPT 的当前定位

pure PPT / 信息卡当前可以保留，但默认只属于：

- 次级支路
- 特定场景下的结构说明支路
- 素材明显不足时的临时结构承载支路

必须明确：

- 它不再是整个项目的默认主承载主线
- 它继续走云端 assembly，不回退本地 fallback
- 它的风格规则继续看 `project_source/17_white_collar_ppt_style_rules.md`

## 7. 当前一句话规则

当前正式默认主线不是 pure PPT，也不是 AI avatar，而是：人物负责判断，自录素材负责证据，少量 PPT 负责显影；正式 assembly 继续走北京区 OSS + 云剪 cloud-only，缺真实素材就诚实 blocked。
