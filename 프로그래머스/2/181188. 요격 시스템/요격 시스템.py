def solution(targets):
    answer = 0
    targets.sort()
    start = end = 0
    for s, e in targets:
        if end <= s:
            answer += 1
            start = s
            end = e
        elif e < end:
            end = e
    return answer