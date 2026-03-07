import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i, _ in enumerate(arr):
    arr[i].sort()

visited = [0]*(N+1)
cnt = 1
def dfs(now):
    global cnt
    visited[now] = cnt
    cnt += 1
    for nxt in arr[now]:
        if visited[nxt]: continue
        dfs(nxt)

dfs(R)

print('\n'.join(map(str, visited[1:])))