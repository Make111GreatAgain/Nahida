---
id: "sha256-1e0dbba290b2-ipfs-principles-and-practice"
title: "IPFS原理与实践"
type: "source"
source_kind: "book"
source_subtype: "local_pdf"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
hierarchy_level: "source"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "董天一"
  - "戴嘉乐"
  - "黄禹铭"
year: 2019
venue: "机械工业出版社"
publisher: "机械工业出版社"
isbn: "978-7-111-62880-4"
source_refs:
  - "isbn:978-7-111-62880-4"
  - "sha256:1e0dbba290b2b4ccd70e8c42f78fc2531b9bf6539b7afe55c699cca43d1fa1e5"
canonical_url: ""
doi: ""
arxiv_id: ""
local_pdf_path: "~/Desktop/paper/IPFS原理与实践 -.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/ipfs-1e0dbba290b2-pages.txt"
pages: 330
page_count: 330
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
classification_status: "corrected_absorbed"
classification_confidence: "high"
primary_domain: "distributed-systems"
primary_direction: "data-management-and-storage"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/content-addressed-storage"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "content-addressed-storage"
secondary_ontology_paths:
  - "blockchain-systems/data-management-and-storage/decentralized-storage-networks"
  - "blockchain-systems/data-management-and-storage/off-chain-application-data-management"
topic_ids:
  - "content-addressed-storage"
  - "peer-to-peer-storage"
  - "ipfs"
  - "distributed-file-systems"
  - "dht-routing"
  - "bitswap"
  - "merkle-dag"
  - "ipld"
  - "cid"
  - "ipns"
  - "libp2p"
  - "filecoin"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "IPFS"
  - "content-addressed storage"
  - "peer-to-peer storage and distribution"
  - "Merkle DAG"
  - "IPLD"
  - "CID"
  - "libp2p"
  - "BitSwap"
  - "IPNS"
  - "Filecoin"
aliases:
  - "IPFS Principles and Practice"
  - "InterPlanetary File System"
  - "IPFS 原理与实践"
tags:
  - "nahida/source"
  - "nahida/source/book"
  - "distributed-systems"
  - "data-management-and-storage"
  - "content-addressed-storage"
classification_evidence:
  - "PDF title page identifies a 2019 Chinese technical book on IPFS by 董天一, 戴嘉乐 and 黄禹铭."
  - "Chapters 1-4 define IPFS as a content-addressed peer-to-peer hypermedia/file-system protocol with DHT routing, BitSwap exchange, Merkle DAG/IPLD/CID and IPNS naming."
  - "Chapter 5 treats Filecoin as an incentive/decentralized-storage-market layer related to IPFS, not as the book's primary consensus topic."
  - "Chapters 6-8 are IPFS development and application practice, including go-ipfs, APIs, pinning, Pubsub, private IPFS networks, Git and streaming-media examples."
  - "Queue path corrected from distributed-systems/consensus/needs-review to distributed-systems/data-management-and-storage/content-addressed-storage."
knowledge_node_refs:
  - "[[content-addressed-storage|Content-addressed Storage and Distribution]]"
  - "[[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]"
  - "[[decentralized-storage-networks|Decentralized Storage Networks]]"
  - "[[off-chain-application-data-management|Off-chain Application Data Management]]"
bridge_refs:
  - "[[content-addressed-storage-to-decentralized-storage-networks|Content-addressed storage -> decentralized storage networks]]"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0106"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0106"
run_id: "nahida-knowledge-20260623-ipfs-principles-and-practice"
managed_by: "nahida"
confidence: "high"
trust_tier: "primary"
---

# IPFS原理与实践

## Paper Identity

| 字段 | 内容 |
| --- | --- |
| 标题 | IPFS原理与实践 |
| 作者 | 董天一；戴嘉乐；黄禹铭 |
| 类型 | 中文技术书 / local PDF source |
| 出版 | 机械工业出版社，2019 |
| ISBN | `978-7-111-62880-4` |
| 本地 PDF | `~/Desktop/paper/IPFS原理与实践 -.pdf` |
| 抽取文本 | `vault/02_Raw/pdf/extracted/ipfs-1e0dbba290b2-pages.txt` |
| SHA-256 | `1e0dbba290b2b4ccd70e8c42f78fc2531b9bf6539b7afe55c699cca43d1fa1e5` |

## Reading Coverage

| 范围 | 覆盖 |
| --- | --- |
| PDF extraction | `pypdf` extraction usable; 330 pages. |
| 已读结构 | Title page, TOC, recommendation/preface, Chapter 1-8, chapter summaries, key mechanism sections. |
| 重点章节 | 第 1 章 IPFS 概念与 HTTP/区块链关系；第 2 章 DHT/BitTorrent/Git/SFS/Merkle；第 3 章 IPFS 七层协议栈；第 4 章 Multiformats/libp2p/IPLD/CID；第 5 章 Filecoin；第 6-8 章 go-ipfs/js-ipfs 开发实践。 |
| 元数据修正 | Queue 作者、标题基本正确；年份从 PDF title page 的纸版出版信息校正为 `2019`，不是 Calibre metadata 的电子文件创建年 `2020`。 |
| 分类修正 | 原 queue path 为 `distributed-systems/consensus/needs-review`。正文显示本书主问题是内容寻址 P2P 存储与分发，不是共识；Filecoin 章节只作为激励/存储市场相关层。 |

## One-Sentence Takeaway

这本书把 IPFS 解释为一个用内容寻址替代位置寻址、用 DHT 找 provider、用 BitSwap 交换块、用 Merkle DAG/IPLD/CID 表示对象、用 IPNS 处理可变命名，并可由 Filecoin 提供存储激励的 P2P 内容存储与分发协议栈。

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | distributed systems | IPFS is a peer-to-peer file/hypermedia protocol and distributed file system. | high | existing domain |
| Direction | data-management-and-storage | main mechanisms are storage, routing, object addressing, block exchange, naming and persistence. | high | existing direction |
| Research problem | content-addressed storage and distribution | content addressing, DHT provider lookup, Merkle DAG, CID, pinning, IPNS and gateways recur across applications. | high | create reusable knowledge node |
| Secondary problem | decentralized storage networks | Filecoin chapter covers storage markets, DSN, PoRep/PoSt and miner incentives. | high | refresh existing blockchain problem node |
| Secondary problem | off-chain application data management | IPFS primitives explain CIDs/pinning/private networks used by blockchain-IPFS application data notes. | medium | bridge/foundation relation, not primary classification |
| Method family | DHT + block exchange + Merkle object graph + self-describing identifiers + mutable naming | Chapter 2-4 | high | source extension |
| Source instance | IPFS, go-ipfs, js-ipfs, Filecoin | named systems/protocols | high | source details; only general concepts lifted |

## Structured Summary

### Problem

传统 Web/HTTP 主要用位置寻址: URL 指向某台服务器、某个路径。这个模型对缓存、内容迁移、镜像、抗审查、单点故障和大规模重复分发并不友好。IPFS 试图把“我要访问某个位置”改成“我要访问某段内容”，让内容由哈希/CID 标识，再由网络寻找可提供该内容的节点。

本书将 IPFS 放在 BitTorrent、DHT、Git、自验证文件系统和 Merkle 数据结构的合流处: BitTorrent 提供 P2P 分块交换直觉，DHT 提供内容/节点发现，Git 提供 Merkle DAG 和版本化对象模型，SFS 提供自验证命名思想。

### IPFS Stack

IPFS 协议栈在书中被拆成七层:

| 层 | 作用 | 关键机制 |
| --- | --- | --- |
| Identity | 生成和验证节点身份 | `NodeId = hash(PubKey)`, key pair, Multihash |
| Network | 跨传输协议连接节点 | TCP/uTP/WebRTC, NAT traversal, multiaddr, overlay network |
| Routing | 找 peer / provider / object | S/Kademlia + Coral-inspired DSHT; small values may sit in DHT, large values store provider refs |
| Exchange | 请求与提供块 | BitSwap, want_list, have_list, ledger, credit/debt strategy |
| Object | 内容对象图 | Merkle DAG, content addressing, tamper evidence, deduplication |
| File | 文件系统建模 | Blob/List/Tree/Commit, versioned file objects, chunking strategy |
| Naming | 可变命名 | IPNS, self-certifying naming, DNS TXT IPNS, human-friendly names |

### Content Addressing And Merkle DAG

IPFS 的底层目标不是把文件名映射到服务器位置，而是把内容块映射到可验证标识。书中反复使用 Merkle Tree / Merkle DAG 来解释这个模式:

- Merkle Tree 适合验证数据块完整性和轻客户端 proof。
- Merkle DAG 是更一般的对象图，节点包含 `Data` 和 `Link`，link 通过 hash 引用其他对象。
- IPFS 使用 Merkle DAG 组织文件对象，带来内容寻址、防篡改、重复数据删除和版本化对象图。
- 对一个文件执行 `ipfs add` 时，系统会把文件切块，再用 UnixFS/Merkle DAG 结构连接；返回的文件 hash 实际上是 DAG root 的内容标识。

这使得“相同内容得到相同 CID”和“内容变化导致 CID 变化”成为系统语义的一部分。开发实践章节用同一文本重复 `ipfs add` 得到相同 CID、改内容后 CID 改变的例子展示了这一点。

### DHT And Routing

第 2 章把 DHT 作为 P2P 内容检索基础。Kademlia 的要点包括:

- 节点 ID 和 key 在同一 hash 空间中。
- 用 XOR distance 衡量 key 和节点之间距离。
- 每个节点维护路由表和 K-Bucket。
- 查找路径通常是对数级跳转。
- 数据或 provider 信息保存在距离 key 更近的节点附近。

第 3 章进一步说明，IPFS 的 routing layer 不是把大对象直接塞进 DHT。小值可以直接存储，大值通常只在 DHT 中存 provider/node reference，再由交换层拿块。

### BitSwap Exchange

BitSwap 是 IPFS 交换层。它向其他节点请求 `want_list` 中的数据块，也为其他节点提供 `have_list` 中已有的数据块。它和 BitTorrent 的相似处是用 P2P 分块交换提升分发效率；差异在于 BitSwap 的市场不局限在某一个 torrent 文件，而是面向 IPFS 网络中所有可交换块。

书中强调 BitSwap 有信用、策略和账单:

- 给其他节点发送数据会增加信用。
- 从其他节点接收数据会降低信用。
- 节点可根据 debt ratio 调整发送概率，避免只下载不上传的 free-riding。
- Ledger 记录发送/接收字节与对等方关系；账单不一致时可重置或拒绝。

这些机制属于 P2P 块交换的局部激励，不等同于 Filecoin 的链上经济激励。

### Multiformats, libp2p, IPLD And CID

第 4 章把 IPFS 拆成三个工程组件:

| 组件 | 作用 | 可复用意义 |
| --- | --- | --- |
| Multiformats | 自描述编码、哈希、地址、codec 和 stream 协议 | 让 hash/function/codec/base/address 不被某一算法或编码格式锁死 |
| libp2p | P2P 网络协议模块库 | 抽象 transport、NAT traversal、peer discovery、DHT、relay、pubsub、RTT 等底层连接问题 |
| IPLD | 内容寻址数据模型 | 让 Merkle links / Merkle DAG / Merkle paths 可跨 IPFS、Git、BitTorrent、区块链等系统引用 |

CID 是自描述内容寻址标识符。CIDv1 组合 multibase 前缀、CID version、multicodec 和 multihash；CIDv0 则受早期 IPFS 默认 Base58btc/SHA2-256/protobuf 约束。知识层应保留的通用点是: CID 把“内容 hash”升级成“可演进、可自描述的内容标识”。

### Naming And Mutability

内容寻址让对象不可变: 内容一改，CID 就改。这对缓存和验证很好，但对“网站首页”“用户资料”等可变对象不够友好。IPNS 在本书中被解释为可变命名层:

- 用户/节点拥有以 NodeId 绑定的命名空间。
- 发布者用私钥签名，把命名空间下的路径指向最新对象。
- 读取者用公钥/NodeId 验证发布真实性。
- DNS TXT、peer links、Proquint 和短地址服务用于提高可读性与可集成性。

因此，IPFS 的抽象边界是: immutable content lives under `/ipfs/<cid>`; mutable names and human-friendly indirection live under `/ipns/...` or gateway/DNS layers.

### Filecoin Boundary

第 5 章说明 Filecoin 和 IPFS 的常见误解: IPFS 不是区块链项目，主要解决数据分发和定位；Filecoin 是区块链/去中心化存储网络，用代币、市场、抵押、存储矿工/检索矿工、PoRep/PoSt 和 DSN 操作处理长期存储与检索服务激励。

关键边界:

- IPFS 可以没有 Filecoin 而运行。
- Filecoin 也可以作为独立区块链/存储市场协议运行。
- 二者互补: IPFS 应用需要更多节点和存储；Filecoin 通过经济激励吸引节点贡献存储和带宽。
- Filecoin 的 DSN 层用 `Put`, `Get`, `Manage` 把存储订单、检索订单、担保品、扇区封存、证明和修复组织起来。
- Filecoin 的检索市场偏链下/实时，存储市场偏链上/订单和证明；这和普通 P2P BitSwap 信用机制不同。

这一部分应进入 [[decentralized-storage-networks|Decentralized Storage Networks]]，但不能把全书分类为 consensus。

### Development Practice

第 6-8 章是工程实践:

- 安装和初始化 go-ipfs；配置 `~/.ipfs` 仓库、API、gateway、swarm、datastore、IPNS 等。
- 用 `ipfs add`, `ipfs cat`, `ipfs ls`, `ipfs dht findprovs`, gateway URL 等与文件系统和网络交互。
- 通过 `ipfs pin` / `pin rm` / `pin ls` 保持本地对象不被垃圾回收。
- 发布动态内容、操作 Merkle DAG block/object、使用 Pubsub、搭建私有 IPFS 网络。
- 用 go-ipfs 优化 Git 分布式服务，用 js-ipfs 构建浏览器流媒体播放系统。

这些章节的可复用知识不是具体命令版本，而是提示: CID 不保证长期可用，实际系统需要 pinning、provider availability、gateway/API、private swarm key、bootstrap 节点和应用层生命周期管理。

## Evaluation And Evidence

本书不是实验论文。它的证据类型是系统性技术讲解、协议栈重构和开发教程。书中提供的性能/应用判断主要是解释性和实践性，不应作为 IPFS/Filecoin 当前生产性能或安全性的最新证据。

| 证据类型 | 用途 | Caveat |
| --- | --- | --- |
| 章节结构 | 清晰说明 IPFS 的底层技术、协议栈、组件和实践路径 | 书籍出版于 2019，具体版本和主网状态可能过时 |
| 机制描述 | 可作为 content-addressed storage / P2P storage foundation source | 对 Filecoin 白皮书状态依赖较旧 |
| 命令/API 示例 | 帮助理解 CID、pinning、gateway、private network 等操作语义 | 不保证命令在最新 go-ipfs/kubo/js-ipfs 中完全一致 |
| Filecoin 章节 | 为 DSN、PoRep/PoSt、存储/检索市场补直接中文 source | 不能替代 Filecoin 当前规范或论文 |

## Limitations And Boundary

- 本书出版于 2019，IPFS/Kubo、Filecoin、libp2p、IPLD、CID 和 js-ipfs 生态后续已有变化；具体版本命令、测试网/主网状态、经济参数不能视为当前事实。
- 本书没有给出新的共识协议；Filecoin 的共识/PoRep/PoSt 章节属于 DSN/区块链存储激励背景。
- IPFS 的内容寻址证明内容完整性，不自动证明内容长期可用、被足够多节点 pin、满足访问控制、或通过经济机制保证检索。
- 私有 IPFS 和 IPFS gateway 是部署/访问方式，不等于公共去中心化网络的安全或可用性。

## What This Source Adds To Nahida

- 创建 [[content-addressed-storage|Content-addressed Storage and Distribution]] 作为 distributed systems/data-management 下的通用问题节点。
- 为已有 [[off-chain-application-data-management|Off-chain Application Data Management]] 补上 CID/IPFS/pinning/private network 的基础来源，但不把施工应用细节塞进 IPFS 节点。
- 刷新 [[decentralized-storage-networks|Decentralized Storage Networks]]，补入 Filecoin/IPFS 关系、DSN `Put/Get/Manage`、存储/检索市场、PoRep/PoSt 和攻击边界。
- 创建 [[content-addressed-storage-to-decentralized-storage-networks|Content-addressed storage -> decentralized storage networks]]，明确“内容寻址/P2P 分发”和“区块链存储市场/激励”之间的可迁移与不可迁移边界。

## Source-Backed Takeaways

- Content addressing changes the retrieval question from “where is this file?” to “who can provide blocks matching this content identifier?”.
- DHT routing and BitSwap exchange are complementary: DHT finds peers/providers, BitSwap moves blocks and tracks exchange behavior.
- Merkle DAG is the object model that makes content addressing, tamper evidence, deduplication and versioned object graphs work together.
- CID is not just a hash string; it packages hash/codec/base/version choices so identifiers can evolve.
- IPNS is needed because immutable content identifiers are awkward for mutable names.
- Filecoin and IPFS should be modeled as adjacent but separate layers: IPFS provides content-addressed distribution; Filecoin adds storage market incentives and proofs.
- CID/hash integrity does not imply availability; pinning, replication, provider incentives and lifecycle management are separate design problems.

## Absorption Targets

| Target | Action | Reason |
| --- | --- | --- |
| [[content-addressed-storage|Content-addressed Storage and Distribution]] | create | Needed as reusable foundation/problem node for IPFS, CID, IPLD, DHT provider routing, BitSwap, pinning and gateways. |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | update | Add content-addressed storage as child; correct consensus-heavy queue bias. |
| [[decentralized-storage-networks|Decentralized Storage Networks]] | update | Add IPFS/Filecoin relationship and Filecoin DSN/proof/market seed evidence. |
| [[off-chain-application-data-management|Off-chain Application Data Management]] | update | Reference content-addressed storage as a foundation dependency for CIDs/private IPFS/pinning. |
| [[content-addressed-storage-to-decentralized-storage-networks|Content-addressed storage -> decentralized storage networks]] | create | Explain why IPFS/Filecoin relate but should not be collapsed. |

## Foundation Candidate Judgment

| 候选 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Content-addressed storage | foundation/problem node | 建立可复用 Knowledge node，作为 IPFS、IPLD/CID、off-chain assets 和 DSN 的底层概念入口 | 把 IPFS 只留在书籍 source note，导致未来 CID/IPFS 查询找不到上层入口 | Chapters 1-4 |
| IPFS | representative protocol/system | 留在 source note 和代表来源；在 Knowledge 节点中作为代表实现 | 为 IPFS 单独建上层孤岛并重复定义全部概念 | Chapters 1, 3, 6-8 |
| CID/IPLD/Merkle DAG/libp2p | foundation candidates / component concepts | 当前先作为 content-addressed-storage 内部章节；等多 source 后再拆 | 在单本书后立即拆出过多薄节点 | Chapters 2-4 |
| Filecoin | DSN representative system / source extension | 进入 decentralized-storage-networks 节点和 bridge | 把全书归入 consensus 或把 Filecoin 与 IPFS 合并 | Chapter 5 |

## Evidence Record

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 |
| --- | --- | --- | --- | --- |
| 本 PDF 是 2019 年中文 IPFS 技术书 | metadata | p2 | Title page lists title, authors, ISBN and publisher/year | high |
| IPFS 主定义是内容寻址、分布式超媒体/文件系统 | source | Chapter 1.1.1 | definition section | high |
| IPFS 整合 DHT、BitTorrent、Git、SFS 和 Merkle structures | source | Chapter 1 summary, Chapter 2 | chapter summary and base-tech sections | high |
| IPFS 协议栈由 Identity/Network/Routing/Exchange/Object/File/Naming 组成 | source | Chapter 3 | protocol-stack section | high |
| BitSwap 是块交换和信用/账单机制，不是链上激励 | source | Chapter 3.4 | want_list/have_list, ledger and strategy sections | high |
| IPLD/CID 是跨内容寻址系统的数据模型与自描述标识 | source | Chapter 4.3 | IPLD/CID sections | high |
| Filecoin 是 IPFS 相关激励层/DSN，不等同于 IPFS | source | Chapter 5.2 | relationship section | high |
| CID 不保证可用性，pinning/private network/gateway 是部署层问题 | source/inference | Chapters 6-7 | pinning, private network and gateway practices | high |

## Knowledge Handoff

- 留在本文元笔记的证据: 目录、章节机制、命令示例、Filecoin 章节、出版信息、具体 go-ipfs/js-ipfs 实战。
- 待更新 Knowledge node: [[content-addressed-storage|Content-addressed Storage and Distribution]], [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]], [[decentralized-storage-networks|Decentralized Storage Networks]], [[off-chain-application-data-management|Off-chain Application Data Management]]。
- 作为哪些 Knowledge node 的 source extension: content-addressed-storage; decentralized-storage-networks; off-chain-application-data-management as foundation reference.
- 需要补的 foundation knowledge/source: IPFS whitepaper/spec, IPLD/CID specs, libp2p docs/spec, Filecoin spec/current docs, PoRep/PoSt direct papers.
- Bridge 候选: content-addressed storage -> decentralized storage networks; content-addressed storage -> off-chain application data management if more sources arrive.
- Review queue: 具体 IPFS/Filecoin 当前状态需未来 freshness run，不在本轮用网页更新。

## Processing Log

| Time | Action | Result |
| --- | --- | --- |
| 2026-06-23 | Queue checkpoint | Processed `item0106` only. |
| 2026-06-23 | Metadata correction | Year corrected to 2019; classification corrected away from consensus. |
| 2026-06-23 | Knowledge absorption | Created content-addressed-storage node and IPFS/Filecoin bridge; refreshed related nodes. |
