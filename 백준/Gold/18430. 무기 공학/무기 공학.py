import sys
input = sys.stdin.readline
# 상 좌 하 우 순서
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bhc(y, x):
    return 0<=y<N and 0<=x<M and not visited[y][x]

def abc(y, x, Sum):
    global Max
    if x >= M:
        x = 0
        y += 1
    if y == N:
        if Max < Sum:
            Max = Sum
        return
    if not visited[y][x]:
        visited[y][x] = True

        if bhc(y-1, x) and bhc(y, x-1):
            visited[y-1][x] = True
            visited[y][x-1] = True
            abc(y, x+1, Sum+2*arr[y][x]+arr[y-1][x]+arr[y][x-1])
            visited[y-1][x] = False
            visited[y][x-1] = False

        if bhc(y-1, x) and bhc(y, x+1):
            visited[y-1][x] = True
            visited[y][x+1] = True
            abc(y, x+2, Sum+2*arr[y][x]+arr[y-1][x]+arr[y][x+1])
            visited[y-1][x] = False
            visited[y][x+1] = False

        if bhc(y+1, x) and bhc(y, x+1):
            visited[y+1][x] = True
            visited[y][x+1] = True
            abc(y, x+2, Sum+2*arr[y][x]+arr[y+1][x]+arr[y][x+1])
            visited[y+1][x] = False
            visited[y][x+1] = False

        if bhc(y+1, x) and bhc(y, x-1):
            visited[y+1][x] = True
            visited[y][x-1] = True
            abc(y, x+1, Sum+2*arr[y][x]+arr[y+1][x]+arr[y][x-1])
            visited[y+1][x] = False
            visited[y][x-1] = False

        visited[y][x] = False
    
    abc(y, x+1, Sum)    

N, M = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
if N == 1 or M == 1:
    print(0)
    sys.exit()

Max = 0
visited = [[False]*M for _ in range(N)]

abc(0, 0, 0)
    
print(Max)