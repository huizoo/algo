import sys
input = sys.stdin.readline

N = int(input())
arr = tuple(map(int, input().split()))
cnt = 0
idx = 0
l = 1
flag = 0
while idx+2*l-1 < N:
    flag = 0
    if arr[idx] == arr[idx+2*l-1]:
        for i in range(1, l):
            if arr[idx+i] != arr[idx+2*l-1-i]:
                l += 1
                break
        else:
            cnt += 1
            idx += 2*l
            l = 1
            flag = 1
    else:
        l += 1

print(cnt if flag else -1)


