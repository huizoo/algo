from collections import deque

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0]*m for _ in range(n)]
    Sum = [0]*m
    for j in range(m):
        for i in range(n):
            if land[i][j] == 0: continue
            if visited[i][j] == 1: continue
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            cnt = 1
            minx, maxx = j, j
            while q:
                nowy, nowx = q.popleft()
                for dy, dx in d:
                    ny, nx = nowy + dy, nowx + dx
                    if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
                    if land[ny][nx] == 0: continue
                    if visited[ny][nx] == 1: continue
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    cnt += 1
                    minx, maxx = min(minx, nx), max(maxx, nx)
            for k in range(minx, maxx+1):
                Sum[k] += cnt
    return max(Sum)