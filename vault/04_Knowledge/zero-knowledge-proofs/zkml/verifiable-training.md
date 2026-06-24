---
id: "nahida-knowledge-zkml-verifiable-training"
title: "Verifiable ML training"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "verifiable-training"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
parent_knowledge_refs:
  - "nahida-knowledge-zkml"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-training"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-training"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
relation_edges:
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "is_a"
    to: "nahida-knowledge-zkml"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-training.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "depends_on"
    to: "nahida-knowledge-memory-efficient-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
      - "vault/05_Bridges/memory-efficient-snarks-to-verifiable-ml-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-verifiable-ml-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-training"
    relation: "bridges_to"
    to: "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
    evidence_refs:
      - "vault/05_Bridges/zkml-verifiable-training-to-federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
  - "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
representative_source_refs:
  - "doi:10.1145/3658644.3690318"
  - "arxiv:2304.05590v2"
query_keys:
  - "Verifiable ML training"
  - "zero-knowledge ML training"
  - "proofs of training"
  - "zero-knowledge forest training"
  - "zkFTP"
  - "PZKP-FL"
  - "ZKP-FL"
  - "verifiable federated training"
  - "Groth16 training proof"
  - "fixed-point zkML training"
aliases:
  - "proofs of training"
  - "ZK ML training proofs"
  - "verifiable federated training"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-ml-training"
  - "proofs-of-training"
  - "federated-learning-integrity"
  - "zk-snarks"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260621-pzkp-fl"
source_refs:
  - "doi:10.1145/3658644.3690318"
  - "arxiv:2304.05590v2"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable ML training

## 定义与范围

- 定义: Verifiable ML training 研究如何证明某个模型确实由指定训练算法、数据集、随机种子和参数训练得到，并在需要时隐藏训练数据、模型结构、模型参数或中间状态。
- 不包含: 单次 prediction correctness、模型性能评估、公平性审计、训练数据合法性、proof-of-learning 的所有定义争议、某个树模型实现细节或一次 benchmark；这些需要单独 source。
- Canonical terms: `verifiable-ml-training`, `proofs of training`
- Aliases/query keys: zero-knowledge ML training, ZK ML training proofs, zkFTP
- Standalone completeness check: 本节点本地解释训练完整性问题、边界、方法路线、代表 source、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“如何证明模型训练过程诚实”“ZK proof of training 属于哪里”“Sparrow/zkFTP 解决什么问题”时先读本节点。
- Update scope: 新 source 若涉及 proof of training、proof of learning、proof of unlearning、tree/forest/neural-network training integrity 或 MLaaS integrity，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

ML prediction proof 只证明某个模型对一个输入的输出正确；training proof 则要证明模型本身是通过指定训练算法从数据得到的。训练任务通常比预测更消耗空间，因为它接触整个 dataset、histograms、gradients、randomness 或 iterative state。Verifiable ML training 因此需要同时处理:

- data/model commitment: 固定被证明的数据和模型。
- training relation: 明确训练算法和随机性。
- privacy: 隐藏数据集、模型或中间训练状态。
- prover scalability: 大数据集 training proof 不能比原生训练/认证多出不可接受的内存。

当前 primary sources 给出两条 seed 路线。Sparrow 针对 decision tree / random forest training 给出 `zkFTP`，用 certification algorithm 加 space-efficient zkSNARK 支撑大数据集训练证明。PZKP-FL 针对 federated learning 的 iterative local training，使用 Groth16 per-piece proofs、Sigma-protocol continuity proofs、fixed-point integer mapping 和 Taylor approximation 证明本地训练过程，同时把结果接入 secure-sum 聚合。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它不等于 Sparrow 或 decision trees。它组织 proof-of-training、proof-of-learning、training certification、training-data commitment、random seed handling 和 training privacy 等可复用问题。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Sparrow 是第一条代表 source；zkFTP、histogram certification 和 concrete benchmarks 留在 source note。
- 需要引用的更基础 Knowledge: [[zkml|zkML]], [[memory-efficient-snarks|Memory-efficient SNARKs]], [[verifiable-inference|Verifiable inference]]。
- 不应拆出的实例/协议/来源: Sparrow、zkFTP、LightGBM/CART/random forest、make_classification、某个 GitHub implementation 默认保留在 source/source-extension 层。

## 解决的问题

Verifiable ML training 解决的是 training integrity and privacy gap:

- verifier 需要相信模型不是事后篡改或虚假训练得到的。
- prover 可能不能公开训练数据或模型细节。
- 训练算法可能包含随机性，需要显式 seed 或 deterministic relation。
- 对大数据集，proof system 的 memory overhead 可能比训练本身更难承受。
- 应明确 proof statement 只能证明“相对于某算法和数据/seed 的训练关系”，不证明训练数据合法、模型公平、泛化能力或安全性。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zkml|zkML]] | child_of | Sparrow source absorption | active_seed |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | scalability dependency | Sparrow uses low-memory proof construction to make forest training proofs fit large datasets | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| tree/forest training proofs | route section | Sparrow currently supplies one source-backed route; not enough to split into a child node | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] | active_seed |
| neural-network / federated training proofs | route section | PZKP-FL 已提供一条 federated iterative training route，但还不足以拆成独立 child node | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] | active_seed |
| proof of unlearning | candidate problem | Not covered by Sparrow source note | none | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Training certification instead of retraining | 设计一个比训练本身更便宜的 verifier/certifier relation，证明模型满足训练输出条件。 | 训练结果可由可验证 certificate 判定。 | certification 必须与训练算法严格等价；算法随机性需显式 seed。 | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] |
| Dataset/model commitments | 对 dataset 和 model/forest commitments 后证明 relation，保护隐私并绑定对象。 | prover 不公开数据/模型或需要防止换模型。 | commitment lifecycle、版本和公开元数据仍需设计。 | Sparrow zkFTP |
| Space-efficient proof backend | 用低内存 SNARK 证明训练/认证 relation，避免 prover memory 随 dataset 爆炸。 | training/certification relation 是 data-parallel 或可拆成 data-parallel circuits。 | 可能增加 prover time；只支持适合 backend 的 circuit class。 | [[memory-efficient-snarks|Memory-efficient SNARKs]]; Sparrow |
| Modular training proof pipeline | 将 assignment、histogram、node split、well-formedness 等步骤分开证明，再用 shared commitments glue。 | 训练算法可模块化分解。 | 每个模块的 hidden inputs 和 commitments 必须一致。 | Sparrow zkFTP |
| Prediction proof composition | 训练证明后，再证明 prediction path/lookup/input relation。 | inference relation 与 committed model 兼容。 | prediction proof 仍是独立问题，可复用 [[verifiable-inference|Verifiable inference]] 路线。 | Sparrow / prior decision-tree prediction works |
| Iterative circuit splitting with continuity proofs | 将多轮训练拆成较小 piece，分别生成 Groth16 proof，再用 Sigma protocol 证明相邻 piece 的 output/input 连续。 | 训练过程可拆成重复计算 piece，且 verifier 接受多 proof / parallel proving。 | Proof 数量可能极大；CRS/setup 和 proof orchestration 复杂。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| Fixed-point and Taylor numeric adaptation | 用 Fraction-Integer mapping 把小数缩放到整数域，用 Taylor expansion 近似 non-linear operators。 | ML 算法包含 fraction、Sigmoid/tanh/exp/sqrt 等操作。 | 近似误差和 scale 选择会影响 exact semantics；仍需更多 numeric zkML sources。 | PZKP-FL §6 |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper | 创建 verifiable ML training 问题节点；提出 zkFTP for forest training/prediction，使用 certification algorithm 与 space-efficient SNARK backend | tree/forest-specific seed; deterministic training/seed assumption; quantized histograms; single-thread benchmark; formal proofs in full version | `p1-p15` |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 补强 neural-network/federated iterative training route；用 Groth16 piece proofs、Sigma continuity proofs、secure sum 和 PZKP numeric adaptation 证明本地训练与聚合 | small ML tasks only; many proofs; trusted setup by publisher; approximation/scaling semantics; no malicious-client poisoning defense | `p1-p15` |

## 正反例约束

- 正确: 把 Sparrow 的 zkFTP 作为 verifiable ML training source extension。
- 正确: 把 training proof 和 prediction proof 区分，prediction 可链接到 [[verifiable-inference|Verifiable inference]]。
- 正确: 把 prover memory bottleneck 通过 bridge 链到 [[memory-efficient-snarks|Memory-efficient SNARKs]]。
- 错误: 声称 training proof 自动证明模型公平、泛化、训练数据合法或输出真实。
- 错误: 把 zkFTP 或 Sparrow 当成基础概念节点本身。

## 当前综合

- Evidence window: `2026-06-20`，仅覆盖当前 vault 已深读 Sparrow。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-20`。
- 综合: 当前节点是 foundation_thin seed，但训练证明的覆盖比 Sparrow 单源时更完整。Sparrow 说明 tree/forest training 可以通过 certification algorithm 和低内存 proof backend 证明；PZKP-FL 说明 federated/iterative neural-network-like training 可以通过 circuit splitting、Groth16 per-piece proofs、Sigma continuity proofs 和 fixed-point/Taylor numeric adaptation 证明。二者共同提示: verifiable training 的核心不是某个模型名，而是 training relation、state continuity、numeric semantics、privacy boundary 和 prover-resource trade-off。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | 创建 verifiable ML training 问题节点；补充 certification algorithm、dataset/model commitments、space-efficient backend | 定义; 方法族; 代表 Sources; Bridge Links | yes | 吸收 neural-network training proof / proof-of-learning / proof-of-unlearning sources 后校准 |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 补充 federated iterative training proof route；记录 piece splitting、continuity proof、fixed-point/Taylor numeric adaptation 与 secure-sum aggregation boundary | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 neural-network proof-of-training / proof-of-learning / secure aggregation / numeric zkML sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[memory-efficient-snarks-to-verifiable-ml-training|Memory-efficient SNARKs -> verifiable ML training]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, scalability_enabler, privacy, implementation_reuse | Low-memory proving transfers to training-certification scalability; model fairness, data legality, accuracy and production governance do not. | active_seed |
| [[zk-snarks-to-zkml-verifiable-training|zk-SNARKs -> zkML verifiable training]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, verifiable_computation, privacy, training_integrity | Groth16 soundness/hiding transfers to per-piece training relation; numeric semantics, proof count and model quality do not. | active_seed |
| [[zkml-verifiable-training-to-federated-learning-integrity|zkML verifiable training -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-training; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, privacy, cross_domain_mapping | Training proof helps detect lazy trainers; poisoning, data quality, convergence and deployment governance remain ML-system concerns. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml-verifiable-training | is_a | nahida-knowledge-zkml | vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-training.md | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | depends_on | nahida-knowledge-memory-efficient-snarks | Sparrow zkFTP uses Sparrow backend | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | bridges_to | nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | depends_on | nahida-knowledge-zk-snarks | PZKP-FL Groth16 construction | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | evidenced_by | vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-training | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | applies_to | nahida-knowledge-federated-learning-integrity | PZKP-FL local computation verification threat model | high | active_seed |
| nahida-knowledge-zkml-verifiable-training | bridges_to | nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| More neural-network/federated proof-of-training sources 缺。 | PZKP-FL 提供第一条 federated iterative route，但仍是单源且小实验。 | nahida-update | high | queued |
| Proof-of-learning/proof-of-unlearning sources 缺。 | 训练证明、学习证明和遗忘证明的 security statement 不同。 | nahida-update / nahida-research-search | medium | queued |
| Production ML pipeline/repo evidence 缺。 | 需要验证 commitment lifecycle、dataset versioning 和 proving deployment。 | nahida-github-repo-analyze | medium | queued |
| Numeric semantics across zkML training sources 未统一。 | PZKP-FL fixed-point/Taylor、zkLLM quantization、ZKLP floating-point 还缺横向 synthesis。 | nahida-knowledge-get / nahida-research-search | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Created verifiable ML training problem node from Sparrow/zkFTP source absorption. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL as federated iterative training proof route and connected to FL integrity. | 1 source note | codex |
