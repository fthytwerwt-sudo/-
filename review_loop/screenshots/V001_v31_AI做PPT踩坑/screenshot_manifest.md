# V001 截图 manifest

## 基础信息

- video_id：V001
- video_slug：V001_v31_AI做PPT踩坑
- video_title：我用 AI 做 PPT 踩过的坑
- record_dir：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`

## 截图分桶

每张截图必须按以下三层归档：

1. 视频：`V001`
2. 时间窗：`24h / 72h / 7d`
3. 数据类型：`platform_metrics / audience_retention / interaction / account_growth / comments / dm / consult / other`

## 截图清单

| screenshot_path | time_window | data_type | source_status | notes |
| --- | --- | --- | --- | --- |
|  | 24h / 72h / 7d | platform_metrics / audience_retention / interaction / account_growth / comments / dm / consult / other | extracted_from_screenshot / uncertain_need_human_check / missing |  |

## 当前目录结构

```text
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

## 写入规则

- 24h 截图只写入 24h。
- 72h 截图只写入 72h。
- 7d 截图只写入 7d。
- 评论截图只进 `comments`。
- 私信截图只进 `dm`。
- 咨询截图只进 `consult`。
- 无法判断类别时先放 `other`，并标记 `uncertain_need_human_check`。
