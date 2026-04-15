# Minecraft-inspired 视觉与声音规则

## 1. 文件定位
本文件只负责 4 件事：
- 定义 vNext 的统一视觉外壳
- 定义 `Minecraft-inspired` 的合法边界
- 规定开头人物壳 / 结尾总结壳 / `Prompt 引用尾卡` 的统一风格
- 给出声音路线建议与参数建议

它不负责：
- 当前待发对象切换
- 最终成片验收
- TTS provider 选型落地
- 任何官方资产复用

## 2. inspired 合法边界
当前只允许：
- `Minecraft-inspired 原创体素方块风`
- 原创体素角色
- 原创体素工作台环境
- 原创体素 UI 面板
- 原创体素色板与几何块面

当前明确禁止：
- 直接复用官方 `logo`
- 直接复用官方 `fonts`
- 直接复用官方 `textures`
- 直接复用官方 `images`
- 直接复用官方 `models`
- 直接复用官方 `sounds`
- 做成让用户误解为官方授权、官方联名或官方素材包

## 3. 当前统一视觉外壳规则

### 3.1 开头人物壳
- 默认统一为：`Minecraft-inspired 原创体素方块风`
- 作用：
  - 承担开头判断进入
  - 承担关键判断句
- 不承担：
  - 中段主体证据
  - 全片主推进

### 3.2 结尾总结壳
- 默认统一为：`Minecraft-inspired 原创体素方块风`
- 作用：
  - 收束本条内容的 3 到 5 个判断点
  - 强化“像游戏工作台里的任务提示板”感觉
- 不承担：
  - 重新解释整条理论

### 3.3 `Prompt 引用尾卡`
- 默认与开头人物壳、结尾总结壳共用同一套色板、材质语言与体素面板语言
- 作用：
  - 引用当前工作包 / 三层 prompt 在干什么
  - 提醒用户下一步最小动作
- 不承担：
  - 主叙事
  - 中段证据

## 4. 默认视觉提示词骨架

### 4.1 开头人物壳
```text
Minecraft-inspired original voxel block style, original character design, calm workplace desk setup, soft block lighting, vertical short-video framing, friendly guide posture, no official game assets, no logos, no textures copied from official materials
```

### 4.2 结尾总结壳
```text
Minecraft-inspired original voxel block style summary card, original voxel UI panel, low-pressure workplace atmosphere, clean 3 to 5 bullet layout, soft contrast, no official fonts, no official textures, no branded assets
```

### 4.3 `Prompt 引用尾卡`
```text
Minecraft-inspired original voxel reference card, original block UI panel, shows prompt layers and action hints, supportive and calm, not flashy, no official assets, no direct franchise references
```

## 5. 默认声音路线

### 5.1 目标感觉
- 平静
- 轻陪伴
- 低压
- 更像游戏向导
- 不像 AI 播报

### 5.2 默认避免
- 播报腔
- 销售腔
- 新闻腔
- 过度热情
- 过度戏剧化

### 5.3 参数建议
- 语速：`0.92 - 1.0`
- 句间停顿：略长于默认
- 音高波动：控制在低到中等范围
- 情绪强度：低到中等
- 目标体验：像陪用户过任务，而不是对用户喊结论

### 5.4 当前状态边界
- 本文件只给“声音路线建议 + 参数建议”
- 不代表已经选定最终 TTS 模型
- 不代表已经完成 `content_validation（内容验证）`

## 6. 一句话规则
**当前 vNext 只允许做 `Minecraft-inspired 原创体素方块风`，统一承接开头人物壳、结尾总结壳和 `Prompt 引用尾卡`；声音路线只允许走“平静、轻陪伴、低压、像游戏向导”的建议方向，不得冒充已经验证完毕的最终声音方案。**
