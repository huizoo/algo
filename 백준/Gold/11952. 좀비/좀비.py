from collections import deque
import sys, heapq
input = sys.stdin.readline

N, M, K, S = map(int, input().split())

P, Q = map(int, input().split())

zombies = set([int(input()) for _ in range(K)])
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

q = deque()
visited = set()
for zombie in zombies:
    q.append((0, zombie))
    visited.add(zombie)

while q:
    dist, now = q.popleft()
    if dist == S: continue
    for nxt in arr[now]:
        if nxt in visited: continue
        visited.add(nxt)
        q.append((dist+1, nxt))

heap2 = list()
arr2 = [1e21]*(N+1)
heap2.append((0, 1))
arr2[1] = 0
# print(arr)
# print(visited)
while heap2:
    cost, now = heapq.heappop(heap2)
    for nxt in arr[now]:
        if nxt in zombies: continue
        if nxt in visited:
            cost2 = cost + Q
            if arr2[nxt] > cost2:
                arr2[nxt] = cost2
                heapq.heappush(heap2, (cost2, nxt))
                # print(1, heap2)
        else:
            cost2 = cost + P
            if arr2[nxt] > cost2:
                arr2[nxt] = cost2
                heapq.heappush(heap2, (cost2, nxt))
                # print(2, heap2)

if N in visited:
    print(arr2[N] - Q)
else:
    print(arr2[N] - P)
