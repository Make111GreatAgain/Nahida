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
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
representative_source_refs:
  - "github:openai/codex@f959e7fc9832dfa0ebfb6542ab1bbf829638ac24"
query_keys:
  - "agent safety harness"
  - "permission harness"
  - "ToolOrchestrator"
  - "guardian review"
  - "sandbox retry"
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
last_synthesized: "2026-06-24"
valid_until: "2026-07-24"
evidence_window_start: "2026-06-24"
evidence_window_end: "2026-06-24"
created: "2026-06-24"
updated: "2026-06-24"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260624-openai-codex"
source_refs:
  - "github:openai/codex@f959e7fc9832dfa0ebfb6542ab1bbf829638ac24"
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

## Boundary

This is a runtime safety harness, not a full formal security proof. The source shows mechanisms and tests, not empirical escape resistance.
