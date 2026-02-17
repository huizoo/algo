from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [-1]*100001
par = [-1]*100001
q = deque([N])
visited[N] = 0

while q:
    now = q.popleft()
    if now == K:
        break
    for nxt in [now-1, now+1, now*2]:
        if 0<=nxt<=100000 and visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            par[nxt] = now
            q.append(nxt)

print(visited[K])

ans = []
while K != -1:
    ans.append(K)
    K = par[K]

print(*ans[::-1])