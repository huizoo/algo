import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
num = 1
while num**2 <= N:
    cnt += 1
    num += 1

print(cnt)