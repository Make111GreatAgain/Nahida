---
id: "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
title: "zk-SNARKs -> zkML verifiable inference"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "zk-snarks"
  - "zkml"
  - "verifiable-inference"
endpoint_knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-zkml-verifiable-inference"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/zkml/verifiable-inference"
relation_types:
  - "application"
  - "verifiable_computation"
  - "privacy"
  - "implementation_reuse"
directionality: "one_way"
maturity: "active_seed"
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
  - "zk-SNARKs for verifiable inference"
  - "zkML verifiable inference"
  - "ZK proofs for LLM inference"
  - "ZK proofs for CNN inference"
  - "ZK proofs for neural network inference"
  - "committed model inference proofs"
  - "zkCNN"
  - "convolution sumcheck"
  - "ZENO"
  - "type-based zkNN optimizer"
  - "privacy-aware knit encoding"
  - "ZK-friendly ML operators"
  - "trustless DNN inference"
  - "Halo2 DNN inference proofs"
  - "ImageNet-scale ZK-SNARK inference"
aliases:
  - "ZK proofs for ML inference"
  - "SNARK-based verifiable inference"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zk-snarks"
  - "zkml"
  - "verifiable-inference"
  - "cnn-inference-proofs"
  - "zk-friendly-ml-operators"
  - "type-based-zkml-optimization"
  - "halo2-plonkish-arithmetization"
  - "mLaaS-prediction-verification"
tags:
  - "nahida/bridge"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
  - "nahida-knowledge-20260623-zeno-verifiable-inference"
  - "nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs"
source_refs:
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
confidence: "high"
trust_tier: "primary"
---

# zk-SNARKs -> zkML verifiable inference

## 关系命题

zk-SNARK/proof-system machinery 可以作为 zkML verifiable inference 的可验证计算层: verifier 不重新执行巨大模型，而是检查一个短 proof，确认公开 input/output 与已承诺模型参数之间的 inference relation 成立；zero-knowledge hiding 用于保护 proprietary weights 或其他 witness。zkCNN 给出 CNN route，zkLLM 给出 LLM route，ZENO 给出 type-preserving zkNN optimization route，trustless DNN inference 给出 Halo2/Plonkish ImageNet-scale DNN route，四者共同说明这是一条 ML inference 问题域桥，而不是单个模型家族的技巧。

这条 bridge 不表示 ZK proof 自动解决 AI legitimacy 的全部问题。它只把 succinct verification、soundness、hiding 和 commitment binding 转移到 inference computation；模型训练来源、版权、fairness、alignment、安全性、输出政策和监管解释仍是 ML/system/application 层问题。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | `zero-knowledge-proofs/proof-systems/zk-snarks` | succinct verification, zero-knowledge hiding, commitments, sumcheck/lookup-style proof engineering | proof-system family / problem |
| [[verifiable-inference|Verifiable inference]] | `zero-knowledge-proofs/zkml/verifiable-inference` | proof that a model output follows from specified input and committed model while preserving selected privacy | zkML problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | zk-SNARK/proof-system techniques are applied to ML/CNN/LLM inference correctness | zkCNN §1-§4; zkLLM §1-§6; ZENO §1-§3 | active_seed |
| `verifiable_computation` | verifier checks inference computation without re-executing full model | zkCNN, zkLLM, ZENO and trustless DNN inference protocols/evaluations | active_seed |
| `privacy` | zero-knowledge and commitments hide model parameters/witness tensors; privacy type information can also drive circuit optimization | zkCNN §4; zkLLM security discussion; ZENO §3-§4; Trustless DNN inference §4-§5 | active_seed |
| `implementation_reuse` | sumcheck, GKR, polynomial commitments, lookup/operator arguments, custom gates and GPU/CPU proving are reused or optimized for ML operators | zkCNN §3-§5; zkLLM §3-§8; ZENO §4-§7; Trustless DNN inference §4-§6 | active_seed |

## Transfer Matrix

| From zk-SNARK/proof systems | Transfers to verifiable inference? | How | Boundary |
| --- | --- | --- | --- |
| Soundness | yes | invalid inference relation should fail verification except negligible probability | only for encoded computation relation |
| Zero knowledge | yes | hides committed weights and private witness tensors | does not hide public architecture or public prompt/output |
| Succinct verification | yes | verifier checks short proof instead of full LLM execution | prover cost remains high |
| Commitments | yes | bind model parameters before inference proof | does not prove model provenance or ownership |
| Sumcheck/tensor arithmetic | yes | verifies matrix multiplications, tensor relations and CNN layer checks | non-arithmetic operators need lookup/gadgets/approximation |
| FFT/convolution sumcheck | yes | verifies CNN convolution layers through FFT/Hadamard/IFFT relations | convolution-specific route; does not cover attention/normalization |
| GKR layer composition | yes | composes arithmetic layer checks and fan-in/inner-product gates | still needs commitment openings, ZK masking and numeric encoding |
| Lookup arguments | yes | verify activation, normalization, Softmax-related functions via tables/decomposition | table size and quantization errors are system-specific |
| GPU proving | partially | makes large tensor proof generation feasible in reported setup | hardware/backend-specific, not a proof-system guarantee |
| Privacy/tensor type information | yes | preserves public/private and tensor/layer semantics so the compiler can choose cheaper proof encodings | assumes annotations are correct and source program semantics are preserved |
| Privacy-adaptive circuit generation | yes | replaces private-private scalar constraints with cheaper public/private linear-combination encodings where one operand is public | only applies when privacy types expose public operands |
| Packed low-bit equality / knit encoding | yes | batches multiple low-bit dot-product checks into one finite-field equality | depends on bit-width bounds and overflow avoidance |
| Tensor-aware circuit IR and scheduling | yes | treats dot products and layers as structured operators rather than scalar gates | does not remove non-arithmetic gadget costs such as ReLU |
| NN-centric reuse and fusion | partially | caches frequent public operand pairs, shares batch constraints and fuses injective layers | workload/profile-specific and not a generic SNARK property |
| Plonkish custom gates | yes | encode quantized DNN dot products and additions more directly in Halo2-style circuits | backend/layout-specific and does not remove prover cost |
| Lookup nonlinearities | yes | verify activation, rescaling and clipping through lookup arguments rather than pure arithmetic gates | table size, fixed-point semantics and rounding policy are source-specific |
| Sampling and escrow protocols | partially | combine ZK prediction proofs with random contesting and economic penalties for MLaaS verification | viability depends on economic assumptions, timeouts and deployment rules, not just SNARK soundness |

## Non-Transfer Boundary

- Verifiable inference does not prove how the model was trained.
- It does not prove training data legality, copyright compliance, fairness, alignment or safety.
- It does not certify that a generated answer is true; it certifies relation to a committed model.
- It does not eliminate model-owner operational costs; proving can still require large GPU resources.
- It does not remove numeric/quantization assumptions.
- It does not make a semi-honest verifier model automatically safe against all malicious behavior.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] Abstract/§1 | LLM inference proof goal and model-parameter privacy | source-authored novelty framing |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]] Abstract/§1 | CNN prediction/accuracy proof goal and model-parameter privacy | source-authored system framing |
| zkCNN §3 | FFT/convolution sumcheck and CNN operator proof route | convolution-specific and quantization-dependent |
| zkCNN §4 | Commit/Prove/Verify, generalized GKR, ReLU/max pooling gadgets | public architecture and secret weights setting |
| zkCNN §5 | LeNet/VGG/VGG16 benchmarks and vCNN/ZEN comparison | hardware/backend-specific evidence |
| zkLLM §3-§4 | sumcheck, commitment and tensor lookup proof machinery | implementation choices are source-specific |
| zkLLM §5 | attention-specific proof route | depends on quantization and approximation |
| zkLLM §6-§7 | Commit/Prove/Verify protocol, security and complexity | semi-honest verifier and committed-model scope |
| zkLLM §8 | OPT/LLaMa-2 benchmarks up to 13B parameters | hardware/backend-specific evidence |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]] Abstract/§1 | zkSNARK NN performance bottleneck and type-preserving optimization goal | source-authored system framing |
| ZENO §3-§4 | `zkTensor` language construct, privacy-adaptive circuits and knit encoding | depends on privacy annotations and bit-width assumptions |
| ZENO §5-§6 | tensor circuit IR, scheduler, cache, batch sharing and fusion | source-specific compiler/runtime design |
| ZENO §7 | up to 8.5x end-to-end speedup and VGG16 proof-time reduction from 398s to 48s | CPU/backend/dataset-specific evaluation |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] Abstract/§1 | MLaaS / trustless DNN inference proof goal and ImageNet-scale claim | source-authored novelty framing |
| Trustless DNN inference §4 | Halo2 custom gates, lookup nonlinearities, fixed-point quantization, sub-circuit reuse and Poseidon commitments | MobileNet/ImageNet and Halo2-specific construction |
| Trustless DNN inference §5 | accuracy verification, prediction verification and trustless retrieval protocols | sampling/escrow viability assumptions are outside pure proof-system security |
| Trustless DNN inference §6 | MobileNet proving/verification/proof-size benchmarks and prior-work comparison | hardware and cost estimates are source-specific |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[zkml|zkML]] | Attach zkCNN, zkLLM and ZENO as representative inference sources | done |
| [[verifiable-inference|Verifiable inference]] | Add CNN, LLM and type-preserving zkNN optimization routes without splitting system names into concepts | done |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | Add method-family node for reusable tensor/operator/compiler routes surfaced by zkCNN, zkLLM and ZENO | done |
| [[zk-snarks|zk-SNARKs]] | Add verifiable ML inference as source extension, not foundation replacement | done |
| [[zero-knowledge-proofs|Zero-knowledge proofs]] | Add zkML as domain child route | done |
| [[verifiable-inference|Verifiable inference]] | Add Halo2/Plonkish ImageNet-scale DNN route and MLaaS protocol evidence from trustless DNN inference | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zk-snarks | applies_to | nahida-knowledge-zkml-verifiable-inference | zkCNN §1-§5; zkLLM §1-§8; ZENO §1-§7 | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | depends_on | nahida-knowledge-zk-snarks | zkCNN, zkLLM, ZENO and trustless DNN inference proof constructions | medium | active_seed |
| nahida-knowledge-zkml-zk-friendly-ml-operators | specializes | nahida-knowledge-zkml-verifiable-inference | ZENO §3-§6; zkCNN/zkLLM operator proof routes | medium | active_seed |
| nahida-knowledge-zk-snarks | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-inference | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-inference | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| ZEN/Mystique/ezDPS source absorbed | Calibrate zkCNN/zkLLM/ZENO against additional zkML inference routes | `nahida-update` |
| Type-preserving zkML compiler source absorbed | Decide whether [[zk-friendly-ml-operators|ZK-friendly ML operators]] should split into compiler frontend, operator encoding and runtime scheduling children | `nahida-update` |
| Additional Halo2/Plonkish zkML source or repository absorbed | Decide whether Plonkish DNN arithmetization deserves a child node or stays route-level | `nahida-update` / `nahida-github-repo-analyze` |
| Proof of training/unlearning source absorbed | Decide whether to create sibling zkML problem nodes | `nahida-update` |
| zkLLM repository analyzed | Add implementation architecture without duplicating paper details | `nahida-github-repo-analyze` |
| Floating-point ZKML source absorbed | Decide whether to bridge [[floating-point-snarks|Floating-point SNARKs]] to verifiable inference | `nahida-update` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Created bridge from zk-SNARK/proof-system machinery to zkML verifiable inference using zkLLM as first source-backed transfer. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Added zkCNN as CNN inference/accuracy proof evidence and calibrated bridge beyond LLM-only route. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zeno-verifiable-inference | Added ZENO as type-preserving zkNN optimization evidence and linked the bridge to ZK-friendly ML operators. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs | Added trustless DNN inference as Halo2/Plonkish ImageNet-scale evidence for SNARK-backed zkML inference and MLaaS protocols. | 1 source note | codex |
