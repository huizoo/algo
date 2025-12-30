from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
T1 = set()
for _ in range(N-1):
    u, v = map(int, input().split())
    # 앞 정점의 번호가 더 작도록 교환
    if u > v:
        u, v = v, u
    T1.add((u, v))


arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    if (u, v) in T1:
        arr[u].append(v)
        arr[v].append(u)

dist = [-1]*(N+1)
visited = [0]*(N+1)

best = 0
bu, bv = -1, -1

def bfs(start):
    q = deque([start])
    dist[start] = 0
    visited2 = [start]
    far_node = start
    far_dist = 0
    while q:
        now = q.popleft()
        d = dist[now]
        if d > far_dist:
            far_dist = d
            far_node = now
        for nxt in arr[now]:
            if dist[nxt] != -1: continue
            dist[nxt] = d + 1
            q.append(nxt)
            visited2.append(nxt)

    return far_node, far_dist, visited2

for i in range(1, N+1):
    if visited[i]: continue
    if not arr[i]: continue
    n1, d1, visited3 = bfs(i)
    dist = [-1]*(N+1)

    n2, d2, visited4 = bfs(n1)
    dist = [-1]*(N+1)

    if d2 > best:
        best = d2
        bu, bv = n1, n2

if best < 1:
    print(-1)
else:
    print(bu, bv)