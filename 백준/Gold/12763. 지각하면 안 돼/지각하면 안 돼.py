import sys, heapq
input = sys.stdin.readline

N = int(input())
T, M = map(int, input().split())
L = int(input())
taxi = [[] for _ in range(N+1)]
for _ in range(L):
    u, v, t, c = map(int, input().split())
    taxi[u].append((v, t, c))
    taxi[v].append((u, t, c))


visited = [[] for _ in range(N+1)]

heap = []
for nxt, t, c in taxi[1]:
    if t > T or c > M : continue
    heapq.heappush(heap, (c, t, nxt))
        

while heap:
    c1, t1, now = heapq.heappop(heap)
    
    if now == N:
        print(c1)
        break

    for nxt, t, c in taxi[now]:
        c2 = c+c1
        t2 = t+t1
        if t2 > T or c2 > M: continue

        for c3, t3 in visited[nxt]:
            if c3 <= c2 and t3 <= t2:
                break
        else:
            visited[nxt].append((c2, t2))
            heapq.heappush(heap, (c2, t2, nxt))

else:
    print(-1)