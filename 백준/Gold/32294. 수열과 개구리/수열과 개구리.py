import sys, heapq
input = sys.stdin.readline
INF = 1<<60
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = [[] for _ in range(N)]
dist = [INF]*N
heap = []
for i, v in enumerate(A):
    b = B[i]
    l = i-v
    r = i+v
    if l >= 0:
        arr[l].append((i, b))
    else:
        dist[i] = min(dist[i], b)
        heapq.heappush(heap, (dist[i], i))
    
    if r < N:
        arr[r].append((i, b))
    else:
        dist[i] = min(dist[i], b)
        heapq.heappush(heap, (dist[i], i))

while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] < cost:
        continue

    for nxt, cost2 in arr[now]:
        ncost = cost + cost2
        if dist[nxt] > ncost:
            dist[nxt] = ncost
            heapq.heappush(heap, (ncost, nxt))

print(*dist)
    
