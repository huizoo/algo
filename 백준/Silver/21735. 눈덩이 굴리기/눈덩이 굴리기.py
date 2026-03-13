import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [0] + list(map(int,input().split())) + [0, 0]

dp = [[-1]*(N+3) for _ in range(M+1)]
dp[0][0] = 1

for i in range(M):
    for j in range(N+1):
        if dp[i][j] == -1:
            continue
        size = dp[i][j]
        dp[i+1][j+1] = max(dp[i+1][j+1], size + arr[j+1])
        dp[i+1][j+2] = max(dp[i+1][j+2], size//2 + arr[j+2])

print(max(max(row) for row in dp))