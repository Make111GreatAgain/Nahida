---
id: "nahida-knowledge-<domain>-research-dynamics"
title: "<Domain> Research Dynamics"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "seed|active|stale|review"
node_kind: "domain_dynamics"
hierarchy_level: "domain_dynamics"
file_slug: "research-dynamics"
domain_id: "<domain>"
direction_id: ""
parent_knowledge_refs:
  - "nahida-knowledge-<domain>"
child_knowledge_refs: []
ontology_path:
  - "<domain>"
primary_ontology_path: "<domain>/research-dynamics"
secondary_ontology_paths: []
relation_edges: []
bridge_refs: []
source_note_refs: []
representative_source_refs: []
query_keys:
  - "<domain> latest progress"
  - "<domain> research trends"
  - "<domain> open problems"
aliases: []
domains:
  - "<domain>"
topics:
  - "research dynamics"
  - "academic focus"
  - "industry focus"
  - "open problems"
tags:
  - "nahida/knowledge"
  - "nahida/domain-dynamics"
freshness_status: "fresh|stale|unknown"
last_synthesized: "YYYY-MM-DD|unknown"
valid_until: "YYYY-MM-DD|unknown"
evidence_window_start: "YYYY-MM-DD|unknown"
evidence_window_end: "YYYY-MM-DD|unknown"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
managed_by: "nahida"
run_ids: []
source_refs: []
confidence: "unknown|low|medium|high"
trust_tier: "unknown|primary|secondary|tertiary|personal"
---

# <Domain> Research Dynamics

## 领域范围与新鲜度

- Parent domain:
- Evidence window:
- Last synthesized:
- Valid until:
- Freshness status:
- Retrieval role: 回答该最大领域的最新进展、研究倾向、学术/工业关注点、待解决问题，避免 query 扫描大量 source notes。
- Update scope: 该领域新增论文、仓库、web research、daily freshness signals、bridge notes、问题节点重大变化。

## 研究动态摘要

用 5-10 条说明本证据窗口内真正改变了什么。不要列论文标题；要写领域层面的变化。

| 动态 | 类型 | 影响的方向/问题 | 证据 | Confidence |
| --- | --- | --- | --- | --- |

## 学术关注

| 关注点 | 为什么重要 | 代表 Sources | 影响的 Knowledge nodes | 未解决点 |
| --- | --- | --- | --- | --- |

## 工业与工程关注

| 关注点 | 工程动机 | 代表仓库/标准/实现/新闻 | 约束或瓶颈 | 影响的 Knowledge nodes |
| --- | --- | --- | --- | --- |

## 新兴方向与热词

| 术语/方向 | 信号来源 | 成熟度 | 是否应建 Knowledge node | Next action |
| --- | --- | --- | --- | --- |

成熟度建议：`watch_term`、`freshness_signal_only`、`candidate_direction`、`active_seed`、`active`、`hype_or_noise`。

## 待解决问题

| Open problem | 类别 | 为什么还没解决 | 当前路线 | 需要的新 source/skill |
| --- | --- | --- | --- | --- |

类别建议：`foundation_gap`、`method_limit`、`evaluation_gap`、`implementation_gap`、`security_gap`、`adoption_gap`、`cost_gap`。

## 方向倾向判断

- 学术界倾向:
- 工业界倾向:
- 二者一致的地方:
- 二者张力:
- 可能的新内容:
- 需要谨慎的推断:

## 证据窗口

| Source/Note | Date | Kind | 支持了什么判断 | Caveat |
| --- | --- | --- | --- | --- |

## 刷新触发器

| Trigger | Condition | Suggested skill | Priority |
| --- | --- | --- | --- |
| Freshness expired | `valid_until` 已过期 | `nahida-daily-fetch` or `nahida-consolidate` | high |
| New deep-read paper changes domain priority | source extension affects academic focus/open problems | `nahida-knowledge-get` | medium |
| New repo/standard/release signals industrial shift | repeated repo/release/standard evidence | `nahida-daily-fetch` -> deep source skill | medium |
| Emerging term repeats across sources | hot term appears in multiple reliable notes | `nahida-research-search` | medium |

## 更新记录

| Date | Run ID | Change | Evidence window | Sources |
| --- | --- | --- | --- | --- |
