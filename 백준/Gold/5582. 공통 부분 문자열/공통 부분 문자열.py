import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
ls = len(s)
lt = len(t)
Max = 0
dp = [[0]*(lt+1) for _ in range(ls+1)]
for i in range(ls):
    for j in range(lt):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
            Max = max(Max, dp[i+1][j+1])

print(Max)