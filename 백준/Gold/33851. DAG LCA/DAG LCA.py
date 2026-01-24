from collections import deque
import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
arr = [[] for _ in range(N+1)]
arr2 = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr2[v].append(u)

def abc(start):
    dist = [-1]*(N+1)
    q = deque([start])
    dist[start] = 0
    while q:
        now = q.popleft()
        for nxt in arr2[now]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[now] + 1
            q.append(nxt)
    return dist

for _ in range(Q):
    a, b = map(int, input().split())

    distA = abc(a)
    distB = abc(b)

    Min = 1e9
    for x in range(1, N+1):
        if distA[x] != -1 and distB[x] != -1:
            Min = min(Min, max(distA[x], distB[x]))

    print(Min if Min != 1e9 else -1)
