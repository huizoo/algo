import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    Set = set(arr)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if 2*arr[j]-arr[i] in Set:
                cnt += 1
    print(cnt)