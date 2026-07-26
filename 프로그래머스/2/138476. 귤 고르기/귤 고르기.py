from collections import Counter

def solution(k, tangerine):
    answer = 0
    for idx, cnt in enumerate(sorted(Counter(tangerine).values(), reverse=True), start=1):
        if (k:=k-cnt) <= 0:
            answer = idx
            break
    return answer