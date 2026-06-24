---
id: "nahida-knowledge-zkml-verifiable-aggregation"
title: "Verifiable aggregation"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "verifiable-aggregation"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
parent_knowledge_refs:
  - "nahida-knowledge-zkml"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-aggregation"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-aggregation"
secondary_ontology_paths:
  - "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
relation_edges:
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "is_a"
    to: "nahida-knowledge-zkml"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-aggregation.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "bridges_to"
    to: "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
    evidence_refs:
      - "vault/05_Bridges/zkml-verifiable-aggregation-to-federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-aggregation"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation"
  - "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
representative_source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
query_keys:
  - "ZK verifiable aggregation"
  - "zkML verifiable aggregation"
  - "verifiable federated aggregation"
  - "zero-knowledge federated learning aggregation"
  - "zkFL"
  - "PZKP-FL secure sum"
  - "ZKP-FL global aggregation verification"
  - "RiseFL"
  - "secure aggregation input validation"
  - "probabilistic L2 norm check"
  - "relaxed SAVI"
aliases:
  - "verifiable federated aggregation"
  - "ZK aggregation proofs for ML"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-aggregation"
  - "federated-learning-integrity"
  - "zk-snarks"
  - "secure-sum"
  - "secure-aggregation-input-validation"
  - "probabilistic-l2-check"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
  - "nahida-knowledge-20260621-pzkp-fl"
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
confidence: "high"
trust_tier: "primary"
---

# Verifiable aggregation

## 定义与范围

- 定义: Verifiable aggregation 是 zkML 中的一个问题层: 用 ZK/VC 证明一组 ML-related updates、gradients、partial results 或 commitments 被按照公开规则正确聚合，而 verifier 不必重新执行完整聚合或看到不应公开的 witness。
- 不包含: 一次模型 inference proof、完整 training provenance、单个协议名或单个 Halo2 circuit；这些分别放在 [[verifiable-inference|Verifiable inference]]、[[verifiable-training|Verifiable ML training]] 或 source note 中。
- Canonical terms: `verifiable aggregation`, `ZK verifiable aggregation`
- Aliases/query keys: verifiable federated aggregation, zero-knowledge federated learning aggregation
- Standalone completeness check: 本节点给出定义、边界、方法路线、代表 source、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“ZK 如何验证 ML 聚合”“zkFL 属于 zkML 哪类问题”时先读本节点。
- Update scope: 新 source 若涉及 ZK/MPC/VC-based aggregation proof、federated learning aggregation verification、gradient aggregation integrity，应刷新本节点。
- Domain dynamics note: [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

zkML 既可以证明单次 inference，也可以证明 training 或 data-processing relation。Verifiable aggregation 位于两者之间: 它不证明模型输出来自 input，也不证明完整训练算法；它证明某个 multi-party ML 系统事件中的 aggregation step 没有被操纵。

zkFL 是当前 seed。它把 federated learning 中 signed client updates 的 aggregation relation 编进 zk-SNARK，证明 aggregator 返回的 `w` 是合法 updates 的和。PZKP-FL 增加一条不同路线: 本地训练 proof 之后，trainers 用 secure sum、Paillier encryption、smart contract 和 Sigma proof 验证 global model aggregation，同时不暴露 local model parameters。RiseFL 再补充第三条路线: 不证明一次 inference 或完整训练，而是对 client updates 做 commitment-compatible ZKP input validation；通过 probabilistic L2-norm predicate 过滤 malformed updates，再只聚合 valid committed updates。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它可组织 FL gradient aggregation、secure aggregation audit、multi-party model-update aggregation、future ZK aggregation sources。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkFL 是第一条 source evidence；protocol details 留在 source note。
- 需要引用的更基础 Knowledge: [[zkml|zkML]], [[zk-snarks|zk-SNARKs]], [[federated-learning-integrity|Federated learning integrity]]；RiseFL 还依赖 Pedersen commitments、VSSS、Sigma protocols 和 Bulletproofs，但这些本轮只作为 source-backed 方法依赖，不单独建节点。
- 不应拆出的实例/协议/来源: zkFL 默认 source instance；Halo2 implementation and Pedersen/signature circuit details 默认 source-local，除非多来源复用。

## 解决的问题

| 子问题 | 说明 | zkFL evidence |
| --- | --- | --- |
| Update binding | 证明每个聚合输入对应某个 signed client commitment | yes |
| Correct sum/aggregation relation | 证明 global update 等于 local updates 的求和 | yes |
| Privacy of verifier/miners | 让验证方不看到 plaintext updates | partially, in blockchain-based zkFL |
| Aggregator integrity | 防止 abandoned/replaced/inserted updates | yes |
| Input-validation under secure aggregation | 在 server 看不到 individual plaintext updates 的同时，检查 update 是否满足公开 predicate | yes, RiseFL for probabilistic L2/sphere/cosine/Zeno++ style checks |
| Update quality | 判断 signed/predicate-passing update 是否语义恶意或 poisoned | no |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zkml|zkML]] | child_of | zkFL source classification correction | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| zk-SNARK aggregation relation | 把 commitments、signatures 和 sum relation 编进 proof，verifier 检查短 proof。 | Aggregation rule simple enough to encode; prover controls witness and statement. | Circuit correctness/proving cost critical; does not prove update quality. | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |
| Commitment-homomorphic aggregation | 用 Pedersen-style commitments 支持 aggregate commitment 与 local commitments 的一致性。 | Update domain can be committed in group arithmetic or encoded appropriately. | Commitment size/communication grows with model parameters; hiding/binding assumptions matter. | zkFL source note |
| Blockchain-assisted verification | Miners verify proof and anchor aggregate commitment hash on chain. | Need public verification/audit trail; chain finality acceptable. | Does not perform on-chain aggregation; data availability remains off-chain. | zkFL blockchain variant |
| Secure-sum aggregation with Sigma consistency proof | Trainers 提交 masked/encrypted local parameters；smart contract 计算 aggregate；Sigma proof 证明 secure-sum 输入与先前 modified statement 中的 local output 一致。 | FL 需要隐藏 local model/intermediate values，同时验证 global aggregate。 | 不证明 client update quality；依赖 Paillier/security-sum assumptions 和 chain execution。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| Commitment-compatible input validation | Client 对 local update 做 Pedersen commitment / VSSS secret sharing，并证明 random projection predicate 和 bounds 成立；server 只 aggregate valid committed updates。 | Secure aggregation 与 malicious-client filtering 同时需要；predicate 可以表示 L2 norm、sphere defense、cosine similarity 或 Zeno++ variant。 | 不是 zkSNARK route；验证是 relaxed/probabilistic；server cost 随 `k` 和 clients 增长；不解决 predicate-passing poisoning。 | [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 创建 verifiable aggregation seed；展示 commitments/signatures/zk-SNARK route for FL aggregation correctness | aggregator sees local updates; proof generation heavy; no malicious-client defense | `p1-p14` |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 补充 secure-sum + smart-contract aggregation route；用 Sigma proof 绑定 aggregation input 与训练 proof 的 modified statement | source also primarily targets verifiable training; aggregation route assumes smart-contract/consensus correctness and does not solve poisoning | `p4-p11` |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | paper | 补充 RiseFL secure aggregation input-validation route；用概率 L2 predicate 与 hybrid commitment 降低 ZKP cost | 不是 zkSNARK；relaxed SAVI permits slight out-of-bound pass probability; not semantic poisoning defense | `p1-p15` |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- 综合: Verifiable aggregation 是 zkML 中区别于 inference 和 full training 的问题层。zkFL 表明 ZK 可以验证多方 updates 是否按规则聚合；PZKP-FL 表明 secure sum + Sigma consistency proof + smart contract 也可作为 FL global aggregation verification route；RiseFL 表明当普通 zkSNARK 不适配 secure aggregation 的 additive-homomorphic interface 时，可以改用 Pedersen/VSSS/Sigma/Bulletproofs route 对 client update 做低成本概率验证。三者都不能替代 FL 系统对 predicate-passing poisoning、selection fairness、convergence 或 deployment cost 的分析。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 zkML/verifiable aggregation problem node；桥接到 ML systems/federated learning integrity | 定义; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收更多 ZK/FL aggregation sources 后校准 |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 增加 secure-sum / smart-contract aggregation verification route，并记录它与 local training proof 的衔接 | 背景; 方法族; 代表 Sources; 当前综合; relation graph | no | 与 zkFL/RoFL/ACORN/EIFFeL/secure aggregation sources 做后续比较 |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | 增加 non-SNARK commitment-compatible input-validation route；把 relaxed SAVI/probabilistic L2 check 放入 verifiable aggregation 的方法族 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | RoFL/ACORN/EIFFeL primary sources 吸收后复核 strict vs probabilistic taxonomy |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-zkml-verifiable-aggregation|zk-SNARKs -> zkML verifiable aggregation]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-aggregation` | application, verifiable_computation, integrity, implementation_reuse | Succinct proof and soundness transfer to aggregation relation; FL privacy/robustness do not. | active_seed |
| [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-aggregation; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, verification_transfer | ZKP route solves aggregator correctness subset; system-level FL concerns remain outside proof system. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml-verifiable-aggregation | is_a | nahida-knowledge-zkml | vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-aggregation.md | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | depends_on | nahida-knowledge-zk-snarks | zkFL proof construction | medium | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | evidenced_by | vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-aggregation | evidenced_by | vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md | source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| More ZK FL aggregation sources | zkFL、PZKP-FL、RiseFL 已给三条路线，但仍需 RoFL/ACORN/EIFFeL primary sources 稳定 taxonomy | nahida-update | high | active_seed_gap |
| Secure aggregation / privacy route | RiseFL 给出一条 secure aggregation + input validation route，但完整 secure aggregation foundation 仍缺 | nahida-research-search | high | active_seed_gap |
| Aggregation beyond FedAvg/FedSum | 不同聚合规则可能改变 proof relation | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Created zkML verifiable aggregation problem node from zkFL. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL secure-sum/global aggregation verification route. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risefl-low-cost-zkp | Added RiseFL as non-SNARK, commitment-compatible secure aggregation input-validation route. | 1 source note | codex |
