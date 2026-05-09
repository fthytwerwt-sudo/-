# 20260510｜execution_supply_pack_test_evidence

## 1. 证据口径

本文件是本轮 `execution_supply_pack family（执行供料包族）` controller 测试的 Git 可追溯证据。

`dist/deepseek_supply_controller/*` 是本地运行产物，本轮不作为 GitHub 主事实提交；GitHub 可追溯证据以本文件为准。

## 2. execution_supply_pack_test_evidence

```yaml
execution_supply_pack_test_evidence:
  tested_actions:
    - action: file_map
      request_file: codex_source/fixtures/deepseek_supply_request_file_map_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: 旧 action 兼容；因任务卡禁止 .env / secret，controller 使用本地兜底供料，不是 DeepSeek 结论。
    - action: editing_decision_pack
      request_file: codex_source/fixtures/deepseek_supply_request_editing_decision_pack_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: 已有剪辑决策包 action 仍可运行；本轮没有真实读取媒体，也没有写成 DeepSeek passed。
    - action: visual_asset_requirement_pack
      request_file: codex_source/fixtures/deepseek_supply_request_visual_asset_requirement_pack_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: 新视觉素材需求包 action 可被 controller 接受，并生成 execution_supply_pack 字段。
    - action: api_asset_generation_pack
      request_file: codex_source/fixtures/deepseek_supply_request_api_asset_generation_pack_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: 新 API 素材生成包 action 可被 controller 接受；api_call_allowed_this_round=false，不读取密钥，不调用 API。
    - action: image_prompt_pack
      request_file: codex_source/fixtures/deepseek_supply_request_image_prompt_pack_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: 新图片 prompt 包 action 可被 controller 接受；只生成 prompt 供料，不生成图片。
    - action: asset_validation_pack
      request_file: codex_source/fixtures/deepseek_supply_request_asset_validation_pack_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: Codex 二次补全新增的素材验收包 action 可运行；用于阻断 AI 图片冒充真实证据。
    - action: assembly_decision_pack
      request_file: codex_source/fixtures/deepseek_supply_request_assembly_decision_pack_example.json
      request_validation_status: passed
      supply_source: fallback_local_only
      fallback_status: used
      context_pack_validation: fallback_local_only
      not_deepseek_conclusion: true
      output_files_local:
        - dist/deepseek_supply_controller/latest_supply_pack.md
        - dist/deepseek_supply_controller/latest_supply_pack.json
        - dist/deepseek_supply_controller/latest_supply_manifest.json
      output_files_committed: false
      evidence_summary: 新装配决策包 action 可被 controller 接受，并生成 execution_supply_pack 字段。
  forbidden_path_tests:
    - request_file: codex_source/fixtures/deepseek_supply_request_bad_forbidden_env_example.json
      request_validation_status: blocked
      supply_source: blocked
      context_pack_validation: blocked
      fallback_status: not_used
      not_deepseek_conclusion: true
      error: request_file_matches_forbidden_path:.env
      evidence_summary: .env 在读取前 blocked。
    - request_file: codex_source/fixtures/deepseek_supply_request_bad_forbidden_media_example.json
      request_validation_status: blocked
      supply_source: blocked
      context_pack_validation: blocked
      fallback_status: not_used
      not_deepseek_conclusion: true
      error: request_file_matches_forbidden_path:素材样例/sample.mp4
      evidence_summary: 媒体路径在读取前 blocked。
    - request_file: codex_source/fixtures/deepseek_supply_request_bad_forbidden_latest_review_pack_example.json
      request_validation_status: blocked
      supply_source: blocked
      context_pack_validation: blocked
      fallback_status: not_used
      not_deepseek_conclusion: true
      error: request_file_matches_forbidden_path:dist/latest_review_pack/summary.json
      evidence_summary: dist/latest_review_pack/ 在读取前 blocked。
  deepseek_actual_participation: false
  fallback_usage: true
  fallback_reason: 本轮禁止读取 .env / secret，controller 按 request 安全策略跳过 DeepSeek API，使用 fallback_local_only。
  remaining_unverified:
    - DeepSeek API 在不读取 .env 的安全注入方式下参与新 action 供料，仍待后续单独验证。
    - 阿里 API 图片生成链路未调用，未生成真实图片。
    - 真实最终文案进入全执行供料链，仍待后续小范围任务验证。
```

## 3. 状态边界

- `technical_validation（技术验证）`: controller、schema、fixtures 可本地运行和解析。
- `mechanism_validation（机制验证）`: 执行供料包族已进入规则、schema、controller、fixtures 和日志证据。
- `deepseek_supply_validation（DeepSeek 供料验证）`: 本轮为 `fallback_local_only` 样例测试，不是 DeepSeek passed。
- `api_generation_validation（API 生成验证）`: 未调用真实 API，未读取 key，未生成图片。
- `content_validation（内容验证）`: 未验证真实视频内容，不得写成 passed。

## 4. 下一个目标

用一条真实最终文案做小范围执行测试：先跑视觉素材需求、API 素材生成计划、图片 prompt、素材验收、装配决策和剪辑决策，不直接生成完整大视频。
