import sys
input = sys.stdin.readline

N = int(input())

Max = 10**6

arr = [0]*(Max+1)
arr[0] = arr[1] = 1
for i in range(2, 10**3):
    for j in range(i*i, Max+1, i):
        arr[j] = 1

prime = []
for i in range(2, Max+1):
    if arr[i] == 0:
        prime.append(i)

for _ in range(N):
    a, b = map(int, input().split())

    l, r = 0, len(prime)
    while l < r:
        mid = (l+r)//2
        if prime[mid] < a:
            l = mid + 1
        else:
            r = mid
    
    l2, r2 = 0, len(prime)
    while l2 < r2:
        mid2 = (l2+r2)//2
        if prime[mid2] <= b:
            l2 = mid2 + 1
        else:
            r2 = mid2
    
    if l > l2-1:
        print(-1)
    else:
        if (l2-l)%2 == 0:
            print(-1)
        else:
            print(prime[(l+l2-1)//2])