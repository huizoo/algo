import sys
input = sys.stdin.readline

N, P = map(int, input().split())
P -= 1

A = list(map(int, input().split()))
B = list(map(int, input().split()))

roads = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    roads[u].append(v)
    roads[v].append(u)

Ans = [0] * N
parent = [-1] * N

stack = [(P, 0)]
parent[P] = P

while stack:
    now, state = stack.pop()

    if state == 0:
        stack.append((now, 1))
        for nxt in roads[now]:
            if nxt != parent[now]:
                parent[nxt] = now
                stack.append((nxt, 0))
    else:
        need = B[now] - A[now]
        for nxt in roads[now]:
            if nxt != parent[now]:
                need += Ans[nxt]
        Ans[now] = max(0, need)

print(Ans[P])
