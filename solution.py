import pandas as pd
import numpy as np
from scipy import stats

chat_id = 584664949 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.04
    mu = 500
    N = len(x)
    X = np.mean(x)
    s = np.std(x)
    T = (X - mu) / (s / np.sqrt(N))
    t_crit = stats.t.ppf(1 - alpha, N - 1)
    return T > t_crit
