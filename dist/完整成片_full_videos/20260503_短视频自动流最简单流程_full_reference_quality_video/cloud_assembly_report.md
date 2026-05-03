# cloud_assembly_report

- status：success
- real_aliyun_api_called_for_assembly：true
- oss_upload_count：20
- ice_request_chain：ListEditingProjects -> UpdateEditingProject -> SubmitMediaProducingJob -> GetMediaProducingJob
- cloud_job_id_desensitized：`adf3...c923`
- polling_status：success
- cloud_export_status：success
- local_download_path：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/full_video.mp4`
- ffprobe_result：passed；1080x1920；H.264；AAC；742.849s
- middle_zoom_preserved_after_cloud_export：true
- local_reference_assembly_used：false
- blocked：false
- blocked_reason：
- signed_url_or_secret_written：false

`scripts/assemble_formal_api_demo.py` 已执行北京区 OSS + ICE / 云剪 cloud-only assembly；未使用 local assembly fallback。中段放大裁切已在上传前写入 prepared_visuals，云剪导出后的 full_video.mp4 抽帧复核仍保留该处理。
