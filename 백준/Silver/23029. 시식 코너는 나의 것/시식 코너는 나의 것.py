import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

dp[0][1] = arr[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]//2

print(max(dp[N-1]))