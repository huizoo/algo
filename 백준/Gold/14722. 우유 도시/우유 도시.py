import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0)]
N = int(input())
arr = [[0]*(N+1)]
for _ in range(N):
    arr.append([0]+list(map(int, input().split())))

arr2 = [[-1]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        now = arr[i][j]
        top = arr2[i-1][j]
        left = arr2[i][j-1]
        if top < left:
            if left%3 == 2 and now == 0:
                arr2[i][j] = left+1
            elif now - left%3 == 1:
                arr2[i][j] = left+1
            else:
                arr2[i][j] = left
        else:
            if top%3 == 2 and now == 0:
                arr2[i][j] = top+1
            elif now - top%3 == 1:
                arr2[i][j] = top+1
            else:
                arr2[i][j] = top

print(arr2[N][N]+1)