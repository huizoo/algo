import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))

visited = [0]*(N+1)
P = [0]*(N+1)

for i in range(1, N+1):
    if visited[i]:
        continue

    cycle = []
    now = i

    while not visited[now]:
        visited[now] = 1
        cycle.append(now)
        now = D[now]

    L = len(cycle)
    move = K % L

    for j in range(L):
        P[cycle[j]] = S[cycle[(j-move)%L]]

print(*P[1:])