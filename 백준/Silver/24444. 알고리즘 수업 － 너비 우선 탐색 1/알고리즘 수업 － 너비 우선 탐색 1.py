from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    arr[i].sort()

visited = [0]*(N+1)
cnt = 1
visited[R] = cnt
q = deque([R])
while q:
    now = q.popleft()
    for nxt in arr[now]:
        if visited[nxt]: continue
        cnt += 1
        visited[nxt] = cnt
        q.append(nxt)

print(*visited[1:], sep='\n')