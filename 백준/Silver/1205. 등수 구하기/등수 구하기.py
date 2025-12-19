import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())

if N > 0:
    rank = list(map(int, input().split()))
    rank.sort()

    if N == P and M <= rank[0]:
        print(-1)
    else:
        x = sum(1 for x in rank if x > M)
        print(x + 1)
else:
    print(1)