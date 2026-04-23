def solution(park, routes):
    y, x = -1, -1
    N, M = len(park), len(park[0])
    for i, row in enumerate(park):
        for j, v in enumerate(row):
            if v == 'S':
                y, x = i, j
                break
    rotated_park = list(zip(*park))
    for route in routes:
        dir, mv = route.split()
        mv = int(mv)
        if dir == 'E':
            if x + mv < M and park[y][x+1:x+mv+1].count('X') == 0:
                x += mv
        elif dir == 'W':
            if x - mv >= 0 and park[y][x-mv:x].count('X') == 0:
                x -= mv
        elif dir == 'S':
            if y + mv < N and rotated_park[x][y+1:y+mv+1].count('X') == 0:
                y += mv
        else:
            if y - mv >= 0 and rotated_park[x][y-mv:y].count('X') == 0:
                y -= mv
    return [y, x]