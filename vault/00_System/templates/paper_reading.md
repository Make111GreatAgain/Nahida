---
id: "paper-identifier-or-nahida-src-YYYYMMDD-slug"
title: "论文标题"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_pending"
reading_coverage: []
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown"
year: "unknown"
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
direction_facets:
  parent_domain: []
  subdomain: []
  problem: []
  method_family: []
  system_layer: []
  evaluation_context: []
  application: []
  bridge: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
managed_by: "nahida"
run_ids: []
source_refs: []
confidence: "medium"
trust_tier: "primary"
primary_direction: ""
secondary_directions: []
classification_status: "staged"
classification_confidence: "medium"
classification_evidence: []
taxonomy_version: "1.0"
---

# 论文标题

## 论文身份

- 标题:
- 作者:
- 机构:
- 会议/期刊:
- 年份:
- DOI:
- arXiv:
- 链接:
- 本地 PDF:
- 代码:
- 数据:
- License:

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_pending|deep_read_complete|scoped_deep_read|extraction_gap|needs_human_review`
- Safe for absorption: false
- PDF extractor:
- 页数:
- 已覆盖章节/页码:
- 已检查附录:
- 未覆盖章节/页码:
- Extraction gaps:
- 精读说明:

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |

## 核心精读笔记

> 这一节不是摘要。它应当把论文的主要论证、机制、实验或证明按证据重建出来，让后续查询不需要重新打开 PDF 才能理解核心内容。

### 背景、动机与问题边界

- 背景脉络:
- 现有方法不足:
- 本文问题定义:
- 明确不解决的问题:
- 证据锚点:

### 模型、假设与定义

- 系统/安全/训练/评估模型:
- 关键定义:
- 符号与参数:
- 假设条件:
- 证据锚点:

### 方法、协议或系统机制

- 组件:
- 流程:
- 关键算法/公式/构造:
- 复杂度、成本或资源需求:
- 证据锚点:

### 理论、证明或正确性论证

- 定理/命题/性质:
- 证明思路:
- 正文没有展开的证明:
- 依赖的外部材料:
- 证据锚点:

### 实验、评估或案例

- 数据集/工作负载/场景:
- Baseline:
- Metrics:
- 主要结果:
- 消融或敏感性分析:
- 失败案例或负面结果:
- 证据锚点:

### 作者结论与我的判断

- 作者明确声称:
- 由证据支持的判断:
- 仍需谨慎的推断:
- 证据锚点:

## 层级候选分类

- L1 Domain candidate:
- L2 Direction candidate:
- L3 Topic/content cluster candidates:
- Ontology path:
- 备选归属:
- 父级领域:
- 学术子领域:
- 任务/问题:
- 方法族:
- 模型/协议/算法族:
- 评测场景:
- Benchmark/应用:
- 别名:
- 相邻方向:
- 置信度:
- 分类理由:
- 分类状态:
- 分类证据:
- Taxonomy version:
- Direction facets:
- Tags:
- Map memberships:
- 归属说明: 本节只给 `nahida-knowledge-get` 的候选与证据，不直接提升为 durable domain/direction/topic。

## 冷启动分层发现

> 当知识库还没有可用分层时，本节必须从论文元数据与正文证据中提取足够通用的上层结构候选。目标不是给论文分类好看，而是让未来 query 能沿 `领域 -> 方向 -> 研究问题/方法族 -> source evidence` 少读笔记，并让某个领域或方向可以被稳定总结和更新。

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain |  | 论文题名、摘要、引言、venue、related work |  | durable parent candidate / review |
| Research background |  | 论文为什么需要这个问题、历史脉络、系统约束 |  | knowledge background / source-only |
| Research problem |  | problem statement、威胁模型、目标、评价问题 |  | problem node / section / review |
| Foundation concepts |  | 论文依赖但不是论文独有的概念，如 CFT/BFT/zk-SNARKs |  | foundation node / foundation_gap |
| Method family |  | 方法类别、协议族、证明系统族、架构范式 |  | method node / source extension |
| Application/evaluation context |  | benchmark、应用场景、数据集、工作负载、deployment context |  | application/evaluation node / source-only |
| Artifact/source instance |  | 论文系统名、协议实例、具体算法、实验 artifact |  | source extension / representative source |

### 分层判断示例

| Source cue | Correct handling | Wrong handling |
| --- | --- | --- |
| `SRaft` / Raft variant in blockchain setting | `blockchain-systems or distributed-systems -> consensus -> crash-fault-tolerance`; `Raft/SRaft` 是协议实例或 source extension | 把 `SRaft` 直接建成领域、方向或基础概念 |
| `Groth16` proving system | `zero-knowledge-proofs -> proof-systems -> zk-SNARKs`; `Groth16` 是代表性 proving system instance | 把 `Groth16` 当成 zk-SNARKs 的完整基础定义 |
| `KZG commitments` | 在 polynomial commitments / SNARKs / data availability 中判断是否足够通用；若缺基础则补 foundation | 只写 KZG 论文贡献，不解释 reusable commitment concept |

## 检索优化判断

- 本论文最应该更新的 Knowledge path:
- 它能帮助未来哪些问题少读 source notes:
- 哪些内容应留在 source note，而不是创建上层节点:
- 哪些上层节点过薄、缺失或需要 foundation_pack:
- 哪些候选只是别名/query key/watch term:

## 一句话贡献

## 问题设定

## 方法概览

### 组成部分

### 流程或协议

### 关键定义、公式、算法或定理

### 假设条件

## 创新点

- 新思想:
- 对已有工作的扩展:
- 工程或实证贡献:
- 依赖的 prior work:

## 实验与结果

### 实验设置

### 数据集或 Benchmark

### Baseline

### 指标

### 主要结果

### 消融实验

### 效率、成本或安全性

### 结果 caveat

## 局限性

### 作者明确说明

### 基于证据的推断

## 可复用思路

## 术语表

## 连接

- 相关论文:
- 相关仓库:
- 相关 Knowledge nodes:
- 相关 Bridges:
- Bridge 候选: endpoint knowledge paths、relation types、relationship thesis、transfer boundary、证据

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |

## 知识交接

- 留在本文元笔记的证据:
- 待更新 Knowledge node:
- 作为哪些 Knowledge node 的 source extension:
- 需要补的 foundation knowledge/source:
- 待新增或复核 domain/direction/problem:
- Bridge 候选:
- Watchlist 词条:
- 后续论文:
- 后续仓库:
- Review queue:

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| CFT/BFT/zk-SNARKs 等通用概念 | foundation_knowledge_candidate | 建/更新完整 Knowledge node，并被相关领域/问题引用 | 让读者从本文或某个协议实例中反推定义 |  |
| Raft/Groth16/本文系统名等 | representative_instance_or_source_extension | 放入代表来源、实例、方法族或 source extension | 当成基础概念独立提升 |  |

## Knowledge 综合交接

- 应创建 Knowledge node:
- 应刷新 Knowledge synthesis section:
- 应标记过期:
- 无需更新的理由:
- 建议 node kind:

## 处理日志
