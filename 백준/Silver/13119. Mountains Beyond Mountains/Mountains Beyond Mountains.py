import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
H = tuple(map(int, input().split()))
# '#', '*', '|'
arr = [['.']*M for _ in range(N)]
for j in range(M):
    for i in range(H[j]):
        arr[i][j] = '#'
for j in range(M):
    if arr[X-1][j] == '.':
        arr[X-1][j] = '-'
    else:
        arr[X-1][j] = '*'
for j in range(2, M, 3):
    if H[j] < X:
        for i in range(H[j], X-1):
            arr[i][j] = '|'

for row in arr[::-1]:
    print(*row, sep='')


