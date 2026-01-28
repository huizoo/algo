import sys
input = sys.stdin.readline
# 상 좌 하 우 순서
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def abc(n, Sum):
    global Max
    if n == nm:
        if Max < Sum:
            Max = Sum
        return
    y, x = seq[n]
    if not visited[y][x]:
        check = [False]*4
        for k in range(4):
            dy, dx = d[k]
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if visited[ny][nx]: continue
            check[k] = True
        if check[0]:
            if check[1]:
                visited[y][x] = True
                visited[y-1][x] = True
                visited[y][x-1] = True
                abc(n+1, Sum+2*arr[y][x]+arr[y-1][x]+arr[y][x-1])
                visited[y][x] = False
                visited[y-1][x] = False
                visited[y][x-1] = False
            if check[3]:
                visited[y][x] = True
                visited[y-1][x] = True
                visited[y][x+1] = True
                abc(n+2, Sum+2*(arr[y][x])+arr[y-1][x]+arr[y][x+1])
                visited[y][x] = False
                visited[y-1][x] = False
                visited[y][x+1] = False
        if check[2]:
            if check[1]:
                visited[y][x] = True
                visited[y+1][x] = True
                visited[y][x-1] = True
                abc(n+1, Sum+2*arr[y][x]+arr[y+1][x]+arr[y][x-1])
                visited[y][x] = False
                visited[y+1][x] = False
                visited[y][x-1] = False
            if check[3]:
                visited[y][x] = True
                visited[y+1][x] = True
                visited[y][x+1] = True
                abc(n+2, Sum+2*arr[y][x]+arr[y+1][x]+arr[y][x+1])
                visited[y][x] = False
                visited[y+1][x] = False
                visited[y][x+1] = False

    abc(n+1, Sum)    

N, M = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
if N == 1 or M == 1:
    print(0)
    sys.exit()


seq = []
for i in range(N):
    for j in range(M):
        seq.append((i, j))

Max = 0
nm = N*M
visited = [[False]*M for _ in range(N)]

abc(0, 0)
    
print(Max)