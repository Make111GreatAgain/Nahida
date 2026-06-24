---
id: "arxiv-1802.07240"
title: "Cobalt: BFT Governance in Open Networks"
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
  - "p1-p4 abstract, introduction, XRP LCP motivation, governance/transaction-network separation, problem framing"
  - "p4-p8 network model, UNL/essential subsets, tS/qS constraints, DABC properties, FLP/randomness motivation"
  - "p8-p12 related work, comparison with PBFT/Aardvark/SINTRA/Honeybadger/XRP LCP/SCP/Tendermint, Cobalt definitions"
  - "p13-p18 linked/fully-linked support lemmas, CRS definition, RBC and DRBC protocol/proofs"
  - "p18-p25 ABBA definition, protocol, FINISH/CONF modifications, proof lemmas and Theorem 24"
  - "p25-p36 DABC formal definition, MVBA protocol/proofs, stamping protocol, Full-Knowledge proof and Theorem 37"
  - "p37-p39 references"
  - "p40-p44 Appendix A transaction-ordering delegation, PBFT-like view-change, fallback Cobalt transaction ordering"
  - "p44-p46 Appendix B CRS implementation with AVSS, randomizing keys, threshold shares over essential subsets"
  - "p47-p49 Appendix C logarithmic expected MVBA round analysis"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1802.07240"
doi: ""
arxiv_id: "1802.07240v1"
venue: "arXiv"
year: "2018"
pdf_pages: 49
pdf_sha256: "32f626edc393b15b8d3e728fc31f05eae0b20a96a30318d71ef1df6d09ce9f94"
local_pdf: "~/Desktop/paper/1802.07240.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/1802.07240-32f626edc393-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "consensus"
topic_ids:
  - "open-network-bft-governance"
  - "byzantine-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "open-network-bft-governance"
primary_ontology_path: "blockchain-systems/consensus/open-network-bft-governance/arxiv-1802.07240"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/arxiv-1802.07240"
path_update_status: "propagated"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "cobalt"
  - "open-network-bft-governance"
  - "democratic-atomic-broadcast"
  - "unique-node-lists"
  - "byzantine-fault-tolerance"
aliases:
  - "Cobalt"
  - "DABC"
  - "Democratic atomic broadcast"
  - "UNL consensus"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "consensus"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "distributed-systems"
  subdomain:
    - "consensus"
  problem:
    - "BFT governance in open networks"
    - "non-uniform trust without global participant agreement"
    - "decentralized amendment ratification"
    - "local consistency under UNL overlap"
  method_family:
    - "democratic atomic broadcast"
    - "essential subsets"
    - "open-network reliable broadcast"
    - "asynchronous binary Byzantine agreement"
    - "external-validity MVBA"
    - "cryptographic common random source"
  system_layer:
    - "governance layer"
    - "validator/UNL configuration"
    - "transaction-network delegation"
  evaluation_context:
    - "formal protocol proof"
    - "appendix complexity analysis"
  application:
    - "XRP Ledger governance"
    - "open-entry voting network"
  bridge:
    - "distributed BFT -> open-network blockchain governance"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-cobalt"
source_refs:
  - "arxiv:1802.07240"
  - "arxiv:1802.07240v1"
  - "sha256:32f626edc393b15b8d3e728fc31f05eae0b20a96a30318d71ef1df6d09ce9f94"
  - "pdf:~/Desktop/paper/1802.07240.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> consensus"
secondary_directions:
  - "distributed-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "arXiv header"
  - "title/abstract"
  - "Sections 2-4 and appendices"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0017"
queue_status: "absorbed"
---

# Cobalt: BFT Governance in Open Networks

## 论文身份

- 标题: Cobalt: BFT Governance in Open Networks
- 作者: Ethan MacBrough
- 机构: Ripple Research
- 年份/版本: 2018, arXiv:1802.07240v1
- DOI: unknown
- 链接: https://arxiv.org/abs/1802.07240
- 本地 PDF: `~/Desktop/paper/1802.07240.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/1802.07240-32f626edc393-pages.txt`
- 代码/数据: unknown in PDF
- License: unknown in PDF

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 49
- 已覆盖章节/页码: p1-p49 full text，包括 Appendix A/B/C
- 未覆盖章节/页码: 无
- Extraction gaps: 正文可读；抽取文本存在 ligature、空格和公式换行噪声；图表不构成核心证据；没有实证评估图表。
- 精读说明: 这是 formal protocol / proof paper，吸收时应把它当成 open-network BFT governance 的 source-backed seed，而不是把 Cobalt 的 XRP-specific 设计直接泛化为所有区块链共识。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / p1-p4 | 动机与贡献 | open networks, non-uniform trust, no global participant agreement; Cobalt 用于 decentralized voting/governance；目标是降低 XRP LCP 的高 UNL overlap bound 并避免卡住 | 贡献定位 | 论文声称在 80% quorum 类 UNL 模型下约需 >60% pairwise overlap |
| §2 / p4-p8 | 网络模型与 DABC | correct/Byzantine/actively Byzantine/honest; UNL, extended UNL, essential subsets, `tS/qS`; DABC Agreement/Linearizability/Democracy/Liveness/Full-Knowledge | 模型定义 | 核心不是 global membership，而是每个节点本地 trust structure |
| §3 / p8-p11 | Related work | PBFT/Aardvark/SINTRA/Honeybadger, XRP LCP, Stellar SCP, Tendermint/PoS 的比较 | 边界定位 | 指出 leader-based、global safety、weak synchrony、stake-weighted governance 等限制 |
| §4 prelude / p11-p14 | 基础定义 | linked, fully linked, healthy, unblocked, strongly/weakly connected; weak/strong support lemmas | 正确性骨架 | local consistency 的数学基础 |
| §4.1 / p14 | Common random source | CRS-Consistency, CRS-Termination, CRS-Randomness | FLP 绕开机制 | 实现在 Appendix B |
| §4.2 / p14-p18 | RBC/DRBC | Bracha-style INIT/ECHO/READY adapted to weak/strong support; DRBC adds support/opposition and democracy | 低层 primitive | Theorem 8/10 |
| §4.3 / p18-p25 | ABBA | Mostefaoui-style async binary agreement adapted with FINISH and CONF; strong validity through UNL chains | 低层 primitive | Theorem 24, probabilistic termination |
| §4.4 / p25-p32 | MVBA | external-validity MVBA using random index `Ir(A)=H(A||sr)` and ABBA STOP round | 多值共识 | Theorem 30; Proposition 25 local consistency |
| §4.5 / p32-p36 | DABC reduction | DRBC distributes `(A, nA)`, stamping protocol assigns activation time, MVBA selects per slot; waiting protocol gives Full-Knowledge | 主协议 | Theorem 37 |
| Appendix A / p40-p44 | Transaction ordering | Cobalt should govern amendments/transaction-network views; transaction network runs fast complete-network BFT; PBFT-like view change and fallback Cobalt ordering | 系统架构 | Separates adaptability from throughput |
| Appendix B / p44-p46 | CRS implementation | AVSS, threshold shares per essential subset, randomizing keys as pseudo-amendments, mixer | 密码假设 | 全部 randomizing keys 被攻破后恢复性不明 |
| Appendix C / p47-p49 | Complexity | Expected MVBA rounds bounded by `c + log3(|S0_i|) + O(1/|S0_i|)` under random oracle assumptions | 效率分析 | 无实证 benchmark |

## 一句话贡献

Cobalt 将 BFT atomic broadcast 改造到没有全局参与者集合、只有非一致 UNL/essential-subset trust structure 的开放网络中，用 `democratic atomic broadcast` 支撑治理 amendment 的安全 ratification，并把交易排序委托给可替换的快速 transaction network。

## 核心精读笔记

### 背景、动机与问题边界

Cobalt 针对的是 XRP LCP 暴露出的两个问题: 一是 classical consensus 通常假设所有节点对参与者集合有共同认知，这与独立运营者、开放参与和 Sybil 风险冲突；二是 XRP LCP 的 UNL overlap bound 经 Chase/MacBrough 重新分析后接近 `>90%`，并且在没有 faulty nodes、99% UNL agreement 的特定网络里也可能停滞。Cobalt 的目标是降低配置压力、保持 consistency，并避免网络在满足 overlap 条件时卡死。证据锚点: p1-p3。

论文的重要架构洞察是将 decentralization 的 redundancy 与 adaptability 拆开。Cobalt 本身相对慢，不建议直接高吞吐排序所有交易；论文建议用 Cobalt 作为 governance layer 只处理 amendments，例如 transaction network 的成员变更；实际 transaction ordering 交给 Honeybadger、Aardvark 等 complete-network 快速 BFT 算法。Cobalt nodes 仍自行验证交易，transaction network 只负责排序。证据锚点: p3, Appendix A p40-p44。

### 网络模型和信任结构

网络中节点集合 `P` 不需要被所有参与者知道，甚至网络大小也不需要全局已知。每对节点之间假设存在 reliable authenticated communication channel，但节点可以要求费用或 proof-of-work 来防 DDoS。正确节点严格按协议执行；Byzantine 节点可崩溃、沉默、发送错误或向不同对象发送冲突消息。论文还区分 `actively Byzantine` 与 `honest`: 崩溃节点可能是 Byzantine，但不一定 actively Byzantine；发送本不会发送的消息才算 actively Byzantine。证据锚点: §2 p4。

每个节点 `Pi` 有自己的 unique node list `UNLi`，表示其听取的节点集合；`UNLi` 不一定包含自己。Cobalt 的更核心对象是 `essential subsets`（`ESi`），`UNLi` 是这些 subsets 的并。每个 essential subset `S` 有 `nS=|S|`、`tS` 和 `qS`，需要满足 `0 <= tS,qS <= nS`、`tS < 2qS - nS`、`2tS < qS`。直觉上，`tS` 是 safety 可容忍的 actively Byzantine 数，`qS` 是 liveness 所需 correct 数。证据锚点: p5-p6。

在 XRP 风格的原始 UNL/quorum 模型中，若使用 80% quorum，论文称可由 Proposition 25 得到大约 `>60%` pairwise UNL overlap 即可保证 consistency。这个数字只适用于该模型转换，不应泛化为所有 essential-subset 配置。证据锚点: p5, p29。

### DABC 问题定义

Cobalt 形式化的问题叫 `democratic atomic broadcast` (DABC)。proposers 可以广播 amendments；节点可支持或反对；节点随后 ratify 某些 amendments 并给出 activation time。DABC 要求 Agreement、Linearizability、Democracy、Liveness 和 Full-Knowledge。Full-Knowledge 是治理层特有要求: 对任意时间 `τ`，节点可运行 waiting protocol 并在有限时间后知道所有 activation time 早于 `τ` 的 amendments，避免不同节点因异步获知协议升级而运行不同版本。证据锚点: p6-p8, p25-p26。

### Local consistency 的基础定义

论文定义 `linked`、`fully linked`、`healthy`、`unblocked`、`strongly connected`、`weakly connected`。两个节点 linked 是指存在共同 essential subset 且其中 actively Byzantine 节点少于 `tS`；fully linked 还要求至少 `qS` correct nodes、至多 `tS` actively Byzantine、且 `tS <= nS - qS`。`strong support` 表示从每个 essential subset 都收到 `qS` 个对应消息；`weak support` 表示从某个 essential subset 收到 `tS+1` 个对应消息。Lemma 1/2 说明 fully linked 节点可把 strong support 传播成 weak support，而 linked 节点不能同时对矛盾消息都看到 strong support。证据锚点: p12-p14。

这个局部化是 Cobalt 与 XRP LCP/SCP 的关键差异之一。论文明确强调 consistency 是 local property: 两个配置良好的 linked 节点不会因为第三方节点配置差而被拖入不一致状态。liveness 仍需要 strong connectivity 等更强条件。证据锚点: p11-p12, Proposition 25 p29。

### RBC 和 DRBC

Cobalt 的 reliable broadcast 是 Bracha RBC 的 open-network 版本。broadcaster 先发 `INIT(M)`，节点按 `ECHO(M)` / `READY(M)` 运行: 收到 direct INIT 后 ECHO；看到 weak ECHO 后也 ECHO；看到 strong ECHO 后 READY；看到 weak READY 后 READY；看到 strong READY 后 accept。Theorem 8 证明该协议满足 RBC-Consistency、Reliability、Validity、Non-Triviality。证据锚点: p14-p17。

DRBC 在 RBC 上加入节点对消息的 support/opposition: 只有支持消息时才发送 `ECHO(M)`，但即使不支持也可能为了可靠性发送 `READY(M)`。DRBC-Democracy 保证若 weakly connected healthy node 接受 `M`，则其某个 essential subset 中 honest nodes 的多数支持 `M`。证据锚点: p17-p18。

### ABBA

Cobalt 的 asynchronous binary Byzantine agreement (ABBA) 改编自 Mostefaoui et al.。协议使用 common random source `ρr`，并包含 `INIT`、`AUX`、`CONF`、`FINISH`。`FINISH` message 让 agreement 成为 local property；`CONF` message 用于在 step 10 之前降低 adversary 预知 CRS 并操控 termination 的能力。Theorem 24 证明 ABBA-Consistency、Termination with probability 1、Strong-Validity。证据锚点: p18-p25。

ABBA 的 Strong-Validity 很重要: 如果 unblocked node 输出 `v`，存在一条沿 UNL 关系的 unblocked-node chain，链末端节点确实 input `v`。这比普通 binary agreement validity 更适合 open-network 模型，因为孤立节点的输入不应凭空决定全局结果。证据锚点: p18-p19, Proposition 22 p24。

### MVBA 与 DABC reduction

Cobalt 的 external-validity MVBA 允许每个节点维护动态 valid input set `values0_i`，并在满足 Assumed-Reliability/Assumed-Validity 的情况下输出某个本节点认为有效的值。它使用 random oracle hash `H(A||sr)` 对每轮候选值排序，并用 ABBA `STOP` instance 决定是否结束或继续缩小候选集合。Theorem 30 证明 MVBA correctness；Proposition 25 证明 MVBA consistency 是 local property。证据锚点: p25-p32。

DABC reduction 的主线是: proposers 用 DRBC 广播 `(A, nA)`，其中 `nA` 是 amendment 所属 slot。节点只有在已经 ratify 更低 slot 且支持上下文一致时才支持该 message。stamping protocol 周期性广播 `CHECK(P, τ)`，在看到足够多 CHECK 后广播/传播 `ACCEPT(A,nA,τ)`，并将 `(A,τ)` 加入 slot `nA` 的 MVBA valid set。等待协议要求节点对所有 `τ' <= τ` 的 CHECK 中提到的 slot 都已 ratify，进而给出 Full-Knowledge。Theorem 37 证明 modified DABC protocol 满足 DABC properties。证据锚点: p32-p36。

### Transaction network delegation 与 view change

Appendix A 说明 Cobalt 可直接排序交易，但效率很差: 单交易 per MVBA 太慢，批量 block 版本也可能有 `O(D*P)` 通信，且延迟随 proposer 数对数增长。论文因此建议用 Cobalt 治理一组 transaction network nodes，让该网络运行 fast complete-network consensus 做交易排序。Cobalt nodes 验证 transaction validity，因此 transaction network 不能任意修改 ledger state；若 transaction network 失败，Cobalt 通过 PBFT-like view change 切换 view。证据锚点: Appendix A p40-p43。

当所有预设 backup views 同时失败时，论文建议临时退回用 Cobalt 自己排序 transaction blocks。为防 censorship，block 不绑定固定 slot；节点一旦看到某 block 为 valid input，就在该 block 被 ratify 前拒绝支持其他 blocks。证据锚点: Appendix A p43-p44。

### CRS implementation

Appendix B 给出 CRS 实现方案: 节点通过 AVSS 将 secret `s` 以 `(tS+1,nS)` threshold shares 分发给多个 essential subsets，并通过 pseudo-amendment 将 public key 加入 randomizing keys。每次 CRS 对每个 randomizing key 生成签名，再把签名混合后输入 random oracle 产生随机值。该设计的关键假设是至少一个 randomizing key 的 secret 对 adversary 保密。论文也承认如果 adversary 同时攻破全部 randomizing keys，理论上系统可能难以恢复。证据锚点: Appendix B p44-p46。

### 效率分析

Appendix C 证明，在 random oracle 假设下，若 hash image 足够大，MVBA 期望终止轮数至多约 `c + log3(|S0_i|) + O(1/|S0_i|)`，其中 `c` 是小常数。直觉是每轮随机索引会淘汰一个常数比例候选值。证据锚点: Proposition 38 p47-p49。

## 层级分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `blockchain-systems` | XRP Ledger、decentralized currencies、governance amendments、transaction network | accepted |
| L2 direction | `consensus` | atomic broadcast, BFT, transaction ordering, governance consensus | accepted |
| L3 topic | `open-network-bft-governance` | non-uniform trust, no global participant agreement, DABC | accepted |
| Secondary path | `distributed-systems/consensus/byzantine-fault-tolerance` | Byzantine, RBC, ABBA, MVBA, FLP, PBFT comparison | accepted as bridge |

## 与现有 Nahida 笔记的关系

- 扩展 [[byzantine-fault-tolerance|Byzantine fault tolerance]]: 从 complete-network/permissioned BFT 扩到 open-network non-uniform trust。
- 扩展 [[blockchain-consensus|Blockchain consensus]]: 增加 governance/amendment consensus，而不只是 PoS finality 或 permissioned CFT。
- 与 [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint]] 对比: Tendermint 用 stake-weighted validators 和 weak synchrony；Cobalt 用 delegated trust / essential subsets 和 probabilistic asynchronous progress。
- 与 [[distributed-bft-to-blockchain-finality|Distributed BFT -> blockchain finality]] 并列: Cobalt 不是 PoS finality source，而是 BFT -> open-network governance 的独立桥。

## Evidence Table

| Claim / observation | Source location | Claim type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Cobalt targets open networks with non-uniform trust and no global participant agreement | Abstract, §1 p1-p3 | problem/goal | high | explicit |
| Essential subsets generalize UNL/quorum decisions and encode `tS/qS` thresholds | §2 p4-p6 | model | high | equations 1-3 |
| In 80% quorum analogue, Cobalt gives roughly `>60%` pairwise overlap for consistency | §2 p5, Proposition 25 p29 | model-specific implication | medium-high | only under translated original UNL formalism |
| DABC includes Agreement, Linearizability, Democracy, Liveness, Full-Knowledge | §2 p6-p8, §4.4 p25-p26 | definition | high | full formal definition |
| Local consistency rests on linked nodes and strong/weak support lemmas | §4 p11-p14, Proposition 25 p29 | theorem/proof | high | key design identity |
| RBC/DRBC adapt Bracha reliable broadcast to essential subsets | §4.2 p14-p18 | protocol | high | Theorem 8/10 |
| ABBA adapts Mostefaoui using FINISH/CONF and CRS | §4.3 p18-p25 | protocol | high | Theorem 24 |
| DABC reduces to DRBC + MVBA + stamping protocol | §4.4-§4.5 p25-p36 | construction | high | Theorem 37 |
| Transaction ordering should be delegated to a fast transaction network under Cobalt governance | §1 p3, Appendix A p40-p44 | architecture | high | recommendation |
| CRS implementation depends on AVSS/randomizing keys and has total-key-compromise caveat | Appendix B p44-p46 | assumption/limitation | high | explicit limitation |
| MVBA expected rounds are logarithmic in valid input count under random oracle assumptions | Appendix C p47-p49 | complexity | high | formal proposition, no empirical test |

## 限制与注意事项

- 没有实证 benchmark；效率结论主要是 asymptotic/probabilistic analysis。
- 论文由 Ripple Research 资助并面向 XRP Ledger governance；跨系统迁移需要检查治理、membership、transaction validity、client/network assumptions。
- `>60%` overlap 是特定 UNL/quorum translation 下的解释，不是所有 essential-subset 配置的统一公式。
- liveness 需要 strong connectivity、unblocked nodes、CRS 和 eventual message delivery；consistency 的假设更弱但不等于全局活性。
- CRS 依赖 AVSS、threshold sharing、randomizing keys 和 consensus 添加 keys；所有 randomizing keys 同时失陷时恢复性未解决。
- Cobalt 不替代高吞吐 transaction ordering；Appendix A 明确建议正常路径使用单独 transaction network。

## 可复用想法

- 把“谁参与共识”从全局集合改成本地 trust graph + overlap conditions，可用于开放网络治理层。
- 将 consistency 做成 local property，让配置差的远端节点不拖垮配置良好的节点对。
- 把治理/规则变更与交易排序分层: 慢但开放的治理层负责更新 fast consensus committee。
- Full-Knowledge 是协议升级治理的关键性质: 节点不仅要同意 amendments，还要知道某时间前所有会激活的 amendments。
- 对开放网络里的 common coin/CRS，需要把 threshold cryptography 改造成 essential-subset 可验证的 randomizing-key 机制。

## 术语表

| Term | 含义 | Evidence |
| --- | --- | --- |
| UNL / unique node list | 节点本地听取的节点集合 | §2 p4-p5 |
| Essential subset | 节点用来做决策的核心 trust subset；UNL 是其并 | §2 p5 |
| `tS`, `qS` | essential subset 的 safety/liveness threshold 参数 | §2 p5-p6 |
| Linked | 两节点共享某个 adequately safe essential subset；用于 local consistency | §4 p12 |
| Fully linked | linked 的更强版本，支持 liveness propagation | §4 p12 |
| Strong support | 每个 essential subset 都收到 `qS` messages | §4 p13 |
| Weak support | 某个 essential subset 收到 `tS+1` messages | §4 p13 |
| DABC | Democratic atomic broadcast，用于 open-network governance amendments | §2 p6-p8 |
| DRBC | Democratic reliable broadcast，RBC 加 support/opposition | §4.2.4 p17-p18 |
| MVBA | External-validity multi-valued Byzantine agreement | §4.4 p25-p32 |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Cobalt's ABBA protocol adapts a Mostefaoui-style asynchronous binary agreement algorithm by adding FINISH messages for local agreement, CONF messages to protect randomness use, and a common random source for probabilistic termination. | `arxiv:1802.07240#p18-p25` | folded_into_meta_note |
| Cobalt's common random source is implemented through AVSS-distributed randomizing keys and threshold shares over essential subsets, and the paper leaves recovery from simultaneous compromise of all randomizing keys unresolved. | `arxiv:1802.07240#p44-p46` | folded_into_meta_note |
| Cobalt is designed as a democratic atomic broadcast protocol for open networks with non-uniform trust and no global agreement on participants. | `arxiv:1802.07240#p1-p3`<br>`arxiv:1802.07240v1#p25-p26` | folded_into_meta_note |
| Cobalt adapts Bracha-style reliable broadcast to the essential-subset model and extends it to democratic reliable broadcast by allowing nodes to support or oppose messages before echoing them. | `arxiv:1802.07240#p14-p18` | folded_into_meta_note |
| Cobalt replaces a single UNL quorum threshold with essential subsets carrying per-subset safety and liveness thresholds, and the original 80 percent UNL-quorum model maps to roughly greater-than-60-percent pairwise overlap for consistency. | `arxiv:1802.07240#p5-p6`<br>`arxiv:1802.07240#p29` | folded_into_meta_note |
| Cobalt's consistency property is local: two honest linked nodes cannot output inconsistent values even if unrelated parts of the open network are poorly configured. | `arxiv:1802.07240#p11-p14`<br>`arxiv:1802.07240#p29` | folded_into_meta_note |
| Under the paper's random-oracle assumptions and sufficiently large hash image, Cobalt's MVBA expected number of rounds is logarithmic in the number of initial valid inputs. | `arxiv:1802.07240#p47-p49` | folded_into_meta_note |
| Cobalt implements democratic atomic broadcast by using DRBC to distribute amendment-slot proposals, a stamping protocol to agree on activation times, and external-validity MVBA to select one valid proposal per slot. | `arxiv:1802.07240#p25-p36` | folded_into_meta_note |
| Cobalt is recommended as an open governance layer for ratifying amendments and transaction-network membership, while ordinary transaction ordering should be delegated to a faster complete-network consensus group. | `arxiv:1802.07240#p3`<br>`arxiv:1802.07240#p40-p44` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt solves democratic atomic broadcast for open networks]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt makes consistency local through linked essential subsets]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt essential subsets generalize UNLs and quorum thresholds]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt DRBC adapts Bracha reliable broadcast to support-weighted open networks]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt ABBA uses FINISH, CONF, and CRS to get local agreement and probabilistic termination]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt reduces DABC to DRBC, stamping, and external-validity MVBA]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt separates open governance from fast transaction ordering]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt CRS depends on randomizing keys, AVSS, and secret-sharing assumptions]]
- [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt MVBA has logarithmic expected rounds under random-oracle assumptions]]

### Concepts to create or update

- Create [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt]].
- Create [[open-network-bft-governance|Democratic atomic broadcast]].
- Create [[open-network-bft-governance|Essential subsets and UNLs]].
- Update [[byzantine-fault-tolerance|Byzantine fault tolerance]].
- Update [[blockchain-consensus|Blockchain consensus]] and create [[open-network-bft-governance|Open-network BFT governance]] topic map.

### Synthesis handoff

- Create `open-network-bft-governance-state-2026-06-11`.
- Refresh `byzantine-fault-tolerance-state-2026-06-11` with Cobalt as open-network BFT extension.
- Create bridge `distributed-bft-to-open-network-blockchain-governance`.

### Review queue items

- `foundation_needed`: Stellar Consensus Protocol should be absorbed directly before treating Cobalt/SCP comparison as settled.
- `implementation_needed`: modern XRPL consensus/governance documentation or code source needed for production behavior.
- `theory_foundation_needed`: FLP, Bracha RBC, Mostefaoui ABBA, and asynchronous common coin sources are prerequisites for a durable protocol-family synthesis.
- `scope_boundary`: Cobalt is a governance/amendment protocol; transaction ordering is delegated in the recommended architecture.
