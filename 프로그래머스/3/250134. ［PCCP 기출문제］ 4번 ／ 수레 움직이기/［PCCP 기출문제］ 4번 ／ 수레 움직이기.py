from collections import deque

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(maze):
    sry = srx = sby = sbx = ery = erx = eby = ebx = -1
    n, m = len(maze), len(maze[0])
    for i, row in enumerate(maze):
        for j, v in enumerate(row):
            if v == 1:
                sry, srx = i, j
            elif v == 2:
                sby, sbx = i, j
            elif v == 3:
                ery, erx = i, j
            elif v == 4:
                eby, ebx = i, j
    
    q = deque()
    q.append((sry, srx, sby, sbx, 1<<(m*sry+srx), 1<<(m*sby+sbx), 0))
    while q:
        ry, rx, by, bx, r_visited, b_visited, cnt = q.popleft()
        if ry == ery and rx == erx and by == eby and bx == ebx:
            return cnt
        
        
        r_nxt = []
        b_nxt = []
        
        if ry == ery and rx == erx:
            r_nxt.append((ry, rx, r_visited))
        else:       
            for dy, dx in d:
                nry, nrx = dy + ry, dx + rx
                if nry<0 or nrx<0 or nry>=n or nrx>=m: continue
                if maze[nry][nrx] == 5: continue
                r_bit = 1<<(m*nry+nrx)
                if r_visited & r_bit: continue
                r_nxt.append((nry, nrx, r_visited | r_bit))
        
        if by == eby and bx == ebx:
            b_nxt.append((by, bx, b_visited))
        else:
            for dy, dx in d:
                nby, nbx = dy + by, dx + bx
                if nby<0 or nbx<0 or nby>=n or nbx>=m: continue
                if maze[nby][nbx] == 5: continue
                b_bit = 1<<(m*nby+nbx)
                if b_visited & b_bit: continue
                b_nxt.append((nby, nbx, b_visited | b_bit))
        
        for nry, nrx, nr_visited in r_nxt:
            for nby, nbx, nb_visited in b_nxt:
                if nry == nby and nrx == nbx: continue
                if nry == by and nrx == bx and nby == ry and nbx == rx: continue
                q.append((nry, nrx, nby, nbx, nr_visited, nb_visited, cnt+1))
                

    return 0