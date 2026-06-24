---
id: "nahida-knowledge-ai-agents"
title: "AI agents"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "domain"
hierarchy_level: "domain"
file_slug: "ai-agents"
domain_id: "ai-agents"
direction_id: ""
parent_knowledge_refs: []
child_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
  - "nahida-knowledge-ai-agents-research-dynamics"
ontology_path:
  - "ai-agents"
primary_ontology_path: "ai-agents"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-ai-agents"
    relation: "has_child"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ai-agents"
    relation: "has_child"
    to: "nahida-knowledge-ai-agents-research-dynamics"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents.md"
      - "vault/04_Knowledge/ai-agents/research-dynamics.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ai-agents"
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
  - "AI agents"
  - "agent systems"
  - "coding agents"
  - "agent runtime"
  - "agent harness"
aliases:
  - "agentic systems"
  - "AI agent systems"
domains:
  - "ai-agents"
topics:
  - "coding-agent-systems"
  - "agent-loop-engineering"
  - "tool-use"
  - "multi-agent"
  - "harness-engineering"
tags:
  - "nahida/knowledge"
  - "nahida/domain"
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
confidence: "medium"
trust_tier: "primary"
---

# AI agents

## 领域范围

AI agents here means software systems that use a model loop plus tools, context, memory/state, permissions, runtime harnesses, and sometimes multi-agent delegation to complete tasks. Current vault evidence for this domain is narrow and implementation-heavy: the `openai/codex` repository, especially its local coding-agent runtime.

## 当前结构

| Child | Scope | Status |
| --- | --- | --- |
| [[coding-agent-systems|Coding agent systems]] | Local coding agents with repository context, tool execution, safety harness, skills, multi-agent control, and eval harnesses. | active_seed |
| [[research-dynamics|AI agents Research Dynamics]] | Current vault state and evidence gaps for AI agents. | active_seed |

## 主要问题簇

| Problem cluster | Why it matters | Evidence |
| --- | --- | --- |
| Agent loop engineering | Separates submission routing, turn execution, model sampling, tool feedback, pending input, and compaction. | [[openai-codex-main-f959e7f|openai/codex]] |
| Tool use and parallelism | Determines how model-visible tool calls become safe, observable, optionally parallel runtime tasks. | [[tool-use-and-parallelism|Tool use and parallelism]] |
| Multi-agent orchestration | Distinguishes sub-agent thread trees, mailbox communication, status and capacity control from same-turn tool parallelism. | [[multi-agent-orchestration|Multi-agent orchestration]] |
| Safety and permissions | Couples approval policy, guardian review, permission hooks, sandboxing, network approval, and retry semantics. | [[safety-and-permission-harness|Safety and permission harness]] |
| Skills and context engineering | Treats prompt fragments, AGENTS.md, skills, plugins, apps and extensions as bounded model-visible context artifacts. | [[skills-and-context-engineering|Skills and context engineering]] |
| Harness engineering | Uses mock model streams and captured request assertions to test agent behavior as event/order/context contracts. | [[eval-and-harness-engineering|Eval and harness engineering]] |

## Evidence Boundary

This node is `foundation_thin`: one strong primary implementation source, but no external survey or comparative analysis yet. It should not answer "what is the state of all AI agents in 2026" without a daily/research fetch.

## Source Extensions

- [[openai-codex-main-f959e7f|openai/codex]] provides a deep implementation example of local coding-agent runtime architecture.

## Bridge Links

- [[tool-parallelism-to-multi-agent-orchestration|Tool parallelism -> multi-agent orchestration]]

## Refresh Rules

- Refresh after new source notes on Agents SDK, Claude Code, Cursor/Windsurf agent runtime, LangGraph, AutoGen/CrewAI, MCP server ecosystems, or agent eval harnesses.
- Reclassify from `foundation_thin` only after at least 3 independent implementation or research sources are absorbed.
