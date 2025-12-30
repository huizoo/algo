import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L, R = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            y, x = i, j
            break
    else:
        continue
    break

cnt = 1
q = [(y, x, L, R)]

while q:
    temp = []
    while q:
        yy, xx, l, r = q.pop()
        for ny in range(yy-1, -1, -1):
            if arr[ny][xx] != 0: break
            arr[ny][xx] = 1
            cnt += 1
            q.append((ny, xx, l, r))
        for ny in range(yy+1, N):
            if arr[ny][xx] != 0: break
            arr[ny][xx] = 1
            cnt += 1
            q.append((ny, xx, l, r))
        if l > 0:
            nx = xx-1
            if nx >= 0 and arr[yy][nx] == 0:
                arr[yy][nx] = 1
                cnt += 1
                temp.append((yy, nx, l-1, r))
        if r > 0:
            nx = xx+1
            if nx < M and arr[yy][nx] == 0: 
                arr[yy][nx] = 1
                cnt += 1
                temp.append((yy, nx, l, r-1))

    q = temp      

print(cnt)