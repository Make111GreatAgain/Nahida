---
id: "nahida-knowledge-skills-and-context-engineering"
title: "Skills and context engineering"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "topic"
hierarchy_level: "topic"
file_slug: "skills-and-context-engineering"
domain_id: "ai-agents"
direction_id: "coding-agent-systems"
parent_knowledge_refs:
  - "nahida-knowledge-coding-agent-systems"
child_knowledge_refs: []
ontology_path:
  - "ai-agents"
  - "coding-agent-systems"
  - "skills-and-context-engineering"
primary_ontology_path: "ai-agents/coding-agent-systems/skills-and-context-engineering"
secondary_ontology_paths:
  - "ai-agents/coding-agent-systems/prompt-engineering"
relation_edges:
  - from: "nahida-knowledge-skills-and-context-engineering"
    relation: "part_of"
    to: "nahida-knowledge-coding-agent-systems"
    evidence_refs:
      - "vault/04_Knowledge/ai-agents/coding-agent-systems/skills-and-context-engineering.md"
      - "vault/04_Knowledge/ai-agents/coding-agent-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-skills-and-context-engineering"
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
  - "skills and context engineering"
  - "Codex skills"
  - "SKILL.md injection"
  - "AGENTS.md prompt context"
  - "prompt engineering"
aliases:
  - "prompt engineering"
  - "context engineering"
domains:
  - "ai-agents"
topics:
  - "skills"
  - "AGENTS.md"
  - "prompt-fragments"
  - "context-engineering"
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

# Skills and context engineering

## 定义

Skills and context engineering is the design of model-visible instruction/context surfaces: base instructions, developer fragments, AGENTS.md project docs, skills, plugins, apps, extension fragments, permissions, multi-agent mode hints, token-budget context, and tool specs.

## Codex Pattern

| Mechanism | Evidence | Role |
| --- | --- | --- |
| Base instructions | Chosen from config, rollout history, or model default (`session/mod.rs:590-605`). | Stable system/developer foundation. |
| Developer sections | Permissions, developer instructions, collaboration mode, realtime, personality, apps, skills, plugins, extensions and token-budget fragments are aggregated (`session/mod.rs:3120-3339`). | Structured prompt assembly. |
| Multi-agent mode | explicit/proactive mode creates developer fragment; none omits it (`session/mod.rs:3371-3385`). | Prompt policy separate from tools. |
| AGENTS.md | Discovers project docs root-to-cwd, enforces byte budget, prefers override file (`agents_md.rs:1-16`, `:120-143`, `:244-258`). | Project context with provenance and bounds. |
| Available skills | `AvailableSkillsInstructions` renders a developer fragment (`available_skills_instructions.rs:8-49`). | Exposes skill catalog. |
| Skill injection | `build_skill_injections` reads exact `SKILL.md` content for explicitly mentioned skills (`core-skills/src/injection.rs:63-116`). | Full skill instructions enter the turn only when selected/mentioned. |
| Mention matching | Structured skill inputs resolve by path before `$skill-name` text scanning (`core-skills/src/injection.rs:138-205`). | Reduces ambiguous activation. |
| Per-turn skills/plugins | `build_skills_and_plugins` merges skills, plugins, connectors, extension inputs, warnings and app mentions (`turn.rs:498-663`). | Dynamic prompt/context injection. |

## Reusable Insight

Prompt engineering in robust agents is not a monolithic string. It is a context-fragment system with provenance, role, lifecycle phase, size limits, explicit activation rules, and tests against request shape.

## Boundary

This node should not infer that Codex's wording is the best possible prompt; it only records the harness architecture for prompt/context construction.
