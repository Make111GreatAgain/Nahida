---
id: "nahida-knowledge-domain-direction-topic"
title: "Knowledge Node Title"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "seed|foundation_thin|active|evergreen|stale|review"
node_kind: "domain|direction|problem|subproblem|method_family|application_area|evaluation_axis"
hierarchy_level: "domain|direction|problem|subproblem|method_family|application_area"
file_slug: "path-safe-knowledge-slug"
domain_id: ""
direction_id: ""
parent_knowledge_refs: []
child_knowledge_refs: []
ontology_path: []
primary_ontology_path: ""
secondary_ontology_paths: []
relation_edges: []
bridge_refs: []
source_note_refs: []
representative_source_refs: []
query_keys: []
aliases: []
domains: []
topics: []
tags:
  - "nahida/knowledge"
freshness_status: "fresh|stale|unknown|not_applicable"
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

# Knowledge Node Title

## 定义与范围

- 定义:
- 不包含:
- Canonical terms:
- Aliases/query keys:
- Standalone completeness check: 本笔记是否能让读者不打开其他笔记也理解该概念/方向/问题的核心含义、边界和用途:
- Retrieval role: 本节点帮助哪些 query 少读 source notes:
- Update scope: 哪些 source 更新会触发本节点刷新:
- Domain dynamics note: 若本节点是 L1 domain，必须链接 `04_Knowledge/<domain>/research-dynamics.md` 或说明 queued/stale/not_applicable:

## 背景

说明理解该节点需要的前置背景、历史动机、基础概念和常见误解。未被来源支持的组织性背景必须标注为 `model_prior_background` 或 `tentative`。

## 基础概念判断

- 是否是基础概念/方向/问题:
- 为什么足够通用:
- 为什么不是单篇论文/单个协议/单个仓库的局部概念:
- 需要引用的更基础 Knowledge:
- 不应拆出的实例/协议/来源:

| 候选 | 判断 | 正确处理 | 错误处理 |
| --- | --- | --- | --- |
| CFT/BFT/zk-SNARKs 等通用概念 | foundation_knowledge | 独立完整解释，并被相关领域/问题引用 | 让读者从某篇论文或某个协议中反推定义 |
| Raft/Groth16 等协议实例 | representative_instance_or_section | 放入代表来源/方法族/实例章节；必要时建 protocol-instance 节点 | 当成整个方向的基础概念 |

## 解决的问题

该节点存在是为了解决什么领域/方向/问题中的什么具体难题。避免按某一篇论文展开。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window:
- Freshness:
- Valid until:
- 综合:

## 领域态势

> 仅 L1 domain 节点需要维护；非 L1 节点写 `not_applicable`。

- Research dynamics note:
- Dynamics freshness:
- Latest academic focus summary:
- Latest industrial focus summary:
- Open-problem summary:
- Next refresh trigger:

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
