import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
arr = []
for i in range(N):
    arr.append((H[i]+A[i]*(N-1), -A[i]))

arr.sort(key=lambda x: (x[1], -x[0]))

Sum = 0

for i in range(N):
    Sum += arr[i][0]+arr[i][1]*i

print(Sum)