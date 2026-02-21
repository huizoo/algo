from math import sqrt
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
x = int(sqrt(b))
arr = [1]*(b-a+1)
for i in range(2, x+1):
    ii = i*i
    start = ((a+ii-1)//ii)*ii

    for j in range(start, b+1, ii):
        arr[j-a] = 0


print(sum(arr))