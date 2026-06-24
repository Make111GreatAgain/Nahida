---
id: "arxiv:2208.00283v2"
title: "Recurring Contingent Service Payment"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1 abstract, introduction, contributions"
  - "p2-p6 preliminaries, related work, zkCSP privacy leakage and free-riding attack"
  - "p6-p9 RC-S-P definition, correctness, malicious-client/server security, privacy"
  - "p9-p13 SAP, generic RC-S-P, RC-PoR-P construction and no-arbiter variant"
  - "p13-p15 RC-PoR-P performance evaluation and comparison"
  - "p15-p40 references, related-work survey, VS/VSID definitions, RC-S-P protocol, security proofs, trade-offs, asymptotic table"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2208.00283v2"
doi: ""
arxiv_id: "2208.00283v2"
venue: "arXiv preprint"
year: "2023"
pdf_pages: 40
pdf_sha256: "35204fe12538caa10e1efd7b54d8fb113f72fb48886c7e97cd58705f50821472"
local_pdf: "~/Desktop/paper/2208.00283v2.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2208.00283v2-35204fe12538-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
topic_ids:
  - "fair-exchange-protocols"
  - "contingent-service-payments"
  - "verifiable-services"
  - "proofs-of-retrievability"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "fair-exchange-protocols"
  - "contingent-service-payments"
primary_ontology_path: "blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments"
secondary_ontology_paths:
  - "verifiable-computation/verifiable-computation-systems"
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
path_update_status: "corrected_from_queue"
related_knowledge_refs:
  - "nahida-knowledge-contingent-service-payments"
  - "nahida-knowledge-blockchain-fair-exchange-protocols"
  - "nahida-knowledge-blockchain-execution-and-transactions"
  - "nahida-knowledge-verifiable-computation-systems"
  - "nahida-knowledge-fair-data-exchange"
bridge_refs:
  - "nahida-bridge-verifiable-computation-systems-to-contingent-service-payments"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "verifiable-computation"
  directions:
    - "execution-and-transactions"
    - "verifiable-computation-systems"
  topics:
    - "fair-exchange-protocols"
    - "contingent-service-payments"
    - "verifiable-services"
    - "proofs-of-retrievability"
domains:
  - "blockchain-systems"
  - "verifiable-computation"
topics:
  - "recurring contingent service payment"
  - "contingent service payment"
  - "fair exchange for verifiable services"
  - "proofs of retrievability payment"
  - "verifiable service with identifiable abort"
  - "statement agreement protocol"
  - "private time bubble"
  - "coin masking"
aliases:
  - "RC-S-P"
  - "RC-PoR-P"
  - "Recurring Contingent Service Payment"
  - "Recurring Contingent Proofs of Retrievability Payment"
  - "contingent service payment"
authors:
  - "Aydin Abadi"
  - "Steven J. Murdoch"
  - "Thomas Zacharias"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "fair-exchange"
  - "proof-of-retrievability"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "execution-and-transactions"
    - "verifiable-computation"
  problem:
    - "clients and servers need fair recurring payment for verifiable services without trusting either side"
    - "blockchain contingent service payment leaks proof status and deposit amount"
    - "existing zkCSP-style PoR payments let malicious clients free-ride by constructing ill-formed metadata"
  method_family:
    - "recurring contingent service payment"
    - "verifiable service with identifiable abort"
    - "statement agreement protocol"
    - "private time bubble and coin masking"
    - "Merkle-tree proof-of-retrievability payment"
  system_layer:
    - "smart contract escrow and coin distribution"
    - "off-chain verifiable service proofs"
    - "dispute resolution by offline arbiter or smart contract"
  evaluation_context:
    - "RC-PoR-P prototype"
    - "C++ off-chain implementation"
    - "Solidity on-chain implementation"
    - "64MB to 4GB files"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
source_refs:
  - "arxiv:2208.00283v2"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> execution-and-transactions -> fair-exchange-protocols -> contingent-service-payments"
secondary_directions:
  - "verifiable-computation -> verifiable-computation-systems"
  - "blockchain-systems -> data-availability-and-light-clients -> fair-data-exchange"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p40"
  - "abstract and Section 7 define recurring contingent service payment, not consensus"
  - "Sections 5-6 target zkCSP privacy leakage and malicious-client free-riding in PoR payments"
  - "Sections 8-9 build SAP, VSID, RC-S-P and RC-PoR-P over smart contracts"
  - "classification corrected from blockchain-systems/consensus/consensus-foundations"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0087"
queue_status: "absorbed"
---

# Recurring Contingent Service Payment

## 论文身份

- 标题: Recurring Contingent Service Payment
- 作者: Aydin Abadi; Steven J. Murdoch; Thomas Zacharias
- 版本: arXiv `2208.00283v2`, `cs.CR`, 2023-04-05
- 本地 PDF: `~/Desktop/paper/2208.00283v2.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/2208.00283v2-35204fe12538-pages.txt`
- SHA-256: `35204fe12538caa10e1efd7b54d8fb113f72fb48886c7e97cd58705f50821472`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- 已覆盖: 摘要/引言、相关工作、zkCSP 攻击与隐私泄露、RC-S-P 定义与安全性、SAP、VS/VSID、泛化协议、RC-PoR-P 构造、性能评估、trade-offs、无仲裁者变体、附录证明。
- Extraction gaps: 表格和公式有 OCR 断行；source note 记录协议结构、关键等式语义和论文给出的数值，不逐字保留所有概率实验。

## 一句话贡献

这篇论文把 blockchain fair exchange 从“一次性买数字商品”扩展到“按周期为可验证服务付费”: RC-S-P 用 VSID、SAP、私有时间泡泡、存款遮蔽和争议归责，让客户端只有在服务证明有效时付款，同时服务器也不会被恶意客户端用无效元数据或查询白嫖。

## 论文要解决的问题

现有 contingent payment / ZKCP / zkCSP 路线通常把卖方视为潜在攻击者，却没有充分处理买方也可能恶意的情况。服务付款场景比买一个静态文件更难，因为服务会重复发生、证明状态本身会泄露系统健康状态，且客户端可能构造 malformed inputs 让诚实服务器生成失败证明，再借此拒付。

论文把问题拆成三个目标:

| 目标 | 含义 | 为什么重要 |
| --- | --- | --- |
| Fair recurring service payment | 多个 billing cycles 中，服务证明有效才付款，服务证明无效则退款/惩罚。 | 云存储、可验证计算、可搜索加密等服务都不是一次性商品交付。 |
| Malicious-client security | 客户端不能用无效 metadata/query 让服务器浪费资源或错误背锅。 | 服务付款天然有“拒付”激励，传统 PoR/VC 常只防恶意 server。 |
| Proof-status and price privacy | 在 private time bubble 内隐藏证明是否通过、实际价格/文件规模等信息。 | 证明失败状态可能暴露服务器故障，存款金额可能暴露服务类型和文件大小。 |

## 分类判断

队列把本篇暂放在 `blockchain-systems/consensus/consensus-foundations`，这是错误分类。本篇没有研究 fault-tolerant agreement、block ordering 或 validator finality；它研究的是 smart contract escrow、付款/退款、争议处理和可验证服务证明的组合协议。

正确主路径是:

```text
blockchain-systems / execution-and-transactions / fair-exchange-protocols / contingent-service-payments
```

Secondary path 是 `verifiable-computation/verifiable-computation-systems`，因为论文抽象了 `Verifiable Service (VS)` 与 `Verifiable Service with Identifiable Abort (VSID)`，覆盖 PoR、verifiable computation、verifiable searchable encryption 和 verifiable information retrieval 等服务。

## 相关工作与攻击面

论文对比的核心相邻路线包括:

| Route | 论文里的角色 | 关键边界 |
| --- | --- | --- |
| Zero-Knowledge Contingent Payment | 用链上 hash-lock 和 ZK proof 购买 secret/digital good。 | 主要是一锤子买卖，服务场景要额外处理 proof status 和恶意客户端。 |
| zkCSP | Campanelli et al. 将 ZKCP 扩展到 contingent service payment，并给出 PoR 实例。 | 本文指出其 PoR 实例存在 free-riding attack 和 privacy leakage。 |
| FairSwap / OPTISWAP | 用 proof-of-misbehavior 降低链上争议成本。 | 适合数字商品交换，不能直接保证可验证服务付款。 |
| Outsourced fair PoR | 让智能合约或 puzzle 支撑 PoR 付款。 | 相关方案多假设客户端诚实，未处理本文的 malformed metadata/query 问题。 |

## zkCSP 的两个问题

### Proof Status Leakage

在 zkCSP / blockchain contingent service payment 中，链上付款结果会公开暴露服务证明是否通过。对 PoR 来说，连续 proof failure 可能显示某个存储服务商正在经历硬件、软件或运维故障。攻击者可以利用这个信息做 targeted social engineering，或者在知道用户数据服务异常时发起更可信的诈骗/钓鱼。

### Deposit Amount Leakage

如果服务价格与文件大小、服务等级或地区有关，链上存款金额会泄露客户端购买的服务形态。即使服务器使用新地址，若多服务商/多协议假设不成立，观察者仍可通过金额模式进行关联。

### Free-Riding Attack

论文给出的攻击发生在 zkCSP 的 PoR 实例里。恶意客户端可以构造 ill-formed PoR metadata，例如对文件块 `m_i` 提供对应另一个 `m'_i` 的 tag。诚实服务器按收到的数据生成 PoR proof，但验证自然失败。因为协议没有让服务器在服务前检查 tag/metadata correctness，也没有 dispute mechanism 能证明失败归因于客户端，客户端可以享受服务或消耗服务器资源却拒付。

这个攻击的本质是: 普通 PoR 假设客户端诚实，只防恶意服务器；contingent service payment 里客户端和服务器都可能作恶，必须把客户端输入正确性纳入协议。

## 核心抽象

### Verifiable Service

`Verifiable Service (VS)` 抽象成五个算法: key generation、setup、query generation、prove、verify。客户端提供服务输入、metadata 和 query；服务器执行函数 `F` 并给出 proof；客户端验证 proof 是否对应 `F(u*, q, pp)`。PoR、verifiable computation、verifiable searchable encryption 和 verifiable information retrieval 都是 VS 的例子。

### VSID

`Verifiable Service with Identifiable Abort (VSID)` 在 VS 上增加两类能力:

- 客户端要证明 metadata 和 query well-formed，服务器可以在服务前拒绝恶意输入。
- 争议时 arbiter 能识别 misbehaving party: 如果 metadata/query proof 错，归责客户端；如果 service proof 错，归责服务器；如果都对，则说明投诉无效。

泛化 VSID 可用 NIZK、签名和 bulletin board 构造；PoR 实例则利用 Merkle tree 和 proof of misbehavior 避免昂贵 ZK proofs。

## RC-S-P 机制

RC-S-P 涉及四个角色: client、server、arbiter 和 smart contract。合约主要托管 deposits、记录加密/填充消息、接收 arbiter report，并按 agreed statement 分配 coins。

协议有八个阶段:

| Phase | 作用 |
| --- | --- |
| `keyGen` | 客户端生成服务验证密钥、加密密钥和 padding 参数。 |
| `cInit` | 客户端生成 metadata、proof/query token、coin token，并部署合约/存款。 |
| `sInit` | 服务器检查输入、SAP statements 和客户端存款，决定是否服务并存入 dispute reserve。 |
| `genQuery` | 客户端每个 billing cycle 生成查询，encrypt-then-pad 后发到合约。 |
| `prove` | 服务器读取并验证查询；若有效则生成服务 proof，若无效则记录 complaint 并发 dummy proof。 |
| `verify` | 客户端本地解密并验证 proof；失败时记录 complaint。 |
| `resolve` | private time bubble 结束后，arbiter 解密相关消息并识别 misbehaving party。 |
| `pay` | 合约验证 coin statement，并按 `yC/yS/y'C/y'S` 计数分配 client/server/arbiter coins。 |

## 关键设计

| 设计 | 解决的问题 | 代价/边界 |
| --- | --- | --- |
| Statement Agreement Protocol | 双方在一开始对 payment details 和 query/proof secret parameters 达成可证明但暂时私密的约定。 | 依赖 commitment hiding/binding、签名和链上合约。 |
| Private time bubble | 在争议窗口前不公开解密 proof/query，不在链上即时结算 proof status。 | 隐私只持续到 bubble burst / dispute resolution。 |
| Coin masking | 客户端和服务器按 price list 最大值存款，隐藏实际服务价格。 | 增加 deposit capital lock-up。 |
| Encrypt-then-pad | 查询和证明先加密再填充到固定形态，隐藏 proof/query status 和 size。 | 增加通信/存储；padding 参数要提前协商。 |
| Arbiter reserve | 作恶或无效投诉的一方支付 arbiter 成本。 | 引入离线可信仲裁者；不过正常路径无需仲裁者在线。 |

## RC-PoR-P 实例

论文给出 PoR 服务的具体实例 `RC-PoR-P`。它不用通用 NIZK 来证明 tag correctness，而是把 PoR 改造成 Merkle-tree-based variant:

- 客户端对文件做 erasure coding，切块并在 block+index 上建 Merkle tree。
- 查询不是发送 `phi` 个 challenge，而是发送 PRF seed，服务器从 seed 导出被挑战 block indices。
- 服务器返回每个被挑战 block 的 Merkle path。
- 客户端如果发现 proof 无效，只需记录一个失败 path 的 index。
- 争议时 arbiter 只验证那一个失败 path，而不必验证 `phi` 个 proofs。

这个设计把 arbiter-side work 从 `phi * log2(m)` 降到 `log2(m)`。论文使用 `phi=460` 作为示例，指出这是约 `1/460` 的争议验证工作量。

## 无仲裁者变体

由于 RC-PoR-P 的争议验证足够便宜，论文还给出把 arbiter 角色委托给 smart contract 的变体。主要变化是:

- 参与者只剩 client、server、smart contract。
- 不再需要记录无效投诉计数 `y'C/y'S`，因为发起投诉的一方先为链上处理付费。
- coin transfer 从补偿 arbiter 改为补偿诚实方的 dispute gas/cost。

这不是通用 RC-S-P 的默认路线，因为只有当争议验证非常轻时，smart contract 才适合作为 arbiter。

## 性能与评估

论文实现了 RC-PoR-P:

| Layer | Implementation |
| --- | --- |
| Off-chain | C++，Crypto++ 与 GMP |
| On-chain | Solidity，Ethereum private blockchain |
| Hardware | off-chain server: dual Intel Xeon Gold 5118, 256GB RAM; on-chain test via MacBook Pro + private chain |
| File sizes | 64MB 到 4GB，对应 `2^22` 到 `2^28` blocks |

关键结果:

| Result | Meaning |
| --- | --- |
| 4GB 文件 proof verification 约 `0.24s` per verification | 客户端验证仍可接受，正文摘要用 90ms 作为较小/给定设置下的验证例。 |
| dispute resolution 约 `10^-4s * z'` at `2^28` blocks | 争议验证极轻，来自只检查一个 Merkle path。 |
| smart contract coin transfer 为常数工作 | 链上不随文件大小验证完整 PoR。 |
| client/server setup 为 `O(m)` | Merkle tree 构造和服务器重建树仍随文件大小线性增长。 |
| prove/verify 为 `O(z * phi * log2(m))` | proof size 和计算比 homomorphic-tag PoR 大，但只用 hash/symmetric encryption。 |

Table 2 对比显示，已有 fair PoR / zkCSP 类方案 proof size 可为 `O(1)`，但不防恶意客户端且不提供本文的 privacy；RC-PoR-P 以较大 proof size 换取 malicious-client security 和 privacy。

## 安全性和假设

RC-S-P 安全性包括:

- malicious server security: 服务器不能拿无效服务 proof 骗过客户端/仲裁者，也不能篡改付款分配。
- malicious client security: 客户端不能用无效 metadata/query 骗服务器服务，也不能把服务器诚实 proof 伪造成失败来拒付。
- privacy: 在 private time bubble 内隐藏服务输入、query/proof status 和实际 price/deposit details。

RC-PoR-P 的 theorem 依赖:

| Assumption | 用途 |
| --- | --- |
| Merkle tree / collision resistance | PoR proof of membership 和 proof of misbehavior soundness。 |
| PRF security | 挑战 indices 在 seed 揭示前不可预测。 |
| Commitment binding/hiding | SAP statement 不可篡改且打开前隐藏。 |
| Digital signature EUF-CMA | 双方不能否认或伪造交易/消息来源。 |
| IND-CPA symmetric encryption | private time bubble 内的 query/proof 隐私。 |
| Secure blockchain/smart contract | 存款、记录、liveness 和 coin distribution 正确执行。 |

## Trade-offs

- 相比 zkCSP，RC-S-P 引入 offline arbiter；这是为了在恶意客户端/服务器双向作恶时仍能归责。
- 为隐藏价格和文件规模，双方需要存入更高的 masked deposits。
- 为防止否认，更多消息需要出现在链上或以可否认性安全的方式传递给 arbiter。
- 通用 RC-S-P 依赖 Ethereum-style smart contract，而不是 Bitcoin 的极简脚本；论文认为所需合约能力仍很有限。
- RC-PoR-P 使用 Merkle proofs，proof size 大于 homomorphic-tag PoR，但避免通用 ZK proof 并获得恶意客户端安全。

## 可复用贡献

| 可复用层 | 提取内容 | Promotion |
| --- | --- | --- |
| Contingent service payments | 服务证明、重复 billing、付款/退款/争议归责的协议问题 | [[contingent-service-payments|Contingent service payments for verifiable services]] |
| Blockchain fair exchange | 从 digital goods 扩展到 recurring verifiable services；补入 proof-status privacy 和 malicious-client threat model | [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] |
| Verifiable service abstraction | VS/VSID 把 PoR、VC、searchable encryption 等服务统一到可付款服务接口 | [[verifiable-computation-systems|Verifiable computation systems]] |
| PoR payment route | Merkle proof of misbehavior 支撑低成本 dispute resolution | [[fair-data-exchange|Fair data exchange for committed data]] as adjacent contrast |
| Cross-domain bridge | VC/VS 的 correctness proof 与 fair exchange 的 payment/escrow layer 分离 | [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]] |

## Evidence Table

| Evidence anchor | Claim supported | Confidence | Upper-layer action |
| --- | --- | --- | --- |
| p1-p2 | RC-S-P 是 generic blockchain-based recurring payment for verifiable service；贡献包括 first formal treatment with malicious client/server and privacy。 | high | create contingent-service-payments node |
| p4-p6 | zkCSP leaks proof status/deposit amount and suffers free-riding attack in PoR instantiations。 | high | update fair-exchange threat model |
| p6-p9 | RC-S-P definition includes correctness, malicious-server/client security and privacy。 | high | source-backed problem definition |
| p9-p13 | SAP + VSID + private time bubble + encryption/padding/masked deposits realize RC-S-P and RC-PoR-P。 | high | method family rows |
| p13-p15 | implementation and performance show low dispute resolution and constant smart contract cost, with setup/proof costs trade-off。 | high | representative source and performance anchors |
| Appendix E-F | VS and VSID definitions generalize PoR/VC/searchable encryption/IR and add identifiable abort。 | high | update verifiable-computation systems |
| Appendix H-L | trade-offs and no-arbiter variant clarify when smart contract can replace arbiter。 | medium | bridge boundary and review candidate |

## Handoff to Knowledge

- Created primary problem node: [[contingent-service-payments|Contingent service payments for verifiable services]].
- Updated parent problem: [[fair-exchange-protocols|Blockchain-based fair exchange protocols]].
- Updated direction: [[execution-and-transactions|Blockchain execution and transactions]].
- Updated adjacent method node: [[verifiable-computation-systems|Verifiable computation systems]].
- Updated adjacent DA/data node: [[fair-data-exchange|Fair data exchange for committed data]].
- Created bridge: [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]].

## Review Notes

| Candidate | Handling | Reason |
| --- | --- | --- |
| `RC-S-P` as standalone knowledge node | rejected | It is the paper's named construction; details stay in source note and method rows. |
| `contingent-service-payments` | promoted | It is a reusable problem family under blockchain fair exchange, already anticipated by parent note. |
| `proofs-of-retrievability` foundation node | review | This source provides enough PoR background for the source note, but the vault lacks dedicated PoR sources; wait for PoR/PDP/storage-proof sources before creating a full foundation node. |
| `verifiable-service-with-identifiable-abort` | keep_section | Strong concept, but currently source-defined; record under VC systems until more sources justify a child node. |
