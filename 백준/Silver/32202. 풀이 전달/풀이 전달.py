from array import array
import sys
input = sys.stdin.readline
MOD = 10**9+7
N = int(input())
dp = [array('I', [1]*2) for _ in range(N)]

for i in range(1, N):
    dp[i][0] = (dp[i-1][0]*2 + dp[i-1][1]) % MOD
    dp[i][1] = (dp[i-1][0]*2) % MOD

print((2*dp[-1][0]+dp[-1][1])%MOD)