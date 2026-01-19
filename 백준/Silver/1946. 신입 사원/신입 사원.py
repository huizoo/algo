import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort()
    cnt = 0
    best = 1e9
    for a, b in arr:
        if b < best:
            best = b
            cnt += 1
        
    print(cnt)