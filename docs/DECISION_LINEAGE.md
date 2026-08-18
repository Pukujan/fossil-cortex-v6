# Cortex V6 / FOSSIL decision lineage

Pack: `pack_a4b5515c4c6a4f38ac433e04b03ab406`

> **STATUS: STAGED / QUARANTINED.**
>
> This file is a human-readable project-pack view, not proof of active FOSSIL state. The initial pack was built through FOSSIL contracts, but the later fresh-audit append bypassed the executable `DurableEventStore` path. Mechanical adversarial validation found all nine newly appended fresh-audit event IDs conflict with FOSSIL deterministic identity and would be rejected by real ingestion.
>
> See `../ingestion/2026-08-18-fresh-audit-validation-failure.md` and repository issue #1. Until that issue closes with real validation/authorization/commit evidence, do **not** treat the fresh/adversarial claims as active DICS/Graphiti knowledge or `CURRENT_BEST`.

## What remains trustworthy as evidence

The repository still preserves useful immutable/project evidence:

- the reconstructed public shared-chat checkpoint, explicitly labeled reconstructed;
- pinned original locked-plan / Issue #9 / PR #20–#24 source snapshots from the initial builder;
- pinned later source artifacts for the fresh audit, OpenCode runbook, and LiteLLM timeout contract.

Source preservation is not the same as knowledge promotion. The invalid fresh event append remains in Git history/files as a rejected staging attempt until rebuilt through FOSSIL contracts.

## Intellectual history — not yet final adjudication

```text
Original long-session V6 plan
  |
  v
Fresh-session audit proposal
  - preserved minimal #2 -> #3 -> #4/#7 research floor
  - challenged Microsoft/AWS layer assumptions
  - moved value gates earlier
  - added OpenCode/LiteLLM/data-egress qualifications
  |
  v
Second adversarial campaign (Cortex-v6 #25)
  - verified main branch protection is absent (#8)
  - found missing durable lifecycle/recovery semantics (#34)
  - found missing immutable project-snapshot fencing (#35)
  - separated authority-grant issuance from scope enforcement (#36)
  - separated logical verification from trust-root/OS isolation (#37)
  - found CI/toolchain provenance gaps (#38)
  - found benchmark tuning/holdout leakage risk (#39)
  - found canonical-current-plan/readiness ambiguity (#40)
  - requires blind independent red-team/adjudication (#41)
  - confirmed the fresh FOSSIL append itself fails deterministic event identity
  |
  v
NEXT: independent critic + adjudication + mechanical verification
  |
  v
Canonical CURRENT PLAN in protected Cortex-v6 GitHub
  |
  v
FOSSIL-backed rebuild / propose / validate / authorize / commit
  |
  v
Only then compute/promote current knowledge positions
```

## Stable candidate invariants that have survived both audit rounds

These remain **candidate current positions supported by primary project evidence**, but this staging repository does not itself promote them into active FOSSIL:

1. Project/human decisions own current project truth and acceptance meaning.
2. Cortex should own only portable authoritative control semantics it can justify: exact work identity, authority, evidence admission, and lifecycle transitions.
3. Model/runtime/FOSSIL/assurance outputs cannot directly declare Cortex work complete.
4. Transcript/model assertions are not authoritative task truth.
5. V5/SCC are donors/oracles/failure corpora rather than runtime inheritance trees.
6. FOSSIL owns durable knowledge/provenance/lineage, not active Cortex lifecycle state.
7. GitHub/CI should be an independent merge boundary—but current branch enforcement must actually be enabled before that is a factual operational claim.
8. Added Cortex mechanism must beat a serious simpler baseline or be narrowed/removed.
9. The #2 -> #3 -> #4/#7 sequence remains a useful **research/composition** floor, not evidence of production readiness.

## Positions explicitly reopened / under challenge

- Microsoft Agent Framework vs AWS AgentCore is not one peer runtime-substitution axis; application framework and hosting/runtime are separate dimensions.
- A generic `AgentRuntime` abstraction is not automatically justified.
- `AssurancePlan`/provider abstractions must earn themselves against direct simpler assurance.
- Fixed role/topology ontologies are not settled.
- project-only/FOSSIL-only/hybrid context remains an experiment.
- 3 probe / 30 normal retries remains a hypothesis with cumulative-budget/failure-taxonomy requirements.
- OpenCode is a replaceable bootstrap engineering shell candidate, not a Cortex dependency or sandbox.
- Different model vendors do not imply full independence when transport/context/runtime/oracle/controller are shared.
- The fresh-audit execution order is superseded by the second adversarial campaign and must not be promoted as current.

## Current external gates

### Cortex-v6

Primary audit/governance source: `Pukujan/Cortex-v6#25`.

Important current blockers include #8 and #26–#41. Issue #40 will eventually publish one concise canonical current plan/readiness ladder to protected `main`. Issue #41 requires a blind independent critic/adjudication pass before START.

### LiteLLM/OpenCode

`Pukujan/litellm-ckff-ops#24` tracks implementation of the 600-second exact-model/no-hidden-cross-model-fallback transport target. Cortex #30/#33/#37 govern egress, bootstrap-shell qualification, and lower-layer isolation.

### FOSSIL

`Pukujan/fossil-cortex-v6#1` is the only current authority for whether this staged fresh/adversarial decision material has passed real FOSSIL ingestion. It has not yet passed.

## FOSSIL promotion rule

Do not hand-edit invalid events into apparent correctness. Rebuild/adjoin the final adjudicated plan through the same FOSSIL stores/contracts used by the original pack builder:

- content-addressed artifacts;
- source snapshots/citations from actual bytes;
- deterministic durable event identities from pack + idempotency key;
- JSON Schema and semantic validation;
- pack write authorization;
- immutable commit/idempotency;
- projection/rebuild evidence when a projection is used;
- explicit claim/challenge/support/supersession history.

The previous fresh audit should remain a proposal in the intellectual history, with adversarial challenges and final adjudication represented as later events rather than rewriting the past.

## Resume rule

A new session should start with:

1. `Pukujan/Cortex-v6#25` and #34–#41;
2. `Pukujan/fossil-cortex-v6#1` plus the validation-failure report;
3. current GitHub branch/PR/ruleset state;
4. only then historical locked/fresh-audit artifacts as lineage context.

If a historical file says `CURRENT` but conflicts with the current GitHub audit/issues or this quarantine status, treat it as historical staging until real FOSSIL adjudication/commit says otherwise.
