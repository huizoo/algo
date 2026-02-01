import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = []
for _ in range(N):
    M, *arr2 = map(int, input().split())
    arr.append(sorted(arr2))

def abc(lst, x):
    l, r = 0, len(lst)
    while l < r:
        mid = (l+r)//2
        if lst[mid] > x:
            r = mid
        else:
            l = mid+1
    return l

for _ in range(Q):
    A, B, C, j = map(int, input().split())
    lo = min(arr[A-1][0], arr[B-1][0], arr[C-1][0])
    hi = max(arr[A-1][-1], arr[B-1][-1], arr[C-1][-1])

    while lo<hi:
        mid = (lo+hi)//2
        cnt = abc(arr[A-1], mid) + abc(arr[B-1], mid) + abc(arr[C-1], mid)
        if cnt >= j:
            hi = mid
        else:
            lo = mid+1

    print(lo)