import numpy as np
def lead_time(failure_time,detection_time): return -999 if detection_time is None else failure_time-detection_time
def paired_gain(efmw_lead,baseline_lead): return efmw_lead-baseline_lead
def raw_fpr(score,threshold,warmup,onset): return float(np.mean(np.asarray(score)[warmup:onset]>threshold))
