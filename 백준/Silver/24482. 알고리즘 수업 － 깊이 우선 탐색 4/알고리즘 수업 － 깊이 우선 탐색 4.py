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

answer = [-1]*(N+1)
def dfs(node, level):
    if answer[node] == -1:
        answer[node] = level
    for nxt in arr[node]:
        if answer[nxt] != -1: continue
        dfs(nxt, level+1)

dfs(R, 0)

print(*answer[1:], sep='\n')