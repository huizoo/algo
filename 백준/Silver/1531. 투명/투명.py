import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0]*102 for _ in range(102)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    arr[y1][x1] += 1
    arr[y1][x2+1] -= 1
    arr[y2+1][x1] -= 1
    arr[y2+1][x2+1] += 1
    
for i in range(1, 101):
    for j in range(1, 101):
        arr[i][j] += arr[i][j-1]
for j in range(1, 101):
    for i in range(1, 101):
        arr[i][j] += arr[i-1][j]

cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] > M:
            cnt += 1

print(cnt)
