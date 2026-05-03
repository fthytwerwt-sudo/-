from __future__ import annotations

import base64
import hashlib
import hmac
import json
import mimetypes
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any


STATUS_BLOCKED = "blocked"
STATUS_FAILED = "failed"
STATUS_SUCCESS = "success"

ALIYUN_ICE_API_VERSION = "2020-11-09"
ALIYUN_ICE_ENDPOINT_TEMPLATE = "https://ice.{region}.aliyuncs.com/"
DEFAULT_ASSET_URL_EXPIRES_SECONDS = 3600


class CloudAssemblyError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        status: str = STATUS_FAILED,
        failure_reason: str = "",
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code
        self.status = status
        self.failure_reason = failure_reason


def execute_cloud_only_assembly(
    manifest: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    assembly_dir = output_dir / "assembly"
    assembly_dir.mkdir(parents=True, exist_ok=True)
    timeline_path = assembly_dir / "cloud_timeline.json"
    request_ids: dict[str, str] = {}
    uploaded_assets: list[dict[str, Any]] = []
    project_id: str | None = None
    project_title = _nested_get(config, "aliyun_ims", "cloud_project_name")
    job_id: str | None = None
    media_id: str | None = None
    output_url: str | None = None
    media_url: str | None = None
    output_object_key: str | None = None
    local_download_path: str | None = None

    try:
        run_id = _build_run_id()
        upload_bundle = _upload_source_assets(
            manifest=manifest,
            config=config,
            run_id=run_id,
        )
        uploaded_assets = upload_bundle["uploaded_assets"]

        timeline = _build_cloud_timeline(
            manifest=manifest,
            upload_bundle=upload_bundle,
        )
        _write_json(timeline_path, _sanitize_timeline_urls(timeline, config))

        timeline_object_key = _build_object_key(
            _nested_get(config, "aliyun_oss", "prefix_temp"),
            run_id,
            "cloud_timeline.json",
        )
        _upload_file_to_oss(
            local_path=timeline_path,
            object_key=timeline_object_key,
            config=config,
        )
        uploaded_assets.append(
            {
                "asset_kind": "timeline_debug",
                "local_path": str(timeline_path),
                "object_key": timeline_object_key,
                "media_url": _build_oss_https_url(config, timeline_object_key),
            }
        )

        project = _resolve_cloud_project(config)
        project_id = project["project_id"]
        project_title = project["project_title"]
        if project.get("request_id"):
            request_ids["list_projects"] = project["request_id"]

        update_result = _update_editing_project(
            config=config,
            project_id=project_id,
            timeline=timeline,
        )
        if update_result.get("request_id"):
            request_ids["update_project"] = update_result["request_id"]

        output_target = _build_output_target(config, run_id)
        output_object_key = output_target["object_key"]
        output_url = output_target["oss_url"]
        media_url = output_target["media_url"]

        submit_result = _submit_media_producing_job(
            config=config,
            project_id=project_id,
            output_media_config=output_target["output_media_config"],
        )
        job_id = submit_result["job_id"]
        media_id = submit_result.get("media_id")
        if submit_result.get("request_id"):
            request_ids["submit_job"] = submit_result["request_id"]

        poll_result = _poll_media_producing_job(
            config=config,
            job_id=job_id,
        )
        if poll_result.get("request_id"):
            request_ids["get_job"] = poll_result["request_id"]
        media_id = poll_result.get("media_id") or media_id
        media_url = poll_result.get("media_url") or media_url
        if output_object_key:
            local_video_path = output_dir / "full_video.mp4"
            download_url = _build_oss_signed_get_url(
                config=config,
                object_key=output_object_key,
                expires_seconds=DEFAULT_ASSET_URL_EXPIRES_SECONDS,
            )
            _download_oss_object(download_url, local_video_path, config)
            local_download_path = str(local_video_path)

        return {
            "status": STATUS_SUCCESS,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "project_id": project_id,
            "project_title": project_title,
            "job_id": job_id,
            "media_id": media_id,
            "output_url": output_url,
            "media_url": media_url,
            "output_object_key": output_object_key,
            "local_download_path": local_download_path,
            "timeline_path": str(timeline_path),
            "request_ids": request_ids,
            "uploaded_assets": _sanitize_uploaded_assets(uploaded_assets, config),
            "missing_prerequisites": [],
            "missing_implementations": [],
        }
    except Exception as exc:
        status = getattr(exc, "status", STATUS_FAILED)
        failure_reason = getattr(exc, "failure_reason", "") or "cloud_assembly_request_failed"
        return {
            "status": status,
            "blocked_reason": _sanitize_message(str(exc), config) if status == STATUS_BLOCKED else "",
            "failure_reason": failure_reason if status == STATUS_FAILED else "",
            "error_message": _sanitize_message(str(exc), config),
            "project_id": project_id,
            "project_title": project_title,
            "job_id": job_id,
            "media_id": media_id,
            "output_url": output_url,
            "media_url": media_url,
            "output_object_key": output_object_key,
            "local_download_path": local_download_path,
            "timeline_path": str(timeline_path),
            "request_ids": request_ids,
            "uploaded_assets": _sanitize_uploaded_assets(uploaded_assets, config),
            "missing_prerequisites": [],
            "missing_implementations": [],
        }


def _upload_source_assets(
    manifest: dict[str, Any],
    config: dict[str, Any],
    run_id: str,
) -> dict[str, Any]:
    uploaded_assets: list[dict[str, Any]] = []
    voiceover_path = _require_local_path(
        _nested_get(manifest, "generation", "voiceover", "audio_path"),
        label="voiceover_audio",
    )
    captions_path = _require_local_path(
        _nested_get(manifest, "generation", "captions", "captions_path"),
        label="captions_srt",
    )

    voiceover_object_key = _build_object_key(
        _nested_get(config, "aliyun_oss", "prefix_raw"),
        run_id,
        f"audio/{voiceover_path.name}",
    )
    captions_object_key = _build_object_key(
        _nested_get(config, "aliyun_oss", "prefix_raw"),
        run_id,
        f"captions/{captions_path.name}",
    )

    _upload_file_to_oss(voiceover_path, voiceover_object_key, config)
    _upload_file_to_oss(captions_path, captions_object_key, config)

    voiceover_url = _build_oss_signed_get_url(
        config=config,
        object_key=voiceover_object_key,
        expires_seconds=DEFAULT_ASSET_URL_EXPIRES_SECONDS,
    )
    captions_url = _build_oss_signed_get_url(
        config=config,
        object_key=captions_object_key,
        expires_seconds=DEFAULT_ASSET_URL_EXPIRES_SECONDS,
    )

    uploaded_assets.extend(
        [
            {
                "asset_kind": "voiceover_audio",
                "local_path": str(voiceover_path),
                "object_key": voiceover_object_key,
                "media_url": voiceover_url,
            },
            {
                "asset_kind": "captions_srt",
                "local_path": str(captions_path),
                "object_key": captions_object_key,
                "media_url": captions_url,
            },
        ]
    )

    segment_media: dict[str, dict[str, Any]] = {}
    for asset in _nested_get(manifest, "generation", "visual_generation", "segment_assets") or []:
        segment_id = asset.get("segment_id")
        if not segment_id:
            continue
        source_path = asset.get("video_asset_path") or asset.get("image_asset_path")
        local_path = _require_local_path(
            source_path,
            label=f"visual_asset_{segment_id}",
        )
        suffix = local_path.suffix or (".mp4" if asset.get("video_asset_path") else ".png")
        object_key = _build_object_key(
            _nested_get(config, "aliyun_oss", "prefix_raw"),
            run_id,
            f"visuals/{segment_id}{suffix}",
        )
        _upload_file_to_oss(local_path, object_key, config)
        media_url = _build_oss_signed_get_url(
            config=config,
            object_key=object_key,
            expires_seconds=DEFAULT_ASSET_URL_EXPIRES_SECONDS,
        )
        clip_type = "Video" if asset.get("video_asset_path") else "Image"
        segment_media[segment_id] = {
            "media_url": media_url,
            "clip_type": clip_type,
            "object_key": object_key,
        }
        uploaded_assets.append(
            {
                "asset_kind": f"visual_{segment_id}",
                "local_path": str(local_path),
                "object_key": object_key,
                "media_url": media_url,
                "clip_type": clip_type,
            }
        )

    return {
        "voiceover_url": voiceover_url,
        "captions_url": captions_url,
        "segment_media": segment_media,
        "uploaded_assets": uploaded_assets,
    }


def _build_cloud_timeline(
    manifest: dict[str, Any],
    upload_bundle: dict[str, Any],
) -> dict[str, Any]:
    total_duration = 0.0
    video_track_clips: list[dict[str, Any]] = []
    for segment in manifest.get("segments", []):
        segment_id = segment["segment_id"]
        media = upload_bundle["segment_media"].get(segment_id)
        if media is None:
            raise CloudAssemblyError(
                f"缺少段落 {segment_id} 的云端 visual 资源。",
                status=STATUS_BLOCKED,
                failure_reason="cloud_assembly_visual_asset_missing",
            )
        timeline = segment["timeline"]
        start_seconds = float(timeline["planned_start_seconds"])
        end_seconds = float(timeline["planned_end_seconds"])
        clip_duration = max(0.0, end_seconds - start_seconds)
        total_duration = max(total_duration, end_seconds)
        # MainTrack clips concatenate when TimelineIn/TimelineOut are omitted.
        # Use source-trim fields here so later clips do not overlap or run full length.
        clip = {
            "Type": media["clip_type"],
            "MediaURL": media["media_url"],
        }
        if media["clip_type"] == "Video":
            clip.update(
                {
                    "In": 0.0,
                    "MaxOut": clip_duration,
                }
            )
        if media["clip_type"] == "Image":
            clip.update(
                {
                    "Duration": clip_duration,
                    "X": 0.0,
                    "Y": 0.0,
                    "Width": 1.0,
                    "Height": 1.0,
                    "AdaptMode": "Cover",
                }
            )
        video_track_clips.append(clip)

    return {
        "VideoTracks": [
            {
                "MainTrack": True,
                "VideoTrackClips": video_track_clips,
            }
        ],
        "AudioTracks": [
            {
                "MainTrack": True,
                "AudioTrackClips": [
                    {
                        "MediaURL": upload_bundle["voiceover_url"],
                        "TimelineIn": 0.0,
                        "TimelineOut": total_duration,
                    }
                ],
            }
        ],
        "SubtitleTracks": [
            {
                "SubtitleTrackClips": [
                    {
                        "Type": "Subtitle",
                        "SubType": "srt",
                        "FileURL": upload_bundle["captions_url"],
                    }
                ]
            }
        ],
    }


def _resolve_cloud_project(config: dict[str, Any]) -> dict[str, str]:
    project_title = _normalize_optional_text(_nested_get(config, "aliyun_ims", "cloud_project_name"))
    if not project_title:
        raise CloudAssemblyError(
            "缺少 aliyun_ims.cloud_project_name，本轮无法定位北京区云剪工程。",
            status=STATUS_BLOCKED,
            failure_reason="cloud_project_name_missing",
        )

    payload = _call_aliyun_ice_openapi(
        action="ListEditingProjects",
        config=config,
        params={"PageNo": 1, "PageSize": 100},
    )
    projects = _extract_projects(payload)
    for project in projects:
        title = _normalize_optional_text(project.get("Title") or project.get("ProjectName"))
        if title == project_title and _normalize_optional_text(project.get("ProjectId")):
            return {
                "project_id": str(project["ProjectId"]),
                "project_title": title,
                "request_id": _normalize_optional_text(payload.get("RequestId")),
            }

    raise CloudAssemblyError(
        f"未在北京区找到云剪工程：{project_title}",
        status=STATUS_BLOCKED,
        failure_reason="cloud_project_not_found",
    )


def _update_editing_project(
    config: dict[str, Any],
    project_id: str,
    timeline: dict[str, Any],
) -> dict[str, str]:
    payload = _call_aliyun_ice_openapi(
        action="UpdateEditingProject",
        config=config,
        params={
            "ProjectId": project_id,
            "Timeline": json.dumps(timeline, ensure_ascii=False, separators=(",", ":")),
        },
    )
    return {"request_id": _normalize_optional_text(payload.get("RequestId"))}


def _submit_media_producing_job(
    config: dict[str, Any],
    project_id: str,
    output_media_config: dict[str, Any],
) -> dict[str, str | None]:
    payload = _call_aliyun_ice_openapi(
        action="SubmitMediaProducingJob",
        config=config,
        params={
            "ProjectId": project_id,
            "OutputMediaConfig": json.dumps(
                output_media_config,
                ensure_ascii=False,
                separators=(",", ":"),
            ),
        },
    )
    job_id = _extract_first_string(payload, "JobId", "MediaProducingJobId")
    if not job_id:
        raise CloudAssemblyError(
            "SubmitMediaProducingJob 返回中缺少 JobId。",
            failure_reason="cloud_assembly_job_id_missing",
        )
    return {
        "job_id": job_id,
        "media_id": _extract_first_string(payload, "MediaId"),
        "request_id": _normalize_optional_text(payload.get("RequestId")),
    }


def _poll_media_producing_job(
    config: dict[str, Any],
    job_id: str,
) -> dict[str, str | None]:
    polling = _nested_get(config, "polling") or {}
    interval_seconds = float(polling.get("interval_seconds") or 5)
    timeout_seconds = float(polling.get("timeout_seconds") or 600)
    started_at = time.time()

    while True:
        payload = _call_aliyun_ice_openapi(
            action="GetMediaProducingJob",
            config=config,
            params={"JobId": job_id},
        )
        job_status = _normalize_job_status(
            _extract_first_string(payload, "Status", "JobStatus") or ""
        )
        request_id = _normalize_optional_text(payload.get("RequestId"))
        media_url = _extract_first_string(payload, "MediaURL", "OutputMediaURL", "FileURL")
        media_id = _extract_first_string(payload, "MediaId")

        if job_status == STATUS_SUCCESS:
            return {
                "request_id": request_id,
                "media_id": media_id,
                "media_url": media_url,
            }
        if job_status == STATUS_FAILED:
            raise CloudAssemblyError(
                _extract_first_string(payload, "Message", "ErrorMessage") or f"云端合成作业失败：{job_id}",
                failure_reason="cloud_assembly_job_failed",
            )
        if time.time() - started_at >= timeout_seconds:
            raise CloudAssemblyError(
                f"云端合成作业轮询超时：{job_id}",
                failure_reason="cloud_assembly_job_poll_timeout",
            )
        time.sleep(interval_seconds)


def _build_output_target(config: dict[str, Any], run_id: str) -> dict[str, Any]:
    bucket = _nested_get(config, "aliyun_oss", "bucket")
    object_key = _build_object_key(
        _nested_get(config, "aliyun_oss", "prefix_final"),
        run_id,
        "formal_api_demo.mp4",
    )
    width, height = _parse_resolution(_nested_get(config, "assembly", "resolution"))
    media_url = _build_oss_https_url(config, object_key)
    return {
        "object_key": object_key,
        "media_url": media_url,
        "oss_url": f"oss://{bucket}/{object_key}",
        "output_media_config": {
            "MediaURL": media_url,
            "Width": width,
            "Height": height,
        },
    }


def _upload_file_to_oss(
    local_path: pathlib.Path,
    object_key: str,
    config: dict[str, Any],
) -> None:
    bucket = _nested_get(config, "aliyun_oss", "bucket")
    endpoint = _nested_get(config, "aliyun_oss", "endpoint")
    access_key_id = _nested_get(config, "aliyun_oss", "access_key_id")
    access_key_secret = _nested_get(config, "aliyun_oss", "access_key_secret")
    if not all([bucket, endpoint, access_key_id, access_key_secret]):
        raise CloudAssemblyError(
            "OSS 上传配置不完整，无法继续执行 cloud assembly。",
            status=STATUS_BLOCKED,
            failure_reason="aliyun_oss_upload_config_incomplete",
        )

    payload = local_path.read_bytes()
    content_type = mimetypes.guess_type(local_path.name)[0] or "application/octet-stream"
    request_url = f"https://{bucket}.{endpoint}/{urllib.parse.quote(object_key, safe='/~')}"
    http_date = _http_date()
    string_to_sign = "\n".join(
        [
            "PUT",
            "",
            content_type,
            http_date,
            f"/{bucket}/{object_key}",
        ]
    )
    signature = base64.b64encode(
        hmac.new(
            str(access_key_secret).encode("utf-8"),
            string_to_sign.encode("utf-8"),
            hashlib.sha1,
        ).digest()
    ).decode("utf-8")
    request = urllib.request.Request(
        request_url,
        data=payload,
        headers={
            "Date": http_date,
            "Content-Type": content_type,
            "Authorization": f"OSS {access_key_id}:{signature}",
        },
        method="PUT",
    )
    try:
        with urllib.request.urlopen(request, timeout=120):
            return
    except urllib.error.HTTPError as exc:
        raise CloudAssemblyError(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
            failure_reason="aliyun_oss_put_object_failed",
        ) from exc
    except urllib.error.URLError as exc:
        raise CloudAssemblyError(
            str(exc.reason or exc),
            error_code="UrlOpenError",
            failure_reason="aliyun_oss_put_object_failed",
        ) from exc


def _download_oss_object(
    signed_url: str,
    destination: pathlib.Path,
    config: dict[str, Any],
) -> None:
    request = urllib.request.Request(signed_url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:
        raise CloudAssemblyError(
            _sanitize_message(_read_urllib_error_message(exc), config),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
            failure_reason="aliyun_oss_download_output_failed",
        ) from exc
    except urllib.error.URLError as exc:
        raise CloudAssemblyError(
            _sanitize_message(str(exc.reason or exc), config),
            error_code="UrlOpenError",
            failure_reason="aliyun_oss_download_output_failed",
        ) from exc
    if not payload:
        raise CloudAssemblyError(
            "云剪导出文件下载为空。",
            failure_reason="aliyun_oss_download_output_empty",
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)


def _sanitize_uploaded_assets(
    uploaded_assets: list[dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    sanitized_assets: list[dict[str, Any]] = []
    for asset in uploaded_assets:
        sanitized = dict(asset)
        media_url = _normalize_optional_text(sanitized.get("media_url"))
        if media_url:
            sanitized["media_url"] = _sanitize_media_url(media_url, config)
        sanitized_assets.append(sanitized)
    return sanitized_assets


def _sanitize_timeline_urls(value: Any, config: dict[str, Any]) -> Any:
    if isinstance(value, dict):
        return {
            key: _sanitize_media_url(item, config)
            if key in {"MediaURL", "FileURL"} and isinstance(item, str)
            else _sanitize_timeline_urls(item, config)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_sanitize_timeline_urls(item, config) for item in value]
    return value


def _sanitize_media_url(media_url: str, config: dict[str, Any]) -> str:
    sanitized = _sanitize_message(media_url, config)
    if "?" in sanitized:
        return sanitized.split("?", 1)[0] + "?<redacted_signature>"
    return sanitized


def _build_oss_signed_get_url(
    config: dict[str, Any],
    object_key: str,
    expires_seconds: int,
) -> str:
    bucket = _nested_get(config, "aliyun_oss", "bucket")
    access_key_id = _nested_get(config, "aliyun_oss", "access_key_id")
    access_key_secret = _nested_get(config, "aliyun_oss", "access_key_secret")
    expires_at = int(time.time()) + int(expires_seconds)
    string_to_sign = "\n".join(
        [
            "GET",
            "",
            "",
            str(expires_at),
            f"/{bucket}/{object_key}",
        ]
    )
    signature = base64.b64encode(
        hmac.new(
            str(access_key_secret).encode("utf-8"),
            string_to_sign.encode("utf-8"),
            hashlib.sha1,
        ).digest()
    ).decode("utf-8")
    base_url = _build_oss_https_url(config, object_key)
    query = urllib.parse.urlencode(
        {
            "OSSAccessKeyId": access_key_id,
            "Expires": expires_at,
            "Signature": signature,
        }
    )
    return f"{base_url}?{query}"


def _call_aliyun_ice_openapi(
    action: str,
    config: dict[str, Any],
    params: dict[str, Any],
) -> dict[str, Any]:
    access_key_id = _nested_get(config, "aliyun_oss", "access_key_id")
    access_key_secret = _nested_get(config, "aliyun_oss", "access_key_secret")
    region = _nested_get(config, "aliyun_ims", "region") or "cn-beijing"
    endpoint = ALIYUN_ICE_ENDPOINT_TEMPLATE.format(region=region)
    request_params = {
        "Action": action,
        "AccessKeyId": access_key_id,
        "Format": "JSON",
        "SignatureMethod": "HMAC-SHA1",
        "SignatureNonce": str(uuid.uuid4()),
        "SignatureVersion": "1.0",
        "Timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "Version": ALIYUN_ICE_API_VERSION,
    }
    for key, value in params.items():
        if value is None:
            continue
        request_params[key] = _stringify_param(value)
    request_params["Signature"] = _sign_rpc_request(
        method="POST",
        params=request_params,
        access_key_secret=str(access_key_secret),
    )
    encoded_body = _encode_rpc_params(request_params).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=encoded_body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    payload = _json_request(request)
    if payload.get("Code") and payload.get("Message"):
        raise CloudAssemblyError(
            f"{payload['Code']}: {payload['Message']}",
            failure_reason=f"aliyun_ice_{action.lower()}_failed",
        )
    return payload


def _json_request(request: urllib.request.Request) -> dict[str, Any]:
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        raise CloudAssemblyError(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
        ) from exc
    except urllib.error.URLError as exc:
        raise CloudAssemblyError(
            str(exc.reason or exc),
            error_code="UrlOpenError",
        ) from exc
    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise CloudAssemblyError(
            "阿里云接口返回了无效 JSON。",
            error_code="InvalidJson",
        ) from exc


def _sign_rpc_request(method: str, params: dict[str, Any], access_key_secret: str) -> str:
    canonical_query = _encode_rpc_params(params)
    string_to_sign = "&".join(
        [
            method.upper(),
            _rpc_percent_encode("/"),
            _rpc_percent_encode(canonical_query),
        ]
    )
    digest = hmac.new(
        f"{access_key_secret}&".encode("utf-8"),
        string_to_sign.encode("utf-8"),
        hashlib.sha1,
    ).digest()
    return base64.b64encode(digest).decode("utf-8")


def _encode_rpc_params(params: dict[str, Any]) -> str:
    parts: list[str] = []
    for key, value in sorted(params.items(), key=lambda item: item[0]):
        parts.append(f"{_rpc_percent_encode(key)}={_rpc_percent_encode(_stringify_param(value))}")
    return "&".join(parts)


def _rpc_percent_encode(value: Any) -> str:
    return urllib.parse.quote(str(value), safe="~")


def _extract_projects(payload: dict[str, Any]) -> list[dict[str, Any]]:
    projects: list[dict[str, Any]] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            if "ProjectId" in node and ("Title" in node or "ProjectName" in node):
                projects.append(node)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(payload)
    return projects


def _extract_first_string(payload: Any, *keys: str) -> str | None:
    if isinstance(payload, dict):
        for key in keys:
            value = payload.get(key)
            if value not in (None, ""):
                return str(value)
        for value in payload.values():
            candidate = _extract_first_string(value, *keys)
            if candidate:
                return candidate
    elif isinstance(payload, list):
        for item in payload:
            candidate = _extract_first_string(item, *keys)
            if candidate:
                return candidate
    return None


def _normalize_job_status(value: str) -> str:
    normalized = value.strip().lower()
    if normalized in {"success", "succeeded", "finished", "completed", "complete"}:
        return STATUS_SUCCESS
    if normalized in {"fail", "failed", "error", "cancelled", "canceled"}:
        return STATUS_FAILED
    return "running"


def _build_object_key(prefix: Any, run_id: str, relative_name: str) -> str:
    normalized_prefix = _normalize_prefix(prefix)
    return f"{normalized_prefix}{run_id}/{relative_name.lstrip('/')}"


def _build_oss_https_url(config: dict[str, Any], object_key: str) -> str:
    bucket_domain = _nested_get(config, "aliyun_oss", "bucket_domain")
    return f"https://{bucket_domain}/{urllib.parse.quote(object_key, safe='/~')}"


def _normalize_prefix(value: Any) -> str:
    normalized = str(value or "").strip().strip("/")
    if not normalized:
        return ""
    return normalized + "/"


def _build_run_id() -> str:
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())


def _parse_resolution(value: Any) -> tuple[int, int]:
    raw = str(value or "1080x1920").strip().lower()
    if "x" not in raw:
        return 1080, 1920
    width, height = raw.split("x", 1)
    try:
        return int(width), int(height)
    except ValueError:
        return 1080, 1920


def _require_local_path(value: Any, *, label: str) -> pathlib.Path:
    normalized = _normalize_optional_text(value)
    if not normalized:
        raise CloudAssemblyError(
            f"缺少 {label} 本地路径，当前无法继续云端 assembly。",
            status=STATUS_BLOCKED,
            failure_reason=f"{label}_path_missing",
        )
    path = pathlib.Path(normalized)
    if not path.exists() or not path.is_file():
        raise CloudAssemblyError(
            f"{label} 文件不存在：{normalized}",
            status=STATUS_BLOCKED,
            failure_reason=f"{label}_path_missing",
        )
    return path


def _read_urllib_error_message(exc: urllib.error.HTTPError) -> str:
    body = ""
    if exc.fp is not None:
        try:
            body = exc.read().decode("utf-8", errors="replace").strip()
        except Exception:
            body = ""
    return body or str(exc)


def _http_date() -> str:
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())


def _write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _stringify_param(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _normalize_optional_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _nested_get(payload: dict[str, Any], *keys: str) -> Any:
    current: Any = payload
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _sanitize_message(message: str, config: dict[str, Any]) -> str:
    sanitized = message.strip()
    for secret_value in (
        _nested_get(config, "auth", "api_key"),
        _nested_get(config, "aliyun_oss", "access_key_id"),
        _nested_get(config, "aliyun_oss", "access_key_secret"),
    ):
        normalized = _normalize_optional_text(secret_value)
        if normalized:
            sanitized = sanitized.replace(normalized, "***")
    return sanitized[:500]
