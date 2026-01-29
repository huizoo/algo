import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

INF = 10**12
lower = -INF
upper = INF

x = 0

for j in range(N):
    if j % 2 == 0:
        upper = min(upper, arr[j]-x)
    else:
        lower = max(lower, x-arr[j])

    x = 2*arr[j]-x

print(max(0, upper-lower+1))
