from math import gcd

def solution(signals):
    LCM = 1
    L = []
    for signal in signals:
        l = sum(signal)
        LCM = LCM*l // gcd(LCM, l)
        L.append(l)
    
    YELLOW = [0]*LCM
    for i, (g, y, r) in enumerate(signals):
        y_idx = g
        length = L[i]
        while y_idx < LCM:
            for j in range(y_idx, y_idx+y):
                YELLOW[j] += 1
            y_idx += length
            
    N = len(signals)
    return (1 + YELLOW.index(N)) if N in YELLOW else -1