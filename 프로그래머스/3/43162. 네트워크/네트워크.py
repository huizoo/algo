def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    for i in range(n):
        if visited[i]: continue
        visited[i] = 1
        answer += 1
        stack = [i]
        while stack:
            now = stack.pop()
            for j, v in enumerate(computers[now]):
                if visited[j]: continue
                if not v: continue
                visited[j] = 1
                stack.append(j)
                
    return answer