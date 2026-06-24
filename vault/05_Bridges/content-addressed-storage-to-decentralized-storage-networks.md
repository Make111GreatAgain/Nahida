---
id: "nahida-bridge-content-addressed-storage-to-decentralized-storage-networks"
title: "Content-addressed storage -> decentralized storage networks"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "content-addressed-storage"
  - "decentralized-storage-networks"
  - "ipfs"
  - "filecoin"
endpoint_knowledge_refs:
  - "nahida-knowledge-content-addressed-storage"
  - "nahida-knowledge-decentralized-storage-networks"
endpoint_paths:
  - "distributed-systems/data-management-and-storage/content-addressed-storage"
  - "blockchain-systems/data-management-and-storage/decentralized-storage-networks"
relation_types:
  - "substrate_to_incentive_layer"
  - "dependency"
  - "boundary"
  - "implementation_context"
directionality: "one_way_with_feedback"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/sha256-1e0dbba290b2-ipfs-principles-and-practice.md"
  - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
representative_source_refs:
  - "isbn:978-7-111-62880-4"
  - "arxiv:2208.09937"
query_keys:
  - "IPFS Filecoin boundary"
  - "content addressing decentralized storage networks"
  - "CID proof of storage"
  - "IPFS DSN"
  - "Filecoin IPFS relation"
  - "内容寻址 去中心化存储网络"
aliases:
  - "IPFS to Filecoin boundary"
  - "Content addressing to storage market incentives"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "content-addressed-storage"
  - "decentralized-storage-networks"
  - "proof-of-storage"
  - "storage markets"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-ipfs-principles-and-practice"
source_refs:
  - "isbn:978-7-111-62880-4"
  - "sha256:1e0dbba290b2b4ccd70e8c42f78fc2531b9bf6539b7afe55c699cca43d1fa1e5"
  - "arxiv:2208.09937"
confidence: "high"
trust_tier: "primary"
---

# Content-addressed storage -> decentralized storage networks

## 关系命题

Content-addressed storage provides the object identity, integrity, routing and block-distribution substrate that decentralized storage networks can build on. Decentralized storage networks add a separate layer: provider incentives, storage/retrieval markets, proof of storage or proof of spacetime, deposits, payments and service-dispute logic.

这条 bridge 的核心不是“IPFS 等于 Filecoin”，而是“IPFS-style content addressing 可以成为 DSN 的数据定位/分发底座；Filecoin/DSN 解决的是 IPFS 自身不自动解决的长期存储、检索服务和经济激励问题”。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[content-addressed-storage|Content-addressed Storage and Distribution]] | `distributed-systems/data-management-and-storage/content-addressed-storage` | CID/content addressing, DHT provider routing, BitSwap, Merkle DAG/IPLD, IPNS, pinning and gateways | P2P content identity and distribution substrate |
| [[decentralized-storage-networks|Decentralized Storage Networks]] | `blockchain-systems/data-management-and-storage/decentralized-storage-networks` | storage markets, provider incentives, proof of storage/retrievability, retrieval service availability, smart-contract payment/dispute routes | blockchain-based outsourced storage market problem |

## Transfer Matrix

| From content-addressed storage | Transfers to DSN? | How | Boundary |
| --- | --- | --- | --- |
| CID / content hash | yes | Binds a storage/retrieval contract to a specific object or Merkle root. | CID proves object identity/integrity, not that provider still stores it. |
| Merkle DAG / Merkle proof vocabulary | yes | Supports chunked files, root commitments, path proofs and challenge sampling. | PoRep/PoSt/PoR security needs additional protocol and adversary assumptions. |
| DHT/provider discovery | partially | Helps locate nodes that advertise content. | Provider advertisement is not an enforceable service contract. |
| BitSwap/block exchange | partially | Moves data blocks and offers local credit/debt exchange behavior. | Local block-exchange credit is weaker than tokenized long-term storage incentives. |
| Pinning / private networks | yes as implementation context | Explains operational availability tools used before or alongside DSN markets. | Pinning is an operator policy; it has no native economic penalty unless wrapped by DSN. |

| From DSN | Transfers back to content-addressed storage? | How | Boundary |
| --- | --- | --- | --- |
| Storage market incentives | maybe | Can pay providers to keep content-addressed objects available. | Economic layer changes availability assumptions, not CID semantics. |
| PoRep/PoSt/PoR | yes as availability assurance | Turns possession/replication/spacetime into challengeable evidence. | Does not replace P2P routing/exchange; proof validity and data delivery can diverge. |
| Retrieval market | yes as service layer | Pays nodes for returning data. | Real-time retrieval may need off-chain channels and dispute paths; not solved by content address alone. |
| Smart-contract settlement | no direct transfer | Settles payments/collateral. | Does not define how objects are chunked, named or routed. |

## Non-Transfer Boundary

- CID/hash integrity does not imply availability. A client can know exactly what object it wants while no reachable provider has it.
- DHT/provider discovery is not service accountability. A provider can advertise, disappear, throttle, or refuse service unless a separate mechanism penalizes it.
- BitSwap credit is not Filecoin economics. BitSwap discourages local free-riding during block exchange, while Filecoin/DSN prices storage/retrieval services and proves persistence over time.
- PoRep/PoSt/PoR does not replace content addressing. Proofs can show possession/replication/spacetime for committed data, but object addressing and retrieval still need identifiers, layout and delivery routes.
- Blockchain storage markets do not automatically make public IPFS content private or access-controlled. Encryption, key management and private network policies remain separate.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] Chapter 1-4 | IPFS content-addressing, DHT, BitSwap, Merkle DAG, IPLD/CID and IPNS stack. | 2019 book; current implementation details need future update. |
| [[sha256-1e0dbba290b2-ipfs-principles-and-practice|IPFS原理与实践]] Chapter 5 | Filecoin/IPFS distinction, DSN, storage/retrieval markets, PoRep/PoSt and incentive layer framing. | Based on early Filecoin material; not current spec. |
| [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] | DSN as storage service incentives, proof/challenge/payment problem rather than content-addressing alone. | Does not build full IPFS substrate; uses Merkle proof/service contract route. |
| [[off-chain-application-data-management|Off-chain Application Data Management]] | Shows blockchain applications can store CIDs on-chain while large objects live off-chain. | Application workflow, not DSN proof/economic layer. |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[content-addressed-storage|Content-addressed Storage and Distribution]] | Created as distributed-systems data-management child and attached this bridge. | done |
| [[decentralized-storage-networks|Decentralized Storage Networks]] | Add IPFS/Filecoin distinction and link this bridge. | done |
| [[off-chain-application-data-management|Off-chain Application Data Management]] | Add content-addressed storage as foundation dependency for CID/private IPFS/pinning. | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| CID/Merkle root as object commitment | `content-addressed-storage` | `decentralized-storage-networks` | substrate | IPFS book Ch. 2-4; Filecoin/DSN Ch. 5 | 把完整性误当作可用性 |
| provider routing vocabulary | `content-addressed-storage` | `decentralized-storage-networks` | implementation_context | IPFS book Ch. 3 | provider discovery 不等于 provider liability |
| proof challenge over chunks | `decentralized-storage-networks` | `content-addressed-storage` | assurance overlay | IPFS book Ch. 5; ICM-DSN | PoRep/PoSt/PoR 与 Merkle chunk proof 语义不同 |
| pinning/replication policy | `content-addressed-storage` | `off-chain application data management` / DSN | operations | IPFS book Ch. 6-7; construction IPFS source | pinning 是运维策略，非自动市场机制 |

## 查询入口

- IPFS 和 Filecoin 的边界是什么?
- CID 能证明什么，不能证明什么?
- 内容寻址为什么还需要 pinning、Filecoin 或其他激励层?
- DHT/BitSwap 与 PoRep/PoSt 的层级关系是什么?
- 链上记录 CID 的应用什么时候只是 off-chain data management，什么时候进入 DSN?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-ipfs-principles-and-practice | Created bridge while absorbing IPFS book and linking content-addressed storage with DSN. | isbn:978-7-111-62880-4; arxiv:2208.09937 | codex |
