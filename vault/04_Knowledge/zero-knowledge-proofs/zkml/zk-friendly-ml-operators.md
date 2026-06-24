---
id: "nahida-knowledge-zkml-zk-friendly-ml-operators"
title: "ZK-friendly ML operators"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "zk-friendly-ml-operators"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
parent_knowledge_refs:
  - "nahida-knowledge-zkml"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "zk-friendly-ml-operators"
primary_ontology_path: "zero-knowledge-proofs/zkml/zk-friendly-ml-operators"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-inference"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
relation_edges:
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "is_a"
    to: "nahida-knowledge-zkml"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/zk-friendly-ml-operators.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "supports"
    to: "nahida-knowledge-zkml-verifiable-inference"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-inference.md"
      - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-inference.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-zkml-verifiable-inference.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
  - "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
  - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
representative_source_refs:
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
query_keys:
  - "ZK-friendly ML operators"
  - "zkML operators"
  - "ML operators in zero-knowledge proofs"
  - "ZK-friendly neural network operators"
  - "ZK-friendly tensor operators"
  - "zero-knowledge neural network compiler"
  - "zkNN operator optimization"
  - "convolution sumcheck"
  - "tensor lookup"
  - "attention proof"
  - "privacy-aware knit encoding"
  - "ZENO circuit"
  - "Halo2 DNN arithmetization"
  - "Plonkish ML operator lowering"
  - "lookup arguments for DNN nonlinearities"
  - "TensorFlow Lite to Halo2"
aliases:
  - "ZK-friendly neural network operators"
  - "zkML operator lowering"
  - "ZK-friendly tensor operators"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-inference"
  - "zk-friendly-ml-operators"
  - "operator-proving"
  - "tensor-arithmetic"
  - "lookup-operators"
  - "type-based-zkml-optimization"
  - "privacy-aware-constraint-reduction"
  - "halo2-plonkish-arithmetization"
  - "lookup-nonlinearities"
  - "fixed-point-quantized-dnn"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260623-zeno-verifiable-inference"
  - "nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs"
source_refs:
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
confidence: "high"
trust_tier: "primary"
---

# ZK-friendly ML operators

## 定义与范围

- 定义: ZK-friendly ML operators 是 zkML 中的方法族，研究如何把 ML 的 tensor、linear algebra、nonlinear functions、attention、convolution、pooling、activation、quantization 和 layer structure 转换成可被 zero-knowledge proof systems 高效证明的关系。
- 不包含: 单篇系统名、一个 operator gadget、某个模型 benchmark、一次 backend speedup 或完整 verifiable inference problem。zkCNN、zkLLM、ZENO、tlookup、zkAttn、ZENO circuit、knit encoding 都是 source instances 或 route details。
- Canonical terms: `ZK-friendly ML operators`, `zkML operator lowering`
- Aliases/query keys: ZK-friendly neural network operators, ZK-friendly tensor operators, ML operators in zero-knowledge proofs
- Standalone completeness check: 本节点本地解释为什么 ML operators 需要特殊 proof encoding、有哪些路线、适用边界和代表 sources；读者不需要先打开 zkCNN/zkLLM/ZENO 才能理解方法族。
- Retrieval role: 查询“ML/NN operator 怎么进 ZKP”“zkCNN、zkLLM、ZENO 的方法差别”“ZK-friendly operator 和 verifiable inference 的关系”时先读本节点。
- Update scope: 新 source 若涉及 ML operator arithmetization、lookup/table route、attention/convolution proof、type-preserving circuit generation、quantized/floating/fixed-point zkML operators、zkNN compiler or repository architecture，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

ML computation 不是普通标量 arithmetic circuit 的简单堆叠。真实模型大量使用 tensor shapes、matrix multiplication、convolution、attention、normalization、activation、pooling、quantization 和 layer-level reuse。ZKP/proof-system backend 通常更擅长 finite-field arithmetic、constraints、commitments、sumcheck、lookup 或 polynomial relations。如果直接把 ML 程序降成低级 scalar gates，会同时丢失 operator structure 和 optimization opportunities。

model_prior_background: 这个方法族位于 [[zkml|zkML]] 与 proof-system engineering 的中间层。它不决定 proof statement 的业务含义；[[verifiable-inference|Verifiable inference]] 决定要证明 output 与 committed model/input relation 一致。本方法族解决的是“这个 relation 如何以可承受代价编码和证明”。Trustless DNN inference 补充一条 Halo2/Plonkish 路线: 用 custom gates 编码 quantized dot products，用 lookup arguments 编码 rescaling/clip/nonlinearities，并通过 TFLite-to-Halo2 translation、fixed-point scale sharing 和 sub-circuit/lookup-table reuse 降低 ImageNet-scale DNN proof overhead。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family`
- 为什么足够通用: 当前 vault 已有四类不同 evidence: zkCNN 处理 CNN convolution/operator proving；zkLLM 处理 LLM tensor lookup 和 attention proof；ZENO 处理 type-preserving zkNN compiler/IR/constraint optimization；trustless DNN inference 处理 Halo2/Plonkish custom-gate + lookup + quantization route。它们共同指向一个可复用方法层，而不是一个系统名。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `zkCNN`、`zkLLM`、`ZENO` 和 `Trustless DNN inference` 都只是代表 sources；`FFT convolution sumcheck`、`tlookup`、`zkAttn`、`knit encoding`、`Halo2 custom gates` 和 `lookup nonlinearities` 默认保留为 route sections/source details。
- 需要引用的更基础 Knowledge: [[zkml|zkML]], [[verifiable-inference|Verifiable inference]], [[zk-snarks|zk-SNARKs]], [[sum-check-protocol|Sum-check protocol]]。
- 不应拆出的实例/协议/来源: zkCNN、zkLLM、ZENO、ZENO circuit、tlookup、zkAttn、VGG16/OPT/LLaMa benchmark 默认不拆成独立 knowledge nodes。

## 解决的问题

ZK-friendly ML operators 解决的是 ML computation 与 ZK proof backend 之间的 representation gap:

- Tensor/linear algebra 如果按 scalar gates 展开，constraint count、dependency 和 prover memory/time 会爆炸。
- Nonlinear functions、activation、Softmax、normalization、comparison 和 lookup-heavy operations 不天然适合 finite-field arithmetic。
- Quantized/fixed/floating numeric semantics 必须明确，否则 proof 证明的是错误或弱化的 relation。
- Privacy boundary 会影响 constraint cost: public weights/private inputs、private weights/private inputs、public/private outputs 的 cost 不一样。
- Verifiable inference 系统需要把 model commitment、operator proof、numeric encoding、privacy hiding 和 prover optimization 组合起来。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zkml|zkML]] | method_family_of | zkCNN, zkLLM, ZENO source absorption | active_seed |
| [[verifiable-inference|Verifiable inference]] | supports | operator lowering makes inference relation feasible | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | current sources mostly use zkSNARK/proof-system machinery | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么暂不拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Structured linear-operator proofs | route section | zkCNN gives convolution route and zkLLM/ZENO give tensor arithmetic context, but current evidence still fits one method-family node. | zkCNN, zkLLM, ZENO | active_seed |
| Lookup/nonlinear operator proofs | route section | zkLLM currently supplies the strongest source evidence; more lookup sources needed before splitting. | zkLLM | review |
| Type-preserving zkNN compiler frontends | route section | ZENO is one strong source; needs ZEN/Mystique/ezDPS/repo evidence before a child node. | ZENO | review |
| Plonkish/Halo2 DNN arithmetization | route section | Trustless DNN inference is one strong source; keep as route until more Halo2/Plonkish zkML systems are absorbed. | Trustless DNN inference | active_seed |
| Numeric semantics for zkML operators | candidate method_family | Floating/fixed/quantized routes touch this, but current vault needs more sources before splitting. | zkCNN, zkLLM, ZENO, floating-point SNARK sources | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Structured tensor/operator proof | 把 convolution、matrix multiplication 或 tensor relation 写成多项式/field relation，而不是完整 scalar circuit。 | ML bottleneck 是 structured linear algebra。 | 依赖 operator algebra、commitments、numeric encoding 和 ZK masking。 | [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]] |
| FFT/convolution sumcheck route | 用 FFT/Hadamard/IFFT relation 和 sumcheck/GKR 验证 CNN convolution。 | CNN inference proof 的主要瓶颈是 convolution layers。 | 主要覆盖 convolution；不直接覆盖 attention 或 normalization。 | zkCNN |
| Tensor/function lookup route | 把 activation、inverse square root、rescaling 等 non-arithmetic operations 转成 lookup relation。 | 函数域可量化或分段，table size 可承受。 | Table size、rounding、domain decomposition 和 backend overhead 是边界。 | [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] |
| Attention-specific proof route | 利用 Softmax shift-invariance、exponential homomorphism 和分段 lookup 证明 attention。 | Transformer/LLM attention 是 dominant bottleneck。 | 依赖 quantization、approximation tolerance 和 segment 参数。 | zkLLM |
| Type-preserving zkNN compiler frontend | 在降到 constraints 前保留 privacy type、tensor type 和 layer structure，指导 circuit generation 和 scheduling。 | 证明对象是 NN inference，且 public/private boundary 和 tensor shapes 明确。 | 不解决 proof-system foundation；依赖应用正确声明 privacy type。 | [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]] |
| Privacy-aware constraint reduction | 按 public/private types 选择 constraint generation；one-private dot product 可把 public scalars 放入 LC coefficients。 | One side of weight/feature is public, or privacy boundary 可精确表达。 | both-private 场景收益较小；误标 privacy 会改变 statement。 | ZENO |
| Packed low-bit equality checks | 用 finite-field bit width 承载多个 low-bit dot-product checks，减少 equality constraints。 | Quantized NN values 低 bit，finite field bit width 足够，且 overflow 可避免。 | Batch size、bit width 和 field size 限制收益；knit encoding 是 ZENO source-local design。 | ZENO |
| Layer-aware reuse/fusion | 重用同一 NN/circuit 的 constraints，缓存 public operand pairs，或 fuse injective layers 以减少 computations。 | 多图 proof、量化 NN、layer structure 稳定。 | 普通 NN fusion 不可直接搬运；ReLU/comparison 等 operator 仍可能昂贵。 | ZENO |
| Halo2/Plonkish custom-gate route | 把 quantized convolution/FC dot products 放进 custom gates，并用 copy constraints/addition gates 拼接长 dot products。 | DNN operators 可量化为 finite-field relations，backend 支持 custom gates/permutation arguments。 | 仍依赖 fixed-point approximation、gate capacity 和 layout choices；不是通用 SNARK 性能保证。 | [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Trustless DNN inference]] |
| Lookup nonlinearities and scale sharing | 对 activation/rescaling/clip 等非线性使用 lookup arguments，并跨层共享 scale denominator / lookup table。 | nonlinear function domain 可量化，多个 layers 能共享 scale/table。 | lookup table size、rounding semantics 和 backend lookup overhead 会限制收益。 | Trustless DNN inference |
| Model-to-circuit translation | 从 TensorFlow Lite model 自动生成 Halo2 circuit，并优先填充既有 rows/gates 以减少新 sub-circuit。 | 模型结构可解析且 operator set 被 translator 支持。 | Translator 正确性和 unsupported operators 需要另行验证；不等于完整 compiler correctness proof。 | Trustless DNN inference |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | paper | 给出 CNN convolution/operator proof route: FFT/convolution sumcheck、generalized GKR、quantized CNN proof assembly | CNN/convolution-specific; public architecture; prover/memory still costly | `p1-p18` |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | paper | 给出 LLM operator route: tensor lookup、attention-specific proof、GPU-parallel proving | semi-honest verifier; quantization/approximation; model commitment only | `p1-p16` |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | paper | 给出 type-preserving zkNN compiler/IR route: privacy/tensor type, privacy-adaptive circuit generation, knit encoding, ZENO circuit, layer scheduler, reuse/fusion | inference-only; CPU evaluation; no new proof-system security; privacy type must be specified correctly | `p1-p15` |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | paper | 给出 Halo2/Plonkish DNN operator route: custom gates for quantized linear layers, lookup nonlinearities/rescaling, sub-circuit reuse, TFLite-to-Halo2 translation | ImageNet/MobileNet-specific evaluation; fixed-point quantization semantics; proof costs remain high | `p1-p12` |

## 正反例约束

- 正确: 把 zkCNN/zkLLM/ZENO 当成本方法族的 source evidence。
- 正确: 把 `tlookup`, `zkAttn`, `ZENO circuit`, `knit encoding` 写作 route details 或 query keys。
- 正确: 把 operator encoding 与 proof statement 区分: operator route 让 relation 可证明，[[verifiable-inference|Verifiable inference]] 定义要证明什么。
- 错误: 认为使用这些 operator route 就自动证明模型训练来源、输出真实性、fairness、安全性或版权合法性。
- 错误: 把某篇论文的 benchmark 数字当成整个方法族的通用性能。
- 错误: 把 ZENO 作为基础概念节点；它是 source/system instance。

## 当前综合

- Evidence window: `2026-06-21` to `2026-06-23`，覆盖当前 vault 已深读 zkCNN、zkLLM、ZENO 和 trustless DNN inference。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: ZK-friendly ML operators 已从 review candidate 升级为 active_seed 方法族。zkCNN 说明结构化 convolution 可以通过 FFT/Hadamard/IFFT 和 sumcheck/GKR route 避免朴素 circuit 展开；zkLLM 说明 LLM 中 non-arithmetic tensor functions 和 attention 需要 lookup/approximation/attention-specific proof route；ZENO 说明在生成 constraints 前保留 privacy/tensor/layer semantics，可以显著降低 zkSNARK NN 的 constraint count、circuit computation dependency 和冗余生成；trustless DNN inference 说明 Halo2/Plonkish backend 下，custom gates、lookup nonlinearities、fixed-point quantization、sub-circuit reuse 和 model-to-circuit translation 也是让 ImageNet-scale DNN inference 可证明的关键路线。四者共同表明 zkML 的核心难点不是“有一个 SNARK 就够”，而是把 ML operator semantics、privacy boundary、numeric encoding 和 prover-system engineering 组合成可验证且可运行的 relation。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | 提供 CNN convolution/operator proof route | 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 ZEN/Mystique/ezDPS 后校准 |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | 提供 LLM lookup/attention operator proof route | 方法族; 代表 Sources | yes | 后续吸收更多 LLM/transformer operator proof sources |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | 将 `ZK-friendly ML operators` 从 review candidate 升级为 active_seed；补充 type-preserving compiler frontend 和 privacy/tensor-driven constraint optimization route | 定义; 方法族; 代表 Sources; 当前综合; 关系图谱 | yes | 后续吸收 trustless DNN inference / zkNN compiler sources 后校准 |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | 补充 Halo2/Plonkish DNN arithmetization route: custom gates、lookup nonlinearities、fixed-point quantization、TFLite-to-Halo2 translation | 背景; 方法族; 代表 Sources; 当前综合; 关系图谱 | yes | 后续吸收 ZEN/Mystique/ezDPS/Halo2 zkML implementations 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-inference` | application, verifiable_computation, privacy, implementation_reuse | Proof-system correctness/hiding transfers to encoded inference relation; operator semantics and privacy/numeric choices remain source/system-specific. | active_seed |
| [[sum-check-protocol-to-zkml-verifiable-inference|Sum-check protocol -> zkML verifiable inference]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/zkml/verifiable-inference` | application, method_transfer, operator_proving | Sumcheck/GKR transfers to encoded tensor/operator relations; non-arithmetic functions, commitments and ZK hiding need extra design. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml-zk-friendly-ml-operators | is_a | nahida-knowledge-zkml | vault/04_Knowledge/zero-knowledge-proofs/zkml/zk-friendly-ml-operators.md | high | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | supports | nahida-knowledge-zkml-verifiable-inference | zkCNN, zkLLM, ZENO source notes | high | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | depends_on | nahida-knowledge-zk-snarks | current sources use zkSNARK/proof-system machinery | medium | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md | source note | high | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md | source note | high | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | evidenced_by | vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md | source note | high | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | evidenced_by | vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md | source note | high | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | bridges_to | nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference | bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| ZEN/Mystique/ezDPS sources 未吸收。 | 需要把 ZENO 与 trustless DNN inference 同 prior zkNN compiler/operator systems 校准，避免少数路线过拟合。 | nahida-update / nahida-research-search | high | queued |
| Numeric semantics for zkML operators 未独立稳定。 | zkCNN/ZENO 依赖 quantized NN，zkLLM 依赖 quantization/approximation；floating-point/fixed-point route 还需要统一边界。 | nahida-knowledge-get / nahida-update | medium | review |
| Repository architecture evidence 缺失。 | 论文 source 说明方法，但 production compiler/API/backend integration 需要 repo-level notes。 | nahida-github-repo-analyze | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-zeno-verifiable-inference | Created active_seed method-family node from zkCNN/zkLLM/ZENO evidence; added ZENO type-preserving zkNN compiler and privacy/tensor-driven optimization route. | 3 source notes | codex |
| 2026-06-23 | nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs | Added Halo2/Plonkish DNN operator arithmetization, lookup nonlinearities, fixed-point quantization and TFLite-to-Halo2 translation as method routes. | 1 source note | codex |
