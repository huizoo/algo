mod = 1_000_000_007

def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1

    if puddles != [[]]:
        for x, y in puddles:
            dp[y-1][x-1] = -1
    
    for y in range(1, n):
        if dp[y][0] != -1:
            dp[y][0] = 1
        else:
            break

    for x in range(1, m):
        if dp[0][x] != -1:
            dp[0][x] = 1
        else:
            break

    for y in range(1, n):
        for x in range(1, m):
            if dp[y][x] == -1: continue
            dp[y][x] = (max(dp[y-1][x], 0) + max(dp[y][x-1], 0)) % mod

    return dp[n-1][m-1] % mod