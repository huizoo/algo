def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    end = 0
    for s, e in targets:
        if end <= s:
            answer += 1
            end = e
    return answer