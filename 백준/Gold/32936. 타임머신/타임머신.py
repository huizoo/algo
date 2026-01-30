from collections import deque
import sys
input = sys.stdin.readline

N, M, a, b, c = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append((v))


q = deque([(1, 0)])
visited = [0]*(N+1)
visited[1] = 1
Min = 10**9
while q:
    now, cost = q.popleft()
    if now == N:
        Min = cost
        break
    for nxt in arr[now]:
        if visited[nxt]: continue
        visited[nxt] = 1
        q.append((nxt, cost+1))

can = [-1]*3
q = deque([(1, 0)])
visited = [0]*(N+1)
visited[1] = 1
while q:
    now, cost = q.popleft()
    if now == a:
        can[0] = cost
        if can[1] != -1: break
    elif now == b:
        can[1] = cost
        if can[0] != -1: break
    for nxt in arr[now]:
        if visited[nxt]: continue
        visited[nxt] = 1
        q.append((nxt, cost+1))

q = deque([(b, 0)])
visited = [0]*(N+1)
visited[b] = 1
while q:
    now, cost = q.popleft()
    if now == N:
        can[2] = cost
        break
    for nxt in arr[now]:
        if visited[nxt]: continue
        visited[nxt] = 1
        q.append((nxt, cost+1))


q = deque([(b, 0)])
visited = [0]*(N+1)
visited[b] = 1
dist_ba = -1
while q:
    now, cost = q.popleft()
    if now == a:
        dist_ba = cost
        break
    for nxt in arr[now]:
        if visited[nxt]: continue
        visited[nxt] = 1
        q.append((nxt, cost+1))

if can[0] != -1 and can[2] != -1 and dist_ba != -1 and dist_ba < c:
    print('-inf')
    sys.exit()

if can[0] != -1 and can[2] != -1:
    Min = min(Min, can[0] + can[2] - c)

print(Min if Min != 10**9 else 'x')