import sys
input = sys.stdin.readline
N = int(input())
dp = [-10**18]*(1<<5)
dp[0] = 0
for i in range(N):
    row = list(map(int, input().split()))
    for mask in range((1<<5)-1, -1, -1):
        if dp[mask] < 0:
            continue
        for j in range(5):
            if mask & (1<<j):
                continue
            
            mask2 = mask | (1<<j)
            dp[mask2] = max(dp[mask2], dp[mask] + row[j])

print(dp[(1<<5)-1])