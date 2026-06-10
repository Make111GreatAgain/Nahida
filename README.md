# Nahida

Nahida is an AI-native Obsidian knowledge-base protocol.

It is not primarily an application. The core deliverable is a vault structure plus Codex skills that let AI agents read, write, retrieve, audit, and maintain knowledge safely.

## What This Repository Contains

- `vault/` - an Obsidian-compatible Nahida vault template.
- `vault/00_System/NAHIDA_SPEC.md` - the operating contract every agent should read before writing.
- `vault/00_System/schemas/` - note type schemas for managed notes.
- `vault/00_System/templates/` - starter templates for source, claim, concept, map, and review notes.
- `skills/` - Codex skill definitions using the `nahida-*` prefix.
- `docs/` - planning notes and implementation guidance.
- `examples/` - small examples of expected Nahida outputs.

## Phase 1 Scope

Phase 1 is deliberately small:

1. Create the vault skeleton and system spec.
2. Define source, claim, concept, bridge, map, project, run, and review queue schemas.
3. Define skill contracts.
4. Import one source manually through the Nahida protocol.
5. Trace one claim back to one source.
6. Update one map.
7. Produce one audit report.

No production automation code is required for Phase 1.
