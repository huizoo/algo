def solution(wallpaper):
    lux = luy = 50; rdx = rdy = -1
    for i, row in enumerate(wallpaper):
        for j, v in enumerate(row):
            if v == '#':
                lux = min(lux, j)
                luy = min(luy, i)
                rdx = max(rdx, j+1)
                rdy = max(rdy, i+1)                
            
    return [luy, lux, rdy, rdx]