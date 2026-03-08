import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def abc(now, par):
    dp[now][1] = arr[now]
    for nxt in nodes[now]:
        if nxt == par: continue
        abc(nxt, now)
        dp[now][1] += dp[nxt][0]
        dp[now][0] += max(dp[nxt][0], dp[nxt][1])
        
N = int(input())
arr = [0] + list(map(int, input().split()))
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
abc(1, 0)
print(max(dp[1]))