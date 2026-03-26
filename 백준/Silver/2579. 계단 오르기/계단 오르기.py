import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*2 for _ in range(N+1)]
dp[1][0] = int(input())
for i in range(2, N+1):
    x = int(input())
    dp[i][0] = max(dp[i][0], dp[i-2][0] + x, dp[i-2][1] + x)
    dp[i][1] = max(dp[i][1], dp[i-1][0] + x)

print(max(dp[N]))
