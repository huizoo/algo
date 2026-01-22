import sys
input = sys.stdin.readline

N = int(input())
arr = tuple(map(int, input().split()))

ans = abs(arr[1] - arr[0])
for i in range(1, N-1):
    ans = min(ans, abs(arr[i+1] - arr[i]))

print(ans)
