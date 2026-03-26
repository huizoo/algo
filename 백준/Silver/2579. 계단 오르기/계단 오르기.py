import sys
input = sys.stdin.readline

N = int(input())
arr = [0]+[int(input()) for _ in range(N)]
dp = [0]*(N+1)
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
for i in range(2, N+1):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(dp[N])
