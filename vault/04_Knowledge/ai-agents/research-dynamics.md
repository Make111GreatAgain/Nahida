---
id: "nahida-knowledge-ai-agents-research-dynamics"
title: "AI agents Research Dynamics"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "domain_dynamics"
hierarchy_level: "domain_dynamics"
file_slug: "research-dynamics"
domain_id: "ai-agents"
direction_id: ""
parent_knowledge_refs:
  - "nahida-knowledge-ai-agents"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
primary_ontology_path: "ai-agents/research-dynamics"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-ai-agents-research-dynamics"
    relation: "part_of"
    to: "nahida-knowledge-ai-agents"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/research-dynamics.md"
      - "vault/04_Knowledge/ai-agents.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ai-agents-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/github/openai-codex-main-f959e7f.md"
    evidence_refs:
      - "vault/03_Sources/github/openai-codex-main-f959e7f.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ai-agents-research-dynamics"
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
  - "AI agents latest progress"
  - "agent systems research dynamics"
  - "coding agent runtime trends"
  - "agent harness engineering"
  - "OpenClaw agent platform"
aliases:
  - "AI agents trends"
domains:
  - "ai-agents"
topics:
  - "research dynamics"
  - "coding-agent-systems"
  - "agent-loop-engineering"
  - "tool-use"
  - "multi-agent"
  - "prompt-engineering"
  - "harness-engineering"
tags:
  - "nahida/knowledge"
  - "nahida/domain-dynamics"
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
confidence: "low"
trust_tier: "primary"
---

# AI agents Research Dynamics

## 领域范围与新鲜度

- Parent domain: [[ai-agents|AI agents]]
- Evidence window: `2026-06-24` to `2026-06-26`
- Last synthesized: `2026-06-26`
- Freshness status: `fresh` for current-vault synthesis only.
- Boundary: this is not an external latest-trends claim. It records what the vault currently knows after absorbing `openai/codex` and a scoped deep read of `openclaw/openclaw`.

## 研究动态摘要

| 动态 | 类型 | 影响的方向/问题 | 证据 | Confidence |
| --- | --- | --- | --- | --- |
| 新增 AI agents domain，以 coding-agent runtime 为首个证据主干。 | intake_state | AI agents / coding agents | [[openai-codex-main-f959e7f|openai/codex]] | medium |
| Codex 把 agent loop 拆成 submission loop、turn loop、sampling/tool-feedback loop。 | implementation_pattern | agent-loop-engineering | [[agent-loop-engineering|Agent loop engineering]] | high |
| 工具并行不是模型自由并发，而是模型 parallel flag + handler capability + runtime RwLock 的组合。 | implementation_pattern | tool-use-and-parallelism | [[tool-use-and-parallelism|Tool use and parallelism]] | high |
| Multi-agent 被实现为线程树控制面，而不是普通工具并行。 | implementation_pattern | multi-agent-orchestration | [[multi-agent-orchestration|Multi-agent orchestration]] | high |
| 安全策略集中在执行编排层，审批、guardian、sandbox、network approval 和 retry 在同一路径中决策。 | implementation_pattern | safety-and-permission-harness | [[safety-and-permission-harness|Safety and permission harness]] | high |
| Skills/AGENTS.md/plugins/apps/extensions 都被建模为有边界的 model-visible context 注入。 | implementation_pattern | skills-and-context-engineering | [[skills-and-context-engineering|Skills and context engineering]] | high |
| Agent harness 需要 mock model streams 与 captured request assertions。 | implementation_pattern | eval-and-harness-engineering | [[eval-and-harness-engineering|Eval and harness engineering]] | high |
| OpenClaw 把 coding-agent loop 扩展到 Gateway、channels、personal workspace、memory、plugin SDK 和 native subagents 的平台形态。 | implementation_pattern | coding-agent-systems / agent-gateway-and-channel-runtime | [[openclaw-openclaw-main-751a6c2|openclaw/openclaw]] | medium-high |
| OpenClaw 的 context engine 与 Markdown memory 表明 agent context 正在从 prompt 拼接走向可替换 context ownership 和文件化长期记忆。 | implementation_pattern | skills-and-context-engineering / performance-and-context-budgeting | [[openclaw-openclaw-main-751a6c2|openclaw/openclaw]] | medium-high |
| OpenClaw 与 Codex 都通过工具面暴露 delegation，但真实边界在持久 agent/session/control plane，而不是 same-turn tool futures。 | comparative_pattern | tool-use-and-parallelism / multi-agent-orchestration | [[tool-parallelism-to-multi-agent-orchestration|Tool parallelism -> multi-agent orchestration]] | high |

## 当前空白

- 缺少 Agents SDK、LangGraph、AutoGen、CrewAI、Claude Code、Cursor/Windsurf 等横向比较。
- 缺少 agent eval benchmark、long-horizon task benchmark、tool-use benchmark 的外部来源。
- 缺少 MCP ecosystem 的独立 source notes。
- 缺少 prompt injection / tool risk / sandbox escape 的安全研究来源。
- 缺少生产 telemetry / latency / context cost 优化的跨系统证据。
- OpenClaw 本次是 scoped raw snapshot，不是完整 clone；移动端 UI、每个 channel adapter、每个 extension 的实现仍未系统审计。

## 观察到的工程名词映射

| Term | Codex-backed meaning |
| --- | --- |
| loop engineering | submission -> turn -> sampling -> tool feedback -> compaction/pending input handling |
| prompt engineering | base instructions, developer/contextual fragments, AGENTS.md, skills, multi-agent mode, permissions, apps/plugins, tool specs |
| tool-use engineering | tool registry, exposure model, direct/deferred search, hooks, runtime dispatch, output truncation |
| harness engineering | mock Responses streams, captured request inspection, integration tests for agent event order and context shape |
| multi-agent orchestration | `AgentControl`, thread tree, session source, mailbox, task path, status subscription, capacity |
| safety harness | approval policy, guardian, permission hooks, sandbox selection, network denial context, retry/escalation |
| context engineering | bounded project docs, skills, extensions, token-budget fragments, auto compaction |
| Gateway runtime | OpenClaw-style daemon/control plane for typed WS requests, role/scope auth, channel ingress, lifecycle events |
| context engine | OpenClaw pluggable lifecycle for ingest, assemble, compact, after-turn, subagent preparation and maintenance |
| personal memory | OpenClaw Markdown-backed `MEMORY.md`, daily notes, `DREAMS.md`, active memory search/get and compaction-time flush |

## Refresh Rules

- Run `nahida-daily-fetch` or `nahida-research-search` before answering "latest AI agent trends".
- Refresh if openai/codex changes multi-agent v2, tool parallelism, ToolOrchestrator, skills extension, or app-server protocol.
