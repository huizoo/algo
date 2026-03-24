import sys
input = sys.stdin.readline

MOD = 10**9 + 7
N = int(input())

a, b = 2, 1
for _ in range(N-1):
    a, b = (2*(a+b))%MOD, a

print((a+b)%MOD)