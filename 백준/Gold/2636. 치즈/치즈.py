import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cheeze = sum(sum(row) for row in arr)
if cheeze == 0:
    print(0, 0, sep='\n')
    sys.exit()
for k in range(1, 101):
    air = [[0]*M for _ in range(N)]
    air[0][0] = 1
    stack = [(0, 0)]
    melt = set()
    while stack:
        y, x = stack.pop()
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if arr[ny][nx] == 1:
                melt.add((ny, nx))
                continue
            if air[ny][nx] == 1: continue
            air[ny][nx] = 1
            stack.append((ny, nx))

    l = len(melt)
    if cheeze - l == 0:
        print(k, l, sep='\n')
        break
    else:
        cheeze -= l
        for y, x in melt:
            arr[y][x] = 0
        
