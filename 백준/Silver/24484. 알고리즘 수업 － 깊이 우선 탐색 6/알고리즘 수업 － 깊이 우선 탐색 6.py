import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    arr[i].sort(reverse=True)

def dfs(now, d):
    global x
    visited[now] = x*d
    x += 1
    for nxt in arr[now]:
        if visited[nxt] == -1:
            dfs(nxt, d+1) 

visited = [-1]*(N+1)
x = 1
dfs(R, 0)

print(sum(x for x in visited if x != -1))