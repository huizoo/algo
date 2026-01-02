import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(map(int, input().split()))
    cnt = 0
    for j in range(1, N-1):
        i = 0
        k = N-1
        while i < j and j < k:
            l = 2*arr[j]
            Sum = arr[i]+arr[k]
            if Sum == l:
                cnt += 1
                i += 1
                k -= 1
            elif Sum > l:
                k -= 1
            else:
                i += 1
            
    print(cnt)