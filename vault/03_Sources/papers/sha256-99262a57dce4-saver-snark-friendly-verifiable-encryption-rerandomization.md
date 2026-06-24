---
id: "sha256-99262a57dce4"
title: "SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization"
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
  - "p1-p2 title, abstract, contribution summary"
  - "p2-p6 introduction, verifiable-encryption requirements, encryption-in-circuit bottleneck, SAVER positioning"
  - "p6-p10 Vote-SAVER motivation, security goals, high-level election flow"
  - "p10-p12 related work"
  - "p12-p20 preliminaries: bilinear groups, assumptions, zk-SNARKs, commit-and-prove, commit-carrying encryption, VE/VD/rerandomization definitions"
  - "p20-p28 SAVER main idea and construction, Algorithms 1-2"
  - "p28-p35 security arguments: IND-CPA, encryption knowledge soundness, rerandomizability, decryption soundness"
  - "p35-p42 Vote-SAVER algorithms and security theorems"
  - "p42-p44 experiments, timing and size table"
  - "p44-p48 conclusion and references"
canonical_url: ""
pdf_url: ""
doi: ""
arxiv_id: ""
eprint_candidate: "2019/1270 inferred from local filename; not externally verified in this run"
venue: "unknown"
year: "2020"
authors:
  - "Jiwon Lee"
  - "Jaekyoung Choi"
  - "Jihye Kim"
  - "Hyunok Oh"
affiliations:
  - "Hanyang University, Seoul, Korea"
  - "Kookmin University, Seoul, Korea"
local_pdf: "~/Desktop/paper/2019-1270.pdf"
sha256: "99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
pages: 48
pdf_extractor: "codex-bundled-python:pypdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/2019-1270-99262a57dce4-pages.txt"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "verifiable-encryption"
  - "zk-snarks"
  - "modular-zksnarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "verifiable-encryption"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/verifiable-encryption/sha256-99262a57dce4"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-99262a57dce4"
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks/sha256-99262a57dce4"
  - "blockchain-systems/data-availability-and-light-clients/fair-data-exchange/sha256-99262a57dce4"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "blockchain-systems"
  directions:
    - "proof-systems"
    - "applications"
    - "data-availability-and-light-clients"
  topics:
    - "verifiable-encryption"
    - "zk-snarks"
    - "commit-and-prove-snarks"
    - "blockchain-voting"
    - "fair-data-exchange"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "SAVER"
  - "verifiable encryption"
  - "verifiable decryption"
  - "rerandomizable encryption"
  - "additively homomorphic encryption"
  - "zk-SNARKs"
  - "Groth16"
  - "commit-and-prove SNARKs"
  - "Vote-SAVER"
aliases:
  - "SAVER"
  - "SNARK-friendly verifiable encryption"
  - "SAVER verifiable encryption"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "zkSNARK"
  - "verifiable-encryption"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "proof systems"
    - "verifiable encryption"
    - "zk-SNARK applications"
  problem:
    - "prove statements about encrypted messages without embedding encryption in the SNARK circuit"
    - "bind ciphertext plaintext to a zk-SNARK witness"
    - "rerandomize ciphertext and proof to hide ballot origin"
  method_family:
    - "SNARK-friendly verifiable encryption"
    - "commit-carrying encryption"
    - "commit-and-prove compatible encryption"
    - "ElGamal-style additively homomorphic encryption"
  proof_model:
    - "pairing-based zk-SNARK"
    - "Groth16-style verification equation"
    - "D-Poly assumption"
    - "batch-PKE assumption"
  application:
    - "blockchain voting"
    - "receipt-free voting"
    - "verifiable tallying"
  bridge:
    - "zk-SNARKs to verifiable encryption"
    - "verifiable encryption to fair data exchange"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0042"
safe_for_absorption: true
source_refs:
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "pdf:~/Desktop/paper/2019-1270.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "blockchain-applications"
  - "fair-data-exchange"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Abstract and Introduction define SAVER as SNARK-friendly verifiable encryption detached from the SNARK circuit"
  - "Sections 3-4 define verifiable encryption, verifiable decryption, rerandomizable encryption and the SAVER algorithms"
  - "Sections 5-6 prove security and apply SAVER to blockchain voting"
taxonomy_version: "1.0"
---

# SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization

## 论文身份

- Title in PDF: SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization
- Queue title: SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with
- Authors: Jiwon Lee, Jaekyoung Choi, Jihye Kim, Hyunok Oh
- Visible affiliations: Hanyang University; Kookmin University
- Local PDF: `~/Desktop/paper/2019-1270.pdf`
- Stable local identity: `sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa`
- External identity: unknown in the PDF metadata. The local filename suggests IACR ePrint `2019/1270`, but this run did not fetch external metadata.
- Extractor: `codex-bundled-python:pypdf`; extraction is usable across all 48 pages, with math/table alignment degradation.

## 精读状态

- Reading status: `deep_read_complete`
- Coverage: abstract, introduction, preliminaries/definitions, SAVER construction, security arguments, Vote-SAVER protocol and security, experiment table, conclusion and references were read.
- Skipped sections: no major section was intentionally skipped.
- Extraction gaps: mathematical notation and subscripts are degraded; the experiment table has one suspicious `55.5s` entry for decryption-proof verification at 1024 bits that appears inconsistent with surrounding millisecond-scale rows, so it is recorded as table/extraction uncertainty rather than normalized silently.
- Safe for absorption: yes. The note supports durable knowledge about verifiable encryption as a reusable proof-system method family, and about SAVER as one source instance.

## 章节地图

| 覆盖范围 | 主要内容 | 作用 |
| --- | --- | --- |
| p1-p2 | Abstract | 定义 SAVER 的目标: 将 encryption 从 SNARK circuit 中分离，同时保留 verifiable encryption/decryption、additive homomorphism、rerandomization。 |
| p2-p6 | Introduction | 说明 naive encryption-in-circuit 的 proving time/CRS blow-up，并提出 ciphertext/plaintext 与 proof witness 的一致性问题。 |
| p6-p10 | Vote-SAVER overview | 把 SAVER 应用于 blockchain voting，强调 voter-held secret key、receipt-freeness、individual verifiability、tally uniqueness、voter anonymity。 |
| p10-p12 | Related work | 定位 pairing-based zk-SNARKs、LegoSNARK/commit-and-prove、voting systems。 |
| p12-p20 | Preliminaries | 给出 bilinear groups、D-Poly/batch-PKE assumptions、zk-SNARK、commit-carrying SNARK、commit-and-prove SNARK、commit-carrying encryption、VE/VD/rerandomization 定义。 |
| p20-p28 | SAVER construction | 对比 Algorithm 1 naive route；Algorithm 2 给出 Setup/KeyGen/Enc/Rerandomize/Verify Enc/Dec/Verify Dec。 |
| p28-p35 | Security | 证明 IND-CPA、encryption knowledge soundness、rerandomizability、perfect decryption soundness。 |
| p35-p42 | Vote-SAVER | 给出 voter/node/admin algorithms、Merkle membership、serial number、防重复投票、rerandomized ballot 和 tally flow。 |
| p42-p44 | Experiments | Vote-SAVER relation evaluation: proving time、encryption/verification/decryption/rerandomization costs、CRS/key/ciphertext/proof sizes。 |
| p44-p48 | Conclusion/references | 总结 SAVER 与 Vote-SAVER，并列出依赖/对照来源。 |

## Hierarchy Candidate Classification

| Layer | Candidate | Confidence | Evidence |
| --- | --- | --- | --- |
| L1 Domain | `zero-knowledge-proofs` | high | 论文核心是 pairing-based zk-SNARK 与 proof/encryption composition。 |
| L2 Direction | `proof-systems` | high | SAVER 是证明系统与加密接口的构造，不是单纯投票协议或链上系统。 |
| L3 Topic | `verifiable-encryption` | high | 论文直接定义并构造可验证加密、可验证解密、可重随机化和同态属性。 |
| Secondary | `zero-knowledge-proofs/proof-systems/zk-snarks` | high | SAVER 依赖 Groth16-like pairing-based zk-SNARK verification equation。 |
| Secondary | `zero-knowledge-proofs/proof-systems/modular-zksnarks` | medium | 论文用 commit-and-prove/commit-carrying 思路让 ciphertext 携带 commitment，并兼容后续证明。 |
| Secondary | `blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | medium | FDE 节点需要 VE/VECK 基础；SAVER 是 generic VE evidence，但不是 fair exchange protocol。 |

Alternative placements considered: `blockchain voting` is an application instance rather than the reusable method family. `proof-system-foundations` is too broad; the precise reusable node is `verifiable-encryption`.

## One-Sentence Contribution

SAVER constructs a pairing-based, SNARK-friendly verifiable encryption scheme that binds encrypted messages to a zk-SNARK witness without placing the encryption algorithm inside the SNARK circuit, while adding homomorphism, verifiable decryption and rerandomization.

## Problem Setting

Many zk-SNARK applications need two guarantees at once: data should remain encrypted, and the public should verify that the encrypted plaintext satisfies a relation. Blockchain voting is the paper's running example: a ballot must be confidential, but validity such as one-hot vote constraints and voter eligibility must still be checked.

The straightforward solution is to put the encryption algorithm into the SNARK circuit and prove that the ciphertext was produced correctly. The paper argues this is unattractive because pairing, hash, public-key encryption, or access-policy logic can make the circuit large, which increases proving time and CRS size. The paper cites prior RSA-OAEP-in-circuit work as already costly and treats more advanced encryption as even worse.

The core consistency problem is not merely to have an encryption and a proof side by side. A verifier must know that the message used in the proof and the message encrypted in the ciphertext are the same. SAVER addresses this by designing encryption that exposes a commitment-compatible handle, then modifying the pairing-based SNARK verification equation so ciphertext components can stand in for encrypted witness statements.

## Method Overview

### 1. Verifiable Encryption Requirements

The paper refines verifiable encryption as an algorithm that outputs `(π, CT)`, where `CT` encrypts a message and `π` proves that the encrypted message satisfies a public relation. The requirements include:

- completeness: honest encryption/proof verifies;
- indistinguishability/IND-CPA-style privacy for encrypted messages;
- encryption knowledge soundness: a valid proof/ciphertext pair implies a witness/plaintext consistent with both;
- consistency between the encrypted message and the proved relation.

SAVER further adds verifiable decryption and rerandomization. Verifiable decryption lets anyone check that a revealed plaintext comes from a ciphertext without knowing the secret key. Rerandomization lets a third party re-randomize both ciphertext and proof so origin linkage is hidden.

### 2. Commit-Carrying Encryption

Section 3.7 defines commit-carrying encryption: public-key encryption whose ciphertext can be efficiently mapped to a commitment `c = fc(CT)` to the same plaintext. This makes encryption compatible with commit-and-prove SNARKs.

This is the concept-level move that belongs in [[verifiable-encryption|Verifiable encryption]]. SAVER the system is source-specific; commit-carrying encryption is the reusable abstraction.

### 3. Why Naive Encryption-In-Circuit Is Avoided

Algorithm 1 sketches a naive construction where the SNARK relation includes encryption, rerandomization and decryption logic. This gives conceptual simplicity but reintroduces the bottleneck: the circuit must express the encryption algorithm and all relevant cryptographic operations.

SAVER's construction instead keeps encryption outside the circuit and alters the verification equation to connect ciphertext components and proof components.

### 4. SAVER Construction

The construction uses a Groth16-like pairing verification equation. If the message block appears in an encrypted statement, the ciphertext includes terms such as `X^r * G^m`. Directly plugging this into the verification equation introduces an extra randomness-dependent term. SAVER extends the CRS/key material with a cancellation component and modifies the proof element `C` so that the verifier can check the proof against ciphertext-derived commitments.

Algorithm 2 contains the system interface:

- `Setup(relation)`: generate CRS for the relation plus additional elements for SAVER's proof/ciphertext linkage.
- `KeyGen(CRS)`: generate encryption/decryption and verification keys.
- `Enc(CRS, PK, M, public statement; witness)`: split the message into blocks, encrypt with ElGamal-like randomness, produce the adjusted SNARK proof.
- `Rerandomize(PK, π, CT)`: re-randomize ciphertext and proof without decrypting or reproving the original witness.
- `Verify Enc(CRS, π, CT, public statement)`: verify ciphertext commitment consistency and the SNARK-style equation.
- `Dec(CRS, SK, VK, CT)`: decrypt short message blocks and output a decryption proof.
- `Verify Dec(CRS, VK, M, ν, CT)`: verify that the decrypted message matches the ciphertext.

The encryption is ElGamal-like over group elements, giving additive homomorphism over encoded message blocks. Because decryption recovers discrete logs of group elements, messages must be split into short blocks. The text gives a small-block intuition and the experiment uses fixed block sizes; the exact block-size normalization should remain source-local.

### 5. Encrypt-With-Prove And Encrypt-And-Prove

SAVER primarily supports an `Enc-with-Prove` mode: the relation is fixed at setup/CRS time and the encryption output includes a proof for that relation. The paper also describes `Enc-and-Prove` compatibility: because ciphertexts carry a commitment-like component, later CP-SNARK-style proofs can prove additional properties about already-encrypted data.

This is why the paper is connected to [[modular-zksnarks|Modular zkSNARKs]] and [[zk-snarks|zk-SNARKs]], but it should not be stored as a new `SAVER` knowledge node. The reusable layer is `verifiable-encryption`.

## Security Content

| Security property | Paper argument | Dependencies / boundary |
| --- | --- | --- |
| Zero-knowledge preservation | The adjusted proof distribution is argued to match the underlying SNARK proof distribution. | Pairing-based SNARK construction and rerandomization details are source-specific. |
| IND-CPA | Theorem 1 proves privacy under a Decisional Poly assumption via a hybrid argument over message blocks. | New/extended D-Poly assumption; short block encoding. |
| Encryption knowledge soundness | Theorem 2 reduces a valid false proof/ciphertext relation to batch-PKE or conjoined Groth16 soundness failure. | Assumes added CRS elements do not break conjoined Groth16 soundness. |
| Rerandomizability | Rerandomized ciphertext/proof distribution matches fresh encryption/proof distribution. | Important for Vote-SAVER anonymity and receipt-freeness. |
| Perfect decryption soundness | Theorem 3: a valid decryption proof forces the decryption proof element to correspond to the ciphertext randomness/key relation. | Does not make decryption efficient for arbitrary large messages; short block search remains. |

## Vote-SAVER Application

Vote-SAVER uses SAVER to avoid election authorities holding voter secret keys. Each voter keeps a secret `skID`; public identity entries are committed in a Merkle tree. A ballot includes:

- election id `eid`;
- serial number `sn = H(eid || skID)` to detect double voting without revealing the voter;
- SAVER ciphertext/proof for vote validity and membership in the voter registry;
- rerandomized proof/ciphertext uploaded by blockchain nodes.

Nodes verify the encrypted proof, reject duplicate serial numbers, rerandomize the ballot, and publish it. Tallying uses additive homomorphism over ciphertexts and verifiable decryption for public tally checking.

The paper claims or proves these security goals in its model:

- board integrity from the blockchain board;
- receipt-freeness from IND-CPA plus rerandomization;
- individual verifiability and non-repudiation from encryption soundness and hash collision resistance;
- eligibility verifiability from SAVER encryption soundness;
- tally uniqueness from verifiable decryption soundness;
- voter anonymity from SAVER zero-knowledge.

Boundary: Vote-SAVER is an application/source instance. Its Merkle membership, election authority, threshold decryption discussion and blockchain-board assumptions stay in this source note unless future sources justify a separate `blockchain voting` knowledge node.

## Evaluation

The experiment implements a Vote-SAVER relation using libsnark on Ubuntu 18.04 with an Intel i5 3.4GHz quad-core CPU and 24GB memory. The relation includes voter membership and one-hot vote validity for a Merkle tree of height 16.

| Message size | Setup | Enc excluding SNARK proof | SNARK prove | Verify Enc | Dec | Rerandomize | CRS | CT | π |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 256 bits | 2.67s | 1.6ms | 0.73s | 8.2ms | 37.7ms | 0.02ms | 16MB | 477B | 128B |
| 512 bits | 2.67s | 2.4ms | 0.73s | 12.7ms | 75.2ms | 0.03ms | 16MB | 749B | 128B |
| 1024 bits | 2.69s | 7.4ms | 0.73s | 21.7ms | 149.7ms | 0.04ms | 16MB | 1293B | 128B |
| 2048 bits | 2.72s | 8.8ms | 0.74s | 39.8ms | 300.4ms | 0.06ms | 16MB | 2381B | 128B |

The paper's headline comparison is that encryption overhead is small compared with SNARK proving, and CRS size stays fixed by the relation rather than growing with encryption-circuit size. Key-size rows are also reported: secret key 32B, public/verification keys grow with message size, and decryption proof `ν` is 32B.

Review caveat: the extracted table shows one `55.5s` value for `Verify Dec` at 1024 bits, inconsistent with neighboring `14.8ms`, `28.3ms`, and `110.1ms` rows. Keep this as a PDF/table verification item rather than a normalized benchmark fact.

## Evidence Table

| Finding | Evidence anchor | Confidence | Notes |
| --- | --- | --- | --- |
| SAVER's core problem is proving relations about encrypted messages without embedding encryption in the SNARK circuit. | Abstract; Introduction p1-p5 | high | This is the primary classification evidence. |
| Commit-carrying encryption is the abstraction that makes encryption compatible with commit-and-prove style composition. | Definition 5 / Section 3.7 | high | Promoted to [[verifiable-encryption|Verifiable encryption]], not a SAVER-specific node. |
| SAVER is tied to pairing-based/Groth16-style SNARK equations. | Section 4 / Algorithm 2 | high | Bridge boundary for [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]]. |
| Additive homomorphism enables tallying encrypted votes. | Section 4 and Vote-SAVER sections | high | Application detail belongs to source and application bridge. |
| Rerandomization is needed for Vote-SAVER origin unlinkability. | Abstract; Vote-SAVER security sections | high | Important for receipt-freeness and anonymity. |
| SAVER does not by itself provide fair exchange/payment atomicity. | Inference from scope; comparison to FDE source | high | This boundary is recorded in [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]]. |

## Knowledge Handoff

| Candidate | Handling | Target | Reason |
| --- | --- | --- | --- |
| Verifiable encryption | new knowledge node | [[verifiable-encryption|Verifiable encryption]] | Reusable method family; now supported by FDE's VECK motivation plus SAVER's generic construction. |
| SAVER | source instance | this note + source-extension rows | Paper-specific construction; should not become a foundation node. |
| zk-SNARKs | update source extension | [[zk-snarks|zk-SNARKs]] | SAVER shows an application/composition route, not a foundation upgrade. |
| Modular zkSNARKs / commit-and-prove | source extension / bridge evidence | [[modular-zksnarks|Modular zkSNARKs]]; [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]] | Commit-carrying encryption borrows CP-SNARK compatibility. |
| Vote-SAVER | source-local application instance | this note | Single paper application; do not split unless more voting sources arrive. |
| Fair data exchange | bridge/application relation | [[fair-data-exchange|Fair data exchange for committed data]]; [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]] | SAVER supplies generic VE foundation; FDE still requires payment/key-release and commitment-specific VECK. |

## Cold-Start Hierarchy Discovery

| Facet | Value | Evidence | Durable handling |
| --- | --- | --- | --- |
| Research field/domain | zero-knowledge proofs | title, abstract, definitions | existing L1 domain |
| Research background | zk-SNARKs combined with encryption causes circuit-cost and consistency problems | Introduction | [[proof-systems|Proof systems]] and [[zk-snarks|zk-SNARKs]] source extension |
| Research problem | verifiable encryption for encrypted witnesses/statements | Sections 3-4 | new [[verifiable-encryption|Verifiable encryption]] node |
| Foundation concepts | zk-SNARKs, commit-and-prove SNARKs, ElGamal-style homomorphic encryption, bilinear groups | preliminaries | source-backed where present; remaining crypto foundations queued |
| Method family | SNARK-friendly commit-carrying verifiable encryption | Sections 3.7-4 | knowledge method route |
| Application/evaluation context | blockchain voting; Vote-SAVER benchmark | Sections 6-7 | source-local application; possible future application node |
| Source instance | SAVER and Vote-SAVER | whole paper | source note and source-extension rows |

## Retrieval Optimization

- Queries like "SAVER 是什么" should open this source note.
- Queries like "verifiable encryption 和 zk-SNARKs 怎么结合" should open [[verifiable-encryption|Verifiable encryption]] plus [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]], and only then this source if details are needed.
- Queries like "FDE/VECK 和 SAVER 有什么关系" should open [[verifiable-encryption-to-fair-data-exchange|Verifiable encryption -> fair data exchange]], not scan all paper notes.
- Source-only details: exact `P1/P2` key elements, theorem proof reductions, Vote-SAVER algorithm steps, benchmark row values and table caveats.

## Domain Dynamics Impact

- Affected L1 domain: `zero-knowledge-proofs`
- Dynamics decision: `unchanged`.
- Reason: SAVER creates a useful method-family node and bridge, but it is an older single paper from the local queue. No web/daily freshness pass was run, so it should not refresh the domain-level "latest research dynamics" note.
- Blockchain systems dynamics: unchanged. SAVER is not a blockchain-system paper; Vote-SAVER and FDE relation are application/bridge evidence only.

## Foundation Candidate Judgment

| Term | Judgment | Reason |
| --- | --- | --- |
| Verifiable encryption | foundation_thin knowledge node | Reusable primitive/method family spanning SAVER and FDE/VECK context. |
| SAVER | source instance | Named construction from one paper; details remain in source note. |
| Vote-SAVER | source-local application | Single application protocol; not enough sources for independent node. |
| Commit-carrying encryption | method section inside verifiable encryption | Important abstraction, but currently evidence comes mainly from this paper. |
| Groth16-like construction | protocol dependency/source detail | Not a separate foundation here; belongs under zk-SNARKs when primary sources are absorbed. |

## Review Items

| Type | Item | Status |
| --- | --- | --- |
| metadata_gap | Venue/canonical URL not available in PDF metadata; filename suggests ePrint `2019/1270`, but external metadata was not fetched. | review |
| table_gap | `Verify Dec` table value for 1024-bit messages appears inconsistent in extraction/source table. | review |
| foundation_needed | General verifiable encryption canonical sources and Camenisch-Shoup-like history are not yet in the vault. | queued |
| comparison_needed | ZKCPlus/ZKCP/FairSwap/FairDownload/FileBounty sources are still needed for fair-exchange comparison. | queued |
| boundary | SAVER supports verifiable encryption and voting; it does not supply payment fairness or data-market economics. | recorded |

## Update Log

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Deep-read SAVER and handed off to verifiable-encryption knowledge node and bridges. | codex |
