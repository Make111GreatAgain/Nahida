---
id: "sha256-b04fe9944676"
title: "Clay Codes: Moulding MDS Codes to Yield an MSR Code"
type: "source"
source_kind: "paper"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
hierarchy_level: "source"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "Myna Vajha"
  - "Vinayak Ramkumar"
  - "Bhagyashree Puranik"
  - "Ganesh Kini"
  - "Elita Lobo"
  - "Birenjith Sasidharan"
  - "P. Vijay Kumar"
  - "Alexander Barg"
  - "Min Ye"
  - "Srinivasan Narayanamurthy"
  - "Syed Hussain"
  - "Siddhartha Nandi"
year: 2018
venue: "16th USENIX Conference on File and Storage Technologies (FAST 2018)"
publisher: "USENIX"
source_refs:
  - "sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a"
  - "usenix:fast18-vajha"
  - "isbn:978-1-931971-42-3"
canonical_url: "https://www.usenix.org/conference/fast18/presentation/vajha"
local_pdf_path: "~/Desktop/paper/Clay.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/clay-b04fe9944676-pages.txt"
pages: 16
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
primary_domain: "distributed-systems"
primary_direction: "data-management-and-storage"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/erasure-coded-storage"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "erasure-coded-storage"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage"
topic_ids:
  - "erasure-coded-storage"
  - "msr-codes"
  - "mds-codes"
  - "vector-erasure-codes"
  - "ceph-erasure-coding"
  - "storage-repair-optimization"
domains:
  - "distributed-systems"
topics:
  - "erasure-coded-storage"
  - "msr-codes"
  - "mds-codes"
  - "vector-erasure-codes"
  - "ceph-erasure-coding"
aliases:
  - "Clay Codes"
  - "Coupled-Layer codes"
  - "Clay MSR codes"
tags:
  - "nahida/source"
  - "paper"
  - "erasure-coded-storage"
classification_status: "corrected_absorbed"
classification_confidence: "high"
knowledge_node_refs:
  - "[[04_Knowledge/distributed-systems/data-management-and-storage|Data management and storage]]"
  - "[[04_Knowledge/distributed-systems/data-management-and-storage/erasure-coded-storage|Erasure-coded storage]]"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0102"
run_id: "nahida-paper-intake-20260623-clay-codes"
managed_by: "nahida"
confidence: "high"
trust_tier: "primary"
---

# Clay Codes: Moulding MDS Codes to Yield an MSR Code

## Paper Identity

| 字段 | 内容 |
| --- | --- |
| 论文 | Clay Codes: Moulding MDS Codes to Yield an MSR Code |
| 作者 | Myna Vajha; Vinayak Ramkumar; Bhagyashree Puranik; Ganesh Kini; Elita Lobo; Birenjith Sasidharan; P. Vijay Kumar; Alexander Barg; Min Ye; Srinivasan Narayanamurthy; Syed Hussain; Siddhartha Nandi |
| 会议 | 16th USENIX Conference on File and Storage Technologies (FAST 2018) |
| 年份 | 2018 |
| URL | https://www.usenix.org/conference/fast18/presentation/vajha |
| 本地 PDF | `~/Desktop/paper/Clay.pdf` |
| 校验和 | `sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a` |

## Reading Coverage

| 范围 | 覆盖 |
| --- | --- |
| PDF extraction | `pypdf` text extraction usable; 16 pages including USENIX cover page and appendix. |
| 主要章节 | Abstract, §1 Introduction, §2 Background, §3 Construction, §4 Ceph and Vector MDS Codes, §5 Experiments, §6 Multiple Failures, §7 Conclusion, Appendix A. |
| 元数据修正 | 队列标题原为 USENIX 会议信息 `February 12-15, 2018...`；真实标题来自首页和正文第 2 页。 |
| safe_for_absorption | yes. 论文的目标、构造、系统实现、实验和限制均已覆盖。 |

## One-Sentence Takeaway

Clay codes 把多个普通 MDS codeword 叠成 layers，再用 pairwise coupling 在层间变换，从而把可工程实现的 MDS 码 mould 成 MSR code，并通过 Ceph vector-code/sub-chunk 支持把理论上的低 repair bandwidth 转成真实存储系统里的 repair traffic、disk read 和 repair time 降低。

## Cold-Start Hierarchy Discovery

| Facet | Result |
| --- | --- |
| Research field/domain | distributed systems |
| Direction | data management and storage |
| Research problem | erasure-coded storage 中的 node repair bandwidth / disk I/O / sub-packetization tradeoff |
| Foundation concepts | erasure coding, Reed-Solomon/MDS codes, vector codes, MSR codes, sub-packetization, distributed object storage |
| Method family | repair-efficient erasure codes; coupled-layer MSR code construction |
| Application/evaluation context | Ceph distributed object storage; single-node and multiple-node repair; EC2 cluster; repair network traffic, disk read, repair time, degraded I/O |
| Source instance | Clay codes and Ceph vector-code support |

## Structured Summary

### Problem

大规模数据中心里节点和磁盘故障频繁，复制虽然修复简单，但存储开销高。Reed-Solomon 等 MDS erasure codes 能用较低冗余提供相同容错能力，但传统 MDS repair 通常需要从大量 surviving nodes 读取和传输比丢失数据更多的数据，导致 repair bandwidth、repair time 和前台业务带宽被占用。

Minimum Storage Regenerating (MSR) codes 在理论上能同时保持 MDS 的最小存储开销和最小 repair bandwidth，但已有 MSR 构造在工程上常有约束：参数范围窄、只优化 data node、sub-packetization 过高、finite field 或计算复杂、只支持少量故障模式，或没有接入真实分布式存储系统。

### Key Idea

Clay 是 Coupled-Layer 的缩写。它从任意一个 scalar MDS code 出发，堆叠多个 MDS codeword 形成 uncoupled code，再对不同 layer 中成对的 symbols 做 pairwise forward/reverse transform。这个 pairwise coupling 让 code 保持 MDS 解码能力，同时在 repair 某个 node 时只需要从 helper nodes 读取部分 layers/sub-chunks，从而达到 MSR repair bandwidth。

这种构造把 Ye-Barg 理论构造转成更容易实现的 coupled-layer 视角：编码、解码和 repair 可以被拆成两个基本操作，分别是底层 scalar MDS decoding 和成对 symbols 的线性变换。

### System Contribution

Ceph 当时只支持 scalar erasure codes，即以 chunk 粒度进行 repair。Clay 属于 vector code，需要 sub-chunk 粒度读取。论文修改 Ceph，使其能够支持任意 vector code 的 sub-chunk repair；这部分贡献已经进入 Ceph master codebase。Clay code 本身实现为 Ceph jerasure plugin 里的 `cl_msr` technique，支持选择 `(n,k,d)` 参数和底层 Vandermonde-RS 或 Cauchy-original MDS code。

### Evidence

论文在 Amazon EC2 上运行 Ceph Jewel 10.2.2，部署 26 个节点：1 个 MON，25 个 OSD，每个节点挂 500GB SSD。评估 C1-C6 六组 Clay 参数，并与相同 `(n,k)` 参数的 RS code 比较。对于 `(20,16,19)`、storage overhead 1.25x 的 Clay code，在固定 64MB 对象 workload 下，论文报告 repair network traffic 降低约 2.9x、disk read 降低约 3.4x、repair time 降低约 3x。

## Detailed Outline

| Section | Pages | Role |
| --- | --- | --- |
| Abstract / §1 Introduction | p2-p3 | 提出问题：MDS 低存储开销但 repair 成本高；MSR 理论强但实践不足；Clay 试图把 MSR 带入 Ceph。 |
| §2 Background and Preliminaries | p3-p6 | 定义 scalar/vector codes、MDS、node repair、MSR codes、sub-packetization 和 desired attributes；比较 RS、PM-RBT、Butterfly、HashTag、Clay。 |
| §2.2 Refinements over Ye-Barg Code | p5-p6 | 说明 Clay 对 Ye-Barg 的工程化改写：coupled-layer 视角、任意 scalar MDS code、multi-failure repair algorithm。 |
| §3 Construction of the Clay Code | p6-p9 | 用 `(4,2)` RS 示例解释 uncoupled code、vertex pairing、PFT/PRT、encoding、repair、decoding、intersection score、general parameters 和 shortening。 |
| §4 Ceph and Vector MDS Codes | p9-p10 | 介绍 Ceph OSD/PG/CRUSH；说明 sub-chunking/interleaving、U-buffer、Jerasure/GF-Complete、repair vs decode selection 和 fractional read。 |
| §5 Experiments and Results | p10-p13 | 单节点 repair 的网络流量、disk read、I/O performance、repair time、encoding time 实验。 |
| §6 Handling Failure of Multiple Nodes | p13 | 多节点 failure pattern 的理论和实验；C4-C6 多 PG、多故障评估。 |
| §7 Conclusions | p13 | 总结 Clay 的理论最优属性和 Ceph 实践收益。 |
| Appendix A | p16 | 给出多节点 repairable failure patterns、repair bandwidth 计算和 generic repair algorithm。 |

## Technical Content

### Scalar Codes, Vector Codes And Sub-Packetization

论文先把 erasure code 分为 scalar 和 vector。Scalar code 每次从 `k` 个 data chunks 取一个 byte 线性组合得到 parity bytes；RS code 可视为 `alpha = 1` 的 scalar code。Vector code 每次处理 `alpha` 个 bytes 的 ordered collection，即 superbyte；`alpha` 被称为 sub-packetization level。

Vector code 的 repair 可以只访问 superbyte 内部分 bytes，因此有机会减少网络传输。为了避免 memory access 随机化，论文使用 interleaving，让不同 codeword 中对应位置的 bytes 连续存放，形成 sub-chunks。

### MDS And MSR

MDS code 的性质是任意 `k` 个 nodes/chunks 可以重建数据，因此在给定容错水平下存储开销最小。MSR code 是 vector MDS code 的子类，在保持最小存储开销的同时最小化 repair bandwidth。对于 `(n,k,d)` MSR code，repair 一个含 `alpha` bytes 的 failed node 时，从 `d` 个 helper nodes 各下载 `beta = alpha / (d-k+1)` bytes，总 repair bandwidth 为 `d beta`。

论文强调 MSR code 的实践属性不只看 repair bandwidth，还包括：

| 属性 | 含义 |
| --- | --- |
| all-node optimal repair | data node 和 parity node 都能以低 repair bandwidth 修复。 |
| disk read optimal | helper node 从磁盘读取的数据量等于实际传输量。 |
| low sub-packetization | `alpha` 不应过高，否则实现和 I/O locality 会受影响。 |
| low finite-field size | field size 不应让计算复杂度过高。 |

### Coupled-Layer Construction

Clay 从一个 scalar MDS code 出发，把多个 codewords 堆叠成 `alpha` 个 layers，得到 uncoupled code `U`。每个 node 对应 data cube 的一个 column，每个 column 内有 `alpha` 个 bytes。随后，Clay 根据 node 坐标 `(x,y)` 和 layer index `z` 进行 vertex pairing：红色 vertices 不配对，其余 vertices 在同一 `y-section` 中与 companion vertex `p*` 成对。

对于未配对 vertex，`C(p) = U(p)`。对于成对 vertices，Clay 使用 pairwise forward transform:

```text
[ C(p)  ]     [1 gamma]^-1 [ U(p)  ]
[ C*(p) ]  =  [gamma 1]   [ U*(p) ]
```

反向则使用 pairwise reverse transform:

```text
[ U(p)  ]     [1 gamma] [ C(p)  ]
[ U*(p) ]  =  [gamma 1] [ C*(p) ]
```

只要 `gamma != 0` 且 `gamma^2 != 1`，`{U(p), U*(p), C(p), C*(p)}` 中任意两个 bytes 可以由其余两个恢复。编码流程因此变成：先把 data 放到 coupled code 的 data nodes，做 PRT 得到 uncoupled data，按 layer 对 uncoupled code 做 scalar MDS encode，再做 PFT 得到 coupled code 的 parity nodes。

### Repair And Decoding

Repair savings 来自只选择与 failed node 红点相交的 layers。以 `(4,2)` 示例为例，repair 一个 failed column 时，helper nodes 只需提供两个 layers 的 bytes，而不是四个 layers 全部 bytes。

Repair 的逻辑是：

1. 从 helper nodes 读取 repair layers 对应的 `C` bytes。
2. 通过 PRT 得到同层、同 `y-section` 中的 `U` bytes。
3. 在每个 layer 内调用底层 scalar MDS decoding 恢复 missing `U` bytes。
4. 用 PFT 性质恢复 failed node 中缺失的 `C` bytes。

Decoding 多个 erasures 时，论文引入 intersection score (IS)，即某 layer 中 erased bytes 同时落在红点上的数量。Decoding 按 IS 从低到高处理：IS=0 的 layer 可直接由已知 `C`/`U` 和 MDS decode 恢复；IS=1 需要使用已恢复低 IS layers 的信息，如此推进。

### General Parameters

Clay 可构造参数：

```text
n = q t
q = d - k + 1
alpha = q^t
beta = q^(t-1)
```

当 `q` 不整除 `n` 时，论文使用 shortening。例如 `(n=14,k=10,d=13)` 中 `q=4`，先构造 `n'=16,k'=12`，再把额外 systematic nodes 的 data bytes 设为 0，得到目标 `(14,10,13)` code。

### Ceph Vector-Code Support

Ceph 的 p-OSD 对 object 先切成 stripes，再按 erasure-code profile 编码。为了支持 vector code，论文让 stripe size `S` 可被 `k alpha` 整除，把每个 data chunk 进一步按 `alpha` 分成 sub-chunks。MSR repair 时，每个 helper node 只需要传 `beta` 个 sub-chunks。

主要实现点：

| 实现点 | 内容 |
| --- | --- |
| Jerasure/GF-Complete | 使用 Ceph 现有 Galois-field arithmetic 和 MDS code library。 |
| U-buffer | 为 uncoupled symbols `U` 增加额外 buffer，大小为 `nL = S n/k` bytes。 |
| pairwise transform functions | 用 `jerasure_matrix_dotprod()` 和 `galois_w08_region_multiply()` 实现 PFT/PRT 相关运算。 |
| `is_repair()` | 在 failure 时选择 bandwidth/disk-I/O efficient repair 或默认 decode。 |
| `minimum_to_repair()` | 选择 `d` 个 helper chunk indices，单故障时要求包含 failed node 所在 `y-section` 的 survivors。 |
| fractional read | 修改 `ECSubRead` 和 Filestore read，使 Ceph 能读 sub-chunk 而非整个 chunk。 |
| Ceph contribution | vector-code sub-chunk support 已进入 Ceph master；Clay plugin 当时尚未进入 master。 |

## Evaluation

### Setup

| 字段 | 内容 |
| --- | --- |
| Platform | Amazon EC2 `m4.xlarge`, 16GB RAM, 4 CPU cores |
| Storage | 每节点 500GB SSD volume |
| Ceph version | Ceph Jewel 10.2.2 |
| Cluster | 26 nodes: 1 MON + 25 OSD nodes |
| Failure domain | node / single OSD |
| Tools | nmon and NMONVisualizer |
| Metrics | repair network traffic, repair disk read, repair time, encoding time, normal/degraded I/O |

Workloads:

| Workload | Object sizes | Distribution | Stripe size |
| --- | --- | --- | --- |
| W1 | 64MB fixed | 8192 objects / 512GB total | 64MB |
| W2 | 64MB, 32MB, 1MB | 82.5%, 10%, 7.5%; total 448GB | 1MB |

Clay codes evaluated:

| Code | `(n,k,d)` | `alpha` | storage overhead | `beta/alpha` |
| --- | --- | --- | --- | --- |
| C1 | `(6,4,5)` | 8 | 1.5 | 0.5 |
| C2 | `(12,9,11)` | 81 | 1.33 | 0.33 |
| C3 | `(20,16,19)` | 1024 | 1.25 | 0.25 |
| C4 | `(14,10,11)` | 128 | 1.4 | 0.5 |
| C5 | `(14,10,12)` | 243 | 1.4 | 0.33 |
| C6 | `(14,10,13)` | 256 | 1.4 | 0.25 |

### Single-Node Repair

For C1, C2 and C3, the paper compares Clay against Ceph RS codes with the same `(n,k)` parameters.

| Metric | Main result |
| --- | --- |
| Network traffic | C1, C2, C3 reduce repair network traffic by about 25%, 52%, and 66% respectively; C3 reaches about 2.9x reduction vs RS. |
| Disk read | Under W1, C1, C2, C3 reduce disk read by about 37.5%, 59.3%, and 70.2%; C3 reaches about 3.4x reduction. |
| Repair time | C3 in single-PG setting reduces repair time by about 3x vs RS. |
| Normal I/O | Normal write/read/random-read performance is approximately same for Clay and RS. |
| Degraded I/O | During background repair, C3 Clay shows higher degraded write/read throughput than `(20,16)` RS; paper reports 106% write and 27% read improvement. |
| Encoding time | Clay encode computation is higher due to PFT/PRT multiplications, but total encoding time remains close because network and disk I/O dominate. |

The W2 workload reveals an important boundary: high `alpha` and small stripe/sub-chunk sizes can create fragmented reads. For C3 with `S=1MB`, helper reads may be 256 fragments of 64 bytes; SSD 4KB granularity means extra disk read, so disk-read optimality at the code level can be weakened by storage-device access granularity.

### Multiple PGs And Multiple Failures

The paper also evaluates 512 PGs and multiple-node failure patterns. In multiple-PG settings, Ceph's dynamic PG/OSD assignment can make a surviving OSD reassigned as replacement, effectively treating some cases as two failures and worsening network traffic performance.

For multiple erasures, Clay can provide savings for many repairable failure patterns, but not all. The appendix specifies repairability:

| Case | Repairable pattern |
| --- | --- |
| `d < n-1` | Can repair `e <= n-d` failures with savings if helper nodes can include all surviving nodes in every failed node's `y-section`; otherwise fallback decode. |
| `d = n-1` | Up to `q-1` failures in one `y-section` can be repaired with savings using all surviving nodes as helpers. |

If computed helper sub-chunks make repair more expensive than decoding, `is_repair()` returns false and the system falls back to decode.

## Evidence Table

| Claim | Evidence anchor | Confidence |
| --- | --- | --- |
| Clay codes are MSR codes built from coupled layers of an MDS code. | Abstract; §3 Construction; §7 Conclusion | high |
| Clay can use any scalar MDS code as building block, not only Vandermonde-RS. | §2.2 Refinements over Ye-Barg Code; §4.4 | high |
| Ceph needed vector-code/sub-chunk support before Clay could be practical. | §1; §4.2-§4.4 | high |
| Sub-chunk/fractional reads can reduce repair network traffic but may fragment disk reads under small stripe/sub-chunk sizes. | §4.2; §5.2 Disk Read | high |
| `(20,16,19)` Clay with 1.25x storage overhead reduces network traffic, disk read and repair time by about 2.9x, 3.4x and 3x versus RS in the evaluated setup. | Abstract; §5.2; §7 | high |
| Multiple-node repair savings depend on failure pattern, helper selection and whether repair beats decode. | §6; Appendix A | high |

## Limitations And Boundaries

| Limitation | Implication |
| --- | --- |
| Clay's benefits depend on workload and stripe/sub-chunk size | Small sub-chunks can turn theoretical disk-read optimality into fragmented reads. |
| Encode computation is higher than RS | For write-heavy systems, PFT/PRT overhead must be included, although paper argues repair is more frequent than writes. |
| Multiple failure savings are pattern-dependent | Not every multi-node failure should use repair; some should fall back to decode. |
| Clay plugin was not yet in Ceph master at publication time | Vector-code support had landed, but Clay deployment still depended on plugin integration. |
| Evaluation uses EC2 m4.xlarge, SSDs, Ceph Jewel 10.2.2 | Results should be revalidated for modern Ceph, NVMe/HDD mix, network speed, and production PG distributions. |

## Knowledge Handoff

### Primary node

Update [[04_Knowledge/distributed-systems/data-management-and-storage/erasure-coded-storage|Erasure-coded storage]].

Delta:

- Add Clay as a second direct source after Elastic Transformation.
- Strengthen the MSR/vector-code route with a practical Ceph implementation.
- Distinguish theory-level repair bandwidth optimality from storage-system granularity, sub-chunk layout and fragmented I/O.
- Replace the previous queue gap "Clay queued" with "Clay absorbed; still need RS/MDS/LRC/MSR foundation pack and production storage sources."

### Direction node

Update [[04_Knowledge/distributed-systems/data-management-and-storage|Data management and storage]] lightly:

- Add Clay as evidence for erasure-coded storage under data management and storage.
- Correct queue classification away from distributed transactions.
- Do not update storage engines directly; Ceph vector-code support is an erasure-coded storage system implementation signal, not a database storage-engine foundation.

### Bridge candidates

No durable new bridge is needed in this run. The existing queued bridge candidates from erasure-coded storage to data availability sampling or asynchronous reliable broadcast remain candidates because Clay is about storage repair, not data availability/security dissemination.

## Foundation Candidate Judgment

| Candidate | Judgment | Handling |
| --- | --- | --- |
| Erasure-coded storage | reusable problem/foundation-thin node | update existing knowledge node |
| MDS codes | foundation/method candidate | keep as method row and gap; needs more foundation sources |
| MSR codes | method-family candidate | add as method route; split later if more sources arrive |
| Clay codes | source instance / representative solution | keep in source note and source-extension rows |
| Ceph vector-code support | implementation contribution | source detail and evidence row; not standalone node yet |
| sub-packetization | evaluation/mechanism axis | query key and method discussion; split only with more sources |

## Retrieval Optimization

Future queries improved:

- “Clay codes 是什么，为什么比 RS repair 更省带宽?”
- “MSR code 在 Ceph 里怎么实现?”
- “vector erasure code / sub-chunk repair 为什么影响 disk read?”
- “纠删码存储里 repair bandwidth、sub-packetization、disk I/O 怎么权衡?”
- “Clay 和 Elastic Transformation 在纠删码修复优化里分别解决什么?”

Queries still needing more sources:

- “RS/MDS code 的基础定义和数学构造是什么?”
- “MSR/LRC/HashTag/Hitchhiker 的完整谱系怎么比较?”
- “现代 Ceph 生产版本是否仍保留这些 vector-code 接口和 Clay 实现?”

## Domain Dynamics Impact

Affected L1 domain: `distributed-systems`.

Decision: `unchanged`. Clay strengthens the existing erasure-coded storage child node but does not materially change domain-level research dynamics. A future dynamics refresh should wait for a cluster of storage-system sources, especially RS/MDS/LRC/MSR foundations, Ceph/OpenEC/HDFS implementations, and degraded-read/repair-scheduling papers.

## Review Items

- Queue title was noisy and has been corrected from the USENIX date/location header to the paper title.
- Classification should be corrected from `distributed-systems/data-management-and-storage/distributed-transactions` to `distributed-systems/data-management-and-storage/erasure-coded-storage`.
- DOI is unknown/not present in extracted PDF; use USENIX URL and checksum identity.
