---
id: "arxiv-1809.09044v1"
title: "Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities"
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
  - "PDF p1 ResearchGate wrapper and metadata"
  - "paper p1-p4 abstract, motivation, blockchain/light-client background, Merkle and erasure-code preliminaries"
  - "paper p5-p11 threat model, state transition model, block/header data structure, execution traces, transition fraud proofs"
  - "paper p11-p24 data availability proofs, 2D Reed-Solomon encoding, random sampling, selective share disclosure, codec fraud proofs, security analysis"
  - "paper p24-p28 implementation, complexity, benchmarks, succinct-proof and locally-decodable-code discussion"
  - "paper p28-p33 related work, conclusion, appendices A-B"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1809.09044"
doi: "10.48550/arxiv.1809.09044"
arxiv_id: "1809.09044v1"
venue: "arXiv preprint"
year: "2018"
pdf_pages: 34
pdf_sha256: "37dc41ed591d94d627e9103041f60c9155981e29fadf8bc097fe3bd95391dafd"
local_pdf: "~/Desktop/paper/Fraud_Proofs_Maximising_Light_Client_Security_and_.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/fraud_proofs_maximising_light_client_security_and_-37dc41ed591d-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
topic_ids:
  - "data-availability-sampling"
  - "fraud-proofs"
  - "light-client-security"
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "data-availability-sampling"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/data-availability-sampling/arxiv-1809.09044v1"
secondary_ontology_paths:
  - "blockchain-systems/data-availability-and-light-clients/fraud-proofs/arxiv-1809.09044v1"
  - "blockchain-systems/scaling-and-sharding/sharded-ledgers/arxiv-1809.09044v1"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
  directions:
    - "data-availability-and-light-clients"
    - "scaling-and-sharding"
    - "execution-and-transactions"
  topics:
    - "data-availability-sampling"
    - "fraud-proofs"
    - "light-client-security"
    - "state-transition-validation"
    - "erasure-coded-blocks"
domains:
  - "blockchain-systems"
topics:
  - "fraud proofs"
  - "data availability proofs"
  - "data availability sampling"
  - "light clients"
  - "SPV clients"
  - "2D Reed-Solomon encoding"
  - "erasure coding"
  - "state transition fraud proofs"
  - "codec fraud proofs"
  - "sharding"
aliases:
  - "Fraud Proofs"
  - "Fraud Proofs with Dishonest Majorities"
  - "data availability proofs"
  - "light-client fraud proofs"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-availability"
  - "light-clients"
direction_facets:
  parent_domain:
    - "blockchain-systems"
  subdomain:
    - "data-availability-and-light-clients"
    - "scaling-and-sharding"
  problem:
    - "light clients need invalid-block detection without honest-majority consensus assumptions"
    - "fraud proofs require block data availability before honest full nodes can generate proofs"
    - "erasure-coded availability sampling must also detect incorrectly generated extended data"
  method_family:
    - "state transition fraud proofs"
    - "2D Reed-Solomon data availability sampling"
    - "codec fraud proofs"
    - "sparse Merkle state witnesses"
    - "execution traces"
  system_layer:
    - "block header data root and state root"
    - "light-client sampling protocol"
    - "full-node fraud proof generation"
    - "network gossip and recovery"
  evaluation_context:
    - "Go prototype"
    - "250 KB and 1 MB block examples"
    - "single-client and multi-client probability analysis"
  bridge:
    - "fraud proofs -> data availability sampling"
    - "data availability -> sharded ledgers"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
source_refs:
  - "doi:10.48550/arxiv.1809.09044"
  - "arxiv:1809.09044v1"
  - "sha256:37dc41ed591d94d627e9103041f60c9155981e29fadf8bc097fe3bd95391dafd"
  - "pdf:~/Desktop/paper/Fraud_Proofs_Maximising_Light_Client_Security_and_.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> data-availability-and-light-clients"
secondary_directions:
  - "blockchain-systems -> scaling-and-sharding"
  - "blockchain-systems -> execution-and-transactions"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title, abstract and arXiv identifier in PDF"
  - "Sections 4-5 define fraud proofs and data availability proofs"
  - "Sections 5.6-5.7 and Section 6 provide probability/security and implementation evidence"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0041"
queue_status: "absorbed"
---

# Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities

## 论文身份

- 标题: Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities
- 作者: Mustafa Al-Bassam, Alberto Sonnino, Vitalik Buterin
- 机构: University College London; Ethereum Research
- 会议/期刊: arXiv preprint; PDF wrapper also shows ResearchGate upload page
- 年份: 2018
- DOI: `10.48550/arxiv.1809.09044`
- arXiv: `1809.09044v1`
- 链接: https://arxiv.org/abs/1809.09044
- 本地 PDF: `~/Desktop/paper/Fraud_Proofs_Maximising_Light_Client_Security_and_.pdf`
- SHA-256: `37dc41ed591d94d627e9103041f60c9155981e29fadf8bc097fe3bd95391dafd`
- 抽取文本: `vault/02_Raw/pdf/extracted/fraud_proofs_maximising_light_client_security_and_-37dc41ed591d-pages.txt`
- 代码: PDF footnote lists `https://github.com/musalbas/rsmt2d`, `https://github.com/asonnino/fraudproofs-prototype`, and `https://github.com/musalbas/smt`; repository code was not inspected in this run.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 34 PDF pages; page 1 is a ResearchGate wrapper, paper text starts on PDF page 2.
- 已覆盖章节/页码: Abstract, Sections 1-9, references, Appendices A-B.
- Extraction gaps: PDF p7 extraction repeats Figure 1 surrounding text many times; core threat model and later sections remain readable. Formulas are noisy but enough to reconstruct definitions, theorem statements, and benchmark tables.
- 精读说明: 本文是 light-client security + data availability 的 foundational seed。吸收时应把 `Fraud Proofs` 作为可复用机制节点 seed，而不是把论文标题升级成知识节点。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| PDF p1 | wrapper metadata | ResearchGate wrapper, title, DOI, partial author profile info | low | 真正论文从 PDF p2 开始 |
| Abstract, §1 / PDF p2-p3 | 问题与贡献 | light clients 不应继续假设 consensus majority honest；fraud proofs + data availability proofs 支持 on-chain scaling and sharding | high | 核心定位 |
| §2 / PDF p3-p5 | background | blockchain models, full vs light clients, UTXO/account models, Merkle/sparse Merkle, Reed-Solomon coding | high | foundation |
| §3 / PDF p5-p8 | threat model | block producers may be dishonest; at least one honest full node; each light client connects to an honest full node; bounded delay `delta`; minimum honest light clients for DA | high | assumption boundary |
| §4.1-§4.3 / PDF p8-p11 | fraud-proof-friendly block structure | header includes `prevHash`, `dataRoot`, `dataLength`, `stateRoot`, `additionalData`; block data includes fixed-size shares and intermediate state roots/traces | high | structure required for proofs |
| §4.4-§4.5 / PDF p10-p12 | transition fraud proof | verifier checks Merkle-authenticated shares, parses a period, and recomputes state transition from pre-root to post-root using witnesses | high | state validity mechanism |
| §5.1 / PDF p12-p13 | strawman DAS | 1D RS encoding plus sampling; issue is invalidly generated extended data needs O(n) fraud proof | high | why 2D matters |
| §5.2-§5.5 / PDF p13-p18 | 2D RS DAS | build 2k x 2k matrix, row/column roots, random sampling, selective disclosure model, codec fraud proofs | high | DAS mechanism |
| §5.6-§5.7 / PDF p18-p25 | security analysis | minimum unavailable shares `(k+1)^2`; single/multi-client detection probability; recovery threshold; standard vs enhanced model | high | formal assurance and limits |
| §6 / PDF p25-p28 | implementation/evaluation | Go implementation, object size/time complexity, 250 KB / 1 MB benchmark tables | high | empirical support |
| §7 / PDF p28-p29 | discussion | succinct proofs can replace some fraud proofs but not availability proofs; locally-decodable-code alternative | medium-high | bridge to ZK/validity-proof future |
| §8-§9 / PDF p29-p30 | related/conclusion | Bitcoin alerts, prior fraud proof discussions, erasure-code storage; summary assumptions | medium-high | scope and prior work |
| Appendix A-B / PDF p33-p34 | double-tree design and index computation | alternative txRoot/traceRoot design lacking DA support; details for codec proof index calculation | medium | implementation detail |

## 一句话贡献

本文提出一个让 light clients 在 dishonest-majority consensus 下接近 full-node 安全性的 fraud proof + data availability proof 组合: 状态转换错误用 execution trace 和 sparse Merkle witnesses 做小型 fraud proof，数据隐藏/错误编码用 2D Reed-Solomon sampling 与 codec fraud proof 处理，从而支撑更大区块和 sharded blockchain 的轻客户端安全。

## 核心精读笔记

### 为什么 light clients 的 honest-majority 假设不够

传统 SPV/light clients 只下载 block headers，不验证完整交易和状态转换，因此默认“共识算法偏好的链只包含有效块”。论文指出在 Bitcoin/Ethereum 当前 full nodes 仍存在时，dishonest majority 主要能 censor/reorder/reverse；但如果绝大多数用户都变成 light clients，恶意多数 block producers 还可以构造包含无效状态转换的区块，light clients 无法本地发现。证据锚点: Abstract, §1 PDF p2-p3。

本文目标是降低 on-chain capacity vs security trade-off: 允许 full nodes 对无效块生成 fraud proofs，light clients 验证后拒绝块；同时用 data availability proofs 确保生成 fraud proofs 所需的 block data 已经发布。证据锚点: §1 PDF p3。

### 威胁模型与最小信任条件

论文明确不依赖 consensus-participating nodes 的 honest majority。Block headers 可能由 adversarial actors 创建并可能无效。Full nodes 也可能不转发信息或转发无效块，但系统假设至少有一个 honest full node 在线、愿意生成并传播 fraud proofs、且没有被 eclipse。每个 light client 至少连接到一个 honest full node。网络有最大延迟 `delta`。对 data availability proofs，还需要足够多 honest light clients 共同采样，使 missing data 可以被重构。证据锚点: §3.3-§3.4 PDF p7-p8。

这组假设比“多数共识诚实”弱，但不是无信任: 如果所有 full nodes 都被 eclipse，或者 honest light clients 数量不足以覆盖样本空间，soundness/agreement 会下降。证据锚点: §5.6-§5.7 PDF p18-p25。

### Fraud proof 需要为区块结构提前设计

为了让 fraud proof 小于 O(n) block size，区块头不能只是 transaction Merkle root。本文的 header 包含:

- `prevHash_i`: previous block header hash。
- `dataRoot_i`: block data Merkle root，data 不只包含 transactions，还包含 intermediate state roots。
- `dataLength_i`: data root leaves 数量。
- `stateRoot_i`: state sparse Merkle tree root。
- `additionalData_i`: PoW nonce / difficulty 等网络特定数据。

Block data 被切成 fixed-size shares；每个 share 的首字节指示其中第一笔 transaction 的起始位置，便于不下载完整块时解析消息边界。协议还定义 period criterion，要求每隔固定数量的 transactions / bytes / gas 插入 intermediate state root。证据锚点: §4.1-§4.3 PDF p8-p11。

### 状态转换 fraud proof 的核心

论文把区块执行抽象为 `transition(S,t) -> S' or err`，并进一步定义 `rootTransition(stateRoot,t,w) -> stateRoot' or err`，其中 witness `w` 是交易读写 state entries 的 sparse Merkle proofs。这样 verifier 不需要全状态，只需前后状态根、相关交易、witnesses 和 dataRoot 下的 Merkle proofs。证据锚点: §3.2, §4.2 PDF p6, p8-p10。

`VerifyTransitionFraudProof` 做四类检查:

1. light client 已保存对应 block header。
2. fraud proof 中每个 share 都由 `dataRoot_i` 的 Merkle proof 认证。
3. `parseShares` 和 `parsePeriod` 能得到 pre-state trace、post-state trace 和 period 内 transactions。
4. 用 witnesses 逐笔运行 `rootTransition`，结果必须与 claimed post-state root 不一致，才接受 fraud proof。

一旦 proof valid，light client 永久拒绝该 block header。证据锚点: §4.4 PDF p10-p12。

### 为什么 fraud proofs 必须和 data availability 绑定

如果 malicious block producer 只广播 header、隐藏 block data，那么 honest full nodes 无法重算 dataRoot/state transition，也就无法生成 fraud proof。生产者甚至可以很久后释放包含无效交易的数据，造成未来区块回滚。因此 light clients 必须先有把握: `dataRoot_i` 对应的数据确实对网络可用。证据锚点: §5 opening PDF p11-p12。

这是本文对 Nahida 很重要的结构信号: fraud proof 不是 DAS 的替代品，DAS 也不是交易有效性证明。它们互补: fraud proofs 证明“这个已发布数据导致的状态转换非法”，DAS 证明“这个数据已经发布且足以让 honest full nodes 生成 fraud proof”。证据锚点: Abstract, §5, §9。

### 1D Reed-Solomon strawman 失败点

直觉方案是把 k 个 shares RS 编码为 2k 个 shares，并让 light clients 随机抽样。如果 producer 隐藏超过 50% shares，客户端快速采到 unavailable share 的概率很高。但 adversarial producer 可能错误生成 extended data，使得即使超过 50% shares 可见，原数据也无法恢复。对普通 1D RS，证明 extended data 错误需要客户端下载/重编码 O(n) 数据。证据锚点: §5.1 PDF p12-p13。

因此本文使用 multidimensional encoding，让错误编码 fraud proof 只需要某个 row/column，而不是整个 block。论文聚焦 2D Reed-Solomon，proof size 降到 O(sqrt(n)) 量级。证据锚点: §5.1 PDF p13。

### 2D Reed-Solomon 编码与 dataRoot

构造过程:

1. 原始 block data 切成 shares，排成 k x k matrix。
2. 对每行、每列做 Reed-Solomon encoding，并对垂直扩展部分再次横向编码，得到 2k x 2k matrix。
3. 对每个 row 和 column 分别建 Merkle tree，得到 `rowRoot` 和 `columnRoot`。
4. 对所有 row/column roots 再建 Merkle tree，得到 `dataRoot_i`。

Light clients 至少下载所有 row/column roots 并检查它们重建出的 root 等于 block header 的 dataRoot。只下载单一 dataRoot 的 super-light clients 可以存在，但无法获得完整 data availability assurance。证据锚点: §5.2 PDF p13-p15。

### 随机抽样与网络恢复

Light client 收到 header 和 row/column roots 后，随机选择若干 unique coordinates，向连接的 full nodes 请求 shares 和 Merkle proofs；验证后把收到的 shares gossip 给 full nodes。若所有 samples 都收到，且在 `2 * delta` 内没有收到 erasure-code fraud proof，则接受该 block available。证据锚点: §5.3 PDF p15-p16。

关键社会性假设是“很多 light clients 的样本合在一起”足以让 full nodes 恢复全矩阵。如果只有单个 light client 采样，它只能给自己高概率检测 unavailable shares，不能保证网络整体恢复数据。证据锚点: §5.6 PDF p18-p24。

### Selective share disclosure 是 DAS 的现实网络问题

如果 producer 能根据 client 身份选择性释放 shares，它可以先满足前 `(k+1)^2` 个 sample requests，使这些 clients 接受 block available，然后在完整矩阵可恢复前停止释放，破坏 soundness/agreement。论文因此区分:

- Standard model: requests 可链接到 client，收到顺序可预测。
- Enhanced model: 不同 sample requests 不能链接到同一 client，并且被网络接收顺序相对其他请求均匀随机；论文举 mix network 作为例子。

Enhanced model 通过隐藏“哪些请求属于同一客户端”来削弱 selective release。证据锚点: §5.4, §5.7 PDF p16, p23-p25。

### Codec fraud proof: 错误 erasure coding 的反驳

如果 full node 收集足够 shares 恢复某行或某列，并发现恢复结果不匹配该 row/column root，它可以广播 `VerifyCodecFraudProof`。Verifier 检查:

1. axis root 本身由 dataRoot 认证。
2. proof 中 shares 位于同一行或列相关位置，并且每个 share 有 Merkle proof。
3. 用这些 shares recover 出完整 row/column 后，recovered root 不等于 axisRoot。

如果 codec fraud proof valid，light client 永久拒绝该 block header。这个机制让“extended data 错误生成”不再需要 O(n) proof。证据锚点: §5.5 PDF p16-p18, Appendix B PDF p34。

### 概率与安全结论

Theorem 1: 在 2k x 2k matrix 中，要让某个 share unrecoverable，至少需要让 k+1 个 rows 或 columns 各自有 k+1 个 unavailable shares；最少 unavailable shares 数量是 `(k+1)^2`。证据锚点: §5.6 PDF p17-p18。

Theorem 2: 单个 light client 随机采样 s 个 shares 时，采到至少一个 unavailable share 的概率为:

```text
p1(X >= 1) = 1 - prod_{i=0}^{s-1}(1 - (k+1)^2 / (4k^2 - i))
```

论文给出直觉: 约 3 次采样有约 60% 概率检测到 incomplete block；15 次采样超过 99%；当 k 很大时近似 `1 - (3/4)^s`。证据锚点: Theorem 2, Figure 6, PDF p18-p20。

Theorem 3 / Corollary 1: 多个 light clients collectively sampling 可以估计有多少 clients 检测到 unavailable share，以及需要多少 clients 才能采到足够 distinct shares 恢复矩阵。Table 1 给出例子: `k=32, s=20` 时约 280 个 light clients 可让 `pe(Z >= gamma) > 0.99`; `k=64, s=20` 时约 1129 个 clients。证据锚点: Figure 8-9, Table 1 PDF p20-p23。

在 standard model 下，producer 可以利用 selective share disclosure 让最早 c 个 clients 失败；在 enhanced model 下，每个 client 均匀承受 denied requests，拒绝概率由 Equation 12 描述。证据锚点: Corollary 2-3 PDF p23-p25。

### 实现与评估

论文实现了 data availability proof scheme 和 state transition fraud proof prototype，总计 2,683 行 Go，并开放为三组库。实验在 Intel Core i5 1.3GHz / 16GB RAM laptop 上运行，hash 使用 SHA-256。证据锚点: §6 PDF p25。

复杂度与对象尺寸:

- State fraud proof: 空间 `O(p + p log(d) + w log(s) + w)`，verification roughly independent of full block size when period size fixed。
- Availability fraud proof: 空间 `O(sqrt(d) + sqrt(d) log(sqrt(d)))`。
- Single sample response: `O(shareSize + log(d))`。
- Block header with axis roots: `O(sqrt(d))`。

Table 4 例子:

| Object | 250 KB block | 1 MB block |
| --- | --- | --- |
| State fraud proof | 14,090 bytes | 14,410 bytes |
| Availability fraud proof | 5,120 bytes | 12,288 bytes |
| Single sample response | 320 bytes | 368 bytes |
| Block header with axis roots | 2,176 bytes | 4,224 bytes |
| Block header excluding axis roots | 128 bytes | 128 bytes |

Table 5 例子:

| Action | 250 KB block | 1 MB block |
| --- | --- | --- |
| Generate state fraud proof | 289.78 ms | 981.88 ms |
| Verify state fraud proof | 1.50 ms | 1.50 ms |
| Generate availability fraud proof | 7.96 ms | 50.88 ms |
| Verify availability fraud proof | 0.05 ms | 0.19 ms |
| Generate/verify single sample response | < 0.00001 ms | < 0.00001 ms |

作者指出 state proof generation 的高常数来自 sparse Merkle tree 每次 update 需要 256 hash operations，可用 SIMD SHA-256、subtree parallelization 或 Patricia-like tree 改善。Availability fraud proof generation 使用 O(k^2) RS library，可用 FFT-based O(k log k) 编码/解码改善。证据锚点: §6.1-§6.2 PDF p25-p28。

### Succinct proofs 能替代什么，不能替代什么

§7.1 讨论 zk-SNARKs / zk-STARKs 等 succinct proofs。它们未来可以证明 erasure code 正确生成，从而不需要 codec fraud proofs；也可以证明 state transition 函数正确，从而降低或移除 fraud proof 需求。但作者强调 succinct proofs 不能移除 availability proofs: 如果数据不可用，honest full nodes 仍无法构造最新 state 或为账户生成 witnesses，某些账户可能永久不可访问。证据锚点: §7.1 PDF p28-p29。

这说明在 Nahida 中应把 fraud proofs、validity proofs 和 data availability proofs 分开建模: validity/succinct proofs 可替代“执行是否正确”的反驳过程，但不能替代“数据是否可获得”的问题。

## 结构化摘要

| 维度 | 内容 |
| --- | --- |
| 解决的问题 | 让 light clients 在不下载完整区块、不假设 consensus majority honest 的情况下，检测 invalid blocks，并确认生成 fraud proofs 所需数据可用。 |
| 核心方法 | 状态转换 fraud proofs + 2D Reed-Solomon data availability sampling + codec fraud proofs + light-client/full-node gossip recovery。 |
| 关键创新 | 把 fraud proof 与 DA proof 组合起来；用 execution traces 和 sparse Merkle witnesses 压缩状态转换 fraud proof；用 2D RS 将错误编码证明限制到 row/column。 |
| 关键假设 | 至少一个 honest full node；每个 light client 连到 honest full node；有足够 honest light clients 采样和 gossip；bounded network delay；enhanced model 需要匿名/随机化 sample request。 |
| 证据 | 定义 soundness/agreement；Theorem 1-4/Corollaries；Go prototype；对象大小和验证时间表。 |
| 限制 | 依赖网络/gossip/anti-eclipse；selective share disclosure 需要增强网络模型；2D RS 有 axis roots/header overhead；state witness 和 trace 改动要求区块结构配合。 |

## Evidence Table

| Claim / finding | Evidence anchor | Confidence | Note |
| --- | --- | --- | --- |
| Fraud proofs alone cannot secure light clients if block data is withheld. | §5 opening PDF p11-p12 | high | DA 是 fraud proof 的前置条件。 |
| Efficient transition fraud proofs require fraud-proof-friendly block data, intermediate roots, and sparse Merkle witnesses. | §4.1-§4.4 PDF p8-p12 | high | 不是任意传统 block format 都能直接支持。 |
| 2D RS DAS 的 unrecoverability 最少需要 `(k+1)^2` unavailable shares。 | Theorem 1 PDF p17-p18 | high | 这支撑 random sampling probability。 |
| 15 samples gives >99% detection probability in the paper's k=32/k=256 examples. | Figure 6 and nearby prose PDF p19-p20 | high | 单客户端 detection，不等于网络恢复。 |
| Network recovery requires many light clients collectively sampling enough distinct shares. | Corollary 1, Table 1 PDF p22-p23 | high | 参数与 matrix size/sample count 强相关。 |
| Enhanced model mitigates selective share disclosure by unlinking sample requests. | §5.4, Corollary 3 PDF p16, p23-p25 | medium-high | 需要 mix-net-like assumption；不是免费获得。 |
| Validity/succinct proofs do not remove the need for availability proofs. | §7.1 PDF p28-p29 | high | 对 rollups/validity proof architecture 很重要。 |

## Knowledge Handoff

### Target Knowledge Nodes

| Target | Handling | Delta |
| --- | --- | --- |
| [[data-availability-and-light-clients|Data availability and light clients]] | update direction | 补入 fraud proofs/data availability proofs as light-client security route。 |
| [[data-availability-sampling|Data availability sampling]] | update problem | 补入 2D Reed-Solomon DAS、codec fraud proofs、selective disclosure boundary。 |
| [[fraud-proofs|Fraud proofs]] | create seed knowledge node | 将 fraud proofs 作为可复用机制解释，而不是论文同名页。 |
| [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]] | update bridge | 本文明确 fraud/DA proofs 是 sharding 的安全前提之一。 |

### Bridge Candidates

| Bridge | Endpoint paths | Reason | Status |
| --- | --- | --- | --- |
| Fraud proofs -> data availability sampling | `blockchain-systems/data-availability-and-light-clients/fraud-proofs`; `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | fraud proofs need data to be available; DAS needs codec fraud proofs or validity proofs to reject malformed erasure coding | create active_seed |
| Data availability -> sharded ledgers | existing bridge | paper states sharded systems require fraud proofs because no single node validates every shard | update existing active_seed |

### Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Handling |
| --- | --- | --- | --- |
| Research field/domain | blockchain-systems | Abstract, §1 | existing domain |
| Direction | data-availability-and-light-clients | Abstract, §5 | existing direction |
| Research problem | light-client security under dishonest-majority consensus | Abstract, §1, §3 | section/source extension |
| Method family | fraud proofs; data availability sampling; erasure-coded availability proofs | §4-§5 | create/update method nodes |
| Foundation concepts | Merkle trees, sparse Merkle trees, Reed-Solomon codes, light clients, full nodes | §2 | mention as foundations; do not create from this source alone |
| Application/evaluation context | sharding, larger blocks, SPV/light clients | Abstract, §1, §9 | bridge/update parent notes |
| Source instance | this arXiv preprint and Go prototypes | §6 footnote | keep in source note |

### Retrieval Optimization

- 未来查询“fraud proofs 为什么需要 data availability”应优先读 [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]]，再读本 source。
- 未来查询“DAS 早期 2D Reed-Solomon 方案怎么工作”应优先读 [[data-availability-sampling|Data availability sampling]] 的方法路线和 source extension。
- 未来查询“validity proofs 能不能替代 DAS”应使用本 source 的 §7.1 边界: 能替代部分 fraud proofs，但不能替代 availability proof。

## Foundation Candidate Judgment

| Candidate | Judgment | Reason |
| --- | --- | --- |
| Fraud proofs | knowledge_node_seed | 可复用 light-client / optimistic verification 机制，当前 vault 已有缺口，且本 paper 是 central source seed。 |
| Data availability proofs | knowledge_section under DAS | 与 DAS 高度重合，先放入 DAS/fraud-proof bridge，不单独拆节点。 |
| 2D Reed-Solomon DAS | source_extension / method row | 具体构造来自本 paper，后续有更多 RS/celestia/Celestia specs 再判断是否拆 method child。 |
| Codec fraud proofs | source_extension under DAS | 是本 scheme 的 sub-mechanism。 |
| Sparse Merkle state witnesses | foundation_gap / background | 不是本文发明，当前 source 只作为应用 evidence。 |
| Succinct validity proofs | review/bridge candidate | 本文只讨论 future alternative，不足以更新 ZKP foundation。 |

## Review Items

| Item | Reason | Suggested follow-up |
| --- | --- | --- |
| `fraud-proofs-foundation-thin` | 当前只有本 paper seed，尚缺 optimistic rollup / Ethereum fraud proof / Plasma / Celestia specs 等 source。 | 后续用 `nahida-update` 或 `nahida-research-search` 补 foundation pack。 |
| `selective-share-disclosure-assumption` | Enhanced model 需要匿名/随机 sample requests，工程部署复杂。 | 后续比较 Celestia/Nitro/Ethereum DA 实践如何处理 peer sampling。 |
| `validity-proof-boundary` | §7.1 明确 ZK validity proofs 不能替代 availability proofs。 | 后续吸收 rollup / validity proof sources 时建立 bridge。 |
