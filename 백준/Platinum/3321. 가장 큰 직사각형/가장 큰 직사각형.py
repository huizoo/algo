import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
dp = [1 if arr[0][j] == 1 else 0 for j in range(M)]
S = dp.count(1)
for i in range(1, N):
    for j in range(M):
        if arr[i][j] == 1:
            dp[j] += 1
        else:
            dp[j] = 0
    dp2 = sorted(dp)
    for k in range(M):
        S = max(S, dp2[k]*(M-k))

print(S)
    