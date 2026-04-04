import sys
input = sys.stdin.readline
H, N = map(int, input().split())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1], reverse=True)
dp = [0]*(H+1)
dp[0] = 1
for i, (h, s) in enumerate(arr):
    for hh in range(H, h-1, -1):
        if dp[hh-h] == 1:
            dp[hh] = 1
    
    if dp[H]:
        print(s)
        break
