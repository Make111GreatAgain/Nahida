---
id: "nahida-bridge-tool-parallelism-to-multi-agent-orchestration"
title: "Tool parallelism -> multi-agent orchestration"
original_title: "Tool parallelism -> multi-agent orchestration"
file_slug: "tool-parallelism-to-multi-agent-orchestration"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "intra_domain_control_boundary"
bridge_status: "active_seed"
endpoint_paths:
  - "ai-agents/coding-agent-systems/tool-use-and-parallelism"
  - "ai-agents/coding-agent-systems/multi-agent-orchestration"
endpoint_knowledge_refs:
  - "nahida-knowledge-tool-use-and-parallelism"
  - "nahida-knowledge-multi-agent-orchestration"
from_domain: "ai-agents"
to_domain: "ai-agents"
from_direction: "coding-agent-systems"
to_direction: "coding-agent-systems"
from_topic: "tool-use-and-parallelism"
to_topic: "multi-agent-orchestration"
relation_types:
  - "distinction"
  - "control_boundary"
  - "implementation_contrast"
  - "coordination_boundary"
directionality: "from_runtime_parallelism_to_agent_control_plane"
relationship_thesis: "In Codex, same-turn tool parallelism is runtime concurrency controlled by model capability, per-tool supports_parallel declarations, and a ToolCallRuntime RwLock. Multi-agent orchestration is a thread-tree control plane built from AgentControl, SessionSource, mailbox communication, task paths, status, and capacity checks. Multi-agent tools are registered through the tool surface, but their semantics create or address agent threads rather than merely overlap handler execution."
transferability: "high"
non_transfer_boundary: "The distinction transfers as an architectural pattern, but concrete Codex details such as MultiAgentV2 tool names, AgentPath resolution, rollout budget, and session source variants are implementation-specific. Do not infer that every agent framework exposes sub-agents as model tools or uses a thread tree."
evidence_window_start: "2026-06-24"
evidence_window_end: "2026-06-24"
domains:
  - "ai-agents"
topics:
  - "tool-use-and-parallelism"
  - "multi-agent-orchestration"
  - "parallel-tool-calls"
  - "AgentControl"
  - "agent-loop-engineering"
source_note_refs:
  - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
knowledge_refs:
  - "nahida-knowledge-tool-use-and-parallelism"
  - "nahida-knowledge-multi-agent-orchestration"
  - "nahida-knowledge-agent-loop-engineering"
query_keys:
  - "tool parallelism vs multi-agent"
  - "parallel tool calls versus subagents"
  - "Codex ToolCallRuntime AgentControl"
  - "agent parallelism control boundary"
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

# Tool parallelism -> multi-agent orchestration

## 命名与路径

- Original title: Tool parallelism -> multi-agent orchestration
- File slug: `tool-parallelism-to-multi-agent-orchestration`
- Path safety check: created under `05_Bridges`.

## 连接命题

- From: `ai-agents/coding-agent-systems/tool-use-and-parallelism`
- To: `ai-agents/coding-agent-systems/multi-agent-orchestration`
- Relation types: distinction, control_boundary, implementation_contrast, coordination_boundary
- Directionality: `from_runtime_parallelism_to_agent_control_plane`
- Relationship thesis: In Codex, same-turn tool parallelism is runtime concurrency controlled by model capability, per-tool `supports_parallel` declarations, and a `ToolCallRuntime` `RwLock`. Multi-agent orchestration is a thread-tree control plane built from `AgentControl`, `SessionSource`, mailbox communication, task paths, status, and capacity checks. Multi-agent tools are registered through the tool surface, but their semantics create or address agent threads rather than merely overlap handler execution.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[tool-use-and-parallelism|Tool use and parallelism]] | `ai-agents/coding-agent-systems/tool-use-and-parallelism` | Same-turn tool planning, dispatch, handler capability and runtime concurrency. | [[openai-codex-main-f959e7f|openai/codex]] | active_seed |
| [[multi-agent-orchestration|Multi-agent orchestration]] | `ai-agents/coding-agent-systems/multi-agent-orchestration` | Sub-agent identity, thread tree, mailbox, status, capacity and follow-up turns. | [[openai-codex-main-f959e7f|openai/codex]] | active_seed |

## 核心区分

| Dimension | Tool parallelism | Multi-agent orchestration |
| --- | --- | --- |
| Unit of work | Tool handler execution inside one model turn. | Agent thread/session with independent turn lifecycle. |
| Control object | `ToolCallRuntime`, `ToolRouter`, `ToolRegistry`. | `AgentControl`, `AgentRegistry`, `SessionSource`, multi-agent V2 residency. |
| Concurrency gate | Per-tool `supports_parallel_tool_calls`; shared read lock for parallel-safe tools, write lock for non-parallel tools. | Capacity checks, spawn slots, task paths, mailbox delivery, status subscription and wait semantics. |
| Model surface | Function/tool calls returned by the model stream. | Multi-agent tools such as spawn, send message, follow-up task, wait, list, interrupt. |
| Lifetime | Usually bounded by the current sampling/tool-feedback step. | Can outlive a single tool call and receive later messages or follow-up turns. |
| Output shape | Tool output item fed back to the current turn. | Inter-agent communication, status/activity events and possibly another agent's final response. |
| Failure boundary | Handler failure, sandbox/approval denial, cancellation, tool output truncation. | Spawn failure, capacity failure, unresolved agent reference, interrupted target, mailbox timeout. |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Two-level parallel gate | Tool-use runtimes | `build_prompt` sets model `parallel_tool_calls`; runtime still asks each handler if parallel-safe. | Requires handlers to declare capability honestly. |
| Read/write lock serialization | Tool execution schedulers | Parallel-safe tools take shared locks; unsafe tools take exclusive lock in `ToolCallRuntime`. | Suitable for coarse runtime serialization, not fine-grained resource scheduling. |
| Control-plane split | Multi-agent systems | `AgentControl` owns spawn, message, path resolution, status and capacity outside generic handler execution. | Codex's thread-tree model may not match graph schedulers or actor pools. |
| Tool-surface bridge | Agent UX/prompt design | Multi-agent operations are exposed as tools, so the model can invoke them through the same Responses tool mechanism. | Same surface does not mean same semantics. The operation changes the agent topology. |
| Prompt encouragement separation | Multi-agent policy | `MultiAgentMode` can inject explicit-only/proactive instructions or omit instructions while keeping tools available. | Tool availability and delegation policy must be treated as separate levers. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Same-turn concurrency | `tool-use-and-parallelism` | `multi-agent-orchestration` | Do not equate overlapping tool handlers with delegated agent work; use it only for bounded runtime acceleration. | `tools/parallel.rs`, `tools/router.rs`, `tools/registry.rs` in [[openai-codex-main-f959e7f|openai/codex]] | Treating tool futures as agents loses identity, status and resumability. |
| Tool exposure patterns | `tool-use-and-parallelism` | `multi-agent-orchestration` | Register multi-agent operations as model tools so they benefit from normal tool planning and dispatch lifecycle. | `spec_plan.rs` registers multi-agent collaboration tools. | Normal dispatch wrappers must not hide control-plane side effects. |
| Capacity and observability | `multi-agent-orchestration` | `tool-use-and-parallelism` | Apply agent-style status/capacity thinking to long-running tools when they become task-like. | `AgentControl` capacity and status paths. | Overbuilding all tools as agents can add unnecessary lifecycle complexity. |

## 非迁移边界

Tool parallelism should not be used to answer "how many agents are running" because it does not create agent identity. Multi-agent orchestration should not be reduced to "parallel tool calls" because spawn/send/follow-up/wait semantics alter the thread tree and mailbox state. Codex intentionally lets the model access multi-agent operations through the tool layer, but the decisive boundary is below the surface: whether the operation merely executes a handler or mutates the agent control plane.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[openai-codex-main-f959e7f|openai/codex]] | Primary implementation source for `ToolCallRuntime`, `ToolRouter`, `ToolRegistry`, `AgentControl`, multi-agent V2 tools and prompt mode instructions. | active_seed |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[tool-use-and-parallelism|Tool use and parallelism]] | Important Boundary / Bridge Links | Records that tool parallelism is same-turn handler concurrency. | active_seed |
| [[multi-agent-orchestration|Multi-agent orchestration]] | Difference From Tool Parallelism / Bridge Links | Records that multi-agent is a thread-tree control plane. | active_seed |
| [[agent-loop-engineering|Agent loop engineering]] | Related loop boundary | Tool futures and mailbox/preemption both appear in the turn loop but represent different state transitions. | active_seed |

## 刷新规则

- Last checked: `2026-06-24`.
- Valid until: `2026-07-24`.
- Refresh triggers: Codex changes to `tools/parallel.rs`, `tools/router.rs`, `tools/registry.rs`, `agent/control.rs`, `tools/handlers/multi_agents_v2/*`, or multi-agent prompt mode schemas.
