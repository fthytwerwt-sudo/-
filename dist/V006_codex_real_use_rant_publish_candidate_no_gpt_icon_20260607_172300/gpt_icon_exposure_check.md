# gpt_icon_exposure_check

```yaml
scanned_full_video: true
sample_strategy:
  - first_10_seconds_every_1s
  - every_20s_until_end
  - final_cta_frame
  - manual_zoom_check_on_dense_text_frames: [120s, 160s, 180s, 260s]
  - manual_zoom_check_on_opening_frames: [0s, 4s, 8s, 10s]
gpt_icon_detected: false
chatgpt_icon_detected: false
openai_icon_detected: false
browser_favicon_detected: false
chatgpt_or_openai_page_title_detected: false
install_download_register_bypass_visual_detected: false
risky_frames: []
action_taken:
  - old_candidate_visuals_not_reused
  - only_new_recordings_M04_M05_M06_used
  - safe_crop_removed_left_sidebar_and_top_browser_window_chrome
  - boundary_cards_used_for_high_risk_concept_segments
final_decision: publish_candidate_ready_for_human_review
human_review_note: "本地抽帧未见 GPT / ChatGPT / OpenAI 图标、favicon 或页面标题；仍建议用户按全片播放做最终平台风险复审。"
```
