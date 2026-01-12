import sys
input = sys.stdin.readline

N = int(input())
cards = input().split()
M, K = map(int, input().split())
roads = [[] for _ in range(M+1)]
for _ in range(K):
    u, v, r = input().split()
    u = int(u)
    v = int(v)
    roads[u].append((v, r))
    roads[v].append((u, r))
        
if roads[1] == []:
    print(0)
    sys.exit()

dp = [-1]*(M+1)
dp[1] = 0

for i in range(N):
    dp2 = [-1] * (M+1)
    c = cards[i]

    for j in range(1, M+1):
        if dp[j] < 0:
            continue
        now = dp[j]
        for nxt, c2 in roads[j]:
            x = 10 if c2 == c else 0
            if dp2[nxt] < now + x:
                dp2[nxt] = now + x

    dp = dp2

print(max(dp[1:]))