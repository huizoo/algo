import sys, heapq
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

M, N = map(int, input().split())
arr = [input().strip() for _ in range(N)]

visited = [[0]*M for _ in range(N)]
heap = []
heapq.heappush(heap, (0, 0, 0))
cnt3 = 0
while heap:
    cnt, y, x = heapq.heappop(heap)
    if y == N-1 and x == M-1:
        cnt3 = cnt
        break
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=N or nx>=M: continue
        if visited[ny][nx] == 1: continue
        if arr[ny][nx] == '1':
            cnt2 = cnt + 1
            heapq.heappush(heap, (cnt2, ny, nx))
            visited[ny][nx] = 1
            continue
        heapq.heappush(heap, (cnt, ny, nx))
        visited[ny][nx] = 1
            
print(cnt3)