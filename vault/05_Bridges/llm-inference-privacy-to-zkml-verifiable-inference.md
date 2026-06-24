---
id: "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
title: "LLM inference privacy -> zkML verifiable inference"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "llm-inference-privacy"
  - "verifiable-inference"
  - "zkml"
endpoint_knowledge_refs:
  - "nahida-knowledge-llm-inference-privacy"
  - "nahida-knowledge-zkml-verifiable-inference"
endpoint_paths:
  - "ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy"
  - "zero-knowledge-proofs/zkml/verifiable-inference"
relation_types:
  - "contrast"
  - "complementary"
  - "trust_boundary"
  - "privacy_boundary"
directionality: "bidirectional"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
representative_source_refs:
  - "doi:10.1109/TIFS.2026.3667458"
  - "doi:10.1145/3658644.3670334"
  - "arxiv:2210.08674"
query_keys:
  - "LLM inference privacy versus verifiable inference"
  - "prompt privacy versus model correctness"
  - "privacy-preserving LLM inference"
  - "ZK verifiable inference prompt privacy boundary"
  - "Rap-LI and zkLLM boundary"
aliases:
  - "prompt privacy vs verifiable inference"
domains:
  - "ml-systems"
  - "zero-knowledge-proofs"
topics:
  - "llm-inference-privacy"
  - "privacy-and-trustworthy-ml"
  - "zkml"
  - "verifiable-inference"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-risk-aware-llm-inference-privacy"
source_refs:
  - "doi:10.1109/TIFS.2026.3667458"
  - "doi:10.1145/3658644.3670334"
  - "arxiv:2210.08674"
confidence: "medium"
trust_tier: "primary"
---

# LLM inference privacy -> zkML verifiable inference

## 关系命题

LLM inference privacy 和 zkML verifiable inference 都处理“用户/客户把输入交给模型推理时能否信任系统”的问题，但二者保护的资产和保证完全不同。

LLM inference privacy 关注 user prompt 在发送给 cloud/black-box LLM 前是否泄露 PII、敏感上下文或个人属性。Rap-LI 的路线是在用户侧做 risk-aware LDP text sanitization，让服务提供者/API adversary 更难看到或推断原始 prompt。

zkML verifiable inference 关注某个 output 是否由指定 input 和 committed model 正确计算得到，并在需要时隐藏 model weights 或 witness。zkLLM/trustless DNN inference 的核心是 computation correctness、commitment binding、succinct verification 和 selected witness hiding。

因此，这条 bridge 的作用是防混淆: prompt privacy 不能推出 inference correctness；verifiable inference 也不能自动保护 prompt PII，尤其当 prompt/output 是 public statement 时。

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[llm-inference-privacy|LLM inference privacy]] | `ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy` | user-side prompt protection, PII/contextual leakage, text sanitization, local DP, privacy-preserving prompt engineering | ML systems problem |
| [[verifiable-inference|Verifiable inference]] | `zero-knowledge-proofs/zkml/verifiable-inference` | proof that output follows from specified input and committed model while hiding selected weights/witness | zkML problem |

## 关系类型

| Relation type | Meaning | Evidence | Status |
| --- | --- | --- | --- |
| `contrast` | Same broad LLM inference setting, different threat model and guarantee. | Rap-LI §I/§IV; zkLLM source note; trustless DNN inference source note | active_seed |
| `complementary` | A production system might need both prompt privacy and output correctness. | Inference trust boundary comparison | candidate |
| `trust_boundary` | Rap-LI assumes black-box provider; zkML inference assumes prover/verifier/proof statement and committed model. | Rap-LI §I; verifiable inference node | active_seed |
| `privacy_boundary` | Prompt sanitization hides user input; ZK hides weights/witness only if encoded as private. | Rap-LI §V; zkLLM/verifiable inference node | active_seed |

## Transfer Matrix

| Capability | Transfers between endpoints? | How | Boundary |
| --- | --- | --- | --- |
| Prompt PII protection | no automatic transfer from verifiable inference | ZK systems can make inputs private only if the statement/protocol is designed that way. | Many zkML inference sources use public prompt/input/output. |
| Model-output correctness | no transfer from prompt sanitization | Rap-LI perturbs prompt before calling the model; it does not prove the model executed correctly. | Sanitized input can still be answered incorrectly. |
| Model-weight privacy | no transfer from prompt privacy | Rap-LI does not protect model owner assets. | ZK/commitment route required. |
| User-side deployability with black-box APIs | transfers only from LLM inference privacy side | Rap-LI needs no server cooperation. | Verifiable inference needs proof-generation/verification support. |
| Formal privacy guarantee | partial but distinct | Rap-LI gives LDP for sanitized text; ZK gives zero-knowledge for encoded witness. | Different adversary, adjacency and leakage definitions. |
| Utility/semantic preservation | shared concern | Prompt perturbation can degrade downstream task utility; ZK inference can preserve exact encoded relation. | ZK exactness depends on quantization/encoding; prompt privacy depends on sanitization quality. |

## Non-Transfer Boundary

- Rap-LI does not prove training provenance, model integrity, inference correctness, fairness, safety or output truthfulness.
- zkML verifiable inference does not automatically hide prompt PII from service provider or verifier.
- A ZK proof with public prompt/output can still reveal sensitive prompt content.
- A sanitized prompt can still leak context through preserved low-risk tokens or utility-preserving substitutions.
- Combining the two would require explicit protocol design: private input commitments, local sanitization policy, proof statement, output policy, logging/retention and user-facing recovery must all be specified.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Risk-Aware Privacy Preservation for LLM Inference]] Abstract/§I/§IV/§V | User-side prompt PII/contextual privacy and risk-aware LDP route | Text-only; NER dependency; no model correctness proof |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] source note | LLM inference correctness proof with committed model and model-parameter hiding | Public architecture/prompt/output; semi-honest verifier |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] source note | MLaaS prediction verification and trustless inference protocol evidence | Quantized/fixed-point model semantics; sampling/escrow assumptions |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[llm-inference-privacy|LLM inference privacy]] | Create problem node and attach bridge to verifiable inference boundary. | done |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | Add LLM prompt privacy as child route and source extension. | done |
| [[verifiable-inference|Verifiable inference]] | Add bridge note clarifying prompt privacy non-transfer. | done |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-llm-inference-privacy | contrasted_with | nahida-knowledge-zkml-verifiable-inference | Rap-LI source note; verifiable inference node | medium | active_seed |
| nahida-knowledge-zkml-verifiable-inference | contrasted_with | nahida-knowledge-llm-inference-privacy | bridge note | medium | active_seed |
| nahida-knowledge-llm-inference-privacy | bridges_to | nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference | bridge note | medium | active_seed |
| nahida-knowledge-zkml-verifiable-inference | bridges_to | nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference | bridge note | medium | active_seed |

## Refresh Triggers

| Trigger | Why | Suggested action |
| --- | --- | --- |
| Private-input zkML inference source absorbed | Could turn contrast into a construction bridge that protects both prompt and inference correctness. | `nahida-update` |
| Cryptographic private LLM inference source absorbed | Need compare HE/MPC/TEE/private input route with text sanitization route. | `nahida-update` |
| Prompt privacy survey absorbed | May split privacy-preserving prompt engineering into a foundation node. | `nahida-research-search` |
| Rap-LI repository analyzed | Could add implementation architecture and deployment boundary. | `nahida-github-repo-analyze` |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-risk-aware-llm-inference-privacy | Created boundary bridge between LLM prompt privacy and zkML verifiable inference during Rap-LI absorption. | 1 new source note + existing zkML sources | codex |
