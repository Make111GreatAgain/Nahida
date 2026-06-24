---
id: "nahida-research-YYYYMMDD-slug"
title: "研究搜索"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "web"
source_subtype: "web_concept"
canonical_url: ""
research_depth: "targeted"
research_scope: "targeted|foundation_pack|application_survey|freshness_scan"
research_status: "normalized"
evidence_window_start: "YYYY-MM-DD|unknown"
evidence_window_end: "YYYY-MM-DD|unknown"
hierarchy_level: "source"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
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
confidence: "medium"
trust_tier: "secondary"
---

# 研究搜索

## 查询约定

- 原始查询:
- 解释后的范围:
- 排除含义:
- 扩展搜索词:
- 时间范围:
- 搜索日期:
- 不覆盖范围:
- 预期用途:

## 来源集合

| 标题 | URL | 作者/组织 | 日期 | 子类型 | Trust tier | 新鲜度 | 选择理由 | 去重状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 深化门

| 条目 | 来源类型 | Deepening decision | Target path candidates | Next skill owner | Durable absorption eligible | Reason |
| --- | --- | --- | --- | --- | --- | --- |

## 跨路径桥接候选

| Candidate | Endpoint paths | Relation types | Thesis | Evidence | Transfer boundary | Maturity | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 层级候选分类

- L1 Domain candidate:
- L2 Direction candidate:
- L3 Topic/content cluster candidates:
- Ontology path:
- 备选归属:
- 父级领域:
- 子领域:
- 任务/问题:
- 方法或实践类别:
- 别名:
- 相邻方向:
- 置信度:
- 分类理由:

## 冷启动分层发现

> research-search 常用于补齐基础知识或新兴方向。若知识库还没有分层，必须先从稳定资料集合中提取通用层级，而不是把某篇博客、新闻或热词直接写成领域。目标是让未来 query 可以通过细粒度层级减少读取量，并能对领域/方向做可维护的总结和刷新。

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain |  | 多个稳定来源的共同定位、标准/综述/官方文档 |  | durable parent candidate / review |
| Research background |  | 历史背景、动机、产业/学术语境、约束 |  | knowledge background / source-only |
| Research/practice problem |  | 被反复提出的问题、评价目标、失败模式 |  | problem node / section / review |
| Foundation concepts |  | 多来源支持的基础概念，如 CFT/BFT/zk-SNARKs |  | foundation node / foundation_gap |
| Method family |  | 方法族、协议族、架构范式、工具链类别 |  | method node / source extension |
| Application/evaluation context |  | 应用领域、benchmark、数据集、部署语境、指标 |  | application/evaluation node / source-only |
| Source instance/news item |  | 单篇文章、新闻、产品发布、单个项目/论文 |  | source note / freshness signal |

### 分层判断示例

| Source set cue | Correct handling | Wrong handling |
| --- | --- | --- |
| 多个资料都讨论 `CFT/BFT` | 建立/补齐 consensus 下的 fault-tolerance 基础节点 | 用某个 Raft/PBFT 文章替代 CFT/BFT 定义 |
| `zk-SNARKs` 基础资料、应用资料和近期论文同时出现 | 补齐 proof systems 下的 zk-SNARKs foundation，并把具体方案列为代表实例 | 把 Groth16 或某条新闻当作整个方向 |
| 新兴热词只有新闻/博客支持 | 作为 watch term 或 freshness signal | 立刻创建 evergreen knowledge node |

## 检索优化判断

- 这组资料最应该更新的 Knowledge path:
- 它能帮助未来哪些问题少读 web source notes:
- 哪些内容只是 freshness/news/watch term:
- 哪些基础概念需要继续用 stable source 补齐:
- 哪些候选应只进入 review queue:

## Foundation Pack 调研

| Stream | 调研目标 | 当前结论 | 代表来源 | 缺口 |
| --- | --- | --- | --- | --- |
| foundation_survey | 基础定义、前置知识、历史背景、规范来源 |  |  |  |
| taxonomy_and_applications | 核心子方向、方法族、应用场景、评价维度 |  |  |  |
| representative_papers | 经典论文、综述、代表方法、近期关键论文 |  |  |  |
| representative_repos | 参考实现、主流工程项目、工具链、benchmark |  |  |  |
| freshness_signals | 新闻、release、热词、主流趋势、可能新内容 |  |  |  |

## 综合理解

### 结论摘要

### 稳定定义

### 当前理解

### 实践语境

### 主要变体

### 近期变化

### 争议观点

### 与已有知识库的关系

## 结构化分解

| 子方向/机制/对象 | 说明 | 证据来源 | 置信度 | 后续处理 |
| --- | --- | --- | --- | --- |

## 证据性 Claim

| Claim | Source refs | 置信度 | Evergreen 或时效性 | 冲突 |
| --- | --- | --- | --- | --- |

## 代表实体

- 项目:
- 论文:
- 标准:
- 数据集:
- 产品:
- 组织:
- Benchmark:
- 协议:

## 代表论文与仓库候选

| 条目 | 类型 | 为什么代表该方向 | 建议 skill | 优先级 | 状态 |
| --- | --- | --- | --- | --- | --- |

## 术语表

- 标准术语:
- 别名:
- 缩写:
- 新兴术语:
- 过时或歧义术语:
- 搜索关键词:

## 开放问题

## Knowledge 综合建议

- 应创建或刷新 Knowledge node:
- Node kind:
- 覆盖范围:
- Valid until 建议:

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |

## 知识交接

- 留在本研究元笔记的证据:
- 待更新 Knowledge node:
- 作为哪些 Knowledge node 的 source extension:
- 待新增或复核 domain/direction/problem:
- Bridge 候选:
- Watchlist 词条:
- 待阅读论文:
- 待分析仓库:
- Daily-fetch 查询:
- Review queue:

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| CFT/BFT/zk-SNARKs/agent memory 等稳定通用概念 | foundation_knowledge_candidate | 用稳定来源补全完整 Knowledge node | 用新闻/博客/单篇论文直接定义 evergreen foundation |  |
| Raft/Groth16/单仓库/单产品发布/单 benchmark | representative_or_freshness_signal | 作为代表实例、source extension、watchlist 或 deepening task | 当成基础概念或方向主干 |  |

## 处理日志
