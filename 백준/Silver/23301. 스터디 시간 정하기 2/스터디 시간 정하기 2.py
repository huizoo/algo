import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = [0]*1001
END = 0
for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        arr[S] += 1
        arr[E] -= 1
        if END < E:
            END = E

cnt = 0
prefix = [0]*1001
for i in range(END):
    prefix[i] += cnt
    prefix[i] += prefix[i-1]
    cnt += arr[i]

s, e = 0, T
Max = 0
for i in range(T, END):
    Sum = prefix[i] - prefix[i-T]
    if Max < Sum:
        Max = Sum
        s, e = i-T, i

print(s, e)