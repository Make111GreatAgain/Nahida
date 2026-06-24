---
id: "nahida-bridge-verifiable-computation-systems-to-contingent-service-payments"
title: "Verifiable computation systems -> contingent service payments"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
domain_id: "verifiable-computation"
direction_id: "verifiable-computation-systems"
topic_ids:
  - "verifiable-computation-systems"
  - "contingent-service-payments"
  - "verifiable-services"
endpoint_knowledge_refs:
  - "nahida-knowledge-verifiable-computation-systems"
  - "nahida-knowledge-contingent-service-payments"
endpoint_paths:
  - "verifiable-computation/verifiable-computation-systems"
  - "blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments"
relation_types:
  - "dependency"
  - "application"
  - "payment_finality_boundary"
  - "trust_model_shift"
directionality: "one_way"
maturity: "active_seed"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
representative_source_refs:
  - "arxiv:2208.00283v2"
query_keys:
  - "verifiable service payment"
  - "verifiable computation contingent payment"
  - "RC-S-P VSID"
  - "proof of retrievability payment"
aliases:
  - "Verifiable services to payment protocols"
  - "VC systems to contingent service payment"
domains:
  - "verifiable-computation"
  - "blockchain-systems"
topics:
  - "verifiable-computation-systems"
  - "contingent-service-payments"
  - "fair-exchange-protocols"
tags:
  - "nahida/bridge"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
source_refs:
  - "arxiv:2208.00283v2"
confidence: "medium"
trust_tier: "primary"
---

# Verifiable computation systems -> contingent service payments

## 关系命题

Verifiable computation / verifiable service systems can be used as the service-correctness layer of contingent service payments: they tell a client whether a delegated service proof is valid, while blockchain fair-exchange protocols decide deposits, dispute economics, proof-status privacy and final coin distribution.

The bridge is one-way. A verifiable service proof does not by itself imply payment fairness; a smart contract payment protocol does not by itself prove the service was correctly performed.

## Endpoint Scope

| Endpoint | Path | Scope in this bridge | Local definition |
| --- | --- | --- | --- |
| [[verifiable-computation-systems|Verifiable computation systems]] | `verifiable-computation/verifiable-computation-systems` | outsourced computation/service correctness, proof verification, source-local VS/VSID abstraction | a system layer that lets a verifier check delegated computation or service results |
| [[contingent-service-payments|Contingent service payments for verifiable services]] | `blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | recurring payment, escrow, refund, dispute and privacy for verifiable services | fair exchange of service proofs and digital coins |

## Transfer Matrix

| From verifiable service systems | Transfers to service payment? | How | Boundary |
| --- | --- | --- | --- |
| Proof of correct service execution/storage | yes | client or arbiter can evaluate service proof validity before paying or refunding | payment finality and deposits are not part of the proof system |
| Public/private verification keys | yes | RC-S-P encrypts/pads proofs and may reveal keys to arbiter after private time bubble | key release can leak proof status after the privacy window |
| Input well-formedness proof | yes, if upgraded to VSID | server can reject malformed metadata/query from malicious client before serving | ordinary VS definitions often assume honest client |
| Identifiable abort | yes | arbiter maps invalid metadata/query to client and invalid service proof to server | requires extra protocol machinery: NIZK/signatures/bulletin board or service-specific shortcuts |
| PoR Merkle proof-of-misbehavior | yes | one invalid path can prove server misbehavior cheaply | this is PoR-specific; not every VC system has cheap dispute proof |

## Non-Transfer Boundary

- VC soundness says invalid computation/storage proofs are hard to fake; it does not say the server will be paid.
- Fair-exchange escrow says coins will move according to contract state; it does not prove service semantics unless linked to a VS/VSID proof.
- Proof-status privacy is a protocol-layer property: encryption, padding, private time bubble and delayed dispute matter even when the service proof itself is sound.
- Malicious-client security often requires strengthening a service scheme. A PoR secure against malicious servers does not automatically protect an honest server from malformed client metadata.
- Smart-contract-as-arbiter is only viable when the dispute proof is cheap enough for on-chain execution.

## Evidence Set

| Evidence | Supports | Caveat |
| --- | --- | --- |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|RC-S-P]] §7 | RC-S-P formalizes recurring fair payment around functions `F,M,E,D,Q` and proof/query phases. | single direct source for this bridge |
| RC-S-P Appendix E | VS covers PoR, provable data possession, verifiable computation, searchable encryption and information retrieval. | local vault still lacks a dedicated `verifiable services` foundation node |
| RC-S-P Appendix F | VSID adds identifiable abort and client input well-formedness. | generic route may need NIZK and signatures |
| RC-S-P §9 | RC-PoR-P avoids generic ZK by using Merkle PoR and proof-of-misbehavior. | PoR-specific shortcut |
| RC-S-P §10 / Appendix M | performance separates off-chain proof work from constant smart-contract coin transfer. | prototype/private-chain measurement |

## Endpoint Updates Required

| Endpoint | Update | Status |
| --- | --- | --- |
| [[verifiable-computation-systems|Verifiable computation systems]] | Add VS/VSID as service-payment-facing route and RC-S-P as source extension. | done |
| [[contingent-service-payments|Contingent service payments for verifiable services]] | Created child problem node and made this bridge its primary cross-domain relation. | done |
| [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] | Promote service-payment variants from watching to active child. | done |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| service proof validity | `verifiable-computation/verifiable-computation-systems` | `blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | dependency | RC-S-P §7, Appendix E | mistaking proof validity for payment fairness |
| identifiable abort | VC/VSID abstraction | service payment disputes | trust_model_shift | RC-S-P Appendix F | ordinary VC schemes may not expose client misbehavior |
| proof-status privacy | service proof transcript | fair-exchange payment protocol | application boundary | RC-S-P §8/G.1 | privacy window eventually opens |
| PoR misbehavior proof | PoR/Merkle service proof | smart-contract-friendly dispute | implementation reuse | RC-S-P §9 | specific to Merkle-like proofs |

## 查询入口

- 可验证计算的 proof 怎么和链上付款分层?
- 为什么 PoR secure against server 不足以做服务付款?
- VSID 解决了 RC-S-P 的哪个威胁模型问题?
- Smart contract 什么时候能替代 fair-exchange arbiter?

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-recurring-contingent-service-payment | Created bridge from RC-S-P absorption. | arxiv:2208.00283v2 | codex |
