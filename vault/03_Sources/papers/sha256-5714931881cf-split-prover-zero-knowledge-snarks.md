---
id: "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
title: "Split Prover Zero-Knowledge SNARKs"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
source_kind: "paper"
source_subtype: "local_pdf"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
paper_title: "Split Prover Zero-Knowledge SNARKs"
authors:
  - "Sanjam Garg"
  - "Aarushi Goel"
  - "Dimitris Kolonelos"
  - "Sina Shiehian"
  - "Rohit Sinha"
year: "2025"
publication_date: "2025-02-26"
venue: ""
doi: ""
arxiv_id: ""
canonical_url: ""
local_pdf: "~/Desktop/paper/2025-373.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2025-373-5714931881cf-pages.txt"
sha256: "5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
page_count: 27
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "split-prover-zksnarks"
  - "private-delegated-proving"
  - "distributed-proof-generation"
  - "zk-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
  - "private-delegated-proving"
  - "split-prover-zksnarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks/sha256-5714931881cf"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/sha256-5714931881cf"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-5714931881cf"
  - "zero-knowledge-proofs/recursion-and-folding/sha256-5714931881cf"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Abstract and Section 1 define the durable problem as two-phase zkSNARK proof generation with partial witness availability and private delegation."
  - "Section 3 gives the reusable split-prover zkSNARK definition with unchanged verifier and split zero-knowledge for aux state."
  - "Section 4 gives a Groth16 split-prover construction; Section 5 gives a Groth16 lower bound."
  - "Queue classification corrected from distributed transactions to private delegated proving / split prover zkSNARKs."
source_relation_edges:
  - from: "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
    relation: "evidences"
    to: "nahida-knowledge-split-prover-zksnarks"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
    relation: "evidences"
    to: "nahida-knowledge-private-delegated-proving"
    confidence: "high"
    status: "active_seed"
  - from: "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
    relation: "evidences"
    to: "nahida-knowledge-distributed-proof-generation"
    confidence: "medium"
    status: "active_seed"
  - from: "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
    relation: "evidences"
    to: "nahida-knowledge-zk-snarks"
    confidence: "medium"
    status: "active_seed"
  - from: "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
    relation: "evidences"
    to: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    confidence: "high"
    status: "active_seed"
domains:
  - "zero-knowledge-proofs"
topics:
  - "split prover zkSNARKs"
  - "private delegated proving"
  - "two-phase proof generation"
  - "partial witness availability"
  - "Groth16"
  - "split zero-knowledge"
  - "delegatable payments"
  - "recursive SNARK comparison"
aliases:
  - "split prover zkSNARK"
  - "two-phase zkSNARK proving"
  - "partial-witness delegated proving"
query_keys:
  - "Split Prover Zero-Knowledge SNARKs"
  - "split prover zkSNARKs"
  - "partial witness zkSNARK delegation"
  - "two-phase Groth16 prover"
  - "delegatable payments zkSNARK"
  - "split zero-knowledge aux state"
  - "Groth16 second prover lower bound"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zk-snarks"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-split-prover-zksnarks"
source_refs:
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
confidence: "high"
trust_tier: "primary"
---

# Split Prover Zero-Knowledge SNARKs

## Source Identity

| Field | Value |
| --- | --- |
| Title | Split Prover Zero-Knowledge SNARKs |
| Authors | Sanjam Garg; Aarushi Goel; Dimitris Kolonelos; Sina Shiehian; Rohit Sinha |
| Date in PDF metadata | 2025-02-26 |
| Local PDF | `~/Desktop/paper/2025-373.pdf` |
| SHA-256 | `5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0` |
| Pages | 27 |
| Metadata caveat | Filename suggests an IACR ePrint-style identifier, but DOI/canonical URL were not externally fetched in this run. |

## Reading Coverage

| Section | Pages | Coverage |
| --- | --- | --- |
| Abstract and contents | p1-p2 | Problem framing, key claims, structure. |
| Introduction | p3-p7 | Contributions, delegatable payments/anonymous credentials applications, comparison with IVC/recursive SNARKs and other delegation frameworks. |
| Preliminaries | p7-p10 | Bilinear groups, zkSNARK properties, Groth16 setup/prover/verifier recap. |
| Split prover definition | p10-p11 | `Setupsplit`, `PI`, `PII`, unchanged verifier, split correctness, split zero-knowledge for aux state. |
| Groth16 construction | p11-p20 | Split R1CS, partial Groth16 proof computation, quotient decomposition, `H` precomputation for small second witness, masking for split zero-knowledge, theorem and efficiency. |
| Lower bound | p21-p23 | Generic-group-style lower bound for second prover group elements / operations in Groth16 split proving. |
| References | p24-p27 | Groth16, Zerocash/Zcash, delegation frameworks, IVC/recursive SNARKs, ROM limitations, FHE/collaborative proving. |

## One-Sentence Memory

This paper introduces split prover zkSNARKs: Alice computes a privacy-preserving first-phase auxiliary state using the witness she has early, Bob later completes a Groth16 proof once the remaining witness is known, the final verifier is exactly the original Groth16 verifier, and the paper proves the second phase is asymptotically tight for Groth16.

## Problem Setting

The motivating situation is not generic prover acceleration. It is a partial-witness and authorization problem. In applications such as Zcash-style payments or anonymous credentials, a large part of the witness may be available before the actual transaction is finalized. Alice may know secret keys, Merkle paths, credential validity material, or old-coin opening data, but the final transaction amount, new outputs, or queried credential property may arrive later.

The desired workflow is:

1. Alice starts proof generation early using `xI, wI`.
2. Alice hands Bob an auxiliary state.
3. Bob learns or receives `xII, wII` later and completes the proof.
4. Bob should not learn the first-phase witness or be able to generate unauthorized proofs on Alice's behalf.
5. The verifier should not detect that the proof was split; existing Groth16 deployments should keep the same verifier.

This differs from ordinary distributed proving and from private delegated proving systems such as Siniel. Siniel assumes the delegator has the whole witness and wants full prover outsourcing while hiding witness shares from multiple workers. Split prover zkSNARKs assume the witness naturally arrives in two stages and focus on safe precomputation plus late completion by another party.

## Main Contributions

| Contribution | What It Adds | Evidence Anchor | Reusable Placement |
| --- | --- | --- | --- |
| Split prover zkSNARK definition | Formalizes setup plus two proving algorithms `PI` and `PII`, with the original verifier unchanged. | Section 3, p10-p11 | [[split-prover-zksnarks|Split prover zkSNARKs]] |
| Split zero-knowledge for aux state | Requires the first-phase aux state to be simulatable from public information and the first subcircuit output `CI(xI,wI)`, not from the full first witness. | Section 3, p10-p11 | [[private-delegated-proving|Private delegated proving]] |
| Groth16 split prover construction | Splits Groth16 proof generation over split R1CS, decomposes the quotient contribution, and adds masking wires for split ZK. | Section 4, p11-p20 | [[zk-snarks|zk-SNARKs]] source extension |
| Tight second-phase complexity | Achieves `O(min{|CII|^2, |C| log |C|})` second-phase time and proves a matching Groth16 lower bound up to log factors/group-operation model. | p3-p4, p20-p23 | source-local theorem |
| Deployment compatibility | Preserves Groth16 verification algorithm and proof shape, though setup is for a modified split relation. | p1, p18-p20 | existing Groth16 deployments with new split setup |

## Definition Detail

The paper replaces the single zkSNARK prover with:

| Algorithm | Input | Output / Role |
| --- | --- | --- |
| `Setupsplit(R, XII, WII)` | Relation `R` and the indices belonging to second-stage public/witness inputs. | Split proving reference string `fsrs`. The verifier key remains compatible with Groth16-style verification of the modified relation. |
| `PI(fsrs, xI, wI)` | First-stage statement/witness. | Auxiliary state `aux` to be handed to the second prover. |
| `PII(fsrs, xII, wII, aux)` | Second-stage statement/witness and aux. | Standard zkSNARK proof `pi`. |
| `V` | Original verifier input/proof. | Same verifier algorithm as the underlying SNARK. |

Split correctness says a proof completed by `PII` verifies for the concatenated statement/witness whenever the whole relation is satisfied. Split zero-knowledge is a property of `aux`, separate from the ordinary zero-knowledge of the final proof. The simulator can depend on the relation, public input partition, and the first subcircuit output `CI(xI,wI)`, because Bob may need this output to finish the computation; it should not need the rest of `wI`.

## Groth16 Construction

### Split R1CS

The construction treats the circuit as `C = CII(xII, wII, CI(xI,wI))`. It converts this into a split R1CS where the extended witness vector is divided into `zI` and `zII`. The `A`, `B`, and `C` matrices are block-structured so first-phase-only, second-phase-only, and cross-output constraints can be isolated.

The unavoidable information crossing the phase boundary is the output of the first subcircuit, called `aux0` in the overview. This is the value Bob needs to continue the computation. The split zero-knowledge goal is therefore not "aux reveals nothing at all"; it is "aux reveals nothing beyond the allowed first-subcircuit output."

### `pi1` and `pi2`

Groth16 proofs contain three group elements. For the first two elements, the construction lets the first prover precompute the contribution of first-phase witness coordinates. The second prover later adds the second-phase contribution and the ordinary Groth16 proving randomness. This part is conceptually straightforward because the expressions are linear in the witness vector plus randomizers.

### `pi3` and Quotient Decomposition

The hard part is `pi3`, whose Groth16 term includes the quotient polynomial contribution. The paper decomposes the quotient into four parts:

| Term | Dependency | Who can compute it |
| --- | --- | --- |
| `q1` | first-phase witness only | Alice / `PI` |
| `q2` | linear in second witness and first-phase data | Alice prepares vector material; Bob combines with `zII` |
| `q3` | symmetric cross term | Alice prepares vector material; Bob combines with `zII` |
| `q4` | second-phase witness only | Bob / `PII` |

The key algebraic tool is that the quotient of a linear combination can be expressed as the linear combination of quotients. This lets the first prover precompute the quotient contributions that depend on `zI` without knowing `zII`.

### Small Second Witness Optimization

When the second-stage witness size `m2` is small, setup can precompute a matrix `H` of group elements so Bob computes the second-phase-only quotient contribution as a quadratic form over `zII` instead of running a full FFT-style quotient computation. This gives second-phase time `O(m2^2)` when `m2` is below the relevant square-root threshold; otherwise Bob falls back to `O(|C| log |C|)`-style quotient computation.

### Split Zero-Knowledge Masking

The direct split construction would leak first-phase material through the aux state. To fix this, the paper modifies the R1CS with dummy/random witness wires `r1, r2, r3, r4` and three extra constraints, using these variables to mask the aux elements. The construction then proves perfect split zero-knowledge by showing that a simulator with setup trapdoor values can sample aux distributions identical to real execution.

This means the final scheme is not simply "take an existing Groth16 SRS and divide the prover code." It needs `Setupsplit` for the modified relation, but the final verification algorithm remains Groth16-style.

## Efficiency And Lower Bound

| Quantity | Paper's claim | Interpretation |
| --- | --- | --- |
| First phase | `O(|CI| * |C| log |C|)` in the theorem statement, with detailed accounting in FFT/MSM terms. | Alice can do substantial work before the whole witness exists; this phase may be heavy but can happen early/offline. |
| Second phase | `O(min{|CII|^2, |C| log |C|})`. | If the late witness/circuit is small, Bob's online completion can be much cheaper than a full Groth16 prover. |
| Aux communication excluding `aux0` | `(2m2 + 4)|G1| + 1|G2|`. | Communication grows with second-phase witness size, not full circuit size. |
| Proof size | Same asymptotic size as Groth16: two `G1` elements and one `G2` element. | Verifier-side compatibility is a central design goal. |
| SRS size | Still `O(n + m)` asymptotically, plus optional split setup material. | Setup is specialized for split proving but not asymptotically larger in the main statement. |
| Lower bound | Any Groth16 split prover of this form needs `Omega(min{|CII|^2, |C|})` group elements/operations in the second phase under the paper's model. | The second phase is essentially optimal for Groth16, so large gains require a different proof system or assumptions. |

## Application Notes

| Application | How Split Proving Helps | Boundary |
| --- | --- | --- |
| Delegatable payments / Zerocash-style JoinSplit | Alice can precompute ownership, membership, and old-coin validity material before the final transaction amount/new output witnesses are known. | Bob must not learn old-coin secrets or be able to authorize transactions independently. |
| Anonymous credentials | Credential validity and ownership can be handled early; late-selected disclosed properties or predicates can be completed later. | The credential-specific statement split must expose only allowed intermediate outputs. |
| Hybrid encryption / ciphertext validity | Key-encapsulation-like material can be known early, while final message/ciphertext pieces arrive later. | The paper frames this as a broader pattern, not a fully evaluated implementation. |

## Boundary With Neighboring Knowledge

| Neighbor | Similarity | Difference / Non-transfer |
| --- | --- | --- |
| [[private-delegated-proving|Private delegated proving]] | Both care about outsourcing prover computation without exposing sensitive witness material. | Split prover handles naturally staged witness availability and often a single assistant; Siniel-style private delegation assumes full witness outsourcing to multiple workers under threshold assumptions. |
| [[distributed-proof-generation|Distributed proof generation]] | Both reduce prover-side burden by involving another party or machines. | Split prover is not general data-parallel proving; it is about phase separation, authorization and aux privacy. |
| [[recursion-and-folding|Recursion and folding]] | Both break proof generation into stages and can support incremental workflows. | IVC/recursive SNARKs normally change verifier semantics/proof composition and often rely on non-black-box random-oracle/generic-group style machinery; split prover keeps the original Groth16 verifier and uses black-box cryptography in the paper's framing. |
| [[zk-snarks|zk-SNARKs]] | The construction is a Groth16 zkSNARK variant and preserves the final proof/verifier interface. | It is not a new general definition of zk-SNARKs; Groth16 specifics and lower bound remain source-local. |

## Evidence Table

| Claim / Finding | Anchor | Confidence | Handling |
| --- | --- | --- | --- |
| The paper initiates split prover zkSNARKs as a reusable model. | Abstract; Section 1; Section 3 | high | create [[split-prover-zksnarks|Split prover zkSNARKs]] |
| Verifier cannot tell whether proof was generated in one phase or split. | Abstract; Section 3; Section 4 theorem | high | method-family property |
| Aux state must hide first-phase witness beyond `CI(xI,wI)`. | Section 3, p10-p11 | high | privacy boundary |
| The construction is Groth16-based and preserves the Groth16 verifier. | Abstract; Section 2.3; Section 4 | high | source extension to [[zk-snarks|zk-SNARKs]] |
| The `pi3` quotient contribution is the core technical obstacle. | Section 4.1-4.2 | high | source-local detail |
| The second prover time is asymptotically tight for Groth16 under the paper's lower-bound model. | Section 5 | high | source-local theorem |
| Random-oracle Fiat-Shamir SNARKs face a barrier for split precomputation because challenges depend on later transcript content. | Section 1.3 | medium | bridge boundary to [[recursion-and-folding|Recursion and folding]] |

## Knowledge Handoff

| Target | Action | Why |
| --- | --- | --- |
| [[split-prover-zksnarks|Split prover zkSNARKs]] | Create new child knowledge node under private delegated proving. | The split gate passes: this is a reusable problem/method family, not merely the paper's system name. |
| [[private-delegated-proving|Private delegated proving]] | Add split-prover route alongside Siniel-style full-witness delegation. | It expands the taxonomy from "hide whole witness while outsourcing" to "hide early witness while completing later." |
| [[distributed-proof-generation|Distributed proof generation]] | Add as a privacy/phase-aware subroute, not as data-parallel scaling. | Query routing needs to distinguish split proving from DIZK/Pianist/Hekaton. |
| [[zk-snarks|zk-SNARKs]] | Add as Groth16-compatible source extension. | The verifier/proof interface remains Groth16, but the foundation node should not absorb all construction detail. |
| [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] | Create bridge. | The paper explicitly contrasts split proving with IVC/recursive SNARKs; the relation is useful but has hard non-transfer boundaries. |

## Cold-Start Hierarchy

```text
zero-knowledge-proofs
  proof-systems
    distributed-proof-generation
      private-delegated-proving
        split-prover-zksnarks
          source: Split Prover Zero-Knowledge SNARKs
    zk-snarks
      Groth16-compatible source extension
  recursion-and-folding
    contrast bridge: split-prover-zksnarks-to-recursion-and-folding
```

## Retrieval Optimization

- Use this source note for exact Groth16 construction details: split R1CS, quotient decomposition, `H` matrix, masking wires, theorem/lower bound.
- Use [[split-prover-zksnarks|Split prover zkSNARKs]] for the reusable problem statement and method-family taxonomy.
- Use [[private-delegated-proving|Private delegated proving]] to compare split proving against Siniel/EOS/zkSaaS-style delegation.
- Use [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] when asking whether split proving can be replaced by IVC/recursive SNARKs.

## Domain Dynamics Impact

- Research dynamics note: not updated from external freshness evidence.
- Structural impact: adds a new child problem under private delegated proving and a contrast bridge to recursion/folding.
- Foundation impact: does not upgrade [[zk-snarks|zk-SNARKs]] to full foundation; Groth16/PLONK/STARK foundation sources remain a gap.

## Review Items

| Item | Reason | Priority |
| --- | --- | --- |
| Confirm canonical URL / ePrint metadata for `2025-373.pdf`. | This run did not fetch external metadata. | medium |
| Absorb Groth16 primary source if not already in vault. | Split prover construction relies on Groth16 but this paper is not a Groth16 foundation source. | high |
| Track whether later split-prover constructions support PLONK/STARK/transparent systems. | The paper identifies a random-oracle Fiat-Shamir barrier; future work may change the taxonomy. | high |
| Compare with Siniel/EOS/zkSaaS primary sources once available. | Private delegated proving taxonomy currently has only Siniel and Split Prover as primary source-backed nodes. | medium |
