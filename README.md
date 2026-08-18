# Cortex V6 decision-lineage pack

> **CURRENT STATUS — STAGED / QUARANTINED, NOT ACTIVE FOSSIL INGESTION**
>
> The original initial pack was built through FOSSIL contracts. The later 2026-08-18 fresh-audit append did **not** go through the real FOSSIL durable-event path and adversarial validation found all nine newly appended event IDs violate FOSSIL deterministic event identity. See `ingestion/2026-08-18-fresh-audit-validation-failure.md` and issue #1.
>
> Do not treat the fresh-audit event files or the previous human `CURRENT` labels as proof that active DICS/Graphiti contains those claims. They are durable staged evidence awaiting rebuild, validation, authorization, commit, and—where applicable—projection/rebuild proof.

This dedicated project pack records the architecture decision trail for Cortex V6 and its boundary with FOSSIL. It is deliberately separate from `fossil-ai-systems`: V6 is the project whose decisions are being recorded, while FOSSIL remains the durable knowledge/evidence subsystem described by those decisions.

`manifest.json` is authoritative about placement status: this is a staged project pack, not an upstream FOSSIL write.

## Current resume point

The original 2026-08-17/18 plan remains preserved as historical evidence. A fresh-session audit on 2026-08-18 challenged parts of that plan, and a subsequent adversarial campaign in `Pukujan/Cortex-v6#25` found additional blockers/issues #34–#41 plus the FOSSIL ingestion defect.

Therefore the earlier fresh-audit decision graph is **not the final current plan**. The intended lineage is now:

```text
original long-session plan
  -> fresh-session audit proposal
  -> adversarial challenges / counterexamples
  -> blind independent critic + adjudication
  -> canonical current V6 plan
  -> real FOSSIL-validated events / promotion receipt
```

Start with:

1. `ingestion/2026-08-18-fresh-audit-validation-failure.md` — why the fresh append is quarantined.
2. `Pukujan/fossil-cortex-v6#1` — real rebuild/validate/commit/promotion gate.
3. `Pukujan/Cortex-v6#25` — current adversarial pre-implementation gate.
4. `Pukujan/Cortex-v6#34`–`#41` — second-round architectural/safety/evaluation findings.
5. `docs/DECISION_LINEAGE.md` — human-readable lineage/status; historical proposal positions are preserved but not promoted merely because they exist.

## Evidence handling

The public ChatGPT share page remains represented only as a reconstructed checkpoint. The original locked V6 plan, Issue #9, and PRs #20–#24 were captured separately as primary source snapshots.

The later fresh-audit staging added version-pinned artifacts for:

- the fresh V6 plan audit;
- the corrected OpenCode bootstrap execution contract;
- the canonical V6/OpenCode 600-second exact-model transport target.

Those source artifacts remain useful evidence. The defect is in treating manually appended event JSON as if it had passed the FOSSIL event-store boundary. Source evidence and durable knowledge promotion are distinct.

## Scope note

This repository does not change FOSSIL core contracts merely by staging Cortex V6 decisions. FOSSIL availability is also not a Cortex V6 runtime correctness dependency. For this project campaign, the owner may choose successful FOSSIL promotion as a continuity/governance gate before high-cost implementation, while the canonical project plan must independently remain durable in protected GitHub.
