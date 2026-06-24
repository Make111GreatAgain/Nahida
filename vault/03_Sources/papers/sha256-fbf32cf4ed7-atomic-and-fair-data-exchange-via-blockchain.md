---
id: "sha256-fbf32cf4ed7"
title: "Atomic and Fair Data Exchange via Blockchain"
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
  - "p1-p3 title, abstract, introduction, FDE problem, high-level protocol, contribution and comparison table"
  - "p3-p5 related work: FairSwap, FileBounty, FairDownload, ZKCP, ZKCPlus, RC-S-P, verifiable encryption"
  - "p5-p7 VECK definition, security properties, FDE syntax, Ethereum/Bitcoin protocol outline"
  - "p7-p13 KZG preliminaries, ElGamal VECK, subset openings, Paillier VECK, theoretical and implementation performance"
  - "p13-p14 multi-client model, open problems, server griefing, distributed data-storage and Danksharding application"
  - "p15-p25 appendices: assumptions, sigma protocols, Danksharding background, Paillier, adaptor signatures, scripts, security proofs"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "IACR Cryptology ePrint 2024/418 in references; local PDF venue not explicit"
year: "2024"
pdf_pages: 25
pdf_sha256: "fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
local_pdf: "~/Desktop/paper/2024-418.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/atomic-and-fair-data-exchange-via-blockchain-fbf32cf4ed7d-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
topic_ids:
  - "fair-data-exchange"
  - "data-availability-sampling"
  - "kzg-commitments"
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "fair-data-exchange"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/fair-data-exchange/sha256-fbf32cf4ed7"
secondary_ontology_paths:
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments/sha256-fbf32cf4ed7"
  - "blockchain-systems/data-availability-and-light-clients/data-availability-sampling/sha256-fbf32cf4ed7"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
    - "cryptographic-protocols"
  directions:
    - "data-availability-and-light-clients"
    - "polynomial-commitments"
    - "proof-systems"
  topics:
    - "fair-data-exchange"
    - "verifiable-encryption-under-committed-key"
    - "kzg-commitments"
    - "data-availability-service-incentives"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
topics:
  - "fair data exchange"
  - "FDE"
  - "VECK"
  - "verifiable encryption"
  - "KZG commitments"
  - "Danksharding"
  - "EIP-4844"
  - "adaptor signatures"
aliases:
  - "FDE"
  - "Atomic and Fair Data Exchange"
  - "Fair Data Exchange via Blockchain"
  - "VECK paper"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-availability"
  - "zero-knowledge-proofs"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
  subdomain:
    - "data-availability-and-light-clients"
    - "polynomial-commitments"
  problem:
    - "servers should be paid for serving committed data without requiring clients to trust delivery"
    - "clients should receive data if and only if servers receive payment"
    - "post-expiry blob data needs trust-minimized retrieval incentives"
  method_family:
    - "blockchain fair exchange"
    - "verifiable encryption under committed key"
    - "KZG selective openings"
    - "adaptor signatures"
    - "multi-client VECK"
  system_layer:
    - "off-chain ciphertext and proof delivery"
    - "on-chain payment/key-release bonding contract"
    - "data availability archival retrieval"
  evaluation_context:
    - "Rust and Solidity implementation"
    - "Ethereum EVM gas evaluation"
    - "Bitcoin script/adaptor signature construction"
    - "BLS12-381 field-element transfer benchmarks"
  bridge:
    - "KZG commitments -> fair data exchange"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
source_refs:
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "pdf:~/Desktop/paper/2024-418.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> data-availability-and-light-clients"
secondary_directions:
  - "zero-knowledge-proofs -> polynomial-commitments"
  - "zero-knowledge-proofs -> proof-systems"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title page and abstract"
  - "Sections 1-8 and appendices A-F"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0038"
queue_status: "absorbed"
---

# Atomic and Fair Data Exchange via Blockchain

## 论文身份

- 标题: Atomic and Fair Data Exchange via Blockchain
- 作者: Ertem Nusret Tas, Istvan Andras Seres, Yinuo Zhang, Mark Melczer, Mahimna Kelkar, Joseph Bonneau, Valeria Nikolaenko
- 机构: Stanford University; Eotvos Lorand University; Guild.xyz; UC Berkeley; Cornell University; a16z Crypto Research; New York University
- 年份: 2024
- 参考条目: references list IACR Cryptology ePrint 2024/418
- DOI/arXiv: PDF 未给出 DOI/arXiv；本地文件名 `2024-418.pdf`
- 代码: `https://github.com/PopcornPaws/fde`
- 本地 PDF: `~/Desktop/paper/2024-418.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/atomic-and-fair-data-exchange-via-blockchain-fbf32cf4ed7d-pages.txt`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 25
- 已覆盖章节/页码: p1-p25 full text, including appendices and contract/script listings
- 未覆盖章节/页码: 无
- Extraction gaps: 数学公式、表格和 Solidity code 存在断词/空格噪声，但协议步骤、定义、theorem、benchmark 数字、appendix 结构可读。
- 精读说明: 该论文主问题不是发明新的 DAS 抽样算法，而是为已承诺数据提供公平、原子、低链上成本的付费检索协议；Danksharding/EIP-4844 是重要应用场景。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 身份与贡献 | 提出 blockchain FDE；定义 VECK；两种 VECK 实例；常数大小链上通信；Danksharding 应用；开源实现 | 核心贡献 | 主路径应为 fair-data-exchange |
| §1 / p1-p3 | 动机与方案概览 | 存储服务有存储激励但缺少“服务/下载”激励；客户端持有承诺，服务器持有数据；区块链作为 TTP 托管 payment/key release | 问题边界 | EIP-4844/expired blob 是应用 |
| §2 / p3-p5 | 相关工作 | FairSwap、FileBounty、FairDownload、BitStream、ZKCP/ZKCPlus、RC-S-P、VE/SAVER/CCE | 定位差异 | 强调无 dispute phase、常数链上 footprint、selective download |
| §3 / p5-p6 | VECK 定义 | Gen/Enc/Verct/Verkey/Dec；correctness、soundness、zero-knowledge；支持 committed data 的函数输出加密 | 方法抽象 | VECK 是本文新 primitive，暂不升为基础节点 |
| §4 / p6-p7 | FDE 语法与链上协议 | FDE.Setup/Com/Vrfy/Exc；client-fairness/server-fairness；Ethereum smart contract；Bitcoin adaptor signatures | 协议主干 | Theorem 4.1 归约到 VECK + chain security |
| §5 / p7-p10 | VECK constructions | KZG preliminaries；ElGamal VECK；subset openings；Paillier VECK | 技术核心 | 与 KZG commitments 建桥 |
| §6 / p10-p13 | 性能评估 | 3 rounds；constant-size on-chain footprint；Rust/Solidity implementation；ElGamal/Paillier prover/verifier/bandwidth/gas | 工程证据 | 需要保留具体数字 |
| §7 / p13-p14 | Multi-client model | 预处理 amortize server work；L-bits zero-knowledge 防止客户端只共享短 key 绕过支付 | 可复用扩展 | 适合多客户端查询同一 blob/block |
| §8 / p13-p14 | 讨论与未来方向 | server griefing、bandwidth overhead、PRF key derivation、distributed data-storage/Danksharding | 缺口 | 给知识节点开放问题 |
| Appendix A-F / p15-p25 | 附录 | DDH/DCR/AGM、Sigma protocols、Danksharding、Paillier、adaptor signatures、Bitcoin/Ethereum scripts、安全证明 | 证明/实现补充 | 支撑安全性质与工程边界 |

## 一句话贡献

论文把“客户端持有数据承诺、服务器持有数据、双方要原子交换数据和付款”的问题形式化为 blockchain Fair Data Exchange，并用 VECK 将大数据正确性验证放到链下，把链上工作压缩为 payment/key-release 验证，从而为 KZG-committed data、特别是 Ethereum blob/Danksharding 数据的付费检索提供 trust-minimized 协议路线。

## 核心精读笔记

### 问题边界: 存储证明不等于服务数据

论文从云存储和区块链 L2/off-chain storage 的缺口出发: proofs-of-retrievability、proofs-of-replication 或存储激励能让服务器因“存着数据”获益，但不能直接保证或激励服务器在客户端下载时实际提供数据。若服务器已经因存储拿到报酬，却不响应下载请求，数据对客户端仍不可用。证据锚点: §1 p1-p2。

FDE 的目标是让服务器在客户端收到承诺下的数据时才得到付款，同时客户端不应在付款前学到数据。这里的公平性不是一般跨链资产交换，也不是单纯的 proof-of-retrievability；它针对的是 committed data delivery。证据锚点: §1 p2, §4.1 p6-p7。

### Strawman 与设计目标

直接把数据发到 L1 smart contract，让合约验证数据匹配承诺再付款，是公平的，但会把全部数据写上链，费用和延迟都不可接受。论文目标是常数轮、低链上 footprint，并把大部分数据和证明保持在链下。证据锚点: §1 p2。

最终协议用链上合约只验证 decryption key 是否匹配先前提交的 verification key。大数据本体、ciphertexts 和 correctness proof 在链下传递；客户端验证后才锁款；服务器只有公开 secret key 才能收款；客户端再从链上读取 secret key 解密。证据锚点: Figure 1, §4.2 p7。

### FDE security: client-fairness 与 server-fairness

FDE 有四个接口: `Setup` 生成公共参数，`Com` 让客户端承诺并把数据交给服务器，`Vrfy` 验证数据与承诺一致，`Exc` 交换数据和 payment tokens。正确性要求诚实双方最终分别得到数据和 token。证据锚点: Definition 4.1-4.2 p6-p7。

Client-fairness 要求恶意服务器不能在客户端没有拿到正确数据时收到正付款；server-fairness 要求恶意客户端如果未让服务器收到约定付款，就不能从 transcript 中学到承诺以外的数据。Theorem 4.1 将这些性质归约到 VECK 的 correctness/soundness/zero-knowledge 与 Ethereum/Bitcoin 的安全和活性。证据锚点: Definition 4.3-4.4, Theorem 4.1, Appendix E.1。

### VECK: committed data 与 committed key 的连接件

VECK 允许服务器在给定数据承诺 `C_w` 和数据 `w` 时，输出 verification key、secret key、ciphertext 和 proof，证明 ciphertext 加密的是 `F(w)`，且之后链上可以只验证 secret key 与 verification key 匹配。Correctness 保障诚实加密可解出 `F(w)`；soundness 保障攻击者不能给出可验证但解密错误的 ciphertext/key；zero-knowledge 保障 ciphertext/proof/key commitment 在 secret key 公开前不泄露数据。证据锚点: Definition 3.1 p5-p6。

论文强调 VECK 可使用 symmetric/one-time encryption，因为 FDE 中密钥由同一次请求生成并只使用一次，不需要 CCA-secure 长期公钥加密。这是它相对传统 verifiable encryption 的设计空间差异。证据锚点: §1 p2-p3, §2 p4-p5。

### KZG 路线与 selective download

论文选择 KZG，因为它提供常数大小 commitment 和可 batch 的 opening proofs，而且 Ethereum Danksharding/EIP-4844 使用 KZG commitments。数据被看作多项式在一组点上的 evaluations；FDE 可以交换全量 evaluations，也可以交换子集。证据锚点: §1 p2, §3 p6, §5 p7-p10。

ElGamal VECK 的直觉是对每个 evaluation 做 exponential ElGamal encryption，并用随机挑战 `alpha` 把“ciphertexts 加密的是 KZG 承诺下的 evaluations”压成一个多项式一致性检查；range proofs 用来处理高熵 field elements 的分块。subset opening 先构造在请求集合 `S` 上一致的低度 polynomial `phi'_S`，再用 full-opening VECK 作为子程序。证据锚点: §5.1-§5.2, Figures 2-4。

Paillier VECK 试图降低 ElGamal 的 plaintext 分块带来的 ciphertext blowup。它用 Paillier ciphertext 加密 evaluations，并通过 Sigma-protocol/Fiat-Shamir 风格 proof 证明 encrypted values 与 KZG commitment 一致；安全基于 DCR、random oracle 和 AGM，正确性有可忽略失败概率。证据锚点: §5.3, Figure 5, Appendix E.3。

### Ethereum 与 Bitcoin 实例

Ethereum 实例中，服务器先在 bonding contract 中登记 verification key、价格、客户端地址和 timeout；客户端验证链下 ciphertext/proof 后锁款；服务器提交 secret key，合约检查 `Verkey(vk, sk)` 后把款项记入服务器余额；如果服务器未按时揭示 key，客户端 timeout 后取回款。证据锚点: §4.2 p7, Appendix C.2 p19-p20。

Bitcoin 不需要 Turing-complete contract，而是用 adaptor signatures。客户端创建 bonding contract，服务器通过 decryption key 适配预签名并花费交易，客户端从 adapted signature 中 extract secret key 以解密数据。附录指出 server signature 与 adaptor signature 双签可避免客户端从 mempool 抢跑。证据锚点: §4.3 p7, Appendix B p18。

### 性能与工程边界

理论上协议是三轮: server 发送 ciphertext/proof，client 链上锁款，server 揭示 VECK decryption key。链上 footprint 为三份 signatures 加两个 group/key 元素，主要数据和 proof 都链下。证据锚点: §6.1 p10-p11。

实现使用 Rust 1.74 和 Solidity 0.8.13。对于 4096 个 BLS12-381 field elements 约 128 KiB 数据，ElGamal 方案的 range proofs + encryptions 约 89 秒，Paillier prover 约 5.09 秒；ElGamal verifier 约 34.15 秒，Paillier verifier 约 19.45 秒，Paillier decrypt 约 9.54 秒。带宽上，ElGamal 约 1.56 MB，约 11.95x overhead；Paillier 约 6.55 MB，约 50.18x overhead。证据锚点: §6.2.1 p11-p12。

Ethereum 合约 gas 在作者 2024-02-03 假设下为常数级: `serverSendsPubKey` 约 158,449/176,296 gas，`clientLocksPayment` 约 30,521 gas，`serverSendsSecKey` 约 73,692/82,475 gas，`withdrawPayment` 约 43,836 gas。这个指标不随数据大小增长，但链下 proving/verifying/bandwidth 仍是主要瓶颈。证据锚点: Table 2 p13。

### Multi-client FDE

多客户端场景下，同一服务器可能反复为多个 light clients 或 archival-data clients 提供同一数据。朴素做法需要为每个客户端重做 encryption/proof；论文提出 MC-VECK，把昂贵 proof 生成放入 preprocessing，在线阶段为每个客户端重随机化 key/ciphertexts，并用 DLEQ proof 证明重随机化正确。证据锚点: §7 p13-p14, Figure 7, Appendix D p20-p21。

安全上，论文引入 `L-bits zero-knowledge`: 已经付款拿到数据的客户端 Alice 若只给 Bob 少量 hint，不应帮助 Bob 在不向服务器获取 decryption key 的情况下学到额外数据；如果 Alice 直接把全部数据给 Bob，则已违背服务器作为数据服务方的设定。证据锚点: §7 p13, Definition D.1 p20。

### Danksharding/EIP-4844 应用

EIP-4844 让 blob data 在链上持久一段时间后过期，但 KZG commitment 会保留。过期后 validators 不再必须存 blob，archive nodes/full nodes 若自愿保存数据，就需要经济激励来服务请求。FDE 可以让用户公平地向这些节点购买 expired blob data。证据锚点: §1 p2, §8 p14。

在 Danksharding 中，数据经 Reed-Solomon erasure coding 分散到不同服务器/validators，客户端需要从多个服务器付费拿 fragments 和 accompanying proofs。论文认为 subset-opening FDE 可独立作用于多个服务器，客户端拿到足够 fragments 后重构原数据。证据锚点: §8 p14, Appendix A.3 p17。

### 限制与开放问题

- 带宽 overhead 仍大: 两个实现都至少约 10x overhead，作者提出可能通过 Paillier packing 或更小 VECK proof 改进。证据锚点: §8 p13。
- Server griefing: 恶意客户端可诱导服务器生成 ciphertext/proof 后不请求 key。作者建议分两段付款，先支付小额计算费，再为 decryption key 支付主费用。证据锚点: §8 p13-p14。
- 市场定价未实现: 附录设想多服务器/多客户端 marketplace，可用类似 constant-product market-making 机制自动定价，但只是 future direction。证据锚点: Appendix F p25。
- VECK 设计空间未穷尽: 可探索 FRI-based commitments、functional encryption 或 generic computation output exchange。证据锚点: Appendix F p25。

## 关键表格与数字

| 项目 | 论文数字 | 解释 |
| --- | --- | --- |
| 链上轮次 | 3 rounds | server ciphertext/proof -> client lock payment -> server reveal key |
| 链上通信 | 3 signatures, 1 verification key, 1 secret key | 大数据和 proof 链下 |
| ElGamal prover | 约 89s for 4096 BLS12-381 elements | range proofs/encryption dominates for large data |
| Paillier prover | 约 5.09s for 4096 BLS scalars | proof size linear; prover/verifier concrete faster |
| ElGamal bandwidth | 1.56 MB for 0.13 MB data, 11.95x overhead | k=8 split scalar |
| Paillier bandwidth | 6.55 MB for 0.13 MB data, 50.18x overhead | large modulus and linear proof |
| ElGamal verifier | 约 34.15s | dominated by split scalar encryption verification |
| Paillier verifier/decrypt | 约 19.45s / 9.54s | for 4096 ciphertexts |
| Ethereum gas | 30k-176k per contract function | constant in exchanged data size under authors' implementation |

## 论文贡献的可吸收结构

| 类型 | 内容 | 应进入哪里 | 是否新建节点 |
| --- | --- | --- | --- |
| research problem | fair exchange of payment for committed data | [[fair-data-exchange|Fair data exchange for committed data]] | yes |
| method family | VECK + blockchain payment/key-release | [[fair-data-exchange|Fair data exchange for committed data]] methods | no standalone yet |
| foundation/usage | KZG selective openings for committed data exchange | [[kzg-commitments|KZG commitments]] source extension | no |
| application | expired EIP-4844/Danksharding blob retrieval incentives | [[data-availability-and-light-clients|Data availability and light clients]] | no |
| bridge | KZG commitments enable FDE correctness proof and selective download | [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] | yes |
| open problem | bandwidth overhead, server griefing, pricing, alternative commitments | fair-data-exchange gaps | no |

## 术语表

| Term | 本文含义 | Nahida 处理 |
| --- | --- | --- |
| Fair Data Exchange (FDE) | 客户端收到承诺下数据 iff 服务器收到付款的协议问题 | L3 topic seed |
| VECK | verifiable encryption under committed key，证明密文加密了承诺数据的函数输出，且 key 可链上验证 | 方法路线，暂不作为基础节点 |
| Verct | 客户端验证 ciphertext/proof 与 commitment 和 vk 一致 | source-local protocol detail |
| Verkey | 链上或 TTP 验证 secret key 与 vk 匹配 | source-local protocol detail |
| KZG commitments | 对 polynomial evaluations 的 succinct commitment/opening | existing knowledge node |
| adaptor signatures | Bitcoin 上实现 key/payment atomicity 的签名机制 | source-local + future bridge candidate |
| MC-VECK | multi-client VECK，通过 preprocessing amortize server work | source-local extension |

## 关系与证据

| Claim/Relation | Evidence anchor | Confidence | Notes |
| --- | --- | --- | --- |
| FDE 解决的是 paid serving/access problem，而不是原始 storage proof | §1 p1-p2 | high | 关键分类纠偏 |
| VECK 将 FDE 降为 decryption-key-for-payment exchange | §3 p5-p6, §4 p6-p7 | high | 支撑 bridge |
| KZG 是本文主 commitment backend，并支持 subset exchange | §1 p2, §5.2 p9-p10 | high | KZG source extension |
| Ethereum on-chain cost constant in data size | §6.2.2 Table 2 | high | 只对作者实现成立 |
| Multi-client model amortizes prover work but不能防止完整数据再分发 | §7 p13-p14 | medium | 安全定义限制明确 |
| EIP-4844/Danksharding 应用是 expired/fragmented data retrieval incentives | §1 p2, §8 p14, Appendix A.3 | high | DA bridge/application |

## 知识库吸收计划

- Primary path: `blockchain-systems/data-availability-and-light-clients/fair-data-exchange`.
- Secondary path: `zero-knowledge-proofs/polynomial-commitments/kzg-commitments`.
- Bridge: `KZG commitments -> fair data exchange`.
- Parent updates: refresh data availability direction, DAS topic, KZG topic, blockchain-systems domain with source extension rows.
- Review/future: future queued ZKCPlus, SAVER, RC-S-P, BitStream/FairSwap-like sources should decide whether `verifiable-encryption` or `fair-exchange-protocols` deserves a broader foundation node.

## 查询入口

- 这篇论文解决的 FDE 问题是什么?
- VECK 与 verifiable encryption / SAVER / KZG 的关系是什么?
- 为什么本文适合 EIP-4844 或 Danksharding expired blob retrieval?
- ElGamal VECK 和 Paillier VECK 的性能取舍是什么?
- 如何在 Ethereum/Bitcoin 上实现 payment-for-key 原子性?
- Multi-client FDE 为什么需要 L-bits zero-knowledge?

## 局限与待复核

| Gap | 为什么重要 | 后续动作 |
| --- | --- | --- |
| 只有本文对 VECK 的直接定义，缺 SAVER/ZKCPlus/VE primary source 深读 | 决定是否拆出 `verifiable encryption` foundation node | 后续吸收 `2019-1270.pdf` 与 `3460120.3484558.pdf` |
| Danksharding/EIP-4844 只来自本文背景和引用，缺官方/基础 source | 避免把应用场景误当成已完整覆盖的 DA foundation | 后续 foundation/research search 或吸收 DA papers |
| 代码仓库未做 repo analysis | source note 只覆盖 paper implementation claims，不验证 repo 架构 | 可用 `nahida-github-repo-analyze` 分析 `PopcornPaws/fde` |
| 市场定价与 server reputation 是设想 | 不应作为已验证机制写入 evergreen knowledge | 保留为 fair-data-exchange open problem |
