---
id: "nahida-knowledge-zk-snarks"
title: "zk-SNARKs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "review"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "zk-snarks"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-proof-systems"
child_knowledge_refs:
  - "nahida-knowledge-modular-zksnarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "zk-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/zk-snarks"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-zk-snarks"
    relation: "is_a"
    to: "nahida-knowledge-proof-systems"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md"
    confidence: "low"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "has_child"
    to: "nahida-knowledge-modular-zksnarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md"
    confidence: "low"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
    confidence: "low"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-cross-chain-privacy-preserving-auditing.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-trustless-cross-chain-bridges.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-privacy-preserving-blockchain-authentication.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-verifiable-encryption"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-verifiable-encryption.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
    evidence_refs:
      - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zk-snarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing"
  - "nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges"
  - "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
  - "nahida-bridge-zk-snarks-to-verifiable-encryption"
source_note_refs:
  - "vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md"
  - "vault/03_Sources/papers/sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges.md"
  - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
  - "vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md"
  - "vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md"
  - "vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md"
  - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md"
  - "vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md"
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
  - "vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md"
  - "vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md"
  - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
  - "vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md"
  - "vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md"
  - "vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md"
representative_source_refs:
  - "iacr:2019/142"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3658644.3690318"
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "doi:10.1145/3575693.3575711"
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "doi:10.1109/TC.2023.3235975"
query_keys:
  - "zk-SNARKs"
  - "zk-snarks"
  - "SNARK"
  - "succinct non-interactive arguments"
  - "zkBridge"
  - "zkLogin"
  - "SNARK proof aggregation"
  - "Groth16 aggregation"
  - "distributed Plonk"
  - "memory-efficient SNARKs"
  - "folding-based SNARKs"
  - "Mangrove"
  - "floating-point SNARKs"
  - "IEEE 754 SNARK circuits"
  - "ZKLP"
  - "verifiable inference"
  - "zkML"
  - "ZK proofs for LLMs"
  - "ZK proofs for CNN inference"
  - "zkCNN"
  - "convolution sumcheck"
  - "GKR CNN proof"
  - "tensor lookup arguments"
  - "space-efficient zkSNARKs"
  - "space-efficient sumcheck"
  - "Sparrow"
  - "verifiable aggregation"
  - "verifiable federated aggregation"
  - "zkFL"
  - "PZKP-FL"
  - "Groth16 training proof"
  - "verifiable federated training"
  - "verifiable encryption"
  - "SAVER"
  - "SNARK-friendly encryption"
  - "commit-carrying encryption"
  - "SNARK benchmarking"
  - "zk-Bench"
  - "ZKP performance evaluation"
  - "split prover zkSNARKs"
  - "Groth16 split prover"
  - "two-phase zkSNARK proving"
  - "hardware-accelerated zkSNARK prover"
  - "GPU zkSNARK prover"
  - "GZKP"
  - "PipeZK"
  - "ASIC zkSNARK prover"
  - "DIZK"
  - "Spark zkSNARK"
  - "distributed Groth16"
  - "EOS private delegation of zkSNARK provers"
  - "universal-setup zkSNARK delegation"
  - "Gemini"
  - "elastic SNARKs"
  - "streaming R1CS"
  - "Epistle"
  - "elastic Plonk"
  - "Plonkish elastic SNARK"
  - "Split hash-based memory optimization"
  - "Good Split"
  - "hash-bound zkSNARK circuit partitioning"
aliases:
  - "SNARK"
  - "succinct non-interactive arguments"
  - "SNARK proof aggregation"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zk-snarks"
  - "recursive-proof-compression"
  - "privacy-preserving-blockchain-authentication"
  - "snark-proof-aggregation"
  - "distributed-proof-generation"
  - "memory-efficient-snarks"
  - "floating-point-snarks"
  - "zkml"
  - "verifiable-inference"
  - "cnn-inference-proofs"
  - "verifiable-ml-training"
  - "verifiable-aggregation"
  - "federated-learning-integrity"
  - "federated-learning"
  - "verifiable-encryption"
  - "proof-system-benchmarking"
  - "split-prover-zksnarks"
  - "hardware-accelerated-proving"
  - "gpu-proving"
  - "asic-proving"
  - "cluster-proving"
  - "private-delegated-proving"
  - "elastic-snarks"
  - "streaming-r1cs"
  - "plonkish-snarks"
  - "hyperplonk"
  - "front-end-circuit-partitioning"
  - "hash-bound-subcircuits"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
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
  - "nahida-knowledge-20260620-zklogin"
  - "nahida-knowledge-20260620-snarkfold"
  - "nahida-knowledge-20260620-pianist"
  - "nahida-knowledge-20260620-mangrove"
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
  - "nahida-knowledge-20260621-pzkp-fl"
  - "nahida-knowledge-20260621-saver-verifiable-encryption"
  - "nahida-knowledge-20260621-zk-bench-proof-system-benchmarking"
  - "nahida-knowledge-20260621-split-prover-zksnarks"
  - "nahida-knowledge-20260621-gzkp-hardware-accelerated-proving"
  - "nahida-knowledge-20260622-pipezk-pipelined-architecture"
  - "nahida-knowledge-20260622-dizk-distributed-zkp"
  - "nahida-knowledge-20260623-eos-private-delegated-proving"
  - "nahida-knowledge-20260622-gemini-elastic-snarks"
  - "nahida-knowledge-20260623-epistle-elastic-snarks"
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
source_refs:
  - "iacr:2019/142"
  - "sha256:fbf50bc93d96eb17631617fb02392162201330463d0eb6a955c0d91c0587f50a"
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "arxiv:2404.14983v2"
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3658644.3690318"
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "sha256:99262a57dce40dfadae1db01d432f088a2780dcc3e16c6316679558dbbed9afa"
  - "sha256:4b56be6d2631a5c5eed0d25ac8430c39976b270ad97f02a3e09df75c96827526"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
  - "doi:10.1145/3575693.3575711"
  - "doi:10.1109/isca52012.2021.00040"
  - "sha256:2714176ef590521c89d34c8b88bc873d52a9c165946fe62996f8c098eede8d75"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:bdda577b4120b37ed21d44cdb73a64376ed153a5fbc79fc0ea62bc171a4635f8"
  - "iacr:2024/872"
  - "doi:10.1109/TC.2023.3235975"
confidence: "low"
trust_tier: "primary"
---

# zk-SNARKs

## 定义与范围

- 定义: zk-SNARKs 是 succinct non-interactive arguments of knowledge 的证明系统族，目标是让 verifier 用短 proof 和较低验证成本检查大计算/约束关系，并在需要时提供零知识。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `zk-snarks`
- Aliases/query keys: SNARK, succinct non-interactive arguments
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `zk-snarks`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

model_prior_background: zk-SNARKs 依赖 arithmetization、commitment/polynomial machinery、setup assumptions 和 prover/verifier tradeoffs。当前 vault 只有 LegoSNARK/KZG/Nova 等间接 seed，因此本节点是 foundation_thin。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[proof-systems|proof-systems]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

为 ZKP proof systems 提供比单个 LegoSNARK paper 更上层的检索入口，避免从某篇框架论文反推 zk-SNARK 定义。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[proof-systems|proof-systems]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| arithmetization to constraints | arithmetization to constraints | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| commitment/opening backend | commitment/opening backend | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| succinct proof and verifier | succinct proof and verifier | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| setup/trust/performance tradeoffs | setup/trust/performance tradeoffs | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| proof aggregation | 将多个 SNARK proofs 聚合成 verifier 更便宜检查的对象，用于降低批量证明验证成本。 | 应用需要验证多个 proofs，且目标 SNARK 支持 aggregation route。 | 具体 proof-system relation、setup、curve/precompile 和 aggregator work 需要单独分析；SnarkFold 不升级 zk-SNARK foundation。 | [[snark-proof-aggregation|SNARK proof aggregation]]; [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold]] |
| distributed SNARK/proof generation | 把 SNARK/proof-system prover work 分摊到多台机器或多阶段参与者，让大电路、大 batch、private delegation 或 partial-witness workflow 在可接受时间和内存中生成 proof。 | prover-side time/memory、witness privacy 或 witness-arrival time 是瓶颈，且 proof-system protocol 支持分布式 polynomial/commitment aggregation、cluster backend、delegated proving 或 split proving。 | 不等于 zk-SNARK foundation；Groth/Spark、Plonk/KZG/DKZG、EOS/Siniel delegated proving、Groth16 split details 和 worker/aux trust 留在 [[distributed-proof-generation|Distributed proof generation]] / [[private-delegated-proving|Private delegated proving]] / [[split-prover-zksnarks|Split prover zkSNARKs]]。 | [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK]]; [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist]]; [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| split prover Groth16 route | 把 Groth16 prover 拆成 early aux generation 与 late proof completion，保持最终 proof/verifier 接口不变。 | 早到 witness 与晚到 witness 可清晰拆分，且第二阶段 prover 不应知道早到 witness。 | Groth16-specific；不升级 zk-SNARK foundation，也不说明 PLONK/STARK/transparent systems 可直接 split。 | [[split-prover-zksnarks|Split prover zkSNARKs]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| memory-efficient / streaming SNARKs | 降低单个 SNARK prover 的 peak memory、pass 数或全局 trace 持有需求，同时保留 succinct verification。 | 单机内存/数据遍历是瓶颈，不一定需要多机 proving。 | 不等于 proof aggregation 或 distributed proof generation；Mangrove/Sparrow/Gemini/Epistle/SPLITA 都不升级 zk-SNARK foundation。 | [[memory-efficient-snarks|Memory-efficient SNARKs]]; [[elastic-snarks|Elastic SNARKs]]; [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove]]; [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]]; [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] |
| front-end circuit partitioning / hash-bound zkSNARKs | 在 R1CS/arithmetic-circuit 前端切分大电路，用 hash digest 绑定跨切分中间状态，从而降低单机 prover peak memory。 | 电路存在 small cross-cut state / Good Split，且可接受 hash circuit overhead 与多 proof/setup/verify steps。 | 属于 low-memory prover engineering route；不能外推出 PLONK/STARK 等系统都可同样切分，也不提供分布式 worker model。 | [[memory-efficient-snarks|Memory-efficient SNARKs]]; [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split]] |
| elastic SNARKs / streaming R1CS and Plonkish PIOP | 同一个 SNARK proof/verifier interface 下，让 prover 在 time-efficient 与 space-efficient 配置之间选择；Gemini 用 streaming R1CS，Epistle 用 streaming HyperPlonk/Plonkish PIOP。 | R1CS 或 Plonkish trace/index/witness 可 streaming，且 PCS/PIOP 层支持低内存生成。 | 增加 prover time/passes；KZG setup/trust assumptions 保留；Epistle 的一般 lookup streaming 仍是缺口；不替代 zk-SNARK 基础定义。 | [[elastic-snarks|Elastic SNARKs]]; [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini]]; [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle]] |
| floating-point arithmetic circuits | 在 SNARK 中准确模拟 IEEE 754 FP32/FP64 operations，支撑真实软件数值语义的证明。 | 应用电路依赖 floating-point geospatial/ML/scientific computations。 | 不等于 zk-SNARK foundation；rounding、lookup、hints 和 abnormal values 留在 [[floating-point-snarks|Floating-point SNARKs]]。 | [[floating-point-snarks|Floating-point SNARKs]]; [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] |
| verifiable ML/CNN/LLM inference | 把 succinct/ZK proof machinery 用于证明 committed model 的 inference relation，并隐藏 weights 或 witness。 | 应用需要验证 inference output，但不能公开模型参数或中间张量。 | 不等于 zk-SNARK foundation；operator decomposition、quantization、GPU/CPU proving 和 AI-legitimacy 边界留在 [[verifiable-inference|Verifiable inference]]。 | [[verifiable-inference|Verifiable inference]]; [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]]; [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]] |
| verifiable ML training | 把 succinct/ZK proof machinery 用于证明 committed data/model/seed 下的 training 或 certification relation。 | 训练 relation 可被形式化，并且需要隐藏数据/模型或压低 verifier cost。 | 不等于 zk-SNARK foundation；训练数据合法性、公平性、泛化和模型质量不由 SNARK 自动保证。 | [[verifiable-training|Verifiable ML training]]; [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] |
| federated iterative training proofs | 用 Groth16 证明本地训练 piece 的电路满足性，再用 Sigma protocol 绑定 piece 连续性。 | FL participant 需要证明自己真实执行本地训练，同时隐藏 local data/intermediate values。 | Proof 数量、trusted setup、fixed-point/Taylor approximation 和 smart-contract assumptions 都是系统边界。 | [[verifiable-training|Verifiable ML training]]; [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| SNARK-friendly verifiable encryption | 用 zk-SNARK 证明加密明文满足关系，并通过 ciphertext/proof 连接避免把 encryption algorithm 放进 circuit。 | 应用需要隐藏明文但公开验证其合法性，如 encrypted ballot、encrypted identity 或 committed-data proof。 | 不等于 zk-SNARK foundation；SAVER 是 pairing/Groth16-like route，encryption privacy、rerandomization 和 verifiable decryption 是独立安全目标。 | [[verifiable-encryption|Verifiable encryption]]; [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER]] |
| SNARK benchmarking and tool selection | 用统一 benchmark framework 比较 arithmetic libraries、ZKP development tools、setup/prove/verify、memory、proof size 和 hardware sensitivity。 | 开发者需要选择 proof-system stack，或判断某篇 paper benchmark 是否能迁移到真实 workload。 | 不等于 zk-SNARK foundation；exact rankings 依赖版本、硬件和 circuit implementation，当前决策需要刷新。 | [[proof-system-benchmarking|Proof-system benchmarking]]; [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench]] |
| hardware-accelerated zkSNARK proving | 用 GPU/ASIC/硬件感知 backend 加速 zkSNARK prover 中的 NTT、MSM 和 finite-field arithmetic。 | prover latency/throughput 是瓶颈，且目标 protocol 的 proving phases 可映射到 accelerator。 | 不改变 zk-SNARK protocol/security；exact speedups 依赖 hardware、curve、field bit width、workload sparsity、module-vs-end-to-end boundary 和 implementation。 | [[hardware-accelerated-proving|Hardware-accelerated proving]]; [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP]]; [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs|LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | paper | 作为 application-only source extension：使用 deVirgo/Groth16 将跨链 light-client verification 压缩为链上短 proof verification | application source; not zk-SNARK foundation evidence | `p8-p13` |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | paper | 作为 application-only source extension：使用 Groth16 隐藏 JWT/salt witness 并支撑链上认证 | application source; not zk-SNARK foundation evidence | `p1-p20` |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | paper | 作为 aggregation-only source extension：用 split IVC/Groth16 folding 聚合多个 SNARK proofs | proof aggregation evidence; not zk-SNARK foundation evidence | `p1-p19`, `p22-p29` |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | paper | 作为 engineering-only source extension：用 Plonk/bivariate KZG 分布式生成 proof，服务 zkRollup prover scaling | proof generation scalability evidence; not zk-SNARK foundation evidence | `p1-p15` |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | paper | 作为 prover-resource source extension：用 folding/PCD 构造 low-memory SNARK | memory-efficient SNARK evidence; not zk-SNARK foundation evidence | `p1-p69` |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | paper | 作为 numeric-circuit source extension：用 Groth16/Plonk 承载 IEEE 754 compliant floating-point operations | floating-point circuit evidence; not zk-SNARK foundation evidence | `p1-p19` |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | paper | 作为 verifiable inference source extension：用 sumcheck、commitments、tensor lookup 和 attention-specific proof 承载 LLM inference correctness | zkML application evidence; not zk-SNARK foundation evidence | `p1-p16` |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | paper | 作为 verifiable inference source extension：用 FFT/convolution sumcheck、GKR 和 polynomial commitments 承载 CNN prediction/accuracy proof | zkML application/operator-proof evidence; not zk-SNARK foundation evidence | `p1-p18` |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper | 作为 prover-resource / zkML training source extension：用 space-efficient sumcheck、streaming GKR 和 zkFTP 承载 data-parallel circuits 与 forest training proofs | memory/training application evidence; not zk-SNARK foundation evidence | `p1-p15` |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | paper | 作为 prover-resource source extension：用 elastic SNARK / streaming R1CS / elastic KZG 让同一 proof interface 支持不同 prover memory/time 配置 | memory-efficient SNARK evidence; not zk-SNARK foundation evidence | `Abstract`, `§2.1-§2.8`, `§4-§10` |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | paper | 作为 prover-resource source extension：用 streaming HyperPlonk/Plonkish PIOP 和 elastic multilinear KZG 扩展 elastic SNARK route | memory-efficient SNARK evidence; not zk-SNARK foundation evidence | `Abstract`, `§2`, `§4-§7` |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | paper | 作为 prover-resource source extension：用 hash-bound circuit partitioning / Good Split / n-Split 降低单机 zkSNARK prover memory | memory-efficient SNARK evidence; not zk-SNARK foundation evidence | `p1-p12`, Table II/III |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 作为 application-only source extension：用 Groth16 per-piece proofs 承载 FL local training correctness，并用 Sigma proofs 绑定 continuity / aggregation consistency | zkML/FL application evidence; not zk-SNARK foundation evidence | `p1-p15` |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization]] | paper | 作为 application/composition source extension：用 Groth16-like proof/ciphertext linkage 承载 encrypted plaintext relation proof | verifiable-encryption evidence; not zk-SNARK foundation evidence | `p1-p44` |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs]] | paper | 作为 evaluation-only source extension：比较 SNARK/ZKP tooling stack 并提供 runtime-estimation methodology | benchmarking evidence; not zk-SNARK foundation evidence | `p1-p21`, `Appendix A-B` |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | paper | 作为 Groth16 engineering source extension：保持 Groth16 verifier 的 two-phase proving、aux split zero-knowledge 和 second-phase lower bound | split-prover evidence; not zk-SNARK foundation evidence | `p1-p23` |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP: A GPU Accelerated Zero-Knowledge Proof System]] | paper | 作为 prover-backend source extension：用 GPU 加速 zkSNARK proof generation 的 NTT/MSM/finite-field arithmetic | hardware-accelerated proving evidence; not zk-SNARK foundation evidence | `p1-p14` |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture]] | paper | 作为 prover-backend source extension：用 custom ASIC / pipelined architecture 加速 zkSNARK prover 的 POLY/NTT 和 MSM | hardware-accelerated proving evidence; not zk-SNARK foundation evidence | `p1-p13` |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | paper | 作为 prover-backend source extension：用 Apache Spark 分布式执行 Groth zkSNARK setup/prover 的 FFT/Lag/MSM 和 QAP reductions | distributed proof generation evidence; not zk-SNARK foundation evidence | `p1-p19` |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | paper | 作为 prover-delegation source extension：用 isolated/collaborative delegated SNARK protocols 和 PIOP consistency checking 私有外包 universal-setup zkSNARK prover | private delegated proving evidence; not zk-SNARK foundation evidence | `p1-p18` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-22`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-22`。
- 综合: 本节点主要是为了修复基础概念缺口；需要后续 foundation_pack research 或 Groth16/PLONK/STARK/Plonk source 才能升级。SnarkFold 新增 aggregation-only source extension；Pianist/DIZK/EOS 分别新增 distributed proving、cluster proving 和 private delegated proving engineering extension；Split Prover 新增 Groth16-compatible split proving extension，说明 zkSNARK prover interface 可以按 witness 到达时间拆分，但这些都不替代 Groth16/zk-SNARK foundation；GZKP 和 PipeZK 新增 hardware-accelerated prover extension，说明 zkSNARK proof generation 的 NTT/MSM/finite-field arithmetic 可分别通过 GPU backend 和 custom ASIC/pipelined backend 优化，但这同样不替代 zk-SNARK foundation。Mangrove、Sparrow、Gemini、Epistle 与 SPLITA 新增 prover-resource extension，其中 Gemini 将低内存路线落在 streaming R1CS、elastic PIOP 与 elastic KZG 上，Epistle 将同一 elastic SNARK 思想扩展到 Plonkish/HyperPlonk multivariate PIOP 与 elastic multilinear KZG，SPLITA 将低内存路线落在 R1CS front-end circuit partitioning 与 hash-bound intermediate state 上；ZKLP 新增 numeric-circuit extension；zkCNN/zkLLM/Sparrow/PZKP-FL 则分别给出 CNN inference、LLM inference、training certification 和 federated iterative training 等 zkML application/proof-engineering extension；SAVER 新增 verifiable-encryption composition route；zk-Bench 新增 benchmarking/evaluation-only source extension。它们都不替代 zk-SNARKs 的基础定义。

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
| [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]] | application-only source extension: uses zk-SNARK/Groth16 for cross-chain unlinkability and audit compression, but does not upgrade zk-SNARK foundation status | Bridge Links; relation graph | no | keep as bridge evidence, not foundation evidence |
| [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]] | application-only source extension: uses deVirgo and Groth16 recursive compression for trustless cross-chain bridge verification, but does not upgrade zk-SNARK foundation status | Bridge Links; relation graph; representative Sources | no | keep as bridge evidence, not foundation evidence |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | application-only source extension: uses Groth16 for privacy-preserving credential authentication, but does not upgrade zk-SNARK foundation status | Bridge Links; relation graph; representative Sources | no | keep as bridge evidence, not foundation evidence |
| [[sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation|SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation]] | aggregation-only source extension: uses Groth16 folding/split IVC to aggregate multiple SNARK proofs, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[snark-proof-aggregation|SNARK proof aggregation]] |
| [[sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp|Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs]] | engineering-only source extension: uses Plonk/bivariate KZG distributed proving for zkRollup/general-circuit prover scalability, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[distributed-proof-generation|Distributed proof generation]] |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | prover-delegation source extension: uses PIOP+PCS delegated SNARK protocols to outsource prover work while hiding witness, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[private-delegated-proving|Private delegated proving]] |
| [[sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks|Mangrove: A Scalable Framework for Folding-based SNARKs]] | prover-resource source extension: uses folding/PCD to construct low-memory/two-pass SNARKs, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | numeric-circuit source extension: uses Groth16/Plonk backends for IEEE 754 compliant floating-point operations, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[floating-point-snarks|Floating-point SNARKs]] |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | zkML/verifiable-inference source extension: uses proof-system machinery for committed LLM inference, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph; Bridge Links | no | route detailed comparison through [[verifiable-inference|Verifiable inference]] |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | zkML/verifiable-inference source extension: uses FFT/convolution sumcheck, GKR and polynomial commitments for CNN prediction/accuracy proof, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph; Bridge Links | no | route detailed comparison through [[verifiable-inference|Verifiable inference]] and [[sum-check-protocol|Sum-check protocol]] |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | prover-resource / zkML-training source extension: uses space-efficient sumcheck and streaming GKR for data-parallel zkSNARKs, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[memory-efficient-snarks|Memory-efficient SNARKs]] and [[verifiable-training|Verifiable ML training]] |
| [[sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments|Gemini: Elastic SNARKs for Diverse Environments]] | prover-resource source extension: uses streaming R1CS, elastic PIOP and elastic KZG for low-memory zkSNARK proving, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[memory-efficient-snarks|Memory-efficient SNARKs]] and [[kzg-commitments|KZG commitments]] |
| [[eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system|Epistle: Elastic Succinct Arguments for Plonk Constraint System]] | prover-resource source extension: uses streaming Plonkish/HyperPlonk PIOP and elastic multilinear KZG for low-memory zkSNARK proving, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[elastic-snarks|Elastic SNARKs]] and [[kzg-commitments|KZG commitments]] |
| [[doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark|Split: A Hash-Based Memory Optimization Method for zk-SNARK]] | prover-resource source extension: uses hash-bound circuit partitioning / Good Split / n-Split to lower single-machine proving memory, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[memory-efficient-snarks|Memory-efficient SNARKs]] |

| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | application-only source extension: uses Halo2/zk-SNARK-style proof for FL aggregation correctness, but does not upgrade zk-SNARK foundation status | Bridge Links; relation graph; representative Sources | no | route detailed comparison through [[verifiable-aggregation|Verifiable aggregation]] and [[federated-learning-integrity|Federated learning integrity]] |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | application-only source extension: uses Groth16 per-piece proofs for FL local training and Sigma proofs for continuity/aggregation consistency, but does not upgrade zk-SNARK foundation status | 方法族与解决路线; representative Sources; relation graph; Bridge Links | no | route detailed comparison through [[verifiable-training|Verifiable ML training]] and [[federated-learning-integrity|Federated learning integrity]] |
| [[sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization|SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization]] | application/composition source extension: uses Groth16-like verification equation and commit-carrying encryption to prove encrypted plaintext properties without encryption-in-circuit | 方法族与解决路线; representative Sources; relation graph; Bridge Links | no | route detailed comparison through [[verifiable-encryption|Verifiable encryption]] |
| [[sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks|zk-Bench: A Toolset for Comparative Evaluation and Performance Benchmarking of SNARKs]] | evaluation-only source extension: benchmarks SNARK/ZKP tools and arithmetic libraries; creates a separate evaluation-axis node without upgrading foundation status | 方法族与解决路线; representative Sources; relation graph | yes | route detailed comparison through [[proof-system-benchmarking|Proof-system benchmarking]] |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | Groth16 engineering source extension: two-phase partial-witness proving with unchanged verifier; creates split-prover child route under private delegated proving | 方法族与解决路线; representative Sources; relation graph | yes | route detailed comparison through [[split-prover-zksnarks|Split prover zkSNARKs]] |
| [[doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system|GZKP: A GPU Accelerated Zero-Knowledge Proof System]] | prover-backend source extension: accelerates zkSNARK NTT/MSM/finite-field arithmetic on GPU; creates hardware-accelerated proving problem node without upgrading foundation status | 方法族与解决路线; representative Sources; relation graph | yes | route detailed comparison through [[hardware-accelerated-proving|Hardware-accelerated proving]] |
| [[doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture|PipeZK: Accelerating Zero-Knowledge Proof with a Pipelined Architecture]] | prover-backend source extension: accelerates zkSNARK POLY/NTT and MSM with custom ASIC / pipelined architecture; refines hardware-accelerated proving without upgrading foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[hardware-accelerated-proving|Hardware-accelerated proving]] |
| [[sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system|DIZK: A Distributed Zero Knowledge Proof System]] | prover-backend source extension: distributes Groth zkSNARK setup/prover with Spark RDDs, distributed FFT/Lag/MSM and dense row/column aware QAP reductions without upgrading foundation status | 方法族与解决路线; representative Sources; relation graph | no | route detailed comparison through [[distributed-proof-generation|Distributed proof generation]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-cross-chain-privacy-preserving-auditing|zk-SNARKs -> cross-chain privacy-preserving auditing]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, privacy, auditability, implementation_reuse | ZK succinctness/zero-knowledge transfers; cross-chain atomicity, SPV/HTLC semantics, denomination policy and audit-chain incentives are blockchain-specific. | active_seed |
| [[zk-snarks-to-trustless-cross-chain-bridges|zk-SNARKs -> trustless cross-chain bridges]] | `zero-knowledge-proofs/proof-systems/zk-snarks; blockchain-systems/interoperability/cross-chain-protocols` | application, succinct_verification, soundness, performance_compression | Proof soundness/succinctness transfers; bridge liveness, sender-chain finality, application state semantics and relayer incentives remain blockchain-specific. | active_seed |
| [[zk-snarks-to-privacy-preserving-blockchain-authentication|zk-SNARKs -> privacy-preserving blockchain authentication]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication` | application, privacy, authentication, implementation_reuse | ZK hiding/succinctness transfers; OP trust, salt recovery, JWK oracle, app liveness and UX recovery are system-specific. | active_seed |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-inference` | application, verifiable_computation, privacy, implementation_reuse | Proof correctness/hiding transfers to inference relation; model training provenance, legality, safety and quality remain ML/system-specific. | active_seed |

| [[zk-snarks-to-zkml-verifiable-aggregation|zk-SNARKs -> zkML verifiable aggregation]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-aggregation` | application, verifiable_computation, integrity, implementation_reuse | Proof-system soundness/succinctness transfers; FL privacy, client poisoning and convergence remain ML-system-specific. | active_seed |
| [[zk-snarks-to-zkml-verifiable-training|zk-SNARKs -> zkML verifiable training]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, verifiable_computation, privacy, training_integrity | Groth16 soundness/hiding transfers to per-piece training relation; numeric semantics, proof count and model quality do not. | active_seed |
| [[zk-snarks-to-verifiable-encryption|zk-SNARKs -> verifiable encryption]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/proof-systems/verifiable-encryption` | dependency, application, method_transfer, proof_encryption_composition | zk-SNARK relation proof transfers to encrypted-message statements; encryption security, homomorphism, rerandomization and payment fairness do not transfer automatically. | active_seed |

## 关系图谱

| From                       | Relation     | To                                                                                                                                           | Evidence                                                                                                                                        | Confidence | Status      |
| -------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------- |
| nahida-knowledge-zk-snarks | is_a         | nahida-knowledge-proof-systems                                                                                                               | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md                  | low        | active_seed |
| nahida-knowledge-zk-snarks | has_child    | nahida-knowledge-modular-zksnarks                                                                                                            | vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md; vault/04_Knowledge/zero-knowledge-proofs/proof-systems/modular-zksnarks.md | low        | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md                        | vault/03_Sources/papers/eprint-2019-142-legosnark-modular-design-and-composition-of-succinct-zero-knowledge-proofs.md                           | low        | active_seed |
| nahida-knowledge-zk-snarks | bridges_to   | nahida-bridge-zk-snarks-to-cross-chain-privacy-preserving-auditing                                                                           | vault/05_Bridges/zk-snarks-to-cross-chain-privacy-preserving-auditing.md                                                                        | medium     | active_seed |
| nahida-knowledge-zk-snarks | bridges_to   | nahida-bridge-zk-snarks-to-trustless-cross-chain-bridges                                                                                     | vault/05_Bridges/zk-snarks-to-trustless-cross-chain-bridges.md                                                                                  | medium     | active_seed |
| nahida-knowledge-zk-snarks | bridges_to   | nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication                                                                      | vault/05_Bridges/zk-snarks-to-privacy-preserving-blockchain-authentication.md                                                                   | medium     | active_seed |
| nahida-knowledge-zk-snarks | bridges_to   | nahida-bridge-zk-snarks-to-zkml-verifiable-inference                                                                                         | vault/05_Bridges/zk-snarks-to-zkml-verifiable-inference.md                                                                                      | high       | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md                                                   | vault/03_Sources/papers/sha256-0d3ac8a1650e-snarkfold-efficient-snark-proof-aggregation.md                                                      | medium     | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md                                                    | vault/03_Sources/papers/sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp.md                                                       | medium     | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks.md                                              | Mangrove source note                                                                                                                            | medium     | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md                                 | zkLLM source note                                                                                                                               | medium     | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md | zkCNN source note                                                                                                                               | medium     | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md                                | Sparrow source note                                                                                                                             | medium     | active_seed |

| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | medium | active_seed |
| nahida-knowledge-zk-snarks | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation | bridge note | high | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md | source note | medium | active_seed |
| nahida-knowledge-zk-snarks | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-training | bridge note | high | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-99262a57dce4-saver-snark-friendly-verifiable-encryption-rerandomization.md | SAVER source note | medium | active_seed |
| nahida-knowledge-zk-snarks | bridges_to | nahida-bridge-zk-snarks-to-verifiable-encryption | bridge note | high | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-4b56be6d2631-zk-bench-toolset-comparative-evaluation-performance-benchmarking-snarks.md | zk-Bench source note | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md | Split Prover source note | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1145-3575693-3575711-gzkp-gpu-accelerated-zero-knowledge-proof-system.md | GZKP source note; hardware-accelerated proving route | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1109-isca52012-2021-00040-pipezk-pipelined-architecture.md | PipeZK source note; custom ASIC hardware-accelerated proving route | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-2714176ef590-dizk-distributed-zero-knowledge-proof-system.md | DIZK source note; distributed Groth/Spark proving route | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/sha256-bdda577b4120-gemini-elastic-snarks-for-diverse-environments.md | Gemini source note; memory-efficient SNARK route | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system.md | Epistle source note; elastic Plonkish SNARK route | medium | active_seed |
| nahida-knowledge-zk-snarks | evidenced_by | vault/03_Sources/papers/doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark.md | Split/SPLITA source note; hash-bound memory-efficient SNARK route | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Groth16、Pinocchio、PLONK、STARK、survey/textbook sources 缺。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |
| SnarkPack/TIPP/Groth16 aggregation primary sources 缺。 | 影响 proof aggregation 路线而非 zk-SNARK foundation | nahida-update | high | pending_queue |
| Plonk foundation 和 distributed Plonk primary comparison sources 缺。 | Pianist 依赖 Plonk/KZG，但本节点不能用 Pianist 替代 foundation。 | nahida-research-search or nahida-update | high | queued |
| DARK/Spartan/PCD primary sources 缺。 | Gemini 已补；Mangrove/Gemini 仍依赖这些比较/机制背景，但本节点不能用单篇 source 替代 foundation。 | nahida-research-search or nahida-update | high | queued |
| More zkML/verifiable inference comparison sources 缺。 | zkCNN/zkLLM 提供 application evidence，但本节点不能用它们替代 zk-SNARK foundation 或完整 zkML comparison。 | nahida-update or nahida-research-search | high | queued |
| Space-efficient SNARK primary comparison sources 缺。 | Sparrow、Gemini 和 Epistle 已补多条路线，但仍需 Ligetron/GKR+Kopis/DARK/Spartan/Plonkish lookup 对照校准 streaming/low-memory SNARK foundation。 | nahida-update or nahida-research-search | medium | queued |
| Verifiable encryption canonical/comparison sources 缺。 | SAVER 支持 zk-SNARKs 与 VE 的组合 route，但不能替代 Groth16/VE/SAVER 之外的通用 foundation。 | nahida-update or nahida-research-search | medium | queued |
| Current SNARK benchmarking/repo sources 缺。 | zk-Bench 是 2023 evaluation seed；当前工程选择仍需分析 repo/current benchmark evidence。 | nahida-github-repo-analyze / nahida-research-search | high | queued |
| Split prover non-Groth16 sources 缺。 | 当前 Split Prover 是 Groth16-specific source extension；不能由此推断 PLONK/STARK/transparent zkSNARK 都可 split。 | nahida-research-search / nahida-daily-fetch | high | watch |
| Hash-bound circuit partitioning follow-up sources 缺。 | SPLITA 只证明 R1CS/xJsnark/libsnark loop workload 的 Good Split route；需要更多 sources 判断 arbitrary circuits、SNARK-friendly hash 和 non-Groth16 backend 的边界。 | nahida-research-search / nahida-update | medium | watch |
| Accelerated prover sources 仍薄。 | GZKP 是 GPU zkSNARK prover seed，PipeZK 是 custom ASIC seed；仍需 FPGA/current GPU prover/production repo sources 判断硬件加速路线边界。 | nahida-update / nahida-github-repo-analyze | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 2 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkcross | Added application bridge from zk-SNARKs to cross-chain privacy-preserving auditing without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkbridge | Added application bridge from zk-SNARKs to trustless cross-chain bridges without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zklogin | Added application bridge from zk-SNARKs to privacy-preserving blockchain authentication without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-snarkfold | Added aggregation-only source extension from SnarkFold without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Added distributed proving engineering source extension from Pianist without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-mangrove | Added memory-efficient SNARK prover-resource source extension from Mangrove without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zklp-floating-point-snarks | Added floating-point numeric-circuit source extension from ZKLP without upgrading foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Added zkML/verifiable-inference source extension from zkLLM without upgrading foundation status. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Added zkCNN as zkML/CNN inference proof source extension without upgrading zk-SNARK foundation status. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Added space-efficient/data-parallel zkSNARK and zkML training source extension from Sparrow without upgrading foundation status. | 1 source note | codex |

| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Added zkFL as application-only evidence for verifiable aggregation; created zk-SNARKs -> zkML verifiable aggregation bridge. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-saver-verifiable-encryption | Added SAVER as application/composition source extension and linked zk-SNARKs to verifiable encryption. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zk-bench-proof-system-benchmarking | Added zk-Bench as evaluation-only source extension and linked it to proof-system benchmarking. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-split-prover-zksnarks | Added Split Prover as Groth16-compatible split proving source extension without upgrading zk-SNARK foundation. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-gzkp-hardware-accelerated-proving | Added GZKP as hardware-accelerated zkSNARK prover source extension without upgrading foundation status. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-gemini-elastic-snarks | Added Gemini as elastic SNARK / streaming R1CS prover-resource source extension without upgrading foundation status. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-epistle-elastic-snarks | Added Epistle as elastic Plonkish / HyperPlonk prover-resource source extension without upgrading foundation status. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-pipezk-pipelined-architecture | Added PipeZK as custom ASIC hardware-accelerated zkSNARK prover source extension without upgrading foundation status. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-dizk-distributed-zkp | Added DIZK as Spark-distributed Groth zkSNARK prover-backend source extension without upgrading foundation status. | 1 source note | codex |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Added SPLITA as hash-bound circuit-partitioning source extension under memory-efficient zkSNARKs without upgrading foundation status. | 1 source note | codex |
