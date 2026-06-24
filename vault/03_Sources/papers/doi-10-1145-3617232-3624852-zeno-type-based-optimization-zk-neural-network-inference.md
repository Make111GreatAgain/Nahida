---
id: "doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference"
title: "ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference"
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
  - "p1-p15 full extracted text"
  - "Abstract, Sections 1-10, Artifact Appendix A, Tables 1-5, Figures 1-15, and references"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3617232.3624852"
doi: "10.1145/3617232.3624852"
arxiv_id: ""
venue: "ACM ASPLOS 2024"
year: "2024"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "verifiable-inference"
  - "zk-friendly-ml-operators"
  - "type-based-zkml-optimization"
  - "zknn-inference-optimization"
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-inference"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-inference"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/zk-friendly-ml-operators"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "ml-systems/privacy-and-trustworthy-ml"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "ml-systems"
  directions:
    - "zkml"
    - "proof-systems"
    - "privacy-and-trustworthy-ml"
  topics:
    - "verifiable-inference"
    - "zk-friendly-ml-operators"
    - "type-based-zkml-optimization"
    - "privacy-aware-constraint-reduction"
    - "tensor-type-circuit-ir"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-inference"
  - "zk-friendly-ml-operators"
  - "type-based-zkml-optimization"
  - "privacy-aware-knit-encoding"
  - "tensor-type-circuit-ir"
  - "zknn-inference-optimization"
aliases:
  - "ZENO"
  - "ZEro knowledge Neural network Optimizer"
  - "type-based zkNN optimizer"
  - "privacy-aware knit encoding"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
  - "nahida/zkml"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "ml-systems"
  subdomain:
    - "zkml"
    - "proof-systems"
    - "privacy-and-trustworthy-ml"
  problem:
    - "efficient zero-knowledge neural network inference"
    - "zkSNARK NN proof generation latency"
    - "semantic loss in scalar-level zkNN circuit generation"
    - "privacy-dependent constraint reduction for zkNN"
  method_family:
    - "ZK-friendly ML operators"
    - "type-preserving zkML compiler frontend"
    - "privacy-adaptive circuit generation"
    - "privacy-aware knit encoding"
    - "tensor-type ZENO circuit IR"
    - "workload-specialized parallel scheduling"
    - "NN-centric computation reuse and fusion"
  system_layer:
    - "verifiable inference"
    - "zkSNARK NN compiler frontend"
    - "circuit generation"
    - "circuit computation"
    - "security computation"
    - "prover-side system optimization"
  evaluation_context:
    - "Arkworks"
    - "Bellman"
    - "Ginger"
    - "MNIST"
    - "CIFAR-10"
    - "ShallowNet"
    - "LeNet"
    - "VGG16"
    - "ResNet-18"
    - "ResNet-50"
  application:
    - "biometric identity proof"
    - "private model evaluation"
    - "MLaaS prediction integrity"
  bridge:
    - "zk-snarks-to-zkml-verifiable-inference"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-zeno-verifiable-inference"
source_refs:
  - "doi:10.1145/3617232.3624852"
  - "sha256:19e5549e2f2d39b23cd4b1aea796e1cf38fd6c4c2f6d0284ed142f330f0e02d2"
confidence: "high"
trust_tier: "primary"
primary_direction: "zkml"
secondary_directions:
  - "proof-systems"
  - "privacy-and-trustworthy-ml"
classification_status: "refined_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Abstract and Section 1 define ZENO as a type-based optimizer for efficient zkSNARK neural-network inference."
  - "Sections 3-6 preserve privacy/tensor semantics, reduce constraints, and optimize circuit computation and NN-level reuse."
  - "The paper targets inference proof generation, not training, proof-system foundation, or generic hardware acceleration."
  - "The queued arXiv ID was a DOI-fragment false positive; the stable identity is DOI 10.1145/3617232.3624852."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0074"
local_pdf: "~/Desktop/paper/3617232.3624852.pdf"
pdf_sha256: "19e5549e2f2d39b23cd4b1aea796e1cf38fd6c4c2f6d0284ed142f330f0e02d2"
extracted_text_path: "vault/02_Raw/pdf/extracted/zeno-a-type-based-optimization-framework-for-zero-knowledge-neural-network-inference-19e5549e2f2d-pages.txt"
---

# ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference

## 论文身份

- 标题: ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference
- 系统/方案名: ZENO / ZEro knowledge Neural network Optimizer
- 作者: Boyuan Feng, Zheng Wang, Yuke Wang, Shu Yang, Yufei Ding
- 机构: University of California, Santa Barbara
- 会议/期刊: ASPLOS 2024
- 年份: 2024
- DOI: 10.1145/3617232.3624852
- arXiv: none observed in local PDF; queue 中的 `7232.36248` 是 DOI 片段误识别。
- 链接: https://doi.org/10.1145/3617232.3624852
- 本地 PDF: `~/Desktop/paper/3617232.3624852.pdf`
- SHA-256: `19e5549e2f2d39b23cd4b1aea796e1cf38fd6c4c2f6d0284ed142f330f0e02d2`
- 页数: 15
- Keywords: ZKP, Neural Networks, Privacy
- 代码: Artifact appendix 给出公开 GitHub: `https://github.com/BoyuanFeng/ZENO`
- License: first page states Creative Commons Attribution International 4.0 License.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 已覆盖章节/页码: Abstract, §1 Introduction, §2 Related Work and Motivation, §3 ZENO Language Construct, §4 Privacy-type Driven Optimization, §5 Tensor-type Driven Optimization, §6 NN-centric System Optimization, §7 Evaluation, §8 Discussion, §9 Conclusion, §10 Acknowledgment, references, Artifact Appendix A.
- 已检查附录: Artifact Appendix A covered.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: figures/tables text extraction is imperfect but all formulas, tables, reported numbers, artifact details, and section logic are readable.
- 精读说明: ZENO 是 zkML/verifiable inference 的系统优化 source。它提出的系统名不升级为知识节点；可复用上层是 [[verifiable-inference|Verifiable inference]] 下的 `type-based zkNN proof generation` route，以及新的方法族 [[zk-friendly-ml-operators|ZK-friendly ML operators]]。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与结果 | zkSNARK NNs 因 million-scale circuits 和 scalar dependency 慢；ZENO 保留 privacy/tensor 类型，做 privacy/tensor-driven optimization；VGG16 proof time 6 min -> 48s，最高 8.5x end-to-end speedup | high | 主分类依据 |
| §1 / p1-p2 | 动机与贡献 | 现有 zkSNARK frameworks 低级 circuit 丢失 NN semantics；缺语义感知优化和 NN-centric reuse/fusion | high | 上层方法族依据 |
| §2.1 / p3-p4 | zkSNARK background | Generate -> Circuit Computation -> Security Computation；public-private multiplication 和 addition 的约束成本差异 | high | privacy-driven optimization 的基础 |
| §2.2 / p4 | zkSNARK NNs | 说明 biometric identity、model privacy、World ID/Leela vs the World 等应用；只关注 inference，不支持 SGD training | medium | scope boundary |
| §2.3 / p4-p5 | Opportunities/challenges | privacy type 和 tensor computation 是两类优化机会；挑战是低级 circuit 无法恢复高层语义，且 gate dependency 重 | high | problem statement |
| §3 / p4-p5 | ZENO language construct | `zkTensor = (Tensor, Privacy)`，privacy/tensor 类型和 dotProduct/FC/convolution/pool/ReLU primitives | high | method-family evidence |
| §4 / p5-p7 | Privacy-type optimizations | privacy-adaptive circuit generation；one-private dot product 从 `n+1` constraints 降到 `1`；knit encoding 把多个低 bit equality checks 打包进一个 finite field | high | core mechanism |
| §5 / p7-p9 | Tensor-type optimizations | ZENO circuit IR 用 multi-child addition gate 降低 circuit computation 从 `O(n^2)` 到 `O(n)`，critical path 2；layer scheduler | high | compiler/IR route |
| §6 / p9-p10 | NN-centric optimizations | frequency-based cache、batch-specialized constraint sharing、zkSNARK-aware NN fusion | high | system optimization route |
| §7 / p10-p13 | Evaluation | Arkworks/Bellman/Ginger baselines；MNIST/CIFAR-10；SHAL/LCS/LCL/VGG16/ResNet；8.5x overall, 67.7x average circuit computation speedup, knit 3.63x | high | empirical evidence |
| §8 / p13 | Discussion | 与 MPC/DP/FHE/privacy-preserving inference 的定位差异；access-control/identity proof deployment vision | medium | boundary and application |
| §9 / p13 | Conclusion | 重申 language construct、privacy/tensor-driven optimizations、NN-centric system optimizations | medium | author framing |
| Artifact Appendix / p15 | Artifact | Rust 1.43.0, Arkworks fork, ZENO-engine, zkNN-circuit; small NN laptop feasible, ResNet-50 large RAM | medium | reproducibility clue |

## 核心精读笔记

> 这篇论文的主线是: 朴素 zkSNARK NN 把神经网络编成低层 scalar gates 后丢失了 privacy type、tensor shape 和 layer structure，于是只能做局部 gate 优化。ZENO 把这些高层语义保留下来，让 circuit generation、constraint generation、parallel scheduling、reuse 和 fusion 都能按 NN 结构优化。

### 背景、动机与问题边界

zkSNARK NN 用 proof 证明 `F(w, x) = y`，同时根据应用隐藏 input image、model weights 或 intermediate witness。论文举的应用包括:

- data privacy: 用户可证明人脸/虹膜身份，而不把原始 biometric image 上传给远程服务。
- model privacy: 公司可证明 model accuracy 或 inference output，而不公开 proprietary weights。

zkSNARK 证明生成被拆成三步:

1. Generate: 把 arithmetic function 映射成 addition/multiplication gates。
2. Circuit Computation: 把 circuit 压成约束系统。
3. Security Computation: 把 constraints 压成固定大小 proof。

ZENO 关注的是 prover/proof-generation latency。它不改变 verifier 语义，不提出新的 proof system，也不覆盖 training/SGD。论文明确说 ZENO focuses on inference and does not support SGD for training。

现有系统的三个瓶颈:

- high-level NN semantics 丢失: privacy、tensor shape、layer structure 一旦变成 assembly-style scalar circuit，很难再恢复。
- scalar-local optimization 不够: NN 主干是 tensor-level convolution/fully-connected/pooling；低级 gates 有重 dependency，难以并行。
- 缺 NN-centric system optimization: 同一 zkNN 在多张图片上共享 circuit，layer fusion/reuse 也和普通 NN compiler 不同；现有 zkSNARK NN 往往重复生成冗余 constraints。

### 模型、假设与定义

- zkSNARK NN 以 plaintext NN arithmetic function 为被证明 relation。
- 输入 `in = (w, x)` 可按 privacy type 标为 `private` 或 `public`。
- Addition 可在 linear combination 中近似“免费”表达；public scalar 与 private scalar 的乘法也可作为 public coefficient 进入 linear combination，通常不新增 private-private multiplication constraint。
- private-private multiplication 会带来 constraints，constraint 数量和 private values 数量直接影响 proof generation latency。
- NN 值通常是 int8/int1/half/single precision，但 zkSNARK 后端在大 finite field 上计算。ZENO 利用这一 bit-width mismatch 做 packing。
- 本文 evaluation 主要是 CPU 端 proof generation；GPU 支持留作 future work。

### ZENO language construct

ZENO 的第一步是保留类型语义，而不是先降到 scalar circuit:

- Standard scalar types: `Const`, `Variable`, `Gate`, `Wire`, `LC`。
- ZENO types:
  - `Privacy`: `private` or `public`。
  - `Tensor`: finite-field data tensor。
  - `zkTensor`: tuple `(T, P)`，其中 `T` 是 tensor，`P` 指定 privacy。

这让用户在 tensor 级写 NN，而不需要手工给每个 scalar 指定 privacy。ZENO primitives 包括:

- `dotProduct`
- `fullyConnected`
- `convolution`
- `pool`
- `ReLU`
- `addTensor`
- `mulTensor`

吸收判断: `ZENO language construct` 是 source-specific 接口名；可复用上层是 `type-preserving zkML compiler frontend` 和 [[zk-friendly-ml-operators|ZK-friendly ML operators]]，不是单独建 ZENO concept。

### Privacy-type driven optimization

#### Privacy-adaptive circuit generation

ZENO 利用 privacy type 减少 constraints。对 dot product `sum_i w_i * x_i`:

- both private: 每个 `w_i * x_i` 是 private-private multiplication，需要 `n` 个 multiplication constraints，再加一次 equality check，总共 `n+1` constraints。
- exactly one side private: public scalars 可作为 linear-combination coefficients，整个 dot product 只需最后一次 equality check，约 `1` 个 constraint。

这个差异是 ZENO 的核心动机之一: 不应该为 public data 引入不必要 privacy cost。

#### Privacy-aware knit encoding

Knit encoding 在只有 feature 或 weight 一侧为 private 时，把多个低 bit dot-product equality checks 打包到一个大 finite field equality check 里。

例子:

- NN feature/weight 是 uint8；finite field 可能是 254-bit。
- 对多个 dot products，ZENO 用 `delta` 做位移编码，把 `LC_1, LC_2, ...` 合成一个 `LC_s`。
- 只做一次 equality check 就能同时检查 `s` 个 dot products。
- Batch size 自动取满足无 overflow 的最大整数: `s <= b_out / (2 * b_in + ceil(log n))`。

安全边界:

- Knit encoding 的安全性依赖 no bit overflow。
- 它利用的是 zkSNARK linear-combination/free-addition property，不改变底层 proof-system security。
- 它适用于 one-private setting；与 ZEN 的 stranded encoding 适用场景不同。

论文比较:

- Knit encoding 最大 constraint saving 约 8x。
- Stranded encoding 最大约 4x，但用于 both-private case，且 decoding overhead 更高。

### Tensor-type driven optimization

#### ZENO circuit IR

传统 circuit 会把 dot product 展开成 `n` 个 multiplication gates 和 `n-1` 个 binary addition gates。Circuit computation 需要递归展开 addition tree，复杂度可到 `O(n^2)`。

ZENO circuit 用 multi-child addition gate:

- Dot product 仍有 `n` 个 multiplication gates，但只有一个 multi-child addition gate。
- Gate 数从 `2n-1` 降到 `n+1`。
- Circuit computation 从 `O(n^2)` 降到 `O(n)`。
- Critical path 从 `n` 降到 `2`。

对 fully-connected、convolution 和 average pooling，ZENO 把它们视为大量 dot products:

- Fully connected: `m` 个 dot products。
- Convolution: 通过 img2col 可看作 matrix-matrix multiplication，即 `mk` 个 dot products。
- Average pool: 可看作全 1 vector 与 grid values 的 dot product。
- ReLU 仍使用 scalar-level circuit，因为 comparison/bit decomposition 无法同样融合。

论文强调 ZENO circuit 和 conventional circuit 生成相同 constraint systems，因此是 in-place replacement，不改变被证明 relation。

#### Workload-specialized parallel scheduler

ZENO 的 scheduler 不是从低级 circuit 重新解析依赖，而是利用 NN layer shape:

1. 根据 plaintext NN layer shapes 统计每层 addition/multiplication 数量。
2. 因为每个 operation 映射到固定 gates，可以直接定位每层 gates。
3. 同一层内 gates 通常可并行，跨层仍保留 NN dependency。
4. 将同层 gates 均匀分给 threads。

这把 tensor/layer structure 变成 circuit computation 阶段的并行信息。

### NN-centric system optimization

#### Frequency-based cache service

ZENO 观察到 uint8 NN values 范围小、权重和 activation 常围绕 0 分布，因此某些 operand pairs 高频出现。它:

- offline profiling 100 张 plaintext images，找 top-k frequent addition/multiplication operand pairs，默认 `k=5`。
- online computation 时查 hash table 复用有限域计算结果。
- 只对 public data 使用 cache，以避免 timing side-channel 风险。

#### Batch-specialized constraint system sharing

同一个 zkNN 处理多张图片时，constraint system 描述的是同一 NN computation。ZENO 的 batch mode:

- 对同一 model/circuit 只执行一次 Generate 和 Circuit Computation。
- 对不同 images 赋不同 variable values。
- 在 ZEN accuracy scheme 这类多图 proof 场景中减少冗余 constraint generation。

#### zkSNARK-aware NN fusion

普通 NN compiler 的 fusion 多用于减少 memory access；zkSNARK NN fusion 目标是减少 computations/constraints。ZENO 不盲目套用普通 layer fusion:

- ReLU 不能简单 fuse 到 convolution，因为 zkSNARK 中 comparison operator 很贵。
- injective scale/add layers 可与 fully-connected/convolution 预计算融合。
- 例子: `Y = W X` 后接 `BN(Y) = gamma * Y + beta`，可预计算 `gamma * W`，直接证明 `(gamma * W)X + beta`。

### 理论、正确性与安全边界

- Tensor-type optimization 和 scheduler 是系统层优化，不引入 cryptographic changes。
- ZENO circuit 生成与 conventional circuit 相同的 constraint relation，因此 correctness 依赖等价的 constraint generation。
- Privacy-aware circuit generation 依赖 privacy type 的正确声明；如果把应私有的值误标为 public，这是 statement design/使用错误，不是优化本身可修复。
- Knit encoding 必须避免 finite-field bit overflow；ZENO 自动选择 batch size。
- Cache service 只缓存 public-data computation；对 private data 做 timing-dependent cache 会有安全风险，论文避免了这一点。
- 论文不证明 architecture privacy、training provenance、model fairness、输出真实性或安全性；它只证明编码后的 NN inference computation relation。

### 实验、评估与结果

Baselines:

- Arkworks: state-of-the-art zkSNARK framework and industry-used baseline。
- Bellman and Ginger: representative general zkSNARK frameworks；论文将 ZENO 编译的 constraints port 到二者比较 security computation。

Datasets/models:

- MNIST, CIFAR-10。
- ShallowNet, LeNetCifarSmall, LeNetCifarLarge, VGG16, ResNet-18, ResNet-50。
- CPU server: Intel Xeon Gold 5218 @ 2.30GHz, 503 GB DRAM。

End-to-end results:

| Model | Arkworks | ZENO | non-zkSNARK NN |
| --- | ---: | ---: | ---: |
| SHAL | 5.1s | 2.1s | 0.2s |
| LCS | 19.6s | 8.5s | 0.8s |
| LCL | 120s | 15.3s | 1.4s |
| VGG16 | 398s | 48s | 4.2s |
| RES18 | 826s | 102s | 8.9s |
| RES50 | 5440s | 680s | 54s |

Key reported speedups:

- Private image and public weights: up to 8.5x end-to-end over Arkworks。
- Private image and private weights: up to 2.01x end-to-end。
- VGG16 proof time reduced from about 6 minutes to 48 seconds in the abstract framing; Table 5 reports 398s -> 48s。
- ResNet-50 reduced from roughly 1.5 hours to around 11 minutes; Table 5 reports 5440s -> 680s。

Optimization analysis:

- Circuit computation step, private image/public weights: average 67.7x speedup, from 15x to 150x。
- Individual contributions in that setting:
  - ZENO circuit: 8.7x。
  - frequency-based cache: 1.2x。
  - workload-specialized scheduler: 6.2x。
- Circuit computation step, private image/private weights: average 9.4x speedup, from 2.5x to 24.6x。
- Layer-level circuit computation:
  - convolution up to 315.6x speedup。
  - fully connected up to 10.5x speedup。
- Knit encoding: up to 3.63x security computation speedup。
- Batch-specialized constraint sharing over 100 images: 6.5% overall speedup。
- Compared with Bellman and Ginger on security computation: ZENO reports 4.09x over Bellman and 5.26x over Ginger。

实验边界:

- Results are CPU/hardware/backend-specific。
- Proof generation is still much slower than non-ZK inference。
- GPU acceleration is discussed as future work, not evaluated by ZENO。
- Networks are quantized/int style zkNNs; floating-point NN semantic fidelity is not the paper's core problem。

### 作者结论与我的判断

作者明确声称:

- ZENO 保留 NN high-level semantics and type information，让 zkSNARK NN 可做更 aggressive compilation。
- Privacy-type driven and tensor-type driven optimizations 能降低 constraints、dependency 和 circuit computation cost。
- NN-centric reuse/fusion 进一步减少冗余。
- ZENO 在六个 zkSNARK NNs 上实现最高 8.5x end-to-end speedup。

由证据支持的判断:

- ZENO 是 zkML verifiable inference 的重要 source，因为它把瓶颈从“如何构造 proof statement”推进到“如何用 ML semantics 优化 proof generation”。
- 它足以把 `ZK-friendly ML operators` 从 review candidate 升级为 active_seed method-family: zkCNN 代表结构化卷积/sumcheck route，zkLLM 代表 lookup/attention route，ZENO 代表 type-preserving compiler/IR/constraint route。
- ZENO 不应该成为独立上层概念；ZENO 是系统实例，类型驱动的 zkNN proof generation 才是可复用方法路线。

仍需谨慎的推断:

- ZENO evaluation 不代表所有 zkML frameworks、all proof systems、GPU/ASIC backends 或 production systems。
- Privacy type optimization 依赖应用正确声明 public/private boundary。
- Knit encoding 的效果依赖 bit width、field size、dot-product length 和 overflow guard。
- ZENO 不解决 exact floating-point semantics；如果后续 source 使用 FP32/FP64，则应链接 [[floating-point-snarks|Floating-point SNARKs]] 或 numeric zkML 节点。

## 层级候选分类

- L1 Domain candidate: `zero-knowledge-proofs`
- L2 Direction candidate: `zkml`
- L3 Topic/content cluster candidates:
  - `verifiable-inference`
  - `zk-friendly-ml-operators`
  - `type-based-zkml-optimization`
  - `privacy-aware-constraint-reduction`
  - `tensor-type-circuit-ir`
- Ontology path: `zero-knowledge-proofs/zkml/verifiable-inference`
- 备选归属:
  - `zero-knowledge-proofs/zkml/zk-friendly-ml-operators`
  - `zero-knowledge-proofs/proof-systems/zk-snarks`
  - `ml-systems/privacy-and-trustworthy-ml`
- 父级领域: zero-knowledge proofs; ML systems
- 学术子领域: zkML; proof-system engineering; trustworthy ML
- 任务/问题: efficient zkNN inference proof generation
- 方法族: type-preserving compiler frontend; privacy-adaptive constraint generation; tensor IR; NN-centric reuse/fusion
- 模型/协议/算法族: zkSNARK NN inference
- 评测场景: MNIST/CIFAR-10, ShallowNet/LeNet/VGG/ResNet, Arkworks/Bellman/Ginger
- Benchmark/应用: biometric identity proof; private model evaluation; MLaaS prediction integrity
- 别名: ZENO; ZEro knowledge Neural network Optimizer
- 相邻方向: [[hardware-accelerated-proving|Hardware-accelerated proving]], [[proof-system-benchmarking|Proof-system benchmarking]], [[floating-point-snarks|Floating-point SNARKs]]
- 置信度: high
- 分类理由: 论文 title/abstract/sections all target zero-knowledge neural-network inference proof generation. It is not a generic SNARK foundation paper because it assumes zkSNARK machinery and optimizes NN-specific circuit/constraint generation.
- 分类状态: refined_from_queue
- 分类证据: Abstract, §1, §3-§7.
- Taxonomy version: 1.0
- Direction facets:
  - parent_domain: zero-knowledge-proofs; ml-systems
  - subdomain: zkml; proof-systems; privacy-and-trustworthy-ml
  - problem: efficient zero-knowledge neural network inference
  - method_family: ZK-friendly ML operators; type-based zkML optimization
  - system_layer: compiler frontend; circuit generation; circuit computation; prover optimization
  - evaluation_context: Arkworks, Bellman, Ginger, MNIST, CIFAR-10, VGG16, ResNet
- Tags: `nahida/source`, `nahida/paper`, `nahida/zkp`, `nahida/zkml`
- Map memberships: [[zkml|zkML]], [[verifiable-inference|Verifiable inference]], [[zk-friendly-ml-operators|ZK-friendly ML operators]]
- 归属说明: 本 source 的通用部分进入 method-family/problem nodes；论文系统名、公式细节、tables、benchmarks 和 artifact 细节保留在 source note。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | zero-knowledge-proofs | Title/abstract/§2 define zkSNARK NN proof generation | high | durable parent |
| Research problem | verifiable inference | §1 and §8 frame identity/model privacy through inference proof | high | update problem node |
| Foundation concepts | zk-SNARKs | §2.1 explains proof generation, constraints and finite fields | high | link foundation node; source extension only |
| Method family | ZK-friendly ML operators | §3-§6 preserve tensor/privacy semantics and optimize ML operator/circuit lowering | high | create active_seed method-family node |
| Application/evaluation context | biometric identity, private model evaluation, MLaaS integrity | §1, §8 and evaluation | medium | source extension / ML systems secondary |
| Artifact/source instance | ZENO | system name and artifact appendix | high | source instance only |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `zero-knowledge-proofs/zkml/verifiable-inference`
- 它能帮助未来哪些问题少读 source notes:
  - “zkNN/zkML 推理证明为什么慢?”
  - “ZENO 属于 zkML 哪个层级?”
  - “privacy type 如何减少 zkSNARK NN constraints?”
  - “zkCNN/zkLLM/ZENO 的方法差别是什么?”
  - “ZK-friendly ML operators 是什么?”
- 哪些内容应留在 source note，而不是创建上层节点:
  - ZENO system name and API details
  - exact formulas for knit encoding
  - individual benchmark numbers and hardware setup
  - artifact repository layout
  - top-k cache parameters and model-specific speedups
- 哪些上层节点过薄、缺失或需要 foundation_pack:
  - [[zk-friendly-ml-operators|ZK-friendly ML operators]] now created as active_seed but still needs ZEN/Mystique/ezDPS/Scaling up trustless DNN inference comparison.
  - [[verifiable-inference|Verifiable inference]] still lacks ZEN/Mystique/ezDPS and production repository architecture.
  - [[floating-point-snarks|Floating-point SNARKs]] may need future bridge to zkML numeric semantics.
- 哪些候选只是别名/query key/watch term:
  - `ZENO`, `ZENO circuit`, `knit encoding`, `privacy-aware knit encoding`, `type-based zkNN optimizer` are query keys/source mechanisms, not standalone foundation nodes yet.

## 可查询关键词

- ZENO
- type-based zkNN optimizer
- zero-knowledge neural network inference
- zkSNARK NN inference optimization
- privacy-adaptive circuit generation
- privacy-aware knit encoding
- ZENO circuit
- tensor-type driven optimization
- zkTensor
- workload-specialized parallel scheduler
- NN-centric system optimization
- zkSNARK-aware NN fusion
- VGG16 zero-knowledge inference proof
- Arkworks zkNN performance

## 更新记录

| 日期 | run_id | 变更 | 证据 | 操作者 |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-zeno-verifiable-inference | Deep-read source note created and classified into zkML/verifiable inference with ZK-friendly ML operators method-family secondary path. | 15-page local PDF, DOI 10.1145/3617232.3624852, sha256:19e5549e2f2d39b23cd4b1aea796e1cf38fd6c4c2f6d0284ed142f330f0e02d2 | codex |
