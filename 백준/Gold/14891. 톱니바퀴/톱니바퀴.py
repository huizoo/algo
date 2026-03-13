import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(4)]
idx = [0]*4

K = int(input())

for _ in range(K):
    a, b = map(int, input().split())
    a -= 1

    arr2 = [0]*4
    arr2[a] = b

    for i in range(a, 0, -1):
        r = arr[i][(idx[i]+6)%8]
        l = arr[i-1][(idx[i-1]+2)%8]
        if r != l:
            arr2[i-1] = -arr2[i]
        else:
            break

    for i in range(a, 3):
        r = arr[i][(idx[i]+2)%8]
        l = arr[i+1][(idx[i+1]+6)%8]
        if r != l:
            arr2[i+1] = -arr2[i]
        else:
            break

    for i in range(4):
        if arr2[i] == 1:
            idx[i] = (idx[i]-1)%8
        elif arr2[i] == -1:
            idx[i] = (idx[i]+1)%8

ans = 0
for i in range(4):
    if arr[i][idx[i]] == '1':
        ans += 1<<i

print(ans)