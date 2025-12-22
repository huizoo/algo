import sys, heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [dict() for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    if end not in arr[start] or cost < arr[start][end]:
        arr[start][end] = cost

start, end = map(int, input().split())

dist = [1e11]*(N+1)
dist[start] = 0

heap = [(0, start)]

while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] < cost:
        continue
    
    for nxt, weight in arr[now].items():
        new_cost = cost + weight
        if dist[nxt] > new_cost:
            dist[nxt] = new_cost
            heapq.heappush(heap, (new_cost, nxt))

print(dist[end])