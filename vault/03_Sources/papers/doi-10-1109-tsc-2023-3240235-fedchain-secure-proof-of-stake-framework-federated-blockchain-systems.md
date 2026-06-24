---
id: "doi:10.1109/tsc.2023.3240235"
title: "FedChain: Secure Proof-of-Stake-Based Framework for Federated-Blockchain Systems"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
source_kind: "paper"
source_subtype: "academic_paper"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage: "full_text_pdf_extraction"
safe_for_absorption: true
identity_key: "doi:10.1109/tsc.2023.3240235"
doi: "10.1109/tsc.2023.3240235"
arxiv_id: ""
canonical_url: "https://doi.org/10.1109/tsc.2023.3240235"
local_pdf: "~/Desktop/paper/FedChain_Secure_Proof-of-Stake-Based_Framework_for_Federated-Blockchain_Systems.pdf"
pdf_sha256: "366c7f96220fc1b0b11210e9d9a976dff066e13d0a2a8c1897e7e1989ca8d718"
extracted_text_path: "vault/02_Raw/pdf/extracted/fedchain_secure_proof-of-stake-based_framework_for_federated-blockchain_systems-366c7f96220f-pages.txt"
pdf_pages: 15
authors:
  - "Cong T. Nguyen"
  - "Dinh Thai Hoang"
  - "Diep N. Nguyen"
  - "Yong Xiao"
  - "Hoang-Anh Pham"
  - "Eryk Dutkiewicz"
  - "Nguyen Huynh Tuong"
venue: "IEEE Transactions on Services Computing"
year: 2023
publication: "IEEE Transactions on Services Computing 16(4):2642-2656"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "proof-of-stake-finality"
  - "federated-blockchain-systems"
  - "cross-chain-incentives"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols"
secondary_ontology_paths:
  - "blockchain-systems/consensus/proof-of-stake-finality"
classification_status: "refined_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Abstract and Section II define a federated-blockchain system and SPV-based cross-chain token transfer protocol"
  - "Section III defines FedChain's PoS consensus mechanism, CP/CG/CQ analysis, and attack boundaries"
  - "Section IV formulates a multiple-leaders multiple-followers Stackelberg game for stake distribution and block rewards"
  - "Section V evaluates security and performance under static/adaptive adversaries and static/dynamic rewards"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0064"
hierarchy_level: "source"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain-protocols"
  - "proof-of-stake-finality"
  - "federated-blockchain-systems"
  - "cross-chain-incentives"
aliases:
  - "FedChain"
  - "Federated-Blockchain Systems"
  - "Secure Proof-of-Stake-Based Framework for Federated-Blockchain Systems"
  - "Stackelberg game for federated blockchains"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "blockchain-systems/interoperability"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-fedchain"
source_refs:
  - "doi:10.1109/tsc.2023.3240235"
confidence: "high"
trust_tier: "primary"
---

# FedChain: Secure Proof-of-Stake-Based Framework for Federated-Blockchain Systems

## 论文身份

| Field | Value |
| --- | --- |
| Title | FedChain: Secure Proof-of-Stake-Based Framework for Federated-Blockchain Systems |
| Authors | Cong T. Nguyen; Dinh Thai Hoang; Diep N. Nguyen; Yong Xiao; Hoang-Anh Pham; Eryk Dutkiewicz; Nguyen Huynh Tuong |
| Venue | IEEE Transactions on Services Computing 16(4):2642-2656 |
| DOI | `10.1109/tsc.2023.3240235` |
| Year | 2023 |
| Local PDF | `~/Desktop/paper/FedChain_Secure_Proof-of-Stake-Based_Framework_for_Federated-Blockchain_Systems.pdf` |
| SHA-256 | `366c7f96220fc1b0b11210e9d9a976dff066e13d0a2a8c1897e7e1989ca8d718` |

## 精读状态

- Reading depth: `deep_read_complete`.
- 覆盖范围: 全文 15 页，包含 introduction、related work、federated-blockchain system model、SPV cross-chain transfer protocol、PoS consensus mechanism、security/performance analysis、Stackelberg game formulation、simulation evaluation、conclusion 和 references。
- 抽取质量: 文本抽取可用，页面边界完整；公式、表格和作者简介有少量排版噪声。在线 supplemental appendices 没有包含在 PDF 正文中，因此附录证明只按正文 theorem statement 和 proof sketch 记录。
- Absorption decision: 作为 [[cross-chain-protocols|Cross-chain protocols]] 的 source extension 吸收，并通过 [[proof-of-stake-finality|Proof-of-stake finality]] 与新的 [[proof-of-stake-finality-to-cross-chain-protocols|Proof-of-stake finality -> cross-chain protocols]] bridge 记录共识/激励对跨链安全的依赖。不新建同名 `FedChain` 知识节点，因为 reusable 层是“跨链协议依赖底层链安全、PoS finality 和 stake distribution incentives”，不是论文系统名本身。

## 章节地图

| Section/Page | 内容 | 记忆锚点 |
| --- | --- | --- |
| p1-p3, Section I | 动机、贡献和 related work：中心化交易所风险、sidechain/PoA/strong federation/PoS sidechain/zk-SNARK sidechain 方案边界。 | cross-chain motivation; related boundary |
| p3-p4, Section II | Federated-blockchain system：多条由 operators 管理的链，stakeholders 可在任意链投资并参与共识；给出 SPV-based cross-chain transfer 流程。 | federated system; SPV transfer |
| p4-p8, Section III | FedChain PoS consensus：epochs/time slots、PVSS randomness、FTS leader/committee selection、rules I1-I4、static/adaptive adversaries、CP/CG/CQ、attack prevention 和 confirmation-time analysis。 | PoS finality; CP/CG/CQ |
| p8-p10, Section IV | Stackelberg game：chains as leaders、stakeholders as followers、reward strategy、stake allocation、Nash equilibrium、Stackelberg equilibrium。 | stake distribution incentives |
| p10-p13, Section V | Evaluation：stake utility、stake distribution、CP/CQ violation probability、confirmation time、throughput reduction under static/adaptive adversaries and static/dynamic rewards。 | dynamic reward evaluation |
| p13, Section VI | 总结：FedChain 组合 cross-chain transfer、PoS consensus、Stackelberg incentives 和 simulations。 | conclusion |
| p13-p15 | References and bios。 | related sources |

## 一句话贡献

FedChain 把 federated-blockchain 中的跨链 token transfer、每条链的 PoS consensus security、以及跨链 stake/reward 分布激励放在同一个框架里：SPV 负责转移证明，PoS consensus 负责各链的 chain security，Stackelberg reward model 负责避免 stake 过度集中到单条链导致“最弱链”拖垮整体跨链安全。

## 核心问题设定

论文的问题不是单纯“跨链转账怎么做”，而是：

- 多个独立 blockchain networks 之间需要转移 tokens，但中心化交易所有被盗、托管和单点信任风险。
- Cross-chain transfer 的 SPV proof 安全性依赖源链本身安全；如果某条链被攻破，整个 federated system 的安全都会受影响。
- Federated-blockchain 允许 stakeholders 在多条链之间自由分配 stake；如果 block rewards 设计不当，stake 可能集中到某条收益高的链，让其他链变弱。
- 因此跨链系统要同时解决三层问题：cross-chain transfer protocol、individual-chain PoS consensus security、multi-chain incentive/stake distribution。

## Federated-Blockchain System

FedChain 的系统由 `M` 条 blockchain networks 和 `N` 个 stakeholders/users 构成：

- 每条 chain 有自己的 tokens、共识机制和 chain operator。
- Stakeholders 可以在任意 chain 上投资 stake，参与 leader/committee selection 并获得 block rewards。
- 用户可通过智能合约在两条链之间转移 token。
- 论文把 transfer ratio/exchange rate 作为链之间预先协商的参数，由 source/destination chain 上的 smart contracts 承接。

这个模型不等同于 permissioned bridge：它有 chain operators，但核心安全推理围绕 PoS stakes、stakeholders、leader/committee selection 和 adversarial stake ratio 展开。其 reusable placement 更适合连接 [[cross-chain-protocols|cross-chain protocols]] 与 [[proof-of-stake-finality|PoS finality]]。

## SPV Cross-Chain Transfer Protocol

FedChain 的 cross-chain transfer 是 SPV-style route：

| Step | 机制 | 安全边界 |
| --- | --- | --- |
| SC0 | 两条链协商 exchange rate，并分别部署 smart contracts。 | exchange rate 和合约初始化是链间 governance/setup 边界。 |
| SC1 | User 在 source chain 把 tokens 转给 source smart contract。 | source-chain transaction inclusion 和 confirmation 需要源链安全。 |
| SC2 | User 在 destination chain 提交 claim transaction 与 source-chain proof。 | destination contract 必须能验证 source transaction/SPV proof。 |
| SC3 | Destination smart contract 检查 proof validity 和 conflict during confirmation。 | 如果 source chain consensus 被破坏，SPV proof 可能变得不可信。 |
| SC4 | Confirmation 后 destination smart contract 释放相应数量的 tokens。 | 目标链执行正确性和合约余额/铸造规则仍是应用边界。 |

论文强调：SPV proof 的 correctness depends on the security of the originating chain。因此 FedChain 后续把重点转向 individual-chain PoS consensus 和激励机制。

## FedChain PoS Consensus Mechanism

FedChain 的共识机制运行在 epochs 和 time slots 上：

- 每个 epoch 包含多个 slots；每个 slot 有一个 designated leader 负责生成 block。
- 系统用 PVSS 生成 unbiased randomness。
- Follow-the-Satoshi (FTS) 根据 stake proportion 选择 leaders 和 committee members。
- Leaders 和 committee members 需要锁定 stakes；这用于抑制 long-range/bribe 等攻击。

### 四条规则

| Rule | 内容 | 作用 |
| --- | --- | --- |
| I1 | PVSS 后广播 leader list。 | 让参与者知道每个 slot 的 leader。 |
| I2 | 如果 designated leader 没有 broadcast block，则加入 empty block。 | 避免 leader failure 停止 chain growth。 |
| I3 | Leader 一旦 broadcast block，之后不能改变该 block。 | 抑制 equivocation/rewriting。 |
| I4 | Honest users adopt the longest valid fork：没有 conflicting blocks，且每个 block 由 designated leader 签名。 | 给出 fork-choice 和 validity 规则。 |

### Adversary model

论文考虑两类 adversaries：

- `static adversary`: 以固定 stake budget 攻击链。
- `adaptive adversary`: 可腐化若干 stakeholders，使其 stakes 变成 adversarial stakes。

攻击类型包括 double-spending、grinding、nothing-at-stake、bribe、transaction denial 和 long-range attacks。

### 安全性质

论文沿用 blockchain backbone/PoS analysis 中的三类性质：

| Property | 论文用途 | FedChain 机制关联 |
| --- | --- | --- |
| Common Prefix (CP) | 限制 honest users 的 chain views 出现深度分叉。 | 用 adversarial ratio 和 confirmation depth `kappa` 控制 violation probability。 |
| Chain Growth (CG) | 保证链持续增长。 | Empty-block rule 让 designated leader failure 不阻断增长。 |
| Chain Quality (CQ) | 保证 honest blocks 在窗口中占有足够比例。 | Stake-weighted leader selection 和 adversarial ratio 决定。 |

正文给出 theorem statements：

- Theorem 1: FedChain consensus satisfies CP, CG, CQ with probabilities tied to adversarial ratio, `kappa`, and slot/window parameters。
- Theorem 2: 在所考虑 adversary models 下，FedChain 可防 double-spending、nothing-at-stake、bribe、transaction denial、grinding 和 long-range attacks；详细证明在 online supplemental appendices。

重要边界：PVSS randomness 在 adversary controls more than 50% stakes 时不再保证 unbiased randomness；因此吸引并分散 stake 是 security requirement，不只是经济优化。

## Performance Analysis Before Incentives

论文将 FedChain consensus 的 transaction confirmation time 与 Bitcoin/PoW 和 Cardano/PoS delayed-finality 进行比较。计算方式是找到让 `PrCP <= 0.1%` 的 confirmation depth `kappa`，再乘以 20 秒 slot duration。

结论是：

- adversarial stake ratio 越高，达到同等 CP violation probability 所需 confirmation time 越长。
- 如果 adversary 控制超过 50% stake，FedChain 的 PVSS randomness 假设失效。
- 因此 individual chains 必须吸引足够 stakes，并避免 stakes 过度集中到少数链。

这直接引出 Stackelberg incentive mechanism。

## Stackelberg Game Formulation

FedChain 的激励问题被建模为 multiple-leaders-multiple-followers Stackelberg game：

- Leaders: chains / chain operators，先宣布 block rewards `R = (R_1, ..., R_M)`。
- Followers: stakeholders，随后决定把预算 stakes `B_n` 投资到哪些 chains。
- Stakeholder `n` 在 chain `m` 投资 `s_n^m`，其 expected payoff 为：

```text
U_n^m = s_n^m / (s_n^m + sum_{i in N-n} s_i^m) * R_m
```

总 payoff 是所有 chains 上 payoff 之和，且 `sum_m s_n^m <= B_n`。

### Follower sub-game

论文给出以下结果：

| Theorem | 结论 | 作用 |
| --- | --- | --- |
| Theorem 3 | Follower sub-game 至少存在一个 Nash equilibrium。 | 证明策略空间和 utility 适合 equilibrium analysis。 |
| Theorem 4 | Follower sub-game equilibrium 唯一，且收敛有保证。 | 让 stake allocation 可预测。 |
| Theorem 5 | Rational stakeholder 总会投资全部 budget。 | 可移除少投策略，简化效用函数。 |
| Theorem 6 | 唯一 equilibrium 满足 `s_n^{*m} = B_n R_m / sum_i R_i`。 | Stake allocation 与 reward ratio 成正比。 |

核心含义：如果某条链 block reward 更高，stakeholders 会按比例把更多 stake 投到该链；因此 reward design 直接控制跨链系统的 stake distribution。

### Leader strategy

Chain operators 的 utility 设计有两个目标：

- 吸引更多 stakes，提高 individual chain 的 security/performance。
- 鼓励 stakes 在多条 chains 之间均匀分布，避免 centralization。

论文将 leader utility 写成 stakeholders' stakes 的 log-weighted benefit 减 block reward，并给出 Theorem 7：

- Theorem 7: 存在唯一 Stackelberg equilibrium，所有 chain operators 的 optimal reward 形式相同；stakeholders 的 optimal strategies 仍满足 reward-ratio allocation。

论文解释：因为 tokens 可跨链转移，整个系统的安全性 as strong as that of the weakest chain；所以所有 chains 需要均衡安全，而不是让单条链吸走大部分 stake。

## Evaluation

评价分两部分：

### Economical benefits and stake distribution

- 小规模示例中，stakeholder 1 在按 Theorem 6 的策略投资时达到最大 utility `U_1^* = 15`，对应 `s_1^* = [16.6, 33.3, 50]`，与 reward ratio `[10, 20, 30]` 一致。
- 多 epoch simulation 显示，在 dynamic reward scheme 下，stakes across chains 更均匀；static reward scheme 更容易产生弱链。

### Security and performance metrics

论文模拟 static/adaptive adversaries、weak/medium/strong adversarial levels、static/dynamic reward schemes，观察：

- `PrCP`: Common Prefix violation probability。
- `PrCQ`: Chain Quality violation probability。
- transaction confirmation time。
- transaction throughput reduction threshold。

主要结果：

| Metric | 结果 | 论文解释 |
| --- | --- | --- |
| `PrCP` | adversary 越强，CP violation probability 越高；dynamic reward 比 static reward 更低，例如文中给出 dynamic scheme at most 14% vs static weakest chain 24% 的对比。 | dynamic reward 让 stakes 更均匀，减轻最弱链风险。 |
| `PrCQ` | adaptive adversary 场景通常更高；dynamic reward 同样改善 weakest-chain security。 | adaptive adversary 可腐化 high-stake stakeholders。 |
| Confirmation time | weak static adversary 下最多约 120 秒，strong static adversary 下可到 220 秒。 | adversary 增强会提高达到 CP 安全阈值所需等待时间。 |
| Throughput reduction | weak static adversary 最多约 24%，strong static adversary 接近 50%。 | adversarial leaders 可创建 empty blocks，降低吞吐。 |

## 关键限制与边界

- FedChain 的 cross-chain transfer 是 token transfer + SPV proof route，不覆盖 arbitrary cross-chain messaging、privacy-preserving bridge、complex cross-chain deals 或 relayer task allocation。
- SPV security 依赖 source chain security；如果某条链被攻破，整个 federated-blockchain system 可能失败。
- PoS analysis 依赖 adversarial stake ratio；PVSS 在 adversary 超过 50% stake 时失去 unbiased randomness 保证。
- 详细 theorem proofs 在 online supplemental appendices，不在本 PDF 正文；source note 只把正文 theorem statements 和 proof intent 作为证据。
- Evaluation 是 simulation/analysis，不是生产部署。
- Stackelberg model 假设 rational stakeholders 按 reward ratios 投资；真实 staking 可能受流动性、锁定期、治理、MEV、交易费和外部市场风险影响。

## Evidence Table

| Claim | Evidence anchor | Confidence | Notes |
| --- | --- | --- | --- |
| FedChain combines cross-chain transfer, PoS consensus and Stackelberg incentives. | Abstract; p1-p3 Introduction; p13 Conclusion | high | 作者明确列为贡献。 |
| Cross-chain transfer uses SPV proof between source and destination smart contracts. | Section II, p3-p4 | high | Transfer steps SC0-SC4。 |
| SPV transfer security depends on originating chain security. | Section II and Section III transition | high | 这是 FedChain 转向 consensus design 的理由。 |
| Consensus uses PVSS randomness and FTS stake-proportional leader/committee selection. | Section III, p4-p6 | high | 机制细节来自正文。 |
| FedChain argues CP/CG/CQ and prevention of several blockchain-specific attacks. | Section III-B, Theorem 1/2, p6-p8 | medium-high | 详细证明在 supplemental appendices。 |
| Stakeholder equilibrium allocates stake proportional to block rewards. | Section IV-B, Theorem 6, p8-p9 | high | 公式 `s_n^{*m} = B_n R_m / sum_i R_i`。 |
| Dynamic reward improves stake distribution, security and performance compared with static reward. | Section V, Figures 6-14, p10-p13 | high | 仿真支持，非生产实测。 |

## Knowledge Handoff

| Target | Handling | Delta |
| --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | source_extension | 新增 PoS-secured federated-chain transfer route：SPV proof 只是 transfer layer，系统安全还依赖每条链的 PoS finality 和 stake distribution。 |
| [[interoperability|Blockchain interoperability]] | source_extension | 新增 federated-blockchain interoperability 信号：跨链互操作不只验证消息/状态，还要管理 weakest-chain security 和 incentives。 |
| [[proof-of-stake-finality|Proof-of-stake finality]] | source_extension | 新增 PVSS + FTS + CP/CG/CQ + attack-prevention 的 PoS consensus route，并强调跨链场景中的 weakest-chain boundary。 |
| [[blockchain-consensus|Blockchain consensus]] | source_extension | 补充 PoS consensus route as cross-chain security substrate，不创建 FedChain 同名节点。 |
| [[proof-of-stake-finality-to-cross-chain-protocols|Proof-of-stake finality -> cross-chain protocols]] | new bridge | 记录跨链协议的 SPV/claim correctness 依赖 source-chain PoS finality、confirmation depth 和 stake distribution。 |

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence |
| --- | --- | --- | --- |
| Research field/domain | `blockchain-systems` | IEEE TSC blockchain/federated-blockchain paper | high |
| Research background | cross-chain token transfer, sidechains, PoS consensus, decentralized exchanges | Introduction and related work | high |
| Reusable problem | secure cross-chain transfer under weakest-chain consensus and stake centralization risks | Sections II-IV | high |
| Foundation concepts | cross-chain protocols, SPV, proof-of-stake finality, CP/CG/CQ, Stackelberg game | Sections II-IV | high |
| Method family | SPV transfer + PoS consensus + dynamic reward/incentive mechanism | Abstract; Sections II-IV | high |
| Application/evaluation context | federated-blockchain token transfer; static/adaptive adversary simulation | Section V | high |
| Source instance | FedChain framework | whole paper | high |

## Promotion Decisions

| Candidate | Generality | Decision | Reason |
| --- | --- | --- | --- |
| FedChain | paper/system instance | source_extension | 只有这一篇 source；作为框架名保留在 source note 和代表 source 行。 |
| Federated-blockchain systems | topic/query key | source_extension + watch term | 可复用但当前 vault 证据不足以拆独立 topic node。 |
| PoS-secured cross-chain transfer | method route | knowledge section + bridge | 连接 cross-chain protocols 与 PoS finality，能降低未来查询成本。 |
| Stackelberg game incentives | mechanism family within this source | source note detail + knowledge row | 当前只是 FedChain 激励机制，不应单独建 blockchain incentive foundation。 |

## Review Items

| Item | Reason | Proposed follow-up |
| --- | --- | --- |
| Queue metadata year/title/arXiv noise | 队列把标题抽成 IEEE 页眉，把 year 记为 2024，并误提取 `2023.32402` as arXiv-like id。 | 已在 source note 修正为 title/year/DOI；queue 可保留原始 metadata，但 classification evidence 记录 refined。 |
| Federated-blockchain systems node | 该词可能是 future topic，但当前只由 FedChain 支撑。 | 等更多 federated/sidechain/relay-chain sources 后复核 split gate。 |
| Blockchain incentive mechanism foundation | Stackelberg game 是通用方法，但 vault 目前没有 cryptoeconomics/incentives hierarchy。 | 后续若吸收 staking/reward/MEV/incentive papers，再建 `blockchain-systems/cryptoeconomics`。 |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-fedchain | Created deep-read source note and handed off to Source + Knowledge + Bridge architecture. | codex |
