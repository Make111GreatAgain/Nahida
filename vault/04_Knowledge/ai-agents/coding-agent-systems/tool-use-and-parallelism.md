---
id: "nahida-knowledge-tool-use-and-parallelism"
title: "Tool use and parallelism"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "tool-use-and-parallelism"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "tool-use-and-parallelism"
primary_ontology_path: "ai-agents/coding-agent-systems/tool-use-and-parallelism"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-tool-use-and-parallelism"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/tool-use-and-parallelism.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-tool-use-and-parallelism"
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
  - "tool use and parallelism"
  - "parallel tool calls"
  - "tool runtime"
  - "ToolCallRuntime"
  - "tool_search deferred tools"
aliases:
  - "tool-use engineering"
domains:
  - "ai-agents"
topics:
  - "tool-use"
  - "parallel-tool-calls"
  - "tool-routing"
  - "deferred-tools"
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

# Tool use and parallelism

## 定义

Tool-use engineering covers how model-visible tool specs are planned, how model response items are parsed into runtime calls, how handlers are registered, how hooks/telemetry/safety wrap execution, and how same-turn tool calls are optionally parallelized.

## Codex Pattern

| Mechanism | Evidence | Detail |
| --- | --- | --- |
| Tool planning | `built_tools` loads MCP, plugins, apps/connectors, discoverable tools, extension executors and dynamic tools (`turn.rs:1162-1294`). | Tool list is per-step and config/model/provider dependent. |
| Exposure model | `ToolExposure` has `Direct`, `Deferred`, `DirectModelOnly`, `Hidden` (`tools/src/tool_executor.rs:13-36`). | Tools can be dispatchable without being initially model-visible. |
| Deferred discovery | `tool_search` is added from deferred tools' `search_info` and uses BM25 (`tool_search.rs:25-94`; `spec_plan.rs:968-989`). | Large tool surfaces can be lazily loaded. |
| Call parsing | `ToolRouter::build_tool_call` maps function calls, client tool_search calls, and custom tool calls (`router.rs:112-160`). | Model events become typed runtime calls. |
| Registry lifecycle | `ToolRegistry` runs pre hooks, handler telemetry, post hooks and lifecycle events (`registry.rs:433-669`). | Tool execution has observable gates before and after handler work. |
| Parallel prompt flag | `build_prompt` sets `parallel_tool_calls` from model info (`turn.rs:1028-1039`). | Model capability is advertised explicitly. |
| Parallel runtime gate | `ToolCallRuntime` takes read locks for parallel-safe tools and write locks for unsafe tools (`parallel.rs:89-121`). | Runtime enforces handler capability even if model emits concurrent calls. |

## Parallelism Rule

Default tool executors are not parallel-safe (`ToolExecutor::supports_parallel_tool_calls` returns false). Handlers must opt in. In Codex:

- `exec_command` opts in.
- MCP tools opt in through server metadata or read-only annotation.
- MCP resource reads and `tool_search` opt in.
- Hidden exposure suppresses parallel support through `ExposureOverride`.

## Important Boundary

Parallel tool calls are same-turn runtime tasks. They do not create new agent identity, a new thread, a mailbox, or an independent turn. That boundary is captured in [[tool-parallelism-to-multi-agent-orchestration|Tool parallelism -> multi-agent orchestration]].

## Harness Evidence

`core/tests/suite/tool_parallelism.rs` verifies parallel execution timing, mixed parallel tools, output grouping/order, and tools starting before a delayed `response.completed`.

## Reusable Insight

Model-level parallel tool support should be treated as permission to emit multiple tool calls, not as a guarantee that every handler is safe to run concurrently. Runtime still needs per-tool capability and serialization semantics.
