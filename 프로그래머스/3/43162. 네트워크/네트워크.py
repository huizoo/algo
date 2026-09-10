def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    
    for i in range(n):
        if visited[i] == 1: continue
        answer += 1
        stack = [i]
        visited[i] = 1
        while stack:
            par = stack.pop()
            for j in range(n):
                if par == j or \
                visited[j] == 1 or \
                computers[par][j] == 0: continue
                visited[j] = 1
                stack.append(j)
    
    return answer