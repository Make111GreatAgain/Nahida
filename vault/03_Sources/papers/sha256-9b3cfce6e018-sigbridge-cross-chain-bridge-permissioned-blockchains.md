---
id: "sha256-9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
title: "sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control"
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
  - "p1-p2 abstract, introduction, motivation, zkBridge comparison and sigBridge overview"
  - "p3 preliminaries: blockchain, light-client protocol, ABAC and Merkle proof"
  - "p3-p6 sigBridge four-layer architecture, entities, algorithms and setup"
  - "p5-p6 security theorems for header synchronization and message passing"
  - "p6-p8 cross-chain user-centric ABAC resource-sharing protocol and security argument"
  - "p8-p9 proof-of-concept implementation and gas/probability evaluation"
  - "p9-p10 conclusion and references"
safe_for_absorption: true
canonical_url: "https://hdl.handle.net/10125/106997"
doi: ""
arxiv_id: ""
venue: "HICSS 2024"
year: "2024"
pdf_pages: 10
pdf_sha256: "9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
local_pdf: "~/Desktop/paper/0502.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/0502-9b3cfce6e018-pages.txt"
pdf_extractor: "existing extracted text; verified with codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "interoperability"
topic_ids:
  - "cross-chain-protocols"
  - "permissioned-blockchain-consensus"
  - "decentralized-access-control"
ontology_path:
  - "blockchain-systems"
  - "interoperability"
  - "cross-chain-protocols"
primary_ontology_path: "blockchain-systems/interoperability/cross-chain-protocols/sha256-9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
secondary_ontology_paths:
  - "blockchain-systems/consensus/permissioned-blockchain-consensus/sha256-9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
  directions:
    - "interoperability"
    - "consensus"
  topics:
    - "cross-chain-protocols"
    - "permissioned-blockchain-consensus"
    - "decentralized-access-control"
domains:
  - "blockchain-systems"
topics:
  - "cross-chain-protocols"
  - "permissioned blockchains"
  - "signature bridge"
  - "light clients"
  - "attribute-based access control"
  - "resource sharing"
aliases:
  - "sigBridge"
  - "signature bridge"
  - "permissioned cross-chain bridge"
  - "cross-chain ABAC"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "interoperability"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "interoperability"
    - "consensus"
  problem:
    - "cross-chain block-header verification for permissioned blockchains"
    - "expensive ZK proof generation for permissioned-chain bridges"
    - "cross-chain decentralized access control"
  method_family:
    - "signature-of-consensus bridge"
    - "probabilistic signature verification"
    - "light-client header synchronization"
    - "Merkle-proof transaction relay"
  system_layer:
    - "relay network"
    - "updater contract"
    - "application contract"
    - "cross-chain synchronization layer"
  evaluation_context:
    - "two private Ethereum networks"
    - "Proof-of-Authority permissioned setting"
    - "Solidity/Truffle/Geth/Puppeth prototype"
  application:
    - "attribute-based access control"
    - "cross-chain resource sharing"
  bridge:
    - "permissioned consensus to cross-chain bridges"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260622-sigbridge"
source_refs:
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
  - "pdf:~/Desktop/paper/0502.pdf"
  - "hdl:10125/106997"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> interoperability"
secondary_directions:
  - "blockchain-systems -> consensus"
classification_status: "reclassified"
classification_confidence: "high"
classification_evidence:
  - "Title, abstract and introduction target a cross-chain bridge for permissioned blockchains"
  - "Section 4 defines sigBridge as a signature-of-consensus bridge over relay network and updater contract"
  - "Section 5 uses the bridge for cross-chain user-centric ABAC resource sharing"
  - "The paper compares against zkBridge but replaces ZK proof computation with consensus-signature verification"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0055"
queue_status: "absorbed"
---

# sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control

## 论文身份

- 标题: sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control
- 作者: Mahmudun Nabi, Reihaneh Safavi-Naini, Sepideh Avizheh, Marc Kneppers, Preston Haffey
- 机构: University of Calgary; Telus Communications Inc.
- 会议/期刊: Proceedings of the 57th Hawaii International Conference on System Sciences (HICSS 2024)
- 年份: 2024
- DOI: unknown
- 链接: `https://hdl.handle.net/10125/106997`
- 本地 PDF: `~/Desktop/paper/0502.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/0502-9b3cfce6e018-pages.txt`
- SHA-256: `9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1`
- License: CC BY-NC-ND 4.0

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: existing text extraction; page count verified with `pypdf`
- 页数: 10
- 已覆盖章节/页码: Abstract, Introduction, Related work, Preliminaries, sigBridge protocol, security arguments, cross-chain ABAC application, implementation, evaluation, conclusion and references
- Extraction gaps: 公式和算法有轻微换行噪声，但定理、算法、表格和核心参数可从文本恢复；图 1-3 已通过图注和正文解释覆盖。
- 精读说明: 这篇论文的 durable value 是把 permissioned blockchain 的 consensus signatures 作为跨链桥验证材料，而不是为 `sigBridge` 创建同名上层概念。它应作为 [[cross-chain-protocols|Cross-chain protocols]] 的 source extension，并通过 bridge 连接到 [[permissioned-blockchain-consensus|Permissioned blockchain consensus]]。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题、贡献和定位 | 对比 zkBridge；在 permissioned chains 中用 consensus signatures 替代 ZK proof；给出 cross-chain ABAC resource-sharing demo | high | 明确 reclassification 依据 |
| §2 / p3 | 相关工作 | committee bridges、light-client/relayer protocols、XCMP/IBC/OPTICS；smart-contract access control | medium | 说明 sigBridge 的应用和对照背景 |
| §3 / p3 | 预备知识 | blockchain/light client、`VerifyHeaderUpdate`、Merkle proof、ABAC | high | 后续协议依赖 |
| §4 / p3-p6 | sigBridge 框架 | 四层互操作架构、relay network、updater contract、application contract、算法 1/2 | high | 核心机制 |
| §4 / p5-p6 | 安全论证 | `epsilon = C(n-alpha,t)/C(n,t)`；liveness 依赖至少一个 honest relayer；message passing 依赖 Merkle proof | high | correctness/efficiency trade-off |
| §5 / p6-p8 | 跨链 access control 应用 | obj-dir cross-chain table、SC-phi policy evaluator、request/token 双向 relay | high | 应用场景，但不宜直接提升为独立领域 |
| §6 / p8-p9 | 实现与评估 | 两个 private Ethereum networks；PoA；Solidity/Truffle/Geth/Puppeth；Table 1/2、Figure 3 | high | gas 与概率权衡 |
| §7 / p9 | 结论和开放问题 | oblivious updater contract；更通用 ZK proof system；heterogeneous multi-chain privacy-preserving resource sharing | medium-high | 后续队列/bridge 触发器 |

## 核心精读笔记

### 背景、动机与问题边界

sigBridge 的问题背景是多链应用需要把一条链上的事件、状态或交易，以可信方式传递到另一条链上的应用合约。zkBridge 通过 relayer + updater contract + ZK proof 让目标链合约验证源链 light-client 状态转移，但该路线为 permissionless chain 的昂贵链上验证而设计。本文认为 permissioned blockchain 的准入、共识节点规模和签名机制不同：链上执行成本更低，consensus signatures 可由目标链合约直接验证，因此不必总是生成昂贵的 ZK proof。证据锚点: Abstract, §1 p1-p2。

本文的边界很清楚：它不是通用 permissionless bridge，也不是完整跨链互操作综述。它针对两条或多条 permissioned blockchains，假设链本身满足 consistency/liveness，且参与 consensus 的节点身份和公钥可被目标链 updater contract 使用。它继承 zkBridge 的 relay/updater/application contract 框架，但把 ZK proof transformation 替换为基于 signatures of consensus 的 `(T, V)`。证据锚点: §1 p2, §4 p3-p4。

### 模型、假设与定义

论文使用四层 permissioned blockchain interoperability architecture：message passing、consensus、cross-chain synchronization、application。sigBridge 实现 cross-chain synchronization layer，并为 application layer 提供可验证的 remote event/transaction evidence。证据锚点: §4 p3-p4。

关键实体包括：

- Relay network: 注册在两条链上的 relayers，运行 light nodes，连接 full nodes，获取源链 signed block headers，并调用目标链 updater contract。sigBridge 中 relayers 还负责从源链 full nodes 获取 transaction 和 Merkle proof；这是因为资源请求者只属于目标链，无法直接联系源链 client。证据锚点: §4.1 p4-p5。
- Updater contract: 部署在目标链，存储源链 header history、源链 consensus rules/parameters 和必要 public keys。它验证 relayer certificate/signature、验证 block header update，并用 Merkle proof 验证 transaction inclusion。证据锚点: Algorithm 2 p5-p6。
- Application contracts: 源链/目标链应用合约通过 relay network 传递业务消息；在 access-control 应用中包括 `obj-dir` 和 `SC-phi_i`。证据锚点: §4.1 p5, §5 p6-p8。

系统安全假设包括：两条 permissioned blockchains 各自满足 consistency/liveness；consensus signatures 和 relayer signatures 不可伪造；relay network 中至少一个 relayer honest 以保证 liveness；relayers 可能恶意、可篡改/丢弃消息或尝试未注册发送；初始 updater contract 状态和 relayer registration 由 trusted authority/admin 建立。证据锚点: §4.1 p5-p6。

### 方法、协议或系统机制

sigBridge 的核心是将源链 block header `blkH = [data, sig_of_con]` 变换为目标链可验证的输入 `[data, T(sig_of_con)]`。在小规模 permissioned chain 中，`T` 可以是 identity function，直接传全部 signatures；在签名数量较多时，`T` 从 `sig_of_con` 中选出符合源链 consensus threshold `n` 的有效签名子集。目标链 updater contract 的 verification `V` 不必验证全部 `n` 个签名，而可以随机抽样验证 `t` 个签名，以在链上成本和错误接受概率之间折中。证据锚点: §4.1 p4-p5。

Header synchronization 流程：

1. relayer 从 `k` 个源链 full nodes 获取 `blkH_r = [data, sig_of_con]`；
2. relayer 应用 `T`，选择 `n` 个有效 consensus signatures，形成 `blkH_r = [data, T(sig_of_con)]`；
3. relayer 用自身私钥签署 header payload，并向目标链 updater contract 提交 `HeaderUpdate(blkH_r, sigma, Cert_pk)`；
4. updater contract 验证 relayer certificate/signature，取上一条 header，从存储的源链 consensus rules 中随机验证 `t` 个 signatures；若通过则将 header 写入 `hdrHistory`。证据锚点: Algorithm 1/2 p5-p6。

Transaction/message relay 流程：

1. 应用合约 `AC1` 调用 relay network 传递消息或 transaction information；
2. relayer 从源链 full nodes 获取 transaction `tx` 及 inclusion Merkle proof `pi`；
3. relayer 签名 `(tx, i, pi)` 并调用目标链 updater contract 的 `VerifyProof`；
4. updater contract 从 `hdrHistory[i]` 取对应 block header，用 Merkle root 验证 inclusion proof，并把验证后的 transaction info 交给目标应用。证据锚点: Algorithm 1/2 p5-p6。

### 理论、证明或正确性论证

Theorem 1 给出 header synchronization 的 `epsilon`-consistency 和 liveness。若 malicious relayer 在 `n` 个提交 signatures 中混入 `alpha` 个 forged/invalid signatures，而 updater contract 随机选择 `t` 个验证，则攻击不被发现的概率为：

```text
epsilon = C(n - alpha, t) / C(n, t)
```

检测概率是 `delta = 1 - epsilon`。当 `t = n` 时，updater contract 验证全部提交签名，`delta = 1`；当 `t` 较小，链上成本降低但错误接受概率上升。证据锚点: Theorem 1 and Figure 2 p5-p6。

Theorem 2 将 message passing 的安全性归约到 updater contract 的 liveness/epsilon-consistency 和 Merkle proof 的 correctness/soundness。也就是说，sigBridge 对交易存在性的保证不是来自 relayer 诚实性，而是来自已经同步的源链 header history 和交易 inclusion proof。证据锚点: p6。

Theorem 3 给出 cross-chain resource-sharing application 的组合安全：若 sigBridge 有 liveness 和 `epsilon`-correctness，且两条链可信执行 smart contracts，则应用达到 `(1 - 3epsilon)`-correctness 和 `(1 - 2epsilon)`-security。三个 correctness failure points 是 cross-chain obj-dir view 不一致、request/token 传递被篡改或重放、policy evaluation 执行错误；security failure points 包括 requester registration/certificate 验证和 replay/freshness failure。证据锚点: §5.2 p7-p8。

### 实验、评估或案例

论文实现了 proof-of-concept cross-chain resource-sharing application，使用两个 private Ethereum networks，Geth/Puppeth 生成 PoA genesis，Solidity 编写 smart contracts，Truffle 编译和部署。系统包括 application contracts (`obj-dir`, `SC-phi_i`) 和 cross-chain updater contracts。`headerUpdate()` 验证 consensus-node signatures；`verifyTx()` 验证 transaction inclusion Merkle proof；`getHeader()` 暴露 header hash 查询。证据锚点: §6 p8。

Table 1 给出 resource-sharing application contracts 的 gas 成本，并用单次 `keccak-256(bytes32)` 的 323 gas 做 hash-equivalent 转换。`registerResource` 约 435,830 gas，`generatePolicy` 约 1,268,843 gas，`requestResourceAccess` 约 199,751 gas。证据锚点: Table 1 p9。

Table 2 对比 sigBridge 与 zkBridge 的 block header verification。在 `N=8` signatures 时，sigBridge data size 1064 bytes，on-chain cost 396K gas，machine required 1；zkBridge with recursive verification proof size 131 bytes，on-chain cost 227K gas，但 machine required 8。在 `N=32` signatures 时，sigBridge data size 4256 bytes、on-chain cost 5M gas、machine required 1；zkBridge 仍为 131 bytes、227K gas，但 machine required 32。这个结果说明 sigBridge 的优势是不用分布式 ZK proving infrastructure，缺点是 signature count 增大时数据量和链上 verification gas 增长明显。证据锚点: Table 2 p9。

Figure 3 展示 `t`、invalid signatures `alpha` 和 gas 成本的 trade-off：提高 `t` 会提高 invalid signature detection probability `delta`，但也提高 verification gas。论文用 `n = 32` 和 `alpha = {4, 10, 18}` 说明该折中。证据锚点: Figure 3 p9。

### 作者结论与我的判断

作者结论是：在 permissioned blockchains 中，sigBridge 可以沿用 zkBridge 的 relay/updater/application architecture，但用 consensus signatures 和抽样验证替代 ZK proof，得到一个可调 correctness/efficiency trade-off，并能支持跨链 user-centric ABAC resource sharing。证据锚点: §7 p9。

我的判断：这篇论文对知识库的最重要增量不是 `sigBridge` 这个系统实例，而是一个 reusable bridge pattern：permissioned consensus signatures can be reused as cross-chain state-verification evidence。它应更新 [[cross-chain-protocols|Cross-chain protocols]] 的方法族和 [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] 的 cross-direction usage，并创建或更新 `permissioned consensus -> cross-chain bridges` 关系。ABAC/resource sharing 是应用证据，暂不单独创建上层节点；应记录 `decentralized-access-control foundation gap`，以后若有更多 access-control sources 再拆应用方向。

## 层级候选分类

- L1 Domain candidate: `blockchain-systems`
- L2 Direction candidate: `interoperability`
- L3 Topic/content cluster candidates: `cross-chain-protocols`
- Ontology path: `blockchain-systems/interoperability/cross-chain-protocols`
- 备选归属: `blockchain-systems/consensus/permissioned-blockchain-consensus` as secondary path
- 父级领域: [[blockchain-systems|Blockchain systems]]
- 学术子领域: [[interoperability|Blockchain interoperability]]
- 任务/问题: permissioned cross-chain block-header verification and cross-chain ABAC resource sharing
- 方法族: signature-of-consensus bridge, probabilistic signature verification, Merkle-proof transaction relay
- 模型/协议/算法族: light-client protocol, updater contract, relay network, PoA/permissioned consensus signatures
- 评测场景: two private Ethereum networks, PoA, Solidity/Truffle/Geth prototype
- Benchmark/应用: decentralized user-centric resource-sharing with ABAC
- 别名: sigBridge, signature bridge, permissioned cross-chain bridge
- 相邻方向: permissioned blockchain consensus; ZK light-client bridges
- 置信度: high
- 分类理由: 论文主体是 cross-chain bridge protocol for permissioned blockchains；ZK 只作为 zkBridge 对照和未来可能路线。
- 分类状态: `reclassified`
- 分类证据: Abstract/§1; §4 sigBridge; §5 application; §6 evaluation
- Taxonomy version: `1.0`
- Direction facets: see frontmatter

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `blockchain-systems` | title, abstract, introduction all target cross-chain bridge and blockchains | high | durable parent |
| Research background | blockchain interoperability, light-client protocols, permissioned consensus, zkBridge | §1-§3 | high | update background of relevant nodes |
| Research problem | verifiable cross-chain state/event transfer between permissioned chains | Abstract, §4 | high | update [[cross-chain-protocols]] |
| Foundation concepts | light client, Merkle proof, ABAC, permissioned consensus signatures | §3 | medium-high | keep local definitions; ABAC foundation gap queued |
| Method family | signature-of-consensus bridge with probabilistic verification | §4, Theorem 1 | high | source extension plus bridge |
| Application/evaluation context | decentralized ABAC resource sharing over two private Ethereum chains | §5-§6 | high | source extension; no standalone node yet |
| Artifact/source instance | sigBridge | title, §4 | high | source instance, not foundation node |

### 分层判断示例

| Source cue | Correct handling | Wrong handling |
| --- | --- | --- |
| `sigBridge` | source/protocol instance under [[cross-chain-protocols]] | create top-level `sigBridge` concept page |
| `signatures of consensus` | bridge from [[permissioned-blockchain-consensus]] to [[cross-chain-protocols]] | bury in source only and lose reusable route |
| `ABAC resource sharing` | application evidence and foundation gap | promote a broad access-control domain from this one paper |
| `zkBridge comparison` | contrast/alternative method route | classify primary path as ZKP application |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `blockchain-systems/interoperability/cross-chain-protocols`
- 它能帮助未来哪些问题少读 source notes: “permissioned chain 跨链桥能否不用 ZK proof?”、“consensus signatures 如何用于跨链 header verification?”、“sigBridge 的安全概率怎么计算?”、“跨链 access-control demo 怎么接桥?”
- 哪些内容应留在 source note，而不是创建上层节点: Algorithm 1/2 逐步参数、Table 1 gas 数字、具体 obj-dir/SC-phi flow、实验工具链细节。
- 哪些上层节点过薄、缺失或需要 foundation_pack: `decentralized-access-control` / ABAC as blockchain application; IBC/OPTICS/XCMP/LayerZero 等非 ZK bridge foundations。
- 哪些候选只是别名/query key/watch term: sigBridge, signature bridge, cross-chain ABAC。

## 一句话贡献

sigBridge 将 permissioned blockchain 的 consensus signatures 变成跨链 header verification evidence，用 `(T, V)` 和随机抽样签名验证替代 zkBridge 的 ZK proof，在 correctness probability 与链上验证成本之间提供可调折中，并用双链 ABAC resource sharing 做 proof-of-concept。

## 问题设定

目标是在 BC1 和 BC2 两条 permissioned blockchains 之间，让 BC2 上的应用可验证 BC1 上某个 event/transaction/header 确实发生。相比 permissionless setting，permissioned setting 有已知 consensus nodes、signatures、公钥和更低链上执行成本，因此论文认为直接验证 consensus signatures 可能比生成/验证 ZK proof 更合适。

## 方法概览

### 组成部分

- Relay network: 同时注册在两条链，运行 light nodes，获取 signed headers、transactions 和 Merkle proofs。
- Updater contract: 目标链上的 cross-chain smart contract，保存 remote header history 和 source-chain consensus rules。
- Application contracts: 需要跨链信息的业务合约，如 `obj-dir` 和 `SC-phi_i`。
- Trusted setup/registration: 初始化 updater contract 的源链 header/public keys/consensus params，并由 authority 给 relayers 发 certificate。

### 流程或协议

- Header path: full nodes -> relayer -> `T(sig_of_con)` -> updater contract -> random verification of `t` signatures -> header history.
- Transaction path: application event -> relayer fetches Merkle proof -> updater contract verifies proof against stored remote header -> target application receives verified message.
- Access-control path: BC1 owner 更新 resource metadata 到 `obj-dir1`，sigBridge relay 到 BC2 的 cross-chain `obj-dir2`；BC2 requester 浏览本地 remote-resource table，再通过 bridge 将 access request 发给 BC1 的 `SC-phi_i`，policy evaluator 返回 token。

### 关键定义、公式、算法或定理

- `T`: 从源链 consensus signatures 中选择目标链需要验证的子集；小规模可为 identity。
- `V`: updater contract 的 verification logic，随机抽样 `t` 个 signatures 并按源链 consensus rules 验证。
- `epsilon = C(n - alpha, t) / C(n, t)`: malicious relayer 混入 `alpha` 个 invalid signatures 时未被检测的概率。
- Theorem 1: header synchronization achieves `epsilon`-consistency and liveness under unforgeable signatures, at least one honest relayer, and sender chain consistency/liveness。
- Theorem 2: message passing inherits updater contract `epsilon`-consistency/liveness and Merkle proof correctness/soundness。
- Theorem 3: resource-sharing application reaches `(1 - 3epsilon)`-correctness and `(1 - 2epsilon)`-security under smart-contract trusted execution。

### 假设条件

- Permissioned chains have known consensus/public-key material and enforce consistency/liveness.
- Consensus/relayer signature schemes are unforgeable.
- At least one relayer is honest for liveness.
- Updater contract initialization is trusted.
- Application-level policy evaluation is correct if the executing chain/smart contract is trusted.
- Merkle proof correctness/soundness holds for transaction inclusion verification.

## 创新点

- 新思想: 在 permissioned chain 中，源链 consensus signatures 本身可成为目标链验证 header correctness 的证据，不一定需要 ZK proof。
- 对已有工作的扩展: 沿用 zkBridge 的 relay/updater/application contract framework，但把 proof-generation transformation 改为 signature subset selection and probabilistic verification。
- 系统化应用: 把单链 decentralized resource-sharing ABAC 扩展到两条 permissioned blockchains。
- 可调参数: 用 `t` 控制 correctness probability 和 gas 成本之间的 trade-off。

## 局限与开放问题

| Limitation / Open problem | 说明 | Evidence |
| --- | --- | --- |
| Signature count scaling | `N=32` 时 sigBridge on-chain cost 达 5M gas，proof size/data size 也随 signatures 增长。 | Table 2 p9 |
| Updater contract knows remote consensus | 当前 updater contract 需要存储源链 consensus rules/public keys；作者提出 future work 是让 updater 对远端 consensus algorithm oblivious。 | §7 p9 |
| Trusted initialization and relayer registration | setup 依赖 admin/authority 初始化 header/public keys 和 relayer certificates。 | §4.1 p5 |
| ABAC foundation thin | 论文给出 ABAC 定义和应用，但知识库还没有完整 access-control/applications foundation。 | §3, §5 |
| Heterogeneous multi-chain privacy | 结论提出 privacy-preserving resource sharing in heterogeneous multi-chain environment 作为未来方向。 | §7 p9 |

## 可吸收上层增量

| Target | Durable delta | Evidence | Action |
| --- | --- | --- | --- |
| [[cross-chain-protocols|Cross-chain protocols]] | 新增 signature-of-consensus bridge 路线，作为 ZK light-client bridge 的 permissioned-chain alternative。 | Abstract, §4, Table 2 | update method/source extension |
| [[interoperability|Blockchain interoperability]] | 互操作方向新增 permissioned bridge trade-off：known membership/signatures 可以降低 proof-generation complexity，但会引入 signature-scaling 和 trusted setup boundary。 | §1, §4, §6 | light update |
| [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] | consensus signatures 不只是排序/finality evidence，也可作为跨链 synchronization verification material。 | §4, Theorem 1 | update source extension/bridge link |
| new bridge | `permissioned consensus -> cross-chain bridges` relation: consensus rules/signatures become bridge verifier input. | §4, Theorem 1, Table 2 | create bridge |

## Handoff to nahida-knowledge-get

- Primary source note: this file.
- Primary knowledge path: `blockchain-systems/interoperability/cross-chain-protocols`.
- Secondary path: `blockchain-systems/consensus/permissioned-blockchain-consensus`.
- Bridge to create/update: `permissioned-consensus-to-cross-chain-bridges`.
- Do not create: `sigBridge` as standalone knowledge node; `ABAC` foundation node from this paper alone.
- Review/foundation gap: queue `decentralized access control / ABAC for blockchain applications` if future sources or user query require it.
