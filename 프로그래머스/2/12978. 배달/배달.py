import heapq

def solution(N, road, K):
    INF = 10**9
    answer = 0
    arr = [[] for _ in range(N+1)]
    for u, v, c in road:
        arr[u].append((v, c))
        arr[v].append((u, c))
    
    dist = [INF]*(N+1)
    dist[1] = 0
    heap = [(1, 0)]
    while heap:
        now, cost = heapq.heappop(heap)
        for nxt, cost2 in arr[now]:
            if dist[nxt] > (ncost:= cost+cost2):
                dist[nxt] = ncost
                heapq.heappush(heap, (nxt, ncost))
    
    return sum(1 if dist[i] <= K else 0 for i in range(1, N+1))