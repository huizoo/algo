import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip()))
arr2 = tuple(map(int, input().rstrip()))
arr3 = arr[:]
arr3[0] = 1 - arr3[0]
arr3[1] = 1 - arr3[1]

cnt1 = 0
cnt2 = 1
for i in range(1, N):
    if arr[i-1] != arr2[i-1]:
        cnt1 += 1
        arr[i-1] = 1 - arr[i-1]
        arr[i] = 1 - arr[i]
        if i+1 < N:
            arr[i+1] = 1 - arr[i+1]

    if arr3[i-1] != arr2[i-1]:
        cnt2 += 1
        arr3[i-1] = 1 - arr3[i-1]
        arr3[i] = 1 - arr3[i]
        if i+1 < N:
            arr3[i+1] = 1 - arr3[i+1]

if arr[-1] == arr2[-1]:
    if arr3[-1] == arr2[-1]:
        print(min(cnt1, cnt2))
    else:
        print(cnt1)
elif arr3[-1] == arr2[-1]:
    print(cnt2)
else:
    print(-1)

