import numpy as np
N_STEPS=500
DEGRADATION_LEN=120
ONSET_LOW=140
ONSET_HIGH=200

def simulate(seed:int, null_degradation:bool=False, reverse_bias:bool=False):
    rng=np.random.default_rng(seed)
    onset=int(rng.integers(ONSET_LOW,ONSET_HIGH))
    failure=onset+DEGRADATION_LEN
    x=0.0
    out=[]
    for t in range(N_STEPS):
        d=0.0 if null_degradation else float(np.clip((t-onset)/DEGRADATION_LEN,0,1.25))
        u=-0.45*x
        a=0.82+0.08*d
        process_noise=rng.normal(0,0.035)
        bias=(-0.05 if reverse_bias else 0.05)*d
        x=a*x+u+process_noise+bias+0.012*d*np.sin(0.18*t)
        y=x+rng.normal(0,0.02)
        out.append((seed,t,y,u,d,onset,failure,int(t>=failure)))
    return out
