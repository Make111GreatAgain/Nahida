---
id: "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
title: "zk-SNARKs -> privacy-preserving blockchain authentication"
original_title: "zk-SNARKs -> privacy-preserving blockchain authentication"
file_slug: "zk-snarks-to-privacy-preserving-blockchain-authentication"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "method_to_application"
bridge_status: "active_seed"
endpoint_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication"
endpoint_knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-privacy-preserving-blockchain-authentication"
from_domain: "zero-knowledge-proofs"
to_domain: "zero-knowledge-proofs"
from_direction: "proof-systems"
to_direction: "applications"
from_topic: "zk-snarks"
to_topic: "privacy-preserving-blockchain-authentication"
relation_types:
  - "application"
  - "privacy"
  - "authentication"
  - "implementation_reuse"
directionality: "from_zk_snarks_to_blockchain_authentication"
relationship_thesis: "zk-SNARK-style proofs let a blockchain verifier check that a user possesses a valid signed identity token, a salted address derivation and a nonce-bound ephemeral key without revealing the JWT or stable identifier. The proof system provides witness hiding and succinct verification; OpenID provider trust, JWK freshness, salt recovery, delegated proving privacy, app liveness and account UX remain system-level responsibilities."
transferability: "medium-high"
non_transfer_boundary: "ZK hiding transfers to JWT/salt privacy and succinct verification transfers to validator checks; it does not remove trust in the OpenID provider's authentication, solve salt loss, provide account recovery, guarantee ZK-service unlinkability under normal delegation, or make an app/backend live."
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "zk-snarks"
  - "privacy-preserving-blockchain-authentication"
  - "wallet-onboarding"
  - "OpenID Connect"
source_note_refs:
  - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
knowledge_refs:
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-privacy-preserving-blockchain-authentication"
query_keys:
  - "zk-SNARKs -> privacy-preserving blockchain authentication"
  - "zkLogin bridge"
  - "ZK wallet authentication"
  - "OpenID JWT zero-knowledge authentication"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zklogin"
source_refs:
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "doi:10.1145/3658644.3690356"
confidence: "high"
trust_tier: "primary"
---

# zk-SNARKs -> privacy-preserving blockchain authentication

## 命名与路径

- Original title: zk-SNARKs -> privacy-preserving blockchain authentication
- File slug: `zk-snarks-to-privacy-preserving-blockchain-authentication`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

[[zk-snarks|zk-SNARKs]] 提供短证明、低验证成本、knowledge-soundness 和 zero-knowledge。[[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] 是应用问题: 用户如何用现有身份凭证认证链上交易，同时不公开身份凭证或 off-chain/on-chain identity link。

这个 bridge 的核心是: proof system 负责隐藏 JWT/salt 等 witness，并让 validator 验证“有效身份凭证 -> 地址 -> ephemeral key -> 交易签名”的关系；但身份提供方信任、salt 管理、JWK oracle、应用活性和账户恢复是系统层问题。

## 连接命题

- From: `zero-knowledge-proofs/proof-systems/zk-snarks`
- To: `zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication`
- Relation types: application, privacy, authentication, implementation_reuse
- Directionality: `from_zk_snarks_to_blockchain_authentication`
- Relationship thesis: zk-SNARK-style proofs let a blockchain verifier check that a user possesses a valid signed identity token, a salted address derivation and a nonce-bound ephemeral key without revealing the JWT or stable identifier. The proof system provides witness hiding and succinct verification; OpenID provider trust, JWK freshness, salt recovery, delegated proving privacy, app liveness and account UX remain system-level responsibilities.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks|zk-SNARKs]] | `zero-knowledge-proofs/proof-systems/zk-snarks` | proof-system capability provider; in zkLogin instantiated with Groth16/circom | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | active_seed |
| [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] | `zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication` | application/problem endpoint | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Witness hiding | Hide JWT payload, stable identifier, salt and nonce randomness from public blockchain. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] §1-§4 | Does not hide issuer and does not remove timing side channels. |
| Succinct verification | Validators verify a compact proof rather than receiving full JWT or re-running Web login. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] §4-§5 | Validator cost still exceeds Ed25519; chain must support the verifier and JWK freshness. |
| Circuitized credential checks | Encode JWT signature, address derivation and nonce binding as constraints. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] §5 | Traditional primitives such as SHA-2/RSA are not ZK-friendly, causing circuit cost. |
| Proof delegation boundary | Offload proving while keeping transaction signing local with ephemeral key. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] §4.3 | Normal delegation preserves security but can break unlinkability if service sees JWT/salt. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| zero-knowledge | `zero-knowledge-proofs/proof-systems/zk-snarks` | `privacy-preserving-blockchain-authentication` | Hide the JWT and salt while proving valid OP signature and address derivation. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | Service-side delegation or weak salt strategy can still reveal links. |
| knowledge soundness | `zero-knowledge-proofs/proof-systems/zk-snarks` | `privacy-preserving-blockchain-authentication` | Validator accepts only if a valid witness exists for the tag/address/key relation. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | If the encoded predicate or JWT parsing assumptions are wrong, proof soundness proves the wrong relation. |
| succinct verification | `zero-knowledge-proofs/proof-systems/zk-snarks` | `privacy-preserving-blockchain-authentication` | Replace public JWT disclosure with compact proof verification. | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | Verification/signature size remains larger than native signatures. |

## 类比、依赖或关系边界

The proof system is the privacy and verifier-cost mechanism; authentication remains a system protocol. A good query answer should not say "ZK removes trust in Google"; it should say zkLogin trusts the OpenID Provider for authentication while using ZK to keep JWT claims and stable identifiers off-chain and unlinkable under the chosen salt mode.

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | primary evidence for ZK-based blockchain authentication with existing credentials | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `zero-knowledge-proofs/proof-systems/zk-snarks` | update Bridge Links; source remains application evidence, not foundation definition | active_seed |
| `zero-knowledge-proofs/applications/blockchain-applications` | add child problem and source extension | active_seed |
| `zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication` | create problem node | active_seed |

## 查询入口

- zk-SNARKs -> privacy-preserving blockchain authentication
- zkLogin bridge
- ZK wallet authentication
- OpenID JWT zero-knowledge authentication

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: ZK Address Abstraction, Aptos Keyless, CanDID, OpenPubkey, passkey wallets, nonce-less provider improvements, production security incidents, or sources changing OP/salt/ZK-service boundary.

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] | Methods, Source Extensions, Bridge Links | zkLogin is primary source | active_seed |
| [[blockchain-applications|ZKP blockchain applications]] | Child structure, Methods, Source Extensions, Bridge Links | New child application problem | active_seed |
| [[zk-snarks|zk-SNARKs]] | Bridge Links only | zkLogin uses Groth16 but does not define zk-SNARK foundation | active_seed |

## 刷新规则

- Last checked: `2026-06-20`
- Valid until: `2026-07-20`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity。
