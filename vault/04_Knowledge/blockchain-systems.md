---
id: "nahida-knowledge-blockchain-systems"
title: "Blockchain systems"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "domain"
hierarchy_level: "domain"
file_slug: "blockchain-systems"
domain_id: "blockchain-systems"
direction_id: ""
parent_knowledge_refs:
  []
child_knowledge_refs:
  - "nahida-knowledge-blockchain-consensus"
  - "nahida-knowledge-blockchain-systems-research-dynamics"
  - "nahida-knowledge-data-availability-and-light-clients"
  - "nahida-knowledge-blockchain-interoperability"
  - "nahida-knowledge-mempool-and-networking"
  - "nahida-knowledge-scaling-and-sharding"
  - "nahida-knowledge-blockchain-execution-and-transactions"
  - "nahida-knowledge-blockchain-data-management-and-storage"
ontology_path:
  - "blockchain-systems"
primary_ontology_path: "blockchain-systems"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-consensus"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-systems-research-dynamics"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/research-dynamics.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-data-availability-and-light-clients"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-interoperability"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/interoperability.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-mempool-and-networking"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/mempool-and-networking.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-scaling-and-sharding"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-execution-and-transactions"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-systems"
    relation: "bridges_to"
    to: "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/blockchain-coordination-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
source_note_refs:
  - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
  - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
  - "vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md"
  - "vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md"
  - "vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md"
  - "vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md"
  - "vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md"
  - "vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md"
  - "vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md"
  - "vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md"
  - "vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md"
  - "vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md"
  - "vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md"
  - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
  - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
  - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
  - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
  - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
  - "vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md"
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
representative_source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "arxiv:1905.09274v4"
  - "doi:10.14778/3476249.3476275"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "arxiv:2107.13047v2"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
  - "doi:10.1016/j.jksuci.2023.101897"
  - "arxiv:2310.10016v1"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "arxiv:1804.00399v4"
  - "arxiv:1809.09044v1"
  - "arxiv:2306.10739v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/tsc.2023.3240235"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "doi:10.3846/jcem.2023.18646"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
query_keys:
  - "Blockchain systems"
  - "blockchain-systems"
  - "区块链系统"
  - "blockchain interoperability"
  - "cross-chain protocols"
  - "trustless cross-chain bridge"
  - "permissioned cross-chain bridge"
  - "sigBridge"
  - "dynamic cross-chain data consistency verification"
  - "DCCV"
  - "cross-chain messaging"
  - "cross-chain message relaying"
  - "permissionless relayers"
  - "relayer coordination"
  - "atomic cross-chain transactions"
  - "atomic cross-chain commitment"
  - "cross-chain deals"
  - "adversarial commerce"
  - "CBC protocol"
  - "blockchain transaction execution"
  - "consensus execution co-design"
  - "data availability sampling"
  - "FRIDA"
  - "FRI-based DAS"
  - "fair data exchange"
  - "expired blob retrieval"
  - "FDE"
  - "permissioned blockchain sharding"
  - "AHL"
  - "fraud proofs"
  - "light-client fraud proofs"
  - "data availability proofs"
  - "blockchain storage"
  - "blockchain state storage"
  - "authenticated state index"
  - "COLE"
  - "Fabric++"
  - "Hyperledger Fabric transaction processing"
  - "FedChain"
  - "federated-blockchain systems"
  - "weakest chain security"
  - "Nezha"
  - "DAG-based blockchain transaction processing"
  - "address-based conflict graph"
  - "hierarchical sorting"
  - "SlimChain"
  - "stateless blockchain"
  - "off-chain storage"
  - "partial Merkle trie"
  - "L2chain"
  - "layer-2 DApp execution"
  - "split-execute-merge"
  - "RSA accumulator state digest"
  - "off-chain application data management"
  - "blockchain IPFS data management"
  - "IPFS Cluster"
  - "blockchain-coordinated distributed training"
  - "TDML"
  - "remote trainer validation"
aliases:
  - "区块链系统"
domains:
  - "blockchain-systems"
topics:
  - "data-availability-sampling"
  - "fri-iopps"
  - "fair-data-exchange"
  - "fraud-proofs"
  - "light-client-security"
  - "blockchain-state-storage"
  - "authenticated-state-indexes"
  - "permissioned cross-chain bridges"
  - "dynamic-data-consistency-verification"
  - "cross-chain-message-relaying"
  - "relayer-coordination"
  - "atomic-cross-chain-transactions"
  - "cross-chain-deals"
  - "adversarial-commerce"
  - "transaction-reordering"
  - "early-abort"
  - "cross-chain-incentives"
  - "proof-of-stake-finality"
  - "dag-based-blockchain-execution"
  - "address-based-conflict-graph"
  - "hierarchical-sorting"
  - "stateless-blockchain"
  - "off-chain-storage"
  - "partial-merkle-trie"
  - "layer-2-dapp-execution"
  - "rsa-accumulator-state-digest"
  - "off-chain-application-data-management"
  - "content-addressed-application-assets"
  - "blockchain-coordinated-training"
  - "trustworthy-distributed-ml"
tags:
  - "nahida/knowledge"
  - "nahida/domain"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-zkcross"
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
  - "nahida-knowledge-20260622-sigbridge"
  - "nahida-knowledge-20260622-dccv-dynamic-cross-chain-data-consistency"
  - "nahida-knowledge-20260622-scalable-cross-chain-messaging"
  - "nahida-knowledge-20260622-atomic-cross-chain-transactions"
  - "nahida-knowledge-20260622-cross-chain-deals"
  - "nahida-knowledge-20260622-cole-blockchain-storage"
  - "nahida-knowledge-20260622-fabric-plus-plus-transaction-processing"
  - "nahida-knowledge-20260622-fedchain"
  - "nahida-knowledge-20260622-nezha-dag-transaction-processing"
  - "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
  - "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
  - "nahida-knowledge-20260623-blockchain-ipfs-construction-data-management"
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
  - "sha256:662f70f3c28a90a2a6c0c7180ccadc1f14f57c14a130c6294d67ccff524464fb"
  - "arxiv:1905.09274v4"
  - "doi:10.14778/3476249.3476275"
  - "sha256:be219323fe92477aaa4791930fa2a2ecb50b131d5fce8e4e995fba1b1613111e"
  - "arxiv:2107.13047v2"
  - "arxiv:1802.07240"
  - "arxiv:2203.05158"
  - "doi:10.1145/3600006.3613164"
  - "sha256:5d39afb8a188d566658c5ac0907657f35d853af10c13250441d9e46729019a1e"
  - "sha256:7ab37dce93ba441fb81d4cde9a1489321a3b18c78348d6c269a5eac1b9e420d8"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:9b3cfce6e0183bdece8ce0a8bf762b10b4e717b183049a5146c7b477e13ab7c1"
  - "doi:10.1016/j.jksuci.2023.101897"
  - "arxiv:2310.10016v1"
  - "arxiv:1905.02847v2"
  - "doi:10.14778/3364324.3364326"
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "arxiv:1804.00399v4"
  - "arxiv:1809.09044v1"
  - "doi:10.48550/arxiv.1809.09044"
  - "arxiv:2306.10739v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/tsc.2023.3240235"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "doi:10.3846/jcem.2023.18646"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
confidence: "medium"
trust_tier: "primary"
---

# Blockchain systems

## 定义与范围

- 定义: Blockchain systems 组织区块链中的共识、finality、mempool/networking、sharding、data availability 和链上/链下执行边界。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `blockchain-systems`
- Aliases/query keys: 区块链系统
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `blockchain-systems`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: [[04_Knowledge/blockchain-systems/research-dynamics|Research dynamics]]

## 背景

该域把分布式系统、密码学、经济激励和工程实现结合起来。当前 vault 证据来自 Tendermint、Casper FFG、SRaft、OmniLedger、LazyLedger、ByShard、RingBFT、AHL、Cobalt、Stratus、MyTumbler/SuperMA、EPIC、zkCross、zkBridge、sigBridge、DCCV、Scalable Cross-Chain Messaging、FedChain、TELL、Fabric++、Nezha、SlimChain、L2chain、FRIDA、Atomic/Fair Data Exchange、Fraud Proofs、COLE 和 Blockchain + IPFS construction data management。

## 基础概念判断

- 是否是基础概念/方向/问题: `domain` / `domain`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: root domain。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

回答区块链如何在开放或许可环境中排序交易、达成 finality、扩容和降低验证成本。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| root | L1 domain/root | canonical current architecture | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[blockchain-consensus|blockchain-consensus]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[mempool-and-networking|mempool-and-networking]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[scaling-and-sharding|scaling-and-sharding]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[data-availability-and-light-clients|data-availability-and-light-clients]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[interoperability|interoperability]] | child | zkCross introduces cross-chain privacy-preserving auditing and protocols | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] | active_seed |
| [[execution-and-transactions|execution-and-transactions]] | child | TELL exposes a reusable execution/transaction layer that should not be folded into consensus | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | active_seed |
| [[data-management-and-storage|data-management-and-storage]] | child | COLE exposes full-node state storage, authenticated indexes, historical provenance, and state-root maintenance; later sources add stateless storage and application-data off-chain assets as reusable blockchain data-management problems distinct from consensus/execution | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]]; [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Blockchain + IPFS construction data management]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| BFT/PoS finality 与治理 | BFT/PoS finality 与治理 | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| shared mempool 与 ordering/data split | shared mempool 与 ordering/data split | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| sharding 与跨 shard 原子性 | sharding 与跨 shard 原子性 | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| permissioned/general-workload sharding | 用 TEE-assisted BFT、随机组片和 BFT reference committee 支持非 UTXO/general workload 的分片执行。 | 许可链、每节点具备 TEE、希望用 shard-level BFT 扩容。 | TEE/SGX 信任强；reference committee 和 chaincode refactoring 是工程瓶颈。 | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| data availability sampling 与 client-side execution | data availability sampling 与 client-side execution | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| transparent data availability commitments | 用 proof-system/FRI machinery 为 light clients 提供无 trusted setup 的 DAS commitment/opening route。 | data availability layer 需要优化 light-client query bandwidth and setup assumptions。 | 不等于 transaction validity；network encoding/storage trade-off 留在 DAS 节点。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| committed-data fair retrieval | 在数据承诺留存而数据本体过期、分散或由 archive servers 持有时，用 FDE/VECK 让客户端公平购买正确数据或片段。 | EIP-4844 expired blobs、Danksharding fragments、off-chain/archival data services。 | 不替代 DAS/validity proof；链下证明与带宽、定价和 griefing 仍是瓶颈。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |
| fraud-proof-backed light-client validation | 用状态转换 fraud proof、codec fraud proof 和 DAS 组合，让 light clients 在数据可用时拒绝无效区块/错误编码。 | light-client security、sharded systems、optimistic validation；至少一个 honest full node 能看到数据。 | 依赖 DA、gossip/anti-eclipse 和 sampling mass；不等于 validity proof，也不解决 shard execution。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| interoperability and cross-chain auditing | 处理多链之间资产/状态/审计交互，并在隐私、原子性和审计效率之间折中。 | 多链系统需要 transfer/exchange/audit，且不希望引入过强 trusted third party。 | 需要额外证明、审计链、committer 假设、gas/proving 预算和匿名集合设计。 | [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]] |
| permissioned cross-chain bridge verification | 用已知成员/共识签名/threshold rules 让目标链 updater contract 验证源链 block headers，并按 `t` 个抽样签名在成本和错误概率之间折中。 | 许可链或联盟链之间的跨链同步，源链 validator public keys 与 consensus rules 可被目标链治理接入。 | 不替代 relayer liveness、Merkle/state proof、trusted setup 和异构共识抽象；signature count 增大时 gas/data size 增长。 | [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge]] |
| dynamic cross-chain data consistency auditing | 用 audit chain、dynamic Merkle hash tree 和 decentralized chameleon hash 检查 source-chain 动态数据更新是否被 target-chain 完整同步。 | 监管/联盟链场景中，多链存储或交互的数据需要可更新且需要跨链副本一致性。 | 依赖 honest audit chain/data owner、threshold key governance、CoSi/multi-signcryption 和合约正确性；不是 trustless permissionless bridge。 | [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|DCCV]] |
| cross-chain relayer coordination | 用 Coordinator、registered relayer set、collateral、task allocation、acknowledgement 和 timeout slashing 协调跨链消息运输。 | Permissionless relayers 重复竞争同一消息，导致 gas waste、吞吐不扩展或强 relayer 垄断时。 | 不替代 light-client/proof correctness；牺牲一部分 redundancy；真实 IBC/relayer ecosystem 仍需 sources。 | [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Scalable Cross-Chain Messaging]] |
| atomic cross-chain transaction coordination | 用 witness/global ledger 或等价 evidence source 协调多条 asset chains 上的 redeem/refund decision，避免 split outcome。 | 多链资产转移/交换需要 all-or-nothing 语义，且不想使用中心化交易所或可信 coordinator。 | HTLC/timelock 有 crash/delay 边界；witness route 需要 finality、fork-depth、attack economics 和跨链 evidence validation。 | [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] |
| execution/transaction processing | 在 ordering/finality 之后或之间执行交易、处理冲突、重执行和提交，并与 consensus/mempool/storage 边界协同。 | 并行执行、leaderless consensus、sharding 或高吞吐许可链。 | execution 优化不等于 consensus safety；高冲突 workload 会增加 abort/re-execution。 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| database-inspired Fabric transaction processing | 用 transaction reordering、early abort 和 conflict graph 把数据库事务管理思想迁移到 Fabric simulate-order-validate 执行管线。 | Hyperledger Fabric-style permissioned chains，readset/writeset 可见且 orderer/peer 可确定性执行规则。 | 不改变 consensus/endorsement safety；Fabric++ 只做 block-local reordering。 | [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] |
| DAG-based blockchain concurrent transaction processing | 用 address-based conflict graph 和 hierarchical sorting 在 epoch-level concurrent blocks 上检测/排序冲突交易，并保留 commit concurrency。 | account-based main-chain/parallel-chain DAG blockchains，block concurrency 高且 read/write addresses 可记录。 | 不提供 consensus safety；不适用于 UTXO/natural-DAG irregular topology；实验为 OHIE/EVM/SmallBank。 | [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] |
| authenticated state storage | 用 state root、Merkleized storage、历史版本布局和可验证 query/provenance proof 管理全节点状态数据。 | archival/full-node storage pressure、state history query、authenticated indexes。 | 不解决共识安全、DA、fork/rewind 或 stateless clients；存储引擎优化必须保持 root digest determinism。 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| stateless/off-chain execution-storage split | consensus nodes 只保存 transaction digests 和 state roots，off-chain storage nodes 保存 full state/full transactions 并提供 execution/read/write/write-proof evidence。 | smart-contract blockchain 中 consensus-node storage/execution pressure 明显。 | 依赖 execution proof、storage-node availability、proof compression 和 recent-window metadata；storage sharding 不等于 consensus sharding。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] |
| layer-2 DApp split-execute-merge | L1 只维护 available-state digest，DApp executors 在 L2 排序/TEE 执行交易，并用 split/merge 事务回写状态摘要。 | DApp 需要减少 L1 处理压力，同时保护交易内容和执行顺序正确性。 | 依赖 TEE、RSA accumulator witness cache 和 L1 split/merge latency；不是完整 rollup/DA/fraud-proof architecture。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] |
| on-chain metadata with off-chain application assets | 链上记录业务元数据、版本、时间戳、权限和 CID；链下内容寻址存储保存照片、视频、BIM、文档等大对象。 | 多组织应用需要可审计数据流，但文件本体太大或太敏感，不适合直接写入 block。 | CID 不等于可用性；需要 pinning/replication/lifecycle policy，且不替代 DA 或 state storage。 | [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Blockchain + IPFS construction data management]] |
| PoS-secured federated blockchain transfer | 把 cross-chain SPV transfer、individual-chain PoS finality 和 multi-chain reward/stake distribution 放在一个系统安全框架里。 | 多条 PoS/federated chains 之间进行 token transfer。 | 不覆盖全部 bridge/message/privacy；Stackelberg model 是分析模型，不是 production incentive proof。 | [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper the Friendly Finality Gadget]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 补入 permissioned/general-workload sharding route：AHL+、TEE RandomnessBeacon、batch reconfiguration、BFT reference committee + 2PC/2PL | TEE 信任假设强；SGX simulation-mode evaluation；reference committee scaling 未完整解决 | §3-§7 |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | paper | 新增 interoperability/cross-chain protocols source extension：CLE/IPA/FAI、two-layer audit chain、ZK transfer/exchange/auditing | single source; modified geth/Solidity; proof/gas/anonymity-set boundaries | `p1-p17` |
| [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control]] | paper | 新增 interoperability/consensus bridge source extension：permissioned consensus signatures 作为跨链 header verification material，并用 ABAC resource-sharing 做应用演示 | single source; trusted setup; PoA/private-Ethereum prototype; not a full access-control foundation | `p1-p10` |
| [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|A secure dynamic cross-chain decentralized data consistency verification model]] | paper | 新增 interoperability/cross-chain protocols source extension：动态数据跨链传输和更新的一致性审计，使用 audit chain、dynamic MHT 和 decentralized chameleon hash | single source; honest audit-chain/data-owner assumption; Fabric synthetic evaluation; not a full dynamic-data-auditing foundation | `p1-p13` |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | paper | 新增 interoperability/cross-chain protocols source extension：把跨链消息运输层的 relayer races、non-scaling throughput、censorship risk 和 coordination incentives 抽成子问题 | single source; no benchmark; not a bridge-verification proof or production relayer study | `p1-p8` |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | paper | 新增 interoperability/cross-chain protocols source extension：把多链资产交易的 all-or-nothing 语义抽成 atomic cross-chain transactions 子问题 | arXiv preprint; analytical evaluation; witness-chain finality/fork/evidence validation assumptions | `p1-p19` |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | paper | 新增 execution-and-transactions 分支；说明 transaction execution 可针对 leaderless consensus instances 做协同优化 | same data-center; RCC+PBFT; throughput excludes consensus latency | `p1-p13` |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric]] | paper | 补强 execution-and-transactions 分支；说明 Fabric EOV transaction processing 可用数据库式 conflict graph reordering 和 early abort 改善 successful throughput | Fabric/Fabric++ source instance; permissioned LAN evaluation; block-local reordering | `p1-p18` |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains]] | paper | 补强 execution-and-transactions 分支；说明 DAG/parallel-chain block production 需要 epoch-level concurrent execution、address-based conflict graph 和 deterministic hierarchical sorting | OHIE/EVM prototype; account-based DAG; SmallBank workload; no production deployment | `p1-p11` |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | paper | 补强 execution-and-transactions 与 data-management/storage 的交界；说明 stateless consensus node 需要 off-chain full state、read/write evidence、partial Merkle trie 和 OCC/SSI commit protocol | SGX-centered prototype; storage-node availability/incentives unresolved; storage sharding does not shard consensus | `p1-p13` |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | paper | 补强 execution-and-transactions 与 data-management/storage 的交界；说明 layer-2 DApp execution 可由 L1 accumulator digest split/merge 与 L2 TEE execution 共同定义。 | TEE trust; RSA accumulator witness overhead; not a full rollup/DA/fraud-proof source | `p1-p14` |
| [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Decentralized System for Construction Projects Data Management Using Blockchain and IPFS]] | paper | 补强 data-management/storage 的 application-data 分支；说明大对象可由链上 metadata/CID 与 private IPFS/IPFS-Cluster 共同管理 | construction case study; CFT Fabric assumption; manual data capture; private-cluster availability boundary | `p1-p18` |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | paper | 新增 data-availability/light-client source extension：transparent FRI-based DAS commitment route and proof-system bridge | single source; no deployment evidence; encoding size trade-off | `§3-§5` |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 新增 data-availability/light-client adjacent source extension：committed-data paid retrieval and service incentives via FDE/VECK | single source; VECK/fair exchange foundation thin; repo not analyzed | `p1-p25` |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities]] | paper | 新增 data-availability/light-client source extension：fraud proofs + DAS for invalid-block detection under dishonest majority | single central seed; modern rollup/Celestia/Ethereum specs still missing | `§3-§7` |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | paper | 新增 data-management/storage 分支；把 full-node state storage、authenticated indexing、provenance query 和 storage-engine adaptation 从 consensus 中拆出 | non-forking blockchain; no rewind; learned index is not integrity layer; artifact repo not analyzed | Abstract, §1-§8 |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | paper | 新增跨 consensus/interoperability 的 source extension：FedChain 说明 cross-chain transfer security depends on PoS finality and stake distribution incentives。 | single paper; simulations/analysis; no production repo | `p1-p13` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: 当前 blockchain-systems 是 source-backed seed，覆盖 consensus/scaling/DA/mempool/interoperability/execution/storage。AHL 新增的结构性信号是 scaling-and-sharding 不只包含 UTXO/payment-ledger sharding，还包含 permissioned/general-workload sharding：TEE-assisted non-equivocating BFT 影响 committee sizing，BFT reference committee 把 2PC/2PL 迁移到 Byzantine shard 环境。zkCross 新增的结构性信号是 interoperability 需要把 cross-chain transfer/exchange/audit 的原子性、隐私、审计效率和第三方信任边界一起处理；sigBridge 新增的结构性信号是 permissioned consensus signatures 可以被 interoperability 层复用为 remote-header verification material，但这种复用依赖 trusted setup、known validators 和 signature verification cost；DCCV 新增的结构性信号是跨链互操作还包含 dynamic data consistency：source-chain 上可授权更新的数据若复制到 target-chain，就需要 audit-chain-backed verification 检查传输完整性和更新同步；Scalable Cross-Chain Messaging 新增的结构性信号是 interoperability 还必须处理 relayer transport：消息正确性证明之外，permissionless relayers 的任务竞争、激励、timeout 和抗审查会决定跨链消息系统是否可扩展；Atomic Commitment Across Blockchains 新增的结构性信号是 interoperability 还必须处理跨链原子性：多链资产 movement 需要共同 commit/refund decision，且 witness/finality/evidence-validation 边界不能被 HTLC 或 bridge verification 概括掉；Cross-chain Deals 进一步说明跨链原子性不等于简单 atomic swap，broker/auction/arbitrage 等复杂 deal 需要 compliant-party acceptable payoff、escrow liveness、timelock 与 certified-blockchain 路线；TELL 新增的结构性信号是 execution layer 需要作为独立方向处理 transaction execution、conflict serialization、commit/re-execution 与 consensus instance 状态的协同；Fabric++ 进一步说明 execution layer 与 database transaction processing 有直接桥接：即使不替换 Fabric substrate，也可以用 block-local reordering 和 early abort 减少 validation abort；Nezha 进一步说明 execution layer 的并发问题也出现在 DAG/parallel-chain block production：共识阶段并发出块后，执行阶段需要 epoch-level concurrent execution、address-based conflict graph 和 deterministic hierarchical sorting；SlimChain 进一步说明 execution 与 storage 之间存在结构性耦合：当 consensus nodes stateless 化并只保存 state roots 时，transaction processing 必须携带 off-chain execution evidence、read/write metadata、write proofs 和 partial authenticated commitments；L2chain 则从 L2 DApp route 说明同一个耦合可以由 accumulator available-state digest 触发：L1 split/merge digest、L2 local ordering 和 TEE two-step execution 共同定义交易处理边界；Blockchain + IPFS construction data management 进一步说明 storage 方向还有应用层大对象路线：业务文件/照片/BIM 不应被混入 state storage 或 DA，而应通过链上 metadata/CID 与链下 content-addressed storage/pinning 生命周期共同管理；FRIDA 新增的结构性信号是 data availability/light-client 路线已经与 proof-system commitments 深度耦合，但该耦合只迁移 commitment/opening 机制，不迁移 execution validity；Atomic/Fair Data Exchange 进一步说明 DA 方向还需要服务激励层，即在 commitment 仍可验证但数据过期或分散后，如何让 archive/data providers 因正确服务获得付款；Fraud Proofs 补上反证式验证边界，即 light-client invalidity detection 必须同时考虑 fraud proofs、data availability、codec proofs 和网络采样假设；COLE 新增的结构性信号是 blockchain systems 还需要 data-management/storage 方向，处理 full-node state history、authenticated indexes、state roots、provenance proofs 和 storage-engine mechanism adaptation。

- FedChain delta: blockchain-systems 的 interoperability 与 consensus 之间出现一条新的 security bridge：跨链 SPV transfer 的安全性由 source-chain PoS finality、confirmation depth、adversarial stake ratio 和 stake/reward 分布共同决定。

## 领域态势

- Research dynamics note: [[04_Knowledge/blockchain-systems/research-dynamics|Research dynamics]]
- Dynamics freshness: stale/queued because no daily-fetch evidence exists
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper the Friendly Finality Gadget]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding|OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment|ByShard: Sharding in a Byzantine Environment]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain|A Raft Variant for Permissioned Blockchain]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology|RingBFT: Resilient Consensus over Sharded Ring Topology]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1802-07240-cobalt-bft-governance-in-open-networks|Cobalt: BFT Governance in Open Networks]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool|Scaling Blockchain Consensus via a Robust Shared Mempool]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus|Flexible Advancement in Asynchronous BFT Consensus]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security|EPIC: Efficient Asynchronous BFT with Adaptive Security]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | adds interoperability/cross-chain privacy-preserving auditing as a new blockchain-systems branch | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合 | yes | continue with zkBridge and cross-chain protocol sources |
| [[sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains|sigBridge: A Cross-chain Bridge for Permissioned Blockchains and its application to decentralized access control]] | adds permissioned signature-based bridge route and cross-direction relation between consensus and interoperability | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[cross-chain-protocols|Cross-chain protocols]], [[permissioned-blockchain-consensus|Permissioned blockchain consensus]] and [[permissioned-consensus-to-cross-chain-bridges|Permissioned consensus -> cross-chain bridges]] |
| [[doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency|A secure dynamic cross-chain decentralized data consistency verification model]] | adds dynamic data consistency auditing route under interoperability/cross-chain protocols | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[cross-chain-protocols|Cross-chain protocols]]; keep DA/storage relation as review until more sources |
| [[arxiv-2310-10016v1-towards-scalable-cross-chain-messaging|Towards Scalable Cross-Chain Messaging]] | adds cross-chain message relaying as a subproblem under interoperability/cross-chain protocols | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[cross-chain-message-relaying|Cross-chain message relaying]]; keep task-allocation bridge as review until foundation sources exist |
| [[arxiv-1905-02847v2-atomic-commitment-across-blockchains|Atomic Commitment Across Blockchains]] | adds atomic cross-chain transactions as a subproblem under interoperability/cross-chain protocols | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] and [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] |
| [[doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce|Cross-chain Deals and Adversarial Commerce]] | adds adversarial-commerce deal safety/liveness and timelock/CBC protocol routes under atomic cross-chain transactions | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[atomic-cross-chain-transactions|Atomic cross-chain transactions]] and [[distributed-transactions-to-atomic-cross-chain-transactions|Distributed transactions -> atomic cross-chain transactions]] |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | adds execution-and-transactions as a new blockchain-systems branch and creates a consensus-execution bridge | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | continue with parallel execution, Fabric/Nezha/SChain, and execution-layer sources |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] | adds database-inspired Fabric transaction reordering and early abort under execution-and-transactions | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[execution-and-transactions|Blockchain execution and transactions]], [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] and [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] | adds DAG-based blockchain transaction-processing route with ACG/HS under execution-and-transactions | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route through [[execution-and-transactions|Blockchain execution and transactions]], [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] and [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | adds stateless/off-chain execution-storage split and creates state-storage -> transaction-processing bridge | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route through [[execution-and-transactions|Blockchain execution and transactions]], [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]], [[data-management-and-storage|Blockchain Data Management and Storage]], [[blockchain-state-storage|Blockchain State Storage]] and [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | adds layer-2 DApp split-execute-merge route and strengthens state-storage -> transaction-processing bridge | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route through [[execution-and-transactions|Blockchain execution and transactions]], [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]], [[data-management-and-storage|Blockchain Data Management and Storage]], [[blockchain-state-storage|Blockchain State Storage]] and [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] |
| [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Blockchain + IPFS construction data management]] | adds off-chain application data-management as a child problem under data-management/storage; corrects queue path away from consensus | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route through [[data-management-and-storage|Blockchain Data Management and Storage]] and [[off-chain-application-data-management|Off-chain Application Data Management]] |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | adds transparent FRI-based DAS route and proof-system bridge to the data-availability direction | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[data-availability-and-light-clients|Data availability and light clients]], [[data-availability-sampling|Data availability sampling]] and [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | adds committed-data fair retrieval/service-incentive route to data-availability direction | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[fair-data-exchange|Fair data exchange for committed data]] and [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | adds permissioned/general-workload sharding source extension with TEE-assisted BFT and BFT reference-committee transaction coordination | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route through [[scaling-and-sharding|Scaling and sharding]], [[sharded-ledgers|Sharded ledgers]], [[bft-consensus-to-sharded-ledgers|BFT consensus -> sharded ledgers]] |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | adds fraud-proof-backed light-client validation route and DAS dependency boundary | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route details through [[data-availability-and-light-clients|Data availability and light clients]], [[fraud-proofs|Fraud proofs]] and [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | adds blockchain data-management/storage branch and state-storage problem node; corrects queue path away from consensus | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合 | yes | route through [[data-management-and-storage|Blockchain Data Management and Storage]], [[blockchain-state-storage|Blockchain State Storage]] and [[storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | 新增 PoS-secured federated transfer：把跨链转移、PoS finality 和 Stackelberg stake/reward distribution 作为一个系统安全问题处理。 | 方法族与解决路线; 代表 Sources; 当前综合 | no new top-level child | route through [[interoperability|Blockchain interoperability]], [[cross-chain-protocols|Cross-chain protocols]], [[proof-of-stake-finality|Proof-of-stake finality]] and [[proof-of-stake-finality-to-cross-chain-protocols|Proof-of-stake finality -> cross-chain protocols]] |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | adds blockchain as participant coordination, private training-trace audit and reward-evidence infrastructure for trustworthy distributed ML; keeps ML training trust as the primary problem. | Bridge Links; 关系图谱; Source Extensions | no new blockchain child | route through [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]] and [[trustworthy-distributed-ml|Trustworthy distributed ML]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]] | `blockchain-systems; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | application, coordination, auditability, incentive | Blockchain contributes coordination and tamper-resistant trace; ML training correctness, privacy, hardware attestation, convergence and model quality do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-blockchain-consensus | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-blockchain-systems-research-dynamics | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/research-dynamics.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-data-availability-and-light-clients | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-blockchain-interoperability | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/interoperability.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-mempool-and-networking | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/mempool-and-networking.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-scaling-and-sharding | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/scaling-and-sharding.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-blockchain-execution-and-transactions | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/execution-and-transactions.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | has_child | nahida-knowledge-blockchain-data-management-and-storage | vault/04_Knowledge/blockchain-systems.md; vault/04_Knowledge/blockchain-systems/data-management-and-storage.md | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md | vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | vault/03_Sources/papers/sha256-662f70f3c28a-omniledger-secure-scale-out-decentralized-ledger-via-sharding.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | vault/03_Sources/papers/doi-10-14778-3476249-3476275-byshard-sharding-in-a-byzantine-environment.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | vault/03_Sources/papers/sha256-be219323fe92-sraft-raft-variant-for-permissioned-blockchain.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | vault/03_Sources/papers/arxiv-2107-13047v2-ringbft-resilient-consensus-over-sharded-ring-topology.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | vault/03_Sources/papers/arxiv-1802-07240-cobalt-bft-governance-in-open-networks.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | vault/03_Sources/papers/arxiv-2203-05158-scaling-blockchain-consensus-via-a-robust-shared-mempool.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | vault/03_Sources/papers/doi-10-1145-3600006-3613164-flexible-advancement-in-asynchronous-bft-consensus.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | vault/03_Sources/papers/sha256-5d39afb8a188-epic-efficient-asynchronous-bft-with-adaptive-security.md | medium | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | vault/03_Sources/papers/sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing.md | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-9b3cfce6e018-sigbridge-cross-chain-bridge-permissioned-blockchains.md | sigBridge source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-1016-j-jksuci-2023-101897-dccv-dynamic-cross-chain-data-consistency.md | DCCV source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-2310-10016v1-towards-scalable-cross-chain-messaging.md | Scalable Cross-Chain Messaging source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-1905-02847v2-atomic-commitment-across-blockchains.md | Atomic Commitment source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-14778-3364324-3364326-cross-chain-deals-adversarial-commerce.md | Cross-chain Deals source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md | vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md | Fabric++ source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md | Nezha source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md | SlimChain source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md | L2chain source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md | Blockchain + IPFS construction data-management source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md | FRIDA source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | FDE source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | AHL source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md | Fraud Proofs source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md | COLE source note | high | active_seed |
| nahida-knowledge-blockchain-systems | evidenced_by | vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md | TDML source note | medium | active_seed |
| nahida-knowledge-blockchain-systems | bridges_to | nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| HotStuff、Narwhal/Tusk、现代 CometBFT、rollups、MEV 与执行层资料缺失。 | 影响本节点 foundation 完整性；Fraud Proofs 已有 seed，但现代 rollup fraud-proof source 仍缺。 | nahida-research-search or nahida-update | medium | queued |
| Universal atomic swaps、production IBC/relayer implementations、relay-chain designs 缺 source。 | Atomic Commitment、Cross-chain Deals 与 Scalable Cross-Chain Messaging 已补 atomicity/deal-safety/relayer-coordination seeds，但 interoperability 分支仍缺真实 relayer/bridge ecosystem 对照。 | nahida-update | high | queued |
| permissioned cross-chain bridges 和 decentralized access control foundations 薄。 | sigBridge 是单 source seed，需更多来源才能拆出稳定应用/方法子节点。 | nahida-update / nahida-research-search | medium | queued |
| dynamic cross-chain data consistency verification 仍薄。 | DCCV 是单 source seed，尚缺 BeDCV/DCIV、动态数据审计和真实跨链数据更新部署对照。 | nahida-update / nahida-research-search | medium | queued |
| Celestia/EIP-4844/HASW23/original FRI 等 DA foundation sources 缺。 | FRIDA 补了 transparent DAS route，但 deployment 和 foundation 对照仍薄。 | nahida-update or nahida-research-search | high | queued |
| committed-data fair exchange、VECK、data-service pricing 仍只有一篇 seed。 | 影响 DA 服务激励和公平交换路线的成熟度判断。 | nahida-update | high | queued |
| TEE-assisted BFT / SGX sharding foundations 仍薄。 | AHL 使用 trusted hardware 改变 BFT fault model 和 shard sizing，但 vault 缺 TrInc/MinBFT/Hybrids on Steroids 等基础 source。 | nahida-update or nahida-research-search | medium | queued |
| stateless blockchain/state expiry/storage-node availability sources 仍薄。 | SlimChain 给出 stateless/off-chain execution-storage split；ICM-DSN 已补入 DSN storage incentives/challenge verification seed，但 stateless clients、Verkle/state expiry、Filecoin/Sia/Storj/Swarm 和 data-serving liveness 仍缺 foundation/implementation 对照。 | nahida-update or nahida-research-search | high | active_seed_gap |
| IPFS/content-addressed application storage sources 仍薄。 | Blockchain + IPFS construction data management 给出应用大对象链上/链下拆分 seed，但还缺 IPFS/IPFS-Cluster/Filecoin/Arweave 和真实应用仓库对照。 | nahida-update or nahida-research-search | medium | queued |
| blockchain coordination for distributed ML 仍是单 source seed。 | TDML 说明 blockchain 可作为 remote training coordination/audit rail，但 vault 缺更多 blockchain-DML、decentralized compute 和 remote trainer attestation 来源。 | nahida-update / nahida-research-search | medium | active_seed_gap |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 11 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkcross | Added interoperability/cross-chain protocols branch from zkCross. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-tell-leaderless-consensus-execution | Added execution-and-transactions branch and consensus-execution bridge from TELL. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Added FRIDA as transparent data-availability commitment route under data-availability/light-clients. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Added committed-data fair retrieval route under data-availability/light-clients. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL as permissioned/general-workload sharding source extension and routed it through sharded ledgers plus BFT/database-transaction bridges. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Added fraud-proof-backed light-client validation and DAS dependency boundary. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-sigbridge | Added sigBridge as permissioned cross-chain bridge source extension and routed it through consensus-interoperability bridge. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-dccv-dynamic-cross-chain-data-consistency | Added DCCV as dynamic cross-chain data consistency source extension and routed it through interoperability/cross-chain protocols. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-scalable-cross-chain-messaging | Added cross-chain message relaying as a relayer transport/coordination subproblem under interoperability. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-fabric-plus-plus-transaction-processing | Added Fabric++ as database-inspired Fabric transaction processing evidence under execution-and-transactions. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-cross-chain-deals | Added Cross-chain Deals as an interoperability/atomicity source extension; kept it below atomic cross-chain transactions rather than creating a source-named knowledge node. | doi:10.14778/3364324.3364326 | codex |
| 2026-06-22 | nahida-knowledge-20260622-nezha-dag-transaction-processing | Added Nezha as DAG-based execution/transaction-processing source extension under execution-and-transactions. | doi:10.1109/icdcs54860.2022.00034 | codex |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Added SlimChain as stateless/off-chain execution-storage source extension and created state-storage-to-transaction-processing bridge. | doi:10.14778/3476249.3476283 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Added L2chain as layer-2 DApp split-execute-merge route and strengthened state-storage-to-transaction-processing bridge. | doi:10.14778/3574245.3574278 | codex |
| 2026-06-23 | nahida-knowledge-20260623-blockchain-ipfs-construction-data-management | Added off-chain application data-management under blockchain data-management/storage. | doi:10.3846/jcem.2023.18646 | codex |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Added TDML as blockchain coordination/audit-rail application evidence and created bridge to trustworthy distributed ML. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-incentive-compatible-decentralized-storage | Added decentralized-storage-networks as blockchain data-management/storage child and created DSN-to-contingent-service-payments bridge. | arxiv:2208.09937 | codex |
