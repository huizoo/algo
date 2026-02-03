import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
d0 = [(0, -1), (0, 1), (1, 0), (1, -1), (-1, -1), (-1, 0)]
d1 = [(0, -1), (0, 1), (1, 0), (1, 1), (-1, 0), (-1, 1)]
Sum = 0

for i in range(N):
    if i%2 == 0:
        for j in range(M):
            if arr[i][j] == '#':
                for di, dj in d0:
                    ni, nj = di+i, dj+j
                    if ni<0 or ni>=N or nj<0 or nj>=M: continue
                    if arr[ni][nj] == '.':
                        Sum += 1
    else:
        for j in range(M):
            if arr[i][j] == '#':
                for di, dj in d1:
                    ni, nj = di+i, dj+j
                    if ni<0 or ni>=N or nj<0 or nj>=M: continue
                    if arr[ni][nj] == '.':
                        Sum += 1

print(Sum)