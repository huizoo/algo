import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
S = 0
dp = [0]*M
for i in range(N):
    for j, value in enumerate(arr[i]):
        if value == '1':
            dp[j] += 1
        else:
            dp[j] = 0
    dp2 = sorted(dp)
    for k, value in enumerate(dp2):
        S = max(S, value*(M-k))

print(S)
    