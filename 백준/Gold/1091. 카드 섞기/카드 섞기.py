import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = [i for i in range(N)]

cnt = 0
visited = set()
visited.add(''.join(map(str, cards)))
while any(P[cards[i]] != i % 3 for i in range(N)):
    cnt += 1
    nxt = [-1]*N
    for i in range(N):
        nxt[S[i]] = cards[i]
    cards = nxt
    check = ''.join(map(str, cards))
    if check in visited:
        print(-1)
        sys.exit()
    visited.add(check)

print(cnt)