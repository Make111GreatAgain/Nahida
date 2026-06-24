---
id: "sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
title: "zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing"
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
  - "p1-p2 abstract, introduction, contributions"
  - "p2-p4 blockchain/cross-chain background, related work, CLE/IPA/FAI challenges"
  - "p4-p6 models, zk-Rollup/zk-SNARK, HTLC, SPV preliminaries"
  - "p6-p10 zkCross architecture, transfer protocol, exchange protocol, auditing protocol"
  - "p11-p12 unlinkability and audit-efficiency analysis"
  - "p12-p14 implementation and performance evaluation"
  - "p14-p17 conclusion, acknowledgement, references"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown in extracted PDF; acknowledgement references USENIX Security shepherd/reviewers"
year: "2024"
pdf_pages: 17
pdf_sha256: "7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
local_pdf: "~/Desktop/paper/2024-888.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2024-888-7ab37dce93ba-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "zkp-blockchain-applications"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/blockchain-applications/sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
  directions:
    - "interoperability"
    - "applications"
  topics:
    - "cross-chain-protocols"
    - "cross-chain-privacy-preserving-auditing"
    - "zkp-blockchain-applications"
    - "zk-snarks"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
topics:
  - "cross-chain-protocols"
  - "privacy-preserving-auditing"
  - "zk-SNARK"
  - "zk-Rollup"
  - "HTLC"
  - "SPV"
  - "unlinkability"
  - "audit chain"
aliases:
  - "zkCross"
  - "cross-chain privacy-preserving auditing"
  - "CLE IPA FAI"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "interoperability"
  - "zero-knowledge-proofs"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
  subdomain:
    - "interoperability"
    - "applications"
  problem:
    - "cross-chain linkability exposure"
    - "incompatibility of privacy and auditing"
    - "full auditing inefficiency"
  method_family:
    - "zk-SNARK-based privacy-preserving cross-chain transfer"
    - "zk-SNARK-based privacy-preserving HTLC exchange"
    - "zk-Rollup-style audit aggregation"
    - "two-layer audit chain architecture"
  system_layer:
    - "cross-chain transfer"
    - "cross-chain exchange"
    - "audit chain"
    - "smart contracts"
  evaluation_context:
    - "modified go-ethereum and Solidity"
    - "xjsnark circuits"
    - "Groth16"
    - "local and 200-node cloud experiments"
  application:
    - "cross-chain privacy-preserving auditing"
    - "blockchain interoperability"
  bridge:
    - "zk-SNARKs to cross-chain privacy-preserving auditing"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-zkcross"
source_refs:
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "pdf:~/Desktop/paper/2024-888.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> interoperability"
secondary_directions:
  - "zero-knowledge-proofs -> applications"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Title, abstract and Section 3 identify cross-chain privacy-preserving auditing challenges"
  - "Sections 5-6 define cross-chain transfer, exchange and auditing protocols using zk-SNARKs"
  - "Section 7 evaluates implementation over local/cloud blockchain networks"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0023"
queue_status: "absorbed"
---

# zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing

## 论文身份

- 标题: zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing
- 作者: Yihao Guo, Minghui Xu, Xiuzhen Cheng, Dongxiao Yu, Wangjie Qiu, Gang Qu, Weibing Wang, Mingming Song
- 机构: Shandong University; Beihang University; University of Maryland; Cloud Inspur Information Technology Co., Ltd.
- 年份: 2024 from queue/local filename
- Venue/DOI/arXiv: extracted PDF 未给出；acknowledgement 提到 USENIX Security shepherd/reviewers，但不作为正式 venue 断言
- 本地 PDF: `~/Desktop/paper/2024-888.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/2024-888-7ab37dce93ba-pages.txt`
- SHA-256: `7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 17
- 已覆盖章节/页码: Abstract, Introduction, Background, Related Work and Motivations, Model and Preliminaries, zkCross protocols, Security Analysis, Performance Evaluation, Conclusion, References
- Extraction gaps: 图中电路细节可从正文和图注恢复核心输入/功能，但图像符号本身未做视觉复核；代码仓库 URL 在 PDF 中为匿名仓库。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | 提出 CLE、IPA、FAI 三个跨链隐私审计挑战；zkCross 两层架构和三协议 | high |
| §2 / p2-p3 | 背景 | Blockchain, permissionless/permissioned, cross-chain transfer/exchange | medium |
| §3 / p3-p4 | 相关工作与动机 | chain-based vs bridge-based cross-chain schemes；隐私、审计、效率缺口 | high |
| §4 / p4-p6 | 模型与预备知识 | 普通链/审计链、committer/auditor、Byzantine threshold、zk-Rollup/zk-SNARK、HTLC、SPV | high |
| §5.1 / p6-p7 | 架构总览 | lower ordinary chains + upper audit chain；ordinary chain state roots 进入 audit chain state tree | high |
| §5.2 / p7-p9 | 隐私跨链协议 | Transfer protocol Θ 隐藏 receiver/amount；Exchange protocol Φ 隐藏 HTLC preimage linkability | high |
| §5.3 / p9-p11 | 审计协议 | Auditing protocol Ψ 用电路合并 audit function、signature verification、state transition、root verification | high |
| §6 / p11-p12 | 安全分析 | Unlinkability theorem；audit efficiency theorem | medium-high |
| §7 / p12-p14 | 实现与实验 | xjsnark/Groth16/modified geth/Solidity；latency/TPS/gas/audit/storage results | high |
| §8 / p14 | 结论 | zkCross 同时支持 privacy protection 与 efficient auditing，未来增强抗攻击和多层审计 | medium |

## 一句话贡献

zkCross 把跨链隐私审计拆成三个问题: cross-chain linkability exposure、privacy/auditing incompatibility、full auditing inefficiency；它用两层 ordinary-chain/audit-chain 架构和三个 zk-SNARK-based protocols，使跨链 transfer/exchange 保持 unlinkability，同时让审计链用 succinct proofs 对多链交易进行高效全审计。

## 核心精读笔记

### 问题设定: CLE、IPA、FAI

论文的核心问题是跨链场景中隐私和审计同时存在却互相牵制。Cross-chain transfer/exchange 会在不同链上留下 sender、receiver、amount、preimage、state transition 等可关联线索；审计又需要透明性和 accountability。单链审计方案默认 auditor 能访问链内信息，但多链环境中 auditor 未必能访问其他链完整交易数据，尤其在 permissioned chain 中更明显。

作者提出三个挑战:

- Cross-chain Linkability Exposure (CLE): 攻击者通过 receiver address、HTLC preimage、transaction amount 等线索关联跨链交互双方。
- Incompatibility of Privacy and Auditing (IPA): 隐私协议减少信息暴露，而审计需要可验证信息；跨链已有隐私方案通常没有设计审计接口。
- Full Auditing Inefficiency (FAI): 多条异构链上的 full auditing 需要检查所有交易；若有 `k` 条链、每条单位时间 `n` 笔交易，relay-based full auditing 负担约为 `O(k * n)`，在大规模跨链场景不可扩展。

### 模型和架构

zkCross 使用两层架构。Lower layer 包含多个 ordinary chains，普通链可以是 permissionless 或 permissioned；ordinary chain 中的节点可作为 committer 聚合链相关数据。Upper layer 是 audit chain，包含 committers 和 auditors。Lower-layer committer 需要在 audit chain 注册成为 upper-layer committer，把普通链状态根和证明上传到审计链；auditors 验证这些证明并执行审计。

论文假设 ordinary chain 每条链至少有一个 honest committer。Permissioned blockchain 中外部 auditors 可能不能自由读取交易，只能通过 gateway 或 explorer 等辅助方式获得 block headers。Audit chain 是 permissionless blockchain，允许实体注册 committer。Threat model 允许 blockchain network 中节点 Byzantine，但不超过各链共识阈值，例如 PBFT 中小于三分之一，PoW 中不超过 50% 计算力。

### ZK/HTLC/SPV 预备知识

论文把 zk-SNARK-based zk-Rollup 抽象为三元组 `Π = (Setup, Prove, Verify)`。电路 `Λ` 约束 public input `x` 和 private witness `w` 的计算关系。zkCross 使用 zk-SNARK 的 succinctness、zero-knowledge、soundness 来把复杂验证转为短证明和低成本验证；具体实现使用 Groth16，但论文说明可按场景替换为 deVirgo 等证明系统。

HTLC 被用来实现 cross-chain exchange 的 atomicity；SPV/Merkle proof 被用来让轻节点验证交易在另一条链的区块中。zkCross 的关键不是重新定义这些基础构件，而是把它们组合成隐私和审计兼容的跨链协议。

### Privacy-preserving transfer protocol Θ

Cross-chain transfer 中，receiver address 和 transfer amount 都会暴露 linkability。zkCross 用两种手段处理:

- Receiver address: sender 在 burn transaction 中写入 `h(fpk_R, r, sn)`，其中 `r` 和 `sn` 是随机数，`r` 由 zk-SNARK 保护。
- Transfer amount: 使用 fixed denomination，把金额拆成标准面额，避免用独特金额匹配 burn/mint transaction。

协议 Θ 包含 Burn、Transmit、Mint、Redeem 四步。Burn 阶段 sender 在源链合约/账户锁定或销毁标准金额，并把 hash commitment 写入交易。Transmit 阶段 sender 把随机数、serial number 和 Merkle proof 离线发送给 receiver。Mint 阶段 receiver 构造电路 `ΛΘ`，用 public inputs `(fpk_R, sn, v, root_Burn)` 和 private inputs `(fpk_S, contract address, r, Merkle path)` 生成 proof，目标链合约验证后 mint 相同价值资产。Redeem 阶段如果 receiver 未按时 mint，sender 可用相似证明取回资产。

该协议保证结果只能是 receiver 成功获得资产，或 sender 超时赎回资产；不会因为隐私隐藏破坏结算正确性。

### Privacy-preserving exchange protocol Φ

Cross-chain exchange 基于 HTLC，但普通 HTLC 使用同一 preimage 生成两条链上的 hash locks，攻击者可通过同一 preimage/hash lock 关联双方账户。zkCross 采用 independent preimages + zk-SNARK proof 的方式，在保持 HTLC atomicity 的同时隐藏 linkability。

协议 Φ 包含 Prepare、Lock、Unlock、Refund。Prepare 阶段，sender 生成两个 preimages、两个 serial numbers，以及一个 256-bit `Z256`，其中 `snI XOR Z256 = snII`。Sender 通过 off-chain proof 证明两个 serial numbers 的关系，而不公开 `snI`。Lock 阶段双方分别用不同 hash lock 锁定资产。Unlock 阶段，先由一方用 on-chain proof 解锁并公开对应 serial number，另一方通过 `Z256` 恢复另一个 serial number，再生成自己的 proof 解锁。Refund 阶段若超时，则双方各自取回锁定资产。

该设计避免双方必须共享同一个 secret，也避免同一 preimage 直接暴露跨链 exchange 的关联关系。

### Cross-chain auditing protocol Ψ

协议 Ψ 解决 IPA 和 FAI。它将 auditing 和 aggregation 放进一个电路 `ΛΨ`，包含四类函数:

- Auditing Function (AF): 检查审计条件，例如地址是否在 blacklist，或金额是否合法。
- Signature Verification Function (SVF): 验证交易签名正确。
- State Transition Function (STF): 验证交易引起的 state transition 正确。
- Root Verification Function (RVF): 重新计算 state root，证明 old/new states 与普通链区块状态根一致。

Committer 对普通链某段交易和状态转移生成 proof。Public inputs 主要是旧 state root 和新 state root；transaction content、account states、signatures 等作为 private inputs。Auditors 或 audit-chain smart contract 验证 proof 后，把最新普通链 state root 存入 audit chain state tree。这样 auditors 不需要获得完整交易内容，也能验证审计条件和状态转移。

复杂审计任务可以聚合多个 proofs，例如审计某节点跨多个区块的总交易额。与逐交易 full auditing 相比，Ψ 把多交易审计压缩为 proof verification。

### 安全分析

论文证明 unlinkability 时考虑 receiver address、preimage 和 transaction amount 三类暴露源。Receiver address 通过 hash + zk-SNARK private input 隐藏；HTLC preimage linkability 通过 independent preimages 和 serial-number proof 消除；amount linkability 通过 fixed denomination 增大同额交易集合。证明假设 anonymity set `|U| > 1`；若某阶段只有唯一活跃 receiver，任何隐私方案都无法隐藏关系。

效率证明依赖 zk-SNARK succinctness。若网络有 `k` 条 ordinary chains，每条链每秒 `m` 个 blocks，每个 block 平均 `n` 笔 transactions，逐交易审计成本为 `t1 * k * m * n`，用 Ψ 审计为 `t2 * k * m`。因为 verification 时间与证明复杂度近似常数，论文称审计效率可近似提升 `n` 倍。

### 实现和实验

实现中 off-chain circuits 使用 xjsnark，约 1,500+ 行；证明系统使用 Groth16。On-chain 部分使用 go-ethereum 和 Solidity，约 500+ 行 Solidity；作者修改 geth/Solidity 以支持 zk-SNARK verification，并把验证 gas 设为 440,000 gas。

实验环境包括本地服务器和云服务器。本地服务器为 Intel Xeon Silver 4214R、98.3GB RAM、Ubuntu 20.04.2。云实验使用 50 台 ecs.g6.3xlarge，每台 12 vCPU/48GB RAM，单机启动 4 个 docker nodes，形成最多 200-node blockchain network；共识为 PoW；每条链 transactions 最多到 10,000。

ZK proof 性能上，`ΛΘ` 和 `ΛonΦ` 的 Setup/Prove 随 block size 从 16 到 256 近似线性增长，Verify 基本保持毫秒级。`ΛoffΦ` 的平均 Setup/Prove/Verify 分别为 6.96s、1.91s、5.16ms。

Transfer/exchange 协议实验中，两条链最多各 100 nodes，pending transactions 数为 nodes 的 10 倍。100 nodes 下:

- Θ: `TxBurn` latency 约 5.50s，`TxMint` 约 6.14s；TPS 分别约 45.78 和 32.58。
- Φ: `TxLock` latency 约 5.44s，`TxUnlock` 约 6.21s；TPS 分别约 48.38 和 32.55。
- Gas: Θ 约 494,000 gas，Φ 约 901,472 gas，按论文假设 gas price 和 ETH/USD 分别约 1.72 USD 与 3.13 USD。

Auditing 协议实验中，20-node audit chain 审计 sender 是否在 blacklist。`ΛΨ` 聚合交易数从 50 到 250 时，verification time 从 8.52ms 增至 16.43ms，proof size 保持 127.38 bytes。对比 full auditing，100 transactions 时不用 Ψ 约 35.66s，用 Ψ 约 1.10s；10,000 transactions 时不用 Ψ 因网络拥塞约 3.15 hours，用 Ψ 约 40s。Gas: Ψ 约 466,520 gas。与 zk-Rollup storage 对比中，Ψ 电路 constraints 略多，但 public inputs 和 verification key 明显更小，论文估计验证 100 transactions 可节省约 16KB 空间和约 1,000 万 gas。

## 可复用知识与来源内边界

### 可上升为 knowledge/source-extension 的内容

- Cross-chain protocols 需要分别处理 transfer 和 exchange；把二者用单一协议覆盖通常会引入第三方或牺牲安全/隐私边界。
- Cross-chain privacy-preserving auditing 的核心 tension 是 CLE、IPA、FAI: unlinkability、auditability、full auditing scalability 不能单独优化。
- zk-SNARK 的 zero-knowledge 和 succinctness 可分别用于隐藏跨链关系线索、压缩审计验证；但 SPV、HTLC、state root、audit chain 等仍是区块链语义。
- Fixed denomination 提升 amount privacy，但会增加交易数量；匿名集合大小是 unlinkability 的实际边界。

### 不应上升为基础概念的内容

- `zkCross` 是 source/system instance，不是 `cross-chain protocols` 或 `zk-SNARKs` 的基础概念。
- `Θ`、`Φ`、`Ψ` 是本文协议实例；除非后续多篇来源使用同类构造，否则保留在 source note 中。
- 本文实验基于修改的 go-ethereum/Solidity、PoW cloud setup 和 Groth16 gas 假设，不能直接代表所有 L1/L2 或生产 bridge 的成本。

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 knowledge/bridge 以 source-extension 形式引用。上层节点应引用本元笔记，而不是复制整篇协议细节。

| Evidence point | Source anchor | Handling |
| --- | --- | --- |
| zkCross 把跨链隐私审计挑战拆为 CLE、IPA、FAI。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p1-p4` | source_extension |
| 两层架构包含 lower ordinary chains 和 upper audit chain，ordinary chain state roots 作为 audit chain state tree leaves。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p4-p7` | source_extension |
| Θ 使用 zk-SNARK 隐藏 receiver address，用 fixed denomination 降低 amount linkability，同时保持 burn/mint/redeem 正确性。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p7-p8` | source_detail |
| Φ 使用 independent preimages、serial numbers 和 zk-SNARK proof 解除 HTLC same-preimage linkability，同时保持 exchange atomicity。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p8-p9` | source_detail |
| Ψ 将 auditing function、signature verification、state transition、root verification 合入电路，让 auditors 验证 proof 而不读取完整交易内容。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p9-p11` | source_extension |
| Unlinkability proof 依赖 hash collision resistance、zk-SNARK zero-knowledge 和匿名集合 `|U| > 1`。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p11-p12` | boundary |
| Audit efficiency theorem: full auditing `O(k*m*n)` 变为 proof verification `O(k*m)`，近似提升 `n` 倍。 | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p12` | source_extension |
| Evaluation reports 10,000 transactions audit time from about 3.15 hours without Ψ to about 40 seconds with Ψ. | `sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8#p13-p14` | evaluation |

## 概念与地图落点

| 层级 | 落点 | 说明 |
| --- | --- | --- |
| Primary topic | [[cross-chain-protocols|Cross-chain protocols]] | 跨链 transfer/exchange/auditing 中隐私、原子性和审计效率的共同问题 |
| Parent direction | [[interoperability|Blockchain interoperability]] | 区块链互操作方向下的跨链协议 source extension |
| Secondary topic | [[blockchain-applications|ZKP blockchain applications]] | ZK proofs 在 blockchain privacy/audit/interoperability 中的应用 |
| Foundation dependency | [[zk-snarks|zk-SNARKs]] | 本文使用 zk-SNARK/Groth16 作为证明后端，但不是 zk-SNARK foundation source |
| Bridge | [[zk-snarks-to-cross-chain-privacy-preserving-auditing|zk-SNARKs -> cross-chain privacy-preserving auditing]] | 证明系统能力到跨链审计问题的 application bridge |

## 适用边界

- 适用于有 cross-chain transfer/exchange/auditing 需求的 blockchain systems。
- 普通链可 permissionless 或 permissioned；audit chain 设计为 permissionless。
- 依赖至少一个 honest committer 和各链共识安全阈值。
- Unlinkability 依赖匿名集合大小、fixed denomination、hash/ZK 假设；唯一活跃 receiver 时不能隐藏 linkability。
- 审计效率来自 proof verification succinctness，但 proving/setup 成本转移到 off-chain committer。

## Path Materialization

| Path role | Ontology path | Action |
| --- | --- | --- |
| Primary | `blockchain-systems/interoperability/cross-chain-protocols/sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8` | source note written and attached as source extension |
| Secondary | `zero-knowledge-proofs/applications/blockchain-applications/sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8` | ZKP blockchain application evidence added |
| Dependency | `zero-knowledge-proofs/proof-systems/zk-snarks/sha256-7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8` | dependency/bridge evidence only, not foundation promotion |
| Bridge | `zero-knowledge-proofs/proof-systems/zk-snarks -> blockchain-systems/interoperability/cross-chain-protocols` | bridge evidence created |

## Path Propagation

| Target note | Planned update | Materiality |
| --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | add privacy-preserving auditing problem, CLE/IPA/FAI, source extension | material |
| [[interoperability|Blockchain interoperability]] | create direction and attach cross-chain protocol child | material |
| [[blockchain-applications|ZKP blockchain applications]] | create application node and add zkCross as source extension | material |
| [[zero-knowledge-proofs|Zero-knowledge proofs]] | add applications child/source extension lightly | light |
| [[zk-snarks|zk-SNARKs]] | add bridge link only; do not upgrade foundation status from this application source | light |

## 吸收结果

- Source note: written as complete meta/source note.
- Knowledge handoff: ready for `nahida-knowledge-get`.
- Promotion decision: no standalone foundation node for `zkCross`, `Θ`, `Φ`, or `Ψ`; create reusable problem/application nodes for cross-chain protocols and ZKP blockchain applications.
