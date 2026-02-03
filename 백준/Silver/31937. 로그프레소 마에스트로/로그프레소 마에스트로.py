import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
virus = set(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(M)]
arr.sort()

for v in virus:
    Set = {v}
    for t, a, b in arr:
        if a in Set:
            Set.add(b)
    if Set == virus:
        print(v)
        sys.exit()