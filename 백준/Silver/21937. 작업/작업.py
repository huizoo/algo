import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

stack = []
stack.append(int(input()))
Set = set()
while stack:
    now = stack.pop()
    for nxt in arr[now]:
        if nxt in Set:
            continue
        stack.append(nxt)
        Set.add(nxt)

print(len(Set))