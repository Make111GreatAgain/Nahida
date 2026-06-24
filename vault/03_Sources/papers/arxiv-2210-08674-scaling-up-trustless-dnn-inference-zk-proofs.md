---
id: "arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs"
title: "Scaling up Trustless DNN Inference with Zero-Knowledge Proofs"
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
  - "p1-p12 full extracted text"
  - "Abstract, Sections 1-6, Appendix A, references"
canonical_url: "https://arxiv.org/abs/2210.08674"
doi: ""
arxiv_id: "2210.08674"
venue: "arXiv 2022; local PDF also contains an ICML 2020 proceedings footer"
year: "2022"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "verifiable-inference"
  - "zk-friendly-ml-operators"
  - "imagenet-scale-inference"
  - "halo2-plonkish-arithmetization"
  - "mLaaS-prediction-verification"
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
    - "zk-snarks"
    - "mLaaS-prediction-verification"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
topics:
  - "zkml"
  - "verifiable-inference"
  - "zk-friendly-ml-operators"
  - "zk-snarks"
  - "halo2"
  - "plonkish-arithmetization"
  - "lookup-arguments"
  - "trustless-dnn-inference"
  - "mLaaS"
aliases:
  - "Trustless DNN inference with ZKPs"
  - "ImageNet-scale ZK-SNARK DNN inference"
  - "Halo2 DNN inference proofs"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "ml-systems"
  subdomain:
    - "zkml"
    - "proof-systems"
    - "privacy-and-trustworthy-ml"
  problem:
    - "verifying MLaaS predictions without trusting the model provider"
    - "proving ImageNet-scale DNN inference with hidden weights or hidden inputs"
    - "auditing model accuracy without revealing proprietary model parameters"
    - "trustless retrieval with ML predicates"
  method_family:
    - "Halo2 and Plonkish arithmetization"
    - "custom gates for quantized linear layers"
    - "lookup arguments for nonlinear activation and rescaling"
    - "sub-circuit reuse and lookup-table sharing"
    - "Poseidon commitments to hidden weights and inputs"
    - "sampling and escrow protocols for MLaaS verification"
  system_layer:
    - "verifiable inference"
    - "model commitment"
    - "MLaaS prediction verification"
    - "model accuracy audit"
    - "trustless retrieval"
  evaluation_context:
    - "MobileNet v2"
    - "ImageNet"
    - "TensorFlow Lite to Halo2 circuit translation"
    - "AWS r6i.32xlarge"
    - "AWS r8i.8xlarge"
  bridge:
    - "zk-snarks-to-zkml-verifiable-inference"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs"
source_refs:
  - "arxiv:2210.08674"
  - "sha256:524f61c7c24776b923e0a3e477bced97e82a1323c219bb5a38f23d4f57933bd9"
confidence: "high"
trust_tier: "primary"
primary_direction: "zkml"
secondary_directions:
  - "proof-systems"
  - "privacy-and-trustworthy-ml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The paper's main problem is proving DNN inference and MLaaS predictions with ZK-SNARKs, not generic proof-system foundations."
  - "Sections 4-6 build and evaluate Halo2 circuits for ImageNet-scale MobileNet inference."
  - "The reusable method layer is ZK-friendly ML operator arithmetization: custom gates, lookup arguments, quantization and sub-circuit reuse."
  - "The protocol layer verifies model accuracy, model predictions and trustless retrieval over committed ML computations."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0089"
local_pdf: "~/Desktop/paper/2210.08674.pdf"
pdf_sha256: "524f61c7c24776b923e0a3e477bced97e82a1323c219bb5a38f23d4f57933bd9"
extracted_text_path: "vault/02_Raw/pdf/extracted/scaling-up-trustless-dnn-inference-with-zero-knowledge-proofs-524f61c7c247-pages.txt"
---

# Scaling up Trustless DNN Inference with Zero-Knowledge Proofs

## 论文身份

- 标题: Scaling up Trustless DNN Inference with Zero-Knowledge Proofs
- 作者: Daniel Kang, Tatsunori Hashimoto, Ion Stoica, Yi Sun
- 会议/期刊: arXiv 2022; local PDF also contains an ICML 2020 proceedings footer.
- 年份: 2022
- DOI: unknown in local PDF
- arXiv: 2210.08674
- 链接: https://arxiv.org/abs/2210.08674
- 本地 PDF: `~/Desktop/paper/2210.08674.pdf`
- 代码/数据: local PDF does not provide a durable repository URL in extracted text.
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 12
- 已覆盖章节/页码: p1-p12, including abstract, introduction, background, circuit construction, trust protocols, evaluation, appendix and references.
- 未覆盖章节/页码: none in extracted local PDF.
- Extraction gaps: tables are text-extracted with minor formatting loss; benchmark rows and protocol values remain readable.
- 精读说明: 队列把该论文放在 `zero-knowledge-proofs/proof-systems/proof-system-foundations`。深读后主路径纠正为 `zero-knowledge-proofs/zkml/verifiable-inference`，因为论文目标是 trustless DNN inference / MLaaS verification；Halo2/Plonkish SNARK 是实现层，lookup/custom gates/sub-circuit reuse 进入 `ZK-friendly ML operators` 方法族。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和贡献 | 用 ZK-SNARKs 在 untrusted setting 验证 DNN inference，声称首次在 commodity hardware 上支持 ImageNet-scale DNN | high | 主分类依据 |
| §1 / p1-p2 | 动机和威胁模型 | MLaaS provider 可能 lazy/dishonest/buggy；consumer 需要验证 prediction、accuracy 或 retrieval predicate | high | ML systems + zkML 交叉 |
| §2 / p2-p3 | 相关工作 | MPC/HE/IP/ZK prior work 的局限；prior ZK NN 多停留在 MNIST/CIFAR/custom protocols | medium | novelty boundary |
| §3 / p3-p4 | ZK-SNARK background | proof statement `y = f(x; w)`，succinctness、non-interactivity、knowledge soundness、zero knowledge；Halo2/Plonkish background | high | proof-system dependency |
| §4 / p4-p6 | ImageNet-scale circuit construction | MobileNet v2, quantization, fixed-point rescaling, custom gates, lookup arguments, TFLite-to-Halo2 translator, Poseidon commitments | high | method-family evidence |
| §5 / p6-p8 | Trust protocols | verifying model accuracy, verifying model predictions, trustless retrieval with ML predicates and escrow/sampling | high | application layer |
| §6 / p8-p10 | Evaluation | MobileNet/ImageNet setup, proving/verification/proof-size results, comparison to ZEN/vCNN/pvCNN/zkCNN lower bounds, protocol costs | high | empirical evidence |
| Appendix A / p10-p11 | Viability proof details | Griefing/timeouts and encrypted data-transfer subprotocol for model accuracy verification | medium | deployment boundary |
| References / p11-p12 | Related work anchors | Halo2, GKR, zkCNN, vCNN, ZEN, proof systems and ML service references | medium | future comparison seeds |

## 核心精读笔记

> 这篇论文的主线是: 在不信任 MLaaS provider 的情况下，用 ZK-SNARK 证明一次 DNN inference、一次模型 accuracy claim 或一个 ML predicate retrieval 结果确实来自承诺的模型和输入，而不必公开模型权重或敏感输入。

### 问题、动机与边界

- 论文面向 ML-as-a-Service setting: model provider 可能为了省钱返回错误结果、用更便宜的模型替代目标模型，或者因为实现 bug 给出错误 prediction。
- Consumer 的目标不是重新执行整个 DNN，而是检查 provider 给出的短 proof，从而确认 output 与公开/承诺的 model-input relation 一致。
- 论文支持三类 hiding/commitment 组合:
  - public input + hidden weights: consumer 看得到 input/output，provider 隐藏 proprietary weights。
  - hidden input + public weights: provider 或 requester 保护输入，证明中使用 input hash。
  - hidden input + hidden weights: 对 input 与 weights 都做 commitment/hash，再证明 inference relation。
- 证明边界很明确: 证明的是 inference computation、accuracy audit 或 retrieval predicate 的执行正确性；不证明模型训练来源、训练数据合法性、fairness、safety、output truth 或模型商业质量。

### 论文贡献

- 给出一个 ImageNet-scale DNN inference 的 ZK-SNARK circuit construction，目标模型是 MobileNet v2，而不是小型 MNIST/CIFAR toy network。
- 使用 Halo2 / Plonkish arithmetization，而不是只依赖 R1CS/Groth16-style scalar circuit；核心工程点是 custom gates、lookup arguments、permutation/copy constraints 和 proof-system-aware layout。
- 为 DNN operator 做专门 arithmetization:
  - 对 quantized linear layers 使用 addition gate 和 fixed-zero-point dot-product gate。
  - 对 ReLU/rescaling/clip 等非线性或非 field-friendly 操作用 lookup arguments。
  - 共享 lookup tables 和 sub-circuit layout，减少 repeated circuit overhead。
  - 从 TensorFlow Lite 模型自动翻译到 Halo2 circuits，尽量复用已有 rows/gates。
- 设计三类 trust protocol:
  - model accuracy verification: provider 证明隐藏模型在测试集上的 accuracy。
  - prediction verification: consumer 对一批 predictions 抽样 contest，provider 对 contested predictions 出具 ZK proofs。
  - trustless retrieval: responder 对 committed dataset 上的 ML predicate 匹配结果给出 proofs。

### Halo2 / Plonkish DNN arithmetization

论文的 proof construction 把 MobileNet-style inference 拆成可证明算子:

- Batch normalization 被融合进 convolution weights/biases，softmax 不进入 proof statement，系统返回 logits。
- 权重和 activation 使用 int8/uint8 quantization；floating scale 用 fixed-point approximation `a / b` 替代，以便落入 finite-field arithmetic。
- Linear layers:
  - dot product gate 固定 zero point，适合 quantized convolution / fully-connected blocks。
  - 长 dot product 超过 gate capacity 时通过 copy constraints 和 addition gate 拼接。
- Nonlinear/rescaling operators:
  - 论文把 rescaling 写成固定 `b` 的除法约束，再用 lookup table 检查 clipping/scaling 后的 output。
  - 选择跨层共享相同 `b`，从而复用 lookup table；residual layers 尤其能受益。
- Commitments:
  - 使用 Poseidon hash circuit 对 hidden input、hidden weights 或二者组合做 binding commitment。
  - 这使 proof statement 可以把公开 hash 与私有 witness 绑定起来。

这部分应吸收到 [[zk-friendly-ml-operators|ZK-friendly ML operators]]，因为它说明 zkML 不只是选择一个 SNARK，还要把 ML numeric/operator semantics 改写成 proof-system 友好的 relation。

### Trust protocols

#### Model accuracy verification

- 场景: consumer 要确认 provider 的 proprietary model 达到某个测试 accuracy，但 provider 不想公开 weights。
- 机制:
  - Consumer 准备测试输入和 labels。
  - Provider 对每个测试 input 的 inference output 生成 ZK proof。
  - Escrow/stake 让 provider 在 accuracy 低于阈值时承担损失，让 honest provider 在满足阈值时得到补偿。
- 关键边界:
  - validity 来自 ZK-SNARK soundness 和 commitment/hash binding。
  - viability 还依赖经济参数、escrow、理性参与者和 timeout/griefing 处理；这不是纯 proof-system 性质。

#### Model prediction verification

- 场景: consumer 已经相信 model accuracy，希望批量购买 predictions，但不想要求每个 prediction 都生成 proof。
- 机制:
  - Provider 先返回一批 predictions。
  - Consumer 记录 input/output hashes，并随机 contest 一部分。
  - Provider 对 contested predictions 提供 ZK-SNARK proofs；失败则触发 penalty。
- 这是一条 sampling + escrow route: 它用经济激励和随机抽检降低每个 prediction 都证明的成本。

#### Trustless retrieval

- 场景: requester 希望在 responder 的 committed dataset 中找出满足 ML predicate 的 records，比如 legal discovery、FOIA 或 copyright dataset check。
- 机制:
  - Responder 先对 dataset records 做 commitments/hashes。
  - Requester 发送 predicate/model。
  - Responder 对匹配 documents 的 inference/predicate evaluation 生成 ZK proofs，并返回匹配 documents。
- 边界:
  - 证明返回 record 属于 committed dataset 并满足 predicate。
  - 若 responder 恶意提交无效 corpus 或漏报，需要外部 signatures、sampling 或制度机制补齐。

### Evaluation

论文评估了 hidden model + hidden input 的较难设置，并报告 setup time、proving time、verification time 和 proof size。Setup once per architecture; proving/verifying per input.

| Model | Top-5 accuracy | Setup | Proving | Verification | Proof size |
| --- | ---: | ---: | ---: | ---: | ---: |
| MobileNet 0.35 / input 96 | 59.1% | 93.9s | 163.2s | 0.74s | 6528 bytes |
| MobileNet 0.5 / input 224 | 75.7% | 937.7s | 1530.7s | 6.32s | 7552 bytes |
| MobileNet 0.75 / input 192 | 79.2% | 1341.2s | 2457.5s | 10.27s | 5952 bytes |

Comparison lower bounds in the paper place prior systems at much higher proving time for comparable ImageNet-scale inference:

| Prior work | Reported lower-bound proving time in paper |
| --- | ---: |
| ZEN | 20000s |
| vCNN | 172800s |
| pvCNN | 31011s |
| zkCNN | 1597s |

Protocol-level cost examples:

- For verified prediction / trustless retrieval at 5% confidence, detecting 5%, 2.5% and 1% tampering uses sample sizes 72, 183 and 366 respectively, with estimated costs $11.99, $30.48 and $60.96.
- For model accuracy verification at 5% confidence, epsilon 5%, 2.5% and 1% use sample sizes 600, 2396 and 14979, with estimated costs $99.93, $399.08 and $2494.90.
- The authors frame these costs as small relative to some large commercial dataset or cloud-inference settings, but the numbers are source-specific and hardware/economic-context dependent.

### 与现有 vault 节点的关系

- [[verifiable-inference|Verifiable inference]]: 本文补充一条 ImageNet-scale DNN / MobileNet route，并把 MLaaS prediction verification 与 trustless retrieval 作为应用协议层。
- [[zk-friendly-ml-operators|ZK-friendly ML operators]]: 本文补充 Halo2/Plonkish custom gates、lookup nonlinearities、fixed-point quantization、TFLite-to-Halo2 translation 和 lookup-table sharing。
- [[zk-snarks|zk-SNARKs]]: 本文使用 ZK-SNARK properties 和 Halo2 backend；不改变 zk-SNARKs 的基础定义。
- [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]: 本文解决的是 provider correctness / model-weight privacy 的一部分，不等于完整 trustworthy ML。

## 可吸收知识点

| Candidate | Kind | Absorb? | Rationale |
| --- | --- | --- | --- |
| ImageNet-scale verifiable DNN inference | route section | yes | 扩展 [[verifiable-inference|Verifiable inference]]，不是独立基础概念 |
| Halo2/Plonkish DNN arithmetization | method route | yes | 扩展 [[zk-friendly-ml-operators|ZK-friendly ML operators]] |
| Lookup arguments for DNN nonlinearities | method route | yes | 与 zkLLM lookup/attention route、zkCNN convolution route 可比较 |
| Sampling + escrow prediction verification | protocol pattern | partial | 写在 source note 和 verifiable inference 应用路线；暂不单独建节点 |
| Trustless retrieval with ML predicates | application route | partial | 当前单源，作为 source extension 和 future bridge seed |
| MobileNet benchmarks | source-local evidence | no as node | 保留在本 source note |
| Paper title/system framing | source instance | no as knowledge node | 不把论文名升级为概念 |

## 不吸收/不外推

- 不把本文的 benchmark 数字推广为所有 zkML inference systems 的通用性能。
- 不把 Halo2 选择等同于 zkML 唯一路线；zkCNN、zkLLM、ZENO 等 source 已显示还有 sumcheck/GKR、GPU/tensor lookup、type-preserving compiler 等路线。
- 不声称本文 proof 解决训练 provenance、数据版权、fairness、alignment 或输出事实性。
- 不把 escrow viability 当成 cryptographic soundness；它依赖经济参数、timeout/griefing 处理和部署环境。

## Handoff 到知识库

| Target | Action | Status |
| --- | --- | --- |
| [[zkml|zkML]] | Add trustless DNN inference as verifiable inference source extension and update current synthesis/gaps. | done in run |
| [[verifiable-inference|Verifiable inference]] | Add Halo2/ImageNet-scale route, prediction/accuracy/retrieval protocol pattern and representative source row. | done in run |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | Add Plonkish custom gates, lookup nonlinearities, fixed-point quantization and TFLite-to-Halo2 translation route. | done in run |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | Add this source as evidence that zk-SNARK machinery transfers to committed DNN inference at ImageNet scale. | done in run |

## 后续问题

- ZEN, Mystique, ezDPS and private inference repositories still need absorption to calibrate how general this paper's Halo2 route is.
- The trustless retrieval protocol may later need a bridge to data discovery / verifiable retrieval if more sources appear.
- Numeric semantics for zkML still deserves its own synthesis after more fixed-point, quantized and floating-point zkML sources are absorbed.
