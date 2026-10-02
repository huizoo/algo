def solution(citations):
    answer = 0
    l = len(citations)
    for i, v in enumerate(sorted(citations)):
        if l - i <= v:
            answer = l - i
            break
    return answer