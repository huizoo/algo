from collections import deque

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(maps):
    for map in maps:
        print(map)
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    visited2 = [[0]*m for _ in range(n)]
    S = E = L = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j, 0)
                visited[i][j] = 1
            elif maps[i][j] == 'E':
                E = (i, j, 0)
            elif maps[i][j] == 'L':
                L = (i, j, 0)
                visited2[i][j] = 1
    
    flag = 0
    
    q = deque([])
    q.append(S)
    while q:
        y, x, cnt = q.popleft()
        if maps[y][x] == 'L':
            answer += cnt
            flag = 1
            break
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=n or nx>=m:continue
            if maps[ny][nx] == 'X': continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1
            q.append((ny, nx, cnt+1))
    
    if flag == 0:
        return -1
    
    
    q2 = deque([])
    q2.append(L)
    while q2:
        y, x, cnt = q2.popleft()
        if maps[y][x] == 'E':
            answer += cnt
            flag = 0
            break
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=n or nx>=m:continue
            if maps[ny][nx] == 'X': continue
            if visited2[ny][nx] == 1: continue
            visited2[ny][nx] = 1
            q2.append((ny, nx, cnt+1))
    
    if flag == 1:
        return -1
    return answer