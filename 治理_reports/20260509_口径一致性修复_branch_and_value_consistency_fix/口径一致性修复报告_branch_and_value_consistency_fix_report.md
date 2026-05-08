# 口径一致性修复报告

## 1. 修复前冲突
- `已确认` 当前主入口、执行规则和 `GPT数据源/` 主体文件大部分已经切到 `main` 与新中心价值。
- `已确认` 但仍有少量尾巴口径没有完全收干净：
  - `GPT数据源/00_项目总述.md` 的总结句仍写着“主线不变，价值不变”，与当前新中心价值冲突。
  - `GPT数据源/07_AI知识类视频价值规则.md` 的一句话规则仍把“一个场景工作包（多个 prompt）”写成当前默认变现单元，口径过重。
  - `GPT数据源/08_当前正式事实.md` 的优先验证项还没把“真实录屏 / 前后变化 / 小样本平台反馈”写全。
- `已确认` `codex/user-readable-map` 的剩余命中主要在 `codex_log/latest.md` 历史正文和 `codex_source/00_codex_readme.md` 的显式历史引用说明中，不再属于当前主线冲突。

## 2. 修复后口径
- `已确认` 当前唯一远端主线 / 默认主读取分支：`main`
- `已确认` `codex/user-readable-map` 只作为：`historical_branch_reference（历史分支引用）`
- `已确认` 当前项目中心价值：`真实 AI 使用经验 + 工作提效实录`
- `已确认` 当前视频默认角色：`真实经验证明壳 / 提效证据入口壳`
- `已确认` `场景化专业输出工作包` 当前角色：`可选沉淀单元 / 产品化承接单元`
- `已确认` 当前内容优先验证：
  - 真实 AI 使用经验
  - 工作提效证据
  - 真实录屏
  - 前后变化
  - 小样本平台反馈
  - 发布后复盘闭环

## 3. 修改文件清单
- [GPT数据源/00_项目总述.md](/Users/fan/Documents/视频工厂/GPT数据源/00_项目总述.md)
- [GPT数据源/07_AI知识类视频价值规则.md](/Users/fan/Documents/视频工厂/GPT数据源/07_AI知识类视频价值规则.md)
- [GPT数据源/08_当前正式事实.md](/Users/fan/Documents/视频工厂/GPT数据源/08_当前正式事实.md)
- [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
- [codex_log/20260509_口径一致性修复_branch_and_value_consistency_fix.md](/Users/fan/Documents/视频工厂/codex_log/20260509_口径一致性修复_branch_and_value_consistency_fix.md)

## 4. 保留不动文件清单
- [AGENTS.md](/Users/fan/Documents/视频工厂/AGENTS.md)
- [codex_source/00_codex_readme.md](/Users/fan/Documents/视频工厂/codex_source/00_codex_readme.md)
- [codex_source/01_execution_rules.md](/Users/fan/Documents/视频工厂/codex_source/01_execution_rules.md)
- [GPT数据源/04_选题与文案规则.md](/Users/fan/Documents/视频工厂/GPT数据源/04_选题与文案规则.md)
- [GPT数据源/05_文案路由规则.md](/Users/fan/Documents/视频工厂/GPT数据源/05_文案路由规则.md)
- [GPT数据源/09_目标态计划.md](/Users/fan/Documents/视频工厂/GPT数据源/09_目标态计划.md)
- [dist/latest_review_pack/](/Users/fan/Documents/视频工厂/dist/latest_review_pack)
- [codex_log/current_publish_target.md](/Users/fan/Documents/视频工厂/codex_log/current_publish_target.md)
- [codex_log/current_publish_target_light_evidence.md](/Users/fan/Documents/视频工厂/codex_log/current_publish_target_light_evidence.md)
- `GPT 数据源/`
- `/Users/fan/Documents/视频工厂归档+删除`

## 5. 剩余旧引用
- `已确认` `codex/user-readable-map` 的剩余命中只在：
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md) 历史正文
  - [codex_source/00_codex_readme.md](/Users/fan/Documents/视频工厂/codex_source/00_codex_readme.md) 的显式 `historical_branch_reference（历史分支引用）` 说明
- `已确认` 这些剩余命中不再代表当前主线或当前同步目标。
- `已确认` 本轮没有大面积重写历史日志正文。

## 6. 验证结果
- `grep -R "codex/user-readable-map" -n AGENTS.md codex_source GPT数据源 codex_log/latest.md review_loop`
  - 当前入口链不再把它写成当前主线；剩余命中仅为历史正文与显式历史引用说明
- `grep -R "当前项目中心价值.*场景化专业输出工作包\\|项目中心价值.*场景化专业输出工作包\\|默认.*工作包" -n GPT数据源 AGENTS.md codex_source review_loop`
  - 当前命中仅反映“工作包降级为可选沉淀”或“不是每条默认都生成工作包”，不再存在“当前中心价值 = 工作包”的冲突
- `grep -R "真实 AI 使用经验" -n GPT数据源 AGENTS.md codex_source codex_log/latest.md review_loop`
  - 当前入口、事实、价值、latest 与 review_loop 记录均已命中
- `grep -R "工作提效实录" -n GPT数据源 AGENTS.md codex_source codex_log/latest.md review_loop`
  - 当前入口、事实、价值、latest 与 review_loop 记录均已命中
- `python3 -m unittest discover -s tests -p 'test*.py'`
  - `已确认` `62 tests` 通过
