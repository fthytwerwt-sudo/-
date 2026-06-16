# Adapter Integration Candidate

This directory is a branch-local, no-render adapter candidate for the
`adapter/agent-service-toolkit-sandbox` branch.

It provides:

- workflow registry for six required candidate workflows
- TaskPacket shape for routing evidence
- task cleaner and workflow router for the six required sample inputs
- contract validator that reuses the existing editing workflow no-render probe
- no-render editing runner
- completion truth guards for false completion claims
- CLI runner:

```bash
python3 -m codex_source.adapter_integration.no_render_adapter_runner --sample all
```

Boundaries:

- no media generation
- no TTS call
- no real media read
- no external API call
- no real DashVector call
- no Chroma ingestion
- no runtime enablement
- no service startup
- no main branch modification

The only valid stopline for this directory is:

```text
adapter_branch_integration_candidate_ready_for_runtime_probe
```
