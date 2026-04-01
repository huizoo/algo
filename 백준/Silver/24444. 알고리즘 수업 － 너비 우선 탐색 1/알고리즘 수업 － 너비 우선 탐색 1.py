from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)

for i in range(N):
    arr[i].sort()

visited = [0]*(N)
cnt = 1
visited[R-1] = cnt
q = deque([R-1])
while q:
    now = q.popleft()
    for nxt in arr[now]:
        if visited[nxt]: continue
        cnt += 1
        visited[nxt] = cnt
        q.append(nxt)

print(*visited, sep='\n')