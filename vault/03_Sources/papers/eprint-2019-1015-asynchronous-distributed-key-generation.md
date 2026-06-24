---
id: "iacr-eprint-2019-1015"
title: "Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures"
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
  - "p1-p4 abstract, introduction, trusted-dealer motivation, contributions and theorem statement"
  - "p4-p7 related work, formal setting overview, cryptographic abstractions and model assumptions"
  - "p7-p12 high-threshold AVSS definition and implementation"
  - "p12-p15 weak DKG protocol, prediction properties and complexity"
  - "p15-p19 eventually perfect common coin construction and proofs"
  - "p19-p21 eventually efficient ABA, ADKG construction, corollaries and conclusion"
  - "p22-p29 references and appendices for formal model and proofs"
canonical_url: "https://eprint.iacr.org/2019/1015"
pdf_url: "https://eprint.iacr.org/2019/1015.pdf"
doi: ""
arxiv_id: ""
venue: "IACR ePrint 2019/1015; local PDF metadata title was generic"
year: "2019"
authors:
  - "Eleftherios Kokoris-Kogias"
  - "Dahlia Malkhi"
  - "Alexander Spiegelman"
affiliations:
  - "Facebook Novi"
  - "IST Austria"
local_pdf: "~/Desktop/paper/2019-1015.pdf"
sha256: "5e06ad31a23a5293c64604366d77ee3a7c59973bc6da8209569acef7edc46fb8"
pages: 29
pdf_extractor: "pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/eprint-5e06ad31a23a5293c64604366d77ee3a7c59973bc6da8209569acef7edc46fb8-pages.txt"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-distributed-key-generation"
  - "asynchronous-bft-consensus"
  - "threshold-cryptographic-setup"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-distributed-key-generation"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation/iacr-eprint-2019-1015"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/iacr-eprint-2019-1015"
  - "distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement/iacr-eprint-2019-1015"
  - "blockchain-systems/blockchain-consensus/asynchronous-bft-consensus/iacr-eprint-2019-1015"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
    - "blockchain-systems"
  directions:
    - "consensus"
    - "blockchain-consensus"
  topics:
    - "asynchronous-distributed-key-generation"
    - "high-threshold-asynchronous-verifiable-secret-sharing"
    - "eventually-perfect-common-coin"
    - "trusted-dealer-free-asynchronous-bft"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "asynchronous distributed key generation"
  - "ADKG"
  - "high-threshold AVSS"
  - "weak DKG"
  - "eventually perfect common coin"
  - "trusted dealer removal"
  - "threshold signatures"
aliases:
  - "ADKG"
  - "Asynchronous Distributed Key Generation"
  - "High-threshold AVSS"
  - "HA-VSS"
  - "Eventually Perfect Common Coin"
  - "EPCC"
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
    - "distributed cryptographic setup"
  problem:
    - "remove trusted dealer assumptions from asynchronous BFT common coins and threshold signatures"
    - "support threshold `2f+1` reconstruction in asynchronous `n=3f+1` systems"
    - "bootstrap VABA and threshold signatures without synchronous DKG"
  method_family:
    - "high-threshold asynchronous verifiable secret sharing"
    - "weak distributed key generation"
    - "eventually perfect common coin"
    - "eventually efficient asynchronous binary agreement"
    - "ACS-style ADKG"
  proof_model:
    - "asynchronous authenticated message passing"
    - "adaptive adversary with `f < n/3`"
    - "computationally bounded adversary"
    - "PKI and cryptographic abstractions, no trusted dealer"
  evaluation_context:
    - "theoretical protocol and proof"
    - "expected communication/time bounds"
  bridge:
    - "trusted-dealer-free threshold setup for asynchronous blockchain consensus primitives"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0081"
safe_for_absorption: true
source_refs:
  - "iacr:2019/1015"
  - "sha256:5e06ad31a23a5293c64604366d77ee3a7c59973bc6da8209569acef7edc46fb8"
  - "pdf:~/Desktop/paper/2019-1015.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "consensus"
secondary_directions:
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
  - "validated-asynchronous-byzantine-agreement"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p29"
  - "title and abstract identify asynchronous distributed key generation as the main contribution"
  - "Sections 3-6 build HA-VSS, wDKG, EPCC, EEABA and ADKG for asynchronous BFT setup"
  - "paper removes trusted dealer assumptions for common coin, VABA and threshold signatures; it is not itself a blockchain consensus protocol"
  - "classification corrected from blockchain-systems/consensus/consensus-foundations to distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation"
metadata_notes:
  - "Local PDF metadata title is only `Eprint`; source title was taken from p1."
  - "Canonical ePrint URL inferred from local filename `2019-1015.pdf` and paper identity; no web fetch was performed in this run."
---

# Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures

## Source Identity

- Local file: `~/Desktop/paper/2019-1015.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/eprint-5e06ad31a23a5293c64604366d77ee3a7c59973bc6da8209569acef7edc46fb8-pages.txt`
- True title: `Asynchronous Distributed Key Generation for Computationally-Secure Randomness, Consensus, and Threshold Signatures`
- Authors: Eleftherios Kokoris-Kogias, Dahlia Malkhi, Alexander Spiegelman
- Source identity: `iacr:2019/1015` inferred from filename and local ePrint-style paper; local PDF metadata itself was generic.
- Reading status: deep read complete, p1-p29.

## One-Line Contribution

The paper introduces the first asynchronous distributed key generation protocol in the `n=3f+1`, `f<n/3` Byzantine setting, using high-threshold AVSS, weak DKG and an eventually perfect common coin to remove trusted-dealer setup from scalable asynchronous consensus and threshold-signature protocols.

## Problem Field

This source belongs primarily under [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]], a method node inside [[asynchronous-bft-consensus|Asynchronous BFT consensus]].

The paper is not a blockchain protocol. Its durable problem is setup: many efficient asynchronous BFT, VABA, SMR and threshold-signature constructions assume a trusted dealer that creates threshold keys or common coins. ADKG replaces that dealer with an asynchronous protocol that honest parties can run under adaptive Byzantine faults.

Secondary fields:

| Field | Why it applies | Boundary |
| --- | --- | --- |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | HA-VSS is the main technical primitive for high reconstruction threshold. | HA-VSS is one AVSS route, not the whole AVSS taxonomy. |
| [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]] | ADKG bootstraps the threshold coin/signature setup assumed by VABA-style protocols. | VABA logic stays in VABA sources; this source removes setup assumptions. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | Blockchain consensus can reuse trusted-dealer-free threshold setup. | It does not solve mempool, transaction dissemination, validator economics, or production key rotation. |

## Section Map

| Pages | Content | Notes |
| --- | --- | --- |
| p1-p2 | Abstract, motivation and Theorem 1.1 | Trusted dealer removal; expected `O(n^4)` communication and `O(f)` time. |
| p2-p4 | Technical contribution summary | HA-VSS, wDKG, EPCC, EEABA, ADKG and VABA corollaries. |
| p4-p6 | Related work | ABA, DKG, VABA and asynchronous MPC positioning. |
| p6-p7 | Model and cryptographic abstractions | Authenticated async message passing, adaptive adversary, PKI, computational security. |
| p7-p12 | HA-VSS | High-threshold AVSS with asymmetric bivariate polynomial. |
| p12-p15 | wDKG | Increasing predictions eventually converge without violating FLP. |
| p15-p19 | EPCC | Eventually perfect common coin built from wDKG predictions and threshold shares. |
| p19-p21 | EEABA and ADKG | EPCC plugged into ABA; ACS-like ADKG over HA-VSS instances. |
| p22-p29 | References and proofs | Formal model, HA-VSS, EPCC and ADKG proofs. |

## Core Claims

| Claim | Evidence | Scope |
| --- | --- | --- |
| ADKG can be built in a fully asynchronous network for `f<n/3`. | Theorem 1.1 and Algorithm 5. | Computationally secure model with authenticated channels and PKI. |
| The paper supports threshold `2f+1` reconstruction in `n=3f+1` asynchronous settings. | HA-VSS contribution and Section 3. | `k <= n-f`, with common use at `k=2f+1`. |
| A trusted dealer is not necessary for threshold coins, VABA and threshold signatures. | Corollaries in Section 1 and Section 6. | Initial setup remains expensive; deployment engineering is not evaluated. |
| The initial ADKG cost is high but amortizable. | Theorem 1.1 and VABA corollary. | One-shot expected `O(n^4)` words and `O(f)` time; later VABA can be `O(n^2)` amortized. |

## Mechanism Notes

### HA-VSS

Existing AVSS constructions struggle with reconstruction thresholds above `n-2f`, because sharing and reconstruction phases each wait for `n-f` responses and Byzantine parties can withhold values. HA-VSS raises the reconstruction threshold up to `n-f` by using an asymmetric bivariate polynomial: one dimension supports low-threshold recovery, and the other supports high-threshold reconstruction.

Key properties:

- Liveness: honest dealer sharing eventually completes for honest parties.
- Agreement: if one honest party completes, all honest parties can complete with a compatible sharing.
- Correctness: honest reconstruction yields the committed secret.
- Privacy: before reconstruction, the adversary does not learn the honest dealer's secret beyond allowed threshold leakage.

### wDKG

wDKG runs `n` HA-VSS instances and emits predictions rather than a final terminating decision. This is deliberate: exact asynchronous agreement on a key set cannot simply terminate deterministically under FLP-style constraints. The protocol instead ensures predictions are monotonically increasing and eventually all honest parties' last prediction matches.

This makes wDKG an eventual agreement detector for key sets.

### EPCC

The eventually perfect common coin uses the converging wDKG predictions. Early coin sequence numbers can disagree, but each disagreement implies progress to a larger prediction set. Since the set can grow only finitely many times, at most `f` coin sequence numbers can disagree; after that, honest parties use a consistent threshold-key view and the coin behaves like a perfect common coin.

### EEABA and ADKG

EEABA plugs EPCC into an asynchronous binary agreement protocol so that after the bounded bad-coin prefix, the ABA runs with efficient expected behavior. ADKG then runs HA-VSS shares and correlated ABA decisions in an ACS-like construction to agree on a common set of usable key shares.

## Why This Is Knowledge, Not Just A Paper Summary

This paper adds a reusable setup layer to the knowledge base:

- Below it are source details: HA-VSS algorithms, wDKG predictions, EPCC coin-share logic, ADKG proofs.
- At its layer is the method field [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]].
- Above it are [[asynchronous-bft-consensus|Asynchronous BFT consensus]], [[validated-asynchronous-byzantine-agreement|VABA]], threshold-signature-based consensus protocols and bridge notes for blockchain consensus.

## Limits And Caveats

- No implementation or benchmark is provided.
- The model assumes PKI, authenticated asynchronous links and computationally bounded adversaries.
- The protocol removes a trusted dealer, but does not remove all setup: parties still need public keys and cryptographic primitives.
- The VABA result is a setup-removal corollary, not a new VABA algorithm.
- Blockchain relevance is indirect: ADKG helps threshold-crypto setup for consensus protocols, but does not address data dissemination, mempools, execution, validator-set governance, or economic finality.
- The local metadata title was weak; the source title and ePrint identity were recovered from the PDF text and filename.

## Absorption Decisions

| Target note | Action | Reason |
| --- | --- | --- |
| [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] | create | ADKG is a reusable method/problem field, not merely this paper's title. |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | update | Adds trusted-dealer-free threshold setup as a method axis. |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | update | HA-VSS is a high-threshold AVSS route. |
| [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]] | update | ADKG removes the trusted-dealer assumption behind threshold-coin setup. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | update | Adds transfer boundary for threshold-setup primitives. |

## Retrieval Hooks

- Query keys: `ADKG`, `asynchronous distributed key generation`, `high-threshold AVSS`, `HA-VSS`, `weak DKG`, `wDKG`, `eventually perfect common coin`, `EPCC`, `trusted dealer removal`, `threshold signatures`, `trusted-dealer-free VABA`.
- Best first hop: [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]].
- Best source comparison: [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] for AVSS lineage and [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]] for VABA setup assumptions.

## Update Log

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-adkg-trusted-dealer-free-async-bft | Deep-read local PDF, corrected queue classification, created source note and propagated into Source + Knowledge + Bridge architecture. | codex |
