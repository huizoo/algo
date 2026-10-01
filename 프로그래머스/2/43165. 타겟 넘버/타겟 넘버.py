from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([1, numbers[0]])
    q.append([1, -numbers[0]])
    
    while q:
        idx, val = q.popleft()
        if idx >= n:
            if val == target:
                answer += 1
            continue
        q.append([idx+1, val+numbers[idx]])
        q.append([idx+1, val-numbers[idx]])
    
    return answer