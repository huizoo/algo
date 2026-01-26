import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
P = sorted(map(int, input().split()))
arr = [0]*N
Sum = 0
for i in range(N):
    Sum += P[i]
    arr[i] = Sum
s, e = P[0], P[-1]
for _ in range(Q):
    X = int(input())
    if X<=s:
        print(arr[N-1]-X*N); continue
    elif X>=e:
        print(X*N-arr[N-1]); continue
    start, end = 0, N-1
    while start < end:
        mid = (start+end)//2
        if P[mid] <= X:
            start = mid+1
        else:
            end = mid

    print(X*(2*start-N)+arr[N-1]-2*arr[start-1])

