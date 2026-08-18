# Cortex V6 decision-lineage pack

This dedicated project pack records the architecture decision trail for Cortex V6 and its boundary with FOSSIL. It is deliberately separate from `fossil-ai-systems`: V6 is the project whose decisions are being recorded, while FOSSIL remains the durable knowledge/evidence subsystem described by those decisions.

## Current resume point

The original 2026-08-17/18 plan is preserved as history. A fresh-session audit on 2026-08-18 partially superseded its **implementation-specific future architecture** while preserving the stable kernel/ownership invariants and the #2 → #3 → #4/#7 floor.

Start with:

1. `docs/DECISION_LINEAGE.md` — human-readable current decision tree and supersession state.
2. `lineages/lin_cortex_v6_fresh_session_audit_20260818.json` — machine-readable fresh-audit decision graph.
3. `Pukujan/Cortex-v6#25` and child issues #26–#33 — current re-baselining work.
4. The pinned primary artifacts/snapshots in this pack for the fresh audit, OpenCode bootstrap contract, and LiteLLM 600-second exact-model target.

The current near-term rule is **do not start by implementing #10**. First integrate and qualify the minimal kernel, run the independent qualification/value gates, then qualify the external bootstrap lane and only add later abstractions one at a time.

## Evidence handling

The public ChatGPT share page remains represented only as a reconstructed checkpoint. The original locked V6 plan, Issue #9, and PRs #20–#24 were captured separately as primary source snapshots.

The fresh-session re-baseline adds new primary, version-pinned artifacts rather than rewriting those original records:

- fresh V6 plan audit;
- corrected OpenCode bootstrap execution contract;
- canonical V6/OpenCode 600-second exact-model transport target.

Append-only claim events capture the new positions and the decision lineage records which older positions are preserved, superseded in part, current, or unresolved.

`docs/DECISION_LINEAGE.md` is the human-readable view; immutable artifacts, snapshots, conversations, lineage, and events are the durable record.

## Scope note

This repository is a dedicated Cortex V6 project decision-lineage pack. It does not change the FOSSIL core schema/storage/ingestion contracts merely by recording V6 decisions; any future FOSSIL-core change still requires its own evidence and decision.