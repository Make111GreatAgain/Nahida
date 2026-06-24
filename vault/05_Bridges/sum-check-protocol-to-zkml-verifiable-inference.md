---
id: "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
title: "Sum-check protocol -> zkML verifiable inference"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "sum-check-protocol"
  - "zkml"
  - "verifiable-inference"
  - "cnn-inference-proofs"
endpoint_knowledge_refs:
  - "nahida-knowledge-sum-check-protocol"
  - "nahida-knowledge-zkml-verifiable-inference"
endpoint_paths:
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/zkml/verifiable-inference"
relation_types:
  - "application"
  - "method_transfer"
  - "verifiable_computation"
  - "operator_proving"
  - "implementation_reuse"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
representative_source_refs:
  - "doi:10.1145/3460120.3485379"
query_keys:
  - "sumcheck for verifiable inference"
  - "convolution sumcheck"
  - "FFT sumcheck"
  - "zkCNN"
  - "CNN inference proof"
aliases:
  - "sumcheck-based zkML inference"
  - "structured operator proving for zkML"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "sum-check-protocol"
  - "zkml"
  - "verifiable-inference"
  - "cnn-inference-proofs"
  - "fft-convolution-sumcheck"
tags:
  - "nahida/bridge"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
source_refs:
  - "doi:10.1145/3460120.3485379"
confidence: "high"
trust_tier: "primary"
---

# Sum-check protocol -> zkML verifiable inference

## 关系命题

Sum-check protocol 可以作为 zkML verifiable inference 的结构化算子证明工具: 对 CNN、LLM 或其他 ML 模型中的线性代数和 tensor relations，prover 不必总是展开完整 arithmetic circuit，而可以把运算写成多项式求和关系，再用 sumcheck/GKR route 证明 output 与 committed model/input 一致。

zkCNN 是当前 bridge 的 source-backed seed。它把 FFT 和 2-D convolution 写成可 sumcheck 的 relation，从而让 CNN convolution layer proof 以 `O(n^2)` 额外 prover time 和 polylog proof/verifier overhead 接入完整 ZK inference protocol。

这条 bridge 不表示 sumcheck 本身已经提供完整 zkML 系统。模型 commitment、zero knowledge、non-interactivity、numeric quantization、非线性 operator、architecture privacy 和 end-to-end protocol assembly 都需要额外 proof-system 组件和 source-specific 设计。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[sum-check-protocol|Sum-check protocol]] | `verifiable-computation/interactive-proofs/sum-check-protocol` | low-cost verification of polynomial-sum relations, including specialized FFT/convolution relations | interactive proof / method |
| [[verifiable-inference|Verifiable inference]] | `zero-knowledge-proofs/zkml/verifiable-inference` | proof that an ML output follows from specified input and committed/known model while preserving selected privacy | zkML problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `application` | sumcheck is applied to ML inference correctness rather than only abstract polynomial claims | zkCNN §3-§4 | active_seed |
| `method_transfer` | Fourier/convolution algebra is translated into sumcheck-friendly MLE relations | zkCNN §3.2-§3.3 | active_seed |
| `verifiable_computation` | verifier checks CNN layer computation without recomputing full convolutional workload | zkCNN protocol/evaluation | active_seed |
| `operator_proving` | CNN operators become proof subroutines: FFT, Hadamard product, IFFT, convolution, matrix multiplication | zkCNN §3-§4 | active_seed |
| `implementation_reuse` | GKR, sumcheck and polynomial commitments are reused in an end-to-end inference proof | zkCNN §4 and Appendix C | active_seed |

## Transfer Matrix

| From sum-check/GKR | Transfers to zkML verifiable inference? | How | Boundary |
| --- | --- | --- | --- |
| Polynomial-sum verification | yes | proves layer/operator relations over multilinear extensions | only after ML operation is encoded as a field relation |
| Random challenge reduction | yes | reduces high-dimensional tensor relation to point evaluations and commitment openings | challenge soundness does not define model/privacy policy |
| FFT-specific sumcheck | yes | validates FFT/IFFT relation used in convolution proof | depends on roots of unity, vectorization and field backend |
| Convolution sumcheck | yes | validates 2-D convolution through FFT/Hadamard/IFFT subrelations | optimized for convolutional layers, not all ML operators |
| GKR layer composition | yes | composes arithmetic layer checks and generalized fan-in gates | non-arithmetic functions still need gadgets/lookup/bit decomposition |
| Zero knowledge | partially | ZK sumcheck can hide messages/witness when combined with masking and PC | plain sumcheck alone is not a full ZK argument system |

## Non-Transfer Boundary

- Sumcheck does not by itself provide model commitment, non-interactivity or polynomial commitment openings.
- Sumcheck proves encoded finite-field relations; it does not guarantee floating-point semantics unless the encoding is separately justified.
- A convolution proof route does not automatically cover attention, normalization, Softmax, training, aggregation or model update provenance.
- Verifiable inference still needs a threat model: what is public, what is committed, what is hidden, and what statement the verifier checks.
- Performance numbers are source-specific and depend on CNN structure, quantization, curve/backend, hardware and memory.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]] Abstract/§1 | CNN prediction and accuracy proof goal with private model parameters | source-authored system claim |
| zkCNN §3.2 | FFT sumcheck: linear extra prover time and logarithmic/polylog verification route | assumes FFT-friendly field/backend |
| zkCNN §3.3 | 2-D convolution verification via FFT/Hadamard/IFFT sumchecks | convolution-specific algebraic route |
| zkCNN §4.2 | generalized GKR gates and arbitrary-layer inputs for CNN proof assembly | engineering choices are source-specific |
| zkCNN §4.3 / Appendix C | Commit/Prove/Verify, ZK argument, PC openings, Fiat-Shamir | full system needs components beyond sumcheck |
| zkCNN §5 | VGG/LeNet benchmarks and vCNN/ZEN comparison | hardware, memory and implementation dependent |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[sum-check-protocol|Sum-check protocol]] | Add FFT/convolution sumcheck as source extension and bridge link | done |
| [[verifiable-inference|Verifiable inference]] | Add CNN inference route alongside LLM route | done |
| [[zkml|zkML]] | Update inference route to include CNN-era source evidence | done |
| [[zk-snarks|zk-SNARKs]] | Record zkCNN as application/proof-engineering evidence, not foundation evidence | done |

## Relation Edges

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-sum-check-protocol | applies_to | nahida-knowledge-zkml-verifiable-inference | zkCNN §3-§4 | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | depends_on | nahida-knowledge-sum-check-protocol | zkCNN FFT/convolution and GKR proof route | high | active_seed |
| nahida-knowledge-sum-check-protocol | bridges_to | nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference | bridge note | high | active_seed |
| nahida-knowledge-zkml-verifiable-inference | bridges_to | nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference | bridge note | high | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| ZEN/Mystique/ezDPS or other CNN/NN zkML sources absorbed | Compare whether convolution/operator proving generalizes or remains zkCNN-specific | `nahida-update` |
| LLM/transformer operator proof sources absorbed | Decide whether to split a broader `ZK-friendly ML operators` method node | `nahida-knowledge-get` |
| Canonical GKR/FFT proof sources absorbed | Strengthen endpoint foundation and separate source-specific engineering from general method | `nahida-research-search` |
| Floating/fixed-point zkML source absorbed | Bridge numeric semantics into operator proof routes | `nahida-update` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Created bridge from sum-check/GKR method layer to zkML verifiable inference using zkCNN as first source-backed CNN operator proof route. | 1 source note | codex |
