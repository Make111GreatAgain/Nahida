---
id: "doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency"
title: "A secure dynamic cross-chain decentralized data consistency verification model"
type: "source"
source_type: "paper"
source_kind: "pdf"
source_subtype: "paper_local"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
safe_for_absorption: true
trust_tier: "primary"
source_identity:
  type: "doi"
  key: "doi:10.1016/j.jksuci.2023.101897"
source_refs:
  - "doi:10.1016/j.jksuci.2023.101897"
  - "sha256:96bb38c339a1823e1edb0594d65a7b9c2fa1113e028cfa8be4c595427c3c7789"
  - "filename:1-s2.0-S1319157823004512-main.pdf"
representative_source_refs:
  - "doi:10.1016/j.jksuci.2023.101897"
authors:
  - "Jiahao Zhao"
  - "Yushu Zhang"
  - "Jiajia Jiang"
  - "Zhongyun Hua"
  - "Yong Xiang"
venue: "Journal of King Saud University - Computer and Information Sciences 36 (2024) 101897"
year: "2024"
doi: "10.1016/j.jksuci.2023.101897"
arxiv_id: ""
canonical_url: "https://doi.org/10.1016/j.jksuci.2023.101897"
local_pdf: "~/Desktop/paper/1-s2.0-S1319157823004512-main.pdf"
pdf_sha256: "96bb38c339a1823e1edb0594d65a7b9c2fa1113e028cfa8be4c595427c3c7789"
extracted_text_path: "vault/02_Raw/pdf/extracted/a-secure-dynamic-cross-chain-decentralized-data-consistency-verification-model-96bb38c339a1-pages.txt"
pages: 13
domain_id: "blockchain-systems"
direction_id: "interoperability"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols"
secondary_ontology_paths:
  - "blockchain-systems/data-availability-and-light-clients"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain-protocols"
  - "dynamic cross-chain data consistency verification"
  - "audit chain"
  - "dynamic data"
  - "decentralized chameleon hash"
  - "collaborative smart-contract deployment"
  - "CoSi"
  - "multi-signcryption"
topic_ids:
  - "cross-chain-protocols"
  - "dynamic-data-consistency-verification"
query_keys:
  - "DCCV"
  - "dynamic cross-chain data consistency verification"
  - "cross-chain dynamic data consistency"
  - "audit chain dynamic data"
  - "decentralized chameleon hash blockchain"
  - "cross-chain data updating consistency"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Title/abstract explicitly identify cross-chain, dynamic data, and data consistency verification."
  - "Sections 4-5 define source chain, target chain, audit chain, collaborative smart contracts, data transferring, data updating, and consistency auditing."
  - "The paper evaluates a Hyperledger Fabric prototype but the main problem is interoperability/cross-chain verification, not transaction execution."
parent_knowledge_refs:
  - "nahida-knowledge-cross-chain-protocols"
  - "nahida-knowledge-blockchain-interoperability"
  - "nahida-knowledge-blockchain-systems"
bridge_refs: []
related_paths:
  - "vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md"
  - "vault/04_Knowledge/blockchain-systems/interoperability.md"
  - "vault/04_Knowledge/blockchain-systems.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0056"
queue_rank: 56
run_ids:
  - "nahida-knowledge-20260622-dccv-dynamic-cross-chain-data-consistency"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# A secure dynamic cross-chain decentralized data consistency verification model

## Paper Identity

| Field | Value |
| --- | --- |
| Title | A secure dynamic cross-chain decentralized data consistency verification model |
| Authors | Jiahao Zhao; Yushu Zhang; Jiajia Jiang; Zhongyun Hua; Yong Xiang |
| Venue | Journal of King Saud University - Computer and Information Sciences 36 (2024) 101897 |
| Year | 2024; available online 2023-12-29 |
| DOI | 10.1016/j.jksuci.2023.101897 |
| Local PDF | `~/Desktop/paper/1-s2.0-S1319157823004512-main.pdf` |
| Source key | `doi:10.1016/j.jksuci.2023.101897`; `sha256:96bb38c339a1823e1edb0594d65a7b9c2fa1113e028cfa8be4c595427c3c7789` |
| Pages | 13 |

## Path Materialization

| Layer | Placement | Evidence | Confidence |
| --- | --- | --- | --- |
| L1 Domain | `blockchain-systems` | Blockchain storage pressure, cross-chain technology, Hyperledger Fabric prototype | high |
| L2 Direction | `interoperability` | Source chain, target chain, audit chain, cross-chain data transfer/update/audit | high |
| L3 Topic | `cross-chain-protocols` | DCCV is a cross-chain consistency verification protocol for dynamic data | high |
| L4 Source | this paper | DOI/PDF source note | high |

Queue correction: the serial queue classified this paper as `blockchain-systems/execution-and-transactions/transaction-processing`. Deep reading shows the primary path should be `blockchain-systems/interoperability/cross-chain-protocols`; execution is only the Fabric/smart-contract substrate.

## Reading Coverage

| Section/pages | What was read | Coverage |
| --- | --- | --- |
| Abstract, §1 / p1-p2 | Problem, motivation, contribution and two consistency meanings | high |
| §2 / p2-p3 | Cross-chain related work and dynamic data auditing related work | high |
| §3 / p3-p4 | Decentralized chameleon hash, CoSi, Merkle hash tree, multi-signcryption, lightweight cryptography preliminaries | high |
| §4 / p4-p5 | System model, threat model, design goals | high |
| §5 / p5-p9 | DCCV construction: initialization, collaborative smart contracts, data transferring, updating, and auditing | high |
| §6 / p9-p10 | Security analysis against tampering, privacy leakage, and audit inconsistency | high |
| §7 / p10-p11 | Hyperledger Fabric experiments and overhead comparisons | high |
| §8 / p11-p12 | Conclusion and future work | high |

## One Sentence Summary

DCCV 用一条可信 audit chain 协调 source chain 与 target chain，通过动态 Merkle hash tree、decentralized chameleon hash、CoSi 签名和 multi-signcryption，验证跨链传输数据的完整性以及源链动态更新是否被目标链完整、正确地同步。

## Problem Setting

论文从两个矛盾出发。第一，区块链交易和数据增长造成存储压力，跨链存储/交互可以把数据分散到多条链上。第二，链的 immutability 阻碍某些数据更新，例如过期身份信息、恶意交易或需要修订的动态数据。Decentralized chameleon hash 可以让链内数据在保持去中心化的条件下被授权更新，但一旦数据已经跨链传输，源链更新后目标链是否同步更新就成为新的 consistency 问题。

本文中 consistency 有两层含义：

| Consistency aspect | Meaning | Where handled |
| --- | --- | --- |
| Transferring consistency | target chain 接收的数据需要与 source chain 存储的数据保持 correctness 和 integrity。 | Periodic audit with Merkle proof/tag comparison |
| Updating consistency | source chain 更新的数据需要在 target chain 上完整且正确地更新。 | Update-triggered audit with decentralized chameleon hash verification |

Related work 中，传统 dynamic PDP/POR/ADS auditing 主要面向 cloud storage，通常依赖 TPA；论文认为这不适合区块链跨链场景，因为 TPA 可能恶意、会破坏去中心化，并且审计对象从 cloud-stored data 变成 cross-chain interaction data。相邻的 cross-chain 工作多关注资产转移、静态数据一致性或隐私保护，DCCV 的定位是 dynamic cross-chain data consistency verification。

## System Model

系统有四类实体。

| Entity | Role |
| --- | --- |
| Data owner (`DO`) | 将原始数据 `F` 预处理为 blinded data `F'`，生成 authentication tags 和 decentralized chameleon hash randomness，然后上传到 source chain。 |
| Source chain (`SC`) | 存储 `F'`，构造 dynamic Merkle hash tree，向 target chain 发送数据和 tags；当数据更新为 `F*` 时，广播 update request 给 target chain 和 audit chain。 |
| Target chain (`TC`) | 接收、验证并存储 `F'` 与 tags；按 source chain 的 update request 更新数据；被 audit chain challenge 时生成 proof。 |
| Audit chain (`AC`) | 由 national regulatory authorities 建立，被假设为 honest/trustworthy；向 SC/TC 发起 challenge，并验证两边 proof 是否一致。 |

Threat model 覆盖三类攻击：

| Attack | Description | DCCV response |
| --- | --- | --- |
| Cross-chain tampering | 传输数据、update request 或 contract deployment request 被伪造/篡改。 | CoSi signature 和 multi-signcryption 验证请求、合约、数据。 |
| Cross-chain privacy leakage | authentication tags 或 update requests 的内容在链间交互中泄漏。 | Blinding + multi-signcryption，安全性归约到 DLP。 |
| Audit inconsistency | target chain 不完整存储/更新数据，但试图伪造 proof 骗过 audit chain。 | Merkle proof、tags、DCH.Verify 和 hash collision/DLP 假设。 |

关键限制是 audit chain 和 data owner 都被假设为 honest。这个模型适合监管链/联盟链场景，不等同于完全 permissionless/trustless bridge。

## DCCV Construction

### 1. Collaborative Smart-Contract Deployment

DCCV 在三条链上部署不同 smart contracts：

| Contract | Chain | Function |
| --- | --- | --- |
| `Ss` | source chain | 处理和更新数据，传输 audit proof、processed data 和 update request。 |
| `St` | target chain | 验证接收数据，按 request 更新数据，生成 target-side storage proof。 |
| `Sa` | audit chain | 生成 challenge，接收并验证 SC/TC 的 proof，输出 consistency result。 |

部署过程由 audit chain 发起。`Sa` 先向 `SC`/`TC` 发送 deployment request；两链节点制定并签名 `Ss`/`St`；`AC` 验签并用 test data 检查 contract 是否满足 request，满足后再签名返回。论文用 CoSi witness co-signature 保护 deployment request 和 smart contract 传输，使跨链合约配置具有可验证关联性。

### 2. Data Transferring

Data owner 先把 `F` 切成 blocks/sectors，并用随机值 `rd` 生成 blinded sectors `f'ij`，从而避免直接暴露原始数据。随后生成 authentication tags 和 initial decentralized chameleon hash randomness `r0`，上传到 `SC`。

`SC` 对收到的数据构造 dynamic Merkle hash tree。与普通 MHT 不同，DCCV 在 leaf/internal node hash 中引入 decentralized chameleon hash，使后续交易更新不必改变 block header hash，同时仍保留可验证路径。`SC` 把 `F'` 和 tag set 打包成 data uploading transaction `Tx1` 发送给 `TC`，传输过程中使用 multi-signcryption 保护 confidentiality、integrity 和 authentication。

`TC` 收到后先验证 signcryption，再验证 uploaded data set 和 tags 是否一致。如果验证失败则拒绝存储；验证通过后存储数据并生成自己的 chameleon hash randomness `r1`。

### 3. Data Updating

更新过程使用 threshold decentralized chameleon hash。论文先按用户节点身份 hash 排序，选择前 `t` 个节点生成共享 update key；为了防止攻击者在前后阶段累计 `t-1` 个 shares，更新阶段阈值扩展为 `2t-1`，并支持节点动态加入/退出时从 `(t,n)` 调整到 `(t',n')`。

更新步骤概括如下：

| Step | Mechanism |
| --- | --- |
| Threshold key generation | 多节点生成 decentralized chameleon hash key shares 和 master public key。 |
| Share re-sharing | 当节点数量/阈值变化时，用随机多项式把 private key shares 更新到新阈值。 |
| Source update | `SC` 节点验证待更新交易对 `(tx, tx')` 签名，替换地址，生成新 MHT root `h*Root`。 |
| Request broadcast | `SC` 生成 update request，收到足够节点确认后计算新 randomness `r'0`，用 multi-signcryption 向 `TC` 发送 `req'`。 |
| Target update | `TC` 验证请求签名，定位 transaction address，更新本地数据，生成 `r'1` 和 updated root `h**Root`。 |

核心思想是：chameleon hash 让被授权的动态更新可以保持 block header hash 不变；threshold 和前序节点验证降低单点 key compromise 或恶意更新风险；audit chain 则在更新后验证 target 是否同步执行。

### 4. Consistency Verification

DCCV 的 audit 分成 periodic audit 和 update-triggered audit。

| Audit type | Challenge/proof | Verification goal |
| --- | --- | --- |
| Periodic data consistency audit | `AC` 随机挑战 MHT positions；`SC`/`TC` 分别返回 tags、siblings、MHT root。 | 检查 target 存储的数据和 source transferred data 是否一致。 |
| Data updating consistency audit | `SC` 返回 updated transaction pairs 和 randomness before/after；`TC` 返回 target-side randomness before/after。 | `AC` 调用 DCH.Verify 检查更新前后的 chameleon hash relationship 是否有效。 |

这使 DCCV 同时覆盖初始跨链传输 integrity 和后续动态更新 consistency。它不是通用 cross-chain messaging protocol，也不是 DA sampling；它是围绕动态数据更新和跨链审计的协议模型。

## Security Claims

| Claim | Paper argument | Assumption | Anchor |
| --- | --- | --- | --- |
| Cross-chain transferred data privacy/integrity is preserved. | 攻击者若要伪造或篡改 multi-signcryption message，需要从 public key 求 private key。 | Discrete Logarithm Problem | Theorem 1, §6 |
| Transferred contracts and requests are secure if receiver-side contract verifies CoSi equation. | CoSi verification equation simplifies to aggregation value `V` when signature was honestly generated. | Correct CoSi verification; honest receiver contract | Theorem 2, §6 |
| Plaintext cross-chain data is protected. | 攻击者无 receiver private key，无法计算解密所需值。 | DLP in multi-signcryption | Theorem 3, §6 |
| Target chain cannot forge audit proof of transferred data. | Forging periodic proof requires hash collision; forging update proof requires valid chameleon hash randomness. | Collision-resistant hash and DLP | Theorem 4, §6 |

这些是理论分析，不是形式化 machine-checked proof。安全边界依赖 honest audit chain、honest data owner、正确实现的 smart contracts、DLP/hash assumptions，以及 consortium/Fabric setting 下的成员与链治理。

## Experimental Evaluation

实验环境是 Hyperledger Fabric v1.4 on Ubuntu 18.04，32 GB memory，三个区块链分别部署 `Sa`、`Ss`、`St`，用 Go 实现 smart contracts。每条链使用 standard Kafka orderer configuration：3 ZooKeeper nodes、4 Kafka brokers、3 Fabric orderers，初始化阶段有 16 peer nodes。由于没有合适的 blockchain dataset，实验使用 synthetic data。

| Evaluation axis | Result/observation | Interpretation |
| --- | --- | --- |
| Data preprocessing overhead | Block size 增大时 preprocessing time 降低；sector number 增大时 tag/MHT 构造成本上升。 | 分块粒度会影响 DO 侧预处理和 Merkle 构造成本。 |
| Data updating and verifying overhead | Threshold 增大时 updating time 上升；verification time 相对稳定。 | 更新成本主要来自节点达成更新 consensus/key participation，验证较固定。 |
| Hash key generation/hash computation | Key generation 随 threshold 增大而上升；Hash/ReHash 基本稳定。 | DCH 的 key generation 是扩展成本，hash computation 不是主要瓶颈。 |
| Multi-signcryption comparison | Paper's scheme reports 1.3026ms signing, 1.0321ms verifying, 2.3347ms total, lower than compared schemes in Table 3。 | 说明链间数据保护在实验参数下可用，但比较范围有限。 |
| Cross-chain data transferring | Data size 增大时 transfer overhead 增加。 | 传输阶段仍受数据量影响，DCCV 没有消除链间带宽成本。 |
| CoSi execution | CoSi 与 RSA-based multi-signature overall time 类似，签名者数量变化实验显示可扩展性。 | 支撑 collaborative contract deployment 的签名聚合选择。 |

## What This Source Adds To Knowledge

| Reusable delta | Target knowledge node | Promotion decision |
| --- | --- | --- |
| Cross-chain protocols 不只处理资产转移/桥，还可以处理动态数据更新后的 source-target consistency auditing。 | [[cross-chain-protocols|Cross-chain protocols]] | source_extension |
| Audit chain 可以作为监管/联盟链场景中的 cross-chain consistency verifier，但这引入 honest/trusted audit-chain 假设。 | [[interoperability|Blockchain interoperability]] | method row / boundary |
| Dynamic Merkle hash tree + decentralized chameleon hash 是可更新链上数据与可验证审计之间的组合模式。 | [[cross-chain-protocols|Cross-chain protocols]] | source_extension; no standalone node yet |
| CoSi + multi-signcryption 在该模型中服务于 contract/request/data transfer authenticity/privacy，而不是完整 bridge finality。 | [[cross-chain-protocols|Cross-chain protocols]] | source-local detail; review for future bridge if more sources appear |

## Limitations And Open Questions

| Limitation/gap | Why it matters |
| --- | --- |
| Audit chain is assumed honest/trustworthy and run by regulatory authorities. | 这与 trustless cross-chain bridges 不同，适合监管/联盟场景；若 audit chain 被攻破或治理失败，模型安全性会下降。 |
| Data owner is assumed honest. | 若 DO 预处理或 tag generation 本身恶意，本文不处理源头数据真实性。 |
| Prototype uses Hyperledger Fabric v1.4 and synthetic data. | 实验说明趋势和可行性，但不代表真实生产 workload、WAN latency 或 heterogeneous-chain deployment。 |
| No implementation details for Ethereum/mixed chains yet. | 结论中把 Ethereum/mixed deployment 留作 future work。 |
| Threshold/chameleon-hash mechanism is mathematically heavy. | 需要实现正确、key-share governance、节点动态加入退出和智能合约验证的工程细节。 |
| PQC/side-channel/lightweight encryption are future work. | 论文安全性主要依赖 DLP/hash assumptions；后量子和实现攻击未覆盖。 |

## Relation Extraction

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| this source | evidenced_by | `doi:10.1016/j.jksuci.2023.101897` | DOI/PDF | high | active |
| this source | instance_of | `blockchain-systems/interoperability/cross-chain-protocols` | §1, §4, §5 | high | active_seed |
| dynamic cross-chain data consistency verification | is_a | cross-chain protocol problem | abstract, §1, §5 | high | active_seed |
| audit chain | used_in | dynamic cross-chain data consistency verification | §4.1, §5.1, §5.5 | high | source_extension |
| decentralized chameleon hash | used_in | dynamic data updating consistency verification | §3.1, §5.5 | high | source_extension |
| CoSi / multi-signcryption | used_in | cross-chain request/data authenticity and privacy | §5.3, §5.4, §6 | high | source_extension |

## Absorption Handoff

| Target | Action |
| --- | --- |
| `vault/04_Knowledge/blockchain-systems/interoperability/cross-chain-protocols.md` | Add DCCV as dynamic data consistency verification route and source extension. |
| `vault/04_Knowledge/blockchain-systems/interoperability.md` | Add parent-level note that interoperability includes dynamic data update consistency, not only assets/headers/auditing privacy. |
| `vault/04_Knowledge/blockchain-systems.md` | Add representative source extension under interoperability. |
| Bridge layer | Do not create a new bridge yet; the cross-cutting relation to storage/data availability is still source-thin and should stay as a review/watch candidate. |

## Update Record

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-dccv-dynamic-cross-chain-data-consistency | Deep-read source note created and classification corrected to cross-chain protocols. | codex |
