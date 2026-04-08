import sys
input = sys.stdin.readline

N, T = map(int, input().split())
dat = [0]*1001
for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        for i in range(S, E):
            dat[i] += 1

Sum = sum(dat[:T])
Max = Sum
ms, me = 0, T
for i in range(T, 1001):
    Sum += dat[i]-dat[i-T]
    if Max < Sum:
        Max = Sum
        ms, me = i-T+1, i+1

print(ms, me)
