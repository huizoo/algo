def solution(points, routes):
    def move(*trc):
        nonlocal time
        if trc in visited:
            danger.add(trc)
        else:
            visited.add(trc)
        time += 1
    
    
    m = len(routes[0])
    visited = set()
    danger = set()
    
    for route in routes:
        time = 0
        
        sr, sc = points[route[0]-1]
        move(time, sr, sc)
        
        for i in range(m-1):
            r, c = points[route[i]-1]
            nr, nc = points[route[i+1]-1]
            
            if r < nr:
                for rr in range(r+1, nr+1):
                    move(time, rr, c)
            else:
                for rr in range(r-1, nr-1, -1):
                    move(time, rr, c)
            
            if c < nc:
                for cc in range(c+1, nc+1):
                    move(time, nr, cc)
            else:
                for cc in range(c-1, nc-1, -1):
                    move(time, nr, cc)
                
    return len(danger)