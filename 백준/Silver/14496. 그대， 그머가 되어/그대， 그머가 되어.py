from collections import deque
import sys, heapq
input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

heap = [(0, a)]
dist = [10**12]*(N+1)
dist[a] = 0
while heap:
    cost, now = heapq.heappop(heap)
    if dist[now] < cost:
        continue
    cost2 = cost + 1
    for nxt in arr[now]:
        if dist[nxt] > cost2:
            dist[nxt] = cost2
            heapq.heappush(heap, (cost2, nxt))

print(dist[b] if dist[b] != 10**12 else -1)

# q = deque([(a, 0)])
# visited = [0]*(N+1)
# visited[a] = 1
# while q:
#     now, cnt = q.popleft()
#     if cnt > M:
#         print(-1)
#         break
#     if now == b:
#         print(cnt)
#         break
#     for nxt in arr[now]:
#         if visited[nxt] == 1: continue
#         visited[nxt] = 1
#         q.append((nxt, cnt+1))

# else:
#     print(-1)