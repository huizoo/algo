import sys
input = sys.stdin.readline

N, P = map(int, input().split())

arr = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    l, p = map(int, input().split())
    while arr[l] and arr[l][-1] > p:
        arr[l].pop()
        cnt += 1
    if arr[l] and arr[l][-1] == p:
        continue
    arr[l].append(p)
    cnt += 1    

print(cnt)