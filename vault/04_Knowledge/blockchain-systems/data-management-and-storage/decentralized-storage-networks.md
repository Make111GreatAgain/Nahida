---
id: "nahida-knowledge-decentralized-storage-networks"
title: "Decentralized Storage Networks"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "decentralized-storage-networks"
domain_id: "blockchain-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "decentralized-storage-networks"
  - "storage-service-incentives"
  - "proof-of-storage"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-data-management-and-storage"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "data-management-and-storage"
  - "decentralized-storage-networks"
primary_ontology_path: "blockchain-systems/data-management-and-storage/decentralized-storage-networks"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments"
  - "verifiable-computation/verifiable-computation-systems"
  - "distributed-systems/data-management-and-storage/content-addressed-storage"
relation_edges:
  - from: "nahida-knowledge-decentralized-storage-networks"
    relation: "part_of"
    to: "nahida-knowledge-blockchain-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-decentralized-storage-networks"
    relation: "depends_on"
    to: "nahida-knowledge-contingent-service-payments"
    evidence_refs:
      - "vault/05_Bridges/decentralized-storage-networks-to-contingent-service-payments.md"
      - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-decentralized-storage-networks"
    relation: "depends_on"
    to: "nahida-knowledge-verifiable-computation-systems"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-decentralized-storage-networks"
    relation: "depends_on"
    to: "nahida-knowledge-content-addressed-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage/content-addressed-storage.md"
      - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-decentralized-storage-networks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-decentralized-storage-networks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-decentralized-storage-networks-to-contingent-service-payments"
  - "nahida-bridge-content-addressed-storage-to-decentralized-storage-networks"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
  - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
representative_source_refs:
  - "arxiv:2208.09937"
  - "isbn:978-7-111-62880-4"
query_keys:
  - "decentralized storage network"
  - "DSN"
  - "Filecoin Sia Storj Swarm"
  - "proof of storage"
  - "proof of spacetime"
  - "proof of retrievability"
  - "storage service incentive"
  - "Filecoin IPFS relation"
  - "IPFS incentive layer"
  - "PoRep PoSt Filecoin"
  - "storage provider service denial attack"
  - "challenge based storage verification"
  - "去中心化存储网络"
  - "存储证明"
  - "存储服务激励"
aliases:
  - "去中心化存储网络"
  - "DSN"
  - "Decentralized storage market"
  - "Storage service incentive layer"
domains:
  - "blockchain-systems"
  - "verifiable-computation"
topics:
  - "decentralized storage"
  - "storage service incentives"
  - "proof of storage"
  - "proof of retrievability"
  - "oracle-assisted verification"
  - "Filecoin"
  - "content-addressed storage"
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
  - "nahida-knowledge-20260623-incentive-compatible-decentralized-storage"
  - "nahida-knowledge-20260623-ipfs-principles-and-practice"
source_refs:
  - "arxiv:2208.09937"
  - "isbn:978-7-111-62880-4"
confidence: "medium"
trust_tier: "primary"
---

# Decentralized Storage Networks

## 定义与范围

- 定义: Decentralized Storage Networks (DSN) 是用区块链账本、代币/合约激励和可验证存储证明组织存储市场的系统问题，目标是让客户端可外包数据，storage providers 可出售存储和检索服务，而不依赖单一中心化云厂商。
- 不包含: 普通区块链全节点 state storage、链上数据库索引、data availability sampling、跨链消息或共识安全；这些分别属于相邻 knowledge 节点。
- Canonical terms: `decentralized storage network`, `proof of storage`, `proof of spacetime`, `proof of retrievability`, `storage contract`, `storage service incentive`。
- Standalone completeness check: 本节点解释 DSN 的问题边界、存储证明/激励/服务可用性路线和当前 source delta；Filecoin/Sia/Storj/Swarm 细节仍需要未来 source 补全。
- Retrieval role: 查询“Filecoin/Sia/Storj/Swarm 属于哪类问题”“存储服务如何激励 provider 诚实保存/返回数据”“PoS/PoR 和链上付款怎么连接”时，先进入本节点。
- Update scope: Filecoin、Sia、Storj、Swarm、proof of storage、proof of replication/spacetime、proof of retrievability、storage-provider reputation、storage-market pricing、challenge-based audit、storage service availability。

## 背景

source_backed_background: `An Incentive-Compatible Mechanism for Decentralized Storage Network` 把 DSN 的主问题从“区块链能否达成共识”转到“存储市场中的服务、证明和付款如何组合”。论文指出，DSN 让微型 storage providers 进入存储市场，并用 blockchain/smart contract 组织付款、抵押和审计；但现有持续 PoS/PoSt 检查会消耗网络资源，而且 provider 可能向网络提交有效证明却拒绝向客户端提供数据。[[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] 进一步补充 Filecoin/IPFS 边界: IPFS 主要解决内容寻址、数据定位和分发，Filecoin 则作为区块链存储市场/激励层处理长期存储、检索、PoRep/PoSt 和矿工收益。

model_prior_background: DSN 与普通 IPFS/content-addressed storage 的差别在于激励和服务合同。CID 或哈希能绑定内容，PoS/PoR 能证明某种保存/可取回性，但客户端真正关心的是数据在需要时能被取回，并且失败时能被补偿。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / application area under blockchain data-management-and-storage。
- 为什么足够通用: Filecoin、Sia、Storj、Swarm、Proof of Storage、PoR、storage markets 和 service availability 会持续收集多个 source，不是 ICM-DSN 这篇论文的局部命名。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `ICM-DSN` 是本文机制实例；`decentralized-storage-networks` 是可容纳 Filecoin/Sia/Storj/Swarm、proof schemes、pricing、retrieval availability 和 dispute routes 的上层问题节点。
- 需要引用的更基础 Knowledge: [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]]、[[04_Knowledge/distributed-systems/data-management-and-storage/content-addressed-storage|Content-addressed Storage and Distribution]]、[[verifiable-computation-systems|Verifiable computation systems]]。
- 不应拆出的实例/来源: ICM-DSN、Chainlink/Kovan prototype、具体 Merkle proof 参数和 payoff example 留在 source note。

## 解决的问题

- 如何让客户端把数据外包给陌生 storage provider，同时保留完整性、可用性和补偿路径。
- 如何证明 provider 确实保存数据，且证明成本不会吞掉存储服务收益。
- 如何避免 provider 只向网络/审计方证明保存，却拒绝实际向客户端返回数据。
- 如何用 smart contract/collateral/premium 处理付款、罚没、退款和争议。
- 如何在读取请求次数影响价格时，避免 provider 或 client 操纵 request counting。
- 如何在内容寻址、PoS/PoR、存储市场和区块链结算之间划清责任边界。
- 如何区分 IPFS/CID/BitSwap 这类内容寻址分发机制与 Filecoin/DSN 这类经济激励、存储证明和检索市场机制。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]] | child_of | DSN 是 blockchain storage/data-management 中面向外包数据和存储市场的一支。 | active_seed |
| [[04_Knowledge/blockchain-systems|Blockchain systems]] | domain | 使用 blockchain/smart contract 作为结算和激励层。 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Storage service incentives | method/problem candidate | 多 source 后可能形成独立问题: premium、collateral、penalty、challenge cost、request pricing。 | ICM-DSN p4-p8 | keep_section |
| Proof of Storage / Proof of Spacetime | foundation candidate | Filecoin/DSN 频繁使用，但 vault 还缺 PoS/PoSt canonical source。 | ICM-DSN related work only | review |
| Proofs of Retrievability | foundation candidate | PoR 与 PoS 边界影响 service-payment 和 storage availability，但当前只来自 RC-S-P 与 ICM-DSN 背景。 | ICM-DSN §2.2; RC-S-P | review |
| Storage service availability | problem candidate | provider 保存数据不等于按需服务客户端，是 DSN/FDE/RC-PoR-P 的共同问题。 | ICM-DSN service denying attack | watching |
| Decentralized storage implementation landscape | application cluster | Filecoin/Sia/Storj/Swarm、IPFS/Arweave、真实运维和经济模型需要 source-backed 对照。 | ICM-DSN §2.1 | queued |
| IPFS/Filecoin boundary | boundary section | Filecoin 常被误解为 IPFS 本身；需要保留“内容寻址 substrate vs 存储市场激励层”的边界。 | IPFS原理与实践 Chapter 5 | keep_section |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Continuous proof auditing | Provider 周期性向网络提交 PoS/PoSt/PDP 证明，证明仍保存数据。 | 网络愿意支付持续审计成本；证明可廉价验证。 | 成本持续发生；不能自动保证客户端实际拿到服务。 | [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] related work |
| Challenge-based storage verification | 只有客户端发起挑战时才通过 smart contract/oracle 检查 storage proof。 | 大多数时间服务正常，争议较少；挑战成本可设计。 | 依赖 rational-player payoff、oracle boundary 和挑战参数。 | [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] |
| Oracle-assisted off-chain verification | 链上合约保存 root/collateral，oracle 在链下向 provider 取 segment 和 Merkle path，再把结果回写合约。 | 链上计算/storage 昂贵，且证明验证可外包。 | oracle 信任和可用性成为边界；不等于纯链上验证。 | ICM-DSN |
| Merkle-tree proof of storage | 链上只存 Merkle root；挑战时 provider 返回 segment 与 Merkle path。 | 需要低参数、无 trusted setup、简单验证。 | 保证弱于完整 PoR；对大文件挑战粒度和概率覆盖需设计。 | ICM-DSN |
| Request-counter pricing | 客户端请求中签名递增 counter，provider cash-out 时提交最后请求。 | 读取次数影响服务价格。 | 仍需挑战机制防 provider 收到请求后不服务。 | ICM-DSN |
| Contingent service payment | 用服务证明、押金和争议归责把“可验证服务”与付款绑定。 | PoR/VC/searchable encryption/信息检索等服务可验证。 | 需要处理恶意客户端、proof-status privacy 和争议成本。 | [[contingent-service-payments|Contingent service payments for verifiable services]] |
| Filecoin-style storage/retrieval markets | 用存储矿工/检索矿工、订单、抵押、PoRep/PoSt 和 DSN Put/Get/Manage 组织长期存储与检索服务 | IPFS/P2P 内容分发需要经济激励或服务合同来获得更强可用性 | 本书是 2019 年 source；当前 Filecoin spec/参数需未来补直接来源 | [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|An Incentive-Compatible Mechanism for Decentralized Storage Network]] | paper | 创建本节点；把 DSN 中的持续 PoS 成本、service-denial attack、challenge-based verification、smart-contract/oracle storage contract 和 request counting 组织为存储服务激励问题。 | 单篇 source seed；Filecoin/Sia/Storj/Swarm 和 PoS/PoR foundation 仍需补直接来源；oracle trust boundary 未深入。 | p1-p13 |
| [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] | book / local PDF | 补入 Filecoin/IPFS 关系、Filecoin 存储/检索市场、DSN Put/Get/Manage、PoRep/PoSt 和攻击边界，强化 DSN 与内容寻址 substrate 的区别。 | 2019 年书籍，Filecoin 章节基于早期材料；不能替代当前规范。 | Chapter 5 |

## 当前综合

- Evidence window: `2026-06-23`。
- Freshness: `fresh` for current-vault source evidence, not a latest-news claim。
- Valid until: `2026-07-23`。
- 综合: DSN 是 blockchain data-management/storage 下的外包存储市场问题。它和 [[off-chain-application-data-management|Off-chain Application Data Management]] 都处理链下数据，但后者关心应用大对象/CID/权限工作流，DSN 关心陌生 provider 的长期存储服务、证明、检索可用性和经济激励。ICM-DSN 的可复用贡献是把“证明一直保存”与“客户端实际取回服务”区分开，并用 challenge + oracle + smart contract 把持续审计改成争议触发审计。IPFS 书籍补充了上游边界: [[content-addressed-storage|Content-addressed Storage and Distribution]] 提供对象身份、路由和分发，Filecoin/DSN 才负责存储市场、矿工激励和 PoRep/PoSt 证明。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] | 新建 DSN 问题节点，纠正队列中的 consensus 误分类；补入 challenge-based storage verification、Merkle PoS、oracle-assisted verification 和 request counting。 | 定义、解决的问题、方法族、代表 Sources、Bridge Links | yes | 后续吸收 Filecoin/Sia/Storj/Swarm、PoS/PoR direct sources 后拆 foundation child |
| [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] | 补入 Filecoin/IPFS 边界、DSN 操作、存储/检索市场和 PoRep/PoSt seed evidence。 | 背景、解决的问题、方法族、代表 Sources、Bridge Links、缺口 | no | 后续补 Filecoin specs/direct proof sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[decentralized-storage-networks-to-contingent-service-payments|Decentralized storage networks -> contingent service payments]] | `blockchain-systems/data-management-and-storage/decentralized-storage-networks` -> `blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | application, shared_pattern, tension | storage proof/service availability can feed payment disputes; fair-exchange payment machinery does not by itself guarantee DSN storage or oracle availability. | active_seed |
| [[content-addressed-storage-to-decentralized-storage-networks|Content-addressed storage -> decentralized storage networks]] | `distributed-systems/data-management-and-storage/content-addressed-storage` -> `blockchain-systems/data-management-and-storage/decentralized-storage-networks` | substrate_to_incentive_layer, boundary | CID/Merkle/P2P substrate can support DSN objects and commitments; storage incentives, proof semantics, payments and availability do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-decentralized-storage-networks | part_of | nahida-knowledge-blockchain-data-management-and-storage | ICM-DSN source note | high | active_seed |
| nahida-knowledge-decentralized-storage-networks | depends_on | nahida-knowledge-contingent-service-payments | DSN service payment bridge; RC-S-P adjacency | medium | active_seed |
| nahida-knowledge-decentralized-storage-networks | depends_on | nahida-knowledge-verifiable-computation-systems | PoS/PoR are verifiable service proofs in the broader sense | medium | active_seed |
| nahida-knowledge-decentralized-storage-networks | depends_on | nahida-knowledge-content-addressed-storage | IPFS/Filecoin boundary and bridge | high | active_seed |
| nahida-knowledge-decentralized-storage-networks | evidenced_by | vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md | source note | high | active_seed |
| nahida-knowledge-decentralized-storage-networks | evidenced_by | vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md | source note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Filecoin/Sia/Storj/Swarm 直接 sources 缺。 | 当前 landscape 来自 ICM-DSN related work，不能替代各系统白皮书/规范。 | `nahida-update` / `nahida-research-search` | high | queued |
| PoS/PoSt/PoRep/PoR foundation 缺。 | DSN 证明语义决定安全边界和付款争议，但目前只有二手背景。 | future paper intake / foundation search | high | queued |
| Filecoin 当前规范缺。 | IPFS 书籍提供 2019 年 Filecoin seed evidence，但不能代表主网后的当前协议细节。 | `nahida-research-search` / future source intake | high | queued |
| Oracle trust model 未展开。 | ICM-DSN 用 Chainlink 把验证和转发搬到链下；oracle 的可用性、诚实性和成本需要单独来源。 | `nahida-research-search` | medium | queued |
| Non-rational adversary / DoS model 薄。 | Game-theoretic mechanism 不覆盖所有非理性破坏、密钥泄露或 collusion。 | future source | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-incentive-compatible-decentralized-storage | Created DSN problem node and attached ICM-DSN as first source extension. | arxiv:2208.09937 | codex |
| 2026-06-23 | nahida-knowledge-20260623-ipfs-principles-and-practice | Added IPFS/Filecoin boundary and linked DSN to content-addressed storage. | isbn:978-7-111-62880-4 | codex |
