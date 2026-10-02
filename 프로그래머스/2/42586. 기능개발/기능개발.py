from math import ceil

def solution(progresses, speeds):
    answer = []
    today = 0
    for p, s in zip(progresses, speeds):
        day = ceil((100-p)/s)
        if today < day:
            today = day
            answer.append(1)
        else:
            answer[-1] += 1
        
    return answer