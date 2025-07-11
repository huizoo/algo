import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cycle = False

def dfs(y, x):
    global cycle
    if cycle:
        return 0
    if arr[y][x] == 'H':
        return 0
    if dp[y][x]:
        return dp[y][x]
    
    num = int(arr[y][x])
    visited[y][x] = 1
    cnt = 0
    
    for dy, dx in d:
        ny, nx = y+num*dy, x+num*dx
        if ny<0 or nx<0 or ny>=N or nx>=M: continue
        if arr[ny][nx] == 'H': continue
        if visited[ny][nx] == 1:
            cycle = True
            return 0
        cnt = max(cnt, dfs(ny, nx) + 1)
    visited[y][x] = 0
    dp[y][x] = cnt
    return dp[y][x]

res = dfs(0, 0) + 1
if cycle:
    print(-1)
else:
    print(res)