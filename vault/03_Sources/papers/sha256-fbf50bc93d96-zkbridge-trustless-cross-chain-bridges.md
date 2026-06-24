---
id: "sha256-fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
title: "zkBridge: Trustless Cross-chain Bridges Made Practical"
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
  - "p1-p3 abstract, introduction, problem, approach, contributions"
  - "p3-p4 blockchain, light client and ZKP preliminaries"
  - "p4-p8 zkBridge protocol, security model, application contracts and use cases"
  - "p8-p10 deVirgo distributed proof generation"
  - "p10-p11 recursive proof compression with Groth16"
  - "p11-p13 implementation and evaluation"
  - "p13-p15 cost analysis, Ethereum-to-EVM direction, related work and references"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3548606.3560652"
doi: "10.1145/3548606.3560652"
arxiv_id: ""
venue: "ACM CCS 2022"
year: "2022"
pdf_pages: 15
pdf_sha256: "fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
local_pdf: "~/Desktop/paper/zkBridge_ccs22.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/zkbridge-trustless-cross-chain-bridges-made-practical-fbf50bc93d96-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "zkp-blockchain-applications"
  - "zk-snarks"
  - "recursive-proofs"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/sha256-fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/blockchain-applications/sha256-fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "zero-knowledge-proofs/proof-systems/sha256-fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "zero-knowledge-proofs/recursion-and-folding/sha256-fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
  directions:
    - "interoperability"
    - "applications"
    - "proof-systems"
    - "recursion-and-folding"
  topics:
    - "cross-chain-protocols"
    - "trustless-cross-chain-bridges"
    - "zkp-blockchain-applications"
    - "zk-snarks"
    - "distributed-proof-generation"
    - "recursive-proof-compression"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
topics:
  - "cross-chain-protocols"
  - "trustless bridges"
  - "light clients"
  - "zk-SNARK"
  - "deVirgo"
  - "Virgo"
  - "Groth16"
  - "recursive proofs"
  - "data-parallel circuits"
aliases:
  - "zkBridge"
  - "trustless cross-chain bridge"
  - "deVirgo cross-chain bridge"
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
    - "proof-systems"
    - "recursion-and-folding"
  problem:
    - "committee-based bridge trust assumptions"
    - "expensive on-chain light-client verification"
    - "large ZK circuits for validating blockchain signatures"
    - "posting/verifying large transparent proofs on-chain"
  method_family:
    - "zk-SNARK-based block-header relay"
    - "light-client correctness proof"
    - "distributed proof generation for data-parallel circuits"
    - "recursive proof compression"
    - "batched header verification"
  system_layer:
    - "block header relay network"
    - "updater contract"
    - "application contracts"
    - "Cosmos-to-Ethereum bridge"
    - "Ethereum-to-EVM-compatible bridge"
  evaluation_context:
    - "128 AWS EC2 c5.24xlarge instances"
    - "Cosmos to Ethereum prototype"
    - "deVirgo C++ implementation"
    - "Solidity updater contract"
    - "Gnark/Groth16 recursive proof"
  application:
    - "trustless cross-chain bridge"
    - "cross-chain message passing"
    - "cross-chain asset transfer"
    - "NFT interoperability"
  bridge:
    - "zk-SNARKs to trustless cross-chain bridges"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-zkbridge"
source_refs:
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "doi:10.1145/3548606.3560652"
  - "pdf:~/Desktop/paper/zkBridge_ccs22.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> interoperability"
secondary_directions:
  - "zero-knowledge-proofs -> applications"
  - "zero-knowledge-proofs -> proof-systems"
  - "zero-knowledge-proofs -> recursion-and-folding"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Title, abstract and introduction define trustless cross-chain bridge as the target problem"
  - "Section 3 defines bridge protocol over light-client correctness proofs and updater contract"
  - "Sections 4-5 define deVirgo and recursive proof compression for ZK performance"
  - "Section 6 evaluates a Cosmos-to-Ethereum prototype"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0024"
queue_status: "absorbed"
---

# zkBridge: Trustless Cross-chain Bridges Made Practical

## 论文身份

- 标题: zkBridge: Trustless Cross-chain Bridges Made Practical
- 作者: Tiancheng Xie, Jiaheng Zhang, Zerui Cheng, Fan Zhang, Yupeng Zhang, Yongzheng Jia, Dan Boneh, Dawn Song
- 机构: UC Berkeley; Tsinghua University; Yale University; Texas A&M University; Overeality Labs; Stanford University
- 年份/Venue: ACM CCS 2022
- DOI: `10.1145/3548606.3560652`
- 本地 PDF: `~/Desktop/paper/zkBridge_ccs22.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/zkbridge-trustless-cross-chain-bridges-made-practical-fbf50bc93d96-pages.txt`
- SHA-256: `fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 本地 PDF/extraction 为 15 页；ACM citation 文本标注 19 pages
- 已覆盖章节/页码: Abstract, Introduction, Background, zkBridge Protocol, Distributed Proof Generation, Recursive Proof Compression, Implementation and Evaluation, Cost Analysis, Ethereum-to-EVM direction, Related Work, Appendix snippets
- Extraction gaps: 图中流程可从正文和图注恢复；Appendix protocols 在提取文本末尾截取到主要协议定义和参考文献，已覆盖正文核心论证。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p3 | 问题、方法、贡献 | 跨链桥要么昂贵要么依赖委员会；zkBridge 用 succinct proofs 做 trustless bridge；贡献 zkBridge、deVirgo、递归压缩和 Cosmos/Ethereum 原型 | high |
| §2 / p3-p4 | 背景 | blockchain security, smart contract gas, light-client protocol, ZKP/SNARK 定义 | high |
| §3 / p4-p8 | 协议 | block-header relay network, updater contract, application contracts, security theorem, message/asset/NFT use cases | high |
| §4 / p8-p10 | deVirgo | 面向 data-parallel circuits 的 distributed Virgo，聚合 sumcheck 和 polynomial commitment，保持 proof size 可控 | high |
| §5 / p10-p11 | 递归压缩 | 用 Groth16 证明 deVirgo verification，把大 proof 压缩成 EVM 友好的常数大小 proof | high |
| §6 / p11-p13 | 实现与实验 | Cosmos->Ethereum prototype，128 AWS instances，deVirgo/RV proof time、proof size、gas、batching、cost | high |
| §6.4-§7 / p13-p15 | 反向桥与相关工作 | Ethereum->EVM-compatible chain 方向用 EthHash/Merkleized DAG；对比委员会桥、optimistic bridge、zk-rollup | medium-high |

## 一句话贡献

zkBridge 把跨链桥的正确性从委员会签名信任迁移到 sender chain light-client verifier + proof soundness：relayer 生成源链区块头状态转移的 ZK proof，目标链 updater contract 验证短 proof 并维护区块头状态；为让 PoS 签名验证这类大电路可用，论文提出 deVirgo 做 data-parallel distributed proof generation，再用 Groth16 递归压缩到链上可验证的 131-byte proof。

## 核心精读笔记

### 问题设定: 跨链桥的信任与成本

论文把 bridge 的核心功能抽象为: 让链 `C2` 上的应用相信链 `C1` 上某个事件或状态确实发生。朴素 light-client/SPV 方案可以减少第三方信任，但目标链 smart contract 要验证所有区块头和共识逻辑，尤其对 PoS/BFT 链会非常昂贵。论文给出的 Cosmos->Ethereum 场景中，直接在 Ethereum 验证单个 Cosmos block header 约需 64M gas。

现实系统常用 committee-based bridges，由 validator committee 对状态转移签名。这降低成本但引入额外信任假设，且小委员会会成为攻击面。论文用 Ronin、PolyNetwork、Wormhole 等攻击作为动机，认为桥接资产的安全性不应低于底层链本身。

### 目标和安全模型

zkBridge 的功能目标是 correctness 和 liveness:

- Correctness: receiver contract 不应接受与 sender chain 实际状态不一致的值。
- Liveness: 若 receiver contract 需要验证 sender chain 某个状态，bridge 最终能提供必要信息。

正确性不依赖 relay committee 的诚实多数，而依赖四个假设: sender/receiver chain 本身 consistent/live；sender chain 有安全 light-client verifier；succinct proof system sound；relay network 中至少一个 honest node 保障 liveness。Relay network 只为活性被信任，不能伪造通过 proof 的错误状态。

### 协议架构

zkBridge 由三层组件组成:

- Block header relay network: relayer 从 sender chain full nodes 获取新区块头，生成 `LightCC(LCS_{r-1}, blkH_{r-1}, blkH_r) -> true` 的 ZK proof，然后把 proof 和新区块头提交到目标链 updater contract。
- Updater contract: 维护 sender chain light-client state 和 headerDAG。`HeaderUpdate` 验证 proof 和父区块关系后更新状态；`GetHeader(t)` 向应用合约暴露区块头查询接口。
- Application contracts: 应用层合约用 updater contract 返回的区块头，再结合用户或第三方提供的 Merkle/state proof，完成交易 inclusion、资产 mint、消息传递等应用逻辑。

这个模块化设计很重要: bridge core 只负责 relay block headers with correctness proofs，不内置 token transfer、message passing 或 NFT 逻辑。应用合约的 state/Merkle proof 是应用层责任。

### 应用用例

论文给出三类上层用例:

- Transaction inclusion / message passing: 把 message 嵌入 sender chain 交易，receiver contract 用区块头和 Merkle proof 验证 inclusion。
- Cross-chain asset transfer/swap: sender chain 上 lock contract 锁定资产，receiver chain 上 mint contract 只有在验证 lock transaction inclusion 后 mint/transfer 对应资产。
- NFT interoperability: 在 sender chain 锁定 NFT ownership，在 receiver chain mint NFT derivative 或 utility，分离 ownership 和 utility。

这些用例都共享同一个底层: updater contract 提供源链可信区块头，应用合约自己验证具体状态或交易。

### 为什么需要 deVirgo

PoS/BFT sender chain 的 light-client verifier 通常要验证许多签名。Cosmos 使用 Curve25519/EdDSA，而 Ethereum EVM 原生支持 BN254。把 Curve25519 签名验证放进 BN254-friendly arithmetic circuit 会很大，单个 Cosmos signature verification 约 2M gates；验证 32 个签名约 64M gates。直接用传统 proof system 生成 proof 过慢。

论文观察到这类电路是 data-parallel: 验证 `N` 个签名就是 `N` 个相同子电路。deVirgo 基于 Virgo，把 prover work 分到多台机器，同时避免 naive distributed proof 的 proof size 线性膨胀。

deVirgo 的关键技术:

- Distributed sumcheck: 每台机器对自己的子电路生成 sumcheck message，master node 聚合成一个 verifier-facing univariate polynomial，因此每轮 proof size 不随机器数线性增长。
- Distributed polynomial commitment: 按 evaluation index 聚合不同机器的数据，让 verifier 用更少 Merkle path 验证多个 opening，避免 naive PC proof size 线性爆炸。
- 组合到 Virgo/GKR: 对 data-parallel layered arithmetic circuit，每层 sumcheck 和 PC 都采用 distributed version。

复杂度结论是: 总 prover work 近似不变，但单机 work 可降为 `O(|C|/N + m log m)`；proof size 仍保持在 `O(d log |C| + lambda(N + log^2 m))` 范围。论文强调 deVirgo 对 zkBridge 工作负载有近线性扩展，并可能对其他 data-parallel ZKP workload 有独立价值。

### 递归压缩: deVirgo + Groth16

deVirgo proof 在普通 CPU 上验证很快，但 proof size 和 verifier work 对链上合约仍太重。论文用两层 recursive proof:

1. 第一层用 deVirgo 为大规模 light-client computation 生成 proof `pi1`。
2. 第二层用 Groth16 为“`pi1` 是有效 deVirgo proof”这个 verification circuit 生成 proof `pi2`。
3. 目标链只验证 Groth16 proof。

这样得到两个互补优势: deVirgo 负责快速并行生成大电路 proof，Groth16 负责 EVM 友好的短 proof 和低 gas verification。论文报告递归后 proof size 约 131 bytes，链上验证约 221K gas；不用递归直接链上验证 Virgo/deVirgo proof 估计约 78M-79M gas，超过单区块 gas limit。

### 实现

论文实现了 Cosmos<->Ethereum 的双向 bridge，重点评估 Cosmos->Ethereum:

- Relayer: 300+ lines Python，获取 Cosmos block headers 并向 Ethereum 提交。
- deVirgo: 10000+ lines C++，用于 distributed proof generation。
- Recursive verification circuit: handcrafted，Groth16 proof generation 使用 Gnark。
- Updater contract: 600+ lines Solidity，验证 Groth16 proof 并存储 Cosmos block headers。

Cosmos block header 包含约 128 个 EdDSA signatures；用 top 32 signatures 可达到 super-majority stake。实现还支持 batching: updater contract 不逐个 block header 验证，而是验证一批 `B` 个连续 headers 的统一 proof，并只在链上存这批 headers 的 Merkle root。Batching 在延迟和成本之间提供可调旋钮。

### 实验结果

实验在 128 台 AWS EC2 c5.24xlarge instances 上运行，每台 Intel Xeon Platinum 8275CL CPU @ 3.00GHz、192GB RAM，报告 10 次平均。

deVirgo 与原始 Virgo 对比:

- 原始 Virgo prover time 随签名数线性增长；Cosmos block header 场景会超过 400s。
- deVirgo 在 128 machines 上验证 128 signatures 的 proof generation time 为 13.28s，约 30x speedup。
- 每台机器通信量约 1GB，总通信量随机器数线性增长，论文认为在 data-center-like relayer deployment 中可接受。

递归压缩结果:

- 32 signatures: deVirgo 12.80s，recursive verification proof 5.41s，总计 18.21s。
- 128 signatures: deVirgo 13.28s，recursive proof 5.49s，总计 18.77s。
- Proof size 从约 1.95MB 降到 131 bytes。
- On-chain verification 从约 78M-79M gas 降到 221K gas。

端到端/成本:

- Cosmos->Ethereum relaying transaction 约 221K gas；abstract/intro 中也给出 under 220K gas 量级。
- 批量 `N=32` headers 时，on-chain cost 约 `210K + 132K = 342K gas`，按论文 2022-08 假设约 $11/batch、$0.3/block。
- zkBridge batching 后 confirmation latency 小于 2 minutes，明显短于 optimistic bridge 的 challenge window 级延迟。
- Hetzner 32-machine deployment 估计约 $8100/month，约 $0.02/block；self-hosted 初始硬件约 $144K，电力约 $5184/month。

### Ethereum->EVM-compatible chains

反向方向从 Ethereum 到 EVM-compatible receiver chain 更容易，因为 proof workload 小得多，不需要 deVirgo。难点是 EthHash memory-hard hash 在链上计算昂贵。论文方案是在 setup 阶段离线预计算 2048 个 EthHash DAGs，为每个 DAG 建 MiMC Merkle tree 并把 roots 存到链上；每 30000 blocks 更新一个 DAG，2048 个 DAG 可覆盖约 10 年。具体 proof 证明 EthHash PoW 相对对应 DAG Merkle root 正确。EthHash PoW verification circuit 约 2M gates，单机可在 10s 内生成 proof。

### 与相关工作的边界

zkBridge 与 committee bridge 的区别是 correctness 不依赖 guardian/validator committee honest majority；与 optimistic bridge 的区别是无需长 challenge window 和高 collateral。与 zk-rollup 的区别是应用目标不同: zk-rollup 用 ZKP 批处理交易执行以扩展 layer-1，zkBridge 用 ZKP 证明另一条链的 light-client state transition。论文认为 deVirgo 的 data-parallel proof generation 思路可能反过来用于 zk-rollup workload。

## 可复用知识与来源内边界

### 可上升为 knowledge/source-extension 的内容

- Cross-chain protocols 中的 trustless light-client bridge 路线: 用 proof soundness 替代 committee trust。
- ZKP blockchain applications 中的 succinct cross-chain state verification: 把 on-chain light-client verifier 压缩成 proof verification。
- Proof systems 中的 data-parallel distributed proof generation 模式: 对重复子电路聚合 sumcheck/PC proof。
- Recursion and folding 中的 recursive proof compression: 用链上友好 SNARK 压缩透明/大 proof。

### 不应上升为独立基础概念的内容

- `zkBridge` 本身是 source/protocol instance，不是上层概念节点。
- `deVirgo` 当前只有本 source 直接支撑，先作为 source-contained protocol 和 proof-systems source extension；后续若有多来源再拆独立 node。
- 实验中的 221K gas、131 bytes、128 AWS machines 是 source evidence，不是普适常数。
- Cosmos/Ethereum 工程细节留在本 source note；上层节点只记录方法族和边界。

## 分层吸收映射

| Knowledge/Bridge target | 更新方式 | 吸收内容 | Source boundary |
| --- | --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | source extension | 新增 trustless bridge / light-client proof relay 路线，与 zkCross 的 privacy/audit 路线并列 | 不复制全部 deVirgo 细节 |
| [[blockchain-applications|ZKP blockchain applications]] | source extension | 新增 succinct light-client/state-transition verification 应用路线 | 不把 ZKP 应用等同 bridge correctness |
| [[zk-snarks|zk-SNARKs]] | bridge evidence only | 补充 zkBridge 使用 deVirgo + Groth16 组合，但不升级 zk-SNARK foundation | 不把 zkBridge 当 zk-SNARK 定义来源 |
| [[proof-systems|Proof systems]] | source extension | 记录 data-parallel distributed proof generation 的 evidence | deVirgo 不单独拆 node |
| [[recursion-and-folding|Recursion and folding]] | source extension | 记录 recursive compression for on-chain verification | 不覆盖 Nova/folding foundation |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | new bridge | 连接 proof-system succinctness/soundness 与 bridge correctness/cost | 明确 light-client/security assumptions 不由 SNARK 自动提供 |

## 关键术语表

| Term | 本文含义 | 上层去向 |
| --- | --- | --- |
| block header relay network | 生成并提交 sender chain block header correctness proof 的 relayers；只为 liveness 信任 | source detail; cross-chain method |
| updater contract | 目标链上验证 proof、维护 sender chain headers/light-client state 的合约 | source detail; cross-chain method |
| LightCC | sender chain light-client block validation rule | [[cross-chain-protocols|Cross-chain protocols]] |
| deVirgo | 面向 data-parallel circuits 的 distributed Virgo proof protocol | source-contained proof-system extension |
| recursive verification | 用 Groth16 证明 deVirgo proof verification，减少链上 proof size/gas | [[recursion-and-folding|Recursion and folding]] source extension |
| batching | 一批 headers 生成统一 proof，只存 batch Merkle root | source detail; method tradeoff |

## 关系与链接

- Primary: [[cross-chain-protocols|Cross-chain protocols]]
- Parent: [[interoperability|Blockchain interoperability]] -> [[blockchain-systems|Blockchain systems]]
- Secondary: [[blockchain-applications|ZKP blockchain applications]], [[zk-snarks|zk-SNARKs]], [[proof-systems|Proof systems]], [[recursion-and-folding|Recursion and folding]]
- Bridge: [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]]
- Sibling source: [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]]

## 质量复核

- 完整性: 覆盖 problem, model, protocol, proof-system design, recursive compression, implementation, evaluation, cost and related-work boundaries。
- 分层性: source note 保留 zkBridge/deVirgo/implementation details；knowledge nodes 只吸收可复用问题和方法族。
- 概念边界: zkBridge 不拆成 concept；deVirgo 暂不拆成 concept；trustless cross-chain bridge 作为 cross-chain protocols 的方法路线。
- 风险: 论文中的部分 dollar cost 和 gas price 是 2022-08 时间点估算，不应当作为当前价格结论。
