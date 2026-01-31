import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    arr[A].append((B, C))
    arr[B].append((A, C))
    
heap = [(0, 1)]
INF = 10**15
dist = [INF]*(N+1)
dist[1] = 0
while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] < cost:
        continue
    if now == N:
        break
    for nxt, cost1 in arr[now]:
        cost2 = cost+cost1
        if dist[nxt] > cost2:
            dist[nxt] = cost2
            heapq.heappush(heap, (cost2, nxt))

print(dist[N])