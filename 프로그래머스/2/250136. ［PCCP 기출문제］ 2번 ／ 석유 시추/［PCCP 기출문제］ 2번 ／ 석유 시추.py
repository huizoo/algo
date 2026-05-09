def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0]*m for _ in range(n)]
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    prefix = [0]*(m+1)
    for i, row in enumerate(land):
        for j, v in enumerate(row):
            if v == 1 and not visited[i][j]:
                l = r = j
                stack = []
                stack.append((i, j))
                cnt = 1
                visited[i][j] = 1
                while stack:
                    y, x = stack.pop()
                    if x < l:
                        l = x
                    elif r < x:
                        r = x
                    for dy, dx in d:
                        ny, nx = dy+y, dx+x
                        if ny<0 or nx<0 or ny>=n or nx>=m: continue
                        if not land[ny][nx]: continue
                        if visited[ny][nx]: continue
                        stack.append((ny, nx))
                        visited[ny][nx] = 1
                        cnt += 1
                prefix[l] += cnt
                prefix[r+1] -= cnt
    Max = 0
    Sum = 0
    for x in prefix:
        Sum += x
        if Max < Sum:
            Max = Sum
    
    return Max