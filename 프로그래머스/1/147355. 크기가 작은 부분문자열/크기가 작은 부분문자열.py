def solution(t, p):
    answer = 0
    lt, lp = len(t), len(p)
    for i in range(lt-lp+1):
        if t[i:i+lp] <= p:
            answer += 1
    return answer