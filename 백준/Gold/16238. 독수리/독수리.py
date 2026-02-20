import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()), reverse=True)
Sum = 0
for idx, value in enumerate(A):
    if value-idx > 0:
        Sum += value-idx
    else:
        break

print(Sum)