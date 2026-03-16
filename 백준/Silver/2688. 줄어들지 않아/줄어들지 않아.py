import sys
input = sys.stdin.readline

dp = [1]*10
cnt = [0]*65
cnt[1] = 10
for i in range(2,65):
    for j in range(1,10):
        dp[j] += dp[j-1]
    cnt[i] = sum(dp)

for _ in range(int(input())):
    N = int(input())
    print(cnt[N])
    