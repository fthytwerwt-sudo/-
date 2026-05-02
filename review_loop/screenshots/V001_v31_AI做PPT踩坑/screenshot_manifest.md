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
| `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/platform_metrics/V001_24h_总览播放互动粉丝_overview_play_interaction_fans_20260502_222405.png` | 24h | platform_metrics | extracted_from_screenshot | 原图已归档；包含播放量、点赞量、评论量、分享量、收藏量、弹幕量、完播率、2s跳出率、涨粉量、脱粉量、粉丝播放占比；部分互动 / 账号增长字段从该图提取。 |
| `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/audience_retention/V001_24h_留存来源互动_retention_traffic_interaction_20260502_222425.png` | 24h | audience_retention | extracted_from_screenshot | 原图已归档；包含完播率、5s完播率、平均播放时长、平均播放占比、2s跳出率、流量来源占比、互动率；播放量未超过 200，留存趋势图未展示有效数据。 |
| `review_loop/screenshots/V001_v31_AI做PPT踩坑/24h/account_growth/V001_24h_观众涨粉脱粉_audience_growth_unfollow_20260502_222440.png` | 24h | account_growth | extracted_from_screenshot | 原图已归档；包含涨粉量、涨粉率、脱粉量、脱粉率、不感兴趣量、不感兴趣率；截图时间仍标记 uncertain_need_human_check。 |

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
