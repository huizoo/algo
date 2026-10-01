from collections import deque

def solution(maps):
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    n = len(maps)
    m = len(maps[0])
    answer = -1
    q = deque()
    q.append([0, 0, 1])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            answer = cnt
            break
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<m:
                if maps[ny][nx] == 0: continue
                if visited[ny][nx]: continue
                visited[ny][nx] = 1
                q.append([ny, nx, cnt+1])

    return answer