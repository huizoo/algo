import sys
input = sys.stdin.readline

arr = [[0]*30 for _ in range(30)]

for i in range(15):
    arr[i][15] = 15
    arr[29-i][15] = 15**3
    arr[15][i] = 1
    arr[15][29-i] = 15**2

arr[15][15] = 0

for row in arr:
    print(*row)