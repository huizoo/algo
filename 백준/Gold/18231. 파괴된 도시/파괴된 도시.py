import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


K = int(input())
fire = list(map(int, input().split()))
fire2 = set(fire)

candidate = set()

for now in fire:
    if now == 1:
        debug = 1
    flag = 0
    for nxt in arr[now]:
        if nxt not in fire2:
            flag = 1
            break
    if flag == 0:
        candidate.add(now)

fire3 = set()
for f in candidate:
    fire3.add(f)
    fire3.update(arr[f])

if fire2 == fire3:
    print(len(candidate))
    print(*candidate, sep=' ')
else:
    print(-1)