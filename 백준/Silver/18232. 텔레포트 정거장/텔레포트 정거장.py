from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

q = deque()
q.append((S, 0))
INF = 1<<31
dist = [INF]*(N+1)
while q:
    now, cost = q.popleft()
    if now == E:
        print(cost)
        break
    for nxt in arr[now]:
        if dist[nxt] > cost+1:
            dist[nxt] = cost+1
            q.append((nxt, cost+1))
    for nxt in [now-1, now+1]:
        if 0 < nxt <= N and dist[nxt] > cost+1:
            dist[nxt] = cost+1
            q.append((nxt, cost+1))