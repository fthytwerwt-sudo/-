# 20260509｜main主线与项目中心价值口径统一

## 1. 本轮目标
- 统一《视频工厂》当前唯一远端主线 / 默认主读取分支为：`main`
- 统一当前项目中心价值为：`真实 AI 使用经验 + 工作提效实录`
- 将 `场景化专业输出工作包` 降级为：`可选沉淀单元 / 产品化承接单元`

## 2. 本轮实际修改
- 已更新主入口与执行入口：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`
- 已补齐当前规则层里的旧分支同步口径：`codex_source/02`、`03`、`08`、`12`、`14`、`locked_reference_registry.md`
- 已更新当前事实与文案价值规则：`GPT数据源/00`、`01`、`03`、`04`、`05`、`07`、`08`、`09`
- 已更新 `codex_log/latest.md` 顶部摘要
- 已新增治理报告：`治理_reports/20260509_main主线与项目中心价值口径统一_main_branch_and_value_alignment/main主线与项目中心价值口径统一报告_main_branch_and_value_alignment_report.md`

## 3. 本轮未修改
- `dist/latest_review_pack/`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `GPT 数据源/`
- `/Users/fan/Documents/视频工厂归档+删除`
- 任何视频、音频、图片、原始素材
- 任何 `content_validation`、`send_ready`、当前发布状态字段

## 4. 当前统一口径
- `已确认` 当前唯一远端主线 / 默认主读取分支：`main`
- `已确认` 当前项目中心价值：`真实 AI 使用经验 + 工作提效实录`
- `已确认` 当前视频默认角色：`真实经验证明壳 / 提效证据入口壳`
- `已确认` `场景化专业输出工作包` 当前角色：`可选沉淀单元 / 产品化承接单元`
- `已确认` 当前内容优先验证：真实经验、工作提效证据、真实录屏、前后变化、小样本平台反馈与发布后复盘

## 5. 尾巴说明
- `codex_log/latest.md` 仍保留大量 `codex/user-readable-map` 历史正文；本轮未重写历史日志，只在顶部补当前口径。
- `codex_log/current_publish_target.md` 仍保留旧主读取分支口径；由于本轮禁止修改该文件，后续若要做状态指针收口，需要单独处理。

## 6. 验证
- `grep -R "codex/user-readable-map" -n AGENTS.md codex_source GPT数据源 codex_log/latest.md review_loop`
  - 当前规则层已不再把它写成默认主线；剩余命中为历史日志正文与显式历史引用说明
- `grep -R "当前项目中心价值.*场景化专业输出工作包" -n GPT数据源 AGENTS.md codex_source`
  - 无命中
- `python3 -m unittest discover -s tests -p 'test*.py'`
  - `已确认` `62 tests` 通过
