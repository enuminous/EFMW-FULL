# EFMW

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/EFMW-FULL) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#core-efmw-and-review)

<details open>
<summary><strong>On this page</strong></summary>

- [Current status](#current-status)
- [Scientific rule](#scientific-rule)
- [Repository map](#repository-map)
- [Install](#install)
- [License](#license)
- [Disclaimer](#disclaimer)


</details>

**Related repositories:** [EFMW-EXP-001](https://github.com/enuminous/EFMW-EXP-001) · [EFMW](https://github.com/enuminous/EFMW) · [EFMW-Safety-001](https://github.com/enuminous/EFMW-Safety-001) · [EFMW-Axioms](https://github.com/enuminous/EFMW-Axioms) · [papers](https://github.com/enuminous/papers)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


> **Reviewer status (2026-10-21):** This repository retains historical EXP-001 material; it is **not** a second independent frozen-run replication. Start with the [portfolio claims register](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/CLAIMS_EVIDENCE_REGISTER.md) and the [frozen-run reconciliation](https://github.com/enuminous/EFMW-EXP-001/blob/main/CONFIRMATORY_RECONCILIATION.md). Compare dated experiment states before quoting older "passed"/"not executed" wording.


<!-- ENUMINOUS-LIFECYCLE:START -->
**Lifecycle review — 2026-10-16: historical EXP-001 result entry point; duplicated layouts.**

Use [the current frozen-run reconciliation](https://github.com/enuminous/EFMW-EXP-001/blob/65134993069c2dc0c46a60fccd8bcdb2d951cdd3/CONFIRMATORY_RECONCILIATION.md) for the reproducible EXP-001 protocol, per-seed data and qualified conclusions. The result preserved here records execution of a transcribed specification when the original frozen ZIP was unavailable; it is not another independent frozen-artifact replication. The reproduction to-do below predates the published frozen-run reproduction; external independent replication remains a separate evidentiary claim. Four substantive Python files also occur in both flat and package/test paths (`metrics.py`, `monitors.py`, `simulator.py`, `test_core.py`); these are copies of the same implementation. The synthetic benchmark result does not establish general EFMW physics or deployment efficacy.

[Portfolio review and evidence](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/REPOSITORY_LIFECYCLE_2026-10-16.md).
<!-- ENUMINOUS-LIFECYCLE:END -->

**EFMW — Einstein–Feynman–Maxwell–Wright experimental framework**

This repository is the public experimental home for EFMW. Its purpose is to separate theory from experiment, calibration from confirmation, and bounded positive results from broader unverified claims.

## Current status

**EFMW-EXP-001-v1.0** tested an EFMW-style recursive coherence monitor on a synthetic partially observed control benchmark.

Frozen primary criterion:

> median paired warning-lead gain >= 10 timesteps over the conventional residual-EWMA baseline.

Held-out confirmatory execution on seeds 1001–1040 reported:

- median baseline lead: 59.0 timesteps
- median EFMW lead: 78.0 timesteps
- median paired gain: 16.5 timesteps
- EFMW win rate: 0.75
- Wilcoxon p-value: 0.003923
- median compute ratio: 1.117

The primary frozen endpoint **passed**.

This supports the bounded EXP-001 monitoring claim on the frozen synthetic benchmark. It does **not** establish EFMW physics generally.

## Scientific rule

> **EFMW receives no credit for explaining a result it did not predict.**

## Repository map

- `docs/` — conceptual and experimental documentation
- `src/efmw/` — reference implementation
- `tests/` — deterministic tests
- `experiments/EXP-001/frozen/` — frozen experiment
- `experiments/EXP-001/results/` — confirmatory result record
- `experiments/EXP-001/audit/` — audit and transport notes
- `schemas/` — machine-readable schemas

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## License

Code: MIT. Documentation: CC BY 4.0 unless otherwise noted.

## Disclaimer

Broader EFMW claims remain unverified unless separately tested.
