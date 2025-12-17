from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

N, M = map(int, input().split())
arr = [input().strip() for _ in range(M)]

visited = [[0]*N for _ in range(M)]

q = deque()
color = [0]*2

for i in range(M):
    for j in range(N):
        if visited[i][j] == 1: continue
        visited[i][j] = 1
        q.append((i, j))
        now = arr[i][j]
        cnt = 1
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if ny < 0 or nx < 0 or ny >= M or nx >= N: continue
                if visited[ny][nx] == 1: continue
                if arr[ny][nx] != now: continue
                visited[ny][nx] = 1
                cnt += 1
                q.append((ny, nx))
        if now == 'W':
            color[0] += cnt**2
        else:
            color[1] += cnt**2

print(*color)

