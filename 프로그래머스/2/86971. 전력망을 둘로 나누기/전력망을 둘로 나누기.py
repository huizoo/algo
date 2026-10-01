def solution(n, wires):
    answer = n - 1
    
    arr = [[] for _ in range(n+1)]
    for u, v in wires:
        arr[u].append(v)
        arr[v].append(u)
    
    for i, (w1, w2) in enumerate(wires):
        cnt = 1
        stack = [w1]
        visited = [0]*(n+1)
        visited[w1] = 1
        while stack:
            now = stack.pop()
            for nxt in arr[now]:
                if nxt == w2: continue
                if visited[nxt] == 1: continue
                cnt += 1
                visited[nxt] = 1
                stack.append(nxt)
        
        answer = min(answer, abs(n - 2*cnt))    
        
    return answer