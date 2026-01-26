from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
lands = defaultdict(set)
visited = [[0]*N for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
land = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0: continue
        if visited[i][j] == 1: continue
        q = [(i, j)]
        lands[land].add((i, j))
        visited[i][j] = 1
        while q:
            y, x = q.pop()
            for dy, dx in d:
                ny, nx = dy+y, dx+x
                if ny<0 or nx<0 or ny>=N or nx>=N: continue
                if arr[ny][nx] == 0: continue
                if visited[ny][nx] == 1: continue
                visited[ny][nx] = 1
                lands[land].add((ny, nx))
                q.append((ny, nx))
        land += 1

Min = 1e9
for i in range(1, land):
    for y, x in lands[i]:
        for j in range(i+1, land):
            for y1, x1 in lands[j]:
                Min = min(Min, abs(y-y1)+abs(x-x1))

print(Min-1)
