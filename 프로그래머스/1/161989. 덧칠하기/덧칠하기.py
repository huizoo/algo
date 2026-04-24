def solution(n, m, section):
    answer = 0
    idx = 0
    N = len(section)
    while idx < N :
        start = section[idx]
        while start <= section[idx] < start + m:
            idx += 1
            if idx >= N:
                break
        answer += 1
    return answer