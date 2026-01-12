import sys, heapq
input = sys.stdin.readline

N = int(input())
T, M = map(int, input().split())
L = int(input())
taxi = [[] for _ in range(N+1)]
for _ in range(L):
    u, v, t, c = map(int, input().split())
    taxi[u].append((v, t, c))
    taxi[v].append((u, t, c))

dist = [[1e9]*(T+1) for _ in range(N+1)]
dist[1][0] = 0

# 현재 소모된 돈, 시간, 현재 위치
heap = [(0, 0, 1)]

while heap:
    c1, t1, now = heapq.heappop(heap)

    for nxt, t, c in taxi[now]:
        c2 = c+c1
        t2 = t+t1
        if t2 > T or c2 > M: continue
        if c2 < dist[nxt][t2]:
            dist[nxt][t2] = c2
            heapq.heappush(heap, (c2, t2, nxt))


answer = min(dist[N])
print(-1 if answer == 1e9 else answer)