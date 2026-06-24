---
id: "github-owner-repo"
project_id: "github:owner/repo"
title: "owner/repo"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active"
write_policy: "managed"
source_kind: "github"
source_subtype: "github_repo"
analysis_depth: "deep_repo_read"
analysis_status: "deep_analysis_pending"
analysis_scope: []
canonical_url: "https://github.com/owner/repo"
analyzed_ref: "unknown"
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
  implementation_category: []
  method_family: []
  runtime_context: []
  application: []
  bridge: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
managed_by: "nahida"
run_ids: []
source_refs: []
confidence: "medium"
trust_tier: "primary"
---

# owner/repo

## 仓库身份

- Owner/name:
- URL:
- 分析 commit/tag/branch:
- 临时 checkout:
- Cleanup 状态:
- License:
- 语言:
- 生态/包类型:
- 包管理器:
- 文档路径:
- 主要入口:

## 精读状态

- Analysis depth: `deep_repo_read`
- Analysis status: `deep_analysis_pending|deep_analysis_complete|scoped_deep_analysis|needs_followup`
- Safe for absorption: false
- 分析范围:
- CodeGraph 使用情况:
- 已读文档:
- 已读 manifest/config:
- 已读 tests/examples:
- 已读核心源码:
- 已追踪流程:
- 未覆盖模块:
- 临时 checkout 处理:

## 仓库阅读地图

| 区域 | 文件/符号 | 阅读目的 | 关键发现 | 证据类型 | 备注 |
| --- | --- | --- | --- | --- | --- |

## 层级候选分类

- L1 Domain candidate:
- L2 Direction candidate:
- L3 Topic/content cluster candidates:
- Ontology path:
- 备选归属:
- 父级领域:
- 子领域:
- 问题区域:
- 实现类别:
- 算法/模型/协议族:
- 运行时上下文:
- 别名:
- 相邻方向:
- 置信度:
- 分类理由:
- Direction facets:
- Tags:
- Map memberships:
- 归属说明: 本节只给 `nahida-knowledge-get` 的候选与证据，不直接提升为 durable domain/direction/topic。

## 冷启动分层发现

> 当知识库还没有可用分层时，本节必须从 README、docs、manifest、API、模块边界、examples/tests 和核心代码流中提取通用上层结构。目标是让未来 query 先读 `04_Knowledge/` 的领域/方向/问题/方法节点，再按需读本 repo source note；不要把仓库名、模块名或实现技巧误升为基础概念。

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research/practice field |  | README/docs 定位、依赖生态、用户场景 |  | durable parent candidate / review |
| Background/context |  | 该仓库要解决的工程背景、行业约束、已有方案 |  | knowledge background / source-only |
| Problem solved |  | README goals、issues addressed、核心流程、测试场景 |  | problem node / section / review |
| Foundation concepts |  | 仓库依赖的通用概念，如 consensus、zk-SNARKs、agent memory |  | foundation node / foundation_gap |
| Method/architecture family |  | 架构范式、协议族、模型/执行引擎、存储/调度模式 |  | method node / source extension |
| Application/evaluation context |  | deployment、benchmark、examples、tests、integration targets |  | application/evaluation node / source-only |
| Repository/source instance |  | repo 名、模块、API、CLI、内部算法名 |  | source extension / representative implementation |

### 分层判断示例

| Repo cue | Correct handling | Wrong handling |
| --- | --- | --- |
| Repo implements a Raft-derived consensus path | 更新 `consensus -> crash-fault-tolerance`，把仓库作为代表实现/工程扩展 | 把 repo 名或内部模块名建成基础知识节点 |
| Repo implements Groth16 prover/verifier | 更新 `ZKP -> proof systems -> zk-SNARKs`，Groth16 是代表实例 | 把 Groth16 当作 ZKP 顶层方向 |
| Repo introduces one optimization flag | 留在 source extension 或方法节点小节 | 为一个 flag 创建独立 knowledge node |

## 检索优化判断

- 本仓库最应该更新的 Knowledge path:
- 它能帮助未来哪些问题少读代码/README/source notes:
- 哪些实现细节应留在 source note:
- 哪些上层节点过薄、缺失或需要 foundation_pack:
- 哪些 API/模块名只是 alias/query key/watch term:

## 问题与价值

## 架构

### 运行形态

### 主要组件

### 边界

### 数据流

### 控制流

### 存储或状态

### 外部服务或协议

## 关键流程追踪

| 流程 | 入口 | 关键文件/符号 | 数据/控制流 | 证据 | 备注 |
| --- | --- | --- | --- | --- | --- |

## 主要模块

| 模块 | 用途 | 关键文件/符号 | 接口 | 依赖 | 证据 |
| --- | --- | --- | --- | --- | --- |

## API、CLI 与配置面

- CLI 命令:
- Public API:
- 配置文件:
- Schema/协议:
- 扩展点:
- 环境变量:
- 生成物:

## 实现模式

- 算法:
- 数据结构:
- 并发/运行时:
- 缓存/索引:
- 持久化:
- Model/proof/agent/pipeline 设计:
- 错误处理:
- 评测/测试:

## 证据矩阵

| 发现 | 证据类型 | 来源/文件 | 置信度 |
| --- | --- | --- | --- |

## README 与代码对照

- 已确认:
- 不清楚:
- 相互矛盾:
- 缺失文档:

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |

## 知识交接

- 留在本仓库元笔记的证据:
- 待更新 Knowledge node:
- 作为哪些 Knowledge node 的 source extension:
- 待新增或复核 domain/direction/problem:
- Watchlist 词条:
- 相关论文:
- 相关仓库:
- Bridge 候选: endpoint knowledge paths、relation types、relationship thesis、transfer boundary、证据
- 需要深入分析的模块:
- Review queue:

## 基础概念候选判断

| 候选术语/模块/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| CFT/BFT/zk-SNARKs/consensus 等通用概念 | foundation_knowledge_candidate | 更新完整 Knowledge node，并把仓库作为实现/实践 evidence | 用仓库 API 或模块名定义基础概念 |  |
| 仓库内部模块/API/单个实现技巧 | source_extension_or_instance | 留在 source note，或作为 source extension/implementation pattern | 当成基础概念独立提升 |  |

## Knowledge 综合交接

- 应创建 Knowledge node:
- 应刷新 Knowledge synthesis section:
- 应标记过期:
- 无需更新的理由:
- 建议 node kind:

## 处理日志

## 临时仓库清理

- Clone path:
- Cleanup status:
- Kept reason:
