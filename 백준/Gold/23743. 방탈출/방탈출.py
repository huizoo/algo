import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]

for idx, t in enumerate(map(int, input().split())):
    edges.append((0, idx+1, t))

edges.sort(key=lambda x: x[2])

par = list(range(N+1))

def find(x):
    if par[x] != x:
       par[x] = find(par[x])
    return par[x]

def union(a, b):
    bossA, bossB = find(a), find(b)
    if bossA == bossB:
        return False
    par[bossA] = bossB
    return True


ans = 0
cnt = 0

for u, v, cost in edges:
    if union(u, v):
        ans += cost
        cnt += 1
        if cnt == N:
            break

print(ans)

