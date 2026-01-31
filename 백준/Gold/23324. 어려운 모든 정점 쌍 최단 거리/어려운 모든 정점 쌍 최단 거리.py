import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[] for _ in range(N+1)]
a, b = None, None
for i in range(1, M+1):
    u, v = map(int, input().split())
    if i == K:
        a, b = u, v
        continue
    arr[u].append(v)
    arr[v].append(u)

stack = [a]
visited = [0]*(N+1)
visited[a] = 1
cnt = 1
while stack:
    now = stack.pop()
    for nxt in arr[now]:
        if visited[nxt]: continue
        visited[nxt] = 1
        stack.append(nxt)
        cnt += 1

if cnt == N:
    print(0)
    sys.exit()

visited = [0]*(N+1)
visited[b] = 1
cnt1 = 1
stack = [b]
while stack:
    now = stack.pop()
    for nxt in arr[now]:
        if visited[nxt]: continue
        visited[nxt] = 1
        stack.append(nxt)
        cnt1 += 1

print(cnt*cnt1)
