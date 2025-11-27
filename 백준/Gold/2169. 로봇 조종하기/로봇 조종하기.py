import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

d = [(0, 1), (-1, 0), (0, -1)]

dp = [[[-1e9]*3 for _ in range(M)] for _ in range(N)]
dp[0][0] = [arr[0][0], arr[0][0], arr[0][0]]
Min = -1e9
for i in range(N):
    if i == 0:
        for j in range(M-1):
            dp[0][j+1][2] = dp[0][j][2] + arr[0][j+1]
            dp[0][j+1][1] = dp[0][j+1][2]
    else:
        for j in range(M):
            if j == 0:
                dp[i][j][1] = max(dp[i-1][j]) + arr[i][j]
                continue
            for k in range(1, 3):
                if k == 1:
                    dp[i][j][1] = max(dp[i-1][j]) + arr[i][j]
                    continue
                ny, nx = i + d[k][0], j + d[k][1]
                if nx < 0 or nx >= M: continue
                dp[i][j][k] = max(dp[ny][nx][1], dp[ny][nx][2]) + arr[i][j]

        for j in range(M-1, -1, -1):
            if j == M-1:
                dp[i][j][1] = max(dp[i-1][j]) + arr[i][j]
            for k in range(1):
                ny, nx = i + d[k][0], j + d[k][1]
                if nx < 0 or nx >= M: continue
                dp[i][j][k] = max(dp[ny][nx][0], dp[ny][nx][1]) + arr[i][j]


print(max(dp[N-1][M-1]))