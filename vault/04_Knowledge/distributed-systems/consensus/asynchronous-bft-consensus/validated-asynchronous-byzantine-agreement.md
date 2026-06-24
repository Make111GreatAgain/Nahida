---
id: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
title: "Validated asynchronous Byzantine agreement"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "subproblem"
file_slug: "validated-asynchronous-byzantine-agreement"
domain_id: "distributed-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-asynchronous-bft-consensus"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "validated-asynchronous-byzantine-agreement"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement"
secondary_ontology_paths:
  - "distributed-systems/consensus/byzantine-fault-tolerance/validated-asynchronous-byzantine-agreement"
  - "blockchain-systems/consensus/validated-asynchronous-byzantine-agreement"
relation_edges:
  - from: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
    relation: "is_a"
    to: "nahida-knowledge-asynchronous-bft-consensus"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement.md"
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
    relation: "depends_on"
    to: "nahida-knowledge-byzantine-fault-tolerance"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md"
      - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-validated-asynchronous-byzantine-agreement"
    relation: "supported_by_setup"
    to: "nahida-knowledge-asynchronous-distributed-key-generation"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md"
      - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-asynchronous-blockchain-consensus"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md"
  - "vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md"
representative_source_refs:
  - "doi:10.1145/3293611.3331612"
  - "iacr:2019/1015"
query_keys:
  - "Validated asynchronous Byzantine agreement"
  - "validated-asynchronous-byzantine-agreement"
  - "VABA"
  - "externally valid asynchronous Byzantine agreement"
  - "multi-valued asynchronous Byzantine agreement"
  - "external validity"
  - "trusted-dealer-free VABA"
  - "ADKG bootstrap for VABA"
  - "threshold coin setup for VABA"
aliases:
  - "VABA"
  - "validated ABA"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "validated-asynchronous-byzantine-agreement"
  - "asynchronous-bft-consensus"
  - "byzantine-fault-tolerance"
  - "trusted-dealer-free-threshold-setup"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement"
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
source_refs:
  - "doi:10.1145/3293611.3331612"
  - "iacr:2019/1015"
confidence: "high"
trust_tier: "primary"
---

# Validated asynchronous Byzantine agreement

## 定义与范围

- 定义: Validated asynchronous Byzantine agreement (VABA) 是一种多值异步 Byzantine agreement 问题，协议必须在不依赖 timing assumption 的网络中让 honest parties 决定同一个 externally valid value，并且在 honest parties 都输入 valid values 时以非平凡概率选择 honest proposer 的值。
- 不包含: 某一篇 VABA 协议论文、某个 threshold-coin 实现、某个区块链系统的 mempool 或交易选择策略；这些留在 source note 或更下层 source extensions。
- Canonical terms: `validated-asynchronous-byzantine-agreement`, `VABA`
- Aliases/query keys: validated ABA, externally valid asynchronous Byzantine agreement, multi-valued asynchronous Byzantine agreement
- Standalone completeness check: 本节点给出 VABA 的本地定义、问题边界、方法路线、代表 source、迁移边界和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 `VABA`、`external validity`、`async BFT multi-valued agreement` 时先到本节点，再打开代表 source。
- Update scope: 新 source 若改变 VABA 定义、复杂度边界、lower bound、终止模型或与 atomic broadcast/SMR 的关系，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

普通 binary asynchronous Byzantine agreement 只决定 0/1；weakly valid multi-valued BA 也可能让协议决定一个对应用无意义的默认值。Atomic Broadcast、fault-tolerant SMR 和区块链排序需要更强的外部有效性: 决定的命令、批次或交易集合必须能被应用层验证，而且协议不能总是绕开 honest proposer 的真实输入。

VABA 因此处在 `asynchronous-bft-consensus` 的下层: 它不是一个完整 blockchain protocol，而是把异步 Byzantine agreement 变成可用于 atomic broadcast/SMR 的问题原语。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `subproblem`。
- 为什么足够通用: VABA 组织 external validity、多值 async BA、atomic broadcast/SMR primitive、threshold coin/provable broadcast 等多个 source-backed 概念，不等同于单篇 Abraham-Malkhi-Spiegelman 2019 协议。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 2019 PODC paper 是代表 source extension；VABA 本身作为问题早于该论文，且与 Cachin et al. 2001、atomic broadcast、SMR 和后续 async BFT 系统相关。
- 需要引用的更基础 Knowledge: [[asynchronous-bft-consensus|asynchronous-bft-consensus]], [[byzantine-fault-tolerance|byzantine-fault-tolerance]]。
- 不应拆出的实例/协议/来源: `Provable-Broadcast`、`Proposal-Promotion`、`Leader-Election`、`KEY/LOCK/COMMIT` 当前只作为方法行；等多个 sources 证明它们复用广泛时再拆独立节点。

## 解决的问题

VABA 解决的是: 在 full asynchronous network 和 Byzantine/adaptive adversary 下，如何让 parties 对一个 externally valid 的多值输入达成一致，同时保证协议不会退化为“总是输出一个默认 valid value”的空协议，并让通信和时间复杂度足以作为 atomic broadcast/SMR 的基础。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | child_of | VABA 是 async BFT 的 externally valid multi-valued agreement 子问题 | active_seed |
| [[byzantine-fault-tolerance|Byzantine fault tolerance]] | depends_on | fault threshold `f < n/3`, Byzantine agreement safety and quorum intersection | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| external validity predicate | concept candidate | 多个 atomic-broadcast/SMR/blockchain sources 若共同使用，可拆成验证层概念 | VABA paper + future sources needed | queued |
| provable broadcast | method candidate | 若后续 source 显示它是 reusable broadcast abstraction，可从 VABA paper 中提取 | VABA paper §3.1 only | hold |
| threshold coin for async BFT | method candidate | common coin/threshold coin 会横跨 binary BA、ACS、VABA | VABA paper + MMR 2014 seed | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Binary BA reduction / classical VABA route | 将 multi-valued external validity 包装到异步 BA 框架中，再用随机化 binary BA 收敛 | authenticated async BFT，外部有效性可验证 | Cachin et al. 2001 baseline 在本 vault 尚缺直接 source；2019 paper 记录其 expected `O(n^3)` word communication | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| Provable broadcast + proposal promotion | 先让 n 个候选 leader 的 proposal 在每个 view 中可证明推进，再随机选择已完成候选，避免选中后才发现 leader 卡住 | authenticated async BFT, threshold signatures, `f < n/3` | 依赖 threshold signature setup；会议版证明压缩 | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| Threshold-coin leader election | 在 proposal-promotion 完成后用 common coin 选唯一 leader，使 completed leader 被选中的概率大于 `2/3` | threshold coin available, adversary cannot predict coin early | trusted dealer/DKG/setup 是部署边界；不是系统实现本身 | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| KEY/LOCK/COMMIT view change | 用 lock safety、key safety、key progress 保证跨 view 不同值不能同时被提交，同时让已锁值可推进或解锁 | view-based async VABA | 需要维护 threshold proofs；细节留在 source note | [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|VABA 2019]] |
| ADKG bootstrap | 用 asynchronous distributed key generation 生成 threshold coin/signature setup，从而移除 VABA 依赖的 trusted dealer 假设。 | VABA/common coin route needs threshold setup; authenticated async network with PKI | ADKG 本身 initial expected `O(n^4)`；不改变 VABA 的 external-validity problem definition | [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | paper | 为 VABA 提供 `f < n/3`、adaptive adversary、expected `O(1)` running time、expected `O(n^2)` word communication 的代表协议，并把 VABA 连接到 atomic broadcast/SMR | authenticated setting；trusted dealer/random oracle/threshold signatures/threshold coin；10 页会议版；无实现评测 | Abstract, Definition 4, Theorem 1, §3.1-§3.6 |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | paper | 作为 setup-removal source：用 ADKG 为 VABA 所需 threshold coin/signature setup 去除 trusted dealer | 不提出新的 VABA problem/algorithm；initial ADKG cost high and amortized | Corollaries in §1 and §6 |

## 正反例约束

- 正确: 把 VABA 作为 externally valid multi-valued async BA 问题来索引，论文只作为代表来源。
- 正确: 把 external validity、quality property、threshold coin、provable broadcast 和 proposal promotion 作为解决路线或 future split candidates。
- 错误: 把 Abraham-Malkhi-Spiegelman 2019 直接当成 `blockchain consensus` 节点的主内容。
- 错误: 把 `external validity` 当成已经完整定义的独立节点；当前只有 VABA source 支撑，还需更多 source。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-20`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: VABA 是 async BFT 从“决定一个 bit”走向“决定一个应用有效对象”的关键问题层。2019 PODC paper 的结构性信号是: 通过先推进多个候选 proposal、再随机选 leader，可以在 adaptive asynchronous setting 下把 validated multi-valued agreement 的 expected word communication 降到 `O(n^2)`，与 adaptive ABA lower-bound order 对齐。ADKG 2019/1015 不改变 VABA 定义，但把 VABA paper 依赖的 trusted dealer/threshold coin setup 变成可由异步 DKG 生成的 setup 层，因此应作为 VABA 的 setup support，而不是 VABA 本体。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: no implementation evidence in current source.
- Open-problem summary: weak termination 下是否有 lower bound 或 near-linear expected communication protocol 仍开放；Cachin et al. 2001 direct source 尚缺。
- Next refresh trigger: new VABA, atomic broadcast, HoneyBadger/BEAT, common coin, RBC or threshold-setup source.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement|Asymptotically Optimal Validated Asynchronous Byzantine Agreement]] | 新建 VABA 子问题节点；补入 expected `O(n^2)` externally valid multi-valued async BA route | 定义; 解决的问题; 方法族; 当前综合; 缺口与队列 | yes, child under async BFT | 后续补 Cachin 2001、HoneyBadger/BEAT/RBC/common coin sources |
| [[eprint-2019-1015-asynchronous-distributed-key-generation|Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures]] | 补入 VABA trusted-dealer-free setup support；保持 ADKG 细节在独立 method 节点 | 方法族; 代表 Sources; 当前综合; relation graph | no, setup support only | 后续补 common coin / threshold setup lineage |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | `distributed-systems/consensus/byzantine-fault-tolerance; distributed-systems/consensus/asynchronous-bft-consensus` | dependency, translation | VABA transfers BA safety and external validity toward atomic broadcast/SMR; transaction dissemination, validator economics, mempool policy and deployment setup remain blockchain/application-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-validated-asynchronous-byzantine-agreement | is_a | nahida-knowledge-asynchronous-bft-consensus | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement.md; vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus.md | high | active_seed |
| nahida-knowledge-validated-asynchronous-byzantine-agreement | depends_on | nahida-knowledge-byzantine-fault-tolerance | vault/04_Knowledge/distributed-systems/consensus/byzantine-fault-tolerance.md; vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | high | active_seed |
| nahida-knowledge-validated-asynchronous-byzantine-agreement | evidenced_by | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | vault/03_Sources/papers/doi-10-1145-3293611-3331612-asymptotically-optimal-validated-asynchronous-byzantine-agreement.md | high | active_seed |
| nahida-knowledge-validated-asynchronous-byzantine-agreement | supported_by_setup | nahida-knowledge-asynchronous-distributed-key-generation | vault/04_Knowledge/distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation.md; vault/03_Sources/papers/eprint-2019-1015-asynchronous-distributed-key-generation.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Cachin et al. 2001 VABA direct source 尚未导入。 | 当前 `O(n^3)` baseline 来自 2019 paper 的相关工作和 open-problem framing | nahida-research-search or nahida-update | high | queued |
| weak termination 下的 lower bound/protocol 未覆盖。 | 2019 paper 明确把它作为 open question | nahida-research-search | medium | queued |
| common coin、RBC、HoneyBadger/BEAT 与 VABA 的关系仍需更多 source。 | 决定 async BFT 到 atomic broadcast/SMR 的完整路径 | nahida-update | medium | queued |
| VABA 的 trusted-dealer-free setup lineage 仍薄。 | ADKG 2019/1015 给出 setup-removal route，但 common coin/DKG 后续发展与实现工程尚未覆盖。 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-vaba-validated-asynchronous-byzantine-agreement | Created VABA knowledge node from PODC 2019 source; connected to async BFT, BFT and async blockchain bridge. | doi:10.1145/3293611.3331612 | codex |
| 2026-06-23 | nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft | Added ADKG as trusted-dealer-free setup support for VABA threshold coin/signatures. | iacr:2019/1015 | codex |
