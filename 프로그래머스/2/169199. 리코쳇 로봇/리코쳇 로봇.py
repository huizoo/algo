from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(board):
    n, m = len(board), len(board[0])
    gy = gx = ry = rx = -1
    for i, row in enumerate(board):
        for j, v in enumerate(row):
            if v == 'G':
                gy, gx = i, j
            elif v == 'R':
                ry, rx = i, j
    
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((ry, rx, 0))   
    visited[ry][rx] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == gy and x == gx:
            return cnt
        
        for dy, dx in d:
            ny, nx = y, x
            while 0<=(ny2:= ny+dy)<n and 0<=(nx2:= nx+dx)<m:
                if board[ny2][nx2] == 'D':
                    break
                ny, nx = ny2, nx2
                
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((ny, nx, cnt+1))
    
    return -1