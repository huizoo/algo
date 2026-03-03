import sys
input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr2 = [[] for _ in range(1000001)]
for i, (a, b, c) in enumerate(arr):
    arr2[a].append(i)
    arr2[b].append(i)
    arr2[c].append(i)

visited = [False]*N
cnt = 0

def abc(x, y):
    for nxt in arr2[x]:
        if visited[nxt]: continue
        if nxt < y: continue
        visited[nxt] = True
        stack.append(nxt)

for i in range(N):
    if visited[i]: continue
    visited[i] = True
    cnt += 1
    stack = [i]
    while stack:
        now = stack.pop()
        a, b, c = arr[now]
        abc(a, now)
        abc(b, now)
        abc(c, now)

print(cnt)