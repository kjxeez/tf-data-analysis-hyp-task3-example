import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 584664949 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.04
    p_val = ztest(x, value=500, alternative='smaller')[1]  # larger

    return p_val < alpha
