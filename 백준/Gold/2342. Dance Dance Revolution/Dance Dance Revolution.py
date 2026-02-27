import sys
input = sys.stdin.readline

dic = {
    1: [2, 1, 3, 4, 3],
    2: [2, 3, 1, 3, 4],
    3: [2, 4, 3, 1, 3],
    4: [2, 3, 4, 3, 1],
}

arr = list(map(int, input().split()))
INF = 10**9
dp = [[INF]*5 for _ in range(5)]
dp[0][0] = 0

for x in arr:
    if x == 0:
        break

    ndp = [[INF]*5 for _ in range(5)]

    for l in range(5):
        for r in range(5):
            if dp[l][r] == INF:
                continue

            ndp[x][r] = min(ndp[x][r], dp[l][r]+dic[x][l])
            ndp[l][x] = min(ndp[l][x], dp[l][r]+dic[x][r])
    
    dp = ndp

print(min(min(row) for row in dp))