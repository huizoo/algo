import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(2)]


dp0 = max(arr[0][0], arr[0][0]+arr[1][0])
dp1 = arr[0][0]+arr[1][0]

for i in range(1, N):
    a, b = arr[0][i], arr[1][i]

    ndp0 = max(dp0+a, dp0+a+b, dp1+a+b)
    ndp1 = max(dp1+b, dp1+a+b, dp0+a+b)

    dp0, dp1 = ndp0, ndp1

print(dp1)
