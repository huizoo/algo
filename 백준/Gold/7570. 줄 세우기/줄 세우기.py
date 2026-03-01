import sys
input = sys.stdin.readline
N = int(input())
visited = [0]*(N+1)
for x in map(int, input().split()):
    visited[x] = visited[x-1] + 1
print(N - max(visited))