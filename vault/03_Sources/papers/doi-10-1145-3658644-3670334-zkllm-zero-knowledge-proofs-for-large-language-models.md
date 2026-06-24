---
id: "doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models"
title: "zkLLM: Zero Knowledge Proofs for Large Language Models"
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
  - "p1-p16 full extracted text"
  - "Appendix A theorem statements and long-version pointer"
  - "Appendix B implementation artifact pointer"
canonical_url: "https://doi.org/10.1145/3658644.3670334"
doi: "10.1145/3658644.3670334"
arxiv_id: "2404.16109"
venue: "ACM CCS 2024"
year: "2024"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "verifiable-inference"
  - "zkml"
  - "large-language-models"
  - "tensor-lookup-arguments"
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-inference"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-inference"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/proof-systems"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "zkml"
    - "proof-systems"
  topics:
    - "verifiable-inference"
    - "large-language-models"
    - "tensor-lookup-arguments"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zkml"
  - "verifiable-inference"
  - "large-language-models"
  - "lookup-arguments"
  - "sumcheck"
aliases:
  - "zkLLM"
  - "ZK proofs for LLMs"
  - "zero-knowledge proofs for large language models"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "zkml"
    - "proof-systems"
  problem:
    - "verifiable LLM inference"
    - "model-parameter privacy during inference auditing"
    - "non-arithmetic tensor operations in ZK proofs"
  method_family:
    - "tensor lookup arguments"
    - "attention-specific ZK protocols"
    - "sumcheck-based tensor arithmetic"
    - "homomorphic polynomial commitments"
  system_layer:
    - "verifiable inference"
    - "model commitment"
    - "GPU proving implementation"
  evaluation_context:
    - "OPT"
    - "LLaMa-2"
    - "BLS12-381"
    - "A100 GPU"
  bridge:
    - "zk-snarks-to-zkml-verifiable-inference"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
source_refs:
  - "doi:10.1145/3658644.3670334"
  - "arxiv:2404.16109"
  - "sha256:1df6be44e1cc301bd6662e0cd84795914b83fe3068621dde51052f61009022e8"
confidence: "high"
trust_tier: "primary"
primary_direction: "zkml"
secondary_directions:
  - "proof-systems"
classification_status: "accepted_with_metadata_correction"
classification_confidence: "high"
classification_evidence:
  - "The paper's main problem is proving LLM inference correctness while hiding proprietary model parameters."
  - "The reusable method layer is ZK proof engineering for tensor operations, lookup-heavy nonlinearities, and attention."
  - "Queue year/arXiv metadata were noisy; the local PDF is the CCS 2024 paper and points to arXiv 2404.16109 as the long version."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0030"
local_pdf: "~/Desktop/paper/3658644.3670334.pdf"
pdf_sha256: "1df6be44e1cc301bd6662e0cd84795914b83fe3068621dde51052f61009022e8"
extracted_text_path: "vault/02_Raw/pdf/extracted/zkllm-zero-knowledge-proofs-for-large-language-models-1df6be44e1cc-pages.txt"
---

# zkLLM: Zero Knowledge Proofs for Large Language Models

## 论文身份

- 标题: zkLLM: Zero Knowledge Proofs for Large Language Models
- 作者: Haochen Sun, Jason Li, Hongyang Zhang
- 机构: University of Waterloo
- 会议/期刊: CCS '24, ACM SIGSAC Conference on Computer and Communications Security
- 年份: 2024
- DOI: 10.1145/3658644.3670334
- arXiv: 2404.16109, PDF 指向 long version
- 链接: https://doi.org/10.1145/3658644.3670334
- 本地 PDF: `~/Desktop/paper/3658644.3670334.pdf`
- 代码/数据: https://github.com/jvhs0706/zkllm-ccs2024
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 16
- 已覆盖章节/页码: p1-p16, including introduction, technical overview, preliminaries, tensor lookup, zkAttn, protocol construction, complexity analysis, evaluation, related work, and appendices.
- 未覆盖章节/页码: none in the local CCS PDF. The long arXiv version is referenced but not reread here.
- Extraction gaps: none material; tables were text-extracted with readable values.
- 精读说明: 队列主路径 `zero-knowledge-proofs/zkml/verifiable-inference` 被接受。该论文是 zkML/verifiable inference source；`tlookup` 与 `zkAttn` 是论文内机制和可迁移方法路线，不单独升级为 source-name concept。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和结果 | 对 LLM 推理生成 ZK proof，隐藏模型参数，支持 13B 参数模型 | high | 主分类依据 |
| §1 / p1-p3 | 动机和贡献 | LLM legitimacy, model confidentiality, tlookup, zkAttn, large-model evaluation | high | 给出边界和贡献 |
| §2 / p3-p5 | Technical overview | LLM operations taxonomy, tensor lookup, attention proof intuition | high | 上层 verifiable inference 方法路线 |
| §3 / p5-p7 | Preliminaries | tensor notation, sumcheck, commitment scheme | medium | proof-system dependency |
| §4 / p7-p9 | Tensor lookup | tlookup protocol, subset/multiplicity identity, non-arithmetic functions | high | reusable mechanism |
| §5 / p9-p11 | zkAttn | Softmax/attention proof, segment decomposition, lookup table reduction | high | LLM-specific bottleneck |
| §6 / p11-p12 | zkLLM construction | Commit/Prove/Verify, transformer operations, reverse proof assembly | high | source-specific protocol |
| §7 / p12-p13 | Analysis | correctness, soundness, zero knowledge, complexity | high | security and cost boundary |
| §8 / p13-p15 | Evaluation | OPT/LLaMa-2 benchmarks, prover/verification/memory/perplexity | high | empirical evidence |
| §9 / p15 | Related work | zkML, zkCNN, ZEN, Mystique, training/unlearning proofs | medium | novelty boundary |
| Appendices / p16 | Formal statements and artifact | theorem pointers, long version, source code URL | medium | provenance |

## 核心精读笔记

> 这篇论文的主线是: 在不泄露 proprietary LLM weights 的前提下，让 verifier 检查某个 prompt/output 是否确实由已承诺的 LLM 推理得到。

### 问题、动机与边界

- 论文把应用动机放在 AI/LLM legitimacy 和监管审计上: LLM owner 可能需要证明某个输出确实来自自己的模型，但又不能公开模型参数。
- 参与方设定:
  - Prover 拥有 LLM，模型结构公开，weights 保密。
  - Verifier 提供或检查 prompt/output，并希望验证 output 的真实性。
  - Verifier 是 semi-honest: 会正确报告验证结果，但会试图从协议中学习模型参数。
- 证明对象是 committed model 上的一次 inference computation，而不是训练数据合法性、模型版权、输出无害性或模型质量。
- 模型参数通过 commitment 固定；ZK hiding 保护 weights，但系统仍需要信任 architecture、commitment setup 和推理 statement 的定义。

### 论文贡献

- `tlookup`: tensor lookup argument。它把 lookup 从扁平向量扩展到 tensor operations，保留 tensor structure 和 parallelization，目标是处理 activation、normalization、rescaling 等 non-arithmetic deep-learning operations。
- `zkAttn`: attention-specific ZK proof。它针对 Softmax in attention 的指数、归一化和 large lookup table 问题，用 shift-invariance、指数同态和分段 lookup 降低开销。
- 实现: CUDA-based implementation using BLS12-381 / ec-gpu, with verifier components adapted from zkCNN/mcl.
- 规模: 支持 OPT 和 LLaMa-2 系列，最大到 13B parameters；论文声称这是第一个展示 billion-scale LLM inference ZK proof 的系统。

### tlookup: tensor lookup argument

tlookup 要解决的问题是: LLM 中很多操作不是 field arithmetic，比如 activation、inverse square root、rescaling、Softmax exponent。直接 bit decomposition 或 multivariate lookup table 会造成不可接受的时间和内存。

核心 identity:

- 若 multiset `S` 被 table `T` 覆盖，则存在 multiplicity vector `m`，使得对随机挑战 `X`:
  - `sum_i 1/(X + S_i) = sum_j m_j/(X + T_j)`
- Verifier 采样 `beta`，prover 给出 inverse tensors `A=(beta+S)^-1` 和 `B=(beta+T)^-1`。
- 协议用 sumcheck 验证 inverse relation 和 sum relation。

对 elementwise non-arithmetic function `f: X -> Y`:

- 用 random linear combination `X + alpha Y` 和 table `T_X + alpha T_Y` 检查 lookup relation。
- 如果 pair `(x,y)` 不在 function table 中，随机 `alpha` 让伪造通过的概率很低。

对 ReLU/rescaling 一类函数:

- 通过 table decomposition 减少 lookup table size 和 witness overhead。
- 论文举例说明可把某些路线从 `O(B gamma)` 压到 `O(B + gamma)`。

### zkAttn: attention-specific proof

Attention 的核心是:

- `Attention(Q,K,V) = Softmax(QK^T / sqrt(d)) V`

直接证明 Softmax 有两个难点:

- logits 范围大，指数函数需要巨大 lookup table。
- Softmax 需要 row-wise normalization，shift constant `z_hat` 的选择和 rounding 会影响正确性。

zkAttn 的路线:

- 利用 Softmax 的 shift-invariance，把每一行 logits 平移到非正 bounded 区间。
- 定义 `z' = z - floor(z_hat)`，令 `z'` 非正且有界。
- 把 `z'` 分解成 `K` 个 base/segment 片段，用指数同态把一个大指数拆成多个小表 lookup 的乘积。
- 每个 segment 通过 tlookup 验证；再验证 segment decomposition、乘积关系和 row-wise sum/normalization。
- 对最高位 segment，table 可以退化成 indicator-like pattern；对最低位 segment，指数值接近 1，可用近似优化。

该方法不是通用“Softmax 已经免费”的证明。它依赖量化、shift 误差、segment 数和 table 参数；论文在 §7 给出误差和复杂度边界。

### zkLLM protocol construction

论文把 transformer inference 拆成若干可证明操作:

- Matrix multiplications: 用 sumcheck/MLE route。
- Activations: SwiGLU/GELU 可转成 lookup/tlookup 形式。
- Normalization: LayerNorm/RMSNorm 需要 inverse square root、rescaling、downscaling 等 lookup-heavy operations。
- Attention: 用 zkAttn 处理 Softmax bottleneck。

协议接口:

- `zkLLM-Commit(W)`: 对模型 weights 生成 commitment。
- `zkLLM-Prove(W, X)`: 对输入 prompt `X` 和输出 `y` 生成 inference proof。
- `zkLLM-Verify(X, y, commitment)`: 验证 output 与 committed weights 的 inference computation 一致。

实现上，proof assembly 从输出 `y` 反向回到 prompt `X` 和 parameters `W`，逐层证明中间 tensor relation。

### 安全与复杂度

- Commitment scheme: Hyrax/Pedersen-style polynomial commitment; no trusted setup; homomorphic; evaluation proof verifier/opening costs sublinear or logarithmic/square-root style depending on step.
- tlookup completeness error: 论文给出大约 `O(N / |F|)`；全系统 honest failure probability 约 `O(C / |F|)`。实现使用 BLS12-381 field，论文实验中没有观察到 verification failures。
- tlookup soundness: 如果 committed `S` 不是 `T` 的 subset，除了可忽略概率 verifier 会拒绝。
- Zero knowledge: 论文基于 ZK sumcheck 和 Pedersen commitments 改编 prior work，目标是隐藏模型参数和 witness tensors。
- zkAttn overhead: roughly `O(Kmn)` prover time/memory and `O(K sqrt(mn))` communication/verifier overhead for attention matrix dimensions, compared with bit decomposition routes that scale with `log B`。

### 实验与结果

实验设置:

- Hardware: 124.5GB memory, 12 CPU cores AMD EPYC 7413, NVIDIA A100SMX4 40GB。
- Models: OPT-125M, 350M, 1.3B, 2.7B, 6.7B, 13B; LLaMa-2-7B, 13B。
- Sequence length: default 2048 from C4。
- Quantization/scaling: embeddings and parameters use scaling factor `2^16`; Softmax input cumulative scaling around `2^64`。
- Softmax proof parameters: `K=5` tlookups, each table size `2^16`; least-significant segments optimized; reported attention error around `1e-2`。

Representative results:

| Model | Commit time | Commitment | Prover time | Proof | Verifier | Memory | C4 perplexity original -> quantized |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OPT-125M | 11.8 s | 0.996 MB | 73.9 s | 141 kB | 0.342 s | 1.88 GB | 26.56 -> 26.65 |
| OPT-350M | 33.1 s | 1.67 MB | 111 s | 144 kB | 0.593 s | 2.38 GB | 22.59 -> 22.66 |
| OPT-1.3B | 127 s | 3.32 MB | 221 s | 147 kB | 0.899 s | 3.71 GB | 16.07 -> 16.12 |
| OPT-2.7B | 273 s | 4.58 MB | 352 s | 152 kB | 1.41 s | 6.60 GB | 14.34 -> 14.37 |
| OPT-6.7B | 654 s | 7.22 MB | 548 s | 157 kB | 2.08 s | 15.0 GB | 12.71 -> 12.73 |
| OPT-13B | 1.27e3 s | 10.1 MB | 713 s | 160 kB | 3.71 s | 22.9 GB | 12.06 -> 12.07 |
| LLaMa-2-7B | 531 s | 7.97 MB | 620 s | 183 kB | 2.36 s | 15.5 GB | 7.036 -> 7.049 |
| LLaMa-2-13B | 986 s | 11.0 MB | 803 s | 188 kB | 3.95 s | 23.1 GB | 6.520 -> 6.528 |

论文总结:

- 13B model inference proof under 15 minutes.
- Proof size below 200 kB.
- Verification roughly 1-4 seconds in table results.
- Commitment size around 10 MB for 13B-class models; commitment time can approach 20 minutes.
- Memory below 23.1 GB in reported large-model experiments, fitting common data-center GPUs.
- Quantization degrades C4 perplexity by less than 0.1, and by less than 0.01 for 13B rows.

### 局限和非目标

- 论文证明的是 committed model 的 inference correctness，不证明 training provenance、copyright compliance、fairness、safety、absence of harmful output 或模型质量。
- Verifier model is semi-honest；恶意 verifier 或交互式协议部署需要额外分析。
- 模型 architecture 是 public，weights 是 committed/private；若 architecture 本身泄露商业信息，本设定不覆盖。
- 结果依赖 quantization/discretization 和 zkAttn approximation tolerance；不同任务可能需要不同误差预算。
- 证明生成仍需要大型 GPU 和显著 commitment/proving time；这不是 consumer-device 级别方案。
- "first" 和 "billion-scale" novelty claims 是论文自述，未通过外部综述验证。

## 方法与机制速查

| 机制 | 在论文中的角色 | 可迁移层级 | 不应误读为 |
| --- | --- | --- | --- |
| tlookup | 处理 tensor-shaped non-arithmetic operations | zkML/verifiable inference method route | 独立基础概念节点或 zkLLM 专有上层概念 |
| zkAttn | 证明 attention/Softmax bottleneck | LLM inference proof route | 通用 Softmax correctness without parameters |
| Sumcheck/MLE | 证明 tensor arithmetic and matrix multiplication | proof-system dependency | 论文自创基础协议 |
| Homomorphic commitments | 固定 secret weights and intermediate tensors | model commitment layer | 训练数据真实性证明 |
| Quantization | 把 LLM arithmetic 接入 finite-field/ZK setting | engineering assumption | 对所有模型无损 |

## 分类吸收

| Nahida layer | Decision | Reason |
| --- | --- | --- |
| Source note | keep as full paper memory | zkLLM 的 protocol、theorems、benchmarks、implementation details 都留在本笔记 |
| Knowledge direction | [[zkml|zkML]] | 多个未来 source 都可能落在 ML computation + ZK proofs |
| Knowledge problem | [[verifiable-inference|Verifiable inference]] | 论文解决的是 inference correctness under model/data privacy |
| Proof-system dependency | [[zk-snarks|zk-SNARKs]] / [[proof-systems|Proof systems]] | tlookup、sumcheck、commitment 是 proof engineering route |
| Bridge | [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | 将 succinct/ZK proof-system能力转移到 ML inference auditing |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Deep-read zkLLM and absorbed it as zkML/verifiable inference source. | codex |
