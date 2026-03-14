import sys
input = sys.stdin.readline

N = 29
M = 14

d = [
    ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)),
    ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)),
]

dp = [[[0]*N for _ in range(N)] for _ in range(M+1)]
dp[0][M][M] = 1

for t in range(1, M+1):
    for y in range(N):
        for x in range(N):
            total = 0
            for dy, dx in d[y&1]:
                ny, nx = dy+y, dx+x
                if ny<0 or nx<0 or ny>=N or nx>=N: continue
                total += dp[t-1][ny][nx]
            dp[t][y][x] = total

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][M][M])