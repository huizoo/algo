import sys, heapq
input = sys.stdin.readline
N, M, A, B, C = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    arr[u].append((v, c))
    arr[v].append((u, c))

def dijkstra(k):
    heap = [(0, 0, A)]
    dist = [1e9]*(N+1)
    dist[A] = 0
    while heap:
        cost, Max, now = heapq.heappop(heap)
        if cost > dist[now]:
            continue
        if cost > C:
            continue
        if now == B:
            return 1
        for nxt, cost1 in arr[now]:
            Max2 = max(Max, cost1)
            if Max2 > k:
                continue
            cost2 = cost+cost1
            if dist[nxt] > cost2:
                dist[nxt] = cost2
                heapq.heappush(heap, (cost2, Max2, nxt))

    return 0

l, r = 0, 20
while l < r:
    mid = (l+r)//2
    if dijkstra(mid):
        r = mid
    else:
        l = mid+1

print(l if dijkstra(l) else -1)