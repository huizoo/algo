from collections import deque
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def can_remove(lst, y, x, n, m, arr):
    global d
    q = deque()
    q.append((y, x))
    visited = [[0]*m for _ in range(n)]
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        if yy in [0, n-1] or xx in [0, m-1]:
            return 1
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or ny>=n or nx<0 or nx>=m: continue
            if visited[ny][nx] == 1: continue
            if lst[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny, nx))
    return 0

def solution(storage, requests):
    global d
    n = len(storage)
    m = len(storage[0])
    cnt = 0
    for i in range(n):
        storage[i] = list(storage[i])
        
        
    def sync(y, x):
        global d
        nonlocal storage, arr, n, m
        q = deque()
        q.append((y, x))
        visited = [[0]*m for _ in range(n)]
        visited[y][x] = 1
        while q:
            yy, xx = q.popleft()
            storage[yy][xx] = 0
            arr[yy][xx] = 2
            for dy, dx in d:
                ny, nx = yy+dy, xx+dx
                if ny<0 or ny>=n or nx<0 or nx>=m: continue
                if visited[ny][nx] == 1: continue
                arr[ny][nx] = 1
                if storage[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    
    arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1:
                arr[i][j] = 1
            elif j == 0 or j == m-1:
                arr[i][j] = 1          
    
    for request in requests:
        c = []
        if len(request) == 1:
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == request and arr[i][j] == 1:
                        c.append((i, j))
                        
            for cy, cx in c:
                cnt += 1
                storage[cy][cx] = 0
                arr[cy][cx] = 2
                for dy, dx in d:
                    ny, nx = cy+dy, cx+dx
                    if ny<0 or ny>=n or nx<0 or nx>=m: continue
                    arr[ny][nx] = 1
                sync(cy, cx)
                    
        else:
            r = request[0]
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == r:
                        c.append((i, j))
            
            a = 1
            for cy, cx in c:
                storage[cy][cx] = 0
                cnt += 1
                print(a)
                a += 1
                if can_remove(storage, cy, cx, n, m, arr):
                    sync(cy, cx)
                    
                    
    return n*m-cnt