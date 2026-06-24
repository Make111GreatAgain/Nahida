---
id: "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
title: "Blockchain coordination -> trustworthy distributed ML"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain"
bridge_status: "active_seed"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "blockchain-systems"
  - "trustworthy-distributed-ml"
  - "blockchain-coordinated-training"
endpoint_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-trustworthy-distributed-ml"
endpoint_paths:
  - "blockchain-systems"
  - "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
from_domain: "blockchain-systems"
to_domain: "ml-systems"
from_direction: ""
to_direction: "privacy-and-trustworthy-ml"
from_topic: ""
to_topic: "trustworthy-distributed-ml"
relation_types:
  - "application"
  - "coordination"
  - "auditability"
  - "incentive"
directionality: "one_way"
relationship_thesis: "Blockchain systems can supply participant coordination, tamper-resistant training traces, validation records, and reward audit rails for trustworthy distributed ML, but they do not by themselves prove ML computation correctness, privacy, hardware truth, convergence, or model quality."
transferability: "medium"
non_transfer_boundary: "Consensus/audit trace transfers; ML training semantics, data quality, stealthy poisoning resistance, privacy leakage, hardware attestation, proof-of-computation, and deployment performance must be handled by ML/security mechanisms outside the chain."
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
  - "nahida-knowledge-trustworthy-distributed-ml"
representative_source_refs:
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
query_keys:
  - "blockchain coordination for trustworthy distributed ML"
  - "blockchain-coordinated distributed training"
  - "TDML blockchain coordination"
  - "proof of training trace audit"
  - "remote trainer validation"
aliases:
  - "Blockchain coordination to trustworthy distributed ML"
domains:
  - "blockchain-systems"
  - "ml-systems"
topics:
  - "trustworthy-distributed-ml"
  - "blockchain-coordinated-training"
  - "remote-trainer-validation"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
source_refs:
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
confidence: "high"
trust_tier: "primary"
---

# Blockchain coordination -> trustworthy distributed ML

## 连接命题

[[blockchain-systems|Blockchain systems]] can be applied to [[trustworthy-distributed-ml|Trustworthy distributed ML]] as a coordination and audit layer: public chains can publish jobs and resource offers, private chains can record training/validation traces, and tamper-resistant transaction logs can support reward settlement. TDML is the current source-backed seed for this bridge.

The relation is one-way application, not concept merger. Blockchain gives a shared record and coordination substrate; it does not make remote ML training correct, private, robust, or high-quality by itself.

## 端点范围

| Endpoint | Path | Scope in bridge | Evidence | Notes |
| --- | --- | --- | --- | --- |
| [[blockchain-systems|Blockchain systems]] | `blockchain-systems` | public/private chain transaction record, participant coordination, tamper-resistant audit trace, reward evidence | TDML §2.2, §3.2, §3.3.2 | Broad endpoint because the vault does not yet have a dedicated blockchain-coordination-for-compute node. |
| [[trustworthy-distributed-ml|Trustworthy distributed ML]] | `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | distributed training with public remote trainers, model/data transfer, validation, malicious trainer detection, incentives | TDML §3.1-§4 | Topic endpoint is specific and source-backed. |

## 端点基础说明

Blockchain systems are distributed ledgers that coordinate state transitions through consensus and store tamper-resistant transaction histories. In this bridge, the relevant subset is not consensus research itself, but the use of public/private chain records as a coordination and audit rail for participants, training events, validation outputs, and rewards.

Trustworthy distributed ML concerns training systems where data, model shards, gradients, parameter servers, and compute nodes cross trust boundaries. Its core question is whether remote training workload and participant behavior can be validated, traced, and governed without assuming every trainer is honest.

## 可迁移知识/模式

| 概念/模式 | 来源方向 | 目标方向 | 可迁移部分 | 不可迁移部分 |
| --- | --- | --- | --- | --- |
| Tamper-resistant transaction log | blockchain-systems | trustworthy distributed ML | record job requests, trainer registration, local model updates, validation results, reward traces | does not prove training computation was correct |
| Public participant coordination | blockchain-systems | trustworthy distributed ML | publish tasks, hardware specs, rewards, trainer/parameter-server registration | does not verify hardware specs or identity beyond system assumptions |
| Private task chain | blockchain-systems | trustworthy distributed ML | maintain task-scoped trace and selected participant state | does not define privacy policy or access control fully |
| Smart-contract/reward audit pattern | blockchain-systems | trustworthy distributed ML | support transparent reward settlement after validation | does not prove incentive compatibility under collusion |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Job/resource discovery | `blockchain-systems` | `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | Public chain publishes client job, parameter-server registration, trainer hiring and hardware specs. | TDML §3.2.1-§3.2.3 | spam, false specs, chain latency, identity management |
| Training trace audit | `blockchain-systems` | `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | Private chain stores local model updates, trainer outputs and validation results. | TDML §3.3.2 | trace is not proof of correct computation |
| Reward evidence | `blockchain-systems` | `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | Clients review chain trace to reward trainers/parameter servers. | TDML §3.3.3 | incentive model is informal |
| Validation trigger | `blockchain-systems` | `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | Private-chain pending validation jobs coordinate idle parameter server validation. | TDML §3.2.1 | validation quality depends on test data and majority assumptions |

## 类比、依赖或关系边界

- 可迁移: participant coordination, tamper-resistant records, auditability, validation-event publication, reward settlement evidence.
- 不可迁移: model convergence, training correctness, formal privacy, poisoning robustness, remote hardware truth, secure tensor/gradient semantics, dataset representativeness.
- 关键假设: chain consensus works, participant access is managed, private-chain records are available for audit, and ML-side validation detects meaningful failures.
- 失效条件: adaptive/colluding trainers, invalid hardware specs, representative test data absent, chain latency/cost too high, private-chain access leaks sensitive training traces, or attackers generate plausible but harmful gradients.

## 证据

| Source/Note | 支撑内容 | 置信度 | 局限 |
| --- | --- | --- | --- |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] Abstract and §1 | Blockchain is proposed to coordinate remote trainers and validate workloads for public remote computing resources. | high | Source-authored claim. |
| Same source §3.2 | Public/private blockchain workflows for data/model parallelism, task publishing and trainer registration. | high | Framework-level design, not full production implementation. |
| Same source §3.3.2 | Proof of Training as traceability/reproducibility record on private chain. | high | Not a cryptographic proof. |
| Same source §4 | ResNet50/CIFAR-10 prototype and malicious gradient attack experiments. | medium | Not a real large-model or deployed blockchain experiment. |

## 路径传播

| Endpoint path | Knowledge update | Relation/index update | Bridge/refresh action | Status |
| --- | --- | --- | --- | --- |
| `blockchain-systems` | Add TDML as application source extension for blockchain coordination in ML systems. | Add `bridges_to` bridge row. | Created this bridge. | done |
| `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | Created active seed problem node. | Add bridge/evidenced_by edges. | Created this bridge. | done |
| `ml-systems/privacy-and-trustworthy-ml` | Add child node and method route. | Add has_child/evidenced_by/bridges_to edges. | Bridge link row. | done |

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[blockchain-systems|Blockchain systems]] | Source Extensions; Bridge Links; relation edges | Blockchain is used as coordination/audit infrastructure for TDML. | done |
| [[trustworthy-distributed-ml|Trustworthy distributed ML]] | New node | TDML reveals a reusable problem layer. | done |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | Child structure and method route | Trustworthy remote training is a new child problem under ML trust. | done |
| [[ml-systems|ML systems]] | Method/source extension and domain dynamics | Expands ML systems beyond FL integrity and synthetic data. | done |

## 查询入口

- Query keys:
  - blockchain coordination for trustworthy distributed ML
  - blockchain-coordinated distributed training
  - TDML blockchain coordination
  - proof of training trace audit
  - remote trainer validation
- Aliases:
  - Blockchain coordination to trustworthy distributed ML
- 典型问题:
  - Blockchain 能给 distributed ML training 带来什么可信性?
  - TDML 的 Proof of Training 是不是 ZK proof?
  - Remote trainers 作恶时，链上记录能解决什么、不能解决什么?
  - public chain/private chain 在 TDML 里分别做什么?

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-23`
- Refresh triggers:
  - 新 blockchain-based FL/DML source 被吸收。
  - 新 decentralized compute/resource marketplace source 被吸收。
  - 新 remote trainer attestation、TEE、ZK proof-of-training 或 robust distributed training source 被吸收。
  - 用户询问 blockchain + distributed ML 的最新工业实践，需要 daily-fetch/research-search。

## 复核笔记

- 本 bridge 是 active_seed，因为当前只有 TDML 一篇 source 直接支撑。
- Endpoint `blockchain-systems` 目前偏宽；后续若出现多篇 compute coordination / blockchain resource marketplace source，应拆出更具体的 blockchain coordination / decentralized compute 子节点，再把本 bridge endpoint 收窄。
- 不应把 TDML 的 trace-based Proof of Training 合并到 ZK proof-of-training；二者边界在 source note 和本 bridge 中已明确。

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Created bridge from blockchain coordination/audit rails to trustworthy distributed ML using TDML. | 1 source note | codex |
