from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())
arr = []
sy, sx = -1, -1
hy, hx = -1, -1
for i in range(N):
    row = input().rstrip()
    if sy == -1 or hy == -1:
        for j, v in enumerate(row):
            if v == 'S':
                sy = i; sx = j
            elif v == 'H':
                hy = i; hx = j
    arr.append(row)

q = deque([(sy, sx, 0, False)])
visited = [[0]*M for _ in range(N)]
visited[sy][sx] = 1
visited2 = [[0]*M for _ in range(N)]
while q:
    y, x, cnt, catch = q.popleft()
    if catch:
        if y == hy and x == hx:
            print(cnt)
            break
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if visited2[ny][nx] == 1: continue
            if arr[ny][nx] == 'D': continue
            visited2[ny][nx] = 1
            q.append((ny, nx, cnt+1, True))
    else:
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if visited[ny][nx] == 1: continue
            if arr[ny][nx] == 'D': continue
            elif arr[ny][nx] == 'F':
                visited2[ny][nx] = 1
                q.append((ny, nx, cnt+1, True))
            else:
                visited[ny][nx] = 1
                q.append((ny, nx, cnt+1, False))

else:
    print(-1)