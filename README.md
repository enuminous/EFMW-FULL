# EFMW

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/EFMW-FULL) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
