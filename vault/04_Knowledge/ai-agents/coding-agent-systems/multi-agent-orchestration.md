---
id: "nahida-knowledge-multi-agent-orchestration"
title: "Multi-agent orchestration"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "multi-agent-orchestration"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "multi-agent-orchestration"
primary_ontology_path: "ai-agents/coding-agent-systems/multi-agent-orchestration"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-multi-agent-orchestration"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/multi-agent-orchestration.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-multi-agent-orchestration"
    relation: "evidenced_by"
    to: "vault/03_Sources/github/openai-codex-main-f959e7f.md"
    evidence_refs:
      - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-tool-parallelism-to-multi-agent-orchestration"
source_note_refs:
  - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
representative_source_refs:
  - "github:openai/codex@f959e7fc9832dfa0ebfb6542ab1bbf829638ac24"
query_keys:
  - "multi-agent orchestration"
  - "sub-agent thread tree"
  - "AgentControl"
  - "multi-agent v2"
  - "agent mailbox"
aliases:
  - "multi-agent"
  - "subagent orchestration"
domains:
  - "ai-agents"
topics:
  - "multi-agent"
  - "subagents"
  - "mailbox"
  - "agent-control"
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

# Multi-agent orchestration

## 定义

Multi-agent orchestration is the control-plane layer that creates and manages sub-agent identities, threads, status, capacity, path references, communication, and follow-up scheduling.

## Codex Pattern

| Mechanism | Evidence | Interpretation |
| --- | --- | --- |
| Shared control plane | `AgentControl` is created once per root thread/session tree and shared by sub-agents (`agent/control.rs:89-108`). | Multi-agent state is scoped to the root tree, not global process state. |
| Thread identity and capacity | `spawn_agent_internal` resolves version, checks capacity, reserves V2 residency/spawn slots and inherits environments/exec policy (`agent/control/spawn.rs:197-244`). | Sub-agent creation is resource controlled. |
| Communication | `send_inter_agent_communication` sends `Op::InterAgentCommunication` and tracks last task message (`agent/control.rs:184-205`). | Messages are first-class operations. |
| Path references | `resolve_agent_reference` resolves relative `AgentPath` to thread id (`agent/control.rs:286-305`). | Tools can target agents by stable task path. |
| V2 tools | `spawn_agent`, `send_message`, `followup_task`, `wait_agent`, `list_agents`, `interrupt_agent` are registered by `spec_plan.rs:795-848`. | Model tool surface maps to control-plane operations. |
| Prompt mode | `MultiAgentModeInstructions` injects explicit-only/proactive developer text, while `none` omits instructions (`context/multi_agent_mode_instructions.rs:6-43`). | Tool availability and prompt encouragement are separate. |
| Mailbox wait | V2 `wait_agent` waits for mailbox/steer activity rather than only final target status (`multi_agents_v2/wait.rs:37-111`). | V2 is more message/activity oriented than V1 target-status waiting. |

## Difference From Tool Parallelism

Tool parallelism overlaps handler execution inside one turn. Multi-agent orchestration creates or addresses independent live threads with their own turn loops and mailbox delivery. A spawned sub-agent can outlive a single tool call, hold status, receive follow-up tasks, and be resumed or listed.

## Reusable Insight

Multi-agent systems need identity, residency/capacity, path resolution, status subscription, and mailbox semantics before "parallel agents" become debuggable. Without those, "spawn a worker" is just another opaque tool call.

## Evidence Boundary

This node is Codex-specific and especially V2-specific. External multi-agent frameworks may use graph schedulers or actor pools rather than thread-tree control.
