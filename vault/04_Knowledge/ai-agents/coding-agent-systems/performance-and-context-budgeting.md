---
id: "nahida-knowledge-performance-and-context-budgeting"
title: "Performance and context budgeting"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "performance-and-context-budgeting"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "performance-and-context-budgeting"
primary_ontology_path: "ai-agents/coding-agent-systems/performance-and-context-budgeting"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-performance-and-context-budgeting"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/performance-and-context-budgeting.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-performance-and-context-budgeting"
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
  - "agent performance optimization"
  - "context budgeting"
  - "auto compaction"
  - "tool output truncation"
  - "startup prewarm"
aliases:
  - "agent performance"
  - "context budget"
domains:
  - "ai-agents"
topics:
  - "performance"
  - "context-budget"
  - "compaction"
  - "prewarm"
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

# Performance and context budgeting

## 定义

Performance and context budgeting covers latency, startup work, repeated discovery, model transport reuse, tool execution overlap, context-window management, output truncation, and retry behavior in agent runtimes.

## Codex Pattern

| Mechanism | Evidence | Effect |
| --- | --- | --- |
| Startup parallel futures | Session init kicks off thread persistence, state DB and auth/MCP futures, then `tokio::join!`s them (`session/session.rs:573-687`). | Reduces startup latency. |
| Plugin/skill warmup | `warm_plugins_and_skills_for_session_init` loads plugin skill roots and skill snapshots (`session/session.rs:447-466`). | Avoids first-turn cold cost. |
| Turn-scoped model session | `ModelClientSession` is reused across retries in a turn because it caches WebSocket and sticky routing state (`session/turn.rs:210-216`). | Reduces retry overhead. |
| Retry handling | `run_sampling_request` honors provider `stream_max_retries` (`turn.rs:1084-1150`). | Recovers transient stream errors. |
| Tool concurrency | `ToolCallRuntime` spawns tasks and uses read/write lock gating (`tools/parallel.rs:115-135`). | Overlaps safe tools while preserving serialization. |
| Auto compaction | pre-sampling/mid-turn compaction can use token-budget, remote, remote v2, or local compaction (`turn.rs:902-975`, `:334-357`). | Keeps long loops under context limits. |
| Output truncation | MCP outputs are headered and truncated before model reinjection (`tools/context.rs:113-143`). | Prevents unbounded tool output. |
| Search/cache | Tool search handler and skills service cache repeated discovery state (`tool_search.rs:31-58`; `core-skills/src/service.rs:65-148`). | Avoids repeated indexing/scanning. |

## Reusable Insight

Agent performance work is not only model latency. It includes startup concurrency, discovery caching, bounded context artifacts, tool output truncation, compaction strategy, runtime parallelism, and transport reuse.

## Boundary

This node records implementation techniques, not measured production latency numbers.
