---
id: "usenixsecurity23-das-high-threshold-adkg"
title: "Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling"
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
  - "p1-p3 title, authors, abstract, introduction, contribution summary and comparison table"
  - "p3-p5 system model, ADKG ideal functionality, high-threshold threat model and protocol overview"
  - "p6-p9 ACSS, MVBA, hyperinvertible-matrix extraction and Algorithm 1 design"
  - "p9-p12 key derivation, MVBA optimization, security proof and performance theorem"
  - "p12-p15 distributed polynomial sampling applications, implementation, evaluation and related work"
  - "p16-p19 references, online error correction appendix and ACSS sharing appendix"
canonical_url: "https://www.usenix.org/conference/usenixsecurity23/presentation/das"
pdf_url: ""
doi: ""
arxiv_id: ""
venue: "32nd USENIX Security Symposium"
year: "2023"
authors:
  - "Sourav Das"
  - "Zhuolun Xiang"
  - "Lefteris Kokoris-Kogias"
  - "Ling Ren"
affiliations:
  - "University of Illinois at Urbana-Champaign"
  - "Aptos"
  - "IST Austria"
  - "Mysten Labs"
local_pdf: "~/Desktop/paper/usenixsecurity23-das.pdf"
sha256: "0cded3a5e3529e9d1e544d84587031cab1588b79f8f5d45d319dbe68c4ef4c8a"
pages: 19
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/usenixsecurity23-das-0cded3a5e352-pages.txt"
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "consensus"
topic_ids:
  - "asynchronous-distributed-key-generation"
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
ontology_path:
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "asynchronous-distributed-key-generation"
primary_ontology_path: "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-distributed-key-generation/usenixsecurity23-das-high-threshold-adkg"
secondary_ontology_paths:
  - "distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-verifiable-secret-sharing/usenixsecurity23-das-high-threshold-adkg"
  - "distributed-systems/consensus/asynchronous-bft-consensus/validated-asynchronous-byzantine-agreement/usenixsecurity23-das-high-threshold-adkg"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
    - "blockchain-systems"
  directions:
    - "consensus"
    - "threshold-cryptographic-setup"
  topics:
    - "asynchronous-distributed-key-generation"
    - "high-threshold-adkg"
    - "distributed-polynomial-sampling"
    - "asynchronous-complete-secret-sharing"
    - "mvba"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "ADKG"
  - "high-threshold ADKG"
  - "distributed polynomial sampling"
  - "asynchronous complete secret sharing"
  - "MVBA"
  - "threshold signatures"
  - "common coin"
aliases:
  - "High-threshold ADKG"
  - "Distributed Polynomial Sampling"
  - "Practical Asynchronous High-threshold DKG"
  - "USENIX Security 2023 Das ADKG"
tags:
  - "nahida/source"
  - "paper"
  - "distributed-systems"
  - "consensus"
  - "asynchronous-bft-consensus"
  - "threshold-cryptography"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "asynchronous BFT consensus"
    - "threshold cryptographic setup"
  problem:
    - "practical high-threshold asynchronous DKG"
    - "avoid expensive high-threshold ACSS in asynchronous DKG"
    - "sample high-degree random polynomials with only low-threshold sharing"
  method_family:
    - "low-threshold ACSS plus MVBA"
    - "hyperinvertible-matrix randomness extraction"
    - "distributed polynomial sampling"
    - "Pedersen commitment based key derivation"
  proof_model:
    - "static Byzantine adversary"
    - "asynchronous private authenticated channels"
    - "n >= 3t + 1"
    - "Discrete Logarithm hardness"
    - "PKI and random-oracle/NIZK components through dependencies"
  evaluation_context:
    - "Python/Rust prototype"
    - "curve25519 and bls12381"
    - "AWS WAN deployment across eight regions"
    - "16, 32, 64, 128 nodes"
  application:
    - "threshold signatures"
    - "threshold encryption"
    - "shared randomness/common coins"
    - "asynchronous proactive secret sharing"
    - "asynchronous MPC preprocessing"
  bridge:
    - "threshold setup for asynchronous BFT and blockchain consensus"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260623-high-threshold-adkg-polynomial-sampling"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0115"
safe_for_absorption: true
source_refs:
  - "usenix:security23/das"
  - "sha256:0cded3a5e3529e9d1e544d84587031cab1588b79f8f5d45d319dbe68c4ef4c8a"
  - "pdf:~/Desktop/paper/usenixsecurity23-das.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "consensus"
secondary_directions:
  - "asynchronous-bft-consensus"
  - "asynchronous-verifiable-secret-sharing"
  - "threshold-cryptographic-setup"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "PDF p1-p2 true title/authors and USENIX Security 2023 venue"
  - "Abstract states high-threshold ADKG and distributed polynomial sampling as main contributions"
  - "Sections 2-5 define and prove an ADKG protocol rather than a generic blockchain consensus protocol"
  - "Sections 6-7 identify reusable distributed polynomial sampling applications and implementation evidence"
metadata_notes:
  - "Queue title was noisy USENIX proceedings boilerplate: `Open access to the Proceedings of the`."
  - "Local PDF metadata title and authors are empty; source identity was corrected from first pages and paper body."
  - "No web fetch was performed; canonical URL and code URL are taken from the PDF text."
---

# Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling

## Source Identity

- Local file: `~/Desktop/paper/usenixsecurity23-das.pdf`
- Extracted text: `vault/02_Raw/pdf/extracted/usenixsecurity23-das-0cded3a5e352-pages.txt`
- True title: `Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling`
- Authors: Sourav Das, Zhuolun Xiang, Lefteris Kokoris-Kogias, Ling Ren
- Venue: 32nd USENIX Security Symposium, 2023
- Canonical URL: `https://www.usenix.org/conference/usenixsecurity23/presentation/das`
- Code URL in paper: `https://github.com/sourav1547/htadkg`
- Strong identity: `sha256:0cded3a5e3529e9d1e544d84587031cab1588b79f8f5d45d319dbe68c4ef4c8a`
- Metadata correction: queue and PDF metadata surfaced USENIX proceedings boilerplate; title/authors/year/classification were corrected from p1-p2.
- Duplicate status: no strong duplicate by checksum/DOI/arXiv in the queue. [[eprint-2019-1015-asynchronous-distributed-key-generation|ADKG 2019/1015]] is a related predecessor, not a duplicate.

## One-Line Contribution

The paper makes high-threshold asynchronous distributed key generation practical by replacing expensive high-threshold ACSS with low-threshold ACSS plus MVBA and hyperinvertible-matrix randomness extraction, thereby sampling a random degree-`ell` polynomial whose evaluation points become high-threshold key shares.

## Problem Field

This source belongs primarily under [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]], inside [[asynchronous-bft-consensus|Asynchronous BFT consensus]].

It is not a blockchain consensus protocol by itself. It is a threshold-cryptographic setup protocol that can support BFT protocols, threshold signatures, threshold encryption, common coins, randomness beacons, asynchronous proactive secret sharing and asynchronous MPC preprocessing. The reusable upper concept is ADKG / distributed threshold setup; the paper-specific instance is the 2023 high-threshold ADKG construction and implementation.

Secondary field links:

| Field | Why it applies | Boundary |
| --- | --- | --- |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | The protocol relies on low-threshold ACSS and inherits ACSS/Pedersen commitment properties. | It avoids high-threshold ACSS instead of proposing a new AVSS taxonomy. |
| [[validated-asynchronous-byzantine-agreement|Validated asynchronous Byzantine agreement]] | The agreement phase uses MVBA to agree on `n-t` completed ACSS instances, and the paper optimizes MVBA computation. | It does not redefine VABA; MVBA is a subroutine. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | Many BFT/blockchain protocols use `2t+1` threshold signatures or common coins. | It does not solve mempool, validator governance, transaction ordering, or production key rotation. |

## Section Map

| Pages | Content | Evidence value |
| --- | --- | --- |
| p1-p2 | USENIX front matter, corrected title/authors, abstract and introduction | Identity and main contribution. |
| p2-p3 | Motivation for high-threshold DKG; comparison table; implementation claim | Shows prior high-threshold ADKG inefficiency and target thresholds. |
| p3-p4 | System model and `F_ADKG` ideal functionality | Defines static adversary, `n >= 3t+1`, `ell in [t,n-t-1]`, additional share exposure and output. |
| p4-p5 | Protocol overview | Explains why high-threshold ADKG is reduced to distributed random polynomial sampling. |
| p6-p7 | ACSS, Pedersen commitments, MVBA and hyperinvertible matrix preliminaries | Identifies reusable primitives and assumptions. |
| p7-p9 | Algorithm 1: sharing, agreement, randomness extraction and key derivation | Mechanism details and key derivation checks. |
| p9-p10 | Common-case key derivation and MVBA computation optimizations | Explains `O(n)` common-case key checks and `O(n^2)` MVBA group operations. |
| p10-p12 | Security proof and performance theorem | Lemma 1, real/ideal simulator and `O(kappa n^3)` communication. |
| p12-p13 | Distributed polynomial sampling applications | Random double sharing for MPC and proactive secret sharing. |
| p13-p15 | Prototype, AWS evaluation, related work and conclusion | Implementation and empirical comparison. |
| p16-p19 | References plus OEC/ACSS appendices | Confirms dependencies and reconstruction/error-correction mechanics. |

## Core Reading Notes

### Background, Motivation And Boundary

DKG bootstraps threshold cryptosystems without a trusted party: nodes jointly generate a public/private key pair, each node keeps one secret share, and later `ell+1` shares can produce threshold signatures, decrypt threshold ciphertexts, or generate shared randomness. In many BFT protocols the reconstruction threshold is high, often `2t+1` among `3t+1`, because threshold signatures or common coins must remain secure even if the adversary sees more partial outputs than the number of actively corrupted nodes.

The paper's key observation is that high-threshold ADKG should not necessarily require high-threshold ACSS. Prior high-threshold ADKG from Das et al. 2022 had very large concrete cost because its high-threshold ACSS component was two to three orders of magnitude slower than the low-threshold counterpart. This paper instead samples a random degree-`ell` polynomial in a distributed way and gives each node one evaluation point.

Boundary:

- Solves practical high-threshold asynchronous DKG for discrete-logarithm-based threshold cryptosystems.
- Supports `ell in [t,n-t-1]` in `n >= 3t+1` asynchronous networks.
- Static adversary can corrupt up to `t` nodes during protocol execution and later learn `ell-t` additional final shares, but not the internal states of those additional nodes.
- Assumes pairwise private/authenticated channels and PKI through the ACSS dependency.
- Does not provide UC proof in the paper; authors state the straight-line simulator suggests UC extension may be possible future work.

### Model, Definitions And Assumptions

The ideal functionality `F_ADKG` samples a random secret `z` in the field, generates `(n, ell+1)` Shamir shares, and outputs `g`, `g^z`, commitments/public threshold keys `g^[z]`, plus each party's share. Security is real/ideal indistinguishability: a simulator that receives the ideal outputs for corrupted and additionally observed shares should reproduce the adversary's view.

Important parameters and primitives:

- `n`: total nodes.
- `t`: Byzantine corruptions tolerated.
- `ell`: reconstruction threshold, with `ell+1` valid shares required.
- `G`: elliptic-curve group of order `q`; security relies on Discrete Logarithm hardness.
- `g,h`: independent generators for Pedersen commitments.
- `ACSS`: low-threshold asynchronous complete secret sharing with homomorphic partial commitments.
- `MVBA`: multi-valued validated Byzantine agreement over a set of completed ACSS instances.
- `OEC`: online error correction used when reconstructing each node's polynomial evaluation.

### Method: Four-Phase High-Threshold ADKG

The protocol has four phases.

1. Sharing phase: each node samples two secrets `a_i,b_i` and shares them via low-threshold ACSS. The ACSS outputs shares and Pedersen commitments. Two secrets per node are enough because each randomness extraction from one vector yields `t+1` random coefficients, and `ell` can be up to `2t`.
2. Agreement phase: nodes wait for `n-t` locally completed ACSS instances and run MVBA with a predicate requiring proposed sets to be locally completed. All honest nodes agree on a set `T` of at least `n-t` ACSS instances, which contains at least `n-2t` honest random contributions.
3. Randomness extraction phase: nodes apply hyperinvertible matrices to the secret-shared vectors `a` and `b`. This locally produces shares of `ell+1` independent random coefficients `z_0...z_ell`. These coefficients define a random degree-`ell` polynomial `z(x)`. Each node computes secret shares of every `z(j)` and sends the appropriate fragments to node `j`; node `j` uses online error correction to recover its evaluation point.
4. Key derivation phase: nodes use homomorphic Pedersen commitments to compute commitments to `z(i)`, verify KEY messages with NIZK proof-of-knowledge and commitment checks, and interpolate `g^z(0)` plus all threshold public keys from `ell+1` valid messages.

The core trick is distributed polynomial sampling: sample the coefficients of the high-degree polynomial in secret-shared form, then evaluate the polynomial across nodes, instead of asking ACSS to directly share a high-degree polynomial.

### MVBA And Key-Derivation Optimizations

The paper reduces MVBA worst-case computation from `O(n^3)` group operations to `O(n^2)` group exponentiations by having one proposer aggregate commitments while other nodes verify one position of the aggregated commitment before participating in reliable broadcast. Since `t+1` honest positions determine a degree-`t` polynomial commitment, successful reliable broadcast implies a valid aggregate commitment.

For key derivation, the naive way computes commitments for all public key shares in `O(n^2)` exponentiations; NTT can reduce this to `O(n log n)`. The paper further uses an optimistic path: with valid proofs and no Byzantine disruption, interpolate `g^z(0)` from `ell+1` KEY messages and check it against the public commitment `c_0`, giving `O(n)` group exponentiations in the fault-free common case; fallback performs full validation.

### Security And Correctness Argument

Lemma 1 shows all honest nodes output the same public key and threshold public keys. MVBA agreement fixes the set `T`; ACSS homomorphic commitments and deterministic randomness extraction make all honest nodes compute the same Pedersen polynomial commitments; online error correction gives honest nodes correct evaluation points; binding of Pedersen commitments plus NIZK knowledge proofs prevents faulty nodes from providing inconsistent public key shares without solving discrete logarithm.

The main theorem constructs a simulator that receives ideal `F_ADKG` outputs for corrupted and additionally observed shares. The simulator samples `h=g^alpha`, follows the real sharing/agreement phases, then adjusts honest RANDEX messages and Pedersen randomness so corrupted parties' observed shares match the ideal polynomial while commitments remain unchanged. Perfect hiding of Pedersen commitments, Shamir secrecy and randomness-extractor uniformity give indistinguishability.

Performance theorem:

- Expected total communication: `O(kappa n^3)`.
- Expected per-node elliptic-curve computation: `O(n^2)` exponentiations.
- Expected latency: `O(log n)` asynchronous rounds.
- Common-case termination: `O(1)` rounds under synchrony/no failures, inherited from prior MVBA behavior.

### Applications Beyond ADKG

The first three phases form a distributed polynomial sampling primitive: after execution, each node learns `z(i)` for a uniformly random degree-`ell` polynomial. The paper points to two applications:

- Asynchronous random double sharing for MPC: with `ell=2t`, nodes get both degree-`t` and degree-`2t` sharings of a random secret, useful for offline/online multiplication.
- Proactive secret sharing: nodes can refresh old shares by sampling a random polynomial with zero constant term and adding `z(i)` to their old share. The refresh is secure against at most `t` corruptions during refresh, while the post-refresh adversary may learn up to `ell` new shares.

These applications make `distributed polynomial sampling` a reusable method route, but this run keeps it inside the ADKG node as a source-extension/method candidate until more independent sources justify a standalone node.

## Evaluation

### Implementation

The prototype is implemented in Python 3.7.13 with Rust libraries for elliptic-curve operations and `asyncio` for concurrency. It supports arbitrary `ell >= t`, curve25519 and bls12381. It builds on the open-source asynchronous DKG implementation from Das et al. 2022, reuses their MVBA implementation, uses low-threshold ACSS from Das et al. 2021, and merges MVBA's sharing phase with the high-threshold ADKG sharing phase by sharing three random secrets in one ACSS instance.

### Setup

The experiments use `n in {16,32,64,128}`, threshold `ell=2t`, AWS `t3a.medium` VMs, one node per VM, Ubuntu 20.04, and eight regions: Canada, Ireland, North California, North Virginia, Oregon, Ohio, Singapore and Tokyo. Baseline is the only existing asynchronous DKG implementation, Das et al. 2022.

### Results

Representative results from Table 3:

| Scheme | Curve | Threshold | n=64 runtime | n=64 bandwidth/node | Notes |
| --- | --- | --- | --- | --- | --- |
| Das et al. 2022 | curve25519 | `2t` | 152.56 s | 18.97 MB | Prior high-threshold ADKG. |
| This work | curve25519 | `2t` | 12.48 s | 3.32 MB | About 8.2% of runtime and 18% of bandwidth vs prior high-threshold baseline. |
| This work | bls12381 | `2t` | 14.50 s | 3.48 MB | Pairing-friendly curve; group operations slower but bandwidth similar. |
| This work | curve25519 | `2t`, n=128 | 46.55 s | 13.10 MB | Demonstrates scaling to 128 WAN nodes. |

The abstract summarizes the improvement as 90% lower running time and 80% lower bandwidth relative to state of the art. The evaluation mostly reflects common-case performance; the paper separately argues worst-case group computation improves from `O(n^3)` in Das et al. 2022 to `O(n^2)` exponentiations.

## Evidence Table

| Claim | Evidence anchor | Confidence | Caveat |
| --- | --- | --- | --- |
| The true title is `Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling`. | p1-p2 title block | high | PDF metadata title is empty; queue title was proceedings boilerplate. |
| The protocol supports high-threshold ADKG for `ell in [t,n-t-1]` with `n >= 3t+1`. | p2 abstract; p3-p4 `F_ADKG` and definition | high | Static adversary and additional-share exposure model are part of security definition. |
| Core method is low-threshold ACSS plus MVBA plus randomness extraction, not high-threshold ACSS. | p4-p5 overview; p7-p9 Algorithm 1 | high | Low-threshold ACSS still depends on PKI/private channels or higher-cost alternatives. |
| Distributed polynomial sampling may support random double sharing and proactive secret sharing. | p12-p13 §6.1-§6.2 | medium | The paper gives constructions/arguments, not a full evaluated MPC/proactive system. |
| Expected communication is `O(kappa n^3)`, per-node EC computation `O(n^2)`, expected rounds `O(log n)`. | p12 Lemmas 2-4 and Theorem 2 | high | Non-EC Reed-Solomon decoding cost can be `O(n^3 log n)` but is claimed not bottleneck. |
| At 64 nodes with curve25519, runtime is 12.48s and bandwidth 3.32MB/node. | p14 Table 3 and §7.3 | high | Single-thread prototype; common-case evaluation. |
| The paper leaves UC proof as future work. | p15 conclusion | high | Stand-alone proof is provided. |

## Knowledge Handoff

### Target Knowledge Updates

| Target | Handling | Delta |
| --- | --- | --- |
| [[asynchronous-distributed-key-generation|Asynchronous distributed key generation]] | source extension and method-route update | Add high-threshold ADKG via distributed polynomial sampling, practical implementation evidence, and evaluation numbers. |
| [[asynchronous-verifiable-secret-sharing|Asynchronous verifiable secret sharing]] | small source extension | Clarify that practical high-threshold ADKG can be built by using low-threshold ACSS plus sampling, avoiding high-threshold ACSS as bottleneck. |
| [[asynchronous-bft-consensus|Asynchronous BFT consensus]] | representative source update | Add high-threshold threshold-crypto setup as a support primitive for BFT common coins/signatures, without recasting it as consensus. |
| [[distributed-bft-to-asynchronous-blockchain-consensus|Distributed BFT -> asynchronous blockchain consensus]] | no new bridge required | Existing bridge covers transfer of async BFT setup primitives to blockchain; update only if later source shows blockchain deployment. |

### Promotion Decisions

| Candidate | Generality | Handling | Reason |
| --- | --- | --- | --- |
| High-threshold ADKG | reusable method variant | section/source-extension under ADKG | It is a variant of existing ADKG method node. |
| Distributed polynomial sampling | reusable method candidate | method route/query key, not standalone node yet | One source shows broad applications, but current vault lacks multiple independent sources. |
| Low-threshold ACSS as high-threshold setup substrate | reusable mechanism | add to AVSS/ADKG method routes | Useful for future ADKG/ACSS queries. |
| MVBA aggregation optimization | subroutine optimization | source note and ADKG method row only | Too specific for a separate knowledge node. |
| Asynchronous random double sharing | application candidate | queued/alias under ADKG | Needs more MPC/proactive secret sharing sources before splitting. |

## Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `distributed-systems` | ADKG, asynchronous network, Byzantine nodes, MVBA, ACSS | high | durable parent |
| Research background | threshold cryptosystems need dealer-free setup; high-threshold cryptography is needed by BFT and common coins | p2 introduction | high | ADKG node background |
| Research problem | practical high-threshold ADKG without expensive high-threshold ACSS | p2-p5 | high | ADKG source extension |
| Foundation concepts | ADKG, ACSS/AVSS, MVBA, Pedersen commitments, hyperinvertible matrices, threshold signatures | p3-p8 | high | existing nodes plus source-local detail |
| Method family | distributed polynomial sampling | p4-p5, p12-p13 | medium-high | method route/query key, future split candidate |
| Application/evaluation context | threshold signatures/common coins, proactive secret sharing, MPC preprocessing, AWS WAN prototype | p2, p12-p14 | high | source extension and retrieval keys |
| Source instance | Das-Xiang-Kokoris-Kogias-Ren USENIX Security 2023 high-threshold ADKG | full paper | high | source note |

## Retrieval Optimization

- Future queries helped: “high-threshold ADKG”, “distributed polynomial sampling”, “为什么不直接用 high-threshold ACSS”, “ADKG 实验性能”, “ADKG 和 BFT threshold signature 的关系”, “异步 DKG 如何支持 2t+1 阈值”.
- Source reads avoided: ordinary questions about protocol phases, assumptions, asymptotic costs, Table 3 results and source classification can be answered from this note plus [[asynchronous-distributed-key-generation|ADKG]].
- Content kept source-only: exact simulator steps, all reference details, appendices, one-off code/library implementation choices.
- Foundation gaps: `common coin` and `distributed polynomial sampling` may become nodes after more sources; `production key rotation/reconfiguration` still lacks direct source.

## Review Items

- `distributed polynomial sampling` is potentially a reusable method node, but this run keeps it as `source_extension` because it currently has one direct source in the managed knowledge tree.
- Canonical PDF URL was not separately fetched; canonical presentation URL is from p1 USENIX front matter.
- Security is stand-alone, not formally UC in the paper.
