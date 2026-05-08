# 复盘到文案调整桥接 review to copy revision bridge

## 文件定位

- 本文件负责把复盘结论转成下一版文案结构改版包。
- 它不是数据记录文件。
- 它不是最终脚本定稿文件。
- 它不是平台风控规则本体。
- 它位于“诊断之后、下轮执行单之前”。

## 触发条件

凡复盘结论命中以下任一项，必须触发本桥接：

1. 文案结构未锁定。
2. 开头钩子待验证或失败。
3. 中段录屏承载不清。
4. 结尾动作缺失或风险高。
5. 平台风险表达需要改写。
6. 画面触发点来自文案 / 画面文字 / 工具界面 / 命令行。
7. 收藏高但播放被异常压制，需要保留内容方向但重做表达。
8. 下一轮唯一改点是发布包装、文案结构、画面表达或录屏承载。

## 默认处理顺序

1. sample_decision（样本判断）
   - normal_sample（正常样本）
   - reference_abnormal_sample（可参考异常样本）
   - excluded_sample（排除样本）

2. problem_layer（问题层）
   - platform_risk（平台风险）
   - copy_structure（文案结构）
   - footage_carrier（录屏承载）
   - publish_packaging（发布包装）
   - content_value（内容价值）
   - technical_execution（技术执行）

3. copy_structure_status（文案结构状态）
   - locked（已锁定）
   - not_locked（未锁定）
   - partial_locked（部分锁定）

4. revision_target（本轮只改什么）
   - 必须只锁一个主变量。
   - 可有一个辅助变量，但必须说明为什么不能拆开。

5. safe_copy_package（安全文案包）
   - 标题
   - 开头判断句
   - block 结构
   - segment 承载
   - 录屏素材要求
   - 风险词替换
   - 结尾动作
   - 发布前检查要求

6. next_round_execution_brief（下一轮执行包）
   - 给 Codex 的下一轮执行输入。
   - 不能只写“改包装”。
   - 必须写清做到哪算改完。

## 输出要求

每次触发本桥接，必须输出：

1. sample_decision（样本判断）
2. problem_layer（问题层）
3. copy_structure_status（文案结构状态）
4. revision_target（本轮改动目标）
5. safe_copy_package（安全文案包）
6. pre_publish_check_requirement（发布前检查要求）
7. next_round_execution_brief（下一轮执行包）
8. blocked_items（阻断项）

## 验收标准

只有同时满足以下条件，才算桥接完成：

1. 已判断样本是否可参考。
2. 已锁定问题层。
3. 已判断文案结构是否锁定。
4. 已生成安全文案包。
5. 已明确发布前风险检查要求。
6. 已生成下一轮执行包草案。
7. 未把异常样本当正常样本。
8. 未把文案结构草案写成最终定稿。

## 禁止误用

- 不得从数据记录直接跳到视频生成。
- 不得只写“下一轮改包装”，但不写文案结构包。
- 不得把平台风控等同于文案结构复盘。
- 不得让 Codex 替代 ChatGPT 做最终内容拍板。
- 不得把 V002 这类异常样本写成内容失败。
- 不得因为平台减推否定内容方向。
