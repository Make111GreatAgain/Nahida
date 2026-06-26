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
  - from: "nahida-knowledge-agent-loop-engineering"
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
  - "agent loop engineering"
  - "agent turn loop"
  - "sampling tool feedback loop"
  - "Codex run_turn"
  - "OpenClaw runEmbeddedAgent"
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

## OpenClaw Pattern

OpenClaw adds a Gateway-shaped loop around the model/tool feedback loop:

| Layer | OpenClaw evidence | Role |
| --- | --- | --- |
| Gateway method | `agent` validates message, agent id, provider/model, session key, delivery target, channel/thread/group, prompt mode, attachments, timeouts, approval followups and idempotency key. | Converts external/channel ingress into a typed Gateway transaction. |
| Dedupe and lifecycle | The handler uses idempotency key as run id, builds lifecycle metadata, records input provenance, and returns cached accepted/final results when dedupe keys match. | Makes agent runs retry-safe from clients/channels. |
| Embedded runtime | `runEmbeddedAgent` resolves/backfills session keys, session file, session/global lanes, queue priority, run context, workspace and runtime plugins. | Serializes per-session state and prepares run-local environment. |
| Model/runtime resolution | The runtime resolves explicit/default/alias model, provider, harness, auth profile and context engine before attempts. | Keeps provider/runtime/harness pluggable. |
| Attempt loop | Runtime plan, prompt additions, context engine assembly, tool construction and `runEmbeddedAttemptWithBackend` are retried with compaction/fallback logic. | Keeps model calls, tools and compaction inside one managed lifecycle. |
| Streaming/persistence | Gateway events, reply shaping, JSONL session entries, compaction adoption and session lifecycle hooks are emitted around the attempt. | Couples user-visible streams with durable transcript state. |

## Comparison

Codex's loop is centered inside a local session: `submission_loop` receives operations and `run_turn` owns sampling, tool feedback, pending input and compaction. OpenClaw puts a daemonized Gateway in front of the same kind of loop, so external surfaces get accepted/final dedupe, channel delivery metadata, session lanes, runtime plugin loading, provider/harness choice and context-engine ownership before the model call happens.

Reusable distinction: Codex is an excellent reference for the inner coding-agent loop; OpenClaw is an excellent reference for wrapping that loop as an always-on multi-channel service.

## Reusable Insight

Agent systems should keep "external submission routing", "turn execution", and "model sampling/tool feedback" as separate layers. This makes it easier to reason about cancellation, approvals, mailbox traffic, compaction, and tool output ordering.

## Evidence Boundary

The node is backed by Codex core runtime and a scoped OpenClaw runtime read. More frameworks are still needed for general claims.
