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
        while g < LCM:
            for i in range(g, g+y):
                YELLOW[i] += 1
            g += length
            
    N = len(signals)
    return (1 + YELLOW.index(N)) if N in YELLOW else -1