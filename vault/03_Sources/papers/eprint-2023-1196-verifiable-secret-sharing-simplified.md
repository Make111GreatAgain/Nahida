---
id: "iacr-eprint-2023-1196"
title: "Verifiable Secret Sharing Simplified"
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
  - "p1-p3 abstract, introduction, problem statement, VSS/PVSS/dual-threshold goals"
  - "p3-p5 model, VSS properties, public verifiability, dual-threshold AVSS definition"
  - "p5-p7 synchronous VSS protocol and proof sketch"
  - "p7-p9 asynchronous VSS protocol, degree-2t fix, storage optimization"
  - "p9-p11 dual-threshold asynchronous VSS protocol with verifiable encryption"
  - "p11-p14 implementation, computation benchmarks, geo-distributed evaluation, discussion"
  - "p14-p18 references and appendices for broadcast, Pedersen commitments, VE and secrecy proofs"
canonical_url: "https://eprint.iacr.org/2023/1196"
pdf_url: "https://eprint.iacr.org/2023/1196.pdf"
doi: ""
arxiv_id: ""
venue: "IACR ePrint 2023/1196 inferred from local filename; no web fetch was performed"
year: "2024"
authors:
  - "Sourav Das"
  - "Zhuolun Xiang"
  - "Alin Tomescu"
  - "Alexander Spiegelman"
  - "Benny Pinkas"
  - "Ling Ren"
affiliations:
  - "University of Illinois at Urbana-Champaign"
  - "Aptos Labs"
  - "Bar-Ilan University"
local_pdf: "~/Desktop/paper/2023-1196.pdf"
sha256: "81dd93d12ed1d22f1bb4ea26c6bf2116f27614ab8a6ccbfbe904732c6d069fe6"
pages: 18
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2023-1196-81dd93d12ed1-pages.txt"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-verifiable-secret-sharing"
  - "dual-threshold-asynchronous-vss"
  - "publicly-verifiable-secret-sharing"
  - "asynchronous-reliable-broadcast"
  - "asynchronous-distributed-key-generation"
  - "verifiable-encryption"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/iacr-eprint-2023-1196"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/dual-threshold-asynchronous-vss/iacr-eprint-2023-1196"
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast/iacr-eprint-2023-1196"
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation/iacr-eprint-2023-1196"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
    - "blockchain-systems"
  directions:
    - "consensus"
  topics:
    - "asynchronous-verifiable-secret-sharing"
    - "dual-threshold-asynchronous-vss"
    - "publicly-verifiable-secret-sharing"
    - "asynchronous-reliable-broadcast"
    - "asynchronous-distributed-key-generation"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "VSS"
  - "AVSS"
  - "PVSS"
  - "dual-threshold AVSS"
  - "publicly verifiable transcripts"
  - "verifiable encryption"
  - "Pedersen polynomial commitment"
aliases:
  - "VSS Simplified"
  - "A-VSS"
  - "DtAVSS"
  - "publicly verifiable VSS"
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
    - "secret sharing primitives"
  problem:
    - "make VSS publicly verifiable without complaint-response complexity"
    - "ensure asynchronous termination for VSS when the dealer is faulty"
    - "separate corruption threshold t from secrecy threshold ell in asynchronous VSS"
  method_family:
    - "acknowledgment-transcript VSS"
    - "degree-2t asynchronous VSS"
    - "dual-threshold AVSS with selective verifiable encryption"
    - "Pedersen polynomial commitments with batch openings"
  proof_model:
    - "static Byzantine adversary"
    - "PKI and authenticated private dealer-to-recipient channels"
    - "synchronous network with n >= 2t + 1"
    - "asynchronous network with n >= 3t + 1"
    - "discrete logarithm assumption"
  evaluation_context:
    - "Rust implementation"
    - "AWS geo-distributed evaluation up to 256 nodes"
    - "comparison with complaint-based AVSS and VE-based VSS"
  bridge:
    - "publicly verifiable threshold setup and randomness support for asynchronous BFT/blockchain systems"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260623-verifiable-secret-sharing-simplified"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0083"
safe_for_absorption: true
source_refs:
  - "iacr:2023/1196"
  - "sha256:81dd93d12ed1d22f1bb4ea26c6bf2116f27614ab8a6ccbfbe904732c6d069fe6"
  - "pdf:~/Desktop/paper/2023-1196.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "consensus"
secondary_directions:
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
  - "asynchronous-reliable-broadcast"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p18"
  - "abstract and definitions target VSS, PVSS, AVSS and dual-threshold AVSS"
  - "Algorithms 1-3 construct synchronous VSS, asynchronous VSS and dual-threshold asynchronous VSS"
  - "Section 8 evaluates AVSS latency and bandwidth, not a full consensus protocol"
  - "classification corrected from distributed-systems/consensus/needs-review to asynchronous-verifiable-secret-sharing"
metadata_notes:
  - "Canonical ePrint URL inferred from local filename `2023-1196.pdf`; no external web verification was performed in this run."
  - "The local extracted text gives the title, authors, definitions, algorithms, evaluation and appendices clearly enough for deep absorption."
---

# Verifiable Secret Sharing Simplified

## Source Identity

- Local file: `~/Desktop/paper/2023-1196.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/2023-1196-81dd93d12ed1-pages.txt`
- True title: `Verifiable Secret Sharing Simplified`
- Authors: Sourav Das, Zhuolun Xiang, Alin Tomescu, Alexander Spiegelman, Benny Pinkas, Ling Ren
- Source identity: `iacr:2023/1196` inferred from local filename and paper identity.
- Reading status: deep read complete, p1-p18.

## One-Line Contribution

The paper replaces complaint-response VSS with signed acknowledgments plus publicly verifiable transcripts, yielding simple synchronous VSS, terminating asynchronous VSS, and dual-threshold asynchronous VSS with substantially lower bandwidth and latency than comparable verifiable-encryption-based designs.

## Problem Field

This source belongs primarily under [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]], a reusable primitive layer inside [[asynchronous-bft-consensus|Asynchronous BFT consensus]].

The durable problem is not a complete blockchain consensus protocol. It is how a dealer can share a secret so that honest parties later reconstruct the same value, third parties can verify that sharing succeeded, and asynchronous systems do not get stuck when a faulty dealer withholds responses.

Secondary fields:

| Field | Why it applies | Boundary |
| --- | --- | --- |
| [[dual-threshold-asynchronous-vss|Dual-threshold asynchronous VSS]] | Algorithm 3 separates the corruption threshold `t` from the secrecy threshold `ell` using selective verifiable encryption. | It is a VSS/AVSS method, not a DKG or consensus protocol by itself. |
| [[asynchronous-reliable-broadcast|Asynchronous reliable broadcast]] | The asynchronous protocols use Byzantine reliable broadcast to make a dealer transcript total: if one honest node outputs, all honest nodes eventually see the transcript. | RBC is a dependency, not the paper's primary contribution. |
| [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] | AVSS and dual-threshold AVSS are setup primitives for DKG, randomness beacons and threshold cryptography. | The paper does not implement a complete ADKG protocol. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | Publicly verifiable sharing and threshold setup can support common-coin and threshold-crypto layers in async BFT systems. | It does not define validator membership, mempool policy, execution or data availability. |

## Section Map

| Pages | Content | Notes |
| --- | --- | --- |
| p1-p3 | Abstract, introduction, motivation and related VSS shortcomings | Existing complaint-based schemes are efficient but lack clean async termination/public verifiability; VE-based schemes have high cost. |
| p3-p5 | Model, VSS/PVSS/dual-threshold definitions and assumptions | Static Byzantine adversary, PKI, private dealer-to-recipient channels, broadcast/RBC as black boxes. |
| p5-p7 | Synchronous VSS | Degree-`t` polynomial, signed ACKs, transcript with ACKs or opened missing shares. |
| p7-p9 | Asynchronous VSS | Degree-`2t` polynomial prevents secrecy loss after missing shares are revealed; RBC gives asynchronous termination. |
| p9-p11 | Dual-threshold asynchronous VSS | Reveal only `2t-ell` missing shares and verifiably encrypt the remaining `ell-t` missing shares. |
| p11-p13 | Implementation and geo-distributed evaluation | Rust implementation, 64/128/256 node AWS experiments, bandwidth and latency comparisons. |
| p13-p14 | Additional comparisons, discussion and conclusion | Interaction vs non-interaction, class-group and bivariate-polynomial comparison, batching/adaptive security as future work. |
| p16-p18 | Appendices | Broadcast definitions, Pedersen polynomial commitment, VE for Pedersen commitments, secrecy proof simulators. |

## Core Claims

| Claim | Evidence | Scope |
| --- | --- | --- |
| ACK transcripts can make VSS publicly verifiable without complaint-response rounds. | Algorithms 1-3 use signatures for ACKs and include missing shares or encrypted shares in a broadcast transcript. | Assumes PKI/signatures and a broadcast primitive. |
| Synchronous VSS tolerates `n >= 2t+1` and costs `O(kappa n^2 + C_BB(kappa n))`. | Theorem 1. | Uses degree-`t` sharing and Byzantine broadcast. |
| Asynchronous VSS with public verifiability and termination can be achieved with degree-`2t` sharing for `n >= 3t+1`. | Algorithm 2 and Theorem 2. | Not dual-threshold: an adversary corrupting `t` nodes may learn up to `2t` points. |
| Dual-threshold AVSS supports secrecy threshold `ell in [t, n-t)` by selectively combining public openings and verifiable encryptions. | Algorithm 3 and Theorem 3. | Uses VE in addition to polynomial commitments, signatures and RBC. |
| In geo-distributed evaluation, the low-threshold AVSS is comparable to complaint-based AVSS while fixing termination/public-verifiability gaps, and the dual-threshold scheme is much faster than VE-only baselines. | Section 8 figures and tables. | Concrete implementation choices matter; the paper compares selected baselines. |

## Mechanism Notes

### ACK-Transcript VSS

The core design replaces complaints with positive acknowledgments. The dealer privately sends each recipient a share, a polynomial commitment and an opening proof. A recipient signs the commitment only if the share verifies. The dealer then broadcasts a transcript containing enough signatures plus explicit share openings for recipients that did not ACK.

This changes the evidence object. A transcript is no longer just "dealer claimed sharing happened"; it contains a third-party-verifiable proof that each recipient either acknowledged the committed sharing instance or had its share publicly opened and verified.

### Synchronous VSS

The synchronous protocol uses a degree-`t` polynomial with secret `s(0)`. After waiting for ACKs, the dealer broadcasts the commitment, a set of signatures, and batch-opened shares for non-ACKing nodes. A valid transcript needs at least `t+1` ACK signatures and must account for every missing signature through a valid share opening.

Reconstruction waits for `t+1` valid shares. The synchronous setting can use the smaller degree because message delays are bounded and the dealer cannot use indefinite scheduling to force extra honest shares into the adversary's view before the sharing result is fixed.

### Asynchronous VSS

The naive asynchronous degree-`t` version leaks too much: the dealer may proceed after `2t+1` ACKs while also revealing missing honest shares, so an adversary can learn enough points to determine the secret.

The paper's fix is to share with a degree-`2t` polynomial. The dealer waits for `2t+1` ACKs and reveals missing shares through reliable broadcast. The adversary may learn up to `2t` points, but that is not enough to determine a degree-`2t` secret polynomial. RBC totality gives the termination property: if one honest node outputs the sharing result, all honest nodes eventually receive the same transcript.

The paper also notes a storage optimization: encode the polynomial commitment and store one Reed-Solomon symbol per node, then reconstruct the commitment during reconstruction with online error correction.

### Dual-Threshold AVSS

Dual-threshold AVSS separates the Byzantine corruption threshold `t` from the reconstruction secrecy threshold `ell`. The protocol still uses degree `2t`, but after `2t+1` ACKs it publicly opens only `2t-ell` missing shares and verifiably encrypts the remaining `ell-t` shares for their recipients.

This keeps any coalition of at most `ell` parties from learning more than `2t` usable points during sharing, while preserving completeness because recipients can decrypt their own missing shares. In the common case, the dealer waits a little longer for more ACKs and often avoids most or all verifiable encryptions.

### Polynomial Commitments And Verifiable Encryption

The paper instantiates polynomial commitments with Pedersen-style commitments plus SCRAPE-style low-degree testing. This keeps commitments hiding while supporting batch openings.

For dual-threshold AVSS, the paper adapts Groth-style verifiable encryption to Pedersen commitments. The main point is practical: Feldman commitments are not hiding for low-entropy secrets, so the VE proof must work with the Pedersen commitment/opening structure rather than assuming a bare `g^s` commitment.

## Evaluation Notes

The implementation is in Rust and, according to the paper, is available at `https://github.com/sourav1547/e2e-vss`. The evaluated stack uses `blstrs`, Pippenger multi-exponentiation, Schnorr signatures and an asynchronous RBC implementation based on prior ADD/RBC work.

Key reported results:

| Comparison | Result | Interpretation |
| --- | --- | --- |
| Low-threshold AVSS vs complaint-based AVSS | Comparable latency/bandwidth; verification is slightly higher but small in absolute terms. | The new scheme pays for signatures/transcript checks while gaining termination and public verifiability. |
| Dual-threshold AVSS vs VE-based VSS | Dealer bandwidth below 50% at `ell=2t` with `Delta=0`; common-case waiting reduces it close to low-threshold AVSS. | Selective VE avoids encrypting every share. |
| End-to-end latency vs VE-based VSS | VE baseline is about 5x-11x slower than low-threshold AVSS; dual-threshold AVSS improves by about 2x at `Delta=0` and 3x-7x with waiting. | Transcript size and propagation latency matter, not only local computation. |
| Reconstruction | Asynchronous reconstruction is about 2x baseline because degree is `2t`; still around tens of milliseconds at 256 nodes in the reported setup. | The main overhead is acceptable for setup/randomness-style use cases. |

## Why This Is Knowledge, Not Just A Paper Summary

This source changes the reusable AVSS layer:

- Below it, the source note keeps Algorithm 1/2/3 mechanics, exact thresholds, implementation choices and benchmark caveats.
- At the knowledge layer, [[asynchronous-verifiable-secret-sharing|AVSS]] gains a publicly verifiable ACK-transcript route.
- A new method node, [[dual-threshold-asynchronous-vss|Dual-threshold asynchronous VSS]], is justified because both this paper and [[eprint-2021-777-asynchronous-data-dissemination|ADD 2021/777]] now support the same reusable problem: separating fault threshold and secrecy/reconstruction threshold in asynchronous sharing.
- Above it, [[asynchronous-distributed-key-generation|ADKG]], randomness beacons and async BFT common-coin layers can reference this as setup machinery rather than carrying the protocol detail themselves.

## Limits And Caveats

- The protocols assume PKI, signatures and private authenticated dealer-to-recipient channels.
- Asynchronous termination relies on Byzantine reliable broadcast as a black-box primitive; the paper does not replace RBC.
- The basic asynchronous VSS is not dual-threshold; dual threshold requires verifiable encryption.
- Degree-`2t` asynchronous sharing increases reconstruction cost and may require degree-switching in applications that need arbitrary-degree secret sharing.
- The protocol is interactive between dealer and recipients; designing an equally efficient non-interactive VSS remains open.
- Batching and adaptive security are listed as future research directions rather than solved properties.
- Canonical ePrint identity was inferred locally; no external web verification was performed in this run.

## Absorption Decisions

| Target note | Action | Reason |
| --- | --- | --- |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | update | Adds ACK-transcript PVSS, terminating degree-`2t` AVSS and implementation evidence. |
| [[dual-threshold-asynchronous-vss|Dual-threshold asynchronous VSS]] | create | Multiple sources now support a reusable method node for separating `t` and `ell` in asynchronous VSS/ACSS. |
| [[asynchronous-reliable-broadcast|Asynchronous reliable broadcast]] | update | Records RBC totality as the termination carrier for A-VSS transcripts. |
| [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] | update | Adds dual-threshold/publicly verifiable VSS as a setup primitive relevant to DKG and threshold crypto. |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | update | Adds dual-threshold AVSS to the async BFT support stack. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | update | Clarifies that publicly verifiable sharing transfers as threshold setup/common-coin infrastructure, not as ledger policy. |

## Retrieval Hooks

- Query keys: `VSS Simplified`, `publicly verifiable VSS`, `PVSS`, `ACK transcript VSS`, `terminating AVSS`, `degree 2t AVSS`, `dual-threshold AVSS`, `verifiable encryption for Pedersen commitments`, `AVSS public transcript`, `ePrint 2023/1196`.

## Update Log

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-verifiable-secret-sharing-simplified | Deep-read source note created and absorbed into AVSS / dual-threshold AVSS architecture. | codex |
