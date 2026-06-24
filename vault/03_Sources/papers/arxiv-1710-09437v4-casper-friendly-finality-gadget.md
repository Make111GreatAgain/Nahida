---
id: "arxiv-1710.09437v4"
title: "Casper the Friendly Finality Gadget"
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
  - "p1-p2 abstract, introduction, PoS schools, Casper as finality overlay, accountability/dynamic validator/defense goals"
  - "p2-p5 Casper protocol, checkpoint tree, votes, supermajority links, justified/finalized checkpoints, two commandments, accountable safety and plausible liveness"
  - "p5-p6 fork-choice rule and dynamic validator sets with forward/rear validator stitching"
  - "p6-p8 long-range revision defense and timestamp/sync assumptions"
  - "p8-p10 catastrophic crashes, inactivity leak, conclusions, future work and references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1710.09437v4"
doi: ""
arxiv_id: "1710.09437v4"
venue: "arXiv"
year: "2019"
pdf_pages: 10
pdf_sha256: "ad23c56c5bd4be231e00d8527df361f4c128d8c02db77aad1942482b11d1a345"
local_pdf: "~/Desktop/paper/1710.09437v4.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/1710.09437v4-ad23c56c5bd4-pages.txt"
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
primary_ontology_path: "blockchain-systems/consensus/proof-of-stake-finality/arxiv-1710.09437v4"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/arxiv-1710.09437v4"
path_update_status: "propagated"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "proof-of-stake-finality"
  - "casper-ffg"
  - "byzantine-fault-tolerance"
aliases:
  - "Casper FFG"
  - "Friendly Finality Gadget"
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
    - "proof-of-stake finality"
    - "finality overlay"
    - "accountable safety"
    - "long-range revisions"
    - "catastrophic crashes"
  method_family:
    - "BFT proof-of-stake"
    - "checkpoint finality"
    - "slashing conditions"
    - "dynamic validator sets"
    - "inactivity leak"
  system_layer:
    - "finality gadget"
    - "validator set"
    - "fork choice"
  evaluation_context:
    - "accountable safety proof"
    - "plausible liveness proof"
    - "attack-defense reasoning"
  application:
    - "Ethereum hybrid PoW/PoS"
    - "block reversion protection"
  bridge:
    - "BFT consensus -> PoS finality overlay"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-casper-friendly-finality-gadget"
source_refs:
  - "arxiv:1710.09437v4"
  - "sha256:ad23c56c5bd4be231e00d8527df361f4c128d8c02db77aad1942482b11d1a345"
  - "pdf:~/Desktop/paper/1710.09437v4.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> consensus"
secondary_directions:
  - "distributed-systems -> consensus"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "arXiv ID"
  - "title"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0008"
queue_status: "absorbed"
---

# Casper the Friendly Finality Gadget

## 论文身份

- 标题: Casper the Friendly Finality Gadget
- 作者: Vitalik Buterin, Virgil Griffith
- 机构: Ethereum Foundation
- 会议/期刊: arXiv
- 年份: 2019
- arXiv: `1710.09437v4`
- 链接: https://arxiv.org/abs/1710.09437v4
- 本地 PDF: `~/Desktop/paper/1710.09437v4.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/1710.09437v4-ad23c56c5bd4-pages.txt`
- 代码/数据: unknown in PDF
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 10
- 已覆盖章节/页码: p1-p10 full text
- 已检查附录: 本 PDF 无附录
- 未覆盖章节/页码: 无
- Extraction gaps: 图注和公式换行有少量抽取噪声，但 theorem、definitions、slashing conditions 和 attack-defense sections 可读
- 精读说明: 论文覆盖 protocol、proof sketches、dynamic validator sets、long-range revisions、catastrophic crashes 和 future work，适合吸收到 PoS finality topic。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1-p2 | Abstract/Introduction | Casper as PoS finality overlay; PoS 两大路线；accountability/dynamic validators/defenses/modular overlay | 贡献定位 | 明确 liveness depends on proposal mechanism |
| p2-p4 | Casper Protocol | checkpoint tree, vote message, supermajority link, justified/finalized checkpoint | 核心定义 | checkpoint spacing 约 100 blocks |
| p4-p5 | Slashing + Proofs | two commandments; accountable safety; plausible liveness | 正确性核心 | Theorem 1/2 |
| p5 | Fork choice | follow chain containing justified checkpoint of greatest height | 协议规则 | 防止 Casper stuck |
| p6 | Dynamic validator sets | dynasty, start/end dynasty, withdrawal delay, forward/rear validator sets | validator churn | stitching prevents disjoint-set safety failure |
| p6-p8 | Long range revisions | no-revert-finalized fork choice, client periodic sync, timestamps, evidence inclusion assumptions | 攻击防御 | weak synchrony assumption |
| p8-p9 | Catastrophic crashes | >1/3 validators offline; inactivity leak; minority soft fork | liveness recovery | exact recovery algorithm open |
| p9-p10 | Conclusions/Future Work | Casper remains imperfect; future PoS proposal, formal fork choice, incentives | limitations | 51%/proposal compromise remains |

## 核心精读笔记

### 背景、动机与问题边界

Casper FFG 的定位不是从零构造一个完整区块生产协议，而是叠加在已有 proposal mechanism 上的 finality gadget。早期 Ethereum 场景里 proposal mechanism 可先由 PoW chain 承担，因此 Casper 负责在 block tree/checkpoint tree 中最终选择 canonical chain，并给已有 PoW 链提供额外 block reversion protection。论文明确区分 safety 与 liveness: Casper 可防止两个冲突 checkpoints 被 finalized，但若 proposal mechanism 被攻击者完全控制，它可能无法继续 finalize 新 checkpoints。证据锚点: p1-p2。

论文把 PoS 分成 chain-based PoS 与 BFT-based PoS 两条路线。Casper 选择 BFT tradition，但做了面向区块链的改造: accountability、dynamic validators、long-range revision/catastrophic crash defenses，以及作为 overlay 升级现有链的模块性。证据锚点: p1-p2。

### 模型、假设与定义

Casper 只在 checkpoint tree 上运行。Genesis 是 checkpoint，每 100 个 blocks 一个 checkpoint；checkpoint height 是从 root 到该 checkpoint 的 parent links 数量。Validator 有 deposit，文中的 `2/3 of validators` 是 deposit-weighted fraction，不是节点数。Vote message 形如 `<validator, source checkpoint, target checkpoint, h(source), h(target)>`，要求 source 是 justified checkpoint，target 是其 descendant。证据锚点: p2-p3。

Supermajority link `a -> b` 表示至少 2/3 deposit-weighted validators 投票从 source a 到 target b；link 可以跳过 checkpoints。Checkpoint justified 当它是 root，或存在来自已 justified checkpoint 的 supermajority link。Checkpoint finalized 当它已 justified，且有到 direct child 的 supermajority link。证据锚点: p3-p4。

### 方法、协议或系统机制

Casper 的核心 slashing 规则是两条 commandments。第一，validator 不得为同一个 target height 发两个不同 votes。第二，validator 不得投一个被另一个 vote 的 source-target 高度区间包住的 vote，即不得出现 `h(s1) < h(s2) < h(t2) < h(t1)`。任何违反任一条件的 validator 都会被 slashed。论文强调这些 slashing violations 与链状态无关，这也是从早期 Casper 版本减少消息类型和条件后的设计选择。证据锚点: p4。

Fork-choice rule 也需要配合 Casper: follow the chain containing the justified checkpoint of the greatest height。论文指出如果用户/validators/block proposers 仍按照 PoW longest-chain 规则，可能出现 Casper stuck 的病态场景，导致最长链上无法 finalized without altruistic sacrifice。该 fork-choice rule 来自 plausible liveness proof: 总能在最高 justified checkpoint 之上继续 finalize。证据锚点: p5。

Dynamic validator sets 通过 dynasty 处理。Validator deposit message 纳入 dynasty d 的 block 后，从 d+2 开始成为 validator；withdraw message 纳入 dynasty d 后，从 d+2 离开 validator set，之后还要经历 withdrawal delay。Casper 定义 forward validator set `Vf(d)` 和 rear validator set `Vr(d)`，要求 target 在 dynasty d 的 supermajority link 同时得到 forward/rear 两个集合各自 2/3 支持，以“缝合”validator set 变化，防止两个冲突 checkpoints 被 disjoint validator sets finalized 而无人可 slash。证据锚点: p6-p7。

### 理论、证明或正确性论证

Accountable safety: 在假设少于 1/3 validators by weight 违反 slashing conditions 下，两个冲突 checkpoints 不能都 finalized。证明利用两个 properties: distinct supermajority links 不可有相同 target height，否则触犯 commandment I；也不可形成 `h(s1)<h(s2)<h(t2)<h(t1)` 的嵌套区间，否则触犯 commandment II。由此每个 height 最多一个 supermajority link target、最多一个 justified checkpoint，进一步推出 conflicting finalized checkpoints 不可能同时存在。证据锚点: p4-p5。

Plausible liveness: 若存在 children extending finalized chain，则总能添加 supermajority links 产生新的 finalized checkpoints，且不违反 commandments。证明取最高 justified checkpoint `a` 和任何 validator 曾投过的最高 target checkpoint `b`；选择 `a` 的 descendant `a'`，其 height 为 `h(b)+1`，可先 justify `a'`，再通过其 direct child finalize `a'`。该性质是 “plausible” 而非完整 network liveness，因为它说明存在安全的投票路径，而实际出块活性仍依赖 proposal mechanism。证据锚点: p4-p5。

### 攻击防御、经济和系统边界

Long-range revisions: withdrawn validators 若过去曾拥有超过 2/3 deposits，可在没有 slash 风险后制造历史冲突 chain。Casper 的防御包括 fork choice never revert finalized block、客户端定期上线获取最新链视图、blocks timestamps，以及 evidence inclusion timeout 规则。论文给出一个 informal timing argument: 若最大通信延迟为 `delta`，withdraw delay `omega > 4 delta`，则 malicious validators 的 evidence 会在客户端接受的链上被纳入。证据锚点: p6-p8。

Catastrophic crashes: 若超过 1/3 validators 同时 crash/offline，无法创建 supermajority links，因此无法 finalized future checkpoints。Casper 提出 inactivity leak: 没有投票的 validators 每个 epoch 损失一部分 deposit，直到仍在线且投票的 validators 重新成为 supermajority。论文承认 inactivity leak 可能导致两个冲突 checkpoints without explicit slashing，但每个集合会在另一条链上因 leak 损失大量 deposit；精确恢复算法仍是 open problem，暂时依赖 validators 检测明显恶意行为和 minority soft fork。证据锚点: p8-p9。

### 作者结论与我的判断

Casper FFG 对 Nahida 的增量是把上一篇 Tendermint 的 PoS-BFT finality seed 细化成 “finality overlay” 模式: checkpoint finality、accountable safety、plausible liveness、fork choice、dynamic validator sets 和 failure recovery。它比 Tendermint draft 更明确地区分 proposal mechanism 与 finality gadget，也更系统地列出 PoS finality 的 long-range 和 catastrophic crash 边界。需要谨慎的是，论文也明确留下 future work: 纯 PoS proposal mechanism、动态权重下的 proof、formal fork choice、经济激励分析。证据锚点: p9-p10。

## 层级候选分类

- L1 Domain candidate: `blockchain-systems`
- L2 Direction candidate: `consensus`
- L3 Topic/content cluster candidates: `proof-of-stake-finality`, `casper-ffg`, `byzantine-fault-tolerance`
- Ontology path: `blockchain-systems/consensus/proof-of-stake-finality/arxiv-1710.09437v4`
- 备选归属: `distributed-systems/consensus/byzantine-fault-tolerance`
- 父级领域: blockchain systems
- 学术子领域: blockchain consensus, BFT proof of stake
- 任务/问题: finality overlay for PoW/PoS proposal mechanisms, block reversion protection
- 方法族: checkpoint finality, slashing conditions, dynamic validator sets, inactivity leak
- 模型/协议/算法族: Casper FFG
- 评测场景: theorem/proof sketches and attack-defense reasoning
- Benchmark/应用: Ethereum hybrid PoW/PoS path
- 别名: Casper FFG, Friendly Finality Gadget
- 相邻方向: Tendermint, PBFT, HotStuff, chain-based PoS
- 置信度: high
- 分类理由: title/abstract/sections all identify Casper as proof-of-stake finality system combining PoS and BFT
- 分类状态: accepted
- 分类证据: arXiv ID, title, abstract, full PDF deep read

## 一句话贡献

Casper FFG 提出一个叠加在区块 proposal mechanism 之上的 PoS finality gadget，用 checkpoint votes、两条 slashing commandments、highest-justified fork choice、dynamic validator set stitching 和 inactivity leak，在 BFT accountable safety 框架下增强现有链的 block reversion 防护。

## 问题设定

已有 PoW 链能提出 blocks，但缺少强 finality；PoS 需要避免 nothing-at-stake、long-range revisions 和大规模 validator offline 后的不可恢复。Casper 目标是在不完全替换 proposal mechanism 的情况下给链提供可追责 finality，并把违规行为转为可 slashing 的证据。

## 方法概览

### 组成部分

- Checkpoint tree: genesis plus every 100th block as checkpoint。
- Vote: `<validator, source, target, h(source), h(target)>`。
- Supermajority link: 2/3 deposit-weighted votes from source to target。
- Justified/finalized checkpoints: BFT-style finality state。
- Slashing conditions: no double vote by target height; no surround vote。
- Fork choice: highest justified checkpoint。
- Dynamic validator set: dynasties, forward/rear validator sets, withdrawal delay。
- Defenses: no revert finalized blocks, client sync, timestamps, inactivity leak。

### 流程或协议

1. Proposal mechanism produces a block tree。
2. Casper abstracts checkpoints from the tree。
3. Validators vote from justified source to descendant target。
4. Supermajority links justify targets; direct-child link finalizes source。
5. Fork choice follows chain with highest justified checkpoint。
6. Dynamic validator changes are delayed and stitched by forward/rear validator set requirements。
7. Slashing evidence punishes violations of commandments。

### 关键定义、公式、算法或定理

- Commandment I: no two distinct votes with same target height。
- Commandment II: no vote within the span of another vote。
- Accountable Safety: conflicting finalized checkpoints require at least 1/3 slashing violations。
- Plausible Liveness: safe supermajority links can always extend the finalized chain when proposal children exist。
- Dynamic sets: `Vf(d) = {v : DS(v) <= d < DE(v)}`, `Vr(d) = {v : DS(v) < d <= DE(v)}`。
- Long-range condition: informal defense requires withdrawal delay `omega > 4 delta` under timing assumptions。

### 假设条件

- Deposit-weighted validators and enforceable slashing。
- Proposal mechanism can provide children for finalized chain if liveness is desired。
- Clients follow Casper fork choice and periodically obtain updated finalized view。
- Dynamic validator transition data is included on chain before relevant checkpoints。

## 实验与结果

- 实验设置: none。
- Baseline: PoW proposal, Tendermint/BFT-style PoS, chain-based PoS discussed qualitatively。
- 指标: no measured performance metrics。
- 主要结果: Accountable Safety theorem, Plausible Liveness theorem, informal defenses for long-range revisions and catastrophic crashes。
- 结果 caveat: proof sketches and informal attack-defense reasoning; economic incentives left for future work。

## 局限性

### 作者明确说明

- Casper provides safety, but liveness depends on proposal mechanism。
- Compromised block proposal mechanism can prevent finalizing new blocks。
- Inactivity leak exact recovery algorithm remains open。
- Future work includes PoS proposal mechanism, dynamic-weight proofs, formal fork choice, and financial incentive analysis。

### 基于证据的推断

- Long-range defense relies on client sync and timing assumptions, not pure cryptographic finality。
- Inactivity leak may permit conflicting finalization without explicit slashing, so it is a recovery mechanism with safety tradeoffs。
- This source does not replace modern Ethereum proof-of-stake specifications.

## 可复用思路

- Separate proposal from finality to modularize blockchain consensus。
- Treat slashing conditions as state-independent evidence rules。
- Use accountable safety as a stronger retrieval concept than generic “BFT safety” for PoS protocols。
- Use dynamic validator set stitching as a pattern for membership changes under economic voting power。
- Model inactivity leak as a liveness-recovery mechanism with explicit safety/economic tradeoffs。

## 术语表

| Term | 解释 |
| --- | --- |
| Casper FFG | Casper the Friendly Finality Gadget, PoS finality overlay |
| checkpoint | every 100th block used by the finality gadget |
| supermajority link | 2/3 deposit-weighted votes from source checkpoint to target checkpoint |
| justified checkpoint | root or target of a supermajority link from a justified source |
| finalized checkpoint | justified checkpoint with a supermajority link to its direct child |
| accountable safety | conflicting finality implies slashable evidence against >=1/3 deposits |
| plausible liveness | safe extension is always possible if proposal children exist |
| inactivity leak | deposit leak for non-voting validators to recover liveness after >1/3 offline |

## 证据表

| Claim | Source location | Claim type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Casper is a PoS finality overlay on a proposal mechanism | p1-p2 | design claim | high | abstract and §1.1 |
| Casper finality uses checkpoints, votes and supermajority links | p2-p4 | mechanism | high | protocol definitions |
| Two slashing commandments support accountable safety | p4-p5 | theorem/mechanism | high | Figure 2 + Theorem 1 |
| Fork choice follows highest justified checkpoint | p5 | mechanism | high | correct-by-construction claim |
| Dynamic validator sets use forward/rear stitching | p6-p7 | mechanism | high | prevents disjoint-set safety failure |
| Long-range defense relies on no-revert-finalized and periodic client sync | p6-p8 | limitation/defense | high | informal proof |
| Inactivity leak addresses catastrophic crashes with tradeoffs | p8-p9 | mechanism/limitation | high | open recovery algorithm |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Casper handles validator-set changes by requiring supermajority links to satisfy both forward and rear validator sets for the target dynasty. | `arxiv:1710.09437v4#p6-p7` | folded_into_meta_note |
| Casper FFG provides safety as a finality overlay on top of a block proposal mechanism, while liveness still depends on that proposal mechanism producing suitable blocks. | `arxiv:1710.09437v4#p1-p2` | folded_into_meta_note |
| Casper's fork-choice rule follows the chain containing the justified checkpoint of greatest height, rather than the ordinary longest-chain PoW rule. | `arxiv:1710.09437v4#p5` | folded_into_meta_note |
| Casper's inactivity leak gradually reduces non-voting validators' deposits so the still-voting validators can again form a supermajority after more than one-third of validators go offline. | `arxiv:1710.09437v4#p8-p9` | folded_into_meta_note |
| Casper defends against long-range revisions by never reverting finalized blocks and expecting clients to periodically sync a complete up-to-date chain view within the withdrawal-delay assumptions. | `arxiv:1710.09437v4#p6-p8` | folded_into_meta_note |
| Casper's no-double-vote and no-surround-vote slashing conditions imply that conflicting finalized checkpoints require at least one-third of validator deposits to be slashable. | `arxiv:1710.09437v4#p4-p5` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- Casper is a finality overlay whose liveness depends on the proposal mechanism.
- Casper's two slashing conditions provide accountable safety.
- Casper's highest-justified-checkpoint fork choice follows from plausible liveness.
- Casper dynamic validator sets use forward/rear validator set stitching.
- Casper long-range revision defense relies on no-revert-finalized and periodic client sync.
- Casper inactivity leak recovers liveness after >1/3 validators go offline but introduces tradeoffs.

### Concepts to create or update

- Create [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper FFG]].
- Create [[proof-of-stake-finality]].
- Create [[proof-of-stake-finality]].
- Update [[proof-of-stake-finality]].
- Update [[proof-of-stake-finality]].
- Update [[distributed-bft-to-blockchain-finality]] bridge.

### Maps and syntheses

- Refresh [[blockchain-systems|Blockchain systems]], [[blockchain-consensus|Blockchain consensus]], [[proof-of-stake-finality|Proof-of-stake finality]].
- Refresh `vault/04_Knowledge/blockchain-systems/blockchain-consensus/proof-of-stake-finality.md`.

### Review queue items

- Need modern Ethereum PoS/spec source for post-Casper implementation status.
- Need HotStuff/modern BFT source for chained finality comparison.
- Need economic incentive source for Casper slashing and inactivity leak.

## Synthesis Handoff

- Refresh `proof-of-stake-finality-state-2026-06-11` from single-source Tendermint seed to two-source Tendermint + Casper seed.
- Keep `foundation_thin`; this is still not foundation_ready without DLS/FLP and modern protocol sources.
