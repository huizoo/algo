def solution(m, n, startX, startY, balls):
    answer = []
    for bx, by in balls:
        candidate = []
        # left, right, over, under
        if startY != by or bx > startX:
            lx, ly = -bx, by
            candidate.append((startX-lx)**2+abs(startY-ly)**2)
        if startY != by or bx < startX:
            rx, ry = 2*m-bx, by
            candidate.append((rx-startX)**2+abs(startY-ry)**2)
        if startX != bx or by < startY:
            ox, oy = bx, 2*n-by
            candidate.append(abs(startX-ox)**2+(oy-startY)**2)
        if startX != bx or by > startY:
            ux, uy = bx, -by
            candidate.append(abs(startX-ux)**2+(startY-uy)**2)
            
        answer.append(min(candidate))
    
    return answer