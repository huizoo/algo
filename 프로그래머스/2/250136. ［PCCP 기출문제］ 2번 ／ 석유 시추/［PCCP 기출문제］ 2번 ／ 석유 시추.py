def solution(land):
    n, m = len(land), len(land[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0]*m for _ in range(n)]
    prefix = [0]*(m+1)
    for i, row in enumerate(land):
        for j, v in enumerate(row):
            if v == 1 and visited[i][j] == 0:
                l = r = j
                stack = []
                stack.append((i, j))
                visited[i][j] = 1
                cnt = 1
                while stack:
                    y, x = stack.pop()
                    if x < l:
                        l = x
                    elif r < x:
                        r = x
                    for dy, dx in d:
                        ny, nx = dy+y, dx+x
                        if 0<=ny<n and 0<=nx<m:
                            if land[ny][nx] == 0: continue
                            if visited[ny][nx] == 1: continue
                            stack.append((ny, nx))
                            visited[ny][nx] = 1
                            cnt += 1
                prefix[l] += cnt
                prefix[r+1] -= cnt
    
    for i in range(m):
        prefix[i+1] += prefix[i]
    
    return max(prefix)