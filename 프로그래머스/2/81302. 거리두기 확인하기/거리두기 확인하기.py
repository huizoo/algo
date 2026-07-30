from collections import deque

def solution(places):
    answer = []
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    def bfs(place, i, j):
        q = deque()
        q.append((i, j, 0))
        visited = [[0]*5 for _ in range(5)]
        visited[i][j] = 1
        while q:
            y, x, cnt = q.popleft()
            if 0<cnt<=2:
                if place[y][x] == 'P':
                    return 0
            if cnt == 2:
                continue
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if ny<0 or nx<0 or ny>=5 or nx>=5: continue
                if (now:=place[ny][nx]) == 'X': continue
                if visited[ny][nx] == 1: continue
                visited[ny][nx] = 1
                q.append((ny, nx, cnt+1))
        return 1
    
    
    def search(place):
        for i, row in enumerate(place):
            for j, v in enumerate(row):
                if v == 'P':
                    if bfs(place, i, j):
                        continue
                    else:
                        return 0
        return 1
    
    
    for place in places:
        answer.append(search(place))
        
    return answer