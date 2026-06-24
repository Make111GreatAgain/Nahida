---
id: "arxiv:2208.09937"
title: "An Incentive-Compatible Mechanism for Decentralized Storage Network"
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
  - "p1-p2 abstract, introduction, DSN motivation, service-denial attack and claimed benefits"
  - "p2-p3 related work: Filecoin, Storj, Sia, Swarm, proof of storage, proof of retrievability and vector commitments"
  - "p3-p4 DSN architecture, storage contract, design goals and threat boundaries"
  - "p4-p6 repeated dynamic game model, payoff inequalities, challenge cost and subgame-perfect equilibrium"
  - "p6-p8 smart-contract/oracle architecture, challenge flow, challenge levels and Merkle proof-of-storage construction"
  - "p8 request-counting support and signed request counter"
  - "p8-p10 Solidity, Chainlink, Node.js prototype and gas/computation evaluation"
  - "p10-p13 conclusion, references and detailed timing tables"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2208.09937"
doi: ""
arxiv_id: "2208.09937"
venue: "arXiv preprint"
year: "2022"
pdf_pages: 13
pdf_sha256: "e1d866d2523f8afa309caa04c3d05b1b948e34ec36fd9e073a1808bd2ad6f0c9"
local_pdf: "~/Desktop/paper/2208.09937.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2208.09937-e1d866d2523f-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "decentralized-storage-networks"
  - "storage-service-incentives"
  - "proof-of-storage"
ontology_path:
  - "blockchain-systems"
  - "data-management-and-storage"
  - "decentralized-storage-networks"
primary_ontology_path: "blockchain-systems/data-management-and-storage/decentralized-storage-networks"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments"
  - "verifiable-computation/verifiable-computation-systems"
path_update_status: "corrected_from_queue"
related_knowledge_refs:
  - "nahida-knowledge-decentralized-storage-networks"
  - "nahida-knowledge-blockchain-data-management-and-storage"
  - "nahida-knowledge-contingent-service-payments"
  - "nahida-knowledge-verifiable-computation-systems"
bridge_refs:
  - "nahida-bridge-decentralized-storage-networks-to-contingent-service-payments"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "verifiable-computation"
  directions:
    - "data-management-and-storage"
    - "execution-and-transactions"
    - "verifiable-computation-systems"
  topics:
    - "decentralized-storage-networks"
    - "storage-service-incentives"
    - "proof-of-storage"
    - "proofs-of-retrievability"
    - "contingent-service-payments"
domains:
  - "blockchain-systems"
  - "verifiable-computation"
topics:
  - "decentralized storage network"
  - "storage service incentive"
  - "proof of storage"
  - "proof of retrievability"
  - "smart contract storage contract"
  - "oracle-assisted verification"
  - "service denial attack"
aliases:
  - "ICM-DSN"
  - "Incentive-compatible DSN"
  - "challenge-based decentralized storage mechanism"
  - "DSN storage service mechanism design"
authors:
  - "Iman Vakilinia"
  - "Weihong Wang"
  - "Jiajun Xin"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-management-and-storage"
  - "decentralized-storage"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "data-management-and-storage"
    - "execution-and-transactions"
  problem:
    - "decentralized storage networks need incentives for honest storage and retrieval service without continuous proof checks"
    - "storage providers may submit valid proof of storage to a network while denying service to the client"
    - "retrieval request counts and dynamic pricing are difficult when clients and storage providers can both deviate"
  method_family:
    - "challenge-based storage verification"
    - "repeated dynamic game mechanism design"
    - "smart contract storage agreement"
    - "oracle-assisted off-chain verification"
    - "Merkle-tree proof of storage"
  system_layer:
    - "DSN storage market"
    - "smart contract escrow and collateral"
    - "oracle network"
    - "off-chain data transfer"
    - "proof-of-storage verification"
  evaluation_context:
    - "Solidity 0.8.7"
    - "Kovan Ethereum test network"
    - "Chainlink oracle"
    - "Node.js external adapter and storage-provider HTTP server"
    - "10MB to 1GB files"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-incentive-compatible-decentralized-storage"
source_refs:
  - "arxiv:2208.09937"
  - "pdf:~/Desktop/paper/2208.09937.pdf"
  - "github:https://github.com/podiumdesu/ICM-DSN"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> data-management-and-storage -> decentralized-storage-networks"
secondary_directions:
  - "blockchain-systems -> execution-and-transactions -> fair-exchange-protocols -> contingent-service-payments"
  - "verifiable-computation -> verifiable-computation-systems"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p13"
  - "abstract and Sections 2-3 discuss decentralized storage networks, proof of storage and storage service contracts"
  - "Sections 4-5 define challenge-based storage verification, smart contracts and oracle-assisted Merkle proof checks"
  - "the paper does not study consensus safety, validator finality or block ordering"
  - "classification corrected from blockchain-systems/consensus/consensus-foundations"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0088"
queue_status: "absorbed"
---

# An Incentive-Compatible Mechanism for Decentralized Storage Network

## 论文身份

- 标题: An Incentive-Compatible Mechanism for Decentralized Storage Network
- 作者: Iman Vakilinia; Weihong Wang; Jiajun Xin
- 版本: arXiv `2208.09937v1`, `cs.GT`, 2022-08-21
- 本地 PDF: `~/Desktop/paper/2208.09937.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/2208.09937-e1d866d2523f-pages.txt`
- SHA-256: `e1d866d2523f8afa309caa04c3d05b1b948e34ec36fd9e073a1808bd2ad6f0c9`
- 论文给出的原型仓库: `https://github.com/podiumdesu/ICM-DSN`。本次只读论文，未重新分析仓库代码。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- 已覆盖: 摘要/引言、DSN 相关工作、PoS/PoR/VC 背景、系统模型、设计目标、动态博弈、挑战式协议、Merkle PoS、请求计数、Solidity/Chainlink 原型和性能表。
- Extraction gaps: 图 5/图 6 的曲线只按正文趋势和附录表格记录；公式排版有断行，但 payoff 关系和参数语义已保留。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p2 | 问题与贡献 | DSN 通过区块链建立存储市场，但持续 PoS 昂贵，且存在 provider 给网络证明却拒绝客户端服务的攻击。 | high |
| §2 / p2-p3 | 相关工作 | Filecoin/Sia/Storj/Swarm、Proof of Storage、PDP、PoSt、PoR、vector commitments。 | high |
| §3 / p3-p4 | 系统模型 | DSN 包含付款结算和存储验证；storage contract/SLA 包括时长、价格、QoS、补偿。 | high |
| §4.1 / p4-p6 | 机制设计 | 把 storage contract 建模为 repeated dynamic game，目标均衡是 `{Share, No Challenge}`。 | high |
| §4.2 / p6-p8 | 协议架构 | smart contract 保存 Merkle root、premium、collateral；oracle 接收 challenge、取数据和 Merkle path、验证并转发/报错。 | high |
| §4.2.1 / p7-p8 | PoS 构造 | 用 Merkle tree 存 digest，挑战 segment 时返回原始 segment 和 Merkle path；链上只存 root。 | high |
| §4.2.2 / p8 | 请求计数 | 客户端签名请求含 counter，provider cash-out 时提交最后一个 signed request。 | medium |
| §5 / p8-p10 | 实现和评估 | Solidity/Kovan/Chainlink/Node.js prototype；合约部署、记录任务、挑战请求 gas；不同文件和 segment size 的时间。 | high |
| Appendix / p12-p13 | 详细表格 | 10MB 到 1GB 文件下 reading/root/path/verification timing。 | medium |

## 一句话贡献

这篇论文把去中心化存储网络的“持续证明存储”改成“客户端挑战时才验证”的机制设计问题: 用重复动态博弈设置押金、挑战成本和证明转发路径，让 storage provider 的均衡策略是诚实保存并向客户端提供数据，同时用 smart contract 和 oracle 把争议验证限制在 challenge 路径中。

## 论文要解决的问题

当前 DSN 方案通常让 storage provider 周期性向网络提交 PoS/PoSt/PDP 证明。论文认为这有两个系统性问题:

| 问题 | 论文解释 | 为什么不是 consensus 问题 |
| --- | --- | --- |
| Continuous verification cost | 持续验证会增加网络和终端用户成本，尤其当大多数合约期内没有争议时。 | 这是存储服务审计频率和费用问题，不涉及 block ordering 或 validator agreement。 |
| Service denying attack | 恶意 provider 可以向 DSN 节点提交有效 PoS，但拒绝向客户端返回数据。 | 网络知道“数据仍可被证明”，不等于客户端实际获得服务；这是服务可用性和激励兼容问题。 |
| Dynamic request pricing | 传统 DSN 难以按读取请求次数动态收费，因为 ack/计数本身可被双方操纵。 | 请求计数属于服务合同和付款结算层。 |

## 分类判断

队列旧路径是 `blockchain-systems/consensus/consensus-foundations`，本次精读后纠正为:

```text
blockchain-systems / data-management-and-storage / decentralized-storage-networks
```

原因: 论文核心对象是 DSN 存储市场、storage contract、proof of storage、client/provider 激励和链上/链下验证架构。它没有讨论拜占庭/崩溃故障共识、validator quorum、最终性或 block proposal。

Secondary path 是:

```text
blockchain-systems / execution-and-transactions / fair-exchange-protocols / contingent-service-payments
```

因为挑战式存储合约同样处理服务付款、押金、争议和可验证服务结果，只是它的主问题是 DSN 存储服务，而非通用 fair exchange。

## 背景与相关工作

论文把 DSN 作为算法化存储市场: 客户端付费外包数据，微型 storage providers 出售闲置存储，区块链负责激励和结算。代表系统包括 Filecoin、Sia、Storj 和 Swarm。

| 系统/路线 | 论文中的角色 | 边界 |
| --- | --- | --- |
| Filecoin | 用 active storage 决定 mining power，并用 Proof-of-Spacetime 检查长期存储；工作在 IPFS 之上。 | 仍属于周期性证明路线；本文想减少持续验证。 |
| Storj | 用 satellite 管理审计、repair、支付、metadata 和节点账户。 | satellite 弱化完全去中心化，且生产/测试环境 DoS 风险需区分。 |
| Sia | file contract 记录价格和 uptime commitment，用 Merkle-tree auditing 让 host 提交随机 segment 证明。 | 仍要求按时间窗向网络提交证明。 |
| Swarm | 为 Ethereum 生态提供存储/服务激励和分发，强调 DDoS-resistant、zero downtime 和自维持激励。 | 本文不重建 Swarm 激励系统，只抽象 DSN contract。 |
| PoR/PDP/PoS | 提供服务器仍保存数据的密码学证据。 | PoR 更强但常有额外密码学/开销；本文选 Merkle PoS 因为 digest 小、无 trusted setup。 |
| Vector commitments | 可作为 succinct membership/position proof。 | RSA/双线性/lattice 路线各有 setup、公共参数或开销问题。 |

## 系统模型

论文中的 DSN 有两个主要模块:

- Payment settlement: 收取客户端费用，支付 storage provider；provider 失败时罚没抵押并补偿客户端。
- Storage verification: 检查 provider 是否仍按合约保存数据，并在挑战时验证证明。

Storage contract/SLA 包含合约长度、费用、服务质量、交付时间、补偿和 Merkle root 等字段。客户端可在上传前加密数据；provider 的冗余、服务器位置、备份和带宽策略被视为 provider 内部优化，不在论文范围内。

## 动态博弈机制

论文把每次服务请求建模为重复动态博弈:

1. Storage provider 选择 `Share` 或 `Not Share`。
2. Client 选择 `Challenge` 或 `No Challenge`。
3. 若挑战发生，storage provider 选择 `Proof` 或 `No Proof`。

目标是让 `{Share, No Challenge}` 成为 subgame-perfect equilibrium。

关键 payoff 约束:

- `No Proof` 是 provider 最差结果，因为要向客户端支付补偿。
- 若 provider 能证明存储，则会选择 `Proof` 而不是 `No Proof`。
- 机制必须让诚实 `Share` 的成本低于被挑战后 `Proof` 的成本，否则 provider 会倾向于先不服务、被挑战再证明。
- 挑战需要对客户端有成本 `X`，否则诚实服务时客户端可能滥用挑战。
- 但在 provider 未服务时，挑战必须有正期望收益: 论文用 `Cc = P*C5 + (1-P)*V - X` 表示挑战期望效用，其中 `P` 是 provider 无法提供服务的概率，`V` 是客户端拿到数据的价值。

这组设计的直觉是: 客户端不应在一切正常时挑战；一旦 provider 拒绝服务，挑战既能拿到数据或补偿，又让 provider 暴露失败。

## 协议架构

论文的协议分为链上合约、oracle 网络和链下数据路径:

1. Client 与 storage provider 达成存储协议，包含合约长度、Merkle root、premium、delivery time 和 compensation。
2. Smart contract 保存 Merkle root、客户端 premium 和 provider collateral。
3. 正常情况下，client 直接向 provider 请求数据，数据传输走链下路径。
4. 若 provider 不服务或返回错误，client 调用合约的 `challenge` 函数，并指定 challenged segment number。
5. Oracle network 向 provider 发出挑战，provider 返回 segment 和 Merkle path。
6. Oracle 计算 root 并与链上 Merkle root 对比。
7. 验证通过时，oracle 把数据副本转发给 client；验证失败时，oracle 向 smart contract 报告 failure，合约按约定把 provider collateral 补偿给 client。

这一步是论文防 service denying attack 的核心: provider 不能只向网络提交证明而不服务客户端，因为挑战路径要求它把被挑战数据给 oracle，再由 oracle 转发给 client。

## Challenge level

为避免大文件挑战过于昂贵，论文允许客户端和 provider 预先把数据分成多个 segments。客户端可以挑战一组 segments，挑战价格随 segment 大小和数量增加。其作用是两边的激励约束:

- 客户端不能低成本滥用挑战来对 provider 做 DoS。
- Provider 不能把“被挑战后一次性传全量数据”的成本作为拒绝协议的理由。
- 对大数据集，挑战可以按抽样/局部段落执行。

## Merkle-tree Proof of Storage

论文定义 PoS 为 `(Setup, Prove, Verify)`:

- `Setup(1^lambda, D, sz)` 输出 digest `d` 和 Merkle tree height `h`。
- `Prove(D, c)` 对 challenged node/segment 输出 proof `pi`。
- `Verify(d, h, c, pi)` 检查 proof 是否能重建链上 digest。

构造方式:

- 将数据 `D` 切为 segments `S = {s1, ..., sm}`，不足 2 的幂时用 0 padding。
- 每个 segment hash 是 Merkle leaf。
- 挑战某个节点时，proof 包含对应 raw segment 和 Merkle path sibling nodes。
- Client 和 provider 各自运行 Setup，并签名 `(d, h)`；合约验证双方签名后只保存 Merkle root。

论文选择 Merkle tree 的理由不是“最强 PoR”，而是 DSN 链上合约场景下 digest 小、无需 trusted setup、公共参数少，且验证成本已纳入 incentive layer。

## 请求计数与动态定价

论文指出，存储服务价格通常和读取请求次数有关，但 naive request counting 要求 provider 返回数据后 client 再签 ack；恶意 client 可以拒绝 ack。论文沿用博弈式挑战机制:

- Client 发送带 counter 的 signed request。
- Provider 收到请求后选择发送或不发送数据。
- 若 provider 不发送，client 可挑战。
- Provider cash-out 时只需提交最后一个 signed request，counter 表示累计请求次数。

这让动态 pricing 不依赖每段数据的 signed acknowledgement。

## 实现与评估

论文原型:

- Solidity `0.8.7` smart contract。
- Kovan Ethereum test network 与 Remix IDE。
- Chainlink oracle；Chainlink core 将 challenge 路由到 external adapter。
- External adapter 用 Node.js HTTP server 编写，调用 simulated storage-provider API。
- Storage provider HTTP server 支持计算 Merkle root、访问文件和生成 Merkle path。
- React/Parcel demo website。

链上 gas:

| Operation | Gas units |
| --- | ---: |
| Contract deployment | 2,491,606 |
| Recording a storage task | 202,001 |
| Challenge request | 192,101 |

性能评估使用 macOS 12.0.1、Apple M1 Pro、32GB 内存，文件大小从 10MB 到 1GB，segment size 从 128B 到 128KB。论文报告:

- segment size 增大时，file reading、Merkle root calculation 和 Merkle path generation 时间下降且边际下降变小。
- Merkle path verification 很快，并且随着 segment size 增大略降。
- 同一 segment size 下，文件变大时 reading/root/path generation 时间同步增长；verification time 仍保持很小。
- 对 1GB 文件和 128KB segment，附录表给出 file reading 约 3446 ms、Merkle root 约 23.972 ms、Merkle path generation 约 20.959 ms、verification 约 0.0305 ms。

## 局限与边界

- 单篇 source seed: 它足以创建 DSN/storage-incentive 问题节点，但不足以完成 Filecoin/Sia/Storj/Swarm 或 PoR/PDP foundation。
- Oracle trust boundary: 论文使用 Chainlink oracle 把链下验证和数据转发接入合约，但没有深入讨论 oracle collusion、availability 或 oracle cost market。
- Merkle PoS is not full PoR: 论文承认 PoR 保证更强；当前构造更像低成本 challenge-time possession proof。
- Game-theoretic assumptions: payoff 设计依赖 rational/self-interested players、挑战成本、补偿金额和数据价值的关系；非理性 DoS 或被盗密钥不由模型覆盖。
- Evaluation scope: 原型验证可行性和计算成本，但未在真实 Filecoin/Sia/Storj 网络或长期经济环境中部署。

## 可吸收知识

| Candidate | Handling | Reason |
| --- | --- | --- |
| `decentralized-storage-networks` | create knowledge node | DSN 是可复用应用/问题层，已有 Filecoin/Sia/Storj/Swarm/PoS/PoR 生态和后续 source 队列。 |
| `storage-service-incentives` | section under DSN node | 当前主要由本文支撑；等多篇 storage incentive source 后再拆独立子节点。 |
| `proof-of-storage` / `proofs-of-retrievability` | review/foundation gap | 本文给背景和 Merkle PoS 实例，但 PoS/PoR foundation 需要直接 canonical sources。 |
| `ICM-DSN` | source-local system instance | 不应成为上层概念；它是本文提出的具体机制。 |
| DSN -> contingent service payments | bridge | 与 RC-S-P 都处理可验证存储服务的付款/争议/客户端-provider 激励，但边界不同。 |

## Evidence anchors

| Evidence | Supports |
| --- | --- |
| Abstract, §1 p1-p2 | DSN motivation, continuous PoS cost, service-denial attack, challenge-based contribution. |
| §2.1 p2 | Filecoin, Sia, Storj, Swarm as DSN landscape. |
| §2.2 p2-p3 | PoS/PDP/PoR/vector commitment background and Merkle/VC tradeoffs. |
| §3 p3-p4 | DSN payment settlement, storage verification and SLA model. |
| §4.1 p4-p6 | Dynamic game, payoff inequalities and equilibrium target. |
| §4.2 p6-p8 | Smart contract/oracle challenge flow and Merkle proof architecture. |
| §4.2.2 p8 | Signed request counter for dynamic pricing. |
| §5 p8-p10 | Solidity/Chainlink implementation and gas/performance evaluation. |

## Handoff to knowledge

- Primary knowledge: [[decentralized-storage-networks|Decentralized Storage Networks]]
- Parent direction: [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]]
- Bridge: [[decentralized-storage-networks-to-contingent-service-payments|Decentralized storage networks -> contingent service payments]]
- Queue correction: `blockchain-systems/consensus/consensus-foundations` -> `blockchain-systems/data-management-and-storage/decentralized-storage-networks`
