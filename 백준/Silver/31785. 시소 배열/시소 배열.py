import sys
input = sys.stdin.readline

Q = int(input())
A = [0]*Q
l = r = 0
Sum = [0]*(Q+1)
for _ in range(Q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        x = arr[1]
        A[r] = x
        Sum[r+1] = Sum[r] + x
        r += 1
    else:
        mid = (r+l)//2
        Sum_mid = Sum[(r+l)//2]
        if Sum_mid - Sum[l] <= Sum[r] - Sum_mid:
            print(Sum_mid - Sum[l])
            l = mid
        else:
            print(Sum[r] - Sum_mid)
            r = mid

print(*A[l:r])