import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[-1]*3 for _ in range(N)]

def abc(n, x):
    if n < 0:
        return 0
    
    if dp[n][x] != -1:
        return dp[n][x]

    if x == 2:
        dp[n][x] = abc(n-1, 1) + arr[n]//2
    elif x == 1:
        dp[n][x] = abc(n-1, 0) + arr[n]
    else:
        dp[n][x] = max(abc(n-1, 0), abc(n-1, 1), abc(n-1, 2))
    
    return dp[n][x]

print(max(abc(N-1, 0), abc(N-1, 1), abc(N-1, 2)))