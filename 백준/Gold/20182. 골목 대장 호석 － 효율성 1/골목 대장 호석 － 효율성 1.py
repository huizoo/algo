import sys, heapq
input = sys.stdin.readline
N, M, A, B, C = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    arr[u].append((v, c))
    arr[v].append((u, c))

heap = [(0, 0, A)]
dist = [1e9]*(N+1)
dist[A] = 0
while heap:
    Max, cost, now = heapq.heappop(heap)
    if cost > dist[now]:
        continue
    if now == B:
        if cost <= C:
            print(Max)
            sys.exit()
    for nxt, cost1 in arr[now]:
        cost2 = cost+cost1
        if dist[nxt] > cost2:
            dist[nxt] = cost2
            heapq.heappush(heap, (max(Max, cost1), cost2, nxt))

print(-1)