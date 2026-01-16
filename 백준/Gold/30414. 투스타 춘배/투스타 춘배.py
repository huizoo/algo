import sys
sys.setrecursionlimit(100100)
input = sys.stdin.readline

N, P = map(int, input().split())
P -= 1

A = list(map(int, input().split()))
B = list(map(int, input().split()))

roads = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    roads[u].append(v)
    roads[v].append(u)

visited = [0] * N

def dfs(now):
    visited[now] = 1
    need = B[now]-A[now]

    for v in roads[now]:
        if not visited[v]:
            need += dfs(v)
    if need < 0:
        return 0
    return need

answer = dfs(P)
print(answer)
