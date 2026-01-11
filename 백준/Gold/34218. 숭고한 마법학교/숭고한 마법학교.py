from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())
sr -= 1
sc -= 1
er -= 1
ec -= 1

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

visited = [[0]*M for _ in range(N)]

q = [(sr, sc)]
visited[sr][sc] = 1
start = set(q)

while q:
    y, x = q.pop()
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or ny>=N or nx<0 or nx>=M: continue
        if arr[ny][nx] == 0: continue
        if visited[ny][nx] == 1: continue
        visited[ny][nx] = 1
        start.add((ny, nx))
        q.append((ny, nx))

if (er, ec) in start:
    print(0)
    sys.exit()

q2 = [(er, ec)]
visited[er][ec] = 1
end = set(q2)

while q2:
    y, x = q2.pop()
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or ny>=N or nx<0 or nx>=M: continue
        if visited[ny][nx]: continue
        if arr[ny][nx] == 0: continue
        visited[ny][nx] = 1
        end.add((ny, nx))
        q2.append((ny, nx))


dist = [[1e9]*M for _ in range(N)]
q3 = deque()

for y, x in start:
    dist[y][x] = 0
    q3.append((y, x))

while q3:
    y, x = q3.popleft()
    
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or ny>=N or nx<0 or nx>=M: continue
        if dist[ny][nx] > dist[y][x] + 1:
            dist[ny][nx] = dist[y][x] + 1
            q3.append((ny, nx))

Min = 1e9
for y, x in end:
    if Min > dist[y][x]:
        Min = dist[y][x]

print(Min)