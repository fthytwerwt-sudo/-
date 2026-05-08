# 文案知识库更新日志

## 2026-04-14 GPT 数据源本地同步

- 本轮完成：
  - 将当前文案知识库第二层内容同步写入本机 `GPT 数据源` 目录
- 本轮写入的本地中文文件：
  - `30_文案知识库说明.md`
  - `31_喜欢样本第一轮分层拆分.md`
  - `32_开头库_v1.md`
  - `33_判断句库_v1.md`
  - `34_过渡句库_v1.md`
  - `35_收束与CTA库_v1.md`
  - `36_当前偏好总结_v1.md`
- 本轮明确：
  - 上述文件写入路径为 `/Users/fan/Documents/视频工厂/GPT 数据源/`
  - 这些文件属于 `local_only`
  - 它们不是 GitHub 仓库正式文件本身
  - 它们也不会自动进入 GPT Project，仍需要用户手动替换数据源文件
- 本轮未做：
  - 文案知识库正文改写
  - 新一轮文案拆分
  - 新建额外同步包目录

## 2026-04-14 喜欢样本初拆

- 新增文件：
  - `11_gold_samples_first_split.md`
  - `12_opening_library_v1.md`
  - `13_judgment_library_v1.md`
  - `14_transition_library_v1.md`
  - `15_closing_and_cta_library_v1.md`
  - `16_current_preference_summary_v1.md`
- 本轮完成：
  - 基于 `01_gold_samples_raw.md` 做了喜欢样本第一轮分层拆分
  - 将文案知识库从“原始入库”推进到“第二层可用结构”
  - 先提炼出开头库、判断句库、过渡句库、收束与 CTA 库、偏好总结 v1
- 本轮明确：
  - 当前判断只基于“喜欢样本”
  - 当前属于第一轮初拆，不是最终风格定稿
  - “只喜欢哪一段” 还没补，所以后续还会继续变细
- 本轮未做：
  - 不喜欢样本深拆
  - “只喜欢哪一段”拆分
  - 口语原话库
  - 自动化机制设计

## 2026-04-13 初始化

- 新增目录：`project_source/30_copy_library/`
- 新增文件：
  - `00_copy_library_readme.md`
  - `01_gold_samples_raw.md`
  - `02_anti_patterns_raw.md`
  - `08_update_log.md`
- 本轮导入的原始样本：
  - `/Users/fan/Documents/视频工厂/文案库/喜欢 txt.txt`
  - `/Users/fan/Documents/视频工厂/文案库/不喜欢.txt`
- 本轮完成：
  - 建立最小可持续维护的文案知识库骨架
  - 将“喜欢 / 不喜欢”两组原始样本正式导入仓库项目脑层
- 本轮未做：
  - 细分类整理
  - 规则总结
  - 文案优劣分析
  - “只喜欢哪一段”层级拆分
