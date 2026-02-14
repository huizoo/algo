import sys
input = sys.stdin.readline
k = int(input())
arr = list(map(int, input().split()))
n = (1<<k+1)-2

arr2 = [0]*n
for i in range(k, 0, -1):
    for j in range(0, 1<<i, 2):
        x = (1<<i)-2
        r2 = 0
        l = arr[x+j]
        r = arr[x+j+1]
        if i != k:
            l += arr2[2*(x+j)+2]
            r += arr2[2*(x+j+1)+2]
        if l < r:
            arr[x+j] += r-l
            arr2[x+j] = r
            arr2[x+j+1] = r
        else:
            arr[x+j+1] += l-r
            arr2[x+j] = l
            arr2[x+j+1] = l

print(sum(arr))