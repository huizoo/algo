import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

inf = -1e9
dp = [inf]*101

dp[arr[0]] = 0

for i in range(1, N):
    now = arr[i]
    dp2 = dp[:]
    for bef in range(1, 101):
        if dp[bef] == inf: continue
        dp2[now] = max(dp2[now], dp[bef] + (now - bef)**2)
        
    dp = dp2

print(max(dp))