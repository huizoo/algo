import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        arr[i][j] += min(arr[i-1][j-1], arr[i-1][j-2])

print(min(arr[N-1]))