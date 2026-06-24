---
id: "nahida-knowledge-asynchronous-data-dissemination"
title: "Asynchronous data dissemination"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method"
hierarchy_level: "method"
file_slug: "asynchronous-data-dissemination"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-data-dissemination"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast"
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing"
relation_edges:
  - from: "nahida-knowledge-asynchronous-data-dissemination"
    relation: "is_a_method_for"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-data-dissemination"
    relation: "supports"
    to: "nahida-knowledge-asynchronous-reliable-broadcast"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-data-dissemination"
    relation: "supports"
    to: "nahida-knowledge-asynchronous-verifiable-secret-sharing"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-data-dissemination"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-asynchronous-data-dissemination"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md"
      - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md"
representative_source_refs:
  - "iacr:2021/777"
query_keys:
  - "Asynchronous data dissemination"
  - "asynchronous-data-dissemination"
  - "ADD"
  - "Byzantine data dissemination"
  - "coded data dissemination"
  - "Reed-Solomon asynchronous dissemination"
  - "online error correction dissemination"
  - "long-message dissemination in asynchronous BFT"
aliases:
  - "ADD"
  - "asynchronous data dissemination"
  - "coded asynchronous dissemination"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous-bft-consensus"
  - "asynchronous-data-dissemination"
  - "asynchronous-reliable-broadcast"
  - "data-dissemination"
tags:
  - "nahida/knowledge"
  - "nahida/method"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
source_refs:
  - "iacr:2021/777"
confidence: "high"
trust_tier: "primary"
---

# Asynchronous data dissemination

## 定义与范围

- 定义: Asynchronous data dissemination (ADD) 是异步 Byzantine 网络中的长消息传播 primitive；当至少 `t+1` 个 honest nodes 初始持有同一个消息 `M` 时，它要求所有 honest nodes 最终输出 `M`。
- 不包含: 完整 consensus protocol、mempool、data availability sampling、单篇论文全文或某个 blockchain 系统实现；这些分别留在 source note 或其他上层节点。
- Canonical terms: `asynchronous-data-dissemination`, `ADD`
- Aliases/query keys: ADD, coded asynchronous dissemination, long-message dissemination in asynchronous BFT
- Standalone completeness check: 本节点给出本地定义、问题、方法路线、代表 source、边界和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 ADD、长消息广播成本、异步 BFT payload dissemination、RBC/AVSS/ADKG 通信复杂度时先到本节点。
- Update scope: 新 source 若改变 fault threshold、message-size threshold、coding technique、RBC/AVSS application 或 lower bound，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

异步 BFT 协议经常需要让一个大对象被所有 honest nodes 获得: block payload、batch、commitment vector、encrypted shares、proof material 或 AVSS/ADKG 里的大消息。直接让每个初始持有者把完整消息发给所有节点会产生 `O(n^2 |M|)` 通信。

ADD 把这个问题拆成两层: 大对象用 erasure coding 分散，小控制消息用 quorum 和纠错检查维持 Byzantine 安全。这样长消息的主成本接近 `O(n|M|)`，额外控制成本保持 `O(n^2)`。

## 基础概念判断

- 是否是基础概念/方向/问题: `method` / `method`。
- 为什么足够通用: ADD 可作为 RBC、AVSS、ACSS、ADKG 和 asynchronous atomic broadcast 的共享通信层，不等同于某个单独协议实例。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 当前代表 source 是 2021/777；ADD 本身是可被其他 broadcast/secret-sharing/consensus source 复用的 problem/primitive。
- 需要引用的更基础 Knowledge: [[asynchronous-bft-consensus|asynchronous-bft-consensus]], [[asynchronous-reliable-broadcast|asynchronous-reliable-broadcast]]。
- 不应拆出的实例/协议/来源: 2021/777 的 Algorithm 1、HOEC 和 concrete constants 留在 source note；后续若多源复用 online error correction 再考虑拆出。

## 解决的问题

ADD 解决的是: 在异步调度和 Byzantine 节点存在时，如何让一个已经由至少 `t+1` 个 honest nodes 持有的大消息被所有 honest nodes 获得，同时避免每个 sender 都全量广播大消息。

它不是 consensus 决定值问题，而是 consensus 和 secret-sharing 之下的 data movement 问题。对长消息协议来说，ADD 决定了 payload 成本能否从二次级下降到线性级。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | method_for | ADD is used to improve RBC, async atomic broadcast, AVSS/ACSS and ADKG communication | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| online error correction for coded dissemination | method candidate | OEC is the decoding test that lets nodes reconstruct despite Byzantine symbols | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | hold |
| high-threshold ADD | method candidate | Extends ADD to `n>2t` with hash-assisted consistency but changes cost and assumptions | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] | hold |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Reed-Solomon coded ADD | 每个 sender 编码 `M`，每个 receiver 只接受 `t+1` 个相同 sender-symbol，再全网广播 accepted symbol 并用 OEC 重构 | asynchronous network, `n=3t+1`, at least `t+1` honest initial holders | `O(n|M|+n^2)` communication；消息需足够大才摊平 field symbol overhead | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| Hash-assisted high-threshold ADD | 用 collision-resistant hash 绑定消息和 coded symbols，使 ADD 可扩展到 `n>2t` | asynchronous network, `n>2t`, hash assumption | 成本为 `O(n^2 |M|/(n-2t)+n^2 kappa)`；不再是纯信息论核心 | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |
| ADD-backed long-message RBC | 先用 RBC 广播 hash，再让持有 payload 的 honest nodes 运行 ADD | long-message RBC, collision-resistant hash | `O(n|M|+kappa n^2)`；classic Bracha RBC direct source仍待补 | [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | paper | 引入 ADD 定义和 `O(n|M|+n^2)` coded dissemination protocol，并给出 lower bound 与 RBC/AVSS/ACSS/ADKG 应用 | main ADD: `t<n/3`, information-theoretic; RBC/high-threshold variants use collision-resistant hash; no implementation benchmark | Definition 3.1, Algorithm 1, Theorem 3.5, §4-§6 |

## 正反例约束

- 正确: 把 ADD 作为异步系统长消息传播 primitive，用来解释 RBC、AVSS、ACSS、ADKG 的 payload 成本。
- 正确: 把具体编码、OEC 和 high-threshold hash variant 的算法细节放回 source note。
- 错误: 把 ADD 当作共识协议或 blockchain data availability sampling。
- 错误: 把 ADD 的 `t+1` 初始 honest holders 假设省略掉；这是定义成立的关键前提。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: ADD 在 async BFT 栈中补上了“长消息如何被可靠地移动”的方法层。它不决定共识值，也不替代 RBC/ACS/AVSS/ADKG；它把这些协议里大对象传播的通信瓶颈降为 `O(n|M|+n^2)` 量级，并由 ADD-backed RBC 把若干 `log n` 因子从上层协议成本中移除。后续如果导入 HoneyBadger/AVID/Bracha RBC 或现代 data availability source，应继续校准 ADD 和 RBC、shared mempool、DAS 的边界。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: no implementation evidence in current source.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new RBC, AVID, HoneyBadger, AVSS/ACSS, ADKG or data-dissemination source.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2021-777-asynchronous-data-dissemination|Asynchronous Data Dissemination and its Applications]] | 新建 ADD method 节点；补入 long-message dissemination route and lower bound | 定义; 方法族; 代表 Sources; 当前综合; Bridge Links | yes, child/method under async BFT | 后续补 Bracha RBC、AVID/HoneyBadger 和 modern data availability/dissemination sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/asynchronous-bft-consensus` | dependency, payload_dissemination_transfer | ADD/RBC communication ideas transfer to long block/batch dissemination in asynchronous ordering; they do not specify mempool policy, data availability sampling, validator membership, execution or economic finality. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-asynchronous-data-dissemination | is_a_method_for | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | high | active_seed |
| nahida-knowledge-asynchronous-data-dissemination | supports | nahida-knowledge-asynchronous-reliable-broadcast | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast.md | high | active_seed |
| nahida-knowledge-asynchronous-data-dissemination | supports | nahida-knowledge-asynchronous-verifiable-secret-sharing | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing.md | high | active_seed |
| nahida-knowledge-asynchronous-data-dissemination | evidenced_by | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | high | active_seed |
| nahida-knowledge-asynchronous-data-dissemination | bridges_to | nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus | vault/05_Bridges/distributed-bft-to-asynchronous-blockchain-consensus.md; vault/03_Sources/papers/eprint-2021-777-asynchronous-data-dissemination.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Bracha RBC and AVID direct sources 尚缺。 | ADD-backed RBC 的比较对象需要直接 foundation source 校准。 | nahida-research-search or nahida-update | high | queued |
| ADD 与 shared mempool / data availability sampling 的边界还需更多 source。 | 区块链系统中 payload movement、availability proof 和 ordering 的边界容易混淆。 | nahida-update | medium | queued |
| Implementation benchmarks 缺失。 | 当前 source 主要是渐进通信和 concrete constants，没有系统性能评测。 | nahida-research-search | low | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Created ADD method node and linked it to async BFT, RBC, AVSS and blockchain-consensus bridge. | iacr:2021/777 | codex |
