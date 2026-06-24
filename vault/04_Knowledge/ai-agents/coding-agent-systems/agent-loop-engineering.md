---
id: "nahida-knowledge-agent-loop-engineering"
title: "Agent loop engineering"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "agent-loop-engineering"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "agent-loop-engineering"
primary_ontology_path: "ai-agents/coding-agent-systems/agent-loop-engineering"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-agent-loop-engineering"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/agent-loop-engineering.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-agent-loop-engineering"
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
  - "agent loop engineering"
  - "agent turn loop"
  - "sampling tool feedback loop"
  - "Codex run_turn"
aliases:
  - "loop engineering"
domains:
  - "ai-agents"
topics:
  - "agent-loop"
  - "turn-loop"
  - "sampling-loop"
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

# Agent loop engineering

## 定义

Agent loop engineering is the design of the control loop that turns user/host submissions into model requests, tool execution, model-visible tool outputs, pending-input handling, stop hooks, and context compaction.

## Codex Pattern

| Layer | Codex evidence | Role |
| --- | --- | --- |
| Submission loop | `submission_loop` dispatches `Op::UserInput`, `InterAgentCommunication`, approvals, dynamic tool responses, compact, review, shutdown (`session/handlers.rs:705-858`). | Serializes external operations into session behavior. |
| Turn spawning | `user_input_or_turn_inner` tries to steer an active turn; if none, merges additional context and `spawn_task`s a regular task (`session/handlers.rs:186-268`). | Decides whether input joins current work or starts a new turn. |
| Turn loop | `run_turn` records context, skills/plugins, hooks, then loops sampling until no follow-up or blocked/aborted (`session/turn.rs:150-380`). | Main agent loop. |
| Sampling | `run_sampling_request` builds tools, base instructions, prompt and retries stream errors (`session/turn.rs:1057-1151`). | Model request loop. |
| Streaming and tool feedback | `try_run_sampling_request` streams events, handles completed output items, starts tool futures, then feeds tool output into future sampling (`session/turn.rs:1871-2053`). | Converts model events to runtime effects. |
| Context pressure | mid-turn compaction runs when follow-up is needed and token limit/new context is reached (`session/turn.rs:334-357`). | Prevents infinite or overflowing loops. |

## 核心机制

- A turn is not one model call; it can be multiple sampling requests separated by tool outputs and compaction.
- Pending user input and mailbox input are checked after sampling, not blindly interleaved into the first request.
- `StepContext` is captured once so advertised tools and tool dispatch use the same request view.
- Stop hooks can block completion and inject continuation fragments.
- The loop records token usage, rate limits, telemetry, turn diff, lifecycle events and rollout persistence.

## Reusable Insight

Agent systems should keep "external submission routing", "turn execution", and "model sampling/tool feedback" as separate layers. This makes it easier to reason about cancellation, approvals, mailbox traffic, compaction, and tool output ordering.

## Evidence Boundary

The node is backed by Codex core runtime only. Comparative loop designs need additional sources.
