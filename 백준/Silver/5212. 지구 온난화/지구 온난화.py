import sys
input = sys.stdin.readline

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

R, C = map(int, input().split())
maps = [input().rstrip() for _ in range(R)]

lands = set()
x1 = y1 = 10
x2 = y2 = -1
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':
            cnt = 0
            for di, dj in d:
                ni, nj = di+i, dj+j
                if ni<0 or nj<0 or ni>=R or nj>=C:
                    cnt += 1; continue
                if maps[ni][nj] == '.':
                    cnt += 1
            
            if cnt < 3:
                lands.add((i, j))
                x1 = min(x1, j)
                y1 = min(y1, i)
                x2 = max(x2, j)
                y2 = max(y2, i)


for i in range(y1, y2+1):
    for j in range(x1, x2+1):
        if (i, j) in lands:
            print('X', end='')
        else:
            print('.', end='')
    print()