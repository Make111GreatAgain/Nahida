---
id: "nahida-knowledge-proof-systems"
title: "Proof systems"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "proof-systems"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-zero-knowledge-proofs"
child_knowledge_refs:
  - "nahida-knowledge-commit-and-prove-arguments"
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-floating-point-snarks"
  - "nahida-knowledge-fri-iopps"
  - "nahida-knowledge-hardware-accelerated-proving"
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-modular-zksnarks"
  - "nahida-knowledge-proof-system-benchmarking"
  - "nahida-knowledge-scalable-proof-generation"
  - "nahida-knowledge-verifiable-encryption"
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-proof-systems"
    relation: "is_a"
    to: "nahida-knowledge-zero-knowledge-proofs"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-modular-zksnarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-verifiable-encryption"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/verifiable-encryption.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-distributed-proof-generation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-memory-efficient-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-floating-point-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-fri-iopps"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/fri-iopps.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-proof-system-benchmarking"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md"
      - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-hardware-accelerated-proving"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md"
      - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
      - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-commit-and-prove-arguments"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md"
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
      - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "has_child"
    to: "nahida-knowledge-zero-knowledge-sets-and-elementary-databases"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases.md"
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-fair-exchange-protocols.md"
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
    evidence_refs:
      - "vault/05_Bridges/distributed-proof-generation-to-snark-proof-aggregation.md"
      - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-verifiable-ml-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/private-delegated-proving-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    evidence_refs:
      - "vault/05_Bridges/split-prover-zksnarks-to-recursion-and-folding.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
    evidence_refs:
      - "vault/05_Bridges/hardware-accelerated-proving-to-proof-system-benchmarking.md"
      - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
      - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-distributed-proof-generation.md"
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
      - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/floating-point-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks"
    evidence_refs:
      - "vault/05_Bridges/commit-and-prove-arguments-to-floating-point-snarks.md"
      - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-systems"
    relation: "bridges_to"
    to: "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
    evidence_refs:
      - "vault/05_Bridges/zero-knowledge-sets-to-verifiable-database-queries.md"
      - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
  - "nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks"
  - "nahida-bridge-distributed-proof-generation-to-zkrollups"
  - "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
  - "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
  - "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
  - "nahida-bridge-fri-iopps-to-data-availability-sampling"
  - "nahida-bridge-zk-snarks-to-verifiable-encryption"
  - "nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation"
  - "nahida-bridge-private-delegated-proving-to-kzg-commitments"
  - "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
  - "nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking"
  - "nahida-bridge-commit-and-prove-arguments-to-scalable-proof-generation"
  - "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
  - "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
  - "nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
  - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
  - "vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
  - "vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md"
  - "vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md"
  - "vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md"
  - "vault/03_Sources/papers/sha256-9c8b8a3f92ae-scalable-zkp-generation-large-scale-computing.md"
representative_source_refs:
  - "doi:10.1145/3460120.3484558"
  - "iacr:2019/142"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3658644.3690318"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "doi:10.1145/3575693.3575711"
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "doi:10.1145/3548606.3560653"
  - "iacr:2023/156"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
query_keys:
  - "Proof systems"
  - "proof-systems"
  - "证明系统"
  - "distributed proof generation"
  - "data-parallel ZKP"
  - "fully distributed ZKPs"
  - "Pianist"
  - "zkRollup prover scaling"
  - "SNARK proof aggregation"
  - "proof aggregation"
  - "memory-efficient SNARKs"
  - "streaming SNARKs"
  - "folding-based SNARKs"
  - "Mangrove"
  - "floating-point SNARKs"
  - "IEEE 754 SNARK circuits"
  - "accurate floating-point proofs"
  - "relative-error floating-point proofs"
  - "approximate floating-point ZK proofs"
  - "zkML proof systems"
  - "verifiable inference"
  - "tensor lookup arguments"
  - "ZK proofs for LLMs"
  - "space-efficient zkSNARKs"
  - "space-efficient sumcheck"
  - "Sparrow"
  - "zero-knowledge forest training"
  - "FRI IOPPs"
  - "FRI"
  - "interactive oracle proofs of proximity"
  - "opening-consistency"
  - "FRIDA"
  - "Verifiable encryption"
  - "SAVER"
  - "SNARK-friendly encryption"
  - "Proof-system benchmarking"
  - "SNARK benchmarking"
  - "zk-Bench"
  - "ZKP performance evaluation"
  - "Hekaton"
  - "divide-and-aggregate zkSNARK"
  - "Mirage aggregation"
  - "private delegated proving"
  - "privacy-preserving prover delegation"
  - "Siniel"
  - "split prover zkSNARKs"
  - "Groth16 split prover"
  - "partial witness zkSNARK proving"
  - "commit-and-prove arguments"
  - "commit-and-prove floating-point SNARKs"
  - "CP-NIZK"
  - "ZKCPlus"
  - "Hardware-accelerated proving"
  - "GPU accelerated ZKP"
  - "GZKP"
  - "PipeZK"
  - "DIZK"
  - "Spark zkSNARK"
  - "ASIC zkSNARK prover"
  - "NTT acceleration"
  - "MSM acceleration"
  - "Gemini"
  - "elastic SNARKs"
  - "streaming R1CS"
  - "Epistle"
  - "elastic Plonk"
  - "Plonkish elastic SNARK"
  - "Split hash-based memory optimization"
  - "Good Split"
  - "hash-bound SNARK circuit partitioning"
  - "zk-vSQL"
  - "function-independent preprocessing"
  - "zero-knowledge verifiable polynomial delegation"
  - "zero-knowledge sets"
  - "ZKS"
  - "ZK-EDB"
  - "ZK-FEDB"
  - "set-operation ZKS"
  - "zero-knowledge database commitments"
  - "Scalable proof generation"
  - "prover scalability"
  - "Yoimiya"
  - "serializable ZK-SNARKs"
aliases:
  - "证明系统"
  - "commit-and-prove"
  - "distributed proof generation"
  - "fully distributed ZKPs"
  - "proof aggregation"
  - "FRI"
  - "zk-vSQL"
domains:
  - "zero-knowledge-proofs"
topics:
  - "proof-systems"
  - "commit-and-prove-arguments"
  - "distributed-proof-generation"
  - "data-parallel-circuits"
  - "snark-proof-aggregation"
  - "zkrollup-prover-scaling"
  - "memory-efficient-snarks"
  - "folding-based-snarks"
  - "floating-point-snarks"
  - "ieee-754"
  - "relative-error-model"
  - "approximate-floating-point-proofs"
  - "zkml"
  - "verifiable-inference"
  - "verifiable-ml-training"
  - "space-efficient-sumcheck"
  - "lookup-arguments"
  - "fri-iopps"
  - "interactive-oracle-proofs-of-proximity"
  - "opening-consistency"
  - "verifiable-encryption"
  - "proof-system-benchmarking"
  - "runtime-estimation"
  - "divide-and-aggregate"
  - "hekaton"
  - "private-delegated-proving"
  - "split-prover-zksnarks"
  - "hardware-accelerated-proving"
  - "gpu-proving"
  - "asic-proving"
  - "cluster-proving"
  - "elastic-snarks"
  - "streaming-r1cs"
  - "plonkish-snarks"
  - "hyperplonk"
  - "front-end-circuit-partitioning"
  - "hash-bound-subcircuits"
  - "function-independent-preprocessing"
  - "zk-vpd"
  - "zero-knowledge-sets"
  - "zero-knowledge-elementary-databases"
  - "set-operation-queries"
  - "scalable-proof-generation"
  - "prover-scalability"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-zkbridge"
  - "nahida-knowledge-20260620-snarkfold"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260620-mangrove"
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
  - "nahida-knowledge-20260621-zk-bench-proof-system-benchmarking"
  - "nahida-knowledge-20260621-hekaton-proof-aggregation"
  - "nahida-knowledge-20260621-siniel-private-delegated-proving"
  - "nahida-knowledge-20260621-split-prover-zksnarks"
  - "nahida-knowledge-20260621-gzkp-hardware-accelerated-proving"
  - "nahida-knowledge-20260622-pipezk-pipelined-architecture"
  - "nahida-knowledge-20260622-dizk-distributed-zkp"
  - "nahida-knowledge-20260622-gemini-elastic-snarks"
  - "nahida-knowledge-20260623-epistle-elastic-snarks"
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
  - "nahida-knowledge-20260622-vsql-zk"
  - "nahida-knowledge-20260623-succinct-zk-floating-point"
  - "nahida-knowledge-20260623-zk-functional-elementary-databases"
  - "nahida-knowledge-20260623-scalable-zkp-generation"
source_refs:
  - "doi:10.1145/3460120.3484558"
  - "iacr:2019/142"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3658644.3690318"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "sha256:7ec0866c4734c64b98972c14f71b53bf12d8d5a26343dce3da72c795fde0ec11"
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "doi:10.1145/3575693.3575711"
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:17844a65dcd51c5aa9e4943cc582c48f3b960c65225becd462dbfe6618122a44"
  - "doi:10.1145/3548606.3560653"
  - "iacr:2023/156"
  - "sha256:9c8b8a3f92aef55804a598fb3e0c98a69572839c3ed654fa9ea476c5e0dab270"
confidence: "medium"
trust_tier: "primary"
---

# Proof systems

## 定义与范围

- 定义: Proof systems 组织 ZKP/VC 中证明者、验证者、约束表达、setup、proof size、verifier cost 和 composability 的方法族。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `proof-systems`
- Aliases/query keys: 证明系统
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `proof-systems`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 vault 覆盖 LegoSNARK 相关 modular zkSNARK seed、ZKCPlus 中 data-parallel commit-and-prove NIZK / fair-exchange application seed、zkBridge 中 deVirgo 的 data-parallel distributed proof generation 应用型 seed、DIZK 中 Spark-distributed Groth zkSNARK setup/prover seed、SnarkFold 中 SNARK proof aggregation 的 verifier-cost/proof-size 优化 seed、Pianist 中 Plonk/bivariate-KZG fully distributed proof generation seed、Mangrove 中 low-memory/folding-based SNARK construction seed、Gemini 中 elastic SNARK / streaming R1CS / elastic KZG seed、Epistle 中 elastic Plonkish / HyperPlonk PIOP / elastic multilinear KZG seed、SPLITA 中 hash-bound R1CS/front-end circuit partitioning seed、zk-vSQL 中 function-independent preprocessing zero-knowledge argument / zk-VPD seed、ZKLP 中 IEEE 754 floating-point SNARK circuits seed、Garg et al. 中 relative-error floating-point proofs / commit-and-prove compiler seed、zkLLM 中 tensor lookup / attention-specific verifiable inference seed、Sparrow 中 data-parallel space-efficient SNARK / sumcheck / zkML training seed、FRIDA 中 FRI IOPP/opening-consistency 的 DAS 应用 seed、SAVER 中 SNARK-friendly verifiable encryption seed、zk-Bench 中 proof-system benchmarking / runtime-estimation seed、Hekaton 中 divide-and-aggregate distributed zkSNARK / proof aggregation fan-in seed、Siniel 中 private delegated proving / witness-private prover outsourcing seed、Split Prover 中 partial-witness two-phase Groth16 proving seed，GZKP 中 GPU hardware-accelerated proving / NTT / MSM / finite-field arithmetic seed，以及 PipeZK 中 custom ASIC / pipelined NTT-MSM accelerator seed；仍缺 zk-SNARK/STARK/IOP/PCP/Plonk/FRI/通用 verifiable encryption/accelerated prover 原始来源等系统性 foundation。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[zero-knowledge-proofs|zero-knowledge-proofs]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

回答如何把计算或陈述编码为可验证证明，并比较不同 proof-system family 的 setup、效率、组合性和应用边界。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zero-knowledge-proofs|zero-knowledge-proofs]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks|zk-snarks]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[modular-zksnarks|modular-zksnarks]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[distributed-proof-generation|Distributed proof generation]] | child / method_family | zkBridge/deVirgo、DIZK、Pianist、Hekaton、Siniel 和 Split Prover now provide multiple source-backed distributed/prover-side routes, including cluster-distributed Groth proving, private delegated proving and partial-witness split proving, so keeping it as a single source-extension row would raise retrieval cost. | [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]]; [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]]; [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]]; [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton]]; [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] | active_seed |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | child / problem | Mangrove, Sparrow, Gemini, Epistle and SPLITA expose a reusable prover-resource problem: reducing SNARK peak memory/pass complexity while retaining succinct verification. | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]]; [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]]; [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] | active_seed |
| [[floating-point-snarks|Floating-point SNARKs]] | child / method_family | ZKLP exposes exact IEEE 754 arithmetic circuits; Garg et al. expose a reusable relative-error route for applications where approximate numerical correctness is acceptable. | [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]]; [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct ZK for Floating Point]] | active_seed |
| [[fri-iopps|FRI IOPPs]] | child / method_family | FRIDA exposes FRI as a reusable IOPP/proximity method family and proves opening-consistency for DAS-style erasure-code commitments. | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] | active_seed |
| [[verifiable-encryption|Verifiable encryption]] | child / method_family | SAVER and FDE/VECK context expose a reusable proof/encryption composition problem: prove properties of encrypted plaintext without making encryption a large SNARK circuit. | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]]; [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | active_seed |
| [[proof-system-benchmarking|Proof-system benchmarking]] | child / evaluation_axis | zk-Bench exposes a reusable evaluation axis for comparing arithmetic libraries, ZKP development tools, hardware choices, memory/proof-size behavior and runtime estimation. | [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench]] | active_seed |
| [[hardware-accelerated-proving|Hardware-accelerated proving]] | child / problem | GZKP and PipeZK expose a reusable prover-side acceleration problem: using GPU/custom hardware-aware NTT, MSM and finite-field arithmetic backends to reduce proof-generation latency. | [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]]; [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] | active_seed |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | child / method_family | LegoSNARK, Geppetto, SAVER, Mangrove, ZKCPlus and Garg et al. now show CP as a cross-source proof interface: modular composition, fair exchange, verifiable encryption and floating-point compiler backend. | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]]; [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]]; [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct ZK for Floating Point]] | active_seed |
| [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] | child / method_family | ZK-FEDB exposes a reusable proof/data-commitment primitive family: membership, non-membership, key-value binding and set-operation queries with zero-knowledge hiding. | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| zk-SNARKs foundation node | zk-SNARKs foundation node | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| [[verifiable-encryption|Verifiable encryption]] | 把加密与 proof relation 绑定，让验证者确认密文中的明文满足关系，同时避免把复杂 encryption algorithm 放进 SNARK circuit。 | 需要隐藏明文但公开验证其合法性，如 voting、committed-data exchange 或 encrypted witness proofs。 | encryption privacy、proof soundness、rerandomization、payment fairness 是不同性质；SAVER 主要是 pairing/Groth16-like route。 | [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| modular zkSNARK composition | modular zkSNARK composition | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| [[commit-and-prove-arguments|Commit-and-prove arguments]] | 先对 witness/message 做 commitment，再证明 commitment 中的值和辅助 witness 满足关系，并让多个证明组件共享同一隐藏对象；也可作为 floating/fixed point compiler 的 R1CS proving backend。 | 模块化 SNARK、verifiable encryption、fair exchange、低内存 witness reuse、shared-state VC 或 relative-error floating-point proof compiler。 | 需要 commitment binding/hiding；CP 只证明一致性，不自动提供 payment fairness、应用语义、数值误差模型或 exact IEEE rounding。 | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]]; [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK]]; [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct ZK for Floating Point]] |
| [[distributed-proof-generation|Distributed proof generation]] | 将 proving work 分发到多台机器或多阶段参与者，并通过 cluster backend、polynomial-IOP/commitment aggregation 或 split aux/proof completion 降低单机/在线 time-memory；其中 [[private-delegated-proving|Private delegated proving]] 进一步要求 witness/aux-sensitive data 对服务器隐藏。 | 大电路、重复子电路、zkRollup/zkEVM batch、light-client verification、prover outsourcing、partial-witness two-phase proving 等 prover-side bottleneck 场景。 | proof-system-specific；communication、trusted setup、worker trust、witness distribution、witness privacy、phase boundary 和生产调度需要单独评估。 | [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]]; [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge]]; [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]]; [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| Split prover zkSNARKs | 把 prover work 按 witness 到达时间拆成 early aux generation 和 late proof completion，同时保持 verifier/proof interface 不变。 | 早到 witness 很重、晚到 witness 较小，且第二阶段 prover 不应学习早到 witness 或独立伪造授权 proof。 | 当前只有 Groth16 construction 和 theory lower bound；不是 generic proof-system foundation。 | [[split-prover-zksnarks|Split prover zkSNARKs]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| SNARK proof aggregation | 将多个 SNARK proofs 合并为一个聚合对象和 aggregation proof，以降低 verifier work/proof size。 | 系统需要批量验证 proofs，且可为目标 SNARK 设计可折叠 relation。 | 不等于生产 benchmark；聚合 prover work 仍随 `n` 增长；具体 SNARK 适配需要专门构造。 | [[snark-proof-aggregation|SNARK proof aggregation]]; [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| Divide-and-aggregate zkSNARKs | 将大电路分区后分布式证明每个 chunk，再用 proof/commitment aggregation fan in 成单个 proof。 | 任意大计算需要横向扩展 prover，且 shared wires 可通过 memory checking 处理。 | 当前是 Hekaton source-backed seed；aggregation 未并行化；implementation/benchmark source-local。 | [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton]] |
| [[memory-efficient-snarks|Memory-efficient SNARKs]] | 通过 streaming、chunking、PCD/folding、elastic prover configurations、hash-bound front-end circuit partitioning 或 proof wrapping 降低 prover peak memory 和全局数据持有需求。 | 单机 prover memory/pass complexity 是瓶颈，但不一定需要多机分布式 proving。 | 与 proof aggregation、distributed proving 相邻但不同；具体路线应下钻到 memory-efficient 子节点。 | [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]]; [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] |
| Hash-bound front-end circuit partitioning | 在 R1CS/arithmetic-circuit 前端把大电路切成顺序子电路，并用 public hash 绑定跨切分中间 state，降低单机 prover peak memory。 | 电路存在 Good Split，跨切分 state 小，且可接受 hash-circuit overhead 和多段证明/验证/设置成本。 | 不提供 distributed worker model；Good Split 搜索、SNARK-friendly hash 和 arbitrary-circuit 适用性仍是后续问题。 | [[memory-efficient-snarks|Memory-efficient SNARKs]]; [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] |
| [[floating-point-snarks|Floating-point SNARKs]] | 在 SNARK/argument 中处理 floating-point arithmetic：一条路线精确模拟 IEEE 754，另一条路线证明每个 gate 满足相对误差界。 | 地理、ML、科学计算等应用依赖 floating-point；需要按“exact library compatibility”或“bounded numerical error”选择路线。 | 不等于 zk-SNARK foundation；relative-error route 不保证 exact IEEE rounding，exact route 不自动降低 prover cost。 | [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]]; [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct ZK for Floating Point]] |
| [[fri-iopps|FRI IOPPs]] | 通过 Reed-Solomon proximity、recursive folding、Merkle-authenticated oracle queries 和 opening-consistency 支撑透明 proof/commitment routes。 | 需要 transparent setup 或 proximity proof machinery，或需要为 DAS 构造 erasure-code commitments。 | 当前由 FRIDA seed 支撑，不替代原始 FRI/STARK foundation；FRIDA 用的是 erasure-code commitment route，不是完整 PCS API。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| [[proof-system-benchmarking|Proof-system benchmarking]] | 用统一指标和可复现实验比较 arithmetic libraries、proof-system phases、proof size、memory 和 hardware sensitivity，并用低层数据估计协议 runtime。 | 需要选择 ZKP tools、评估 prover/verifier tradeoffs 或判断 paper benchmark 是否可迁移。 | 不是某个 proof system；exact rankings 依赖版本、电路实现和硬件，生产决策需要刷新。 | [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench]] |
| [[hardware-accelerated-proving|Hardware-accelerated proving]] | 用 GPU/FPGA/ASIC/multi-GPU 或硬件感知 arithmetic backend 加速 prover-heavy stages，例如 NTT/FFT、MSM 和有限域运算。 | Prover latency/throughput 是瓶颈，且 workload 能映射到硬件并行结构。 | 不改变 proof protocol security；exact speedups 依赖硬件、curve、bit width、workload sparsity、memory budget、module-vs-end-to-end boundary 和实现版本。 | [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]]; [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] |
| ML tensor/operator proving | 用 sumcheck/MLE 处理 tensor arithmetic，用 lookup/tensor lookup 处理 activation、normalization、attention 等非算术操作。 | ML/LLM inference relation 需要被编码为可验证 proof statement。 | 不等于 proof-system foundation；量化误差、table size、GPU proving 和模型边界留在 [[verifiable-inference|Verifiable inference]] / source note。 | [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] |
| Data-parallel space-efficient SNARKs | 用 space-efficient sumcheck、streaming GKR、sublinear public-parameter polynomial commitments 和 Fiat-Shamir 组合，在 data-parallel layered circuits 上降低 prover memory。 | 计算可表达为 layered data-parallel arithmetic circuits，且 prover memory 比总 circuit size 更关键。 | 适用电路类受限；可能增加 prover time；sumcheck/GKR 细节通过 bridge 连接到 [[sum-check-protocol|Sum-check protocol]]。 | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] |
| Elastic SNARKs / streaming R1CS and Plonkish PIOP | 在同一 proof/verifier interface 下，让 prover 选择线性时间/线性内存或准线性时间/对数内存配置；Gemini 是 R1CS route，Epistle 是 Plonkish/HyperPlonk route。 | R1CS 或 Plonkish trace/index/witness 能被 streaming 生成或重放，并且 PIOP 与 PCS 层都支持 streaming。 | KZG trusted setup/pairing assumptions 保留；Plonkish lookup streaming 与应用端 trace generation 需单独分析。 | [[elastic-snarks|Elastic SNARKs]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] |
| function-independent preprocessing zero-knowledge arguments | 让 preprocessing 只依赖输入/见证长度上界而非具体电路；evaluation phase 用 committed CMT/sum-check 和 zk-VPD 隐藏 witness 与中间值。 | 计算在 setup 时未知，且不希望通过 universal circuit 承受过大 concrete overhead。 | 仍是 trusted preprocessing 和交互式 argument；依赖同态承诺、ZKeq/ZKprod、q-SDH 和 knowledge-of-exponent 型假设。 | [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] |
| [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] | 承诺集合或 elementary database 后证明 membership、non-membership、key-value 绑定和 set-operation query relation，同时隐藏集合/数据库大小和未返回元素。 | 需要对 committed set/database 做私有查询证明，并且 query completeness 不能靠公开全库 witness。 | 当前 source 依赖 unknown-order groups、random oracle/generic group model；SQL/storage/transactions 不属于该 primitive。 | [[eprint-2023-156-zero-knowledge-functional-elementary-databases|ZK-FEDB]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 作为 data-parallel distributed proof generation source extension，提出 deVirgo 并用于跨链桥大电路 proving | 应用驱动 source；deVirgo 尚未作为独立 foundation node | `p8-p10` |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | paper | 作为 distributed proof generation source extension，给出 Spark-distributed Groth zkSNARK setup/prover route | 不升级 zk-SNARK foundation；benchmark numbers are Spark/EC2/Groth/R1CS/QAP/source-local | `p1-p19` |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | paper | 作为 proof aggregation source extension，说明 verifier-cost/proof-size 可通过 split IVC aggregation route 优化 | 不升级 proof-system foundation；Groth16 relation trick 留在 source note | `p1-p19`, `p22-p29` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 作为 distributed proof generation source extension，给出 Plonk/bivariate-KZG fully distributed ZKP 路线，并评估 zkRollup/general-circuit prover scaling | 不升级 Plonk/zk-SNARK foundation；DKZG/RCPS/benchmark details 留在 source note | `p1-p15` |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | paper | 作为 memory-efficient SNARKs source extension，给出 uniform compiler + decoupled PCD + commit-and-fold 的 low-memory folding-based SNARK 路线 | 不升级 Plonk/PCD/folding foundation；性能为估计/benchmark synthesis，生产实现缺 | `p1-p69` |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | paper | 作为 floating-point SNARKs source extension，给出 IEEE 754 compliant primitive circuits 和 ZKLP application evaluation | 不升级 zk-SNARK foundation；location authenticity 不由 FP circuits 保证 | `p1-p19` |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | paper | 作为 ML tensor/operator proving source extension，给出 tlookup、zkAttn、sumcheck/commitment route 和 LLM inference evaluation | 不升级 zk-SNARK foundation；不证明 training provenance 或 AI safety | `p1-p16` |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper | 作为 data-parallel space-efficient SNARK source extension，给出 O(sqrt N)-buffer product-form sumcheck、streaming GKR 和 zkFTP training application | 只覆盖 layered data-parallel circuits；single-thread implementation；formal proofs in full version | `p1-p15` |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | paper | 作为 elastic SNARK source extension，给出 streaming R1CS、elastic PIOP、elastic KZG 和单机超大 R1CS proving evidence | 低内存换取更多 passes/准线性时间；R1CS trace streaming 是输入模型假设；不升级 zk-SNARK foundation | `Abstract`, `§2.1-§2.8`, `§4-§10` |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | paper | 作为 elastic SNARK source extension，给出 streaming HyperPlonk/Plonkish PIOP、elastic multilinear KZG 和低内存 Plonkish proving evidence | lookup protocol 未一般性流式化；custom gate degree 固定；不升级 zk-SNARK/PLONK foundation | `Abstract`, `§2`, `§4-§7` |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | paper | 作为 function-independent preprocessing zero-knowledge argument source extension，给出 zk-VPD、committed sum-check/CMT 和 VC argument 组合 | 仍是 trusted preprocessing / interactive argument；不升级 zk-SNARK/STARK foundation | `§1`, `§3-§6` |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] | paper | 作为 relative-error floating-point proof source extension，给出 commit-and-prove compiler backend、batch range proof without bit decomposition 和 R1CS-size comparison | 不提供 exact IEEE rounding；完整 proof/instantiation 部分在 full version；不是 zkML inference source | `Abstract`, `§2-§6`, Tables 1-3 |
| [[eprint-2023-156-zero-knowledge-functional-elementary-databases|Zero-Knowledge Functional Elementary Databases]] | paper | 作为 ZKS/ZK-EDB source extension，给出 set-operation ZKS、ZK-FEDB 和 database-size-hiding functional query proof route | 不升级 SNARK/STARK foundation；SQL/storage/transactions 留给 application/database source | `Abstract`, `§3-§5` |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | paper | 作为 hash-bound circuit partitioning source extension，给出 Good Split / n-Split 和单机 prover peak-memory reduction evidence | 不升级 zk-SNARK foundation；loop/xJsnark/libsnark benchmark 和 SHA256 hash overhead 留在 source note | `p1-p12`, Table II/III |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | paper | 作为 FRI IOPP source extension，给出 FRI/batched FRI opening-consistency proof，并把 IOPP 编译到 DAS erasure-code commitments | 不是 FRI 原始论文；主要应用目标是 DAS，不证明 general STARK/PCS landscape | `§3-§5`, `Appendix C` |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization]] | paper | 作为 verifiable-encryption source extension，给出 SNARK-friendly VE、verifiable decryption、rerandomization 和 Vote-SAVER application | 不升级 zk-SNARK foundation；pairing/Groth16-like construction 和 benchmark details 留在 source note | `p1-p44` |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs]] | paper | 作为 proof-system benchmarking source extension，给出 arithmetic/circuit benchmark framework、runtime estimator 和 tool-selection evidence | 不升级 zk-SNARK foundation；numeric rankings are version/hardware/circuit dependent and repo not analyzed | `p1-p21`, `Appendix A-B` |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | paper | 作为 distributed-proof-generation/proof-aggregation source extension，给出 divide-and-aggregate zkSNARK、partition-friendly memory checking 和 Mirage commit-carrying aggregation route | 不升级 zk-SNARK foundation；Hekaton system details and benchmark numbers stay in source note | `p1-p35`, Appendix `p36-p44` |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | paper | 作为 private delegated proving source extension，给出 witness-private zkSNARK prover outsourcing、WCC/PCC consistency checkers 和 KZG-backed binding route | 不升级 generic distributed ZKP foundation；EOS/zkSaaS/collaborative zkSNARKs 对照仍需 source-level 吸收 | `p1-p30` |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | paper | 作为 split prover source extension，给出 partial-witness two-phase Groth16 proving、aux split zero-knowledge 和 tight second-phase lower bound | 不升级 Groth16/zk-SNARK foundation；implementation 和 non-Groth16 follow-up 仍缺 | `p1-p23` |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange]] | paper | 作为 commit-and-prove arguments source extension，给出 data-parallel CP-NIZK、MiMC-CTR proof-of-delivery 和 fair-exchange application | 不升级为通用 transparent proof-system foundation；protocol/evaluation details stay in source note | `p1-p20` |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP: A GPU Accelerated Zero-Knowledge Proof System]] | paper | 作为 hardware-accelerated proving source extension，给出 GPU NTT/MSM/finite-field library/multi-GPU prover backend seed | 不升级 zk-SNARK foundation；benchmark numbers are hardware/backend/workload specific | `p1-p14` |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture]] | paper | 作为 hardware-accelerated proving source extension，给出 custom ASIC / pipelined POLY-NTT and MSM prover backend seed | 不升级 zk-SNARK foundation；benchmark numbers are process-node/backend/workload specific | `p1-p13` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-23`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 此方向已作为 ZKP 的 proof-system 入口，但目前必须标记 foundation_thin。ZKCPlus 把 commit-and-prove 从 modular-zkSNARKs 的局部行提升为独立 method-family seed：CP 可以服务 fair exchange 的 committed data / predicate / ciphertext consistency，而不是只服务 SNARK gadget composition；Garg et al. 进一步把 CP 作为 relative-error floating-point proof compiler backend，说明 CP 的可迁移对象是 committed-witness/R1CS proving interface，而不是 payment fairness 或 numeric semantics。zkBridge/DIZK/Pianist/Hekaton/Siniel/Split Prover 覆盖 distributed/prover-side engineering 的多类 evidence：data-parallel route、Spark-distributed Groth route、bivariate Plonk route、divide-and-aggregate via proof aggregation route、full-witness private delegation route、partial-witness split proving route；GZKP/PipeZK 把另一条 prover-side route 独立出来: hardware-accelerated proving，分别关注 GPU NTT/MSM/finite-field arithmetic and custom ASIC/pipelined NTT-MSM backend。SnarkFold/Hekaton 共同扩展 proof aggregation，但分别走 split-IVC/folding 和 Mirage commit-carrying aggregation。Mangrove/Sparrow/Gemini/Epistle/SPLITA 共同把 memory-efficient SNARKs 拆成 folding/PCD、data-parallel streaming GKR/sumcheck、elastic SNARKs、hash-bound front-end circuit partitioning 四条路线，其中 [[elastic-snarks|Elastic SNARKs]] 现在有 Gemini R1CS 与 Epistle Plonkish/HyperPlonk 两个来源；zk-vSQL 增加 function-independent preprocessing zero-knowledge argument route，强调 setup 与具体电路解耦但保留 trusted preprocessing 与交互式边界；ZKLP/Garg et al. 共同扩展 floating-point SNARKs，但前者是 exact IEEE 754 compatibility route，后者是 relative-error approximate route；zkLLM 覆盖 ML tensor/operator proving；FRIDA 新增 FRI IOPP/opening-consistency seed；SAVER 新增 verifiable encryption seed；zk-Bench/DIZK/GZKP/PipeZK/SPLITA 共同提醒 proof-system 节点要区分“主问题”“机制依赖”和“评测证据”: sumcheck/GKR/FRI/VE/aggregation/KZG consistency checking/elastic KZG/elastic multilinear KZG/zk-VPD/Groth16 split proving/CP-NIZK proof-of-delivery/NTT-MSM hardware acceleration/cluster proving/hash-bound circuit partitioning 都是可迁移或待验证机制，benchmark 数值、lower bound、module speedup、single-machine memory reduction、R1CS-size reduction 和 exact rankings 必须留在 source note 或专门评测节点里。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | source extension | data-parallel distributed proof generation / deVirgo evidence | 方法族与解决路线; 代表 Sources; 当前综合 | no | keep as source-contained protocol until more sources justify split |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | source extension | Spark-distributed Groth zkSNARK setup/prover; distributed FFT/Lag/MSM; QAP dense row/column handling; source-local cluster benchmark | 方法族与解决路线; 代表 Sources; 当前综合 | no | route details through [[distributed-proof-generation|Distributed proof generation]] and [[proof-system-benchmarking|Proof-system benchmarking]] |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | source extension | SNARK proof aggregation / verifier-cost compression evidence | 方法族与解决路线; 代表 Sources; 当前综合 | no | route detailed comparison through [[snark-proof-aggregation|SNARK proof aggregation]] |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | source extension + child split trigger | Plonk/bivariate-KZG fully distributed proof generation; zkRollup/general-circuit proving evaluation | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route detailed comparison through [[distributed-proof-generation|Distributed proof generation]] |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | source extension + child split trigger | low-memory folding-based SNARK construction; uniform compiler; decoupled PCD; commit-and-fold; performance estimates | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route detailed comparison through [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | source extension + child split trigger | IEEE 754 compliant floating-point SNARK circuits; lookup/hint optimization; TestFloat and ZKLP evaluation | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route detailed comparison through [[floating-point-snarks|Floating-point SNARKs]] |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | source extension | tensor lookup, attention proof and committed-model inference proof route | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route detailed comparison through [[verifiable-inference|Verifiable inference]] |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | source extension | data-parallel space-efficient SNARK; O(sqrt N)-buffer product-form sumcheck; streaming GKR; zkFTP training application | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[memory-efficient-snarks|Memory-efficient SNARKs]], [[sum-check-protocol|Sum-check protocol]] and [[verifiable-training|Verifiable ML training]] |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | source extension + bridge trigger | elastic SNARKs; streaming R1CS; elastic PIOP; elastic KZG; arkworks implementation evidence | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[memory-efficient-snarks|Memory-efficient SNARKs]], [[kzg-commitments|KZG commitments]] and [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | source extension + bridge trigger | elastic Plonkish SNARKs; streaming HyperPlonk PIOP; elastic multilinear KZG | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[elastic-snarks|Elastic SNARKs]], [[kzg-commitments|KZG commitments]] and [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | source extension + bridge trigger | hash-bound front-end circuit partitioning; Good Split/n-Split; single-machine prover-memory benchmark; contrast with DIZK cluster route | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[memory-efficient-snarks|Memory-efficient SNARKs]] and [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]] |
| [[sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql|A Zero-Knowledge Version of vSQL]] | source extension + bridge evidence | function-independent preprocessing zero-knowledge argument; zk-VPD; committed sum-check/CMT | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route VC details through [[verifiable-computation-systems|Verifiable computation systems]] and component details through [[polynomial-commitments|Polynomial commitments]] / [[sum-check-protocol|Sum-check protocol]] |
| [[doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations|Succinct Zero Knowledge for Floating Point Computations]] | source extension + bridge trigger | relative-error floating/fixed point proof compiler; commit-and-prove backend; batch range proof without bit decomposition; R1CS-size evidence | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[floating-point-snarks|Floating-point SNARKs]], [[commit-and-prove-arguments|Commit-and-prove arguments]] and [[commit-and-prove-arguments-to-floating-point-snarks|Commit-and-prove arguments -> Floating-point SNARKs]] |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | source extension + child split trigger | FRI/batched FRI opening-consistency; IOPP-to-erasure-code-commitment compiler for DAS | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[fri-iopps|FRI IOPPs]] and [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization]] | source extension + child split trigger | SNARK-friendly verifiable encryption; commit-carrying encryption; verifiable decryption; rerandomizable proof/ciphertext | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[verifiable-encryption|Verifiable encryption]] and [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]] |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs]] | source extension + child split trigger | proof-system benchmarking/evaluation axis; arithmetic and circuit benchmarks; runtime estimation; hardware sensitivity | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合 | yes | route details through [[proof-system-benchmarking|Proof-system benchmarking]]; analyze zk-Bench repo if implementation/reproducibility details matter |
| [[sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation|Hekaton: Horizontally-Scalable zkSNARKs via Proof Aggregation]] | source extension + bridge trigger | divide-and-aggregate distributed zkSNARK; partition-friendly memory checking; Mirage commit-carrying aggregation; source-local scaling benchmark | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[distributed-proof-generation|Distributed proof generation]], [[snark-proof-aggregation|SNARK proof aggregation]] and [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | source extension + child split trigger | private delegated proving; witness-private prover outsourcing; WCC/PCC consistency checkers; KZG-backed binding route | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[private-delegated-proving|Private delegated proving]] and [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | source extension + child split trigger | split prover zkSNARKs; partial-witness precomputation; Groth16-compatible two-phase proving; recursion/folding contrast boundary | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[split-prover-zksnarks|Split prover zkSNARKs]] and [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | source extension + child split trigger | data-parallel CP-NIZK; commit-and-prove proof-of-delivery; fair-exchange proof protocol bridge | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[commit-and-prove-arguments|Commit-and-prove arguments]] and [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]] | source extension + child split trigger | GPU hardware-accelerated proving; NTT/MSM/finite-field arithmetic backend; accelerator-aware benchmark evidence | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[hardware-accelerated-proving|Hardware-accelerated proving]] and [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]] |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] | source extension | custom ASIC / pipelined hardware-accelerated proving; POLY/NTT and MSM accelerator backend; source-local 28 nm benchmark evidence | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | route details through [[hardware-accelerated-proving|Hardware-accelerated proving]] and [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, soundness, performance_compression | deVirgo/Groth16 proof-system engineering transfers to bridge verification cost; chain semantics remain blockchain-specific. | active_seed |
| [[distributed-proof-generation-to-zkrollups|Distributed proof generation -> zkRollup prover scaling]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/applications/blockchain-applications` | application, applies_to, scalability_enabler, implementation_reuse | Prover parallelization transfers to rollup proving; rollup security, data availability, sequencer economics and finality remain application-specific. | active_seed |
| [[folding-schemes-to-memory-efficient-snarks|Folding schemes -> memory-efficient SNARKs]] | `zero-knowledge-proofs/recursion-and-folding/folding-schemes; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | application, method_transfer, performance_compression, dependency | Folding/PCD transfers as a low-memory SNARK construction route; arithmetization, commitments, PCD assumptions and performance estimates remain source-specific. | active_seed |
| [[floating-point-snarks-to-privacy-preserving-location-proofs|Floating-point SNARKs -> privacy-preserving location proofs]] | `zero-knowledge-proofs/proof-systems/floating-point-snarks; zero-knowledge-proofs/applications/privacy-preserving-location-proofs` | application, method_transfer, numerical_soundness, dependency | IEEE 754 arithmetic transfers to geospatial proof accuracy; location provenance and application policy remain source-specific. | active_seed |
| [[commit-and-prove-arguments-to-floating-point-snarks|Commit-and-prove arguments -> Floating-point SNARKs]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; zero-knowledge-proofs/proof-systems/floating-point-snarks` | dependency, compiler_backend, method_transfer | CP transfers as committed-witness/R1CS backend for relative-error floating-point proofs; exact IEEE rounding and application-level numerical stability do not transfer. | active_seed |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-inference` | application, verifiable_computation, privacy, implementation_reuse | Proof-system correctness/hiding transfers to inference computation; model legality, training provenance, safety and quality remain outside the proof statement. | active_seed |
| [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/proof-systems/memory-efficient-snarks` | dependency, method_transfer, prover_space_reduction, implementation_reuse | Product-form sumcheck transfers as a low-memory SNARK building block; sumcheck alone is not a SNARK and does not provide commitments/non-interactivity. | active_seed |
| [[memory-efficient-snarks-to-verifiable-ml-training|Memory-efficient SNARKs -> verifiable ML training]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, scalability_enabler, privacy, implementation_reuse | Low-memory proving transfers to training-certification scalability; model fairness, data legality, accuracy and production governance do not. | active_seed |
| [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] | `zero-knowledge-proofs/proof-systems/fri-iopps; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | method_transfer, application, dependency, transparent_commitment_route | FRI proximity/opening-consistency transfers to DAS commitment/opening; blockchain data availability and execution validity remain separate. | active_seed |
| [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/proof-systems/verifiable-encryption` | dependency, application, method_transfer, proof_encryption_composition | zk-SNARK succinctness/soundness transfers to encrypted-relation proof; encryption privacy, homomorphism, rerandomization and payment fairness remain separate. | active_seed |
| [[distributed-proof-generation-to-snark-proof-aggregation|Distributed proof generation -> SNARK proof aggregation]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation; zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation` | method_transfer, scalability_enabler, performance_compression, implementation_reuse | Proof aggregation can fan in distributed chunk proofs; partitioning, witness distribution, scheduling and exact aggregation scheme remain source-specific. | active_seed |
| [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, verification_enabler, implementation_reuse, privacy_preserving_delegation | KZG supplies consistency-binding commitments/openings; witness-sharing, authentication, adversary threshold and zkSNARK backend remain delegated-proving details. | active_seed |
| [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks; zero-knowledge-proofs/recursion-and-folding` | contrast, design_boundary, phase_decomposition | Phase decomposition transfers as a question; verifier preservation, aux privacy and authorization boundary remain split-prover-specific. | active_seed |
| [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; blockchain-systems/execution-and-transactions/fair-exchange-protocols` | dependency, application, proof_protocol_enabler | CP-NIZK transfers committed-witness consistency; payment/key-release fairness remains blockchain protocol-specific. | active_seed |
| [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/proof-systems/distributed-proof-generation` | contrast, shared_bottleneck, scalability_alternative | Single-machine low-memory routes such as SPLITA and distributed routes such as DIZK share prover-resource pressure, but worker trust, communication, scheduling and cluster economics do not transfer. | active_seed |
| [[hardware-accelerated-proving-to-proof-system-benchmarking|Hardware-accelerated proving -> Proof-system benchmarking]] | `zero-knowledge-proofs/proof-systems/hardware-accelerated-proving; zero-knowledge-proofs/proof-systems/proof-system-benchmarking` | evaluation_axis, benchmark_dependency, hardware_sensitivity, implementation_reuse | Benchmark discipline transfers to accelerated provers; exact speedups, kernel designs, memory budgets and hardware availability remain source-specific. | active_seed |
| [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]] | `zero-knowledge-proofs/proof-systems/zero-knowledge-sets-and-elementary-databases; zero-knowledge-proofs/applications/verifiable-database-queries` | dependency, method_transfer, application | Set-operation query proof transfers to database-query completeness; SQL planning, storage execution, transaction isolation and database engine design do not. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-proof-systems | is_a | nahida-knowledge-zero-knowledge-proofs | vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md; vault/04_Knowledge/zero-knowledge-proofs.md | medium | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-modular-zksnarks | vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md | medium | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-zk-snarks | vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md | medium | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-distributed-proof-generation | vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-floating-point-snarks | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/floating-point-snarks.md | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-fri-iopps | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/fri-iopps.md | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md | vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md | medium | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md | medium | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-memory-efficient-snarks | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md | Mangrove source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md | ZKLP source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md | zkLLM source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md | Sparrow source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md | FRIDA source note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-sum-check-protocol-to-memory-efficient-snarks | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-fri-iopps-to-data-availability-sampling | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-verifiable-encryption | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/verifiable-encryption.md | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md | SAVER source note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-zk-snarks-to-verifiable-encryption | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-proof-system-benchmarking | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-commit-and-prove-arguments | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/commit-and-prove-arguments.md | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md | zk-Bench source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-7ec0866c4734-hekaton-horizontally-scalable-zksnarks-proof-aggregation.md | Hekaton source note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-distributed-proof-generation-to-snark-proof-aggregation | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md | Siniel source note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-private-delegated-proving-to-kzg-commitments | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md | Split Prover source note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-split-prover-zksnarks-to-recursion-and-folding | bridge note | medium | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md | ZKCPlus source note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-hardware-accelerated-proving | [[hardware-accelerated-proving|Hardware-accelerated proving]] | high | active_seed |
| nahida-knowledge-proof-systems | has_child | nahida-knowledge-zero-knowledge-sets-and-elementary-databases | [[zero-knowledge-sets-and-elementary-databases|Zero-knowledge sets and elementary databases]] | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md | GZKP source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md | PipeZK source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md | DIZK source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md | Gemini source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md | Epistle source note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/sha256-17844a65dcd5-zk-vsql-zero-knowledge-version-of-vsql.md | zk-vSQL §1/§3-§6 | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations.md | Garg et al. §2-§6; relative-error floating-point CP compiler | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-commit-and-prove-arguments-to-floating-point-snarks | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-memory-efficient-snarks-to-kzg-commitments | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md | SPLITA source note; hash-bound memory-efficient SNARK route | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation | bridge note; SPLITA and DIZK source notes | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-hardware-accelerated-proving-to-proof-system-benchmarking | bridge note | high | active_seed |
| nahida-knowledge-proof-systems | evidenced_by | vault/03_Sources/papers/eprint-2023-156-zero-knowledge-functional-elementary-databases.md | ZK-FEDB source note; set-operation ZKS and functional EDB route | high | active_seed |
| nahida-knowledge-proof-systems | bridges_to | nahida-bridge-zero-knowledge-sets-to-verifiable-database-queries | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Groth16、PLONK、STARK、IOP/PCP、arithmetization、aPlonk/deVirgo primary 等 comparison sources 缺。 | 影响本节点 foundation 和 distributed proving comparison 完整性；DIZK PDF 已吸收，但 repo/current artifact 未验证。 | nahida-research-search or nahida-update | medium | queued |
| DIZK repository/current artifact 缺。 | DIZK PDF 已吸收为 cluster proving seed，但 source code、current maintenance 和 reproducibility scripts 未分析。 | nahida-github-repo-analyze | medium | queued_if_repo_known |
| Proof aggregation primary sources 缺 SnarkPack/TIPP 等；Hekaton 已吸收为 commit-carrying heterogeneous aggregation route。 | 影响 verifier-cost/proof-size optimization 路线比较 | nahida-update | high | pending_queue |
| DARK/Spartan/PCD/Plonk primary sources 缺。 | Gemini 已补；仍影响 memory-efficient SNARKs 路线比较和 Mangrove/Gemini 边界校准 | nahida-update or nahida-research-search | high | queued |
| Floating-point ZKP prior sources 缺。 | 影响 IEEE 754 SNARK circuits 的 novelty 和可迁移性比较 | nahida-update or nahida-research-search | high | queued |
| Exact IEEE route vs relative-error route comparison still thin. | ZKLP and Garg et al. show two useful floating-point proof semantics, but the decision rule for finance/scientific/ML workloads needs more sources and numerical-analysis evidence. | nahida-update / nahida-research-search | high | queued |
| zkML/verifiable inference prior systems 缺。 | 影响 ML operator proving 和 committed-model inference 的路线比较 | nahida-update or nahida-research-search | high | queued |
| Ligetron/Sparrow/Gemini/Epistle 对比来源仍薄。 | 影响 space-efficient SNARKs 内部路线比较，尤其 public parameters、buffer accounting、R1CS streaming、Plonkish streaming 与 data-parallel circuit assumptions。 | nahida-update or nahida-research-search | medium | queued |
| Hash-bound circuit partitioning follow-up sources 缺。 | SPLITA 给出 Good Split/n-Split 的 R1CS/xJsnark/libsnark route，但 arbitrary-circuit split search、SNARK-friendly hash choice 和 non-Groth16 backend 是否可迁移仍需更多来源。 | nahida-research-search / nahida-update | medium | queued |
| Function-independent preprocessing comparison sources 缺。 | zk-vSQL 补了 zero-knowledge vSQL route，但仍缺 vSQL original、CMT/GKR、Pinocchio/Geppetto/Universal-circuit comparison 来校准 setup/circuit-independence tradeoff。 | nahida-update / nahida-research-search | medium | queued |
| Original FRI、DEEP-FRI、STARK/transparent proof-system primary sources 缺。 | FRIDA 提供 FRI opening-consistency application seed，但不足以完成 FRI/STARK foundation。 | nahida-update or nahida-research-search | high | queued |
| Generic verifiable encryption canonical sources、ZKCP/FairSwap-like comparison sources 缺。 | SAVER 和 ZKCPlus 提供 VE/CP-adjacent seeds，但不足以完成 verifiable-encryption foundation 或 fair-exchange protocol landscape。 | nahida-update or nahida-research-search | high | queued |
| CP-NIZK/commit-and-prove canonical comparison sources still thin. | ZKCPlus/LegoSNARK/Geppetto/SAVER/Mangrove 足以创建 foundation-thin node，但 construction taxonomy 仍不完整。 | nahida-research-search / nahida-update | high | queued |
| Current proof-system benchmark and repo evidence 缺。 | zk-Bench 提供 2023 benchmark/tooling seed；当前工具选择和生产性能需要 repo/current benchmark refresh。 | nahida-github-repo-analyze / nahida-research-search | high | queued |
| Private delegated proving 对照 sources 缺。 | Siniel 给出 strong seed，但 EOS、zkSaaS、FHE-based 或 collaborative zkSNARKs 还没吸收，暂不能把其 WCC/PCC 设计泛化为全领域标准。 | nahida-update / nahida-research-search | high | queued |
| Split prover non-Groth16 follow-up 与实现 evidence 缺。 | Split Prover 给出 Groth16 theory route；需要判断 PLONK/STARK/transparent systems 和真实 delegatable-payment workload 是否支持同类 split。 | nahida-research-search / nahida-github-repo-analyze | high | watch |
| Accelerated prover sources and repos still thin. | GZKP provides a strong GPU source seed and PipeZK provides a custom ASIC seed, but FPGA/current GPU prover and production artifacts are needed before a mature accelerator taxonomy. | nahida-update / nahida-github-repo-analyze / nahida-daily-fetch | high | queued |
| ZKS/ZK-EDB foundation and private query sources are thin. | ZK-FEDB provides a strong set-operation route, but MRK03, ZK-EEDB, ZKSQL and private aggregate query sources are still needed before a mature database-query proof taxonomy. | nahida-update / nahida-research-search | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkbridge | Added deVirgo/data-parallel distributed proof generation as source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-snarkfold | Added SNARK proof aggregation as proof-system engineering source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Split distributed proof generation into child method-family node and added Pianist source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Split memory-efficient SNARKs into child problem node and added Mangrove source extension. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-gemini-elastic-snarks | Added Gemini elastic SNARK / streaming R1CS source extension and KZG bridge. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-epistle-elastic-snarks | Added Epistle elastic Plonkish / HyperPlonk source extension and elastic SNARK child-route evidence. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Added SPLITA hash-bound circuit partitioning route and bridge from memory-efficient SNARKs to distributed proof generation. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-vsql-zk | Added function-independent preprocessing zero-knowledge argument route and component bridge evidence. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-succinct-zk-floating-point | Added relative-error floating-point proof route and bridge from commit-and-prove arguments to floating-point SNARKs. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zk-functional-elementary-databases | Added ZKS/ZK-EDB method-family seed and bridge to verifiable database queries. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zklp-floating-point-snarks | Split floating-point SNARKs into child method-family node and added ZKLP source extension. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Added ML tensor/operator proving source extension for zkML verifiable inference. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Added data-parallel space-efficient SNARK route and bridges to sum-check/verifiable ML training. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Split FRI IOPPs into a foundation-thin method-family node and linked it to DAS via bridge. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Split verifiable encryption into a foundation-thin method-family node and linked it to zk-SNARKs/FDE boundaries. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zk-bench-proof-system-benchmarking | Split proof-system benchmarking into a foundation-thin evaluation-axis node and added zk-Bench as source extension. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-hekaton-proof-aggregation | Added Hekaton as divide-and-aggregate proof-system source extension and linked distributed proof generation to SNARK proof aggregation. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-siniel-private-delegated-proving | Added Siniel as private delegated proving source extension and linked delegated proving to KZG commitments. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-split-prover-zksnarks | Added Split Prover as partial-witness delegated proving source extension and linked it to recursion/folding boundary. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Split commit-and-prove arguments into a foundation-thin method-family node and linked CP-NIZK to blockchain fair exchange. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-gzkp-hardware-accelerated-proving | Split hardware-accelerated proving into a foundation-thin problem node and linked it to proof-system benchmarking. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-pipezk-pipelined-architecture | Added PipeZK as custom ASIC / pipelined accelerator evidence under hardware-accelerated proving. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-dizk-distributed-zkp | Added DIZK as Spark-distributed Groth zkSNARK source extension under distributed proof generation. | 1 source note | codex |
