import sys
input = sys.stdin.readline

def findboss(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x

def union(a, b, flag):
    bossA, bossB = findboss(a), findboss(b)
    if bossA == bossB:
        return 1
    if flag:
        global ans
        ans += cnt[bossA] * cnt[bossB]

    if rank[bossA] < rank[bossB]:
        par[bossA] = bossB
        cnt[bossB] += cnt[bossA]
    else:
        par[bossB] = bossA
        cnt[bossA] += cnt[bossB]
        if rank[bossB] == rank[bossA]:
            rank[bossA] += 1
    return 0

N, M, Q = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(M)]
arr2 = [1]*(M)
for _ in range(Q):
    arr2[int(input())-1] = 0

rank = [0]*(N+1)
par = [i for i in range(N+1)]
cnt = [1]*(N+1)
nxt = []
ans = 0

for i in range(M):
    if arr2[i]:
        union(*arr[i], 0)
    else:
        nxt.append(i)


for i in reversed(nxt):
    union(*arr[i], 1)

print(ans)
