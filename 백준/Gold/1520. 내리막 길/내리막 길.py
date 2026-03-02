import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
arr2 = []
for i, row in enumerate(arr):
    for j, v in enumerate(row):
        arr2.append((v, i, j))

arr2.sort(reverse=True)

dp = [[0]*N for _ in range(M)]
dp[0][0] = 1

for h, y, x in arr2:
    if dp[y][x] == 0:
        continue

    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=M or nx>=N: continue
        if arr[ny][nx] < arr[y][x]:
            dp[ny][nx] += dp[y][x]

print(dp[M-1][N-1])