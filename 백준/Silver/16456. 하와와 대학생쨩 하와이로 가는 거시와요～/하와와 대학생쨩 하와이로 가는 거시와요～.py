import sys
input = sys.stdin.readline
N = int(input())
MOD = 10**9+9
arr = [0]*(max(7, N+1))
arr[1] = 1
arr[2] = 1
arr[3] = 2
arr[4] = 3
arr[5] = 4
arr[6] = 6
for i in range(7, N+1):
    arr[i] = (arr[i-1]+arr[i-3])%MOD

print(arr[N])
