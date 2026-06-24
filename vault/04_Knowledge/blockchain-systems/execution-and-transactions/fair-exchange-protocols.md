---
id: "nahida-knowledge-blockchain-fair-exchange-protocols"
title: "Blockchain-based fair exchange protocols"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "fair-exchange-protocols"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-execution-and-transactions"
child_knowledge_refs:
  - "nahida-knowledge-fair-data-exchange"
  - "nahida-knowledge-contingent-service-payments"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "fair-exchange-protocols"
primary_ontology_path: "blockchain-systems/execution-and-transactions/fair-exchange-protocols"
secondary_ontology_paths:
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
relation_edges:
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-execution-and-transactions"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/fair-exchange-protocols.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "has_child"
    to: "nahida-knowledge-fair-data-exchange"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fair-data-exchange.md"
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "has_child"
    to: "nahida-knowledge-contingent-service-payments"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments.md"
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "depends_on"
    to: "nahida-knowledge-commit-and-prove-arguments"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
      - "vault/05_Bridges/commit-and-prove-arguments-to-fair-exchange-protocols.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-fair-exchange-protocols"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
  - "nahida-bridge-verifiable-encryption-to-fair-data-exchange"
  - "nahida-bridge-verifiable-computation-systems-to-contingent-service-payments"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
representative_source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "arxiv:2208.00283v2"
query_keys:
  - "blockchain fair exchange"
  - "fair exchange protocols"
  - "Zero-Knowledge Contingent Payment"
  - "ZKCP"
  - "ZKCPlus"
  - "FairSwap"
  - "payment for digital goods"
  - "contingent service payment"
  - "recurring contingent service payment"
  - "RC-S-P"
  - "RC-PoR-P"
aliases:
  - "Blockchain fair exchange"
  - "ZKCP-style fair exchange"
  - "trustless digital-goods exchange"
  - "service-payment fair exchange"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
topics:
  - "fair-exchange-protocols"
  - "zero-knowledge-contingent-payment"
  - "fair-data-exchange"
  - "contingent-service-payments"
  - "commit-and-prove-arguments"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-21"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "arxiv:2208.00283v2"
confidence: "medium"
trust_tier: "primary"
---

# Blockchain-based fair exchange protocols

## 定义与范围

- 定义: Blockchain-based fair exchange protocols 研究如何用区块链脚本、smart contract、transaction lock 或 adaptor-signature 类机制，让不互信双方公平交换数字商品、服务结果或数据访问权与付款。
- 不包含: 普通支付系统、单个数据市场价格策略、某个 smart contract API、某篇论文的完整协议转录、proof-system 内部代数证明；这些分别留在 source note、应用节点或 proof-system 节点。
- Canonical terms: `fair exchange`, `Zero-Knowledge Contingent Payment`, `ZKCP`, `ZKCPlus`, `blockchain fair exchange`.
- Retrieval role: 查询 ZKCP/ZKCPlus/FairSwap/FDE/RC-S-P/“买数据或服务怎么公平付款”时，先读本节点，再按问题转到 [[fair-data-exchange|Fair data exchange for committed data]]、[[contingent-service-payments|Contingent service payments for verifiable services]] 或 [[commit-and-prove-arguments|Commit-and-prove arguments]]。
- Update scope: 新 source 若涉及 ZKCP、ZKCPlus、FairSwap、FileBounty、FairDownload、ZKCSP、recurring contingent service payment、cross-chain deal 或 data-sale fairness，应刷新本节点。

## 背景

传统公平交换需要可信第三方，否则强公平性通常不可达。区块链给出的替代方式是让交易锁、时间锁、合约状态或 adaptor signature 承担公开仲裁角色: 大数据和证明仍在链下传输，链上只处理付款、退款和锁的最终检查。

这类协议通常有两个子问题:

- 信息正确性: 买方在付款前如何确信将得到满足谓词的数据、服务或解密能力。
- 付款原子性: 卖方如何在释放 key/opening/proof 后获得付款，买方如何在失败或超时后退款。

ZKCPlus 的贡献在于把信息正确性部分组织成 commit-first 的 CP-NIZK 流程；Atomic/FDE 则把这一问题具体化为 committed data retrieval / DA 服务激励。RC-S-P 补上另一条服务型路线: 当交易对象不是静态商品而是周期性 verifiable service proof 时，协议还必须处理 malicious client、proof-status privacy 和 dispute attribution。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它横跨 ZKCP/ZKCPlus、FairSwap-like dispute routes、committed-data FDE、ZKCSP 和 future data/service payment sources；不是 ZKCPlus 这一篇的标题页。
- 为什么不是单篇 source: 当前至少有 ZKCPlus 和 Atomic/FDE 两个已吸收 source，并且队列/已有 notes 多次将 ZKCP/FairSwap/FileBounty/FairDownload 列为待补 landscape。
- 需要引用的更基础 Knowledge: [[execution-and-transactions|Blockchain execution and transactions]], [[commit-and-prove-arguments|Commit-and-prove arguments]], [[verifiable-encryption|Verifiable encryption]]。
- 不应拆出的实例/协议/来源: ZKCPlus、ZKCP、FairSwap、VECK、FDE-ElGamal、FDE-Paillier 默认作为 source extension 或 future source candidates；除非多来源查询证明需要 protocol-instance index。

## 解决的问题

让一方在不信任对方的情况下购买数字商品、数据子集、模型参数、查询结果或服务证明，并同时避免:

- 买方付款后拿不到正确数据或 key；
- 卖方先发数据后收不到钱；
- 链上存储/验证完整数据导致成本不可接受；
- proof 或 dispute 成本随数据规模不可扩展；
- 买方用验证过程提前学习商品内容。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[execution-and-transactions|Blockchain execution and transactions]] | child_of | fair exchange depends on transaction locks, contract finalize/refund and payment-state transitions | active_seed |
| [[blockchain-systems|Blockchain systems]] | domain | blockchain replaces centralized fair-exchange arbiter with public settlement | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[fair-data-exchange|Fair data exchange for committed data]] | problem / application subproblem | committed DA retrieval/data-service payment has KZG/VECK and DA-specific assumptions, so it should stay specialized. | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | active_seed |
| `ZKCP/ZKCPlus-style proof-validated exchange` | method section | ZKCPlus deep-read source gives enough detail for a route, but original ZKCP source itself is not yet deeply read. | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | keep_section |
| `dispute-based fair exchange` | method candidate | ZKCPlus related work mentions FairSwap as proof-of-misbehavior route; direct FairSwap source is missing. | ZKCPlus related work only | review |
| [[contingent-service-payments|Contingent service payments for verifiable services]] | subproblem | ZKCSP/RC-S-P/RC-PoR-P 需要处理服务证明、重复付款、proof-status privacy 和 malicious-client free-riding，已经不是普通数字商品交换的一行方法。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| ZKCP-style proof before payment | 卖方先给出 ciphertext、lock 和 ZK proof，买方验证后锁款；卖方揭示 key/opening 才能收款。 | 买方能用谓词定义“合格商品”，商品可加密交付。 | 原始 ZKCP 的 trusted setup、seller proving 和 large predicate 支持较弱。 | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] |
| ZKCPlus commit/validate/deliver split | 先承诺商品，再分别证明 predicate validity 和 encrypted delivery，多个 predicate 可组合。 | 大数据、模型、SQL 查询或需要多轮验证的数字商品。 | 证明和通信仍在链下；买方验证质量取决于 predicate/test design。 | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] |
| Commitment lock instead of hash lock | 链上验证 key commitment opening，减少 hash circuit/proof 与链上 lock 的不匹配。 | 链支持 Pedersen commitment opening 或等价曲线操作。 | 依赖 commitment binding/hiding；不解决 censorship、timeout 或 data redistribution。 | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] |
| Dispute / proof-of-misbehavior route | 买方被欺骗时提交 misbehavior proof 恢复公平。 | 希望减少 upfront ZK proving，且能接受 dispute phase。 | 公平性更弱；链上争议成本可能随 proof size 增长。 | ZKCPlus related work mentions FairSwap; direct source pending |
| Committed-data FDE | 客户端持有数据承诺，服务器链下提供 ciphertext/proof，链上做 payment/key-release。 | DA/archive data retrieval, KZG commitments, data-service markets. | 是 fair exchange 的 committed-data 子问题，不覆盖 CNN/SQL/model-sale 一般场景。 | [[fair-data-exchange|Fair data exchange for committed data]] |
| Recurring contingent service payment | 用 VSID/SAP/private time bubble/masked deposits 让可验证服务按周期结算，并在争议时识别客户端或服务器作恶。 | PoR、verifiable computation、searchable encryption 等服务证明可被验证且需要重复收费。 | 通用版本引入 arbiter、更多链上消息和更高 deposit；PoR 实例可用 Merkle proof-of-misbehavior 降低争议成本。 | [[contingent-service-payments|Contingent service payments for verifiable services]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | paper | 创建本节点；把 ZKCP 改成 commit-first、CP-NIZK-based、支持大规模 predicate 的 fair-exchange route。 | 原始 ZKCP/FairSwap 直接来源未深读；implementation repo 未分析。 | p1-p20 |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 提供 committed-data/FDE 子问题: DA/archival data retrieval 的 payment-for-key fairness。 | 专注 committed data/KZG/VECK；不是通用数字商品 fair exchange。 | p1-p25 |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | paper | 把 service-payment variants 升级为子问题；定义 RC-S-P，指出 zkCSP free-riding/privacy 问题，并给出 RC-PoR-P。 | PoR foundation、ZKCSP original 和 FairSwap original 仍需补源。 | p1-p15; Appendix E-L |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，覆盖当前 vault 已吸收 source。
- Freshness: `fresh` for current-vault synthesis; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: Fair exchange protocol 是 blockchain execution/transaction 层上的应用协议问题: 区块链保证结算/退款的公共状态，proof/encryption/commitment 层保证买方在付款前能验证将得到的对象。ZKCPlus 把 ZKCP 改成以 commitment 为中心的 validate/deliver 分层，适合复杂 predicate 和大规模数据；Atomic/FDE 则把同一公平交换思想落到 committed data / DA retrieval 服务激励上。RC-S-P 进一步说明 fair exchange 还有服务型子问题: 当对象是 recurring verifiable service 而非静态商品时，协议需要防 proof-status leakage、deposit amount leakage 和 malicious-client free-riding。三者共同说明 fair exchange 不应只挂在 DA 节点下；DA/FDE 和 contingent service payments 是两个需要分别维护的子问题。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | 新增 broader fair-exchange parent；记录 ZKCP limitation、commit-first protocol、CP-NIZK proof-of-delivery、CNN/SQL applications。 | 定义与范围; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 继续吸收 ZKCP/FairSwap/FileBounty/FairDownload 对照来源 |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | 从 DA-specific `fair-data-exchange` 子问题连接到 broader fair exchange landscape。 | 下级结构; 代表 Sources; 当前综合 | yes | 保持 DA/FDE 细节在 [[fair-data-exchange|Fair data exchange for committed data]] |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | 将 service-payment variants 从 watching 升级为 [[contingent-service-payments|Contingent service payments for verifiable services]]；补入 malicious-client、proof-status privacy、VSID/SAP 和 RC-PoR-P。 | 定义与范围; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 补 ZKCSP/FairSwap/PoR direct sources，判断是否拆 PoR payments |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; blockchain-systems/execution-and-transactions/fair-exchange-protocols` | dependency, application, proof_protocol_enabler | CP-NIZK transfers relation proof over committed data; payment fairness, timeout/refund and market semantics remain fair-exchange protocol responsibilities. | active_seed |
| [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] | `zero-knowledge-proofs/proof-systems/verifiable-encryption; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application | VE/VECK explains ciphertext correctness for committed data; broad fair exchange still needs transaction lock and application predicates. | active_seed |
| [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]] | `verifiable-computation/verifiable-computation-systems; blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | dependency, application, payment_finality_boundary | VS/VC/PoR supplies service correctness; smart contracts supply escrow, dispute economics, privacy window and final coin distribution. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-fair-exchange-protocols | is_a | nahida-knowledge-blockchain-execution-and-transactions | fair exchange depends on transaction/contract state | high | active_seed |
| nahida-knowledge-blockchain-fair-exchange-protocols | has_child | nahida-knowledge-fair-data-exchange | Atomic/FDE source and DA-specific child | medium | active_seed |
| nahida-knowledge-blockchain-fair-exchange-protocols | has_child | nahida-knowledge-contingent-service-payments | RC-S-P source and service-payment child | high | active_seed |
| nahida-knowledge-blockchain-fair-exchange-protocols | depends_on | nahida-knowledge-commit-and-prove-arguments | ZKCPlus CP-NIZK route | high | active_seed |
| nahida-knowledge-blockchain-fair-exchange-protocols | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md | ZKCPlus source note | high | active_seed |
| nahida-knowledge-blockchain-fair-exchange-protocols | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | FDE source note | medium | active_seed |
| nahida-knowledge-blockchain-fair-exchange-protocols | evidenced_by | vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md | RC-S-P source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Original ZKCP/FairSwap/FileBounty/FairDownload/FairDAG-like direct sources 缺。 | 目前 landscape 主要由 ZKCPlus related work 和 FDE comparison 支撑，不能完整比较 strong vs weak fairness。 | nahida-update or nahida-research-search | high | queued |
| ZKCSP original / RC-S-P follow-up / PoR payment sources 仍薄。 | RC-S-P 已给出服务付款 seed，但 zkCSP、outsourced fair PoR、FairSwap-for-service 仍需 direct sources 校准 landscape。 | continue paper intake / nahida-research-search | high | queued |
| Implementation/repo evidence 缺。 | 需要确认 contract/API/node architecture、gas measurement and reproducibility。 | nahida-github-repo-analyze | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Created broader blockchain fair-exchange problem node and attached ZKCPlus + FDE as source extensions. | 2 source notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-recurring-contingent-service-payment | Promoted contingent service payments as child problem and attached RC-S-P / RC-PoR-P route. | arxiv:2208.00283v2 | codex |
