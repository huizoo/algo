import sys
input = sys.stdin.readline

N, P = map(int, input().split())

arr = [[] for _ in range(7)]
cnt = 0

def abc(x, y):
    global cnt
    while arr[x] and arr[x][-1] > y:
        arr[x].pop()
        cnt += 1
    if arr[x] and arr[x][-1] == y:
        return
    arr[x].append(y)
    cnt += 1    

for _ in range(N):
    l, p = map(int, input().split())
    abc(l, p)

print(cnt)