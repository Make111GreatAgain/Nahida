---
id: "nahida-knowledge-verifiable-encryption"
title: "Verifiable encryption"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "verifiable-encryption"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "verifiable-encryption"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/verifiable-encryption"
secondary_ontology_paths:
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols"
relation_edges:
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/verifiable-encryption.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
      - "vault/05_Bridges/zk-snarks-to-verifiable-encryption.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "applies_to"
    to: "nahida-knowledge-fair-data-exchange"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
      - "vault/05_Bridges/verifiable-encryption-to-fair-data-exchange.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-verifiable-encryption"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-verifiable-encryption.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-verifiable-encryption"
    relation: "bridges_to"
    to: "nahida-bridge-verifiable-encryption-to-fair-data-exchange"
    evidence_refs:
      - "vault/05_Bridges/verifiable-encryption-to-fair-data-exchange.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-verifiable-encryption"
  - "nahida-bridge-verifiable-encryption-to-fair-data-exchange"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
representative_source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
query_keys:
  - "Verifiable encryption"
  - "verifiable-encryption"
  - "可验证加密"
  - "SAVER"
  - "SNARK-friendly encryption"
  - "commit-carrying encryption"
  - "verifiable decryption"
  - "rerandomizable encryption"
  - "VECK"
  - "ZKCPlus"
  - "proof of delivery"
aliases:
  - "可验证加密"
  - "SNARK-friendly verifiable encryption"
  - "commit-carrying encryption"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "verifiable-encryption"
  - "fair-exchange-protocols"
  - "zk-snarks"
  - "fair-data-exchange"
  - "verifiable-decryption"
  - "rerandomization"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-21"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-21"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable encryption

## 定义与范围

- 定义: Verifiable encryption 是把公钥加密和证明系统组合起来的一类方法，使外部验证者能检查“密文中的明文满足某个关系”，同时明文仍保持加密。它不仅需要证明关系成立，还需要证明关系里的 witness 与 ciphertext 里的 plaintext 是同一个对象。
- 不包含: 普通加密、单个投票协议、单个 fair-exchange protocol、某篇论文的局部公式或具体密钥元素；这些留在 source note 或 source-extension 行里。
- Canonical terms: `verifiable encryption`, `verifiable decryption`, `commit-carrying encryption`, `SNARK-friendly encryption`
- Standalone completeness check: 本节点给出本地定义、问题、方法路线、代表 source、应用边界和 bridge；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“如何证明加密明文满足关系”“SAVER 和 zk-SNARKs 怎么连接”“VECK/SAVER/FDE 的关系”时优先读本节点。
- Update scope: 后续 ZKCP、FairSwap/FairDownload/FileBounty、通用 VE canonical sources 或更多 voting/fair-exchange source 深读后应刷新本节点；ZKCPlus 已作为 VE-adjacent proof-of-delivery source 吸收，但不把它误标成通用 VE construction。
- Domain dynamics note: not_applicable

## 背景

在许多 ZKP 应用里，数据既不能公开，又必须被验证其结构或合法性。最直接的做法是把 encryption algorithm 放进 SNARK circuit 中证明 ciphertext 生成正确，但这会把 pairing、hash、公钥加密或访问控制逻辑转换成大量约束，导致 proving time 和 CRS size 变大。

SAVER 提供的 source-backed seed 是: 让 ciphertext 暴露一个 commitment-compatible handle，并把 pairing-based SNARK verification equation 改成能接收 ciphertext-derived commitments。Atomic/Fair Data Exchange 里的 VECK 则提供另一个应用 seed: 对已承诺数据做可验证加密，使链上 payment/key-release 能围绕密文和 decryption key 原子化。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family` / `method_family`。
- 为什么足够通用: 它跨 SAVER、VECK/FDE、blockchain voting、ZKCPlus proof-of-delivery 边界和后续 ZKCP/FairSwap-like sources；未来 query 不应从单篇 SAVER 或 FDE note 反推整个 primitive。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: SAVER 是一种构造，VECK 是 FDE source 的 commitment-specific variant；它们都作为 representative source extension。
- 需要引用的更基础 Knowledge: [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]]。
- 不应拆出的实例/协议/来源: SAVER、Vote-SAVER、VECK、FDE-ElGamal、FDE-Paillier 默认作为 source-local construction/source extension。

## 解决的问题

Verifiable encryption 解决的是 proof/encryption composition 的一致性问题:

- 明文不能公开，但验证者需要知道它满足某个 public relation。
- 证明系统里的 witness 和 ciphertext 的 plaintext 必须绑定，不能证明 `m` 却加密另一个 `m'`。
- 加密算法本身可能很难或很贵地放入 SNARK circuit。
- 在某些应用里还需要 verifiable decryption、homomorphic aggregation 或 rerandomization。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|Proof systems]] | child_of | SAVER source note; proof-system composition problem | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on / application route | SAVER uses pairing-based zk-SNARK verification equation | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| `commit-carrying encryption` | method section | SAVER 定义的 commit-carrying encryption 是 VE 与 CP-SNARK 连接的关键接口，但目前主要来自一篇 source。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | keep_section |
| `verifiable decryption` | method section | 可公开验证解密结果，服务 tally 和 fair-exchange key-release 检查。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | keep_section |
| `VECK` | variant/source-local method | FDE 中的 verifiable encryption under committed key 与 KZG/commitment-specific fair exchange 绑定。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Encryption-in-circuit baseline | 把 encryption correctness 直接写入 SNARK relation。 | 加密算法简单，或 circuit/CRS/proving 成本可接受。 | 对复杂公钥加密、pairing/hash/access-policy operations 成本高。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| Commit-carrying encryption | ciphertext 可映射为同一明文的 commitment，让 proof system 证明 commitment 相关关系。 | proof system 支持 commit-and-prove / commitment-bearing relation。 | 需要专门构造 encryption/ciphertext format；普通 encryption 不自动满足。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| SNARK-friendly conjoined verification | 用 pairing-based SNARK verification equation 连接 ciphertext components 和 proof components，避免把 encryption 放进 circuit。 | Groth16-like/pairing-based setting，relation 在 setup 时固定或可 CP-SNARK 组合。 | 依赖具体 CRS/key elements、D-Poly/batch-PKE assumptions；不自动迁移到任意 SNARK。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| Verifiable decryption | 解密者给出短 proof，公众验证 plaintext 确实来自 ciphertext。 | 投票 tally、fair exchange key-release 或公开结算需要可审计解密。 | 不等于高吞吐大消息解密；SAVER 需要短 message blocks/discrete-log recovery。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| Rerandomizable encryption and proof | 第三方可重随机化 ciphertext/proof，隐藏原 prover/encryptor 关联。 | 匿名投票、mixing、抗 receipt/linkability 场景。 | 只处理 origin unlinkability；不解决身份注册、链上 board 或经济激励问题。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| VECK for committed data exchange | 证明 ciphertext 解密后对应已承诺数据/评估值，链上再做 payment/key-release。 | 客户端持有 commitment，服务器持有数据，且需要公平付费检索。 | payment fairness 来自链上/adaptor-signature layer，不来自 VE 本身；KZG-specific route 需单独分析。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| Proof of encrypted delivery via CP-NIZK | 证明 ciphertext 加密的是同一份已承诺数据，并把 key lock/opening 接到公平交换协议。 | ZKCP/ZKCPlus-style digital goods exchange where proof-before-payment is needed. | 这是 VE-adjacent proof/encryption consistency，不等同 SAVER-style generic verifiable encryption；payment fairness 仍由 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] 处理。 | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization]] | paper | 创建本节点 seed；给出 SNARK-friendly VE、commit-carrying encryption、verifiable decryption、rerandomization 和 Vote-SAVER application | 主要是 pairing-based/Groth16-like construction；canonical VE history/foundation sources 缺 | `p1-p44` |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 提供 VECK/FDE 应用 seed: verifiable encryption under committed key 支撑 committed-data fair exchange | VECK 是 FDE source-local variant；不等于完整 VE foundation | `§3`, `§5` |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange]] | paper | 提供 VE-adjacent proof-of-delivery route：CP-NIZK 证明 encrypted delivery 和 committed data 一致 | 不升级 generic VE foundation；主要通过 [[commit-and-prove-arguments|Commit-and-prove arguments]] 与 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] 路由 | `p7-p10` |

## 正反例约束

- 正确: 把 SAVER 作为 representative source，提取 `verifiable encryption` 作为可复用方法族。
- 正确: 在 fair-exchange 查询里说明 VE/VECK 只负责密文正确性，payment fairness 仍由区块链或 adaptor signature 协议提供。
- 错误: 创建一个上层 `SAVER` 概念页，让 future query 必须读论文才能理解 VE。
- 错误: 把 zk-SNARK soundness 直接等同于 encryption security、fairness 或 receipt-freeness。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-21`，覆盖 FDE source seed 和 SAVER source seed。
- Freshness: `fresh` for current-vault synthesis; not a latest-news claim.
- Valid until: `2026-07-21`。
- 综合: 当前 vault 可以把 `verifiable encryption` 从 FDE 的候选项升级为 `foundation_thin` 方法族。SAVER 证明 VE 可以作为 proof-system composition problem 来组织: ciphertext 需要携带可证明的 commitment-like handle，SNARK 需要绑定 encrypted plaintext 和 witness relation；FDE/VECK 则展示 VE 作为 fair exchange 的密码学子层，但 fairness 和 payment/key-release 不属于 VE 本身。ZKCPlus 新增了 proof-of-delivery 的相邻证据：CP-NIZK 也能证明 ciphertext 与 committed data/key lock 一致，但它更应作为 [[commit-and-prove-arguments|Commit-and-prove arguments]] 到 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] 的桥，而不是直接扩张 VE 的定义。后续需要 ZKCP/FairSwap-like sources 和通用 VE foundation sources 才能升级为 foundation-complete。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: ZKCP/FairSwap/FileBounty/FairDownload or canonical VE source absorption.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] | 新增 generic SNARK-friendly VE seed；证明 `verifiable-encryption` 值得独立成方法族节点 | 定义与范围; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 ZKCPlus/VE canonical sources 强化 foundation |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | 补充 VECK/FDE 应用边界: VE supports committed-data correctness but not payment fairness by itself | 方法族; Bridge Links; 缺口与队列 | yes | 通过 [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] 维护边界 |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | 补充 VE-adjacent proof-of-delivery 边界: CP-NIZK 可证明密文和已承诺商品一致，但 primary route 是 CP -> fair exchange bridge。 | 方法族; 代表 Sources; 当前综合; 缺口与队列 | no | 通过 [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] 维护边界 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/proof-systems/verifiable-encryption` | dependency, method_transfer, proof_encryption_composition | zk-SNARK succinctness/soundness transfers to relation proof; encryption privacy, homomorphism and rerandomization require separate construction/security. | active_seed |
| [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] | `zero-knowledge-proofs/proof-systems/verifiable-encryption; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application, payment_protocol_enabler | VE/VECK transfers ciphertext correctness; fair exchange still needs blockchain/adaptor-signature payment/key-release and commitment-specific construction. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-verifiable-encryption | is_a | nahida-knowledge-proof-systems | this node; proof-systems parent | high | active_seed |
| nahida-knowledge-verifiable-encryption | depends_on | nahida-knowledge-zk-snarks | SAVER source; bridge note | high | active_seed |
| nahida-knowledge-verifiable-encryption | applies_to | nahida-knowledge-fair-data-exchange | FDE source; bridge note | medium | active_seed |
| nahida-knowledge-verifiable-encryption | evidenced_by | vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md | SAVER source note | high | active_seed |
| nahida-knowledge-verifiable-encryption | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | FDE source note | medium | active_seed |
| nahida-knowledge-verifiable-encryption | bridges_to | nahida-bridge-zk-snarks-to-verifiable-encryption | bridge note | high | active_seed |
| nahida-knowledge-verifiable-encryption | bridges_to | nahida-bridge-verifiable-encryption-to-fair-data-exchange | bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Generic verifiable encryption canonical/foundation sources 缺。 | 当前 foundation 主要靠 SAVER + FDE/VECK 应用 seed，历史定义与通用 construction landscape 不完整。 | nahida-research-search or nahida-update | high | queued |
| ZKCP/FairSwap/FairDownload/FileBounty 缺 source note 或未吸收。 | 需要比较 fair-exchange protocol 如何使用 VE/commitment/payment layers；ZKCPlus 已吸收但主要路由到 CP/fair-exchange bridge。 | nahida-update | high | queued |
| Blockchain voting sources 缺。 | Vote-SAVER 是单一 application source，不能独立代表 voting protocol landscape。 | nahida-update or nahida-research-search | medium | queued |
| Non-pairing / transparent / PLONK/STARK-compatible VE route 缺。 | SAVER 主要是 pairing-based/Groth16-like route，迁移到其他 proof systems 需要新证据。 | nahida-research-search | medium | watching |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Created foundation-thin method-family node from SAVER and FDE/VECK context. | 2 source notes | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Added ZKCPlus as VE-adjacent proof-of-delivery boundary and routed primary relationship through CP/fair-exchange bridge. | doi:10.1145/3460120.3484558 | codex |
