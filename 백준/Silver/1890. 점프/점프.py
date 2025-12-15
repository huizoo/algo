import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        k = arr[i][j]
        if k == 0: break
        if i+k < N:
            dp[i+k][j] += dp[i][j]
        if j+k < N:
            dp[i][j+k] += dp[i][j]

print(dp[N-1][N-1])