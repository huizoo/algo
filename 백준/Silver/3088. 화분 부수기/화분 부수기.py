import sys
input = sys.stdin.readline
N = int(input())
visited = [False]*1000001
cnt = 0
for _ in range(N):
    a, b, c =  map(int, input().split())
    if not visited[a] | visited[b] | visited[c]:
        cnt += 1
    visited[a] = visited[b] = visited[c] = True
print(cnt)