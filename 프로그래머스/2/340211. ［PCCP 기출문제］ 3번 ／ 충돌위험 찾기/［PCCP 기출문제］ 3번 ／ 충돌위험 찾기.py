from collections import defaultdict

def solution(points, routes):
    answer = 0
    
    n, x, m = len(points), len(routes), len(routes[0])
    
    visited = defaultdict(list)
    
    for j in range(x):
        for i in range(m):
            if i == 0: continue
            next_y, next_x = points[routes[j][i]-1]
            now_y, now_x = points[routes[j][i-1]-1]
            if i == 1:
                visited[j].append((now_y, now_x))
            end = abs(next_y - now_y) + abs(next_x - now_x)
            for _ in range(end):
                if next_y > now_y:
                    now_y += 1                    
                elif next_y < now_y:
                    now_y -= 1
                elif next_x > now_x:
                    now_x += 1
                elif next_x < now_x:
                    now_x -= 1
                visited[j].append((now_y, now_x))

    Max = 0
    for i in visited:
        Max = max(Max, len(visited[i]))
    
    for i in range(Max):
        check = set()
        duplication = set()
        for j in range(x):
            if len(visited[j]) - 1 >= i:
                if visited[j][i] in check:
                    duplication.add(visited[j][i])
                else:
                    check.add(visited[j][i])
        
        if len(check) != x:
            answer += len(duplication)
            
        
    return answer