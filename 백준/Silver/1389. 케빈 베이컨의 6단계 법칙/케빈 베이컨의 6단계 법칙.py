# 이강호 - 천민호 - 최백준 - 김선영 - 김도현 - 민세희
# 1 3
# 1 4
# 2 3
# 3 4
# 4 5
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
arr2 = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

Min = [1e9, 1e9]
for i in range(1, N+1):  
    q = deque()
    q.append([i, 0])
    visited = [0]*(N+1)
    visited[i] = 1
    cntt = 0
    while q:
        now, cnt = q.popleft()
        cntt += cnt
        for nxt in arr[now]:
            if visited[nxt] == 1: continue
            visited[nxt] = 1
            q.append([nxt, cnt + 1])
    if Min[0] > cntt:
        Min = [cntt, i]

print(Min[1])