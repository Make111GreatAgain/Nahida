---
id: "sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql"
title: "A Zero-Knowledge Version of vSQL"
type: "source"
source_type: "paper"
source_kind: "pdf"
source_subtype: "paper_local"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
safe_for_absorption: true
trust_tier: "primary"
source_identity:
  type: "pdf"
  key: "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
source_refs:
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "filename:vSQL_ZK.pdf"
representative_source_refs:
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
authors:
  - "Yupeng Zhang"
  - "Daniel Genkin"
  - "Jonathan Katz"
  - "Dimitrios Papadopoulos"
  - "Charalampos Papamanthou"
year: "2017"
doi: ""
arxiv_id: ""
canonical_url: ""
venue: "preprint / local PDF"
local_pdf: "~/Desktop/paper/vSQL_ZK.pdf"
pdf_sha256: "17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
extracted_text_path: "vault/02_Raw/pdf/extracted/vsql_zk-17844a65dcd5-pages.txt"
pages: 24
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems"
secondary_ontology_paths:
  - "verifiable-computation/verifiable-computation-systems"
  - "zero-knowledge-proofs/polynomial-commitments"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "function-independent-preprocessing"
  - "zk-vpd"
  - "verifiable-polynomial-delegation"
  - "homomorphic-commitment-sumcheck"
  - "cmt-over-commitments"
  - "modular-zksnarks"
topic_ids:
  - "function-independent-preprocessing"
  - "zk-vpd"
  - "verifiable-polynomial-delegation"
  - "sum-check-protocol"
query_keys:
  - "A Zero-Knowledge Version of vSQL"
  - "zk-vSQL"
  - "vSQL zero knowledge"
  - "zero-knowledge verifiable polynomial delegation"
  - "zk-VPD"
  - "function-independent preprocessing"
  - "CMT over homomorphic commitments"
  - "sum-check over homomorphic commitments"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The abstract states that vSQL is efficient but not zero-knowledge and that this paper adds a zero-knowledge version."
  - "Section 3 constructs a zero-knowledge verifiable polynomial-delegation protocol."
  - "Sections 4 and 5 run sum-check and CMT over homomorphic commitments."
  - "Section 6 gives a zero-knowledge argument with preprocessing that depends on input-size bounds rather than the specific circuit."
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
  - "nahida-knowledge-verifiable-computation-systems"
  - "nahida-knowledge-polynomial-commitments"
  - "nahida-knowledge-sum-check-protocol"
  - "nahida-knowledge-modular-zksnarks"
bridge_refs:
  - "nahida-bridge-modular-zksnarks-to-polynomial-commitments-and-sum-check"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
  - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments.md"
  - "vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md"
  - "vault/05_Bridges/modular-zksnarks-to-polynomial-commitments-and-sum-check.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0054"
queue_rank: 54
run_ids:
  - "nahida-knowledge-20260622-vsql-zk"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# A Zero-Knowledge Version of vSQL

## Paper Identity

| Field | Value |
| --- | --- |
| Title | A Zero-Knowledge Version of vSQL |
| Authors | Yupeng Zhang; Daniel Genkin; Jonathan Katz; Dimitrios Papadopoulos; Charalampos Papamanthou |
| Year | 2017 |
| Local PDF | `~/Desktop/paper/vSQL_ZK.pdf` |
| Source key | `sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44` |
| Pages | 24 |
| Extracted text | `vault/02_Raw/pdf/extracted/vsql_zk-17844a65dcd5-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260622-vsql-zk`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0054`
- Queue title correction: 队列标题包含作者名；本 source note 采用 PDF 首页标题 `A Zero-Knowledge Version of vSQL`。
- Primary classification correction: 队列中的 `proof-system-foundations` 过宽；本论文主要作为 proof-system / VC-system source extension，并对 [[polynomial-commitments|Polynomial commitments]]、[[sum-check-protocol|Sum-check protocol]] 和 [[modular-zksnarks|Modular zkSNARKs]] 形成桥接证据。

## 一句话贡献

这篇论文把 vSQL 的函数无关预处理 VC 路线改造成零知识 argument: 用 zero-knowledge verifiable polynomial delegation 隐藏多项式评估值，并把 sum-check/CMT 的消息放进加性同态承诺里，从而避免泄露 witness 和中间线值。

## 章节地图

| Section | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, 1 | 说明 vSQL 的优势是 circuit-independent preprocessing 与较少 cryptographic operations，但原系统不具备 zero-knowledge。 | 支撑 proof-system / VC-system problem setting。 |
| 2.1-2.3 | q-SDH、extended power knowledge-of-exponent、argument definitions、linearly homomorphic commitments、ZKeq/ZKprod。 | 记录安全假设与承诺上证明的依赖边界。 |
| 2.4 | Layered arithmetic circuit、wiring predicates、multilinear/polynomial notation。 | 连接 CMT/GKR-style delegated computation。 |
| 3 | Zero-knowledge verifiable polynomial delegation protocol。 | 作为 [[polynomial-commitments|Polynomial commitments]] 的 zk-VPD source extension。 |
| 4 | Sum-check over homomorphic commitments。 | 作为 [[sum-check-protocol|Sum-check protocol]] 的承诺化/ZK source extension。 |
| 5 | CMT over homomorphic commitments。 | 说明 CMT 中间 wire values 可被承诺隐藏。 |
| 6 | Zero-knowledge argument with function-independent preprocessing。 | 连接 proof systems 与 VC systems；说明预处理只依赖输入/见证长度上界而非具体电路。 |
| References | CMT/GKR, Pedersen, vSQL, QAP/SNARK, Geppetto, Pinocchio 等背景。 | 保留后续补 source 的线索，不直接作为已读事实吸收。 |

## 解决的问题

论文针对的是 vSQL 原始路线的一个硬缺口：

- 传统 preprocessing-based VC/SNARK 系统若针对具体电路预处理，换计算就要重新做昂贵预处理。
- 若预处理 universal circuit，则电路尺寸和 concrete overhead 会显著增大。
- vSQL 用 CMT protocol + verifiable polynomial delegation 支持 circuit-independent preprocessing，并把 cryptographic operations 降到与输入大小而不是乘法门数相关。
- 但原 vSQL 不隐藏 witness；sum-check/CMT 的多项式消息和中间线值也可能泄露 witness 相关信息。
- 因此本论文的目标不是重新发明 sum-check 或 KZG，而是把 vSQL-style VC argument 的关键组件改为零知识版本，并保持类似渐近性能。

## 核心方法

### Zero-knowledge VPD

Section 3 的 `zk-VPD` 把普通 VPD 的公开评估值改成对评估值的承诺：

- `CommitPoly` 承诺一个多变量多项式。
- `CommitValue` 不直接输出 `f(t)`，而是输出对 `f(t)` 的 hiding commitment 和 proof。
- `Ver` 只检查该 commitment 与多项式承诺、查询点和 proof 是否一致。
- 该构造依赖 pairings、q-SDH 和 `(d,l)-Extended Power Knowledge of Exponent` 类型假设。
- Theorem 1 给出 completeness、binding/extractability 和 zero-knowledge，并记录复杂度：`KeyGen` 随变量/degree setup 增长，`Ver` 为 `O(l)`，多项式承诺为常数个 group elements，evaluation proof 为 `O(l)` 个 group elements。

对知识库的吸收边界：这不是完整 PCS landscape 的新 foundation；它是 vSQL/PolyCom 前史中的 zero-knowledge VPD route，适合补进 [[polynomial-commitments|Polynomial commitments]] 的 source extension 和 modular zkSNARK bridge。

### Sum-check over homomorphic commitments

Section 4 先回顾 sum-check：prover 每轮发送一个 univariate polynomial，verifier 用 degree check、random challenge 和最终点值检查把指数规模求和降到低成本验证。

论文指出泄露点在于：这些每轮 polynomial coefficients 会暴露 `g` 的额外信息，作为 NP argument 的子协议时可能泄露 witness。

Construction 2 的修正是：

- prover 对每轮 `g_i` 的系数发送 commitments，而不是明文系数。
- verifier 利用 commitment 的线性同态性计算对 `g_i(0)+g_i(1)` 或 `g_i(r_i)` 的承诺。
- verifier 通过 `ZKeq` 检查两个 commitments 的 preimage 相等。
- final check 仍通过 commitment equality 完成。
- Theorem 3 说明在 extractable homomorphic commitments 和 `ZKeq` soundness 下，soundness 仍是 `d*l/|F|` 量级。
- Lemma 2 给出只用 `cp, com0, m, t0` 模拟 Step 1 视图的零知识逻辑。

这条路线应写入 [[sum-check-protocol|Sum-check protocol]]，但边界要清楚：承诺化 sum-check 本身仍不是 SNARK，也不自动提供 non-interactivity；它是给更大 argument/VC construction 使用的零知识子协议。

### CMT over homomorphic commitments

Section 5 将 CMT protocol 的 layer-by-layer circuit verification 放到 commitments 上：

- 原 CMT 用 multilinear extensions 和 sum-check，把第 `i` 层正确性规约到第 `i+1` 层。
- 直接运行会泄露 circuit intermediate values。
- Construction 3 中 prover 对 input wires、output claim、中间 `t1,t2,t3`、line polynomial `h` 等发送 commitments。
- verifier 用 `ZKprod` 检查乘法关系，用 `ZKeq` 检查承诺中的线性/点值关系。
- Theorem 5 给出对 layered arithmetic circuit 的 interactive argument，soundness 为 `O(d * log S / |F|)`。
- Lemma 3 证明 Steps 1-2 的 verifier 视图可在不知道输入 `x` 的情况下模拟。

重要边界：Construction 3 的最后会 reveal input 并直接检查；论文在 Section 5 明确指出这一步不能进入最终零知识构造，Section 6 用 zk-VPD 替换它。

### Function-independent preprocessing argument

Section 6 把两个零知识组件组合为最终 argument：

- preprocessing phase 只对输入大小参数 `n` 和电路大小上界 `t` 运行 `KeyGen(1^lambda, n, 1)`。
- proving key / verification key 不依赖具体 circuit wiring。
- prover 承诺输入层的 multilinear extension `V_d`。
- CMT-over-commitments 将电路正确性规约到对 `V_d` 的随机点评估。
- zk-VPD 证明 `V_d` 在随机点和 public input 子空间上的 committed evaluation 是正确的。
- `ZKeq` 把 CMT 给出的 committed value 与 zk-VPD 给出的 committed value 连接起来。

Theorem 6 结论：

- 对关系 `R = {(C,x;w): |C| <= t, inp(C) <= n, C(x;w)=1}` 给出 zero-knowledge argument system。
- prover time 为 `O(|C| * log(width(C)))`。
- 若 `C` 是 log-space uniform，verifier time 为 `O(|x| + d * polylog(|C|))`。
- 交互轮数为 `O(d log(width(C)))`。
- 若 circuit depth `d` 为 `polylog(|C|)`，构造是 succinct argument。

## 创新点

1. 把 vSQL 的 VPD 组件改为 zero-knowledge VPD，使 verifier 验证 committed evaluation 而不是明文 evaluation。
2. 把 sum-check 的 polynomial messages 放入同态承诺，并用 `ZKeq` 保留 round consistency。
3. 把 CMT 的 layer-reduction 消息放入承诺，并用 `ZKprod`/`ZKeq` 隐藏 intermediate wire values。
4. 用 zk-VPD 替换 CMT 最后 reveal input 的检查步骤，得到完整 zero-knowledge argument。
5. 保留 vSQL-style circuit-independent preprocessing 语义：setup 依赖输入/见证长度上界，不依赖待验证电路。

## 局限与外推边界

- 构造是交互式 argument；本 source note 不把它直接等同为普通 deployed zk-SNARK。
- preprocessing 仍是 trusted preprocessing；论文没有消除 setup trust。
- 安全性依赖 q-SDH 和 non-standard knowledge-of-exponent 型假设；这些假设不应被推广成所有 PCS/SNARK 的共同假设。
- 零知识化会带来额外 cryptographic operations；论文只说渐近性能与 vSQL 相同，并预期双方有轻微 overhead。
- 论文不是 benchmark paper；没有给出实现评估或真实 SQL workload 的新实验。
- PDF 没有提供 DOI/arXiv/venue 元数据；本轮未联网补外部身份。

## 层级候选分类

| Candidate | Decision | Reason |
| --- | --- | --- |
| [[proof-systems|Proof systems]] | primary | 论文核心产物是 zero-knowledge argument system 与其组件构造。 |
| [[verifiable-computation-systems|Verifiable computation systems]] | secondary | vSQL-style function-independent preprocessing 是 VC 系统问题，但本论文新增性是零知识化。 |
| [[polynomial-commitments|Polynomial commitments]] | source extension | `zk-VPD` 是 committed polynomial evaluation / delegation route。 |
| [[sum-check-protocol|Sum-check protocol]] | source extension | Construction 2 给出 sum-check over homomorphic commitments。 |
| [[modular-zksnarks|Modular zkSNARKs]] | bridge evidence | LegoSNARK 的 PolyCom/CP gadgets 依赖 zk-vSQL/VPD-style machinery；这篇补主源校准。 |
| `zk-vSQL` standalone node | reject for now | 当前只是单篇 paper/protocol label，先保留在 source note 和方法路线中。 |
| `function-independent preprocessing` standalone node | review later | 这是可复用问题，但当前已读 source 仍薄；先作为 proof-system/VC-system route。 |

## 知识交接

### 应更新的 Knowledge

- [[proof-systems|Proof systems]]: 增加 `function-independent preprocessing zero-knowledge arguments` source extension，保留它与 SNARK/VC 的边界。
- [[verifiable-computation-systems|Verifiable computation systems]]: 增加 vSQL-style circuit-independent preprocessing route 的零知识版本。
- [[polynomial-commitments|Polynomial commitments]]: 增加 `zk-VPD`/committed polynomial evaluation route；不要把它误归为 KZG child。
- [[sum-check-protocol|Sum-check protocol]]: 增加 homomorphic-commitment sum-check route。
- [[modular-zksnarks|Modular zkSNARKs]]: 增加 upstream evidence，说明 LegoSNARK/PolyCom 的部分前史来自 zk-vSQL/VPD-style polynomial delegation。

### 应刷新 Bridge

- 刷新 [[modular-zksnarks-to-polynomial-commitments-and-sum-check|Modular zkSNARKs -> polynomial commitments and sum-check]]，把 `Absorb zk-vSQL/PolyCom primary source` 从 review need 变成已补证据。

### 不应新建的 Knowledge

- 不新建 `vSQL` 或 `zk-vSQL` 知识节点；这是 source/protocol-instance label。
- 不新建 `zk-VPD` 子节点；目前主要由本 source 支撑，先作为 polynomial commitments 的 source extension。
- 不把 `CMT over commitments` 独立成节点；它是 CMT/sum-check/commitment 组合路线，先通过 source note 与 bridge 检索。

## 检索优化判断

| Query | Should hit | Why |
| --- | --- | --- |
| `zk-vSQL` | this source note; bridge | 论文 title/alias and LegoSNARK PolyCom bridge |
| `function-independent preprocessing` | this source note; [[verifiable-computation-systems|Verifiable computation systems]] | 核心 problem setting |
| `zero-knowledge verifiable polynomial delegation` | this source note; [[polynomial-commitments|Polynomial commitments]] | Section 3 contribution |
| `sum-check over commitments` | this source note; [[sum-check-protocol|Sum-check protocol]] | Section 4 contribution |
| `CMT over homomorphic commitments` | this source note; [[verifiable-computation-systems|Verifiable computation systems]] | Section 5 contribution |
| `PolyCom source` | this source note; [[modular-zksnarks-to-polynomial-commitments-and-sum-check|bridge]] | LegoSNARK bridge review need |

## Evidence Notes

| Evidence anchor | Observation | Absorption target |
| --- | --- | --- |
| Abstract | vSQL is efficient and avoids QAP-style heavy cryptographic operations, but lacks zero-knowledge; this work adds a zero-knowledge version. | [[proof-systems|Proof systems]] |
| §1 | vSQL preprocessing depends on an upper bound on input size, not the specific circuit; vSQL cryptographic operations are linear in input size, but original vSQL is not zero-knowledge. | [[verifiable-computation-systems|Verifiable computation systems]] |
| Theorem 1 / Construction 1 | `zk-VPD` commits to polynomial evaluations and proves correctness without revealing the value. | [[polynomial-commitments|Polynomial commitments]] |
| Construction 2 / Theorem 3 | Sum-check messages can be replaced by homomorphic commitments plus `ZKeq` while preserving soundness structure. | [[sum-check-protocol|Sum-check protocol]] |
| Construction 3 / Theorem 5 | CMT can run over homomorphic commitments, hiding internal wire values while keeping layer-reduction soundness. | [[verifiable-computation-systems|Verifiable computation systems]] |
| Theorem 6 | Final protocol is zero-knowledge and retains function-independent preprocessing; succinct if depth is polylogarithmic. | [[proof-systems|Proof systems]] |
| References and LegoSNARK source note | LegoSNARK later extracts PolyCom/CPpoly from zk-vSQL/VPD-style machinery. | [[modular-zksnarks-to-polynomial-commitments-and-sum-check|bridge]] |

## 处理日志

| Date | Run ID | Action | Reviewer |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-vsql-zk | Deep-read `vSQL_ZK.pdf`; created source note; queued absorption into Source + Knowledge + Bridge architecture. | codex |
