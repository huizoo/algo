from collections import Counter

def solution(k, tangerine):
    answer = 0
    table = Counter(tangerine)
    cnt = 0
    for t, c in sorted(table.items(), key=lambda x: -x[1]):
        if cnt + c > k:
            answer += 1
            cnt = k
            break
        elif cnt + c == k:
            answer += 1
            cnt += c
            break
        else:
            answer += 1
            cnt += c
    return answer