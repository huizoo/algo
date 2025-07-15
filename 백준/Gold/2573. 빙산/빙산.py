import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
N1, M1 = N-1, M-1
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arr = [list(map(int, input().split())) for _ in range(N)]

# 현재 빙산의 상태를 넣고 빙산 상하좌우에 빈칸의 개수가 기록된 배열(lst2)을 반환
def abc(lst):
    lst2 = [[0]*M for _ in range(N)]
    for y in range(1, N1):
        for x in range(1, M1):
            if lst[y][x] != 0:
                zero_cnt = 0
                for dy, dx in d:
                    ny, nx = y+dy, x+dx
                    if ny<0 or nx<0 or ny>=N or nx>=M: continue
                    if lst[ny][nx] == 0:
                        zero_cnt += 1
                lst2[y][x] = zero_cnt
    return lst2

# 현재 빙산의 상태를 넣고 빈칸의 개수만큼 녹은 빙산의 상태 반환
def bbq(lst, lst2):
    for i in range(N):
        for j in range(M):
            if lst2[i][j] != 0:
                lst[i][j] = max(0, lst[i][j] - lst2[i][j])
    return lst

# 현재 빙산의 상태를 넣고 한 덩어리라면 0 반환하고 두 덩어리로 나뉜다면 1 반환
def bfs(lst):
    ice_cnt = 0
    q = deque([])    
    visited = [[0]*M for _ in range(N)]
    for i in range(1, N1):
        for j in range(1, M1):
            if lst[i][j] != 0:
                if ice_cnt == 0:
                    q.append((i, j))
                    visited[i][j] = 1
                ice_cnt += 1
    
    while q:
        y, x = q.popleft()
        ice_cnt -= 1
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<1 or nx<1 or ny>=N1 or nx>=M1: continue
            if visited[ny][nx] == 1: continue
            if lst[ny][nx] == 0: continue
            visited[ny][nx] = 1
            q.append((ny, nx))
    
    if ice_cnt == 0:
        return 0
    else:
        return 1
    
# 빙산이 다 녹았다면 0 반환, 아직 덜 녹았다면 1 반환
def check(lst):
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0:
               return 1
    return 0


year = 1

while 1:
    if bfs(bbq(arr, abc(arr))) == 1:
        print(year)
        break
    else:
        if check(arr) == 1:
            year += 1
            continue
        else:
            print(0)
            break