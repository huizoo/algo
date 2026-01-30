import sys
input = sys.stdin.readline

N, A = map(int, input().split())
k = 0
while N >= A:
    temp = N // A
    k += temp
    N = temp

print(k)