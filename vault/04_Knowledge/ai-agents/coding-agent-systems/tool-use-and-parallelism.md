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
  - from: "nahida-knowledge-tool-use-and-parallelism"
    relation: "evidenced_by"
    to: "vault/03_Sources/github/openclaw-openclaw-main-751a6c2.md"
    evidence_refs:
      - "vault/03_Sources/github/openclaw-openclaw-main-751a6c2.md"
    confidence: "medium-high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-tool-parallelism-to-multi-agent-orchestration"
source_note_refs:
  - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
  - "vault/03_Sources/github/openclaw-openclaw-main-751a6c2.md"
representative_source_refs:
  - "github:openai/codex@f959e7fc9832dfa0ebfb6542ab1bbf829638ac24"
  - "github:openclaw/openclaw@751a6c23f098e16a82f4afe7d4d674df1412a968"
query_keys:
  - "tool use and parallelism"
  - "parallel tool calls"
  - "tool runtime"
  - "ToolCallRuntime"
  - "tool_search deferred tools"
  - "OpenClaw tool policy"
  - "OpenClaw before_tool_call"
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

## OpenClaw Pattern

OpenClaw broadens tool-use engineering from "runtime dispatch" into "tool family construction plus policy":

| Mechanism | OpenClaw evidence | Interpretation |
| --- | --- | --- |
| Tool families | `OpenClawCodingToolConstructionPlan` separates base, shell, channel, OpenClaw and plugin tools. | Tool surface is assembled by family instead of one static registry. |
| OpenClaw tools | The plan includes sessions/history/list/send/spawn/yield, subagents, message, canvas, cron, gateway, goals, skill workshop, web_fetch/search, image, TTS and update_plan. | Platform tools expose Gateway, channel, automation and delegation capabilities. |
| Allowlist/group expansion | Tool construction expands plugin groups and applies raw allowlists/forced message behavior. | Large plugin surfaces are governed by group semantics. |
| Effective policy | `agent-tools.policy.ts` combines config/session/agent/model/group/subagent layers and has subagent always-denied/leaf-denied tools. | Availability is contextual and identity-sensitive. |
| Before-tool runtime | `before_tool_call` runs plugin hooks, trusted policies, approvals, diagnostics, loop detection, skill telemetry and argument adjustments. | Tool execution has a policy hook pipeline before handler work. |
| Sandbox integration | Sandbox context, registry and filesystem bridge resolve per-run workspaces, mounts and guarded file operations. | Tool execution can be tied to sandbox state and host-path guards. |

OpenClaw evidence does not show the same precise `ToolCallRuntime` RwLock parallelism pattern recorded in Codex. Its stronger contribution here is composition: tool families, channel/platform tools, plugin group expansion, policy layers and pre-call hooks.

## Harness Evidence

`core/tests/suite/tool_parallelism.rs` verifies parallel execution timing, mixed parallel tools, output grouping/order, and tools starting before a delayed `response.completed`.

## Reusable Insight

Model-level parallel tool support should be treated as permission to emit multiple tool calls, not as a guarantee that every handler is safe to run concurrently. Runtime still needs per-tool capability and serialization semantics.
