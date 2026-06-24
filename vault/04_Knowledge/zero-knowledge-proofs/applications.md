---
id: "nahida-knowledge-zkp-applications"
title: "ZKP applications"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "applications"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
parent_knowledge_refs:
  - "nahida-knowledge-zero-knowledge-proofs"
child_knowledge_refs:
  - "nahida-knowledge-zkp-blockchain-applications"
  - "nahida-knowledge-privacy-preserving-location-proofs"
  - "nahida-knowledge-verifiable-database-queries"
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
primary_ontology_path: "zero-knowledge-proofs/applications"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-zkp-applications"
    relation: "is_a"
    to: "nahida-knowledge-zero-knowledge-proofs"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
      - "vault/04_Knowledge/zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "has_child"
    to: "nahida-knowledge-zkp-blockchain-applications"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "has_child"
    to: "nahida-knowledge-privacy-preserving-location-proofs"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/privacy-preserving-location-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "has_child"
    to: "nahida-knowledge-verifiable-database-queries"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-applications"
    relation: "bridges_to"
    to: "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
  - "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
source_note_refs:
  - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
  - "vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md"
representative_source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1109/TBDATA.2024.3403370"
  - "iacr:2023/156"
  - "doi:10.14778/3594512.3594513"
query_keys:
  - "ZKP applications"
  - "zero-knowledge applications"
  - "zero-knowledge-proofs applications"
  - "ZK applications"
  - "succinct light-client verification"
  - "privacy-preserving blockchain authentication"
  - "zkLogin"
  - "zkRollup prover scaling"
  - "privacy-preserving location proofs"
  - "zero-knowledge location privacy"
  - "ZKLP"
  - "private proximity testing"
  - "zkML applications"
  - "verifiable inference"
  - "ZK proofs for LLMs"
  - "verifiable federated aggregation"
  - "federated learning integrity"
  - "zkFL"
  - "verifiable database queries"
  - "zero-knowledge database queries"
  - "ZK-FEDB"
  - "ZKSQL"
  - "zero-knowledge SQL"
  - "functional elementary databases"
  - "database-size hiding query proofs"
aliases:
  - "zero-knowledge applications"
  - "ZK applications"
domains:
  - "zero-knowledge-proofs"
topics:
  - "applications"
  - "blockchain-applications"
  - "trustless bridges"
  - "privacy-preserving-blockchain-authentication"
  - "zkrollup-prover-scaling"
  - "privacy-preserving-location-proofs"
  - "location-privacy"
  - "zkml"
  - "verifiable-inference"
  - "verifiable-aggregation"
  - "federated-learning-integrity"
  - "verifiable-database-queries"
  - "functional-database-queries"
  - "zero-knowledge-elementary-databases"
  - "zero-knowledge-sql"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkcross"
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260620-zklogin"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
  - "nahida-knowledge-20260623-zk-functional-elementary-databases"
  - "nahida-knowledge-20260623-zksql"
source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1109/TBDATA.2024.3403370"
  - "iacr:2023/156"
  - "doi:10.14778/3594512.3594513"
confidence: "medium"
trust_tier: "primary"
---

# ZKP applications

## 定义与范围

- 定义: ZKP applications 组织 zero-knowledge proofs 在区块链、隐私、审计、身份、机器学习和可验证数据处理等具体系统问题中的应用方式。
- 不包含: 单篇应用论文、单个协议名、某个电路实现或一次 benchmark；这些留在 `03_Sources` source note。
- Canonical terms: `zero-knowledge applications`, `ZKP applications`
- Aliases/query keys: ZK applications, zero-knowledge applications
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 ZKP applications，再按需打开 blockchain applications 或 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: [[04_Knowledge/zero-knowledge-proofs/research-dynamics|Research dynamics]]

## 背景

当前 source seeds 是 zkCross、zkBridge、zkLogin、Pianist、ZKLP 和 zkLLM。zkCross 展示一个典型应用模式: ZK proof-system 的 zero-knowledge 与 succinctness 被用于区块链互操作问题，一方面隐藏跨链交互关系，另一方面压缩审计验证。zkBridge 展示第二个模式: ZK proof-system 的 succinctness/soundness 被用于把跨链桥的 light-client verification 从链上直接执行变成短 proof verification。zkLogin 展示第三个模式: ZK 把现有身份凭证作为 hidden witness，用于隐私保护的链上认证。Pianist 展示第四个模式: 当应用已经接受 succinct verification 后，prover-side generation 本身会成为应用瓶颈，需要 distributed proof generation 支撑 zkRollup/zkEVM 批处理规模。ZKLP 展示第五个模式: ZK 把精确位置作为 hidden witness，证明地理区域或近邻关系，同时把 geospatial floating-point 数值语义作为应用正确性的关键依赖。zkLLM 展示第六个模式: ZK 可用于证明 committed model 的 LLM inference output 正确，同时隐藏模型参数。ZK-FEDB 与 ZKSQL 展示第七个模式: ZK 证明被用于数据库查询回答的 correctness/completeness，其中 ZKSQL 把该模式推进到 SQL operator pipeline。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织未来 zkLogin、zkML、zkBridge、privacy-preserving audit、verifiable database 等应用来源。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkCross 只是 application source extension；本节点是 ZKP 域的应用方向。
- 需要引用的更基础 Knowledge: [[zero-knowledge-proofs|zero-knowledge-proofs]]。
- 不应拆出的实例/协议/来源: zkCross、zkBridge、zkLogin、zkLLM 等默认作为 source/system instances，除非多来源证明需要独立子问题节点。

## 解决的问题

把 ZK 的隐私性、可验证性和 succinct verification 能力映射到具体系统目标，同时明确哪些代价被转移到 prover、setup、gas、硬件或协议假设中。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zero-knowledge-proofs|Zero-knowledge proofs]] | child_of | zkCross source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[blockchain-applications|ZKP blockchain applications]] | child | blockchain 是当前 source 队列中 ZKP 应用最密集的方向之一 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] | active_seed |
| [[privacy-preserving-location-proofs|Privacy-preserving location proofs]] | child | location privacy 是非区块链应用问题，且 ZKLP 给出 geospatial proof + proximity testing 完整 seed | [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] | active_seed |
| [[verifiable-database-queries|Verifiable database queries]] | child / problem | ZK-FEDB exposes committed functional-query completeness; ZKSQL exposes SQL/operator-at-a-time answer integrity. | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB]]; [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Privacy applications | 用 zero-knowledge 隐藏 witness、地址、preimage 或交易内容，同时保持可验证性。 | 系统需要验证约束但不能暴露敏感数据。 | 匿名集合、metadata leakage 和 proof setup 仍可能限制隐私。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| Succinct audit/verification | 用 succinct proof 把大量交易/状态检查压缩成低成本 verification。 | verifier/on-chain/auditor 资源昂贵，prover 可离线承担成本。 | proving 成本、circuit size、gas 和可信 setup 需要单独评估。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| Succinct state/light-client verification | 用短证明把昂贵的跨链状态转移或 light-client verification 压缩到 receiver/on-chain verifier 可承担的成本。 | verifier/on-chain 资源昂贵，且系统能把验证逻辑电路化。 | 不能替代底层链安全、liveness 或应用状态语义；prover/递归成本需要评估。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Privacy-preserving credential authentication | 用 ZK 证明身份凭证、地址和临时签名 key 的关系，同时隐藏凭证内容和 stable identifier。 | 应用需要复用 Web2/legacy credentials 进行链上认证，但不能公开身份细节。 | 仍需要身份提供方信任、salt 管理、JWK freshness、应用活性和恢复策略。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |
| zkRollup prover scaling | 用 distributed proof generation 分摊 rollup/zkEVM proof generation 的 time/memory bottleneck，使更大 batch 能在固定窗口内生成 proof。 | proof verification 已经可接受，但 prover 端成为 throughput 瓶颈。 | 不解决 data availability、sequencer ordering、rollup security 或 prover economics；具体收益依赖 proof-system/circuit/backend。 | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] |
| Privacy-preserving location proofs | 用 ZK 证明 precise location witness 满足 region/cell/proximity predicate，同时隐藏精确经纬度。 | 应用需要验证地理位置关系，但不能暴露用户完整位置。 | 主电路不保证位置来源真实；还需要 location provenance 或 authenticated sensor/GNSS/TLS route。 | [[privacy-preserving-location-proofs|Privacy-preserving location proofs]]; [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] |
| Verifiable ML/LLM inference | 用 ZK proof 证明 committed model 的 output 确实由指定 input 推理得到，同时隐藏模型参数或 witness。 | 模型 owner 需要接受审计但不公开 proprietary weights。 | 只证明 inference relation；不证明训练来源、模型版权、fairness、safety 或输出事实性。 | [[zkml|zkML]]; [[verifiable-inference|Verifiable inference]]; [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] |

| Verifiable federated aggregation | 用 ZK proof 证明 federated learning aggregate 来自合法 signed updates，并可把验证外包给 clients/miners。 | FL aggregator 不能被完全信任，且 aggregation relation 可电路化。 | 不解决 malicious clients、aggregator privacy 或 proof-generation cost。 | [[verifiable-aggregation|Verifiable aggregation]]; [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |
| Verifiable database queries | 用 ZK query proof 证明返回 records 或 SQL answer 满足查询且没有遗漏匹配 records，同时隐藏未返回数据、数据库大小、input rows 或 intermediate results。 | 数据库/目录/承诺数据结构需要可验证查询，而不能把全库或所有非匹配记录暴露给 verifier。 | ZK-FEDB 覆盖 elementary database functional queries；ZKSQL 覆盖公开 query/DAG/cardinality 条件下的 SQL operator pipeline；query privacy、storage execution 和 transactions 仍需独立 source。 | [[verifiable-database-queries|Verifiable database queries]]; [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB]]; [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | paper | 增加 ZKP application seed：ZK 用于跨链 unlinkability 和审计压缩 | 应用 source；不作为 zk-SNARK foundation definition | `p1-p17` |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 增加 ZKP application seed：ZK 用于 trustless bridge/light-client verification compression | 应用 source；不作为 zk-SNARK foundation definition | `p1-p15` |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | paper | 增加 ZKP application seed：ZK 用于身份凭证隐私和链上认证 | 应用 source；不作为 zk-SNARK foundation definition | `p1-p20` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 增加 ZKP application seed：distributed proof generation 用于 zkRollup/zkEVM prover scalability | 应用/proof-system bridge source；不作为 rollup security foundation | `p1-p15` |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | paper | 增加 ZKP application seed：privacy-preserving location proofs and private proximity testing | 应用/proof-system bridge source；不保证 location authenticity | `p1-p19` |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | paper | 增加 ZKP application seed：verifiable LLM inference and model-parameter privacy | 应用/proof-system bridge source；不保证 training provenance or AI safety | `p1-p16` |

| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 新增 ZKP application seed: verifiable aggregation for federated learning and blockchain-assisted verification | aggregator sees local updates; no malicious-client defense; proof generation heavy | `p1-p14` |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | paper | 新增 ZKP application seed: functional database query correctness/completeness with database-size hiding | elementary database functional queries only; not SQL, aggregate analytics or transaction processing | `Abstract`, `§1`, `§4-§5` |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs]] | paper | 新增 ZKP application seed: SQL/operator-at-a-time query answer correctness and completeness with input/intermediate zero-knowledge | schema/cardinalities/query/DAG/answer public; not query privacy, transaction processing or full DBMS verification | `Abstract`, `§3-§5` |

## 当前综合

- Evidence window: `2026-06-20`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: 当前 ZKP applications 节点是 source-backed seed，重点记录“ZK 能力 -> 系统目标”的迁移，而不是 proof-system theory。zkCross 贡献 privacy/auditability 应用路线；zkBridge 贡献 succinct light-client verification 和 on-chain proof compression 应用路线；zkLogin 贡献 privacy-preserving credential authentication 和 keyless wallet onboarding 路线；Pianist 贡献 zkRollup/zkEVM prover scaling 应用路线，说明应用层瓶颈可能从 verifier/gas 转移到 proof generation throughput。ZKLP 贡献 privacy-preserving location proof 路线，说明应用正确性还可能依赖数值语义一致性和 location provenance。zkLLM 贡献 verifiable ML/LLM inference 路线，说明 ZK 可以用于 model-output authenticity，但证明边界必须限制在 committed-model inference relation 内。ZK-FEDB 与 ZKSQL 共同贡献 verifiable database query 路线，说明应用层的关键约束可能是 query completeness、database-size/input hiding 与 SQL operator semantics，而不只是证明每条返回记录满足谓词。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | 新增 ZKP applications 方向 seed；将 zero-knowledge 和 succinctness 映射到 cross-chain privacy/auditing | 定义与范围; 方法族与解决路线; 代表 Sources; 当前综合 | yes | 后续吸收 zkBridge、zkLogin、zkML sources 后扩展 |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | 新增 succinct light-client verification 应用路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合 | yes | 后续吸收 ZK bridge/rollup/zkVM sources 后扩展 |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | 新增 privacy-preserving credential authentication 应用路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合 | yes | 后续吸收 keyless wallet/credential sources 后扩展 |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | 新增 zkRollup prover scaling 应用路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 rollup prover repos/benchmarks 后复核 |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | 新增 privacy-preserving location proofs 应用路线 | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 location provenance/private proximity primary sources 后复核 |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | 新增 verifiable ML/LLM inference 应用路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 zkML prior systems/repositories 后复核 |

| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 verifiable federated aggregation 应用路线，并连接到 ML systems/federated learning integrity | 方法族与解决路线; 代表 Sources; Bridge Links | yes | 后续吸收 FL privacy/security sources 后复核是否拆更多 application child |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | 新增 verifiable database queries 问题节点，并把 ZKS/EDB primitive 迁移到应用查询完整性问题 | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 ZKSQL/private aggregate query sources 后复核 SQL/aggregate 分支 |
| [[doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation|ZKSQL]] | 扩展 verifiable database queries 到 SQL/operator-at-a-time proof route，并纠正队列误分的 distributed-transactions 路径 | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合 | no | 后续补 query privacy + verifiability hybrid sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-cross-chain-privacy-preserving-auditing|zk-SNARKs -> cross-chain privacy-preserving auditing]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, privacy, auditability, implementation_reuse | ZK succinctness/zero-knowledge transfers; cross-chain atomicity, SPV/HTLC semantics, denomination policy and audit-chain incentives are blockchain-specific. | active_seed |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, soundness, performance_compression | Proof soundness/succinctness transfers; bridge liveness, sender-chain finality, application state semantics and relayer incentives remain blockchain-specific. | active_seed |
| [[zk-snarks-to-privacy-preserving-blockchain-authentication|zk-SNARKs -> privacy-preserving blockchain authentication]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication` | application, privacy, authentication, implementation_reuse | ZK hiding/succinctness transfers; OP trust, salt recovery, JWK oracle, app liveness and UX recovery are system-specific. | active_seed |
| [[distributed-proof-generation-to-zkrollups|Distributed proof generation -> zkRollup prover scaling]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/applications/blockchain-applications` | application, scalability_enabler, implementation_reuse | Prover parallelization transfers; rollup security, data availability and sequencing do not. | active_seed |
| [[floating-point-snarks-to-privacy-preserving-location-proofs|Floating-point SNARKs -> privacy-preserving location proofs]] | `zero-knowledge-proofs/proof-systems/floating-point-snarks; zero-knowledge-proofs/applications/privacy-preserving-location-proofs` | application, method_transfer, numerical_soundness, dependency | IEEE 754 arithmetic transfers to geospatial proof accuracy; location provenance and application policy do not. | active_seed |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-inference` | application, verifiable_computation, privacy, implementation_reuse | ZK proof-system machinery transfers to inference auditing; training provenance, legality and safety do not. | active_seed |

| [[zk-snarks-to-zkml-verifiable-aggregation|zk-SNARKs -> zkML verifiable aggregation]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-aggregation` | application, verifiable_computation, integrity, implementation_reuse | Proof-system capability transfers to aggregation relation; FL system guarantees remain outside ZKP. | active_seed |
| [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]] | `zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases; zero-knowledge-proofs/applications/verifiable-database-queries` | dependency, method_transfer, application | ZKS set-operation proofs transfer to query-support completeness; SQL planning, transaction isolation and storage execution remain separate. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkp-applications | is_a | nahida-knowledge-zero-knowledge-proofs | vault/04_Knowledge/zero-knowledge-proofs/applications.md | medium | active_seed |
| nahida-knowledge-zkp-applications | has_child | nahida-knowledge-zkp-blockchain-applications | vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications.md | medium | active_seed |
| nahida-knowledge-zkp-applications | has_child | nahida-knowledge-privacy-preserving-location-proofs | vault/04_Knowledge/zero-knowledge-proofs/applications/privacy-preserving-location-proofs.md | high | active_seed |
| nahida-knowledge-zkp-applications | has_child | nahida-knowledge-verifiable-database-queries | vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md | vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md | vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md | high | active_seed |

| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md | source note | high | active_seed |
| nahida-knowledge-zkp-applications | evidenced_by | vault/03_Sources/papers/doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation.md | ZKSQL source note | high | active_seed |
| nahida-knowledge-zkp-applications | bridges_to | nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Query privacy + verifiability hybrid、authenticated SQL foundations、ZK rollup production/prover repo 等应用来源仍缺。 | ZK-FEDB 与 ZKSQL 已建立 verifiable database query seed，但 privacy/integrity hybrid 和生产路线仍需要稳定应用分类。 | nahida-update | high | queued |
| Location provenance/private proximity primary sources 缺。 | ZKLP 主协议不保证位置真实性，应用节点需要 provenance evidence。 | nahida-update / nahida-research-search | high | queued |
| Verifiable inference prior systems and repos 缺。 | 需要比较 zkLLM 与其他 zkML routes，避免应用节点被单源定义。 | nahida-update / nahida-github-repo-analyze | high | pending_queue |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkcross | Created ZKP applications direction from zkCross source absorption. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkbridge | Added succinct light-client verification application route. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zklogin | Added privacy-preserving credential authentication application route. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Added zkRollup prover scaling application route from Pianist. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zklp-floating-point-snarks | Added privacy-preserving location proof application route from ZKLP. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Added verifiable ML/LLM inference application route from zkLLM. | 1 source note | codex |

| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Added verifiable federated aggregation as a ZKP application route from zkFL. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zk-functional-elementary-databases | Added verifiable database queries as a ZKP application problem from ZK-FEDB. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zksql | Added SQL/operator-at-a-time verifiable database query evidence from ZKSQL. | doi:10.14778/3594512.3594513 | codex |
