import sys
input = sys.stdin.readline

def solve(N):
    INF = 10**21
    minx, maxx = -INF, INF
    miny, maxy = -INF, INF

    parity = None

    for _ in range(N):
        a, b, c = map(int, input().split())

        minx = max(minx, a + b - c)
        maxx = min(maxx, a + b + c)
        miny = max(miny, a - b - c)
        maxy = min(maxy, a - b + c)

        p = (a + b + c) & 1
        if parity is None:
            parity = p
        elif parity != p:
            print('NO')
            return

    if minx > maxx or miny > maxy:
        print('NO')
        return

    x = minx if (minx & 1) == parity else minx + 1
    y = miny if (miny & 1) == parity else miny + 1

    if x > maxx or y > maxy:
        print('NO')
        return

    a = (x + y) // 2
    b = (x - y) // 2
    print(a, b)

solve(int(input()))
