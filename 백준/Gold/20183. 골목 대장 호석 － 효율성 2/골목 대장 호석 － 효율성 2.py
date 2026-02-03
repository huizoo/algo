from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M, A, B, C = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))
    arr[v].append((u, w))

INF = 10**10
heap = [(0, 0, A)]
Max = [INF]*(N+1)
Max[A] = 0
while heap:
    max_cost1, cost1, now = heappop(heap)
    if now == B:
        print(max_cost1)
        sys.exit()
    for nxt, cost2 in arr[now]:
        cost3 = cost1 + cost2
        if cost3 > C: continue
        max_cost2 = max(max_cost1, cost2)
        if Max[nxt] <= max_cost2: continue
        Max[nxt] = max_cost2
        heappush(heap, (max_cost2, cost3, nxt))

print(-1)