import sys
input = sys.stdin.readline
# 상 좌 하 우 순서
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def abc(n, Sum):
    global Max
    if Sum == 998:
        debug = 1
    if n == nm:
        if Max < Sum:
            Max = Sum
        return
    y, x = seq[n]
    if not visited[y][x]:
        for k in range(4):
            dy, dx = d[k-1]
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if visited[ny][nx]: continue
            dy1, dx1 = d[k]
            ny1, nx1 = dy1+y, dx1+x
            if ny1<0 or nx1<0 or ny1>=N or nx1>=M: continue
            if visited[ny1][nx1]: continue
            visited[y][x] = True
            visited[ny][nx] = True
            visited[ny1][nx1] = True
            abc(n+1, Sum+2*arr[y][x]+arr[ny][nx]+arr[ny1][nx1])
            visited[y][x] = False
            visited[ny][nx] = False
            visited[ny1][nx1] = False
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
for i in range(2*N):
    visited = [[False]*M for _ in range(N)]
    abc(i, 0)
    
print(Max)