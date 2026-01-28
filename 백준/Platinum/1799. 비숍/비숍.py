import sys
input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

dia1 = 0
dia2 = 0
Max1 = 0
Max2 = 0
def dfs(y, x, Sum, c):
    global Max1, Max2, dia1, dia2
    if x >= N:
        y += 1
        x = (c+y)%2
    if y == N:
        if c:
            if Max1 < Sum:
                Max1 = Sum
        else:
            if Max2 < Sum:
                Max2 = Sum
        return
    if arr[y][x] and not 1<<(y+x)&dia1 and not 1<<(N-y+x)&dia2:
        dia1 |= 1<<(y+x)
        dia2 |= 1<<(N-y+x)
        dfs(y, x+2, Sum+1, c)
        dia1 ^= 1<<(y+x)
        dia2 ^= 1<<(N-y+x)
    
    dfs(y, x+2, Sum, c)

dfs(0, 0, 0, 0)
dfs(0, 1, 0, 1)

print(Max1+Max2)