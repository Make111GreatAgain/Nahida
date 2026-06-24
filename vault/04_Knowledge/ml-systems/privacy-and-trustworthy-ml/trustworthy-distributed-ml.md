---
id: "nahida-knowledge-trustworthy-distributed-ml"
title: "Trustworthy distributed ML"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "trustworthy-distributed-ml"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
parent_knowledge_refs:
  - "nahida-knowledge-privacy-and-trustworthy-ml"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "trustworthy-distributed-ml"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
secondary_ontology_paths:
  - "blockchain-systems"
relation_edges:
  - from: "nahida-knowledge-trustworthy-distributed-ml"
    relation: "is_a"
    to: "nahida-knowledge-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-trustworthy-distributed-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-trustworthy-distributed-ml"
    relation: "bridges_to"
    to: "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/blockchain-coordination-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-trustworthy-distributed-ml"
    relation: "bridges_to"
    to: "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/dnn-training-parallelism-to-trustworthy-distributed-ml.md"
      - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
  - "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
source_note_refs:
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
representative_source_refs:
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
query_keys:
  - "trustworthy distributed ML"
  - "trustworthy distributed machine learning"
  - "TDML"
  - "blockchain-coordinated distributed training"
  - "remote trainer validation"
  - "public remote computing resources"
  - "proof of training"
  - "distributed training integrity"
  - "DNN training parallelism trust boundary"
  - "pipeline parallelism remote trainers"
aliases:
  - "trustworthy distributed machine learning"
  - "可信分布式机器学习"
  - "TDML problem"
domains:
  - "ml-systems"
  - "blockchain-systems"
topics:
  - "privacy-and-trustworthy-ml"
  - "trustworthy-distributed-ml"
  - "distributed-training-integrity"
  - "blockchain-coordinated-training"
  - "malicious-node-detection"
  - "dnn-training-parallelism"
  - "training-systems"
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
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
  - "nahida-knowledge-20260623-pipedream-dnn-training-parallelism"
source_refs:
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
confidence: "medium"
trust_tier: "primary"
---

# Trustworthy distributed ML

## 定义与范围

- 定义: Trustworthy distributed ML 研究当训练数据、模型分片、梯度、参数服务器和计算节点跨多个组织或公开远程资源分布时，训练 workload、参与方行为、模型更新、审计记录和奖励结算如何保持可验证、可追溯、抗篡改和可治理。
- 不包含: 某篇论文提出的 TDML 框架本身、某个训练脚本、单次 ResNet50/CIFAR-10 实验、某个 blockchain deployment 或某个 reward policy；这些保留在 source note 或 source-extension 行里。
- Canonical terms: `trustworthy distributed ML`, `trustworthy distributed machine learning`
- Aliases/query keys: TDML, blockchain-coordinated distributed training, remote trainer validation, proof of training
- Standalone completeness check: 本节点本地解释了问题边界、威胁模型、解决路线、代表 source、bridge 和缺口；读者不必打开 TDML 论文也能理解该问题层。
- Retrieval role: 查询公共远程算力训练、remote trainers 是否可信、distributed ML 里的 blockchain 协调、proof of training 与 ZK proof 区别时，先读本节点。
- Update scope: 新 source 若涉及 decentralized/distributed training, remote compute marketplace, blockchain FL/DML, malicious trainer detection, proof-of-training, robust distributed training, trainer attestation，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: Distributed ML 不只关心训练速度，也关心训练责任边界。传统 data parallelism、model parallelism、pipeline parallelism 和 federated learning 假设的协调环境各不相同: 有的默认节点由同一组织管理，有的默认客户端只持有本地数据，有的只处理单一 aggregator 的正确性。若训练算力来自公共远程节点，系统还需要回答谁发布任务、谁提供硬件、谁能看到数据/模型/中间 tensor、谁验证训练结果、谁承担奖励与惩罚。

TDML 当前给出本节点的第一个 source-backed seed。它把可信分布式训练拆成 public blockchain job/resource discovery、private blockchain training trace、IPFS data references、encrypted RPC tensor transfer、cross-validation、gradient-based malicious trainer detection 和 reward audit。这个 seed 的重点是 system trust orchestration，不是 zero-knowledge proof 或形式化 verifiable computation。

PipeDream 作为 bridge evidence 补清了一个边界: data/model/pipeline parallelism 可以作为 TDML 这类系统的 execution substrate，但 PipeDream 本身只解决受控集群里的训练吞吐、communication bottleneck、pipeline scheduling 和 parameter versioning；它不解决 remote trainer honesty、privacy、hardware attestation 或 reward accountability。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它可组织远程训练节点可信性、public compute resource coordination、训练 trace audit、malicious trainer detection、blockchain-coordinated training、trainer attestation 和 reward/incentive governance 等后续来源。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: TDML 是代表 source；本节点的持久对象是“分布式训练可信性”问题，而不是 TDML 的 8/10-step workflow。
- 需要引用的更基础 Knowledge: [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]], [[ml-systems|ML systems]], [[blockchain-systems|Blockchain systems]].
- 不应拆出的实例/协议/来源: TDML、具体 ResNet50/CIFAR-10 原型、某个梯度攻击实验、某个 reward budget 字段默认留在 source note。

## 解决的问题

| 子问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Remote trainer selection | 如何发现、筛选、接入公开远程算力节点 | TDML public blockchain job/trainer registration |
| Training workload traceability | 如何记录每个 epoch 的 local model、trainer outputs、validation results 和 reward evidence | TDML private blockchain trace |
| Data/model transfer boundary | 数据 batch、model shards、intermediate tensors 和 gradients 如何在 public network 中传输 | TDML IPFS CIDs + encrypted RPC + encrypted transactions |
| Malicious trainer detection | remote trainer 可能提交伪造 tensor/gradient 或扰动 local model，系统如何定位并隔离 | TDML cross-validation + gradient clustering |
| Aggregation filtering | 如何减少 poor/malicious local models 对 global model 的影响 | TDML top-K local model aggregation |
| Reward/accountability | 如何按训练 trace 分配 reward 并提高作恶成本 | TDML incentive discussion |
| Formal training correctness | 是否能不用重算就证明训练按算法完成 | TDML does not solve; proof-of-training is trace-based audit |
| Privacy leakage | 是否防止 gradients/intermediate states 泄露训练数据或模型 | TDML only partially addresses transmission secrecy; no formal privacy proof |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | child_of | TDML source classification and privacy/trust boundary | active_seed |
| [[ml-systems|ML systems]] | part_of domain | TDML is a distributed ML training system source | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| blockchain-coordinated training | method family candidate | 如果后续多篇论文/仓库都用链上任务协调、私链审计和 reward trace，可拆成方法族节点。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] | candidate |
| malicious trainer detection | subproblem candidate | 当前只有 TDML 的 cross-validation + gradient clustering seed；需更多 robust DML/FL sources。 | TDML §3.3 and §4.4 | watch |
| trainer attestation / remote hardware trust | foundation gap | TDML 只让 trainers 注册 hardware specs，没有证明 remote environment integrity。 | TDML limitation | queued |
| decentralized compute marketplace for ML | adjacent application/problem | TDML 有 reward budget 和 public remote resources，但 marketplace 证据不足。 | TDML §3.2.3 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Blockchain-coordinated training trace | 用 public chain 做 job/resource discovery，用 private chain 记录训练过程、validation results 和 reward evidence。 | 需要跨组织或公开远程节点参与，且 auditability 比纯性能更重要。 | 不自动证明计算正确、隐私、硬件真实性或模型质量；chain latency/cost 未评估。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] |
| Cross-validation-based model screening | 空闲 parameter server 用 test dataset 验证其他 local models，并用低性能 outlier 触发检测。 | 有可用 test dataset，且 local model performance 能反映恶意或无效训练。 | stealthy poisoning 和 data-quality attack 可能通过；test dataset 代表性是信任边界。 | TDML |
| Gradient-based malicious trainer localization | 对 layer gradients 投影并聚类，识别 manipulated gradients，再映射到 trainer。 | 恶意 gradients 与 benign gradients 可分离。 | 对 collusion、small stealthy perturbation、adaptive attacker 的边界不充分。 | TDML; MANDERA as prior work |
| Top-K local model aggregation | 只平均 top-K best local models，以过滤 poor/malicious local models。 | 存在多个 data-parallel local models 且 validation results 可比较。 | 可能牺牲 diversity；不证明剩余 top-K 都 benign。 | TDML |
| Parallel-training execution substrate | 使用 data/model/pipeline parallelism 承载分布式训练 workload，提高吞吐或突破单机内存。 | 可信性系统仍需要实际训练 runtime 和 parallelism primitives。 | 性能并行不证明 trainer 诚实、不保护隐私、不提供 attestation 或 reward audit。 | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] via bridge |
| Cryptographic proof-of-training | 用 ZK/VC/TEE/attestation 证明训练 computation 或环境状态。 | 需要强正确性而不愿重算训练。 | TDML 未实现；是后续扩展方向。 | gap |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | paper | 创建 trustworthy distributed ML problem seed；提出 blockchain-coordinated data/model parallelism、remote trainer validation、malicious-gradient detection 和 reward trace route。 | ResNet50/CIFAR-10 原型；无真实大模型；无 formal privacy/security proof；proof-of-training 是 trace audit 不是 ZK proof。 | `p1-p11`; §3.1-§3.3; §4 |

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current-vault source absorption; not an external latest claim.
- Valid until: `2026-07-23`.
- 综合: Trustworthy distributed ML 当前是 active_seed 问题节点。TDML 表明，当 ML 训练转向公开远程算力时，可信性问题会从 FL 的 aggregation correctness 扩展到任务发布、资源筛选、模型切分、训练 trace、跨验证、恶意 trainer 定位和 reward settlement。Blockchain 可作为协调和审计基础设施，但它提供的是 traceability 与 tamper-resistant record，不是训练计算正确性、隐私或硬件可信性的完整证明。后续要把这个节点做实，需要补充 robust distributed training、trainer attestation、decentralized compute marketplace、privacy leakage 和 cryptographic proof-of-training sources。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | 新增 trustworthy distributed ML problem node；把 blockchain coordination 与 ML training trust 通过 bridge 连接；纠正 queue 中 zkML/verifiable-inference 误分。 | 全文; Bridge Links; 缺口与队列 | yes | 后续吸收 BFL/robust distributed training/attestation/decentralized compute sources 后校准 |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | 补充 performance parallelism substrate 与 trust boundary；明确 PipeDream 是训练吞吐系统，不是可信远程训练方案。 | 背景; 方法族; Bridge Links; 缺口与队列 | no | 后续吸收现代训练系统和 remote-training trust sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]] | `blockchain-systems; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | application, coordination, auditability, incentive | Blockchain transfers participant coordination and tamper-resistant trace; it does not transfer ML correctness, privacy, hardware attestation, convergence or model quality. | active_seed |
| [[dnn-training-parallelism-to-trustworthy-distributed-ml|DNN training parallelism -> trustworthy distributed ML]] | `ml-systems/training-systems/dnn-training-parallelism; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | substrate, contrast, trust_boundary, implementation_reuse | Parallel training transfers performance substrate and terminology; it does not transfer remote trainer trust, privacy, hardware attestation, malicious-node detection or reward accountability. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-trustworthy-distributed-ml | is_a | nahida-knowledge-privacy-and-trustworthy-ml | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml.md | high | active_seed |
| nahida-knowledge-trustworthy-distributed-ml | evidenced_by | vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md | source note | high | active_seed |
| nahida-knowledge-trustworthy-distributed-ml | bridges_to | nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml | bridge note | high | active_seed |
| nahida-knowledge-trustworthy-distributed-ml | bridges_to | nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Blockchain/DML foundation sources | TDML 是单篇 source，不能代表 blockchain-based DML 全景。 | nahida-research-search / nahida-update | high | active_seed_gap |
| Trainer attestation and hardware truth | TDML 让 trainers 注册硬件规格，但没有证明远程环境真实性。 | nahida-research-search / nahida-github-repo-analyze | high | queued |
| Formal proof-of-training | TDML proof-of-training 是 trace audit，不是 cryptographic proof。 | nahida-update | medium | queued |
| Robust distributed training under adaptive attacks | TDML 只评估 zero/mean/Gaussian attacks。 | nahida-update | high | queued |
| Blockchain overhead and deployment evidence | TDML 没有量化 chain/IPFS/RPC cost。 | nahida-github-repo-analyze / nahida-update | medium | queued |
| Parallelism/trust boundary sources | PipeDream 只覆盖性能并行，TDML 覆盖可信协调；仍缺二者在现代 remote/decentralized training 中结合的 source。 | nahida-update / nahida-github-repo-analyze | medium | active_seed_gap |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Created problem seed from TDML and connected it to blockchain coordination bridge. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Added bridge boundary to DNN training parallelism / PipeDream; kept PipeDream as performance substrate evidence, not trust solution. | 1 source note | codex |
