---
id: "nahida-knowledge-zkml-verifiable-inference"
title: "Verifiable inference"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "verifiable-inference"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
parent_knowledge_refs:
  - "nahida-knowledge-zkml"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-inference"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-inference"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/zkml/zk-friendly-ml-operators"
  - "zero-knowledge-proofs/applications"
relation_edges:
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "is_a"
    to: "nahida-knowledge-zkml"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-inference.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-zkml-verifiable-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "uses_method_family"
    to: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/zk-friendly-ml-operators.md"
      - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml-verifiable-inference"
    relation: "bridges_to"
    to: "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/llm-inference-privacy-to-zkml-verifiable-inference.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
  - "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
  - "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
  - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
  - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
representative_source_refs:
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
query_keys:
  - "Verifiable inference"
  - "verifiable ML inference"
  - "verifiable LLM inference"
  - "zero-knowledge inference proof"
  - "LLM inference correctness proof"
  - "zkLLM"
  - "CNN inference proof"
  - "zero-knowledge CNN inference"
  - "zkCNN"
  - "FFT convolution sumcheck"
  - "ZENO"
  - "type-based zkNN optimizer"
  - "privacy-aware knit encoding"
  - "ZK-friendly ML operators"
  - "trustless DNN inference"
  - "ImageNet-scale ZK-SNARK inference"
  - "Halo2 DNN inference proofs"
  - "MLaaS prediction verification"
  - "prompt privacy versus verifiable inference"
aliases:
  - "verifiable ML inference"
  - "ZK inference proofs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zkml"
  - "verifiable-inference"
  - "large-language-models"
  - "cnn-inference-proofs"
  - "fft-convolution-sumcheck"
  - "zk-friendly-ml-operators"
  - "type-based-zkml-optimization"
  - "zknn-inference-optimization"
  - "imagenet-scale-inference"
  - "halo2-plonkish-arithmetization"
  - "mLaaS-prediction-verification"
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
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
  - "nahida-knowledge-20260623-zeno-verifiable-inference"
  - "nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs"
  - "nahida-knowledge-20260623-risk-aware-llm-inference-privacy"
source_refs:
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable inference

## 定义与范围

- 定义: Verifiable inference 是 zkML 中的一个问题域，研究如何证明某个 ML/LLM output 是由指定 input 和已承诺/指定 model 正确推理得到，同时按系统需求隐藏 model weights、input、intermediate tensors 或其他 witness。
- 不包含: 模型训练过程证明、训练数据合规性、输出安全性、公平性评估、模型质量评估、单个 attention gadget 或某个 benchmark；这些需要单独 source 或上层问题节点。
- Canonical terms: `verifiable-inference`, `verifiable ML inference`
- Aliases/query keys: verifiable LLM inference, zero-knowledge inference proof, LLM inference correctness proof, CNN inference proof, zkCNN, ZENO, type-based zkNN optimizer
- Standalone completeness check: 本节点本地解释问题、边界、方法路线、适用条件、代表 source、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“怎么证明 LLM/CNN/NN 输出是真的”“模型参数不公开时如何验证 inference”“zkLLM/zkCNN/ZENO 属于什么问题”时先读本节点。
- Update scope: 新 source 若提供 ML/LLM/NN inference proof、private model evaluation、operator proof route、type-preserving zkNN compiler、GPU prover implementation 或 verifiable inference repository architecture，应刷新本节点。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

普通 ML inference verification 可以检查输出是否由某个模型和输入计算得到，但在商业 LLM 场景中，模型 weights 往往是 proprietary；在隐私场景中，输入或中间状态也可能敏感。Verifiable inference 因此需要同时满足:

- computation correctness: output 与公开 relation 一致。
- privacy/hiding: 不泄露被保护的 weights/input/witness。
- binding: 被证明的模型或参数已通过 commitment 或其他机制固定。
- efficiency: proof size、verification time、prover time 和 memory 能随模型规模被接受。

zkLLM 给出的 seed 是 LLM inference 场景: public architecture + committed secret weights + public prompt/output + ZK proof of computation。zkCNN 补充了更早的 CNN inference 场景: public CNN architecture + committed secret weights + public input/output + FFT/convolution sumcheck 和 GKR route 证明 convolutional layers、activation/pooling 与 fully-connected layers。ZENO 再补充 zkNN inference proof generation 的 compiler/system route: 在降到 constraints 前保留 privacy type、tensor type 和 layer structure，用 privacy-adaptive circuit generation、knit encoding、ZENO circuit、parallel scheduler 与 NN-centric reuse/fusion 降低 prover-side latency。Scaling up Trustless DNN Inference with Zero-Knowledge Proofs 补充 Halo2/Plonkish route: 用 custom gates、lookup arguments、fixed-point quantization、sub-circuit reuse 和 Poseidon commitments 证明 ImageNet-scale MobileNet inference，并把 proof 接到 MLaaS prediction verification、model accuracy audit 和 trustless retrieval protocols。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它描述一类可复用目标，不等于 zkLLM 或 zkCNN。CNN、transformer、recommendation model、private model evaluation 都可进入此节点。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkLLM、zkCNN 和 ZENO 是 source instances；tlookup、zkAttn、FFT convolution sumcheck、ZENO circuit、knit encoding、VGG16 benchmark 保留在 source note 或方法路线。
- 需要引用的更基础 Knowledge: [[zkml|zkML]], [[zk-friendly-ml-operators|ZK-friendly ML operators]], [[zk-snarks|zk-SNARKs]], [[proof-systems|Proof systems]], [[sum-check-protocol|Sum-check protocol]]。
- 不应拆出的实例/协议/来源: zkLLM、zkCNN、ZENO、tlookup、zkAttn、ZENO circuit、knit encoding、VGG16、OPT、LLaMa-2、A100 benchmark 默认不拆成独立 knowledge nodes。

## 解决的问题

Verifiable inference 解决的是 inference authenticity and privacy gap:

- Verifier 想确认 output 确实来自指定 model/input，而不是 prover 任意编造。
- Prover 想隐藏 proprietary model weights 或 sensitive witness。
- 大模型包含大量 tensor arithmetic 和 non-arithmetic operators，不能直接用朴素 circuit 表示。
- 即使 proof statement 已确定，若降级为 scalar-level circuit 时丢失 privacy/tensor/layer semantics，proof generation 也会被 constraints、gate dependency 和冗余 circuit computation 拖垮。
- 系统需要明确 proof 能证明什么，不能把 inference correctness 误读为训练 provenance、版权合规、对齐或安全审查。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zkml|zkML]] | child_of | zkLLM source absorption | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | zkLLM uses zero-knowledge proof-system machinery and commitments | active_seed |
| [[sum-check-protocol|Sum-check protocol]] | depends_on | zkCNN uses FFT/convolution sumcheck and generalized GKR to prove CNN inference operators | active_seed |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | uses_method_family | zkCNN, zkLLM and ZENO provide operator/proof-generation routes | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| LLM inference proofs | route section | 当前只有 zkLLM 一篇主 source；保留为章节，不拆独立节点。 | [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] | active_seed |
| CNN inference proofs | route section | zkCNN 提供 CNN prediction/accuracy proof route；当前作为章节和 source extension，不拆独立节点。 | [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]] | active_seed |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | method_family | zkCNN 的 convolution/operator proof、zkLLM 的 lookup/attention、ZENO 的 type-preserving zkNN compiler 共同支持一个可复用方法族。 | zkCNN; zkLLM; ZENO | active_seed |
| Type-based zkNN proof generation | route section | 当前由 ZENO 提供一条强 source route；保留为章节，不拆独立 child node。 | [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]] | active_seed |
| ImageNet-scale DNN inference proofs | route section | Trustless DNN inference 提供 Halo2/Plonkish MobileNet route；当前作为 source extension 和方法路线，不拆独立节点。 | [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | active_seed |
| Tensor lookup / non-arithmetic operators | route section | 已纳入 [[zk-friendly-ml-operators|ZK-friendly ML operators]]；当前仍以 zkLLM 为主 source。 | zkLLM | active_seed |
| Attention proof route | route section | zkLLM 的 zkAttn 是 LLM-specific bottleneck route，但当前证据仍单源。 | zkLLM §5 | active_seed |
| Structured linear-operator proofs | route section | zkCNN 的 FFT/convolution sumcheck 和 ZENO 的 tensor-type circuit IR 都说明 tensor structure 应保留；当前作为方法族内部路线。 | zkCNN; ZENO | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Model commitment | 对 weights 做 binding commitment，证明后续 inference relation 相对 committed model 成立。 | 模型 architecture 可公开，weights 需要隐藏但固定。 | 不证明 training provenance；commitment 生命周期和更新策略要另行设计。 | [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]]; [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]] |
| Sumcheck/MLE tensor arithmetic | 用 proof-system route 验证 matrix multiplication、tensor linear algebra 和层间 relation。 | 计算主干可表示为 field/tensor arithmetic。 | 非线性、normalization、Softmax、pooling 仍需额外方法。 | zkLLM §3-§6; zkCNN §3-§4 |
| FFT/convolution sumcheck | 把 CNN convolution 写成 FFT/Hadamard/IFFT 多项式关系，用专门 sumcheck 验证结构化线性算子。 | CNN/卷积层可在 FFT-friendly field 和量化语义下表达。 | 主要覆盖 convolution；不自动覆盖 attention、normalization 或 floating-point semantics。 | zkCNN §3 |
| Generalized GKR layer route | 用 fan-in addition/multiplication gates、arbitrary-layer inputs 和 random linear combination 拼接 CNN layers。 | 层级计算可被 GKR-style relation 描述。 | 需要配合 commitments、ZK masking、非线性 gadgets 和 numeric encoding。 | zkCNN §4 |
| Tensor/function lookup | 把 activation、inverse square root、rescaling 等 non-arithmetic operations 转成 lookup relation，并用 random linear combination 绑定 input/output pair。 | 操作可量化为 table 或 table decomposition。 | table size、rounding、function domain 和 backend overhead 是主要限制。 | zkLLM §4 |
| Attention-specific proof | 利用 Softmax shift-invariance、指数同态和分段 lookup 证明 attention，避免巨大 multivariate table。 | transformer/LLM attention 是瓶颈，logit 范围和误差预算可控。 | 依赖 quantization、segment 参数和 approximation tolerance。 | zkLLM §5 |
| GPU-parallel proving | 用 CUDA/GPU 处理大 tensor proving workload。 | 大模型推理证明需要高吞吐 proving。 | benchmark 不自动迁移到不同硬件、backend 或模型。 | zkLLM §8 |
| Type-preserving zkNN compiler frontend | 用 `zkTensor = (Tensor, Privacy)`、tensor primitives 和 layer structure 保留高层语义，指导 circuit generation。 | zkNN inference 的 public/private boundary 和 tensor shapes 可在前端表达。 | 不是新 proof system；误标 privacy 会改变 statement。 | ZENO §3 |
| Privacy-adaptive circuit generation | 按 public/private types 生成 constraints；one-private dot product 只需最后 equality check。 | weight 或 feature 一侧 public，另一侧 private，且 relation 可用 LC 表示。 | both-private 场景收益较小；依赖正确 privacy type。 | ZENO §4.1 |
| Privacy-aware knit encoding | 将多个低 bit dot-product equality checks 打包进大 finite field equality check。 | 量化 NN values 低 bit，finite field bit width 足够且无 overflow。 | Batch size 受 bit width/field/length 限制；ZENO source-local design。 | ZENO §4.2 |
| Tensor-type circuit IR and scheduler | 用 multi-child addition gate 的 ZENO circuit 降低 circuit computation 复杂度，并按 layer shape 调度并行。 | dot-product-heavy FC/convolution/pooling layers。 | ReLU/comparison 等仍需要 scalar gadgets；speedup 与模型/backend 有关。 | ZENO §5 |
| NN-centric reuse/fusion | 对 public frequent operands 缓存、跨图共享 constraint system、融合 injective layers。 | 量化 NN、多图证明或可预计算 scale/add layers。 | 普通 NN fusion 不可直接搬运；安全边界依赖 public-data cache。 | ZENO §6 |
| Halo2/Plonkish DNN arithmetization | 用 custom gates 表示量化 dot products，用 lookup arguments 表示 activation/rescaling/clip，并通过 sub-circuit/lookup-table sharing 降低 circuit overhead。 | DNN 可量化为 fixed-point/uint8 relations，architecture 可公开，backend 支持 Halo2-style lookup/custom gates。 | Proof 仍然昂贵；quantization/fixed-point approximation 会限定被证明的 numeric semantics。 | Trustless DNN inference §4 |
| Sampling + escrow prediction verification | 不对每个 prediction 都证明，而是批量返回 predictions，随机 contest 子集并用 ZK proof + penalty 约束 provider。 | MLaaS prediction purchase 可以容忍抽检，并有 escrow/stake 机制。 | Viability 是经济/协议性质，不等于 cryptographic soundness；需要 timeout/griefing 处理。 | Trustless DNN inference §5 |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | paper | 创建 verifiable inference 问题节点；展示 committed LLM inference correctness proof、weights hiding、tlookup/zkAttn route、13B-scale evaluation | semi-honest verifier, public architecture, quantized inference, committed-model only, hardware-dependent proving | `p1-p16` |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | paper | 补充 CNN prediction/accuracy proof route；展示 committed secret weights、FFT/convolution sumcheck、generalized GKR、LeNet/VGG/VGG16 evaluation | public architecture, quantized CNN computation, no architecture hiding, prover/memory still costly | `p1-p18` |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | paper | 补充 type-based zkNN inference optimization route；展示 privacy/tensor semantics、ZENO circuit、knit encoding、scheduler/reuse/fusion，最高 8.5x end-to-end speedup | inference-only, CPU evaluation, quantized NN setting, no new proof-system security, no training/architecture privacy | `p1-p15` |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | paper | 补充 Halo2/Plonkish ImageNet-scale DNN route；展示 MobileNet inference proof、lookup nonlinearities、sub-circuit reuse、model accuracy/prediction/retrieval protocols | quantized/fixed-point DNN semantics, hardware-specific proving costs, escrow/sampling assumptions, does not prove training provenance or model quality | `p1-p12` |

## 正反例约束

- 正确: 把 zkLLM/zkCNN 作为 verifiable inference 的 source extensions。
- 正确: 把 ZENO 作为 type-based zkNN proof generation source extension，把 [[zk-friendly-ml-operators|ZK-friendly ML operators]] 作为方法族节点。
- 正确: 把 tlookup/zkAttn 写在方法路线或 source note，不把论文机制名直接升级为基础概念。
- 正确: 把 ZENO circuit、knit encoding、scheduler 和 benchmark 数字留在 source note 或方法路线，不把 ZENO 系统名升级为基础概念。
- 正确: 把 FFT/convolution sumcheck 写成方法路线或 bridge，不把 zkCNN 系统名升级为基础概念。
- 正确: 明确 proof statement 是 "output follows from committed model and prompt"。
- 错误: 声称 verifiable inference 自动证明模型训练数据合法、模型公平、输出安全或 regulatory compliance。
- 错误: 把 large-model benchmark 当作所有 zkML 系统都会达到的性能。
- 错误: 声称 verifiable inference 自动保护用户 prompt 中的 PII。若 prompt/input/output 是 public statement，ZK proof 不提供 prompt privacy；该边界应通过 [[llm-inference-privacy|LLM inference privacy]] 或额外 private-input protocol 处理。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，覆盖当前 vault 已深读 zkLLM、zkCNN、ZENO 与 trustless DNN inference。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: Verifiable inference 现在有四条 source-backed route。zkCNN 说明 CNN-era inference proof 的瓶颈在 convolutional layers、量化 CNN semantics、GKR 层组合和 model-parameter privacy，FFT/convolution sumcheck 可以把结构化线性算子接入 proof；zkLLM 说明 LLM/transformer route 的瓶颈转向 non-arithmetic tensor operators、attention/Softmax、large-model memory 和 GPU proving；ZENO 说明即使底层 zkSNARK machinery 已定，zkNN inference 仍需要保留 privacy/tensor/layer semantics 来降低 constraints、circuit-computation dependency 和冗余生成；trustless DNN inference 说明 Halo2/Plonkish custom gates、lookup arguments、fixed-point quantization 和 sub-circuit reuse 可以把 ImageNet-scale MobileNet inference 接入 ZK-SNARK，并进一步组合 sampling/escrow protocols 支撑 MLaaS prediction、accuracy audit 与 trustless retrieval。四者共同支持本节点作为问题域，并把 [[zk-friendly-ml-operators|ZK-friendly ML operators]] 维持为 active_seed 方法族。该节点仍是 foundation_thin，因为 ZEN/Mystique/ezDPS、private inference repositories、proof-of-training/unlearning 和 production model-commitment lifecycle 仍未充分吸收。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | 创建 verifiable inference 问题节点；记录 LLM inference proof 方法路线和边界 | 定义; 解决的问题; 方法族; 代表 Sources; Bridge Links | yes | 吸收 zkML prior systems/repositories 后校准 |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | 补充 CNN inference proof route；新增 FFT/convolution sumcheck 和 generalized GKR layer engineering 方法路线 | 背景; 下级结构; 方法族; 代表 Sources; Bridge Links; 关系图谱 | yes | 吸收 ZEN/Mystique/ezDPS 后校准 CNN/NN proof routes |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | 补充 type-based zkNN proof generation route；新增 ZK-friendly ML operators 方法族节点；记录 privacy/tensor-driven constraint/circuit optimization | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links; 关系图谱 | yes | 吸收 ZEN/Mystique/ezDPS/trustless DNN inference 后校准 |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | 补充 Halo2/Plonkish ImageNet-scale DNN route；记录 lookup nonlinearities、sub-circuit reuse、MobileNet evaluation 和 MLaaS trust protocols | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links; 关系图谱 | yes | 吸收 ZEN/Mystique/ezDPS/private inference repositories 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-inference` | application, verifiable_computation, privacy, implementation_reuse | ZK proof-system correctness/hiding transfers to inference computation; ML training provenance, legality, safety and quality do not. | active_seed |
| [[sum-check-protocol-to-zkml-verifiable-inference|Sum-check protocol -> zkML verifiable inference]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/zkml/verifiable-inference` | application, method_transfer, verifiable_computation, operator_proving | Sumcheck/GKR transfers to encoded ML operator relations; commitment, ZK, numeric semantics and non-arithmetic operators need extra components. | active_seed |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | `zero-knowledge-proofs/zkml/zk-friendly-ml-operators; zero-knowledge-proofs/zkml/verifiable-inference` | method_family, operator_lowering, proof_generation_optimization | Operator/circuit techniques make inference relation feasible; they do not define the model commitment lifecycle or application trust policy. | active_seed |
| [[llm-inference-privacy-to-zkml-verifiable-inference|LLM inference privacy -> zkML verifiable inference]] | `ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy; zero-knowledge-proofs/zkml/verifiable-inference` | contrast, complementary, trust_boundary, privacy_boundary | Prompt privacy protects or sanitizes user input before black-box LLM; verifiable inference proves committed-model computation. Neither guarantee automatically transfers. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml-verifiable-inference | is_a | nahida-knowledge-zkml | vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-inference.md | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | depends_on | nahida-knowledge-zk-snarks | zkLLM proof-system construction | medium | active_seed |
| nahida-knowledge-zkml-verifiable-inference | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-inference | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | depends_on | nahida-knowledge-sum-check-protocol | zkCNN FFT/convolution and GKR route | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | bridges_to | nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | uses_method_family | nahida-knowledge-zkml-zk-friendly-ml-operators | ZENO/zkCNN/zkLLM source notes | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | evidenced_by | vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | evidenced_by | vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md | source note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | bridges_to | nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference | bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| More zkML verifiable inference systems 未吸收。 | 需要比较 zkCNN/zkLLM/ZENO/trustless DNN inference 与 ZEN/Mystique/ezDPS、private inference repositories 等路线。 | nahida-update / nahida-research-search | high | queued |
| ZK-friendly ML operators 仍是 active_seed。 | 当前已由 zkCNN/zkLLM/ZENO 建立方法族，但 numeric semantics、operator coverage 和 compiler/repo evidence 仍薄。 | nahida-update / nahida-github-repo-analyze | high | queued |
| Verifier threat model 扩展缺。 | zkLLM 使用 semi-honest verifier，实际部署可能需要恶意 verifier/interactive audit 分析。 | nahida-update | medium | queued |
| Model commitment lifecycle 缺。 | 生产系统需要处理模型版本、更新、revocation 和 public commitment registry。 | nahida-github-repo-analyze / nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Created verifiable inference problem node from zkLLM source absorption. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Added zkCNN as CNN inference proof route and bridged sum-check/GKR method layer into verifiable inference. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zeno-verifiable-inference | Added ZENO as type-based zkNN proof generation route and created ZK-friendly ML operators method-family node. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs | Added trustless DNN inference as Halo2/Plonkish ImageNet-scale verifiable inference route and MLaaS protocol evidence. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risk-aware-llm-inference-privacy | Added boundary bridge clarifying that prompt PII privacy and committed-model inference correctness do not transfer automatically. | 1 bridge note | codex |
