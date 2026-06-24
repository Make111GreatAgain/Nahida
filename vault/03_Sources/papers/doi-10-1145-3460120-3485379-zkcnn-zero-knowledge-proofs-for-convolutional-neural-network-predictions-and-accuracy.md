---
id: "doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy"
title: "zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy"
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
  - "p1-p18 full extracted text"
  - "Sections 1-5, evaluation, references, and appendices A-C"
canonical_url: "https://doi.org/10.1145/3460120.3485379"
doi: "10.1145/3460120.3485379"
arxiv_id: ""
venue: "ACM CCS 2021"
year: "2021"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "verifiable-inference"
  - "zkml"
  - "cnn-inference-proofs"
  - "fft-convolution-sumcheck"
  - "gkr-protocol"
  - "sum-check-protocol"
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-inference"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-inference"
secondary_ontology_paths:
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "ml-systems/privacy-and-trustworthy-ml"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
    - "ml-systems"
  directions:
    - "zkml"
    - "interactive-proofs"
    - "proof-systems"
    - "privacy-and-trustworthy-ml"
  topics:
    - "verifiable-inference"
    - "sum-check-protocol"
    - "zk-snarks"
    - "cnn-inference-proofs"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-inference"
  - "cnn-inference-proofs"
  - "sumcheck"
  - "gkr"
  - "polynomial-commitments"
  - "trustworthy-ml"
aliases:
  - "zkCNN"
  - "Zero Knowledge Proofs for CNN Predictions"
  - "zero-knowledge CNN inference"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
    - "ml-systems"
  subdomain:
    - "zkml"
    - "interactive-proofs"
    - "proof-systems"
    - "privacy-and-trustworthy-ml"
  problem:
    - "CNN inference correctness with private model parameters"
    - "verifiable MLaaS prediction"
    - "model accuracy claims without revealing weights"
    - "efficient proof of convolutional layers"
  method_family:
    - "FFT sumcheck"
    - "2-D convolution sumcheck"
    - "generalized GKR gates"
    - "zero-knowledge polynomial commitments"
    - "quantized CNN arithmetic"
  system_layer:
    - "verifiable inference"
    - "model commitment"
    - "CNN operator proving"
    - "accuracy proof over benchmark samples"
  evaluation_context:
    - "LeNet"
    - "VGG11"
    - "VGG16"
    - "MNIST"
    - "CIFAR-10"
    - "BLS12-381"
  bridge:
    - "zk-snarks-to-zkml-verifiable-inference"
    - "sum-check-protocol-to-zkml-verifiable-inference"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
source_refs:
  - "doi:10.1145/3460120.3485379"
  - "sha256:0c1b1b225158c99d0750626d98159ad13f166313518ebfcb21bec582dbbd5266"
confidence: "high"
trust_tier: "primary"
primary_direction: "zkml"
secondary_directions:
  - "interactive-proofs"
  - "proof-systems"
  - "privacy-and-trustworthy-ml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The paper's main problem is proving CNN prediction correctness while keeping model parameters secret."
  - "The reusable method contribution is sumcheck/GKR proof engineering for FFT and convolutional layers."
  - "The ML-systems relevance is trustworthy MLaaS prediction and accuracy auditing, but the primary mechanism is ZK proof construction."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0048"
local_pdf: "~/Desktop/paper/3460120.3485379.pdf"
pdf_sha256: "0c1b1b225158c99d0750626d98159ad13f166313518ebfcb21bec582dbbd5266"
extracted_text_path: "vault/02_Raw/pdf/extracted/zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy-0c1b1b225158-pages.txt"
---

# zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy

## 论文身份

- 标题: zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy
- 作者: Tianyi Liu, Xiang Xie, Yupeng Zhang
- 会议/期刊: CCS '21, ACM SIGSAC Conference on Computer and Communications Security
- 年份: 2021
- DOI: 10.1145/3460120.3485379
- arXiv: unknown in local PDF
- 链接: https://doi.org/10.1145/3460120.3485379
- 本地 PDF: `~/Desktop/paper/3460120.3485379.pdf`
- 代码/数据: 论文说明实现约 5000 行 C++，基于若干开源组件；本地 PDF 未给出明确仓库 URL。
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 18
- 已覆盖章节/页码: p1-p18, including abstract, introduction, preliminaries, FFT/convolution sumcheck protocols, zkCNN construction, implementation/evaluation, references, and appendices A-C.
- 未覆盖章节/页码: none in the local CCS PDF.
- Extraction gaps: figures/tables are text-extracted imperfectly but enough for all reported protocol and benchmark values.
- 精读说明: 队列元数据把该论文暂放在 ML systems 路线；深读后主路径纠正为 `zero-knowledge-proofs/zkml/verifiable-inference`。zkCNN 是 source instance；“CNN inference proof”“FFT/convolution sumcheck route”进入上层问题域/方法路线，不把 zkCNN 单独升为通用概念节点。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和结果 | 对 CNN 预测和模型 accuracy 生成 ZK proof，同时隐藏模型参数 | high | 主分类依据 |
| §1 / p1-p3 | 动机和贡献 | MLaaS 预测可信性、模型保密、FFT/卷积 sumcheck、GKR 改造、VGG16 结果 | high | 上层 zkML/verifiable inference route |
| §2 / p3-p5 | Preliminaries | CNN layers, convolution, sumcheck, GKR, ZK argument, polynomial commitments | medium | 方法依赖 |
| §3.1 / p5 | Existing approaches | arithmetic-circuit, FFT-circuit, vCNN polynomial multiplication route 的瓶颈 | high | novelty boundary |
| §3.2 / p5-p7 | FFT sumcheck | 用 Fourier matrix MLE 和 roots-of-unity product form 把 FFT proof generation 降到线性额外时间 | high | reusable method |
| §3.3 / p7-p8 | 2-D convolution | 向量化 2-D convolution，经 FFT/Hadamard/IFFT 三个 sumcheck 验证 | high | CNN operator proving |
| §4.1 / p8 | zkCNN definition | Commit/Prove/Verify 接口，public architecture + secret weights，支持 prediction/accuracy proof | high | source problem statement |
| §4.2 / p8-p10 | GKR generalization | fan-in addition/multiplication gates, arbitrary-layer inputs, multi-channel IFFT reduction | high | proof-system engineering |
| §4.3 / p10-p11 | Full construction | quantization, ReLU/max pooling gadgets, PC openings, Fiat-Shamir non-interactivity | high | protocol assembly |
| §5 / p11-p13 | Evaluation | C++ implementation, FFT/convolution benchmarks, LeNet/VGG/VGG16, vCNN/ZEN comparison | high | empirical evidence |
| Appendices / p15-p18 | Formal statements | GKR theorem, ZK argument/PC definitions, zkCNN formal protocol and proof sketch | high | correctness/soundness/ZK boundary |

## 核心精读笔记

> 这篇论文的主线是: 在 CNN 模型参数保密的前提下，让外部 verifier 检查某次 prediction 或一组 accuracy claim 是否确实由已承诺的 CNN 模型计算得到。

### 问题、动机与边界

- 论文面向 MLaaS / proprietary model setting: model owner 不愿公开 weights，但 verifier 需要确认返回 prediction 是由某个高质量模型正确计算出来的。
- 典型场景包括:
  - MLaaS provider 证明预测结果来自承诺的高质量 CNN，而不是低成本或错误模型。
  - 研究者或系统方证明某个 CNN 在私有 benchmark/adversarial examples 上达到给定 accuracy。
  - 公开模型 + 私有输入、私有模型 + 公开输入或二者都私有的变体可通过 commit-and-prove route 支持，但本文主线是公开 architecture、秘密 weights。
- 论文默认 CNN structure 公开，只隐藏 parameters。architecture hiding 明确留作 future work。
- 证明对象是 inference/accuracy computation relation，不证明训练 provenance、数据合法性、模型版权或安全性。

### 论文贡献

- 新的 FFT sumcheck protocol:
  - 对长度 `N` 的 vector，prover 生成 FFT sumcheck messages 的额外时间是 `O(N)`，比实际计算 FFT 的 `O(N log N)` 更低。
  - proof size 为 `O(log N)`；若 verifier 需要避免直接计算 Fourier MLE，可递归使用 sumcheck，把 verifier 时间和 proof size 控制在 `O(log^2 N)`。
- 新的 2-D convolution verification:
  - 将二维卷积转成一维卷积，再用 `FFT(X) * FFT(W)` 和 IFFT relation 验证。
  - Prover additional time `O(n^2)`，proof size 和 verifier time `O(log^2 n)`。
  - 不需要像 vCNN 那样对 convolution output 额外做 commitment，因此避免 commitment 成为主要瓶颈。
- CNN proof-system engineering:
  - generalized GKR addition/multiplication gates 支持 fan-in additions 和 inner products，用一次 sumcheck 处理较大的 layer relation。
  - 支持 arbitrary-layer inputs，让卷积/全连接层直接引用 witness/model 参数，而不是被迫穿过所有相邻层。
  - 多通道卷积利用 FFT 线性性，把 IFFT 次数从 `ch_in * ch_out` 降到 `ch_out`。
  - ReLU + max pooling gadget 把符号检查和最大值检查合并，只需要额外一次 bit decomposition。
- 实现和结果:
  - VGG16 / CIFAR-10 / 15.2M parameters 的单张 prediction proof: prover 88.3s，verifier 59.3ms，proof 341KB。
  - 相比 vCNN 的 VGG16 estimate，prover 速度约提升 1264x；代价是 proof size 比 pairing-SNARK 路线更大。

### FFT sumcheck route

论文把 FFT 写成 Fourier matrix 乘法:

- `a(y) = sum_x c(x) F(y,x)`
- 把 vector `a` 和 `c` 视为 multilinear extension，用 sumcheck 验证某个随机点上的 `a(u)` 是否等于 `sum_x c(x) F(u,x)`。

难点是 verifier/prover 如果直接维护 `F(u,x)` 表会有 `O(MN)` 代价。zkCNN 的关键技巧是:

- 用 roots of unity 把 Fourier matrix 的 MLE 写成 product form。
- 初始化 bookkeeping tables `A_F` 时只需要 `O(M+N)`。
- 每轮 sumcheck 更新 `F(u,x)` 相关项时不需要重复展开完整 matrix。

因此 FFT proof generation 成为线性额外工作，而不是把 FFT circuit 电路化后得到 `O(N log N)` gate proof。

### 2-D convolution sumcheck route

CNN 的核心瓶颈是卷积层。zkCNN 的路线是:

1. 将 `n x n` input 和 `w x w` kernel 通过 reversal / vectorization 变成一维向量。
2. 用 FFT 计算一维 convolution:
   - `Ubar = IFFT(FFT(Xbar) ⊙ FFT(Wbar))`
3. 对三类 relation 分别证明:
   - `FFT(Xbar)` 和 `FFT(Wbar)` 正确；
   - Hadamard product 正确；
   - IFFT 结果与输出卷积值一致。

这一路线的通用意义是: 对卷积这类高结构线性算子，不一定要构造完整 arithmetic circuit；可以把 operator algebra 拆成若干可 sumcheck 的多项式关系。

### zkCNN protocol construction

协议接口:

- `KeyGen`: 生成 polynomial commitment parameters。
- `Commit(W)`: prover 对 CNN weights 做 commitment。
- `Prove(W, X)`: 对输入 `X`、模型 `W` 和输出 `y` 生成 prediction proof。
- `Verify(comW, X, y, pi)`: verifier 检查 `y` 是否由 committed model 正确计算。

核心假设与语义:

- CNN architecture 公开，weights 保密。
- Verifier 可以看到输入 `X` 和输出 `y`，或通过 commit-and-prove 变体支持 secret input。
- Accuracy proof 可通过对 dataset 中多张图片重复 prediction proof / batch relation 来证明。
- Fiat-Shamir heuristic 用于把交互式 protocol 转成 non-interactive proof，安全性在 random oracle model 下陈述。

### GKR generalization and layer engineering

论文没有只靠 convolution sumcheck 拼系统，而是系统性改造了 GKR route:

- Generalized addition gates: 一个 gate 可以聚合多个 input values，避免把大 fan-in addition 展开成二叉树。
- Generalized multiplication gates: 可表达 inner product relation，用一次 sumcheck 处理矩阵/全连接层中的向量乘加。
- Arbitrary-layer inputs: layer 可以直接读取 witness/model 参数层，使 GKR claim 最终只需用 random linear combination 归约到一个 input evaluation。
- 多通道卷积:
  - 传统 route 对每个 input-channel/output-channel pair 做 IFFT。
  - zkCNN 利用 FFT 线性性，先聚合 Hadamard products，再对每个 output channel 做一次 IFFT。

这些技巧是上层 `verifiable inference` 可复用的方法族，但它们仍以 zkCNN 这篇 source 为具体实例。

### Quantization, ReLU and max pooling

zkCNN 使用 fixed-point quantization:

- 用 affine integer mapping `a = L(q - Z)` 表示 real value。
- 把 scale/zero point normalization 延后处理，使 sumcheck 主要作用在 integer-like relation 上。
- 论文使用 8-bit quantized weights/values，并用 32-bit normalized scale。

ReLU 和 max pooling:

- ReLU 通过绝对值和 sign bit 的 bit decomposition 检查。
- Max pooling 要求 prover 给出最大值，再证明所有差值非负且至少一个差值为零。
- ReLU + max pooling 可以组合，减少额外 bit decomposition 次数。

这部分是 numeric semantics 的边界: 证明的是量化后 CNN 的计算正确性，而不是原始 floating-point 网络语义完全一致。

### 安全性与正确性

- Correctness: honest prover 对 committed weights 和真实 CNN computation 生成的 proof 应通过验证。
- Soundness: 若 prediction claim 与 committed CNN computation 不一致，除非 sumcheck/GKR/PC soundness 被破坏，否则 verifier 以 overwhelming probability 拒绝。
- Zero knowledge: 协议用 zero-knowledge sumcheck、low-degree extension masking 和 zero-knowledge polynomial commitments 隐藏 weights 与 witness values。
- Knowledge soundness 在 appendices 中通过 polynomial commitment 的 knowledge soundness 给出更强版本。
- 论文使用 discrete-log-based polynomial commitment，无 trusted setup；prover 需要 `O(N)` exponentiations，proof/verifier 约 `O(sqrt N)` 量级。

### 实验与结果

实现与环境:

- C++ implementation, about 5000 LOC, based on existing open-source implementations。
- BLS12-381 curve with mcl library；单 CPU core；AMD EPYC 7R32 64-core machine, 128GB RAM；10-run averages。
- 论文指出 memory 是 scaling bottleneck；VGG16 和多图 accuracy proof 需要显著内存。

FFT benchmark:

- vector size `2^10` 的 FFT proof 约 0.6ms，`2^18` 约 0.1s。
- 相比 FFT-circuit baseline，速度从 17x 到 33.2x；proof size 小 15.4x 到 35.4x。
- 相比 naive sumcheck，`2^8` 时约 80x faster；naive route 在 `2^14` OOM。

Convolution benchmark:

- 32x32 input, 4x4 kernel: 4.7ms vs baseline 7.7ms。
- 32x32 input, 16x16 kernel: speedup 8.5x。
- 256x256 input, 64x64 kernel: speedup 291x。
- Proof size 约 5.6KB 到 8.4KB，verifier 约 0.1ms 到 0.3ms。

CNN end-to-end:

- LeNet / MNIST: prover 0.441s，verifier 5.80ms，proof 71.3KB。
- VGG11 / CIFAR-10: prover 47.8s，verifier 39.3ms，proof 304KB。
- VGG16 / CIFAR-10: prover 88.3s，verifier 59.3ms，proof 341KB。
- 与 vCNN/ZEN 比较:
  - LeNet avg pooling: zkCNN 0.49s vs vCNN 5.49s。
  - LeNet CIFAR-10 avg pooling: zkCNN 0.56s vs ZEN 119.5s。
  - VGG16: zkCNN 88.3s vs vCNN 约 31 hours estimate，约 1264x faster。
- Accuracy proof:
  - VGG16 on 20 images: prover 520s，proof 635KB，verifier 121ms。
  - proof/verifier 增长部分来自 polynomial commitment witness padding 到 powers of two。

## 对 Nahida 分层知识库的吸收判断

### 应进入的上层节点

- [[verifiable-inference|Verifiable inference]]: zkCNN 是 CNN-era source-backed route，补足 zkLLM 之前的 CNN inference proof 路线。
- [[zkml|zkML]]: 作为 zkML 的 inference 子问题 source，而不是单独概念。
- [[sum-check-protocol|Sum-check protocol]]: FFT/convolution sumcheck 是 sumcheck 在结构化线性算子上的重要应用。
- [[zk-snarks|zk-SNARKs]]: zkCNN 使用 ZK arguments、GKR、polynomial commitments 和 Fiat-Shamir non-interactivity，是 zkML proof-system engineering 的 source extension。
- [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]: 只作为 cross-domain ML trust evidence；主机制仍属于 ZKP/zkML。

### 不应升级为独立知识节点的内容

- `zkCNN`: 单篇论文和系统名，保留为 source note。
- `FFT sumcheck for convolution`: 当前是方法路线；若后续多篇 source 独立复用，可升级为 `operator proving` 或 `structured linear operator proofs` 节点。
- `VGG16 benchmark`, `LeNet benchmark`, `CIFAR-10 accuracy proof`: 只作为 source evidence。
- 论文中的 implementation/mcl/BLS12-381 选择: 属于 source-specific backend detail。

### 新增桥接需求

- 新建 [[sum-check-protocol-to-zkml-verifiable-inference|Sum-check protocol -> zkML verifiable inference]]，说明 sumcheck/GKR 如何从交互式证明工具迁移到 CNN/ML operator proving。
- 更新 [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]]，把 zkCNN 加入 zkLLM 之前的 CNN route，校准“verifiable inference”并非只等于 LLM route。

## 边界与残留问题

- Architecture privacy: 本文隐藏 weights，不隐藏 CNN architecture。
- Setup/trust: polynomial commitment route no trusted setup，但依赖 discrete-log security 和具体 PC implementation。
- Numeric semantics: 证明的是 quantized CNN computation，不直接证明 floating-point model semantics。
- Prover cost: 相比 prior CNN ZK 系统快很多，但 VGG16 仍需分钟级 prover time；多样本 accuracy proof 仍有内存/时间瓶颈。
- Proof size tradeoff: proof size 比 pairing-based vCNN/ZEN 大，但避免了 trusted setup / large CRS tradeoff。
- Scope: 论文不覆盖 transformers、LLM attention、training proof、model update provenance、fairness 或 robustness。

## 可查询关键词

- zkCNN
- zero-knowledge CNN inference
- CNN prediction proof
- VGG16 zero-knowledge proof
- convolution sumcheck
- FFT sumcheck
- GKR CNN proof
- model-parameter privacy
- MLaaS prediction integrity
- zero-knowledge accuracy proof

## 更新记录

| 日期 | run_id | 变更 | 证据 | 操作者 |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Deep-read source note created and classified into zkML/verifiable inference with sum-check and ML-trust secondary paths. | 18-page local PDF, DOI 10.1145/3460120.3485379, sha256:0c1b1b225158c99d0750626d98159ad13f166313518ebfcb21bec582dbbd5266 | codex |
