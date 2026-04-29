from collections import deque

def solution(m, n, h, w, drops):
    INF = 10**9
    
    arr = [[INF] * n for _ in range(m)]
    
    for idx, (i, j) in enumerate(drops, start=1):
        arr[i][j] = idx
    
    row = [[0] * (n-w+1) for _ in range(m)]
    
    for i in range(m):
        q = deque()
        
        for j in range(n):
            while q and arr[i][q[-1]] >= arr[i][j]:
                q.pop()
            q.append(j)
            
            if q[0] <= j-w:
                q.popleft()
            
            if j >= w-1:
                row[i][j-w+1] = arr[i][q[0]]

    score = [[0] * (n-w+1) for _ in range(m-h+1)]
    
    for j in range(n-w+1):
        q = deque()
        
        for i in range(m):
            while q and row[q[-1]][j] >= row[i][j]:
                q.pop()
            q.append(i)
            
            if q[0] <= i-h:
                q.popleft()
            
            if i >= h-1:
                x = i-h+1
                score[x][j] = row[q[0]][j]
    
    best = -1
    answer = [0, 0]
    
    for i in range(m-h+1):
        for j in range(n-w+1):
            if score[i][j] > best:
                best = score[i][j]
                answer = [i, j]
    
    return answer