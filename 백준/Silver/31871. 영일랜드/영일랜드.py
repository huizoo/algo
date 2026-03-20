import sys
input = sys.stdin.readline

def dfs(now, cost, mask):
    global Max
    if now == 0:
        if mask & check == check:
            Max = max(Max, cost)
        return
    
    if memo[now][mask] < cost:
        memo[now][mask] = cost
    else:
        return
    
    for nxt, cost2 in arr[now]:
        if 1<<nxt & mask: continue
        dfs(nxt, cost+cost2, mask | 1<<nxt)

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))

check = (1<<N+1)-1
Max = -1
memo = [[0]*(1<<N+1) for _ in range(N+1)]
for v, w in arr[0]:
    dfs(v, w, 1<<v)

print(Max)