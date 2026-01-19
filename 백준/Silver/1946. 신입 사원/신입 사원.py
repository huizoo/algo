import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0]*(N+1)
    for _ in range(1, N+1):
        a, b = map(int, input().split())
        arr[a] = b
    cnt = 0
    best = 1e9
    for i in range(1, N+1):
        if arr[i] < best:
            best = arr[i]
            cnt += 1
        
    print(cnt)