# 09 Reference-to-Execution Contract｜参考到执行契约

```json
{
  "reference_to_execution_contract": {
    "reference_anchor": {
      "source_path": "/Users/fan/Documents/视频工厂/文案库/文案对标.MP4",
      "reference_type": "project_internal_reference_video + secondary liked/disliked copy notes",
      "selected_video": "文案对标.MP4",
      "audit_confidence": "medium_high_for_visual_structure; partial_for_transcript_and_sfx"
    },
    "effect_targets": {
      "copy_effect": "顺口开头 + 具体问题 + 三层比较 + 真实屏幕/表格证明 + 边界句",
      "visual_effect": "问题卡定题、文档/表格高亮、主持人/结论卡翻译复杂信息",
      "motion_effect": "快切预览结果，局部高亮字段，表格/文档持屏阅读",
      "audio_effect": "持续口播为主，音效只服务动作，不抢表格信息",
      "card_effect": "判断卡负责问题和边界，信息卡负责结构，结果卡负责表格/结论",
      "pacing_effect": "开头快，中段证据慢，结尾低压行动"
    },
    "function_fields": {
      "opening_hook": "先抛具体反差：不是让AI选爆品，而是先把商品筛成可复查清单",
      "pain_point_setup": "手动翻商品卡信息太散，普通问AI容易泛泛回答",
      "proof_structure": "商品卡字段 -> 候选表/云盘表格 -> 聊天框结论",
      "judgment_card_usage": "每个关键判断前用短卡说明这段在判断什么",
      "motion_efficiency_usage": "搜索/筛选/表格/结论出现时用高亮和局部放大",
      "audio_sfx_usage": "自制/授权轻音效服务 typing/click/table/ding，不使用原音频",
      "visual_style_usage": "继承问题卡和高亮功能，不继承皮肤/人物/平台UI",
      "ending_action": "告诉用户下一步核哪几个商品、看哪些风险字段"
    },
    "deviation_check": {
      "must_match": [
        "开头有具体问题",
        "关键高光绑定真实页面/字段/表格/聊天框结论",
        "判断卡不替代证据",
        "结尾有下一步动作"
      ],
      "may_adapt": [
        "横屏16:9布局",
        "视频工厂自有卡片皮肤",
        "自制音效",
        "Codex操作电脑素材"
      ],
      "must_not_copy": [
        "原始文案",
        "人物/头像/账号",
        "抖音UI",
        "BGM/SFX",
        "字体/卡片皮肤",
        "第三方文档和画面资产"
      ],
      "blocked_if": [
        "只有泛泛讲AI提效没有商品字段",
        "画面和口播不对齐",
        "表格小字不可读",
        "暗示AI直接选爆品或商业验证成功",
        "使用未授权第三方资产"
      ]
    },
    "done_when": {
      "reference_pack_created": true,
      "transferable_rules_clear": true,
      "non_transferable_risks_clear": true,
      "chatgpt_handoff_pack_ready": true
    }
  }
}
```

## boundary

本 contract 只继承机制、节奏、颗粒度、卡片功能和动效功能；不得继承第三方人物、原始文案、商标、音频、BGM、素材资产或平台 UI。
