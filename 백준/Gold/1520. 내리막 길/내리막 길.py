import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

def dfs(y, x, now):
    if y == M-1 and x == N-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=M or nx>=N: continue
        if arr[ny][nx] >= now: continue
        dp[y][x] += dfs(ny, nx, arr[ny][nx])
    
    return dp[y][x]

dfs(0, 0, arr[0][0])


print(dp[0][0])