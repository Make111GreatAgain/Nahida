---
id: "nahida-knowledge-zkp-blockchain-applications"
title: "ZKP blockchain applications"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "blockchain-applications"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
parent_knowledge_refs:
  - "nahida-knowledge-zkp-applications"
child_knowledge_refs:
  - "nahida-knowledge-privacy-preserving-blockchain-authentication"
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
  - "blockchain-applications"
primary_ontology_path: "zero-knowledge-proofs/applications/blockchain-applications"
secondary_ontology_paths:
  - "blockchain-systems/interoperability/cross-chain-protocols"
relation_edges:
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "is_a"
    to: "nahida-knowledge-zkp-applications"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "has_child"
    to: "nahida-knowledge-privacy-preserving-blockchain-authentication"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-cross-chain-privacy-preserving-auditing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-trustless-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-privacy-preserving-blockchain-authentication.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-proof-generation-to-zkrollups"
    evidence_refs:
      - "vault/05_Bridges/distributed-proof-generation-to-zkrollups.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkp-blockchain-applications"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
  - "nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges"
  - "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
  - "nahida-bridge-distributed-proof-generation-to-zkrollups"
source_note_refs:
  - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
representative_source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "doi:10.1109/TBDATA.2024.3403370"
query_keys:
  - "ZKP blockchain applications"
  - "blockchain applications of zero-knowledge proofs"
  - "zk-SNARK blockchain applications"
  - "cross-chain privacy-preserving auditing"
  - "ZK cross-chain bridge"
  - "succinct light-client verification"
  - "privacy-preserving blockchain authentication"
  - "zkLogin"
  - "zkRollup prover scaling"
  - "distributed ZKP rollup"
  - "blockchain-based federated learning verification"
  - "zkFL"
  - "federated learning integrity"
aliases:
  - "blockchain applications of ZKP"
  - "zk-SNARK blockchain applications"
  - "ZK cross-chain bridge"
  - "privacy-preserving blockchain authentication"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "blockchain-applications"
  - "cross-chain-privacy-preserving-auditing"
  - "trustless bridges"
  - "light-client verification"
  - "privacy-preserving-blockchain-authentication"
  - "zkrollup-prover-scaling"
  - "blockchain-based-verification"
  - "federated-learning-integrity"
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
  - "nahida-knowledge-20260620-zkcross"
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260620-zklogin"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "doi:10.1109/TBDATA.2024.3403370"
confidence: "medium"
trust_tier: "primary"
---

# ZKP blockchain applications

## 定义与范围

- 定义: ZKP blockchain applications 研究 zero-knowledge proofs 如何用于区块链隐私、跨链互操作、审计、身份、扩容和链上可验证执行。
- 不包含: 单篇应用论文、单个协议名、某个电路或合约的源内细节；这些留在 `03_Sources` source note。
- Canonical terms: `blockchain applications of ZKP`
- Aliases/query keys: zk-SNARK blockchain applications, cross-chain privacy-preserving auditing
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 ZKP 在 blockchain systems 中解决哪些问题，再按需打开 cross-chain protocols 或 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

zkCross、zkBridge、zkLogin 和 Pianist 是当前 seeds。zkCross 展示 ZKP 在 blockchain 中的两类应用能力: zero-knowledge 隐藏 cross-chain interaction linkability，succinctness 压缩 audit verification。zkBridge 展示另一类应用能力: 用 succinct proof 把 sender-chain light-client verification 从 receiver-chain smart contract 中移出，降低 gas/storage 成本并避免 committee correctness trust。zkLogin 展示第三类应用能力: 用 ZK 隐藏身份凭证/JWT witness，同时让链验证 credential、地址和 ephemeral key 的关系。Pianist 展示第四类应用能力: zkRollup/zkEVM 的 verifier 端已被 ZKP 压缩后，prover-side proof generation 会成为扩容瓶颈，需要 distributed proof generation 支撑更大 batch。它们都不是 zk-SNARK foundation source，而是 blockchain application sources。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它可组织 zkBridge、zkLogin、zkML、private payments、auditable storage 等 blockchain/ZKP 应用。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkCross 和它的三协议 Θ/Φ/Ψ 只作为 source extension。
- 需要引用的更基础 Knowledge: [[applications|ZKP applications]], [[zk-snarks|zk-SNARKs]], [[cross-chain-protocols|Cross-chain protocols]]。
- 不应拆出的实例/协议/来源: zkCross、zkBridge、zkLogin、zkLLM 等默认 source/system instances。

## 解决的问题

把 ZK proof-system 能力映射到区块链系统目标，并明确 proof generation、verification gas、privacy leakage、state access 和 chain interoperability 的边界。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[applications|ZKP applications]] | child_of | zkCross source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| cross-chain privacy-preserving auditing | section | 当前只有 zkCross 一个 source；先作为本节点应用路线，不单独拆 node。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] | source_extension |
| succinct light-client verification | section | 当前只有 zkBridge 一个 source；先作为本节点应用路线，不单独拆 node。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] | source_extension |
| [[privacy-preserving-blockchain-authentication|privacy-preserving blockchain authentication]] | child | zkLogin 让 blockchain authentication/keyless wallet onboarding 成为独立应用问题，且有完整 source 支撑。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | active_seed |
| zkRollup prover scaling | section / bridge | 当前 Pianist 给出强 source，但仍缺 production rollup prover/repo 多来源；先作为本节点应用路线和 bridge，不单独拆 child。 | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Privacy-preserving cross-chain transfer | 用 zk-SNARK 隐藏 receiver address，fixed denomination 降低 amount linkability，同时用 SPV/Merkle proof 保持 mint/redeem correctness。 | transfer 需要 unlinkability 且不引入 trusted third party。 | denomination 增加交易数量；匿名集合为隐私硬边界。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| Privacy-preserving cross-chain exchange | 用 independent preimages 和 ZK proof 消除 HTLC same-preimage linkability，同时保持 atomicity。 | exchange 需要双方跨链锁定/解锁资产。 | 多轮交互和 proof/gas 成本较 transfer 更高。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| Succinct cross-chain auditing | 把审计函数、签名验证、状态转移和 root verification 压缩进 proof，audit chain 验证 proof 而非逐交易读取。 | auditors 不能或不应访问完整交易内容，且 full auditing 成本过高。 | Proving 成本转移给 committer；需要可靠 state roots 和至少一个 honest committer。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| Succinct light-client verification | 用 ZK proof 证明 sender-chain block-header/light-client transition，让 receiver-chain updater contract 只验证短 proof。 | receiver chain 直接验证 sender-chain consensus/signatures 成本过高，且不想引入 bridge committee correctness trust。 | Proving 成本、递归压缩、curve/precompile 支持、finality/orphan handling 和 relayer liveness 仍需系统设计。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Recursive proof compression for on-chain verification | 先用并行/透明 proof system 证明大电路，再用 Groth16 等链上友好 SNARK 压缩 verification circuit。 | 大 proof 直接链上验证不可行，但 receiver chain 可便宜验证 Groth16 类 proof。 | 增加递归 proving time；只在目标链支持低成本 verifier 时收益明显。 | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]] |
| Privacy-preserving blockchain authentication | 用 JWT/OpenID credential 作为 hidden witness，证明 identity credential、salted address 和 nonce-bound ephemeral key 一致，链上只验证 proof 和临时签名。 | 钱包 onboarding 需要复用现有身份凭证，但不想公开身份信息或让新中介获得 custody/signing power。 | 仍信任 OP authentication；salt/JWK/ZK service/app liveness 是系统边界。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |
| zkRollup prover scaling via distributed proving | 把 rollup/zkEVM proof generation 分到多台机器，目标是在更大 batch 下保持 proof/verifier 成本常数或小幅增加。 | verifier/gas 已可接受，但 prover time/memory 成为 throughput 瓶颈。 | 不解决 DA、sequencer ordering、state correctness、prover market incentive 或生产 fault recovery；具体适用性取决于电路和 proof system。 | [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]] |

| Blockchain-based federated aggregation verification | Miners verify ZK proof for an off-chain aggregate and store `H(Enc(w))` on chain, so later clients can check round state without on-chain aggregation. | FL participants need public verification/audit trail but model aggregation is too large for chain execution. | Finality delay, gas, off-chain data availability and proof generation remain bottlenecks. | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | paper | 增加 blockchain/ZKP application seed：cross-chain privacy-preserving transfer/exchange/audit | 单一 source；modified geth/Solidity; Groth16 gas setup; anonymity-set limitation | `p1-p17` |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 增加 blockchain/ZKP application seed：trustless bridge, light-client verification compression, recursive on-chain proof | 单一 source；性能数字依赖 2022 Cosmos/Ethereum 原型和实验环境 | `p1-p15` |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | paper | 增加 blockchain/ZKP application seed：privacy-preserving authentication, keyless wallet onboarding, JWT witness, salted address | 单一 source；依赖 OP/JWK/salt management/Groth16 ceremony；生产数字不泛化 | `p1-p20` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 增加 blockchain/ZKP application seed：zkRollup/zkEVM prover scaling through fully distributed ZKPs | 单一 source；R1CS-to-Plonk conversion、BN254/Gnark 环境、witness distribution 和经济模型不泛化 | `p1-p15` |

| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 增加 blockchain/ZKP application seed: proof verification and hash anchoring for FL aggregation, without on-chain aggregation | 单一 source；finality/gas数字是论文设置；不解决 off-chain DA 或 aggregator privacy | `p1-p14` |

## 当前综合

- Evidence window: `2026-06-20`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: ZKP blockchain applications 当前有四个 seeds。zkCross 的可复用结构是: zero-knowledge 隐藏 linkability sources，succinct verification 用于审计压缩。zkBridge 的可复用结构是: succinct proof 把 light-client verification 从链上直接执行变为短 proof verification。zkLogin 的可复用结构是: ZK proof 把身份凭证作为 hidden witness，用 salt/nonce/ephemeral key 把 Web identity 与链上交易认证连接起来。Pianist 的可复用结构是: 当 rollup/zkEVM 的 verifier 端已经被 proof 压缩后，proof generation 本身需要分布式化以支持更大交易 batch。跨链语义、finality、OP trust、salt recovery、JWK freshness、app liveness、DA、sequencing 和 prover economics 等仍属于系统层。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | 新增 cross-chain privacy-preserving auditing 应用路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 zkBridge/zkLogin/zkML sources 后扩展应用分类 |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | 新增 trustless bridge 和 succinct light-client verification 应用路线 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 IBC/optimistic bridge/production bridge sources 后复核 |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | 新增 privacy-preserving blockchain authentication child node and wallet onboarding route | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 ZK Address Abstraction/Aptos Keyless/OpenPubkey/CanDID 后复核 |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | 新增 zkRollup/zkEVM prover scaling 路线，并桥接到 [[distributed-proof-generation|Distributed proof generation]] | 背景; 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 production rollup prover repos/benchmarks 后复核是否拆 child |

| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 blockchain-based federated aggregation verification 路线；强调链上只验证 proof/hash，不执行 aggregation | 方法族与解决路线; 代表 Sources; 当前综合 | yes | 后续吸收 blockchain FL / secure aggregation sources 后决定是否拆 child |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-cross-chain-privacy-preserving-auditing|zk-SNARKs -> cross-chain privacy-preserving auditing]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, privacy, auditability, implementation_reuse | ZK succinctness/zero-knowledge transfers; cross-chain atomicity, SPV/HTLC semantics, denomination policy and audit-chain incentives are blockchain-specific. | active_seed |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, soundness, performance_compression | Proof soundness/succinctness transfers; bridge liveness, sender-chain finality, application state semantics and relayer incentives remain blockchain-specific. | active_seed |
| [[zk-snarks-to-privacy-preserving-blockchain-authentication|zk-SNARKs -> privacy-preserving blockchain authentication]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication` | application, privacy, authentication, implementation_reuse | ZK hiding/succinctness transfers; OP trust, salt recovery, JWK oracle, app liveness and UX recovery are system-specific. | active_seed |
| [[distributed-proof-generation-to-zkrollups|Distributed proof generation -> zkRollup prover scaling]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/applications/blockchain-applications` | application, scalability_enabler, implementation_reuse | Prover parallelization transfers; rollup security, DA, sequencing, finality and economics remain system-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkp-blockchain-applications | is_a | nahida-knowledge-zkp-applications | vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications.md | medium | active_seed |
| nahida-knowledge-zkp-blockchain-applications | has_child | nahida-knowledge-privacy-preserving-blockchain-authentication | vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | evidenced_by | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | evidenced_by | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | evidenced_by | vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md | vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | bridges_to | nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing | vault/05_Bridges/zk-snarks-to-cross-chain-privacy-preserving-auditing.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | bridges_to | nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges | vault/05_Bridges/zk-snarks-to-trustless-cross-chain-bridges.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | bridges_to | nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication | vault/05_Bridges/zk-snarks-to-privacy-preserving-blockchain-authentication.md | high | active_seed |
| nahida-knowledge-zkp-blockchain-applications | bridges_to | nahida-bridge-distributed-proof-generation-to-zkrollups | vault/05_Bridges/distributed-proof-generation-to-zkrollups.md | high | active_seed |

| nahida-knowledge-zkp-blockchain-applications | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| ZK rollup production prover repos/benchmarks、private payments、zkML blockchain applications 缺 source。 | 需要更多来源才能把应用分类从跨链/认证/prover-scaling seeds 提升为 durable taxonomy。 | nahida-update | high | queued |
| ZK Address Abstraction、Aptos Keyless、OpenPubkey、CanDID 缺 source。 | 需要比较 keyless wallet / Web2 credential authentication 的 security/privacy/liveness 边界。 | nahida-update / nahida-research-search | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkcross | Created ZKP blockchain applications problem node and added zkCross source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkbridge | Added succinct light-client verification and trustless bridge application route. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zklogin | Added privacy-preserving blockchain authentication child node and zkLogin source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Added zkRollup prover scaling route and bridge to distributed proof generation. | 1 source note | codex |

| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Added blockchain-based FL aggregation verification source extension from zkFL. | 1 source note | codex |
