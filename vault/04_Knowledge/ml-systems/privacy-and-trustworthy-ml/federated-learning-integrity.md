---
id: "nahida-knowledge-federated-learning-integrity"
title: "Federated learning integrity"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "federated-learning-integrity"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
parent_knowledge_refs:
  - "nahida-knowledge-privacy-and-trustworthy-ml"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "federated-learning-integrity"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-aggregation"
  - "zero-knowledge-proofs/zkml/verifiable-training"
relation_edges:
  - from: "nahida-knowledge-federated-learning-integrity"
    relation: "is_a"
    to: "nahida-knowledge-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-federated-learning-integrity"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-federated-learning-integrity"
    relation: "bridges_to"
    to: "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
    evidence_refs:
      - "vault/05_Bridges/zkml-verifiable-aggregation-to-federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-federated-learning-integrity"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-federated-learning-integrity"
    relation: "bridges_to"
    to: "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
    evidence_refs:
      - "vault/05_Bridges/zkml-verifiable-training-to-federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-federated-learning-integrity"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
  - "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
representative_source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
query_keys:
  - "federated learning integrity"
  - "verifiable federated learning"
  - "malicious aggregator"
  - "federated aggregation verification"
  - "zkFL"
  - "PZKP-FL"
  - "verifiable federated training"
  - "lazy trainer"
  - "RiseFL"
  - "secure aggregation input validation"
  - "relaxed SAVI"
  - "probabilistic L2 norm check"
aliases:
  - "FL integrity"
  - "verifiable federated learning"
  - "federated aggregation integrity"
  - "federated training integrity"
domains:
  - "ml-systems"
topics:
  - "federated-learning"
  - "federated-learning-integrity"
  - "verifiable-aggregation"
  - "verifiable-training"
  - "malicious-aggregator"
  - "lazy-trainer"
  - "malicious-client-input-validation"
  - "secure-aggregation"
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

# Federated learning integrity

## 定义与范围

- 定义: Federated learning integrity 研究多 client 协作训练中，local updates、aggregation result、participant set、round state 和 audit record 是否被正确处理，尤其是 aggregator/coordinator 是否可能篡改 global update。
- 不包含: 单个协议名、某个 ZKP circuit、某个模型 benchmark 或全部 FL privacy 问题；这些分别留在 source note、ZKP application node 或相邻问题节点。
- Canonical terms: `federated learning integrity`, `verifiable federated learning`
- Aliases/query keys: FL integrity, federated aggregation integrity, malicious aggregator
- Standalone completeness check: 本节点给出问题定义、威胁边界、解决路线、代表 source、当前综合和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“FL aggregator 能不能作恶”“如何验证 federated aggregation”“zkFL 解决什么问题”时先读本节点。
- Update scope: 新 source 若涉及 FL aggregation verification、secure/robust aggregation、malicious clients、blockchain FL、ZKP/MPC/TEE based verification，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

Federated learning 把训练数据留在 clients 本地，但 global model 仍依赖一个或多个 coordinating/aggregation components。即使数据不集中，系统仍可能出现 integrity failure: aggregator 可选择哪些 updates 进入 global update、如何加权、是否伪造参与者、是否把不同结果返回给不同 clients。

zkFL 提供当前 vault 的第一个 source-backed seed: 对每轮 signed client updates 的 commitments 和 sum relation 生成 zk-SNARK proof，让 clients 或 miners 验证 aggregation correctness。PZKP-FL 补充第二条 seed: 用 Groth16/Sigma proofs 验证 trainers 的本地训练过程，并用 secure sum + smart contract 验证 global aggregation，从而把 lazy trainer 和 unreliable publisher 都纳入同一 FL integrity 视角。RiseFL 补上第三条 seed: 在 single-server secure aggregation 设置中，用 Pedersen commitment、VSSS、Sigma/Bulletproofs-style proofs 和 probabilistic L2-norm check 过滤 malformed client updates，同时尽量保持 client input privacy。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它组织 malicious aggregator、verifiable aggregation、blockchain-audited FL、secure aggregation integrity 和 robust FL 等来源。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkFL 是当前代表 source；protocol details、FedAvg benchmark 和 Halo2 implementation 留在 source note。
- 需要引用的更基础 Knowledge: [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]], [[ml-systems|ML systems]]。
- 不应拆出的实例/协议/来源: zkFL、PZKP-FL、RoFL、RiseFL 默认作为 source/system instances，除非多来源支撑独立方法族节点。

## 解决的问题

| 子问题 | 说明 | 当前 zkFL 覆盖度 |
| --- | --- | --- |
| Aggregator abandonment | aggregator 丢弃某些 honest updates | covered |
| Aggregator replacement | aggregator 用 fake update 替换 signed client update | covered |
| Fake insertion | aggregator 插入 fake client/update | covered |
| Lazy trainer local computation cheating | trainer 不真实训练，只提交随机/伪造 local parameters | covered by PZKP-FL local computation proofs |
| Publisher incorrect global aggregation | publisher 返回与 secure-sum 不一致的 global model | covered by PZKP-FL aggregation proof route |
| Client poisoning | client 提供恶意但签名合法的 update | partially covered by RiseFL when the update violates public predicates; not covered for predicate-passing poisoning |
| Aggregator privacy leakage | aggregator 从 plaintext updates 推断 client data | partially covered by RiseFL secure aggregation route; not covered by zkFL base route |
| Cross-round auditability | 让下一轮 participants 检查前一轮 aggregate | partially covered by blockchain-based zkFL |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | child_of | zkFL source classification | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Commitment + signature based update binding | 每个 client 对 committed update 签名，使 aggregator 不能替换 statement 中的 update。 | PKI 或公钥分发可信；clients 能签名并发送 commitments。 | 只绑定来源与 statement，不判断 update 是否 benign。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |
| [[verifiable-aggregation|ZK verifiable aggregation]] | aggregator 证明 aggregate 等于全部 signed committed updates 的求和。 | Aggregation relation 可电路化，prover 成本可承受。 | Proof generation heavy；circuit correctness 成为信任边界。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |
| Blockchain-based proof verification | miners 验证 proof，并把 `H(Enc(w))` 上链，让 selected clients 检查 round state。 | 需要公开验证和跨轮 audit trail；链 finality/gas 可接受。 | 不做 on-chain aggregation；finality、data availability、hash anchoring 仍是系统假设。 | zkFL blockchain variant |
| [[verifiable-training|ZK verifiable local training]] | 每个 trainer 对本地训练 piece 生成 Groth16 proof，并用 Sigma proof 绑定 piece continuity，防止少训练或伪造参数。 | 训练算法可电路化且可拆 piece；系统能承受大量 proofs。 | 不判断数据质量或 poisoning；proof/orchestration 成本高。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| Secure-sum global aggregation verification | Trainers 用 Paillier/mask secure sum 提交 local parameters，并用 Sigma proof 证明聚合输入与训练输出一致。 | 需要隐藏 local model/intermediate values，同时验证 aggregate。 | 依赖 smart contract/consensus 和 encryption assumptions；不解决 client quality。 | PZKP-FL |
| Secure aggregation input validation | Clients 先承诺 update 并证明其满足公开 predicate；server 只聚合未被标记的 committed/secret-shared valid updates。 | 单 server FL；最多 `m < n/2` malicious clients；update quality 可用 L2/sphere/cosine/Zeno++ 类 predicate 近似。 | relaxed/probabilistic；轻微越界可能通过；不判断语义 poisoning、数据质量或 convergence。 | [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] |
| Secure aggregation privacy | 隐藏 local updates，使 aggregator 不能直接看到 client updates。 | 目标是 privacy rather than integrity；可与 integrity route 组合。 | 当前 source 未覆盖，需新 sources。 | gap |
| Robust aggregation against malicious clients | 降低 poisoned updates 对 global model 的影响。 | clients themselves may be adversarial。 | zkFL 不解决，需要独立 problem/source。 | gap |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 创建 malicious-aggregator / verifiable aggregation seed；给出 base zkFL 和 blockchain-based zkFL | aggregator sees local updates; no malicious-client defense; proof generation and communication heavy | `p1-p14` |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 补充 lazy-trainer local computation verification、secure-sum aggregation verification 和 local data/intermediate privacy route | 小模型实验；大量 proofs；trusted setup and numeric approximation assumptions; 不解决 poisoning/update quality | `p1-p15` |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | paper | 补充 RiseFL: secure aggregation + probabilistic input validation route，区分 malicious-client malformed-update filtering 与 malicious-aggregator verification | relaxed SAVI; single-server; not zkSNARK-based; predicate-passing poisoning 和 data quality 仍不解决 | `p1-p15` |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- 综合: Federated learning integrity 与 privacy-preserving FL 是相邻但不同的问题。zkFL 的价值是把 aggregator correctness 从 trust assumption 转成 proof verification；PZKP-FL 的价值是把 trainer local computation correctness 和 publisher/global aggregation correctness 也拉进可验证范围；RiseFL 的价值是把 secure aggregation 下的 malicious-client input validation 做成低成本、Byzantine-robust 的概率证明路线。三者仍不把 FL 系统变成完全隐私、安全或鲁棒: predicate-passing poisoning、数据质量、participant selection、convergence、server/system governance 和生产成本仍需独立 source。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 malicious aggregator / aggregation verification problem seed；补充 blockchain verification variant | 定义; 解决的问题; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 RoFL/ACORN/EIFFeL 后校准 |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 补充 lazy trainer / unreliable publisher 双 threat model；加入 local computation verification、secure-sum aggregation verification 与 local-data privacy route | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续与 RoFL/ACORN/EIFFeL/secure aggregation/robust FL sources 比较 |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | 补充 RiseFL malicious-client malformed-update filtering route；把 secure aggregation privacy 与 probabilistic predicate validation 接到同一 FL integrity 视角 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL primary sources 后稳定 secure aggregation input-validation taxonomy |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-aggregation; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, verification_transfer | Proof verifies aggregation relation; FL convergence, privacy, client robustness and deployment governance do not transfer automatically. | active_seed |
| [[zkml-verifiable-training-to-federated-learning-integrity|zkML verifiable training -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-training; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, privacy, cross_domain_mapping | Training proof detects lazy local computation; poisoning, data quality and convergence do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-federated-learning-integrity | is_a | nahida-knowledge-privacy-and-trustworthy-ml | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity.md | high | active_seed |
| nahida-knowledge-federated-learning-integrity | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | high | active_seed |
| nahida-knowledge-federated-learning-integrity | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-federated-learning-integrity | evidenced_by | vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md | source note | high | active_seed |
| nahida-knowledge-federated-learning-integrity | bridges_to | nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-federated-learning-integrity | evidenced_by | vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md | source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Malicious client / poisoning route 仍薄 | RiseFL 覆盖 malformed/out-of-bound updates，但不覆盖 predicate-passing poisoning、数据质量或 adaptive poisoning | nahida-update | high | active_seed_gap |
| Secure aggregation privacy route 仍薄 | RiseFL 覆盖一条 single-server secure aggregation + validation route，但不足以代表完整 privacy-preserving FL landscape | nahida-update / nahida-research-search | high | active_seed_gap |
| RoFL/ACORN/EIFFeL primary sources 未吸收 | RiseFL 只作为 related-work 比较引用它们；需要 primary notes 稳定 strict-check vs probabilistic-check taxonomy | nahida-update | high | queued |
| Blockchain FL production constraints 缺 source | zkFL 的 chain finality/gas 是论文设置，不是当前最新事实 | nahida-daily-fetch / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Created federated learning integrity problem node from zkFL. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL as local training and secure-sum aggregation integrity route. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risefl-low-cost-zkp | Added RiseFL as secure aggregation input-validation route and clarified malicious-client vs malicious-aggregator threat boundaries. | 1 source note | codex |
