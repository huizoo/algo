from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L, R = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '2':
            y, x = i, j

cango = set()
q = deque()
q.append((y, x, L, R))
cango.add((y, x))
d = (-1, 1)
while q:
    yy, xx, l, r = q.popleft()
    for dy in d:
        ny = yy+dy
        if ny < 0 or ny >= N: continue
        if arr[ny][xx] == '1': continue
        if (ny, xx) in cango: continue
        cango.add((ny, xx))
        q.appendleft((ny, xx, l, r))
    if l > 0:
        nx = xx-1
        if nx >= 0 and arr[yy][nx] != '1' and (yy, nx) not in cango: 
            cango.add((yy, nx))
            q.append((yy, nx, l-1, r))
    if r > 0:
        nx = xx+1
        if nx < M and arr[yy][nx] != '1' and (yy, nx) not in cango: 
            cango.add((yy, nx))
            q.append((yy, nx, l, r-1))
        

print(len(cango))