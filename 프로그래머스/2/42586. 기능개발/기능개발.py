def solution(progresses, speeds):
    answer = []
    today = 0
    for p, s in zip(progresses, speeds):
        day = 1
        while p + s < 100:
            p += s
            day += 1
        if today < day:
            today = day
            answer.append(1)
        else:
            answer[-1] += 1
        
    return answer