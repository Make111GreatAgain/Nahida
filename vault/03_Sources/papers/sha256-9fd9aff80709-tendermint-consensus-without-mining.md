---
id: "sha256-9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
title: "Tendermint: Consensus without Mining"
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
  - "p1-p2 abstract, introduction, proof-of-work critique, security quantification problem"
  - "p2-p4 terms, block structure, validators, bonding, forks, evidence and short/long-range attacks"
  - "p4-p8 FLP/partial synchrony context, DLS ancestry, round protocol, locking, safety and liveness sketches"
  - "p8-p10 cooperation incentives, sparse signatures, validator timeouts, block propagation optimizations"
  - "p10-p11 conclusion and references"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "Draft v.0.6"
year: "2014"
pdf_pages: 11
pdf_sha256: "9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
local_pdf: "~/Desktop/paper/Tendermint Consensus without Mining.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/tendermint-consensus-without-mining-9fd9aff80709-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "consensus"
topic_ids:
  - "proof-of-stake-finality"
  - "byzantine-fault-tolerance"
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "proof-of-stake-finality"
primary_ontology_path: "blockchain-systems/consensus/proof-of-stake-finality/sha256-9fd9aff80709"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/sha256-9fd9aff80709"
path_update_status: "propagated"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "proof-of-stake-finality"
  - "byzantine-fault-tolerance"
  - "tendermint"
aliases:
  - "Tendermint"
  - "Tendermint consensus"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "consensus"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "consensus"
  problem:
    - "mining-free blockchain consensus"
    - "proof-of-stake finality"
    - "double-spend resistance"
    - "byzantine validator voting"
  method_family:
    - "partial-synchrony BFT"
    - "bonded proof-of-stake validators"
    - "round-based propose-prevote-precommit"
    - "locking and proof-of-lock"
  system_layer:
    - "blockchain consensus"
    - "validator set"
    - "finality layer"
  evaluation_context:
    - "safety proof sketch"
    - "liveness proof sketch"
    - "economic penalty reasoning"
  application:
    - "cryptocurrency ledger"
    - "double-spend prevention"
  bridge:
    - "distributed BFT -> blockchain finality"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-tendermint-consensus-without-mining"
source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "pdf:~/Desktop/paper/Tendermint Consensus without Mining.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> consensus"
secondary_directions:
  - "distributed-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "filename/title"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0007"
queue_status: "absorbed"
---

# Tendermint: Consensus without Mining

## 论文身份

- 标题: Tendermint: Consensus without Mining
- 作者: Jae Kwon
- 邮箱/机构: `yk239@cornell.edu`; affiliation not otherwise stated in PDF
- 版本: Draft v.0.6
- 年份: 2014
- DOI: unknown
- arXiv: unknown
- 本地 PDF: `~/Desktop/paper/Tendermint Consensus without Mining.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/tendermint-consensus-without-mining-9fd9aff80709-pages.txt`
- 代码/数据: unknown in this PDF
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 11
- 已覆盖章节/页码: p1-p11 full text
- 已检查附录: 本 PDF 无附录；文中有未完成的 TODO
- 未覆盖章节/页码: 无
- Extraction gaps: 页面可读；少量单词粘连和 ligature 噪声；Figure 内容只有标题和周边正文，正文足以重建协议
- 精读说明: 这是 early draft v0.6，`Optimizations` 和 `Conclusion` 明显未完成；可作为 Tendermint/PoS-BFT seed，但不应当当作现代 Tendermint 规格书。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1 | Abstract/Introduction | PoW 成本、确认慢、安全难量化；提出无需 mining 的 blockchain consensus | 贡献定位 | 直接声明改造 Byzantine Generals solution |
| p2 | Security quantification | PoW/PoS 安全的外生/内生成本，nothing-at-stake，double-spend penalty | 问题设定 | 经济安全动机 |
| p2-p4 | Terms/Block/Validators | blockchain、transactions、block hash、validator bonding、2/3 majority、fork/evidence/unbonding | 模型定义 | finality 与 slashing 的基础 |
| p4-p5 | Byzantine consensus context | FLP、partial synchrony、DLS algorithm 2'、<1/3 Byzantine voting power | 理论依赖 | 明确不是 pure async |
| p5-p8 | Algorithm | propose/prevote/precommit/commit/new height，weighted round-robin proposer，locks/proof-of-lock | 协议机制 | 核心可吸收内容 |
| p8 | Safety/Liveness | safety proof sketch; liveness via proof-of-lock unlocking older locks | 正确性论证 | sketch 级别，不是完整形式化证明 |
| p8-p9 | Cooperation | validator fee sharing and tit-for-tat exclusion argument | 经济激励 | 辅助性论证，简化假设多 |
| p9-p10 | Optimizations | sparse signature set TODO, validator timeout/unbonding, faster propagation TODO | 工程限制 | 明确不完整 |
| p10-p11 | Conclusion/References | 极简 conclusion; Bitcoin, NXT, BitShares, DLS, FLP, BFT survey refs | 上下文 | refs 可作为 foundation follow-up |

## 核心精读笔记

### 背景、动机与问题边界

Tendermint 的问题出发点是 Bitcoin 式 PoW consensus 的成本和安全可量化性。论文认为 PoW 需要高能耗，交易确认慢，并且攻击/防御能力依赖矿机、电力等外生因素，难以直接量化。它希望把安全性转成更内生的 validator bond 经济惩罚: 如果短期 double-spend 必然要求足够多 bonded validators 双签，就能用证据交易销毁其 bonded coins。证据锚点: p1-p4。

该论文解决的是 blockchain ledger 的 finality/consensus，而不是一般数据库复制。它假设 validators 有 bonded coins 和投票权，网络是 peer-to-peer gossip，系统需要防御 malicious Byzantine actors 导致的 double-spend。它不声称解决 long-range attacks 的全部问题；相反，明确要求用户在 unbonding period 内周期性同步链，以避免 validators 解锁并卖出 stake 后发布历史 fork。证据锚点: p3-p4。

### 模型、假设与定义

Validator 是通过 bond transaction 锁定 coins 的账户，投票权等于 bonded coins。`2/3 majority` 指至少 2/3 total voting power，`1/3 majority` 指至少 1/3 total voting power。一个 block 在 2/3 validators 签 commit votes 后被 committed。若同一高度两个 blocks 都有 2/3 commit signatures，则两个 2/3 集合必然交叠，至少 1/3 voting power 发生 duplicitous signing。证据锚点: p3-p4。

协议假设 partial synchrony: 存在未知消息延迟上界 `Delta`；non-Byzantine nodes 有短时间足够准确的本地时钟，但不要求全局时间一致。Tendermint 继承/改造 Dwork-Lynch-Stockmeyer (DLS) partial synchrony BFT 思路，容忍小于 1/3 Byzantine voting power。证据锚点: p4-p5。

### 方法、协议或系统机制

每个 blockchain height 运行 round-based protocol。每轮包含 `Propose`、`Prevote`、`Precommit` 三个普通步骤，以及 `Commit`、`NewHeight` 两个特殊步骤。Proposer 以 round-robin 方式选择，频率与 voting power 成比例。若 proposer 已被某个旧 round 的 block 锁定，则提议 locked block，并带上 `proof-of-lock`。证据锚点: p5-p6。

在 `Prevote` 步骤，validator 若已锁定旧 block 就 prevote locked block；否则若收到当前 round 的 acceptable proposal，就 prevote proposal；否则 prevote nil。`Precommit` 步骤中，若 validator 收到某个 block 超过 2/3 prevotes，则 precommit 该 block 并 lock；若收到超过 2/3 nil prevotes，则 unlock。锁定或解锁时会收集对应 prevotes 作为后续 proposal 的 proof-of-lock。证据锚点: p6-p7。

在 `Precommit` 结束时，若节点看到某个 block 超过 2/3 precommits，就进入 `Commit`。真正 finalize 前还要收到该 block，并等待至少 2/3 commits。`NewHeight` 用于为前一高度收集额外 commits，让慢 validators 的 signatures 能被纳入链中。任意时刻若节点看到某 block 超过 2/3 commits，会立即进入 `Commit`；任意时刻若锁定在 round R 的节点看到更高 round `R'` 的 proof-of-lock，会解锁。证据锚点: p7-p8。

### 理论、证明或正确性论证

Safety proof sketch: 若 Byzantine voting power 小于 1/3，且至少一个 good validator 在最早 round R decide block B，则它看到超过 2/3 precommits for B。因为 Byzantine 少于 1/3，至少 1/3 good validators 在 round R precommit B 并锁定 B。之后 good validators 不会在没有更高 proof-of-lock 的情况下解锁，论文声称因此不会有 good validator decide 不同 block。证据锚点: p8。

Liveness proof sketch: deadlock 只会来自不同 good validators 在不同 rounds 锁定不同 blocks。若某些 good validators 锁在 B/R，另一些锁在 B'/R' 且 R < R'，那么 good proposer 提出的来自 R' 的 proof-of-lock 最终会解锁旧 round 的 locks，使协议继续推进。这个论证依赖 partial synchrony 和每轮时长递增。证据锚点: p5, p8。

### 实验、评估或案例

论文没有给实现评测、性能数据或真实部署数据。它的“评估”主要是机制论证: 2/3 quorum arithmetic、slashing evidence、partial-synchrony liveness sketch，以及合作章节中的 fee-exclusion game reasoning。优化章节含 TODO，因此 sparse signature set 和 faster block propagation 不能当作已完成贡献。证据锚点: p8-p10。

### 作者结论与我的判断

作者明确提出 Tendermint 是无需 proof-of-work mining 的 blockchain consensus protocol，基于 DLS partial synchrony BFT，并通过 bonded validators/slashing 把短期 double-spend 成本内生化。我的判断: 这篇是 Nahida 中 `blockchain-systems/consensus/proof-of-stake-finality` 的高价值 seed，因为它把经典 BFT/partial synchrony 迁移到 PoS blockchain finality，但它是早期 draft，不能覆盖现代 Tendermint 的完整工程规格、IBC/Cosmos 生态或后续共识变体。证据锚点: p1-p10。

## 层级候选分类

- L1 Domain candidate: `blockchain-systems`
- L2 Direction candidate: `consensus`
- L3 Topic/content cluster candidates: `proof-of-stake-finality`, `byzantine-fault-tolerance`, `tendermint`
- Ontology path: `blockchain-systems/consensus/proof-of-stake-finality/sha256-9fd9aff80709`
- 备选归属: `distributed-systems/consensus/byzantine-fault-tolerance`
- 父级领域: blockchain systems
- 学术子领域: blockchain consensus, proof-of-stake finality, Byzantine fault tolerance
- 任务/问题: double-spend prevention without proof-of-work mining
- 方法族: partial-synchrony BFT, bonded validators, slashing evidence, propose/prevote/precommit rounds
- 模型/协议/算法族: Tendermint, DLS-style BFT
- 评测场景: proof sketches and economic penalty reasoning
- Benchmark/应用: cryptocurrency ledger
- 别名: Tendermint consensus
- 相邻方向: PBFT, DLS partial synchrony, Casper FFG, HotStuff
- 置信度: high
- 分类理由: title/abstract/sections all identify mining-free blockchain consensus based on Byzantine consensus
- 分类状态: accepted
- 分类证据: title, abstract, full PDF deep read

## 一句话贡献

Tendermint 将 DLS-style partial-synchrony BFT 改造成 bonded validator blockchain consensus，用 propose/prevote/precommit/commit rounds、2/3 voting power finality、locking/proof-of-lock 和 slashing evidence 替代 proof-of-work mining 来保护短期 double-spend。

## 问题设定

目标是维护去中心化交易账本，在 malicious Byzantine validators 可能偏离协议时防止 double-spend。PoW 的外生成本、安全阈值和确认延迟不易量化；Tendermint 试图用 bonded stake 的内生惩罚和 BFT finality 给出更清晰的安全边界。

## 方法概览

### 组成部分

- Blockchain state: blocks, transactions, block hash, state hash, validation hash。
- Validator set: bonded accounts with voting power。
- Votes: prevote, precommit, commit。
- Quorum: 2/3 voting power for finality; 1/3 duplicitous signing as fork evidence threshold。
- Protocol steps: propose, prevote, precommit, commit, new height。
- Safety devices: locks, proof-of-lock, evidence transactions, unbonding period。

### 流程或协议

1. 每个 height 从 `NewHeight` 开始，按 round 运行。
2. 当前 round proposer 广播 block proposal；若已有 lock，附带 proof-of-lock。
3. Validators prevote proposal、locked block 或 nil。
4. Validators 看到某 block 超过 2/3 prevotes 后 precommit 并 lock；看到 nil 超过 2/3 prevotes 则 unlock。
5. 节点看到某 block 超过 2/3 precommits 后进入 commit；收到 block 和超过 2/3 commits 后 finalize。
6. 若看到更高 round 的 proof-of-lock，可以解锁旧 round lock。

### 关键定义、公式、算法或定理

- Fork condition: two 2/3 commit sets at same height imply at least 1/3 voting power signed duplicitously。
- Fault threshold: tolerates less than 1/3 Byzantine voting power。
- Partial synchrony: unknown finite message delay bound plus sufficiently accurate local clocks during a height。
- Round time increases by a small fixed increment so the network can eventually make progress。

### 假设条件

- Validators 的 voting power 由 bonded coins 决定。
- Evidence can be committed before unbonded coins are spent for short-range penalties。
- Network is partially synchronous, not fully asynchronous。
- Good validators follow locking/unlocking rules。

## 创新点

- 新思想: 用 bonded validator BFT finality 替代 PoW mining，并把短期 double-spend 成本转为可惩罚 stake。
- 对已有工作的扩展: 从 DLS partial synchrony BFT 改造到 gossip blockchain。
- 工程或实证贡献: block/validator/vote structures and round state machine sketch。
- 依赖的 prior work: Byzantine Generals Problem, DLS partial synchrony, FLP impossibility, Merkle trees。

## 实验与结果

- 实验设置: none。
- Baseline: Bitcoin/PoW, NXT, BitShares DPoS as motivating comparisons; not quantitatively evaluated。
- 指标: no measured metrics。
- 主要结果: safety/liveness proof sketches and economic penalty argument。
- 结果 caveat: Draft v0.6; sparse signatures and faster propagation are TODO; no implementation/performance evidence。

## 局限性

### 作者明确说明

- Long-range double-spend remains possible after validators unbond and sell coins; users should sync within the unbonding period。
- Sparse signature set and faster block propagation are TODOs。

### 基于证据的推断

- Safety/liveness 是 sketch 级，不是完整 formal proof。
- Cooperation analysis is stylized and assumes simple repeated interactions; it should not be promoted to full incentive compatibility theorem。
- 现代 Tendermint/CometBFT 的工程实践需要后续 sources。

## 可复用思路

- 把 BFT quorum intersection 与 slashing evidence 结合，形成可审计的 short-range finality。
- 用 lock/proof-of-lock 在 round-based BFT 中协调 safety 与 liveness。
- 将 unbonding period 作为安全窗口，明确 long-range attack 的 operational assumption。
- 在区块链知识图谱中把 `distributed-systems/consensus/byzantine-fault-tolerance` 桥接到 `blockchain-systems/consensus/proof-of-stake-finality`。

## 术语表

| Term | 解释 |
| --- | --- |
| validator | 锁定 bonded coins 并参与投票的账户/节点 |
| voting power | bonded coins 决定的投票权重 |
| 2/3 majority | 至少 2/3 total voting power |
| proof-of-lock | 支持某个 lock/unlock 状态的 prevote 集合 |
| short-range double-spend | guilty validators 仍在 unbonding window 内可被 slashed 的近期 fork |
| long-range double-spend | validators 已 unbond/sell stake 后发布历史 fork |

## 证据表

| Claim | Source location | Claim type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Tendermint aims to replace PoW mining with BFT blockchain consensus | p1 | design claim | high | abstract/introduction |
| Forks require at least 1/3 duplicitous signing under two 2/3 commit sets | p3-p4 | theorem/mechanism | high | quorum arithmetic |
| The protocol runs propose/prevote/precommit/commit/new-height rounds | p5-p8 | mechanism | high | core algorithm |
| Locks and proof-of-lock are safety/liveness devices | p6-p8 | mechanism | high | proof sketches |
| Liveness depends on partial synchrony and increasing round durations | p5, p8 | assumption/theorem sketch | medium-high | not full proof |
| Long-range attacks require periodic sync within unbonding period | p4 | limitation | high | author-stated |
| Sparse signature set and faster block propagation are unfinished | p9-p10 | limitation | high | TODO sections |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Tendermint proposes a blockchain consensus protocol without proof-of-work mining by adapting DLS-style partial-synchrony Byzantine consensus to bonded validators. | `sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p1`<br>`sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p4-p5` | folded_into_meta_note |
| In Tendermint, two committed blocks at the same height require at least one-third of validator voting power to have signed duplicitously. | `sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p3-p4` | folded_into_meta_note |
| Tendermint's liveness relies on partial synchrony, sufficiently accurate local clocks during a height, and rounds whose durations increase over time. | `sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p4-p5`<br>`sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p8` | folded_into_meta_note |
| Tendermint's locking and proof-of-lock rules prevent good validators from deciding conflicting blocks when Byzantine voting power is below one-third. | `sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p6-p8` | folded_into_meta_note |
| Tendermint determines each block height through rounds composed of propose, prevote, precommit, commit, and new-height steps. | `sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p5-p8` | folded_into_meta_note |
| Tendermint's draft mitigation for long-range double-spend attacks requires users to sync within the unbonding period so evidence can matter before guilty validators' coins are spendable. | `sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635#p4` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- Tendermint adapts partial-synchrony BFT to mining-free blockchain consensus.
- Two conflicting 2/3 commit sets imply at least 1/3 duplicitous validator voting power.
- Tendermint uses a propose/prevote/precommit/commit round protocol.
- Tendermint locking and proof-of-lock are the core safety/liveness coordination device.
- Tendermint liveness depends on partial synchrony and increasing round durations.
- Tendermint long-range attack mitigation depends on unbonding-period sync assumptions.

### Concepts to create or update

- Create [[proof-of-stake-finality]] as `blockchain-systems/consensus` topic concept.
- Create [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint]] as protocol concept.
- Create [[proof-of-stake-finality]] as economic/security mechanism seed.
- Update [[byzantine-fault-tolerance]] with blockchain source extension.

### Maps and bridges

- Create `blockchain-systems` domain seed.
- Create `blockchain-consensus` direction seed for domain-specific consensus.
- Create `proof-of-stake-finality` topic map and synthesis.
- Create bridge [[distributed-bft-to-blockchain-finality|Distributed BFT -> blockchain finality]].

### Review queue items

- Need DLS partial synchrony foundation source.
- Need modern Tendermint/CometBFT implementation source.
- Need Casper FFG next, already queued as item 0008.

## Synthesis Handoff

- Create `vault/04_Knowledge/blockchain-systems/blockchain-consensus/proof-of-stake-finality.md`.
- Keep foundation status `foundation_thin`; this is a seed, not full direction maturity.
- Mark blockchain consensus parent map as `seed` and queue HotStuff/Casper/modern Tendermint sources.
