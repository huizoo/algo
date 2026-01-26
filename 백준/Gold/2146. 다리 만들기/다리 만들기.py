import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
sea = 2
stack2 = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            stack = [(i, j)]
            arr[i][j] = -1
            while stack:
                y, x = stack.pop()
                for dy, dx in d:
                    ny, nx = dy+y, dx+x
                    if ny<0 or nx<0 or ny>=N or nx>=N: continue
                    now = arr[ny][nx]
                    if now == 1:
                        arr[ny][nx] = -1
                        stack.append((ny, nx))
                    elif now == 0:
                        arr[ny][nx] = sea
                        stack2.append((ny, nx))
                    elif 1 < now < sea:
                        print(1)
                        sys.exit()
                        
            sea += 1

dist = 2
temp = 0
while stack2:
    stack3 = stack2
    stack2 = []
    for y, x in stack3:
        now = arr[y][x]
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            nxt = arr[ny][nx]
            if nxt == 0:
                arr[ny][nx] = now
                stack2.append((ny, nx))
            elif 1 < nxt < now:
                temp = dist+1
            elif now < nxt:
                print(dist)
                sys.exit()
    dist += 2
    if temp:
        print(temp)
        sys.exit()
