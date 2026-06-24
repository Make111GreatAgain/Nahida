---
id: "nahida-src-YYYYMMDD-slug"
title: "来源标题"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "raw"
source_kind: "web"
source_subtype: "web_concept"
canonical_url: ""
author_or_org: ""
published: "unknown"
accessed: "YYYY-MM-DD"
file_slug: "path-safe-source-slug"
hierarchy_level: "source"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
primary_ontology_path: ""
secondary_ontology_paths: []
path_update_status: "not_propagated|propagated|queued|review"
hierarchy_candidates:
  domains: []
  directions: []
  topics: []
domains: []
topics: []
aliases: []
tags: []
direction_facets: {}
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
managed_by: "nahida"
run_ids: []
source_refs: []
confidence: "unknown"
trust_tier: "unknown"
---

# 来源标题

## 来源身份

- 标题:
- 作者/组织:
- URL:
- 发布/更新日期:
- 访问日期:
- Source kind/subtype:
- Trust tier:
- 适用范围:

## 范围与阅读状态

- 已读范围:
- 未读或不可访问:
- 抽取质量:
- 是否可作为 durable evidence:
- Standalone completeness check: 本 source 笔记是否足够详细，未来不用重新打开原 PDF/仓库/网页也能回答普通问题:

## 摘要结论

用 3-7 条说明这个来源真正贡献了什么，而不是复述标题。

## 为什么重要

说明它对哪个方向、问题、概念、实践或趋势有价值。

## 冷启动分层发现

当现有知识库没有清晰层级时，必须从本 source 的元数据和内容里抽取可复用层级，而不是按 source 名称建层。

| Facet | Candidate | Evidence | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Research field/domain |  |  |  |  |
| Research background |  |  |  |  |
| Research problem |  |  |  |  |
| Foundation concepts |  |  |  |  |
| Method family |  |  |  |  |
| Application/evaluation context |  |  |  |  |
| Artifact/source instance |  |  |  |  |

## 检索优化判断

- 这个 source 应该帮助哪些 Knowledge node 变得更容易查询:
- 哪些未来问题可以因此少读 source:
- 哪些内容只应留在 source，不应进入上层:

## 结构化内容

### 核心概念

### 关键机制或流程

### 实践细节

### 限制与 caveat

## 证据记录

> 默认留在本 source 笔记。Source 是外部来源的完整记忆，不按方向存放。可复用内容由 `nahida-knowledge-get` 吸收到 `04_Knowledge/` 的知识节点；跨领域或跨问题关系进入 `05_Bridges/`。不要为普通 source-local 事实创建新的 claim/concept/map/synthesis 笔记。

| 事实/观察 | 证据位置 | 置信度 | 时效性 | 上层处理 | 备注 |
| --- | --- | --- | --- | --- | --- |

## Knowledge/Bridge 候选

| 候选内容 | 类型 | 目标 knowledge/bridge | 证据 | 决策 |
| --- | --- | --- | --- | --- |

## 基础概念候选判断

| 候选术语/方法 | 是否足够通用 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| CFT/BFT/zk-SNARKs 等 | likely foundation knowledge | 交给 `nahida-knowledge-get` 建/更新完整 Knowledge node | 只作为本文局部术语或让读者读本文才理解 |  |
| Raft/Groth16/单仓库模块等 | likely instance/source extension | 放入代表来源、实例、方法族或 source extension | 当成基础概念独立提升 |  |

## 层级候选与标签

- L1 Domain candidate:
- L2 Direction candidate:
- L3 Topic/content cluster candidates:
- Ontology path:
- 备选归属:
- Primary direction:
- Secondary directions:
- Direction facets:
- Tags:
- Aliases:
- 归属说明: 本节只给 `nahida-knowledge-get` 的候选与证据，不直接提升为 durable domain/direction/topic。

## 可复用记忆

- 可更新 knowledge node:
- 可新建 knowledge node:
- 可形成 bridge: endpoint knowledge paths、relation types、relationship thesis、transfer boundary、证据
- 应留在 source 内的内容:
- 需要联网补充的 foundation knowledge（仅 update/research/knowledge-get 模式允许；query 禁止联网）:
- 后续应读:

## 处理日志
