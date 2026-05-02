# 多项目仓库入口规则

## 1. 当前仓库身份

当前这是【多项目仓库】。

必须明确：
- 不能再把整个仓库直接写死成单一项目入口
- 不能再把所有新会话默认接成 `AI 直播前台验证项目`
- 不能再把《视频工厂》误判成直播项目的历史残片

当前仓库至少同时承载以下两条入口：
1. 《视频工厂》
2. `AI 直播前台验证项目`

默认规则：
- 命中《视频工厂》时，走《视频工厂》入口
- 命中 `AI 直播前台验证项目` 时，走直播入口
- 未命中任一项目时，不得擅自继承任何业务事实，必须先阻断并做路由判断

## 2. 默认项目分流规则

### 2.1 永远先读
进入当前仓库后，固定先读：
1. `AGENTS.md`

### 2.2 《视频工厂》命中规则
若任务命中以下任一关键词，默认按《视频工厂》接手：
- `视频工厂`
- `API 生成真人`
- `用户录制素材`
- `录制素材`
- `少量 PPT`
- `云端剪辑`
- `GPT数据源`
- `GPT 数据源`
- `豆包 prompt`
- `current_publish_target`
- `场景化专业输出工作包`
- `证明壳`
- `入口壳`
- `产品单元`

命中《视频工厂》后，默认先读：
1. `GPT数据源/00_项目总述.md`
2. `GPT数据源/01_项目系统提示词.md`
3. `GPT数据源/03_总索引与阅读顺序.md`
4. `GPT数据源/08_当前正式事实.md`
5. `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
6. `codex_source/00_codex_readme.md`
7. `codex_log/latest.md`

当前《视频工厂》正式来源顺序：
1. `GPT数据源/` 当前 10 份执行包
2. `codex_log/latest.md`
3. `dist/latest_review_pack/summary.json`
4. `dist/latest_review_pack/review_manifest.md`
5. `codex_source/00_codex_readme.md`

`project_source/` 只作为历史 / 辅助主题化镜像，不得默认高于 `GPT数据源/` 当前 10 份执行包、`codex_log/latest.md` 或 `dist/latest_review_pack/`。

当前已确认：
- `latest_review_pack` 当前指向 `20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- `current_video_baseline = v3.1（当前视频基线）`
- `future_iteration_base = v3.1（后续升级 / 修改 / 技术优化 / GPT 文案侧回炉的默认基础）`
- v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `technical_validation = passed（v3.1 技术验证通过）`，但 `technical_line_locked = false（技术线未锁定）`
- `technical_upgrade_next = true（下一步仍需技术升级）`
- `content_validation = gray_testing_not_final_passed（灰度测试中，不等于内容最终通过；不得写成内容通过）`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `visual_route_map.json（视觉路由表）` 与 `visual_route_validation_report.json（视觉路由验证报告）` 已随 v3.1 基线进入 `dist/latest_review_pack/`
- `publish_status = gray_test_published（v3.1 已发片，进入灰度测试）`
- `gray_test_status = active（灰度测试中）`
- `post_publish_review_required = true（需要发布后复盘）`
- `current_phase = post_publish_gray_test（发布后灰度测试阶段）`
- 上述 `content_validation` 是当前发布后阶段口径；不得把它写成 `passed`
- 发布后复盘默认走 `review_loop/`，不另起独立灰度系统
- 当前灰度测试目标看 `codex_log/current_gray_test_target.md`
- 当前灰度测试指标体系 V1 看 `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- 当前 7 天播放量 6000 是小样本阶段基础测试流量门槛，不是最终商业目标
- 当前指标体系不是运营数据大表，而是下一轮改动定位器
- 当前截图优先录入规则看 `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- 当前 v3.1 主记录目录看 `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
- 当前 v3.1 截图证据目录看 `review_loop/screenshots/V001_v31_AI做PPT踩坑/`
- 当前下一步不是先写新文案，而是先记录 24h / 72h / 7 天数据，回答四个复盘问题，再由 ChatGPT / 用户判断下一轮只改一个变量

### 2.2A 视频修改必须同步口径规则

以后凡是修改《视频工厂》的任何视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件。

默认必须同步检查：
1. `codex_log/latest.md`
2. `codex_log/current_publish_target.md`
3. `codex_log/current_publish_target_light_evidence.md`
4. `GPT数据源/08_当前正式事实.md`
5. `dist/latest_review_pack/summary.json`
6. `dist/latest_review_pack/review_manifest.md`
7. 如改变入口 / 分支 / 读取顺序，还必须同步 `AGENTS.md` 和 `codex_source/00_codex_readme.md`

硬规则：
- 不允许只改视频、不改口径
- 不允许只在工作分支改口径、不同步默认主读取分支
- 不允许把历史样片写成当前最新样片
- 不允许把 `technical_validation` 写成 `content_validation`
- 不允许用户未最终确认前把当前片子写成可发送状态
- 不允许旧 `round` 状态继续覆盖最新 `latest_review_pack`
- 只要改动会影响新会话默认接手判断，就必须同步到 `codex/user-readable-map`

### 2.2B 《视频工厂》旧口径降权规则

当前《视频工厂》接手时，必须先应用以下覆盖规则：

- `round34` 只能作为历史中段剪辑 / 提示卡参考，不是当前最新样片状态。
- PR #22 仍是 v3 历史候选草稿 PR；v3 不再作为后续默认修改基础，不得直接合并覆盖当前 v3.1 基线。
- PR #23 的“PR #7 A 优先”是旧只读判断，已被用户最新确认覆盖；PR #23 只能作为历史样本包。
- PR #24 的 v3.1 有效产物已安全回流到主读取分支；PR #24 本身不得再直接合并，以免回退 PR #25 清理结果。
- 后续骚萌卡唯一执行参考是 `PR7_B_骚萌反应页.png`；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- PR #7 A 只能作为历史 / candidate 对照，不能出现在任何未来执行 reference 字段里。
- `归档_archive/旧口径_old_context_*/` 只保存旧判断证据，不作为默认事实入口。
- 后续所有 v3.1 基线升级必须保留并复核 `visual_route_map.json（视觉路由表）`，不得让段落提示卡、信息卡、骚萌卡共用同一套外壳。

### 2.2C 《视频工厂》单工作区硬规则 single_workspace_rule

`已确认` 《视频工厂》唯一正式工作区固定为：

- `/Users/fan/Documents/视频工厂`

硬规则：

- Codex 后续不得默认新建 `/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*`、`/Users/fan/Documents/视频工厂-worktrees` 作为外部散工作区。
- 如果需要新分支，必须在 `/Users/fan/Documents/视频工厂` 内执行 `git switch -c <branch>` 或切换既有分支。
- 不得默认使用 `git worktree add` 创建外部 Git 工作区；除非用户当轮明确授权。
- 所有最终产物、样片、复审包、截图归档、治理报告、路径索引、执行日志和清理记录，都必须落在 `/Users/fan/Documents/视频工厂` 内部。
- `/Users/fan/Desktop`、`/Users/fan/Downloads`、`/private/tmp`、`/Users/fan/Documents/视频工厂_*`、`/Users/fan/Documents/视频工厂-*` 不得作为最终交付路径。
- 如果必须临时读取外部路径，只能作为 `source（来源）` 只读读取；必须回收到唯一正式工作区后，才能写入路径索引或默认执行口径。
- `codex_log/current_local_artifact_paths.md` 的 `canonical_local_path（首选本地路径）` 只能指向 `/Users/fan/Documents/视频工厂` 内部。
- 旧外部路径最多只能写为 `historical_source_path（历史来源路径）` 或 `fallback_path（备选路径）`，不得作为默认执行路径。
- 后续清理、归档、迁移任务也必须从 `/Users/fan/Documents/视频工厂` 发起、记录和提交。

若任务继续命中《视频工厂》的内容生产，再补读：
8. `GPT数据源/04_选题与文案规则.md`
9. `GPT数据源/05_文案路由规则.md`
10. `GPT数据源/07_AI知识类视频价值规则.md`

若任务继续命中《视频工厂》的阶段 / 复盘 / 商业化，再补读：
11. `GPT数据源/09_目标态计划.md`

若任务命中《视频工厂》的截图 / 数据截图 / 24h / 72h / 7 天 / 灰度测试 / 发片复盘 / 发片 / 发布后 / 复盘 / 数据记录 / 私信 / 咨询，再补读：
12. `codex_log/current_gray_test_target.md`
13. `review_loop/00_review_loop_readme.md`
14. `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
15. `review_loop/02_video_record_template.md`
16. `review_loop/03_result_dashboard_template.md`
17. `review_loop/04_diagnosis_template.md`
18. `review_loop/05_dual_review_handoff_template.md`
19. `review_loop/06_next_round_task_template.md`
20. `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
21. `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
22. `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
23. `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`

截图优先录入机制硬规则：
- 命中“截图 / 数据截图 / 24h / 72h / 7 天 / 灰度测试 / 发片复盘 / 私信 / 咨询”时，默认进入 `review_loop/` 截图优先录入机制。
- 必须按 `video_id` 分开记录；不同视频不得混写。
- 必须按 `24h / 72h / 7d` 分开记录；不同时间窗不得互相覆盖。
- 必须按数据类型分开归档；平台数据、留存完播、互动、账号增长、评论、私信、咨询不得混写。
- Codex 只做截图归档、字段提取、缺失标记、初检和交接，不做最终内容判断。

后续复盘默认先回答四个问题：
1. 这条有没有达到 6000 播放基础门槛？
2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
3. 下一轮只改哪一个变量？
4. 为什么先改它，改完看哪个指标？

当前灰度测试硬边界：
- 发片不等于内容过线
- 灰度测试不等于验证成功
- `send_ready` 仍保持 `false`
- `visual_master_locked` 仍保持 `false`
- PR #7 B 仍是后续骚萌卡唯一执行参考，PR #7 A 仍只作历史 / candidate 对照
- 下一轮文案前必须先看 v3.1 灰度测试记录和四个复盘问题

### 2.3 `AI 直播前台验证项目` 命中规则
若任务命中以下任一关键词，默认按 `AI 直播前台验证项目` 接手：
- `AI 直播前台`
- `直播前台`
- `数字人前台`
- `抖音高分直播间`
- `阿里数字人`
- `ASR`
- `TTS`
- `RTC`
- `推流`
- `云直播`
- `多房间扩容`
- `1 台阿里云服务器带 5 个直播间`

命中直播项目后，默认先读：
1. `项目资料_docs/系统协议_system/00_协作协议_collaboration_protocol.md`
2. `项目资料_docs/直播前台项目_live_frontend_project/00_项目总说明_project_brief.md`
3. `项目资料_docs/直播前台项目_live_frontend_project/01_执行合同与验收_execution_contract.md`
4. `项目资料_docs/直播前台项目_live_frontend_project/02_当前任务与研究问题_current_task.md`

### 2.4 未命中时的阻断规则
若任务未命中《视频工厂》或 `AI 直播前台验证项目` 任一关键词，则必须：
1. 先阻断，不得直接进入任一项目业务判断
2. 先把当前任务标记为：`待路由`
3. 先做项目分流判断，再继续执行

### 2.5 双命中或冲突命中
若同一任务同时命中两个项目关键词，默认先按“路由层冲突”处理：
1. 先识别任务到底是在修入口 / 修分流 / 修接手机制，还是在处理某一项目业务
2. 若属于入口 / 分流 / 接手机制，先只修路由层，不扩写业务规则
3. 若属于业务任务，再按显式目标对象选择唯一项目入口
4. 先输出当前冲突点
5. 再给一个最小路由判断

若任务命中不清，也按同一规则处理：
1. 先输出冲突点
2. 再给一个最小路由判断
3. 未完成路由前，不直接拍板进入任一项目

## 3. 文件与目录命名规则

从现在开始，除工具链 / 系统强制要求的固定文件名外，之后所有新建业务文件和业务文件夹默认必须使用“中文 + 英文”命名。

推荐格式：
- `中文名_english_name`

该规则默认覆盖：
- 业务文件
- 文档文件
- 日志文件
- 资料文件
- 脚本文件
- 目录名

默认禁止：
- 新建纯英文业务文件名
- 新建纯英文文档文件名
- 新建纯英文日志文件名
- 新建纯英文资料文件名
- 新建纯英文脚本文件名
- 新建纯英文目录名

已有文件和已有文件夹本轮不追溯改名；后续若要迁移既有命名，必须另起审计任务，先确认引用、工具链约束和迁移风险。

固定例外：
- `AGENTS.md`
  原因：Codex 固定入口文件名，不能改。
- `README.md`
  原因：常见仓库入口文件名，外部工具和 GitHub 页面可能直接识别。
- `package.json`
  原因：Node.js / npm 工具链固定清单文件名。
- `package-lock.json`
  原因：Node.js / npm 工具链固定锁文件名。
- `.gitignore`
  原因：Git 固定忽略配置文件名。
- `.git/`
  原因：Git 系统目录。
- `.github/`
  原因：GitHub 工作流与仓库配置固定目录。
- `node_modules/`
  原因：Node.js 依赖安装目录。

工具链强制例外规则：
- 若未来遇到工具链强制英文固定文件名，必须明确标注为“工具链强制例外”
- 必须写清楚为什么不能改名
- 不允许把例外范围扩大到普通业务文件

系统目录说明：
- `.git/`、`.omx/`、`.gitignore`、`package.json`、`package-lock.json` 等现有工具链 / 系统文件属于历史或工具运行要求，不作为新建业务命名范例

## 4. 默认修改权限规则

默认不要随便改：
- 协作协议类文件
- 项目总说明类文件

在任务明确要求时可以更新：
- `项目资料_docs/直播前台项目_live_frontend_project/01_执行合同与验收_execution_contract.md`
- `项目资料_docs/直播前台项目_live_frontend_project/02_当前任务与研究问题_current_task.md`

允许持续更新：
- `执行日志_codex_log/最新摘要_latest.md`
- 其他阶段摘要 / 执行日志类文件

## 5. 默认执行规则

执行前默认动作：
- 先读 `AGENTS.md`
- 先判断当前任务命中哪个项目入口
- 先判断当前任务属于账号层、项目层、执行层还是路由层
- 未命中项目入口前，不得擅自继承任何项目业务事实
- 命中《视频工厂》后，再按《视频工厂》入口继续
- 命中《视频工厂》后，账号层长期规则仍按硬约束执行；若用户当前在问机制层 / 配合层问题，先答机制层，不直接被项目业务细节带走
- 命中直播项目后，再按直播入口继续

形成可判断小闭环后，默认动作：
1. 先更新 `执行日志_codex_log/最新摘要_latest.md`
2. 命中条件时补完整执行日志
3. commit 当前改动
4. push 当前工作分支 / 当前 PR
5. 再交回 GPT 基于 GitHub 最新结果复审

不要只在本地改完就停。

什么叫“可判断小闭环”：
- 已完成一轮明确文件修改
- 已形成一版可读的规则稿 / 项目骨架 / 研究稿
- 已形成新的 blocker / 冲突点 / 交接点，需要基于真实结果判断
- 已完成一轮值得复审的仓库改动

可以暂不 push 的情况：
- 当前仍是明显半成品
- 改动边界仍在摇摆
- 还没形成可判断小闭环
- 日志还没更新
- 本轮只有纯读取、无修改、无新结论

额外硬规则：
- 路由层任务只修入口、分流、接手顺序与已知边界，不擅自改业务规则

## 6. 诚实状态标记规则

凡涉及完成度、验证情况、可行性、自动化程度、能力边界，必须明确标状态。

默认只使用：
- 已确认
- 部分成立
- 待验证
- 推测
- 通用建议

禁止把中间态说成完成态。

## 7. 表达规则

- 默认中文沟通优先
- 命令、代码、配置键、字段名、环境变量、路径、报错原文、术语保留英文原词
- 先给主结论，再给最必要说明
- 需要复制的内容默认放进完整 Markdown 代码块
- 文件名、目录名、字段名、配置项若出现英文，默认使用“原文 + 中文备注”或直接换成清楚中文

## 8. 最终汇报与交接口径

- 以后最终汇报最后一栏统一使用“下一个目标”。
- 不再默认使用“下一步行动建议”。
- “下一个目标”必须表达下一轮要达成的状态，而不是泛泛行动建议。
- 如果必须写动作，动作必须服务于“下一个目标”。
