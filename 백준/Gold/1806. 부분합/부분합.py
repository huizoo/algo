import sys

input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

Sum = 0
start = 0
Min = 100000
for i in range(N):
    Sum += arr[i]
    while Sum >= S:
        Min = min(Min, i-start+1)
        Sum -= arr[start]
        start += 1

if Min == 100000:
    print(0)
else:    
    print(Min)
