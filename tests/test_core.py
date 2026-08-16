import numpy as np
from efmw import simulate,residuals,baseline_score,efmw_score

def test_deterministic(): assert simulate(1001)==simulate(1001)
def test_failure_offset():
    rows=simulate(1001); assert rows[0][6]-rows[0][5]==120
def test_monitor_shapes():
    rows=simulate(1001); y=np.array([r[2] for r in rows]); u=np.array([r[3] for r in rows])
    assert residuals(y,u).shape==y.shape
    assert baseline_score(y,u).shape==y.shape
    assert efmw_score(y,u).shape==y.shape
def test_scores_nonnegative():
    rows=simulate(1001); y=np.array([r[2] for r in rows]); u=np.array([r[3] for r in rows])
    assert np.all(baseline_score(y,u)>=0); assert np.all(efmw_score(y,u)>=0)
