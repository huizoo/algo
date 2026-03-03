import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
ry, rx = -1, -1
dp = [[-10**9]*M for _ in range(N)]
EXIT = []
for i in range(N):
    row = input().rstrip()
    arr.append(row)
    for j, v in enumerate(row):
        if v == 'R':
            ry = i; rx = j
        elif v == 'O':
            EXIT.append((i, j))

dp[ry][rx] = 0

for j in range(rx+1, M):
    for i in range(N):
        if arr[i][j] == '#':
            continue

        temp = -10**9
        for ni in [i-1, i, i+1]:
            if 0 <= ni < N:
                temp = max(temp, dp[ni][j-1])

        dp[i][j] = temp + (1 if arr[i][j] == 'C' else 0)

Max = -1
for y, x in EXIT:
    Max = max(Max, dp[y][x])

print(Max)