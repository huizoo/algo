import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
lo = [0]*N
hi = [0]*N
for i in range(N):
    a, b = map(int, input().split())
    lo[i] = a-b
    hi[i] = a+b

arr1 = sorted(lo)
arr2 = sorted(hi)

for i in range(N):
    print(bisect_left(arr2, lo[i])+1, bisect_right(arr1, hi[i]))