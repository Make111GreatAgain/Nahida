---
id: "iacr-eprint-2021-777"
title: "Asynchronous Data Dissemination and its Applications"
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
  - "p1-p3 abstract, introduction, ADD motivation, applications and contribution table"
  - "p3-p6 system model, Reed-Solomon preliminaries, online error correction and ADD definition"
  - "p6-p8 ADD protocol, reconstruction, high-threshold variant and analysis"
  - "p8-p10 ADD-based reliable broadcast and long-message RBC analysis"
  - "p10-p13 AVSS, ACSS and dual-threshold ACSS constructions"
  - "p13-p14 communication lower bounds for DD, RBC, AVSS, ACSS and ACSS*"
  - "p14-p17 related work, discussion, concrete constants and appendix"
canonical_url: "https://eprint.iacr.org/2021/777"
pdf_url: "https://eprint.iacr.org/2021/777.pdf"
doi: ""
arxiv_id: ""
venue: "IACR ePrint 2021/777 inferred from local filename; local PDF uses ACM acmart metadata"
year: "2021"
authors:
  - "Sourav Das"
  - "Zhuolun Xiang"
  - "Ling Ren"
affiliations:
  - "University of Illinois at Urbana-Champaign"
local_pdf: "~/Desktop/paper/2021-777.pdf"
sha256: "15dfe25db85fe91b69aeedfd2b8a47fd087bbc9b8e28232ea50521f0fb9817ef"
pages: 17
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/asynchronous-data-dissemination-and-its-applications-15dfe25db85f-pages.txt"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-data-dissemination"
  - "asynchronous-reliable-broadcast"
  - "asynchronous-verifiable-secret-sharing"
  - "asynchronous-distributed-key-generation"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-data-dissemination"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-data-dissemination/iacr-eprint-2021-777"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast/iacr-eprint-2021-777"
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/iacr-eprint-2021-777"
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation/iacr-eprint-2021-777"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
    - "blockchain-systems"
  directions:
    - "consensus"
  topics:
    - "asynchronous-data-dissemination"
    - "asynchronous-reliable-broadcast"
    - "asynchronous-verifiable-secret-sharing"
    - "asynchronous-complete-secret-sharing"
    - "asynchronous-distributed-key-generation"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous data dissemination"
  - "ADD"
  - "reliable broadcast"
  - "RBC"
  - "AVSS"
  - "ACSS"
  - "dual-threshold ACSS"
  - "ADKG communication complexity"
aliases:
  - "ADD"
  - "Asynchronous Data Dissemination"
  - "long-message reliable broadcast"
  - "ADD-based RBC"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "asynchronous BFT consensus"
    - "broadcast and dissemination primitives"
  problem:
    - "disseminate a long message to all honest nodes when at least t+1 honest nodes initially hold it"
    - "reduce long-message reliable broadcast communication without trusted setup"
    - "reduce communication for AVSS, ACSS, dual-threshold ACSS and ADKG"
  method_family:
    - "Reed-Solomon coded data dissemination"
    - "online error correction"
    - "hash-gated reliable broadcast"
    - "Pedersen-commitment AVSS"
    - "PVSS-based dual-threshold ACSS"
  proof_model:
    - "asynchronous message passing"
    - "Byzantine adversary with t < n/3 for main ADD"
    - "n > 2t high-threshold ADD with collision-resistant hash"
    - "information-theoretic ADD core"
  evaluation_context:
    - "asymptotic communication analysis"
    - "communication lower bounds"
  bridge:
    - "payload dissemination and broadcast primitives for asynchronous blockchain consensus"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260623-asynchronous-data-dissemination"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0082"
safe_for_absorption: true
source_refs:
  - "iacr:2021/777"
  - "sha256:15dfe25db85fe91b69aeedfd2b8a47fd087bbc9b8e28232ea50521f0fb9817ef"
  - "pdf:~/Desktop/paper/2021-777.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "consensus"
secondary_directions:
  - "asynchronous-bft-consensus"
  - "asynchronous-reliable-broadcast"
  - "asynchronous-verifiable-secret-sharing"
  - "asynchronous-distributed-key-generation"
classification_status: "refined_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p17"
  - "Definition 3.1 introduces Asynchronous Data Dissemination as the central primitive"
  - "Algorithm 1 gives an information-theoretic ADD protocol for t<n/3 with O(n|M|+n^2) communication"
  - "Section 4 builds ADD-based long-message RBC with O(n|M|+kappa n^2) communication"
  - "Section 5 applies the RBC/ADD route to AVSS, ACSS and dual-threshold ACSS"
  - "classification refined from distributed-systems/consensus/needs-review to asynchronous-data-dissemination under async BFT"
metadata_notes:
  - "Canonical ePrint URL inferred from local filename `2021-777.pdf` and PDF identity; no web fetch was performed in this run."
  - "Local PDF metadata title was accurate, but authors were recovered from p1 because metadata had no author field."
---

# Asynchronous Data Dissemination and its Applications

## Source Identity

- Local file: `~/Desktop/paper/2021-777.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/asynchronous-data-dissemination-and-its-applications-15dfe25db85f-pages.txt`
- True title: `Asynchronous Data Dissemination and its Applications`
- Authors: Sourav Das, Zhuolun Xiang, Ling Ren
- Source identity: `iacr:2021/777` inferred from local filename and paper identity.
- Reading status: deep read complete, p1-p17.

## One-Line Contribution

The paper introduces Asynchronous Data Dissemination (ADD), a long-message dissemination primitive for asynchronous Byzantine networks, and uses it to remove a `log n` communication factor from reliable broadcast, AVSS, ACSS, dual-threshold ACSS and ADKG-related applications.

## Problem Field

This source belongs primarily under [[asynchronous-data-dissemination|Asynchronous data dissemination]], a method/primitive node inside [[asynchronous-bft-consensus|Asynchronous BFT consensus]].

The durable problem is not one concrete blockchain protocol. It is the lower communication layer used by asynchronous consensus and cryptographic setup protocols when a large message or large proof material must become available to all honest nodes.

Secondary fields:

| Field | Why it applies | Boundary |
| --- | --- | --- |
| [[asynchronous-reliable-broadcast|Asynchronous reliable broadcast]] | ADD turns long-message RBC into hash broadcast plus coded dissemination. | Classic Bracha RBC lineage still needs direct source coverage. |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | The paper improves AVSS, ACSS and dual-threshold ACSS communication using improved RBC plus new sharing techniques. | It is one communication-efficient route, not the entire AVSS taxonomy. |
| [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] | ADKG protocols that use many RBC instances inherit the improved long-message RBC cost. | It does not replace ADKG setup protocols. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | Long-message dissemination is relevant to blocks, batches and asynchronous atomic broadcast. | It does not solve mempool policy, data availability sampling, validator economics or execution. |

## Section Map

| Pages | Content | Notes |
| --- | --- | --- |
| p1-p3 | Abstract, introduction and contribution table | ADD problem, RBC/AVSS/ACSS/ADKG improvements. |
| p3-p4 | Model and preliminaries | Asynchronous message passing, Byzantine faults, Reed-Solomon encoding and online error correction. |
| p4-p6 | ADD definition and main protocol | `t+1` honest initial holders, RS symbols, `t+1` matching symbol acceptance and OEC reconstruction. |
| p6-p8 | Analysis and high-threshold ADD | Main `t<n/3` information-theoretic ADD plus `n>2t` hash-assisted variant. |
| p8-p10 | Reliable broadcast | Bracha RBC on hash plus ADD on payload; four-round variant. |
| p10-p13 | AVSS, ACSS and dual-threshold ACSS | Pedersen commitments, encrypted shares, PVSS and NIZK routes. |
| p13-p14 | Lower bounds | DD/RBC lower bounds `Omega(n|M|+n^2)` and AVSS/ACSS lower bounds `Omega(n^2)`. |
| p14-p17 | Related work, discussion and appendix | Concrete constants, computation caveats, merged RBC details. |

## Core Claims

| Claim | Evidence | Scope |
| --- | --- | --- |
| ADD is solvable when at least `t+1` honest nodes initially hold the same message. | Definition 3.1 and Algorithm 1. | Main protocol assumes `n=3t+1`; high-threshold variant changes assumptions. |
| The main ADD protocol costs `O(n|M|+n^2)` communication. | Theorem 3.5. | Information-theoretic core; useful for messages at least `Omega(n log n)` bits. |
| ADD-based RBC costs `O(n|M|+kappa n^2)` with collision-resistant hashes. | Section 4 and Theorem 4.7. | Improves prior `O(n|M|+kappa n^2 log n)` long-message RBC under the same hash setting. |
| Improved RBC lowers async atomic broadcast and ADKG communication from `O(kappa n^3 log n)` to `O(kappa n^3)` when they run `O(n)` RBC instances on `O(kappa n)` messages. | Section 4.2. | This is an application-level asymptotic consequence, not a new ADKG protocol. |
| AVSS, ACSS and dual-threshold ACSS can reach `O(kappa n^2)` communication without trusted setup. | Section 5 and contribution table. | Uses cryptographic assumptions for complete/dual-threshold variants. |

## Mechanism Notes

### ADD

ADD asks all honest nodes to eventually output `M`, assuming at least `t+1` honest nodes initially hold `M`. The `t+1` threshold is necessary: below it, a receiver cannot distinguish honest senders from malicious claimants.

The protocol uses Reed-Solomon coding. Each sender encodes `M` into `n` symbols and sends symbol `m_j` to node `j`; node `j` accepts a symbol after seeing `t+1` identical `DISPERSE` messages. Nodes then broadcast their accepted reconstruction symbols. Online error correction decodes once enough symbols agree with a degree-`t` polynomial.

The result is a separation between payload movement and all-to-all control traffic: only coded pieces of the long message move along `O(n)` total payload paths, while the Byzantine consistency checks consume `O(n^2)` small messages.

### Reliable Broadcast

The paper uses ADD to build long-message RBC by broadcasting only a hash with Bracha RBC, then running ADD on the payload when the hash is accepted. The hash RBC ensures that at least `t+1` honest nodes start ADD with the same message and no honest node starts ADD with a different message.

This changes long-message RBC from Merkle-path-heavy dissemination to hash-plus-coded dissemination. The consequence is the removal of the `log n` factor in prior AVID-style constructions, at the cost of relying on collision-resistant hash functions for RBC.

### AVSS, ACSS And Dual-Threshold ACSS

AVSS uses Pedersen polynomial commitments with improved RBC to communicate commitments and enough share material at `O(kappa n^2)` communication.

ACSS strengthens AVSS by requiring completeness: if any honest node completes sharing, every honest node eventually obtains a share on a degree-`t` polynomial. The paper uses encrypted shares and a recovery path so missing shares can be delivered without trusting the dealer.

Dual-threshold ACSS separates the sharing fault threshold `t` from the reconstruction secrecy threshold `l`. It uses PVSS and NIZK proofs so encrypted shares are publicly verifiable; this supports stronger secrecy thresholds with `l < n-t`.

## Why This Is Knowledge, Not Just A Paper Summary

This paper adds a reusable communication layer to the knowledge base:

- Below it are source details: exact ADD pseudocode, OEC checks, hash-assisted high-threshold variant, AVSS/ACSS proof structure and constants.
- At its layer are [[asynchronous-data-dissemination|Asynchronous data dissemination]] and [[asynchronous-reliable-broadcast|Asynchronous reliable broadcast]].
- Above it are [[asynchronous-bft-consensus|Asynchronous BFT consensus]], [[asynchronous-verifiable-secret-sharing|AVSS]], [[asynchronous-distributed-key-generation|ADKG]] and asynchronous blockchain consensus bridge notes.

## Limits And Caveats

- ADD is a communication primitive, not a full consensus or blockchain protocol.
- Main ADD is information-theoretic for `t<n/3`; the high-threshold variant uses collision-resistant hashes and has worse dependence on `n-2t`.
- ADD improves communication but increases coding/decoding computation. The discussion notes that malicious nodes can force multiple decoding attempts.
- The RBC improvement uses collision-resistant hashes; the paper's pure ADD core and RBC application have different assumptions.
- The paper improves asymptotic communication for ADKG-style protocols through improved RBC, but does not replace the ADKG logic itself.
- Canonical ePrint identity was inferred locally; no external web verification was performed in this run.

## Absorption Decisions

| Target note | Action | Reason |
| --- | --- | --- |
| [[asynchronous-data-dissemination|Asynchronous data dissemination]] | create | ADD is a reusable primitive/problem field introduced by this paper and useful beyond the source instance. |
| [[asynchronous-reliable-broadcast|Asynchronous reliable broadcast]] | create | RBC is already referenced across VABA, EPIC, Cobalt and AVSS notes; this source supplies a direct long-message RBC route. |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | update | Adds a broadcast/data-dissemination layer below ACS, VABA, AVSS and ADKG. |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | update | Adds communication-efficient AVSS/ACSS/dual-threshold ACSS route. |
| [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] | update | Records the inherited `O(kappa n^3)` communication improvement from long-message RBC. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | update | Adds transfer boundary for payload dissemination and long-message RBC. |

## Retrieval Hooks

- Query keys: `ADD`, `asynchronous data dissemination`, `long-message RBC`, `asynchronous reliable broadcast`, `Bracha RBC with ADD`, `AVSS communication complexity`, `ACSS`, `dual-threshold ACSS`, `ADKG communication O(kappa n^3)`.
- Best first hop: [[asynchronous-data-dissemination|Asynchronous data dissemination]].
- Best comparison: [[asynchronous-reliable-broadcast|Asynchronous reliable broadcast]] for RBC, [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] for AVSS/ACSS and [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] for ADKG consequences.

## Update Log

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-asynchronous-data-dissemination | Deep-read local PDF, refined queue classification, created source note and propagated into Source + Knowledge + Bridge architecture. | codex |
