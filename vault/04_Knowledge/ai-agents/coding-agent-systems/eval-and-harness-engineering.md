---
id: "nahida-knowledge-eval-and-harness-engineering"
title: "Eval and harness engineering"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "eval-and-harness-engineering"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "eval-and-harness-engineering"
primary_ontology_path: "ai-agents/coding-agent-systems/eval-and-harness-engineering"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-eval-and-harness-engineering"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/eval-and-harness-engineering.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-eval-and-harness-engineering"
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
  - "eval and harness engineering"
  - "agent test harness"
  - "mock Responses SSE"
  - "Codex integration tests"
aliases:
  - "harness engineering"
  - "agent evaluation harness"
domains:
  - "ai-agents"
topics:
  - "eval"
  - "harness"
  - "integration-tests"
  - "mock-model"
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

# Eval and harness engineering

## 定义

Eval and harness engineering for agents is the test infrastructure that can drive synthetic model responses, capture outgoing model requests, assert context/tool/event shape, simulate tool outputs and streaming delays, and cover safety/context/multi-agent regressions.

## Codex Pattern

| Harness component | Evidence | Role |
| --- | --- | --- |
| TestCodex builder | `core/tests/common/test_codex.rs` creates temp local/remote environments and configured `CodexThread` instances. | Reusable runtime fixture. |
| Mock Responses server | `core/tests/common/responses.rs` captures request bodies, decodes zstd, exposes instructions, inputs and tools. | Assertions see what the model actually received. |
| Synthetic streams | SSE helpers emit created/function_call/assistant/completed events. | Tests model-event order without real model calls. |
| Parallelism tests | `tool_parallelism.rs` uses barriers/sleeps and delayed stream completion. | Tests concurrency and output ordering. |
| Multi-agent prompt tests | `multi_agent_mode.rs` checks sticky mode and developer fragment injection/omission. | Tests prompt state, not just tool implementation. |
| Broad suite coverage | `core/tests/suite/*` covers approvals, hooks, MCP, skills, request permissions, guardian, compaction, token budget, shell, sandbox and model switching. | Treats agent behavior as integration contracts. |

## Reusable Insight

Agent eval harnesses should assert the request sent to the model and the protocol events emitted by the runtime. Unit tests of helper functions are insufficient because many agent regressions are context-shape, stream-order, approval, or tool-output replay bugs.

## Boundary

This node records engineering harness patterns. It does not record benchmark results for model quality or task success.
