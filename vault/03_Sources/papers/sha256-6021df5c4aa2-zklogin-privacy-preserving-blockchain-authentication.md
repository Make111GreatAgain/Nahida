---
id: "sha256-6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
title: "zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials"
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
  - "p1-p4 abstract, introduction, zkLogin approach, features, challenges and contributions"
  - "p4-p6 OpenID Connect and Tagged Witness Signature preliminaries"
  - "p6-p10 zkLogin system model, address derivation, workflow and modes"
  - "p10-p12 security, unlinkability, nonce-less providers and novel features"
  - "p12-p15 implementation, deployment, circuit optimizations, evaluation and related work"
  - "p15-p20 references and appendices for NIZK/TWS proofs and Groth16 ceremony"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3658644.3690356"
doi: "10.1145/3658644.3690356"
arxiv_id: "2401.11735v2"
venue: "ACM CCS 2024"
year: "2024"
pdf_pages: 20
pdf_sha256: "6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
local_pdf: "~/Desktop/paper/zklogin.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/zklogin-privacy-preserving-blockchain-authentication-with-existing-credentials-6021df5c4aa2-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
topic_ids:
  - "blockchain-applications"
  - "privacy-preserving-blockchain-authentication"
  - "zk-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
  - "blockchain-applications"
  - "privacy-preserving-blockchain-authentication"
primary_ontology_path: "zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication/sha256-6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "zero-knowledge-proofs/applications/blockchain-applications/sha256-6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "blockchain-systems"
  directions:
    - "applications"
    - "proof-systems"
  topics:
    - "blockchain-applications"
    - "privacy-preserving-blockchain-authentication"
    - "wallet-onboarding"
    - "tagged-witness-signatures"
    - "OpenID Connect"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "blockchain authentication"
  - "wallet onboarding"
  - "OpenID Connect"
  - "JWT"
  - "Groth16"
  - "Tagged Witness Signature"
  - "unlinkability"
  - "salt management"
  - "delegated proving"
aliases:
  - "zkLogin"
  - "keyless blockchain accounts"
  - "privacy-preserving social login wallet"
  - "Tagged Witness Signature"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "blockchain-applications"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "blockchain-systems"
  subdomain:
    - "applications"
    - "proof-systems"
  problem:
    - "private-key wallet onboarding friction"
    - "trusted oracle requirement for OAuth wallets"
    - "JWT payload privacy on public blockchains"
    - "off-chain identity to on-chain address unlinkability"
    - "resource-constrained ZKP generation"
  method_family:
    - "Tagged Witness Signature"
    - "nonce-bound ephemeral key"
    - "salted address derivation"
    - "Groth16 JWT proof"
    - "delegated ZKP generation"
    - "TEE or MPC salt service"
  system_layer:
    - "OpenID Provider"
    - "application frontend"
    - "salt service"
    - "ZK service"
    - "blockchain validators"
  evaluation_context:
    - "Sui production deployment"
    - "Groth16/circom circuit"
    - "AWS Nitro enclave salt service"
    - "rapid-snark ZK service"
    - "Sui validator testbed"
  application:
    - "wallet onboarding"
    - "privacy-preserving blockchain authentication"
    - "content credentials"
    - "claimable accounts"
  bridge:
    - "zk-SNARKs to privacy-preserving blockchain authentication"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-zklogin"
source_refs:
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "doi:10.1145/3658644.3690356"
  - "arxiv:2401.11735v2"
  - "pdf:~/Desktop/paper/zklogin.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "zero-knowledge-proofs -> applications"
secondary_directions:
  - "zero-knowledge-proofs -> proof-systems"
  - "blockchain-systems -> authentication/wallets"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Title, abstract and Section 1 identify privacy-preserving blockchain authentication with existing credentials"
  - "Sections 3-4 define Tagged Witness Signature and the zkLogin system"
  - "Section 5 documents production implementation and evaluation"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0025"
queue_status: "absorbed"
---

# zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials

## 论文身份

- 标题: zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials
- 作者: Foteini Baldimtsi, Konstantinos Kryptos Chalkias, Yan Ji, Jonas Lindstrom, Deepak Maram, Ben Riva, Arnab Roy, Mahdi Sedaghat, Joy Wang
- 机构: Mysten Labs; George Mason University; Cornell Tech; COSIC, KU Leuven
- 年份/Venue: ACM CCS 2024
- DOI: `10.1145/3658644.3690356`
- arXiv: `2401.11735v2`
- 本地 PDF: `~/Desktop/paper/zklogin.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/zklogin-privacy-preserving-blockchain-authentication-with-existing-credentials-6021df5c4aa2-pages.txt`
- SHA-256: `6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 20
- 已覆盖章节/页码: Abstract, Introduction, OIDC/JWT preliminaries, Tagged Witness Signature, zkLogin system, modes, security analysis, nonce-less extension, features, implementation/evaluation, related work, appendices
- Extraction gaps: 图表和公式由正文文字/图注覆盖；生产部署的 repository/transcript URL 没有单独联网复核。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p4 | 问题、方案、贡献 | 用 OpenID Connect/JWT 认证区块链交易；nonce 绑定 ephemeral key；salt 保护身份链接；提出 TWS | high |
| §2 / p4-p5 | 背景 | OpenID Connect, JWT header/payload/signature, RS256, JWK/key rotation | high |
| §3 / p5-p6 | 抽象原语 | Tagged Witness Signature: completeness, unforgeability, witness hiding | high |
| §4 / p6-p12 | 系统 | zkLogin model, address derivation, workflow, salt/ZKP delegation modes, security/unlinkability, nonce-less extension, features | high |
| §5 / p12-p14 | 实现评估 | Groth16/circom/R1CS, JWT validation/parsing circuit, salt service, ZK service, latency, validator overhead | high |
| §6-§7 / p14-p15 | 对比与结论 | OAuth wallets, ZK address abstraction, CanDID, Bonsai Pay, Aptos Keyless；总结依赖 OP auth 而非额外可信方 | medium-high |
| Appendix / p16-p20 | 形式证明与 ceremony | NIZK/SNARK definitions, TWS proofs, Groth16 ceremony, aud rationale, escaped quote risk | medium-high |

## 一句话贡献

zkLogin 将 OpenID Provider 签发的 JWT 作为隐藏 witness，让用户用已有 Web2 凭证生成可验证的区块链交易签名；它通过 nonce 绑定 ephemeral public key 和 expiry、salted address derivation 隐藏 off-chain/on-chain identity link，并用 Groth16 证明 JWT validity/address/key binding，从而在不引入额外 custody/oracle signing party 的情况下改善钱包 onboarding。

## 核心精读笔记

### 问题设定: 钱包密钥管理与 OAuth 直连的隐私问题

传统 non-custodial wallet 要求用户管理私钥、助记词或硬件钱包，容易丢失或使用门槛高。Custodial service 改善 UX，但把资产控制权交给平台，存在 mismanagement、hack 或 fraud 风险。

直接使用 OAuth/OIDC 看似自然: 用户用 Google/Apple/Facebook 等账户登录，然后把身份信息传给链上合约。但 public blockchain 不能直接作为 OAuth client，通常需要 trusted web server/oracle relay；而且若把 JWT payload 上链，会公开 email、name、sub、profile 等敏感 claims。zkLogin 的目标是: 复用现有 OpenID 认证，不引入额外可信 signing/custody party，并隐藏 off-chain identity 与 on-chain address 的链接。

### 核心机制: JWT 作为 witness，nonce 作为 ephemeral key certificate

zkLogin 的关键 trick 是在 OIDC nonce 中嵌入 ephemeral public key 和 expiry。用户/应用先生成 ephemeral key pair `(sk_u, vk_u)`，选择链上可理解的 expiry `Tmax`，采样随机数 `r`，设置:

`nonce = H(vk_u, Tmax, r)`

OpenID Provider 签发的 JWT 因此隐式证明“这个已认证用户同意把 `vk_u` 用作本 session 的临时签名 key”。zkLogin signature 包含:

- 一个 ZKP，证明存在 JWT、salt、nonce randomness，使 JWT 由 OP 签发，JWT 中 nonce 绑定 `vk_u/Tmax/r`，并且 `zkaddr = H(stid, aud, iss, salt)`。
- 一个传统签名 `Sig.Sign(sk_u, tx)`，授权具体交易。

这样单个 ZKP 可以在同一 session 内被多个交易复用，交易本身只需要 ephemeral private key 签名。ZK proof generation 可以被安全外包，因为 ZK service 不知道 `sk_u`，不能单独构造完整 zkLogin signature。

### 地址、salt 与 unlinkability

zkLogin address 由 stable identifier、app audience、issuer 和 salt 派生:

`zkaddr = H(stid, aud, iss, salt)`

`stid` 可以是 OIDC `sub`，也可以是 email/username/phone 等稳定唯一字段，但是否稳定依赖 provider。`aud` 必须进入地址，避免恶意 app 复用同一个 public `sub` 盗用用户资产，也避免不同 app context 下 subject collision。`iss` 标识 provider。

salt 是隐私关键。如果没有 salt 或公开 salt，地址可被 link 回 email/sub 等 off-chain identity；如果 salt 隐藏，则链上只能看到 issuer，无法把账户和具体身份绑定。salt 管理有两类路线:

- Salt service managed: service 用 seed `k_seed` 和 JWT claims 派生 salt。可用 TEE 或 MPC 隐藏 seed；也可以要求 JWT 之外的第二因素。
- User managed: 用户/设备本地保存 salt，降低 app 依赖，但要处理设备丢失、跨设备同步和备份。

论文明确区分 security 和 unlinkability: salt service 作恶通常不能偷资产，因为没有 ephemeral private key；但如果它看到 JWT 和 salt，就可能破坏 unlinkability。

### Tagged Witness Signature

论文提出 Tagged Witness Signature (TWS) 来形式化 zkLogin 的密码学核心。TWS 允许 signer 通过证明自己知道某个 tag 的 witness 来签名，而不是持有长期私钥。与 Signature of Knowledge 相比，TWS 强调 witness leakage 和 tag freshness: 即使旧 tag 的 witness 泄露，也不能为 fresh tag 伪造签名。

zkLogin 中:

- tag 包含 OP public key、issuer、zkaddr、expiry。
- witness 包含 JWT、salt、nonce randomness、ephemeral key pair。
- unforgeability 依赖 NIZK knowledge-soundness、JWT signature EUF-CMA、ephemeral signature EUF-CMA 和 hash collision resistance。
- witness hiding 依赖 NIZK zero-knowledge。

### 系统工作流

zkLogin 的四个主要实体是 OpenID Provider、User、Application 和 Blockchain。论文假设 app backend 不可信、frontend 可信；OP 是信任根，但不是 custodian，且无需知道 zkLogin 存在。

工作流:

1. Get JWT: app/frontend 生成 ephemeral key 和 nonce，用户通过 OP 登录，获得 JWT。
2. Get Salt: 从 salt service 获取或本地读取 salt。
3. Compute ZKP: 证明 JWT validity、address derivation、nonce/key/expiry binding。
4. Submit Transaction: 用 `sk_u` 签交易，提交 `(vk_u, Tmax, sig_u, proof)`；validators 验证 proof、OP JWK/current key、ephemeral signature 和 expiry bound。

区块链需要支持 on-chain/off-chain verifier 逻辑、JWK oracle 或等价机制来跟踪 OP public keys。验证还要限制 `Tmax < Tcur + delta`，防止 app 设置过长有效期。

### Salt service 与 ZKP service 模式

Salt service choices:

- Plaintext: UX 简单，但 service 可关联身份与地址，也能看到 JWT。
- Enclave: TEE/Nitro/SGX 保护 salt seed，可隐藏 salt 和 JWT，但存在 side-channel 风险。
- Plain MPC: seed secret-shared，少于阈值的节点不能恢复 salt；但单个节点仍可能看到用户 JWT。
- MPC with ZK and secret-shared stable ID: 用户生成多个 ZKP，节点只处理 secret shares，隐私更强但成本更高。

ZKP generation choices:

- Local ZKP generation: 隐私最好，但移动端/浏览器上可能慢或崩溃。
- Normal delegation: 把 JWT 和 salt 给 ZK service 生成 proof。安全仍成立，因为 service 没有 `sk_u`；但 service 可破坏 unlinkability。
- Full-private delegation: 用 MPC/TEE 隐藏 witness，保护 ZK service 侧隐私，代价更高。

### 安全与隐私边界

论文给出四个定理:

- TWS unforgeability: 依赖 proof knowledge-soundness、JWT/Sig EUF-CMA、hash collision resistance。
- TWS witness hiding: 依赖 proof zero-knowledge。
- zkLogin security: 从 TWS unforgeability 归约得到。
- zkLogin unlinkability: 从 TWS witness hiding 和 `zkaddr` 作为隐藏 commitment 得到。

关键边界:

- App: 影响 liveness，不应能偷资产；若 app 停止服务，用户资产可能锁住。可用多 app multisig 降低风险。
- Salt service: 作恶不破坏交易 unforgeability，但会影响 unlinkability。
- OP: 如果仅凭 JWT 就能从 salt service 取 salt，恶意 OP 可签发 JWT 并破坏安全；更高安全要求 user-managed salt 或第二因素。
- Blockchain: 链上可见 issuer 和 zkLogin signatures，但不应看到 JWT 其他敏感 claims。
- Timing side channel: OP 可能通过登录时间和链上交易时间做不完美关联；可用预取 JWT/ZKP 和 proof reuse 缓解。

### Nonce-less providers

如果某些 provider 不支持 nonce，论文提出 nonce-less adaptation: 直接 hash JWT、ephemeral key 和 timestamp，并用 ZKP 证明 hash/JWT/signature/address 一致。这个方案灵活性和安全性更弱，因为 fresh JWT 若给到 ZK service，service 可能自己签交易；因此 nonce-less 方案只适合本地 proof generation。作者把更安全/更友好的 nonce-less 支持留作未来工作。

### 新功能: discoverability、partial reveal、anonymous accounts、claimability

zkLogin 支持几类传统钱包不容易实现的功能:

- Discoverability: 用户主动公开 stable ID、aud 和 salt，证明某链上账户属于某邮箱/用户名，适合公开内容凭证或透明身份。
- Partial reveal: 只公开 stable ID 的一部分，例如 email domain，证明组织归属而不公开个人身份。
- Anonymous blockchain accounts: 地址由某个 email domain/TLD 或明确 anonymity set 派生，用户证明自己属于集合。
- Claimability: 在接收方还没有链上账户前，发送方可用接收方 email 和 salt 派生地址并发送资产；salt 通过私人渠道给接收方。

### 实现与部署

zkLogin 使用 Groth16 和 circom 实现，电路约 1.1M constraints。由于 Groth16 需要 circuit-specific trusted setup，团队组织了超过 100 名外部贡献者参与的 ceremony，并使用 Perpetual Powers of Tau phase 1、Drand random beacon 和可验证 transcript。

电路主要包含两部分:

- JWT validation: RS256 = SHA-256 + RSA PKCS#1 v1.5 verification。SHA-2 约 750k constraints，占 66%；RSA bigint operations 约 155k，占 14%。
- JWT parsing: 约 235k constraints，占 20%。不是完整 JSON parser，而是 selective parsing top-level key-value claims，如 stable ID、nonce、aud、email_verified。Base64 decoding 和 slicing 是主要成本。

重要优化:

- Header 作为 public input，不在电路内 Base64 decode，因为 header 不包含敏感/linkable claims。
- Payload 完整 Base64 decode 后只解析必要 top-level claims。
- Slicing 中把 8-bit characters pack 成 128-bit field elements，再做 slicing，约 4.8x reduction per slice，整体 slicing constraints 降低超过一个数量级。

### 评估

部署/评估配置:

- Salt service: AWS Nitro enclave on m5.xlarge，平均 salt retrieval latency 0.2s。
- ZK service: rapid-snark on Google Cloud n2d-standard-16，16 vCPU/64GB RAM。
- Witness calculator: 550.05 +/- 22.42ms。
- Groth16 proof generation: 2.1 +/- 0.15s。
- End-to-end ZKP service latency: 2.78 +/- 0.25s over 300 runs。
- End-user first transaction confirmation: 3.52 +/- 0.36s，包括 salt/ZKP/sign/confirmation，不包括 Google sign-in pop-up。
- Traditional signature confirmation: 120.74 +/- 5.32ms。
- zkLogin signature verification: 2.04ms on Apple M1 Pro；Ed25519 verification 56.3 microseconds。
- zkLogin signature size: about 1300 bytes Base64，约比 EdDSA signature 大一个数量级。
- 8 validator testbed, 1000 TPS load: EdDSA 约 850 TPS，zkLogin 约 750 TPS，约 11% decrease。

论文指出，第一笔交易额外数秒可通过 session proof reuse 和后台预取隐藏；同一 session 的后续交易接近传统签名体验。

### 相关工作定位

与 OAuth wallets / MPC wallets 相比，zkLogin 不让 app/MPC wallet service 持有直接签名能力；app 主要影响 liveness，不应影响 security。与 ZK Address Abstraction 相比，zkLogin 不把交易本身绑进 proof，因此单 proof 可复用多笔交易；同时不要求 provider 使用 ZK-friendly EdDSA，而是支持广泛使用的 RS256 JWT。与 CanDID 相比，zkLogin 不引入额外 MPC committee 来 port credentials，但只支持包含签名的 credential，如 OIDC JWT。与 Bonsai Pay/Aptos Keyless 相比，论文强调 proof latency、stable identifier privacy 和中心化/恢复应用风险的差异。

## 可复用知识与来源内边界

### 可上升为 knowledge/source-extension 的内容

- Privacy-preserving blockchain authentication: 用现有身份凭证认证链上交易，同时隐藏身份链接。
- Keyless/social-login wallet onboarding: 改善 UX，但必须区分 custody/security/liveness/privacy。
- Tagged Witness Signature: 用短期 witness 和 tag freshness 抽象 JWT-based signing。
- Salted address derivation: 用 `H(stid, aud, iss, salt)` 建立可选 discoverability/unlinkability。
- Delegated ZKP generation boundary: proof service 可不影响安全，但可能影响 unlinkability。

### 不应上升为独立基础概念的内容

- `zkLogin` 是 source/system instance，不是上层概念节点。
- Sui 部署、AWS Nitro、rapid-snark、1.1M constraints、3.52s latency 是 source evidence，不是普适结论。
- TWS 当前只有本 source 直接支撑；先作为 source-contained primitive 和应用节点的方法族，不单独拆 foundation node。
- OpenID Connect/JWT 在本 source note 中足够解释；若后续需要 Web identity foundation，再单独补基础概念 source。

## 分层吸收映射

| Knowledge/Bridge target | 更新方式 | 吸收内容 | Source boundary |
| --- | --- | --- | --- |
| [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] | new problem node | 钱包 onboarding、JWT witness、salt unlinkability、delegated proving security/privacy boundary | 不复制全部电路/部署细节 |
| [[blockchain-applications|ZKP blockchain applications]] | child + source extension | 新增 blockchain authentication/keyless account 应用路线 | 不把 zkLogin 当作所有身份系统综述 |
| [[applications|ZKP applications]] | source extension | ZK 用于身份凭证隐私和链上认证 | 不升级 proof-system foundation |
| [[zk-snarks|zk-SNARKs]] | bridge evidence only | Groth16 用作 practical verifier-friendly proof | 不把 zkLogin 当 zk-SNARK 定义来源 |
| [[zk-snarks-to-privacy-preserving-blockchain-authentication|zk-SNARKs -> privacy-preserving blockchain authentication]] | new bridge | 连接 proof-system hiding/succinctness 与 wallet/authentication system goals | OP trust、salt management、JWK oracle 和 liveness 不由 SNARK 自动提供 |

## 关键术语表

| Term | 本文含义 | 上层去向 |
| --- | --- | --- |
| OpenID Provider (OP) | 签发 JWT 的身份平台，如 Google/Apple/Facebook | source detail; identity dependency |
| JWT | OP 签名的 ID token，作为 zkLogin witness | source detail |
| stable identifier | JWT 中稳定唯一标识，如 sub/email | [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] |
| salt | 隐藏 stable identifier 与 zkaddr 链接的随机性 | [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] |
| ephemeral key pair | session-level transaction signing key, nonce-bound by JWT | [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]] |
| Tagged Witness Signature | 用 tag/witness freshness 抽象 JWT-based signatures | source-contained primitive |
| ZK service | 可外包 proof generation 的服务；安全与隐私边界不同 | source detail; method boundary |

## 关系与链接

- Primary: [[privacy-preserving-blockchain-authentication|Privacy-preserving blockchain authentication]]
- Parent: [[blockchain-applications|ZKP blockchain applications]] -> [[applications|ZKP applications]] -> [[zero-knowledge-proofs|Zero-knowledge proofs]]
- Dependency: [[zk-snarks|zk-SNARKs]]
- Bridge: [[zk-snarks-to-privacy-preserving-blockchain-authentication|zk-SNARKs -> privacy-preserving blockchain authentication]]
- Nearby sources: [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]], [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross: A Novel Architecture for Cross-Chain Privacy-Preserving Auditing]]

## 质量复核

- 完整性: 覆盖 problem, cryptographic primitive, system workflow, modes, security/privacy boundary, implementation, evaluation, related work and ceremony appendix。
- 分层性: source note 保留 JWT parsing/RSA/TEE/benchmark 细节；knowledge nodes 只吸收 wallet authentication 问题和方法族。
- 概念边界: zkLogin 不拆成 concept；TWS 暂不拆 foundation node；privacy-preserving blockchain authentication 作为应用问题节点。
- 风险: 生产部署和性能数字受 Sui、Groth16/circom、云服务配置和 2024 工具链影响；不可作为当前通用性能结论。
