# 截图数据录入规则 screenshot data intake rules

## 1. 文件定位

本文件负责《视频工厂》发布后运营数据截图录入规则。

`已确认` 2026-05-15 起，当前默认路由从 `gray_test_data_intake（灰度数据录入）` 迁移为 `operation_data_intake（运营数据录入）`。

旧 `gray_test_data_intake` 只作为历史兼容别名保留；新截图、平台数据、评论、私信或咨询默认先读取 `codex_log/current_operation_target.md` 和 `review_loop/operation_records_index.md`。

它解决的问题是：

- 用户不手填完整数据表
- 用户直接给截图
- Codex 根据截图提取数据
- 数据必须按视频、时间窗、数据类型分开
- Codex 记录和初检，ChatGPT / 用户最终判断

它不是：

- 自动化采集系统
- OCR 准确率承诺
- 内容质量最终判断规则
- 新的复盘系统

本文件属于既有 `review_loop/（发布后复盘执行层）`，不得替代 `review_loop/` 另起一套系统。

## 2. 总原则

用户后续可以直接提交截图，Codex 负责：

- 保存截图证据
- 判断截图归属
- 提取可识别字段
- 标记缺失字段
- 标记不确定字段
- 更新对应视频记录
- 输出给 ChatGPT 的复盘输入

用户不需要手填完整数据表。

## 3. 三层分桶

截图必须按三层分桶：

```text
第一层：视频
第二层：时间窗
第三层：数据类型
```

写入数据前必须先确认：

1. 这张截图属于哪一条视频。
2. 这张截图属于哪个时间窗。
3. 这张截图属于哪类数据。

任一层无法确认时，不得入表；先写入缺失 / 不确定记录。

## 4. 视频层

每条视频必须有唯一 `video_id（视频编号）`。

当前 v3.1 视频：

- `video_id = V001`
- `video_slug = v31_AI做PPT踩坑`
- `video_title = 我用 AI 做 PPT 踩过的坑`
- `video_baseline = v3.1`

当前记录目录：

- `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`

当前截图目录：

- `review_loop/screenshots/V001_v31_AI做PPT踩坑/`

如果后续有新视频，必须新建新的 `video_id`，不得复用 `V001`。

## 5. 时间窗层

同一视频必须分开记录：

- `24h（24 小时初检）`
- `72h（72 小时复检）`
- `7d（7 天封账）`

不能混写。

硬规则：

- `24h` 截图只写入 `24h` 记录。
- `72h` 截图只写入 `72h` 记录。
- `7d` 截图只写入 `7d` 记录。
- `72h` 数据不得覆盖 `24h` 数据。
- `7d` 数据不得混成 `72h` 数据。

## 6. 数据类型层

每个时间窗下再分：

- `platform_metrics（平台数据）`
- `audience_retention（留存 / 完播）`
- `interaction（点赞 / 收藏 / 评论 / 转发）`
- `account_growth（主页访问 / 涨粉）`
- `comments（评论截图）`
- `dm（私信截图）`
- `consult（咨询截图）`
- `other（其他证据）`

数据类型无法确认时，先放入 `other` 并标记 `uncertain_need_human_check`，不得硬归类。

## 7. 推荐目录结构

```text
review_loop/screenshots/{video_slug}/
  24h/
    platform_metrics/
    audience_retention/
    interaction/
    account_growth/
    comments/
    dm/
    consult/
    other/
  72h/
    platform_metrics/
    audience_retention/
    interaction/
    account_growth/
    comments/
    dm/
    consult/
    other/
  7d/
    platform_metrics/
    audience_retention/
    interaction/
    account_growth/
    comments/
    dm/
    consult/
    other/
```

当前 V001 使用：

- `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/`
- `review_loop/screenshots/V001_v31_AI做PPT踩坑/72h/`
- `review_loop/screenshots/V001_v31_AI做PPT踩坑/7d/`

## 8. 识别状态

每个字段必须标记来源状态：

- `extracted_from_screenshot（已从截图提取）`
- `user_provided（用户手动提供）`
- `calculated_from_fields（由字段计算）`
- `missing（截图未提供）`
- `uncertain_need_human_check（识别不确定，待人工确认）`
- `not_applicable（不适用）`

字段提取必须保留来源截图路径；没有来源路径的字段只能写为 `user_provided`、`calculated_from_fields`、`missing` 或 `uncertain_need_human_check`。

## 9. Codex 截图录入流程

用户给截图后，Codex 默认执行：

1. 判断 `video_id`。
2. 判断时间窗：`24h / 72h / 7d`。
3. 判断数据类型：平台数据、留存、互动、账号增长、评论、私信、咨询或其他。
4. 将截图归档到对应目录。
5. 更新对应 `V001_*_screenshot_extract_report.md`。
6. 将可识别字段写入 `V001_gray_test_record.md` 的对应时间窗。
7. 将缺失字段写入 `V001_missing_fields.md`。
8. 将待人工确认字段标记为 `uncertain_need_human_check`。
9. 更新 `V001_chatgpt_review_input.md` 给 ChatGPT 复盘。

## 10. 禁止硬猜

禁止：

- 截图看不清就猜数字
- 把估算写成确定值
- 把评论截图当私信截图
- 把咨询截图当私信截图
- 把 24h 截图写进 72h
- 把 72h 截图覆盖 24h
- 把 7d 截图混成 72h
- 把不同视频截图混到同一记录
- 把私信数自动等于有效咨询数
- 把咨询数硬猜成私信数
- 把播放量高写成内容通过
- 把灰度测试写成最终成功

## 11. 分工边界

用户负责：

- 提供截图
- 必要时补充截图所属视频、时间窗或平台信息
- 对识别不确定字段做确认

Codex 负责：

- 截图归档
- 字段提取
- 缺失标记
- 不确定标记
- 更新记录
- 输出 ChatGPT 复盘输入

ChatGPT / 用户负责：

- 最终判断四个复盘问题
- 判断下一轮只改哪一个变量
- 判断内容是否真正通过

Codex 不做最终内容判断。
