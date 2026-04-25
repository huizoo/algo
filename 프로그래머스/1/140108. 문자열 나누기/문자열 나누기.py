def solution(s):
    answer = 0
    x = None
    cnt = 0
    for i, v in enumerate(s):
        if cnt == 0:
            answer += 1
            x = v
            cnt += 1
        elif x == v:
            cnt += 1
        else:
            cnt -= 1
    
    return answer