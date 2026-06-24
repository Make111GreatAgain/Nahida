---
id: "nahida-knowledge-contingent-service-payments"
title: "Contingent service payments for verifiable services"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "subproblem"
file_slug: "contingent-service-payments"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-fair-exchange-protocols"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "fair-exchange-protocols"
  - "contingent-service-payments"
primary_ontology_path: "blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments"
secondary_ontology_paths:
  - "verifiable-computation/verifiable-computation-systems"
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange"
relation_edges:
  - from: "nahida-knowledge-contingent-service-payments"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-fair-exchange-protocols"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/fair-exchange-protocols.md"
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-contingent-service-payments"
    relation: "depends_on"
    to: "nahida-knowledge-verifiable-computation-systems"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
      - "vault/05_Bridges/verifiable-computation-systems-to-contingent-service-payments.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-contingent-service-payments"
    relation: "adjacent_to"
    to: "nahida-knowledge-fair-data-exchange"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fair-data-exchange.md"
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-contingent-service-payments"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-verifiable-computation-systems-to-contingent-service-payments"
  - "nahida-bridge-decentralized-storage-networks-to-contingent-service-payments"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
  - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
representative_source_refs:
  - "arxiv:2208.00283v2"
  - "arxiv:2208.09937"
query_keys:
  - "contingent service payment"
  - "recurring contingent service payment"
  - "RC-S-P"
  - "RC-PoR-P"
  - "proof of retrievability payment"
  - "verifiable service payment"
  - "ZKCSP free-riding"
  - "decentralized storage service payment"
  - "proof of storage payment"
aliases:
  - "Contingent service payment"
  - "Recurring contingent service payment"
  - "Fair exchange for verifiable services"
domains:
  - "blockchain-systems"
  - "verifiable-computation"
topics:
  - "contingent-service-payments"
  - "fair-exchange-protocols"
  - "verifiable-services"
  - "proofs-of-retrievability"
  - "decentralized-storage-networks"
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
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
  - "nahida-knowledge-20260623-incentive-compatible-decentralized-storage"
source_refs:
  - "arxiv:2208.00283v2"
  - "arxiv:2208.09937"
confidence: "high"
trust_tier: "primary"
---

# Contingent service payments for verifiable services

## 定义与范围

- 定义: Contingent service payments for verifiable services 研究如何让客户端为可验证服务的周期性证明付款: 服务器只有在提供有效服务证明时才能收款，客户端只有在证明无效或自身输入无效被识别时才会退款/受罚。
- 不包含: 普通文件购买、一次性数字商品交换、单个 PoR 协议细节、某篇论文的完整概率实验；这些分别留在 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]]、source note 或未来 PoR foundation 节点。
- Canonical terms: `contingent service payment`, `recurring contingent service payment`, `RC-S-P`, `RC-PoR-P`, `ZKCSP`.
- Standalone completeness check: 本节点解释服务付款问题、威胁模型、方法路线、来源和与 VC/PoR/FDE 的边界；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“为 PoR/VC 服务按次付款”“zkCSP 为什么会被 free-riding”“RC-S-P/RC-PoR-P 属于哪里”时先读本节点，再打开 source note。
- Update scope: 后续吸收 ZKCSP、outsourced fair PoR、FileBounty、FairSwap-for-service、verifiable service payment 或 recurring service-market sources 时刷新本节点。

## 背景

Blockchain fair exchange 最常见的表述是“买方用链上锁款换取卖方的数字商品或解密 key”。Contingent service payment 把对象换成服务证明: 客户端不是购买一个静态文件，而是持续购买存储可取回性、可验证计算、可搜索加密查询或信息检索等服务。

这会引入两个额外问题。第一，服务证明失败本身可能泄露服务器状态，不能立刻把 proof status 暴露到链上。第二，客户端也有作恶激励，可能用无效 metadata 或 query 让诚实服务器生成失败证明，再利用失败结果拒绝付款。

## 基础概念判断

- 是否是基础概念/方向/问题: `subproblem` under blockchain fair exchange。
- 为什么足够通用: 它覆盖 ZKCSP、RC-S-P、RC-PoR-P、PoR/VC/searchable-encryption payment 等一类问题，不是 RC-S-P 这一篇的标题。
- 为什么不是单篇 source: Parent node 已提前把 service-payment variants 作为候选；本篇补足定义、攻击、通用协议和 PoR 实例，足以把候选升级为 active seed。
- 需要引用的更基础 Knowledge: [[fair-exchange-protocols|Blockchain-based fair exchange protocols]], [[verifiable-computation-systems|Verifiable computation systems]], [[fair-data-exchange|Fair data exchange for committed data]]。
- 不应拆出的实例/协议/来源: RC-S-P、RC-PoR-P、SAP、VSID 目前作为方法路线和 source-local details；等有多篇来源复用后再考虑独立节点。

## 解决的问题

本节点回答: 当服务本身可由 cryptographic proof 或 verifiable protocol 检查时，如何把服务正确性、付款、退款、争议成本和隐私同时组织进一个可重复执行的 fair-exchange 协议。

典型问题包括:

- 恶意服务器提交无效服务 proof 后是否还能拿钱。
- 恶意客户端提供 malformed metadata/query 后是否还能让服务器背锅或拒付。
- proof status、文件大小、服务类型、价格是否被链上交易公开。
- 争议时如何低成本识别到底是客户端、服务器还是投诉方作恶。
- 普通 verifiable service 的“证明正确”如何和 smart contract 的“付款最终性”分层。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] | child_of | contingent service payment is fair exchange of service proofs and coins | active_seed |
| [[execution-and-transactions|Blockchain execution and transactions]] | direction | smart contract escrow, timeout, dispute and coin distribution are transaction-layer responsibilities | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| `proof-of-retrievability payments` | method/application candidate | RC-PoR-P gives a concrete PoR route, but PoR foundation and other PoR payment sources are still thin. | [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-S-P]] | keep_section |
| `verifiable service with identifiable abort` | method/concept candidate | VSID is reusable across VS/VC/PoR, but currently source-defined in this paper. | RC-S-P Appendix F | watching |
| `private proof-status settlement` | mechanism candidate | private time bubble, encryption/padding and delayed dispute appear reusable beyond this paper. | RC-S-P §8/G.1 | watching |
| `decentralized storage service payments` | application candidate | ICM-DSN shows a DSN-specific challenge route where proof verification, data forwarding, premium/collateral and request counting interact. | [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] | bridge_only |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| zkCSP-style service payment | 服务方证明自己知道有效 service proof，链上 hash-lock / payment route 结算。 | 一次或多次购买可验证服务证明，且客户端被假设较诚实。 | RC-S-P 指出其 PoR 实例泄露 proof status/deposit amount，并可被 malicious client free-ride。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-S-P]] related work/attack |
| VSID-backed recurring payment | 把普通 VS 升级为 VSID: 客户端证明 metadata/query well-formed，仲裁者能识别错误归因。 | 客户端和服务器都可能恶意，服务证明需要重复结算。 | 通用版本通常需要 NIZK、签名、bulletin board 和离线 arbiter。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-S-P]] |
| SAP + private time bubble | 双方用 commitment/smart contract 对 payment/query/proof 参数达成私密约定，等隐私窗口结束再处理争议。 | proof status 或服务价格有隐私价值。 | 隐私只持续到 bubble burst；需要 masked deposits 和 padding。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-S-P]] |
| Merkle PoR proof-of-misbehavior route | 用 Merkle-tree PoR 和单路径 proof of misbehavior，让 arbiter 只检查一个失败 path。 | PoR 服务、挑战可由 PRF seed 生成，争议可由单个 Merkle path 说明。 | proof size 为 `O(phi log m)`，但避免通用 ZK proof；PoR foundation 仍需更多来源。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-PoR-P]] |
| Smart-contract-as-arbiter variant | 当争议验证足够便宜时，把 arbiter 的 resolve 逻辑放进合约。 | 如 RC-PoR-P 这种只需验证一个 Merkle path 的场景。 | 投诉方要预付链上执行成本；不适合通用高成本 VS。 | [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-S-P Appendix L]] |
| DSN challenge contract route | 客户端不正常收到服务时挑战，oracle 取 segment/Merkle path 验证并转发数据或触发补偿。 | 去中心化存储服务、proof of storage 和 usage-based request pricing。 | 不是完整 RC-S-P 隐私协议；oracle trust boundary 明显；主路径仍属于 DSN/data-management。 | [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | paper | 创建本节点；定义 RC-S-P、识别 zkCSP free-riding/privacy 问题，给出 RC-PoR-P 实例和性能评估。 | 单篇 source seed；PoR foundation、ZKCSP original、FairSwap original 仍需补源。 | p1-p15, Appendix E-L |
| [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|An Incentive-Compatible Mechanism for Decentralized Storage Network]] | paper | 作为 bridge evidence 补充 DSN-specific service-payment route：challenge-based storage verification、oracle data forwarding、premium/collateral 和 request counter。 | 主路径是 decentralized storage networks；不替代 RC-S-P/PoR payment foundation。 | p1-p10 |

## 当前综合

- Evidence window: `2026-06-23`。
- Freshness: `fresh` for current-vault source evidence, not a latest-news claim。
- 综合: Contingent service payment 是 blockchain fair exchange 的服务型子问题。与 ZKCPlus/FDE 的“买数据/买 ciphertext/key”不同，这里交易对象是周期性服务 proof，因此协议必须同时处理 malicious client、proof-status privacy 和争议归责。RC-S-P 给出的分层很重要: verifiable service / VSID 负责服务正确性和归责，SAP/private time bubble/coin masking 负责链上隐私与付款参数，smart contract 负责 escrow 和最终分配。RC-PoR-P 说明当底层服务支持低成本 proof of misbehavior 时，可以不用昂贵 ZK proof，甚至让 smart contract 承担 arbiter。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | 创建 contingent-service-payments 子问题；补入 zkCSP 攻击、VSID、SAP、private time bubble、RC-PoR-P。 | all sections | yes | 后续补 ZKCSP/FairSwap/PoR direct sources，判断是否拆 PoR payments / VSID child |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]] | `verifiable-computation/verifiable-computation-systems; blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | dependency, application, payment-finality-boundary | VS/VC/PoR supplies verifiable service correctness; smart contracts supply escrow, dispute economics and final coin distribution. | active_seed |
| [[decentralized-storage-networks-to-contingent-service-payments|Decentralized storage networks -> contingent service payments]] | `blockchain-systems/data-management-and-storage/decentralized-storage-networks; blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | application, shared_pattern, tension | DSN storage proof and service availability can feed payment disputes; fair-exchange logic does not by itself guarantee storage availability or oracle honesty. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-contingent-service-payments | is_a | nahida-knowledge-blockchain-fair-exchange-protocols | RC-S-P source and parent node candidate | high | active_seed |
| nahida-knowledge-contingent-service-payments | depends_on | nahida-knowledge-verifiable-computation-systems | VS/VSID abstraction and bridge | medium | active_seed |
| nahida-knowledge-contingent-service-payments | adjacent_to | nahida-knowledge-fair-data-exchange | PoR/data retrieval/payment adjacency | medium | active_seed |
| nahida-knowledge-contingent-service-payments | evidenced_by | vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md | source note | high | active_seed |
| nahida-knowledge-contingent-service-payments | bridges_to | nahida-bridge-decentralized-storage-networks-to-contingent-service-payments | ICM-DSN bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| ZKCSP original and Campanelli/Fuchsbauer/Nguyen follow-ups 缺 direct source。 | 当前对 zkCSP 的攻击/边界主要来自 RC-S-P 论文，应补原始路线避免二手理解。 | continue paper intake / nahida-research-search | high | queued |
| PoR/PDP foundation source 缺。 | RC-PoR-P 的底层 Merkle PoR 细节目前只作为本 source 的局部定义，不能替代 PoR foundation。 | nahida-update foundation_pack | medium | queued |
| DSN storage-service payment 和 oracle trust 边界仍薄。 | ICM-DSN 补入 challenge-based storage contract，但还缺 Filecoin/Sia/Storj/Swarm 和 oracle/security direct sources。 | nahida-update / nahida-research-search | high | queued |
| FairSwap/OPTISWAP original source 缺。 | proof-of-misbehavior route 对比目前来自 related work，不能完整判断 service-payment 可迁移性。 | nahida-update / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-recurring-contingent-service-payment | Promoted service-payment variants into active contingent-service-payments child problem and attached RC-S-P source. | arxiv:2208.00283v2 | codex |
| 2026-06-23 | nahida-knowledge-20260623-incentive-compatible-decentralized-storage | Added DSN bridge evidence and clarified challenge-based storage contracts as adjacent, not identical, to RC-S-P. | arxiv:2208.09937 | codex |
