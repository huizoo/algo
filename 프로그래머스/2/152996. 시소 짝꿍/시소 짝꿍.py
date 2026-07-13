from collections import Counter
from math import comb

def is_balanced(a, b):
    if a*2 == b:
        return True
    if a*3 == 2*b:
        return True
    if a*4 == 3*b:
        return True
    return False

def solution(weights):
    answer = 0
    dic = Counter(weights)
    for w, cnt in dic.items():
        for w2, cnt2 in dic.items():
            if w == w2:
                answer += comb(cnt, 2)
            elif is_balanced(w, w2):
                answer += cnt*cnt2
    return answer