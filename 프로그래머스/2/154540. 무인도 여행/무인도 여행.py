from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(maps):
    answer = []
    l = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(l)]
    for i in range(l):
        for j in range(m):
            if maps[i][j] == 'X': continue
            if visited[i][j] == 1: continue
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            cnt = 0
            while q:
                y, x = q.popleft()
                cnt += int(maps[y][x])
                for dy, dx in d:
                    ny, nx = y+dy, x+dx
                    if ny<0 or nx<0 or ny>=l or nx>=m: continue
                    if maps[ny][nx] == 'X': continue
                    if visited[ny][nx] == 1: continue
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                    
            answer.append(cnt)
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer