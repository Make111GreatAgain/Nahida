---
id: "nahida-knowledge-dnn-training-parallelism"
title: "DNN training parallelism"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "dnn-training-parallelism"
domain_id: "ml-systems"
direction_id: "training-systems"
parent_knowledge_refs:
  - "nahida-knowledge-ml-training-systems"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "training-systems"
  - "dnn-training-parallelism"
primary_ontology_path: "ml-systems/training-systems/dnn-training-parallelism"
secondary_ontology_paths:
  - "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
relation_edges:
  - from: "nahida-knowledge-dnn-training-parallelism"
    relation: "is_a"
    to: "nahida-knowledge-ml-training-systems"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/training-systems/dnn-training-parallelism.md"
      - "vault/04_Knowledge/ml-systems/training-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-dnn-training-parallelism"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-dnn-training-parallelism"
    relation: "bridges_to"
    to: "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/dnn-training-parallelism-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
representative_source_refs:
  - "doi:10.1145/3341301.3359646"
query_keys:
  - "DNN training parallelism"
  - "distributed DNN training"
  - "data parallelism"
  - "model parallelism"
  - "pipeline parallelism"
  - "hybrid parallelism"
  - "PipeDream"
  - "1F1B"
  - "weight stashing"
  - "training communication bottleneck"
aliases:
  - "distributed DNN training"
  - "DNN 并行训练"
domains:
  - "ml-systems"
topics:
  - "training-systems"
  - "dnn-training-parallelism"
  - "pipeline-parallelism"
  - "data-parallelism"
  - "model-parallelism"
  - "training-throughput"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-pipedream-dnn-training-parallelism"
source_refs:
  - "doi:10.1145/3341301.3359646"
confidence: "medium"
trust_tier: "primary"
---

# DNN training parallelism

## 定义与范围

- 定义: DNN training parallelism 研究如何把深度神经网络训练的 forward、backward、parameter update、activation/gradient communication 和 runtime state 分布到多个 workers/accelerators 上，同时控制吞吐、内存、通信、调度正确性和统计效率。
- 不包含: 某个具体系统名、单个 pipeline schedule、某个模型实验、某个 GPU 集群配置或某个框架 API；这些保留在 source notes。
- Canonical terms: `DNN training parallelism`, `distributed DNN training`
- Aliases/query keys: data parallelism, model parallelism, pipeline parallelism, 1F1B, weight stashing, PipeDream
- Standalone completeness check: 本节点解释 DNN 并行训练的问题、方法族、PipeDream route、适用边界和 bridge；读者不必打开 PipeDream source note 也能理解问题层。
- Retrieval role: 查询训练并行策略、pipeline parallelism、communication bottleneck、PipeDream 机制时，先读本节点，再打开 source。
- Update scope: 新 source 若涉及 data/model/pipeline/tensor parallelism、stage replication、training scheduler/runtime、large-model training parallelism 或 distributed optimizer，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: DNN 训练的核心循环包含 forward pass、loss、backward pass 和参数更新。并行训练不是简单把算子丢给更多 GPU，因为 DNN 的参数、激活、梯度和 optimizer state 在不同并行策略下会产生不同通信路径。Data parallelism 复制完整模型并同步梯度，model parallelism 切分模型，pipeline parallelism 把模型划分为 stages 并让不同 minibatches 交错前进。每条路线都在 hardware utilization、communication cost、memory footprint、统计效率和实现复杂度之间交换。

PipeDream 当前给出本节点的第一个 source-backed seed。它从 data parallelism 的高 worker 通信瓶颈出发，提出把 inter-batch pipelining 加到 intra-batch parallelism 上，并用 automatic layer partitioning、stage replication、1F1B/1F1B-RR scheduling 和 weight stashing 管理吞吐和参数版本一致性。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它可组织多篇训练系统论文中的 data/model/pipeline/hybrid parallelism、communication overlap、memory tradeoff、scheduler correctness 和 time-to-accuracy 问题。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: PipeDream 是代表 source；本节点关注 DNN 并行训练问题，而不是 PipeDream 这个系统。
- 需要引用的更基础 Knowledge: [[training-systems|ML training systems]], [[ml-systems|ML systems]].
- 不应拆出的实例/协议/来源: PipeDream、1F1B、weight stashing、VerticalSync、NOAM 默认留在本节点方法路线和 source note 中，除非后续多源支持独立抽象。

## 解决的问题

| 子问题 | 说明 | PipeDream route |
| --- | --- | --- |
| Worker scaling | 增加 workers 后如何避免通信开销抵消计算收益。 | 减少跨 server all-reduce，改为相邻 pipeline stages 传 activation/gradient。 |
| Load balancing | 不同层计算时间和通信量不同，如何避免最慢 stage 决定吞吐。 | 通过 profiling + dynamic programming 自动 partition layers，并允许 stage replication。 |
| Pipeline stalls | DNN forward/backward 双向依赖会让 naive pipeline 空泡增多。 | 1F1B steady-state schedule 并发不同 minibatches 的 forward/backward。 |
| Parameter version consistency | forward 和 backward 若使用不同权重版本，梯度可能无意义。 | Weight stashing 保存 minibatch forward 时使用的 stage-level weight version。 |
| Statistical efficiency | 系统吞吐提升是否导致更多 epochs 或收敛失败。 | 评估显示达到目标精度所需 epoch 与 data parallelism 接近；staleness bounded。 |
| Memory overhead | pipeline 中 in-flight minibatches、intermediates 和权重版本会增加 memory。 | 每 stage 只持有部分模型；memory 与 data parallelism 大致同级，但仍需权衡 pipeline depth。 |
| Trust boundary | 多 worker 是否可信、远程 trainer 是否真实执行训练。 | 不由 PipeDream 解决；通过 bridge 接到 trustworthy distributed ML。 |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[training-systems|ML training systems]] | child_of | PipeDream source classification and training systems node | active_seed |

## 方法族与解决路线

| 方法/路线 | 适用问题 | 核心机制 | 风险/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Data parallelism | 模型可放入单 worker，需要简单扩展训练吞吐。 | 复制模型；不同 workers 处理不同 data shards；同步梯度/参数。 | 参数通信量随 worker 数增长；large batch/async staleness 可能影响收敛。 | PipeDream comparison |
| Model parallelism | 模型太大或某些层计算可切分。 | 模型层或算子分配给不同 workers。 | worker 空闲、手工 partitioning、activation communication。 | PipeDream comparison |
| Pipeline parallelism | 模型能按层形成 stages，需要提高 utilization。 | stages 并行处理不同 minibatches，重叠 computation/communication。 | pipeline bubbles、flush、forward/backward state dependency。 | PipeDream |
| Hybrid parallelism / stage replication | 某些 stages 是瓶颈，或部分层复制更划算。 | 对 stages 选择 replication factor，stage 内 data-parallel sync。 | 优化空间复杂，replicated stage 仍有同步成本。 | PipeDream |
| Parameter version management | Pipeline 并发导致不同 minibatches 使用不同参数版本。 | weight stashing, optional vertical sync, bounded staleness reasoning。 | 需要额外 GPU memory；不同 stages 的版本一致性仍可能松弛。 | PipeDream |

## PipeDream 对应的问题与解决方法

### 针对的问题

PipeDream 针对的是 DNN 训练在多 GPU/多服务器上继续扩展时遇到的通信瓶颈和 pipeline 利用率问题。传统 data parallelism 在高 worker 数下需要频繁跨 worker 同步大模型参数或梯度；model parallelism 虽然可以降低单 worker 内存压力，但 naive route 常让 workers 轮流空闲。PipeDream 试图在不显著增加收敛 epoch 的前提下，用 pipeline parallelism 和 hybrid stage replication 提高系统吞吐。

### 解决路径

1. Profile every layer: 记录每层 forward/backward 计算时间、activation/output size 和 weight size。
2. Optimize partition: 通过 dynamic programming 在硬件拓扑层级上搜索 stage partition、replication factor 和 in-flight minibatches。
3. Schedule with 1F1B: startup 填满 pipeline；steady state 让 worker 交替处理 forward 和 backward，减少 stalls。
4. Use 1F1B-RR for replicas: 对 replicated stages 用 deterministic round-robin 绑定 minibatch 到 worker，降低协调成本。
5. Stash weights and intermediates: 每个 minibatch 的 backward 使用其 forward 时的 weight version 和 intermediate states，保证 stage-level gradient correctness。
6. Fall back when needed: 对 ResNet-50 这类非 pipeline 友好模型，optimizer 会选择 data parallelism。

### 当前证据

PipeDream 在 VGG-16、AlexNet、GNMT、AWD-LSTM、S2VT 等 workloads 上获得显著 throughput/time-to-accuracy 提升；但在 ResNet-50 上退化到 data parallelism，说明并行策略必须由模型结构、参数/activation 通信和硬件拓扑共同决定。

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | paper | 创建 DNN training parallelism problem seed；提供 pipeline parallelism、stage replication、automatic partitioning、1F1B scheduling、weight stashing 和 evaluation evidence。 | 不解决远程不可信 worker、数据隐私、attestation 或形式化 proof-of-training；pipeline 不适合所有模型。 | `p1-p13`; §4-§6 |

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current-vault source absorption; not an external latest claim.
- Valid until: `2026-07-23`.
- 综合: DNN training parallelism 当前是 active_seed 问题节点。PipeDream 证明并行训练策略不能只按“更多 GPU”粗略选择，而要看模型层计算、参数/activation 大小、网络拓扑和收敛目标。Pipeline parallelism 能把不同 minibatches 的 forward/backward 重叠起来，减少通信暴露和 worker 空闲；但 DNN 的 backward 依赖 forward 状态，所以必须处理 parameter versioning 和 intermediate state。PipeDream 的 1F1B + weight stashing 是一个重要 route；但本节点仍需要更多 sources 才能区分现代 pipeline/tensor parallelism、ZeRO/FSDP memory optimization、large-scale LLM training runtime 和 production scheduler 的边界。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | 新增 DNN training parallelism 节点；把 PipeDream 的系统贡献放到问题层而不是提升为基础概念。 | 定义; 解决的问题; 方法族; PipeDream route; Bridge Links | yes | 后续吸收 GPipe/PiPPy/Megatron/DeepSpeed/ZeRO/FSDP 后复核是否拆 pipeline parallelism 方法节点 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[dnn-training-parallelism-to-trustworthy-distributed-ml|DNN training parallelism -> trustworthy distributed ML]] | `ml-systems/training-systems/dnn-training-parallelism; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | substrate, contrast, trust_boundary | Parallel training transfers performance mechanisms and terminology; it does not transfer trainer honesty, privacy, hardware truth, malicious-node detection or reward audit. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-dnn-training-parallelism | is_a | nahida-knowledge-ml-training-systems | vault/04_Knowledge/ml-systems/training-systems.md | high | active_seed |
| nahida-knowledge-dnn-training-parallelism | evidenced_by | vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md | source note | high | active_seed |
| nahida-knowledge-dnn-training-parallelism | bridges_to | nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Pipeline parallelism source coverage thin | PipeDream 是强 seed，但需要 GPipe/PiPPy/Megatron/DeepSpeed 等 sources 校准概念。 | nahida-update / nahida-github-repo-analyze | high | active_seed_gap |
| Tensor parallelism absent | 现代大模型训练常结合 tensor/pipeline/data parallelism。 | nahida-update | high | queued |
| Memory optimization boundary absent | ZeRO/FSDP/offloading/recomputation 与 pipeline parallelism 的关系还未系统化。 | nahida-update | high | queued |
| Trust boundary needs separate evidence | PipeDream 假设受控 workers；remote/public training 需 TDML/attestation/proof-of-training sources。 | nahida-update | medium | active_seed_gap |
| Hardware/backend evolution | 2019 PyTorch/Gloo/NCCL 限制可能已过时，需要现代 implementation evidence。 | nahida-github-repo-analyze / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Created DNN training parallelism problem node from PipeDream and linked it to trustworthy distributed ML via bridge. | 1 source note | codex |
