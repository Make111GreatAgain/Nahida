---
id: "nahida-knowledge-safety-and-permission-harness"
title: "Safety and permission harness"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "safety-and-permission-harness"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "safety-and-permission-harness"
primary_ontology_path: "ai-agents/coding-agent-systems/safety-and-permission-harness"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-safety-and-permission-harness"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/safety-and-permission-harness.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-safety-and-permission-harness"
    relation: "evidenced_by"
    to: "vault/03_Sources/github/openai-codex-main-f959e7f.md"
    evidence_refs:
      - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-safety-and-permission-harness"
    relation: "evidenced_by"
    to: "vault/03_Sources/github/openclaw-openclaw-main-751a6c2.md"
    evidence_refs:
      - "vault/03_Sources/github/openclaw-openclaw-main-751a6c2.md"
    confidence: "medium-high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
  - "vault/03_Sources/github/openclaw-openclaw-main-751a6c2.md"
representative_source_refs:
  - "github:openai/codex@f959e7fc9832dfa0ebfb6542ab1bbf829638ac24"
  - "github:openclaw/openclaw@751a6c23f098e16a82f4afe7d4d674df1412a968"
query_keys:
  - "agent safety harness"
  - "permission harness"
  - "ToolOrchestrator"
  - "guardian review"
  - "sandbox retry"
  - "OpenClaw pairing"
  - "OpenClaw sandbox bridge"
aliases:
  - "agent safety policy"
domains:
  - "ai-agents"
topics:
  - "safety"
  - "permissions"
  - "sandboxing"
  - "guardian"
  - "execpolicy"
tags:
  - "nahida/knowledge"
  - "nahida/topic"
freshness_status: "fresh"
last_synthesized: "2026-06-26"
valid_until: "2026-07-26"
evidence_window_start: "2026-06-24"
evidence_window_end: "2026-06-26"
created: "2026-06-24"
updated: "2026-06-26"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260624-openai-codex"
  - "nahida-knowledge-20260626-openclaw"
source_refs:
  - "github:openai/codex@f959e7fc9832dfa0ebfb6542ab1bbf829638ac24"
  - "github:openclaw/openclaw@751a6c23f098e16a82f4afe7d4d674df1412a968"
confidence: "high"
trust_tier: "primary"
---

# Safety and permission harness

## 定义

Safety and permission harness is the execution-time control layer that decides whether a tool can run, under what sandbox and network constraints, who approves escalation, and how denials/retries are represented to the model and user.

## Codex Pattern

| Safety layer | Evidence | Role |
| --- | --- | --- |
| Approval requirement | `ToolOrchestrator::run` derives tool-specific or default exec approval requirement (`orchestrator.rs:154-158`). | Determines skip, forbidden, or needs approval. |
| Guardian/user routing | strict auto-review and guardian routing are computed before approval (`orchestrator.rs:145-150`). | Allows automated reviewer or user as decision source. |
| Permission hooks | PermissionRequest hooks take top precedence before guardian/user path (`orchestrator.rs:510-575`). | Configured policy can approve/deny programmatically. |
| Sandbox selection | First attempt selects sandbox from filesystem/network policy and sandbox preference (`orchestrator.rs:223-277`). | Execution environment is policy-derived. |
| Network approval | `run_attempt` begins and finalizes immediate/deferred network approval (`orchestrator.rs:61-132`). | Network denials become auditable approval contexts. |
| Retry/escalation | Sandbox denial may trigger fresh approval and retry with a different sandbox strategy (`orchestrator.rs:297-493`). | Escalation is explicit and telemetry-recorded. |
| Request permissions tool | `request_permissions` normalizes additional permissions and waits for host response (`request_permissions.rs:42-120`). | Model can ask for broader permissions through a controlled surface. |
| Exec policy | `Policy` stores prefix and network rules; rules include decisions and justifications (`execpolicy/src/policy.rs:28-134`; `rule.rs:37-115`). | Command/network allow/deny/prompt is declarative. |

## Reusable Insight

Agent safety should be close to execution orchestration, not scattered across handlers. Codex demonstrates a layered path where hooks, guardian/user approval, sandbox choice, managed network, and retry semantics are all visible to one orchestrator.

## OpenClaw Pattern

OpenClaw splits safety across Gateway, runtime policy and sandboxing:

| Safety layer | OpenClaw evidence | Role |
| --- | --- | --- |
| Pairing/auth | README and Gateway protocol describe DM security defaults, pairing approvals, role/scope handshake and device signatures. | Controls who can invoke the local personal agent over channels/devices. |
| Gateway method authorization | `agent` handler authorizes model overrides and internal session effects, validates approval followups and tracks idempotency. | Prevents clients from freely changing runtime-critical fields. |
| Effective tool policy | Tool policy combines config, session, agent, provider/model, group and subagent capability layers. | Makes tool availability contextual. |
| Subagent denylists | Subagents have always-denied and leaf-denied tools plus inherited capabilities. | Delegated agents do not automatically inherit root privileges. |
| Before-tool hooks | `before_tool_call` applies plugin hooks, trusted policies, approvals, diagnostics, loop detection and telemetry. | Centralizes final pre-execution checks. |
| Sandbox bridge | Sandbox context/registry/filesystem bridge creates per-run layouts, mounts and guarded host path operations. | Separates sandbox workspace from host filesystem authority. |

Comparison: Codex concentrates safety in `ToolOrchestrator` around exec/network/sandbox/retry; OpenClaw adds an outer Gateway security boundary and broader channel/subagent policy layers.

## Boundary

This is a runtime safety harness, not a full formal security proof. The source shows mechanisms and tests, not empirical escape resistance.
