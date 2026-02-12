import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, L = map(int, input().split())
    arr[A].append([B, L])
    arr[B].append([A, L])

INF = 1<<31
dist = [INF]*(N+1)
prev = [-1]*(N+1)
dist[1] = 0
heap = [(0, 1)]

while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] < cost:
        continue
    if now == N:
        break
    for nxt, cost2 in arr[now]:
        ncost = cost+cost2
        if dist[nxt] > ncost:
            dist[nxt] = ncost
            prev[nxt] = now
            heapq.heappush(heap, (ncost, nxt))


c1 = dist[N]
SE = []
idx = N
while idx != 1:
    SE.append((prev[idx], idx))
    idx = prev[idx]


Max = 0
for n, m in SE:
    dist = [INF]*(N+1)
    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        cost, now = heapq.heappop(heap)
        if dist[now] < cost:
            continue
        if now == N:
            break
        for nxt, cost2 in arr[now]:
            if n == now and m == nxt:
                cost2 *= 2
            ncost = cost+cost2
            if dist[nxt] > ncost:
                dist[nxt] = ncost
                heapq.heappush(heap, (ncost, nxt))
    
    Max = max(Max, dist[N]-c1)

print(Max)