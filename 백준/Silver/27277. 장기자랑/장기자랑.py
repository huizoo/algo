import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + sorted(map(int, input().split()))
Sum = 0
for i in range((N+1)//2):
    Sum += arr[-i-1] - arr[i]

print(Sum)