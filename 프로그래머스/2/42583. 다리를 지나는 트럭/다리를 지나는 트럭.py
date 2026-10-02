from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque() # (시간, 무게)
    n = len(truck_weights)
    max_time = bridge_length * n + 1
    idx = 0
    
    for time in range(1, max_time + 1):
        if q and time - q[0][0] >= bridge_length:
            q.popleft()
        if sum(q[i][1] for i in range(len(q))) + truck_weights[idx] <= weight:
            q.append((time, truck_weights[idx]))
            idx += 1
        
        if idx == n:
            answer = time + bridge_length
            break
            
    return answer