import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
if N > 0:
    rank = list(map(int, input().split()))
    rank.sort(reverse=True)

    if N == P and M <= rank[-1]:
        print(-1)
    else:
        higher = 0
        for x in rank:
            if x > M:
                higher += 1
            else:
                break
        print(higher + 1)
else:
    print(1)
