---
id: "nahida-knowledge-fair-data-exchange"
title: "Fair data exchange for committed data"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "fair-data-exchange"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
parent_knowledge_refs:
  - "nahida-knowledge-data-availability-and-light-clients"
  - "nahida-knowledge-blockchain-fair-exchange-protocols"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "fair-data-exchange"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
relation_edges:
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-fair-exchange-protocols"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/fair-exchange-protocols.md"
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "is_a"
    to: "nahida-knowledge-data-availability-and-light-clients"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fair-data-exchange.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-fair-exchange-protocols.md"
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "depends_on"
    to: "nahida-knowledge-kzg-commitments"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
      - "vault/05_Bridges/kzg-commitments-to-fair-data-exchange.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "applies_to"
    to: "nahida-knowledge-data-availability-sampling"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "bridges_to"
    to: "nahida-bridge-kzg-commitments-to-fair-data-exchange"
    evidence_refs:
      - "vault/05_Bridges/kzg-commitments-to-fair-data-exchange.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "depends_on"
    to: "nahida-knowledge-verifiable-encryption"
    evidence_refs:
      - "vault/05_Bridges/verifiable-encryption-to-fair-data-exchange.md"
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "bridges_to"
    to: "nahida-bridge-verifiable-encryption-to-fair-data-exchange"
    evidence_refs:
      - "vault/05_Bridges/verifiable-encryption-to-fair-data-exchange.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-fair-data-exchange"
    relation: "adjacent_to"
    to: "nahida-knowledge-contingent-service-payments"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments.md"
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
  - "nahida-bridge-kzg-commitments-to-fair-data-exchange"
  - "nahida-bridge-verifiable-encryption-to-fair-data-exchange"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
  - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
representative_source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
query_keys:
  - "Fair data exchange"
  - "FDE"
  - "fair exchange of committed data"
  - "atomic data exchange"
  - "payment for data availability retrieval"
  - "VECK"
  - "verifiable encryption under committed key"
  - "verifiable encryption"
  - "SAVER"
  - "ZKCPlus"
  - "ZKCP"
  - "proof of retrievability payment"
  - "RC-PoR-P"
aliases:
  - "FDE"
  - "blockchain fair data exchange"
  - "atomic and fair data exchange"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
topics:
  - "fair-data-exchange"
  - "fair-exchange-protocols"
  - "data-availability-service-incentives"
  - "proofs-of-retrievability"
  - "kzg-commitments"
  - "verifiable-encryption"
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
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "arxiv:2208.00283v2"
confidence: "high"
trust_tier: "primary"
---

# Fair data exchange for committed data

## 定义与范围

- 定义: Fair data exchange for committed data 研究在客户端只持有数据承诺、服务器持有完整或部分数据时，如何让“客户端收到承诺下正确数据”和“服务器收到付款”原子地绑定。它现在作为 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] 的 DA/committed-data 子问题维护。
- 不包含: 单个实现、某篇论文的局部公式、具体 smart contract 函数、某个数据市场的价格策略；这些留在 source note 或 source extension。
- Canonical terms: `fair data exchange`, `blockchain Fair Data Exchange`, `FDE`
- Aliases/query keys: FDE, atomic data exchange, fair exchange of committed data, payment for committed data, VECK。
- Standalone completeness check: 本节点解释问题、背景、方法路线、代表 source、与 DA/KZG 的关系和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“如何公平付费下载链下/过期 blob 数据”“VECK 在区块链里解决什么问题”“data availability 服务激励”时先读本节点。
- Update scope: 后续 FairSwap/FileBounty/FairDownload/RC-S-P/BitStream 等 source 深读后应刷新本节点；更广的 fair-exchange landscape 已拆到 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]]，本节点保持 committed-data / DA retrieval 子问题范围。
- Domain dynamics note: not_applicable

## 背景

区块链和去中心化存储常能激励“存储数据”或“把承诺写入链上”，但客户端真正需要的是在请求时取回数据。Proof-of-retrievability 或 proof-of-replication 可以证明存储状态，却不直接让服务器因每次下载服务得到报酬，也不能阻止服务器在需要访问时拒绝服务。

FDE 把区块链当作透明可信第三方来托管付款，但不把大数据写入链上。关键结构是: 数据和正确性证明链下传输，链上只执行 payment/key-release 逻辑。这样，区块链保证原子性，密码证明保证客户端在付款前能确信 ciphertext 解密后对应承诺数据。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它不是只描述 2024/418 一篇论文，而是组织 committed data serving、fair exchange、DA retrieval incentives、payment-for-key atomicity、verifiable encryption 等未来来源。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 当前只有一篇主 source，因此状态是 `active_seed`；具体 VECK 构造、Solidity 函数、benchmark 留在 source note。
- 需要引用的更基础 Knowledge: [[data-availability-and-light-clients|Data availability and light clients]], [[kzg-commitments|KZG commitments]]。
- 不应拆出的实例/协议/来源: VECK、FDE-ElGamal、FDE-Paillier、PopcornPaws/fde 暂作为 source-local method/source extension；除非后续多来源证明它们成为独立方法族。

## 解决的问题

已承诺数据的服务方如何在不信任客户端的情况下收款，客户端又如何在不信任服务方的情况下确认将得到正确数据。更具体地:

- 客户端先持有短承诺 `com` 或 KZG commitment，而不想把完整数据放上链验证。
- 服务器持有数据或数据片段，并希望按下载/服务次数获得报酬。
- 区块链可以可靠托管 payment，但链上存储和计算昂贵。
- 协议必须同时保证 client-fairness 与 server-fairness。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[data-availability-and-light-clients|Data availability and light clients]] | child_of | FDE directly targets availability service/retrieval incentives for committed data | active_seed |
| [[blockchain-systems|Blockchain systems]] | domain | blockchain provides transparent payment/key-release environment | active_seed |
| [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] | parent/problem family | ZKCPlus and FDE together show broader fair-exchange landscape; FDE is the committed-data/DA specialization | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[verifiable-encryption|Verifiable encryption]] | method_family / adjacent dependency | VE/VECK/SAVER 已形成独立 cryptographic primitive/method-family seed；本节点只引用它解释 ciphertext correctness，不把 payment fairness 归给 VE。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]]; [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | active_seed |
| `payment-for-key atomicity` | mechanism candidate | Ethereum contract/adaptor signature route 可能跨多个 fair-exchange protocol 重复出现 | 本 source + future Bitcoin/ZKCP sources | candidate |
| `data-availability-service-markets` | application/problem candidate | expired blob、archival data、data market pricing 可能需要独立应用节点 | 本 source 的 EIP-4844/Danksharding 应用 | candidate |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| On-chain data verification strawman | 把数据发到合约，合约验证数据匹配承诺后付款。 | 数据很小或链上计算/存储成本可接受。 | 对大数据不可行；链上存储昂贵，交互和延迟增加。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| VECK + payment/key release | 服务器链下发送 ciphertext/proof；客户端验证后锁款；服务器链上揭示 decryption key 才能收款；客户端读 key 解密。 | 客户端持有 committed data 的承诺，且链上可验证 key 与 vk 匹配。 | 链下 proving/verifying/bandwidth 仍重；server griefing 需经济缓解。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| KZG selective-opening FDE | 将数据视为 polynomial evaluations，用 KZG commitment 和 subset opening VECK 支持只购买部分数据。 | 数据承诺基于 KZG 或可转成 vector/polynomial commitment。 | 依赖 SRS/pairing assumptions；实现细节与 commitment backend 绑定。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| Bitcoin adaptor-signature FDE | 用 adaptor signature 把 payment transaction 的完整签名和 decryption key 绑定。 | 无 Turing-complete smart contract，但支持足够脚本和 adaptor signature flow。 | 需要处理 timelock、mempool/finalization 和双签防抢跑。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| Multi-client VECK | 预处理昂贵 proof/ciphertexts，在线为每个客户端重随机化 key，amortize server work。 | 多个客户端反复请求同一 committed data。 | 不能阻止客户端直接再分发完整数据；只处理短 hint/secret-key 绕过支付。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| Generic verifiable-encryption layer | 将 ciphertext/plaintext consistency 和 relation proof 作为独立 cryptographic primitive 处理，再由 FDE 协议添加 payment/key-release。 | 需要解释 VECK/SAVER/ZKCPlus 等来源与 FDE 的分层关系。 | SAVER 不是 fair-exchange protocol；VE 只提供密文正确性/可验证解密，不提供付款公平性。 | [[verifiable-encryption|Verifiable encryption]]; [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] |
| ZKCPlus-style CP proof-before-payment | 先承诺数字商品，再用 CP-NIZK 验证 predicate 和 encrypted delivery，链上只处理 lock/reveal/finalize。 | 一般数字商品、模型或查询结果；需要多个 proof phases 引用同一隐藏对象。 | 不是 KZG/DA-specific FDE；committed-data retrieval 细节仍以 Atomic/FDE 为主。 | [[fair-exchange-protocols|Blockchain-based fair exchange protocols]]; [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] |
| PoR service-payment contrast | Proof-of-retrievability 证明服务器持续保存/可取回数据；RC-PoR-P 用 recurring payment 和 dispute attribution 为这种服务付款。 | 付费对象是“存储可取回性证明”而不是直接下载 committed data。 | 与 FDE 相邻但不同: FDE 买数据访问/key release，RC-PoR-P 买服务证明并处理 proof-status privacy。 | [[contingent-service-payments|Contingent service payments for verifiable services]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 创建本节点 seed；形式化 FDE、定义 VECK、给出 Ethereum/Bitcoin 协议、ElGamal/Paillier constructions、multi-client model 和 implementation benchmarks | 单一 source；VECK/fair exchange foundation 仍薄；代码仓库未单独分析；pricing/reputation 是 future direction | `p1-p25` |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization]] | paper | 作为 adjacent VE foundation seed：说明 verifiable encryption 如何证明 encrypted plaintext properties，并帮助界定 FDE 中 VECK 的 cryptographic layer | 不是 FDE 协议；没有 payment/key-release/fairness phase，细节留在 [[verifiable-encryption|Verifiable encryption]] | `p1-p44` |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange]] | paper | 作为 broader fair-exchange comparison source：ZKCP/ZKCPlus route 用 CP-NIZK proof-of-delivery 支撑一般数字商品交换 | 不是 committed-data/KZG-specific FDE source；细节通过 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] 和 [[commit-and-prove-arguments|Commit-and-prove arguments]] 路由 | `p1-p20` |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | paper | 作为 PoR/service-payment comparison source：说明 PoR 证明存储状态可以进入 recurring payment，但不是 FDE 的 data/key release route | 不是 committed-data retrieval 协议；细节通过 [[contingent-service-payments|Contingent service payments for verifiable services]] 路由 | `p1-p15`, Appendix E-L |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: FDE 是 data availability/light-client 方向里的“服务访问激励”问题，而不是 DAS 的抽样算法本身。2024/418 的核心贡献是把 committed data 的正确性检查放到 VECK 里，把大数据传输放到链下，把链上工作压缩为 payment/key-release 原子性。SAVER 新增了 generic verifiable-encryption 视角，说明 VECK 应被看作 [[verifiable-encryption|Verifiable encryption]] 的 commitment-specific/fair-exchange variant，而不是 FDE 节点里未定义的孤立术语。ZKCPlus 则把更广的 ZKCP-style fair exchange 抽出来：它证明一般数字商品的 predicate 和 encrypted delivery，但不是 KZG/DA-specific retrieval 协议。RC-S-P/RC-PoR-P 进一步界定了 FDE 的相邻边界: PoR 可以证明存储可取回性并作为 recurring service payment 的对象，但 FDE 的核心仍是 committed data retrieval / key release，不应把所有 PoR 服务付款都塞进本节点。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | 新增 FDE topic seed：client/server fairness, VECK, Ethereum/Bitcoin payment-key release, multi-client preprocessing, Danksharding expired data retrieval | 定义与范围; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 ZKCPlus/RC-S-P/FairSwap-like sources 时判断是否拆出更广 fair-exchange 节点 |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | 补充 adjacent cryptographic layer：SAVER 支持 `verifiable-encryption` 独立成节点，并界定 VE 与 FDE 的边界 | 下级结构; 方法族; 当前综合; Bridge Links; 缺口与队列 | yes | 用 [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] 维护边界；SAVER 不作为 FDE 协议代表 |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | 把 broader fair-exchange landscape 从 DA-specific FDE 中拆出；ZKCPlus 作为 comparison/application source，不替代 Atomic/FDE 的 committed-data route。 | 定义与范围; 上层位置; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续 FairSwap/ZKCP direct sources refresh [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | 补充 PoR/service-payment adjacency：PoR 证明和 recurring payment 属于 service-payment 子问题，不替代 committed-data FDE route。 | 方法族; 代表 Sources; 当前综合; 关系图谱 | no | 通过 [[contingent-service-payments|Contingent service payments for verifiable services]] 维护 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application, cryptographic_enabler | KZG commitment/opening supports committed-data correctness and subset retrieval; it does not by itself provide payment fairness or market incentives. | active_seed |
| [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] | `zero-knowledge-proofs/proof-systems/verifiable-encryption; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application, payment_protocol_enabler | VE/VECK supplies ciphertext correctness and verifiable decryption; blockchain/adaptor-signature layer supplies payment/key-release fairness. | active_seed |
| [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; blockchain-systems/execution-and-transactions/fair-exchange-protocols` | dependency, application, proof_protocol_enabler | CP-NIZK transfers predicate/delivery consistency; FDE-specific DA retrieval and KZG/VECK constructions remain separate. | active_seed |
| [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]] | `verifiable-computation/verifiable-computation-systems; blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | adjacent_dependency | PoR/VC proof validity can support service-payment protocols; it is adjacent to FDE but does not replace committed-data/key-release fairness. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-fair-data-exchange | is_a | nahida-knowledge-data-availability-and-light-clients | FDE source note and parent direction | high | active_seed |
| nahida-knowledge-fair-data-exchange | is_a | nahida-knowledge-blockchain-fair-exchange-protocols | ZKCPlus and FDE show broad parent plus DA specialization | medium | active_seed |
| nahida-knowledge-fair-data-exchange | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | source note | high | active_seed |
| nahida-knowledge-fair-data-exchange | depends_on | nahida-knowledge-kzg-commitments | source note; bridge note | high | active_seed |
| nahida-knowledge-fair-data-exchange | applies_to | nahida-knowledge-data-availability-sampling | EIP-4844/Danksharding application sections | medium | active_seed |
| nahida-knowledge-fair-data-exchange | bridges_to | nahida-bridge-kzg-commitments-to-fair-data-exchange | bridge note | high | active_seed |
| nahida-knowledge-fair-data-exchange | depends_on | nahida-knowledge-verifiable-encryption | FDE source note; SAVER source note; bridge note | medium | active_seed |
| nahida-knowledge-fair-data-exchange | bridges_to | nahida-bridge-verifiable-encryption-to-fair-data-exchange | bridge note | medium | active_seed |
| nahida-knowledge-fair-data-exchange | bridges_to | nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols | bridge note | medium | active_seed |
| nahida-knowledge-fair-data-exchange | adjacent_to | nahida-knowledge-contingent-service-payments | RC-PoR-P PoR/service-payment contrast | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| ZKCP、FairSwap/FairDownload/FileBounty 缺 source note 或未吸收。 | ZKCPlus 已触发 broader fair-exchange parent，但 strong/weak fairness、dispute route 和 original ZKCP 仍需直接来源。 | nahida-update | high | queued |
| EIP-4844/Danksharding 官方或 foundation source 缺。 | 当前只从 FDE/FRIDA/LazyLedger 侧理解 DA 应用，不能做完整 DA 综述。 | nahida-research-search or nahida-update | medium | queued |
| `PopcornPaws/fde` repo 未分析。 | 论文声称开源实现，但知识库没有实现架构、合约/API、benchmark reproduction note。 | nahida-github-repo-analyze | medium | queued |
| 服务定价、server griefing、声誉/市场机制未验证。 | 影响 FDE 作为真实 data market primitive 的落地判断。 | nahida-research-search or future source absorption | medium | watching |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Created fair-data-exchange topic under data-availability/light-clients from 2024/418. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Promoted verifiable encryption from candidate to adjacent method-family dependency and recorded SAVER boundary. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Linked FDE as DA-specific child under broader blockchain fair exchange and added ZKCPlus comparison boundary. | doi:10.1145/3460120.3484558 | codex |
| 2026-06-23 | nahida-knowledge-20260623-recurring-contingent-service-payment | Added RC-PoR-P as adjacent PoR/service-payment contrast without changing committed-data FDE scope. | arxiv:2208.00283v2 | codex |
