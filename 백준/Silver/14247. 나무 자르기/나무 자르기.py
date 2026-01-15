import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

arr = sorted(list(zip(H, A)), key=lambda x: x[1])

Sum = 0
for idx, (h, a) in enumerate(arr):
    Sum += h + a*idx

print(Sum)
