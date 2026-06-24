---
id: "sha256-e52dd885d13f"
title: "BlockSketch: A Hybrid Tree-based Sketch for Account-Specific Transaction Retrieval Query"
type: "source"
source_kind: "paper"
status: "absorbed"
created: "2026-06-23"
updated: "2026-06-23"
year: "2024"
venue: "unknown"
authors:
  - "Yushi Liu"
  - "Xiaodong Qi"
  - "Zhao Zhang"
  - "Cheqing Jin"
  - "Aoying Zhou"
source_refs:
  - "sha256:e52dd885d13f5be90c84ff96c0b20110fbeb5b82f7236460bb348d28fb9a44f1"
local_pdf_path: "~/Desktop/paper/BlockSketch.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/blocksketch-e52dd885d13f-pages.txt"
queue_id: "item0100"
run_ids:
  - "nahida-paper-read-20260623-blocksketch"
  - "nahida-knowledge-20260623-blocksketch-transaction-retrieval"
primary_ontology_path: "blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage/storage-engines"
domains:
  - "blockchain-systems"
subdomains:
  - "data-management-and-storage"
topics:
  - "blockchain-query-processing-and-indexing"
  - "account-specific-transaction-retrieval"
  - "probabilistic-data-structures"
source_role: "representative_system_source"
confidence: "high"
path_update_status: "propagated"
review_status: "reviewed"
---

# BlockSketch: A Hybrid Tree-based Sketch for Account-Specific Transaction Retrieval Query

> [!summary]
> BlockSketch 把“给定账户，找出历史或近期区块中包含该账户交易的区块”建模为 Multi-Set Multi-Membership Query（MS-MMQ），并用二叉时间窗口树、Bloom filter、Sketch 与冷热账户分层编码来降低区块链账户交易检索的内存、同步与误报成本。它属于[[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing|区块链查询处理与索引]]，不是共识协议。

## Source Identity

| Field | Value |
| --- | --- |
| Title | BlockSketch: A Hybrid Tree-based Sketch for Account-Specific Transaction Retrieval Query |
| Authors | Yushi Liu; Xiaodong Qi; Zhao Zhang; Cheqing Jin; Aoying Zhou |
| Year | 2024 |
| Venue | Unknown in local PDF metadata |
| Local PDF | `~/Desktop/paper/BlockSketch.pdf` |
| Fingerprint | `sha256:e52dd885d13f5be90c84ff96c0b20110fbeb5b82f7236460bb348d28fb9a44f1` |
| Primary path | `blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing` |

## Problem Addressed

Blockchains expose transaction histories as ordered blocks, but many analytics and monitoring workloads need account-centric retrieval: given account `q` and optional time range `[s,t]`, return all blocks containing transactions involving `q`.

The paper formalizes this as:

`M_q^[s,t] = {B in B | exists tx in B, tx.acc = q and tx.ts in [s,t]}`

The desired query result is a candidate block set `hat(BT)` such that the true block set `BT` is contained in it, while minimizing false-positive blocks and memory overhead.

This problem appears in:

- DeFi or phishing account tracking.
- Regulatory and compliance monitoring.
- Blockchain analytics over historical and recent blocks.
- Transaction retrieval where full off-chain database synchronization is too costly.

## Prior Approach Landscape

| Approach family | How it handles the problem | Limitation emphasized by the paper |
| --- | --- | --- |
| On-chain or system-level query indexes | Maintain indexes inside blockchain-oriented systems such as EtherQL or SEBDB-style query layers. | Higher storage and maintenance cost. |
| Off-chain analytics synchronization | Synchronize chain data into external systems such as The Graph or BlockSci-like analysis stacks. | Doubles or greatly increases storage footprint and introduces synchronization complexity. |
| General MS-MMQ probabilistic structures | Use Bloom filter or sketch-family structures to answer multi-set membership queries. | Preallocated memory is awkward for streaming block growth; accuracy degrades for high-multiplicity accounts. |
| Bloom-tree style indexes | Store Bloom filters on tree nodes and descend on positive matches. | Can be memory-heavy because high-level nodes repeatedly encode many accounts. |

## Core Idea

BlockSketch uses the power-law distribution of blockchain account access: most accounts appear in few blocks, while a smaller set of hot accounts appears many times. Instead of encoding every account uniformly, it separates hot and cold accounts at each tree node.

The design has four coupled ideas:

- Partition recent blocks into chronological windows and build one BlockSketch per window.
- Represent blocks inside a window as leaves of a binary tree.
- Store locally hot accounts in Bloom filters because hot accounts benefit from cheap pruning.
- Store cold-account jump pointers in Sketches so the query can skip directly to the next relevant subtree.

This turns account-specific retrieval into a tree traversal that alternates between:

- **Level-down:** Bloom filter says the account is locally hot, so both children may contain it.
- **Jump:** Bloom filter says it is not locally hot, so a Sketch returns one or more candidate jump nodes.
- **Re-entry:** if a Bloom false positive led traversal down a path where the Sketch cannot continue, the query checks the parent Sketch to avoid false negatives caused by the interaction between Bloom and Sketch decisions.

## Data Model and Construction

| Concept | Meaning in BlockSketch |
| --- | --- |
| Leaf node | One block, storing the accounts present in that block. |
| Index node | A binary-tree parent whose account set is the union of its children. |
| Locally hot account | An account present in both child account sets of an index node. |
| Locally cold account | An account present in exactly one child account set. |
| Jump node | The highest descendant below the current node where the account becomes hot again, or the leaf that contains it. |
| Buffer | Temporary construction-time state that remembers jump nodes before being released. |

Construction is bottom-up as blocks arrive:

1. Create leaf nodes for new blocks.
2. Pair siblings and create parent nodes.
3. Compute hot accounts by child intersection and cold accounts by child symmetric difference.
4. Insert hot accounts into the parent Bloom filter.
5. Insert cold-to-hot transition information into Sketch tuples.
6. Merge and release buffers as nodes become complete.

## Query Processing

For a query account and time range, BlockSketch first identifies windows overlapping the requested time range. Each relevant window is searched independently, then candidate blocks are retrieved and verified to remove false-positive blocks.

Inside one window:

- Time-range pruning skips nodes outside the requested interval.
- Bloom-positive nodes trigger level-down traversal.
- Bloom-negative nodes query Sketches for jump nodes.
- Re-entry repairs the path if a Bloom false positive would otherwise hide the Sketch entry needed for a true block.

Because windows do not overlap, window-level query processing can be parallelized.

## BlockSketch+

BlockSketch+ adds flat nodes by merging every `tau` leaf nodes and sharing a Sketch among them. It removes Bloom filters inside the flat node and uses the shared Sketch to identify candidate leaves. The paper reports that `tau = 4` or `tau = 8` balances memory and accuracy well; too large a flat node can increase false positives because more accounts compete inside the same Sketch.

## Evaluation Evidence

| Aspect | Evidence reported |
| --- | --- |
| Implementation | Golang 1.22.2, about 4,000 lines of core code; standalone integration with Ethereum/geth and modified block cache for windows. |
| Dataset | Ethereum blocks from height 17,000,000 to 18,000,000 via Ethereum ETL. |
| Window size | `|W| = 1024` blocks in the main setup. |
| Workloads | Account workloads with hot-account ratios of 10%, 20%, 40%, and 60%; accounts with multiplicity above 20 in a window are treated as hot for workload construction. |
| Baselines | RAMBO, CSC, and BloomTree-style indexing. |
| Accuracy | At high hot-account ratio and 3 MB memory, BlockSketch variants stay below one false-positive case in the reported sample, while CSC and RAMBO show substantially more. |
| Multiplicity behavior | RAMBO and CSC perform very well for low multiplicity, but their false-positive rates rise sharply as multiplicity increases; BlockSketch improves for higher-multiplicity accounts because Bloom pruning absorbs hot accounts. |
| Query latency | BlockSketch reports up to 26% and 47% lower latency than CSC and RAMBO in the tested setup. |
| Time pruning | Time-range pruning reduces query time strongly for high-multiplicity accounts, with reported reductions up to 91% in one setting. |
| Memory comparison | BloomTree can be faster, but it uses about 2x memory in the reported settings and up to 2.4x as window size grows. |

## Contribution to the Knowledge Base

BlockSketch is useful as a representative source for the `blockchain-query-processing-and-indexing` problem layer:

- It distinguishes blockchain analytics retrieval from state storage, consensus, data availability, and bridge protocols.
- It provides a concrete query formulation for account-specific transaction retrieval.
- It shows how probabilistic data structures can be adapted to blockchain workloads with streaming windows and power-law account distributions.
- It creates a bridge candidate from blockchain data management to general storage-engine/indexing techniques such as Bloom filters, Count-Min Sketches, and multi-set membership indexes.

## Claims Preserved Inside This Source Note

- The central problem is account-specific transaction retrieval over block histories, not agreement or ledger ordering.
- The paper’s main mechanism is a hybrid Bloom-filter/Sketch binary tree with hot/cold local account classification.
- The false-negative repair is not automatic from Bloom and Sketch individually; it is an explicit traversal re-entry rule required by their interaction.
- The strongest empirical advantage is for high-multiplicity accounts and mixed hot-account workloads, where general sketch-based methods suffer more false positives.
- BlockSketch trades a small low-multiplicity disadvantage against better high-multiplicity accuracy and lower memory than BloomTree-style designs.

## Relations

| Relation | Target | Rationale |
| --- | --- | --- |
| instantiates_problem | [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing|Blockchain Query Processing and Indexing]] | The paper gives a concrete account-specific transaction retrieval system. |
| belongs_to_parent | [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]] | It is a blockchain data access/indexing technique. |
| method_bridge_candidate | [[04_Knowledge/distributed-systems/data-management-and-storage/storage-engines|Storage Engines]] | It uses Bloom filters, sketches, tree indexes, cache windows, and memory/accuracy tradeoffs familiar from storage engines. |
| not_a | [[04_Knowledge/blockchain-systems/blockchain-consensus|Blockchain Consensus]] | The paper does not change transaction ordering, leader election, BFT/CFT assumptions, or finality. |

## Absorption Notes

- Queue classification was corrected from `blockchain-systems/consensus/consensus-foundations` to `blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing`.
- No durable bridge note was created yet because the bridge to probabilistic data structures needs a stronger standalone method-family node before becoming a stable cross-domain bridge.
- Venue and DOI are absent from the local PDF metadata; keep them unknown unless a later metadata pass verifies them.
