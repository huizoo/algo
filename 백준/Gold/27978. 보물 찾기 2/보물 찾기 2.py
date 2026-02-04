import sys, heapq
input = sys.stdin.readline
H, W = map(int, input().split())
sy = sx = ey = ex = -1
arr = []
for i in range(H):
    row = input().rstrip()
    arr.append(row)
    for j in range(W):
        if row[j] == 'K':
            sy = i; sx = j
        elif row[j] == '*':
            ey = i; ex = j

d = [
    (1, 0, 1),
    (1, 1, 0),
    (0, 1, 0),
    (-1, 1, 0),
    (-1, 0, 1),
    (-1, -1, 1),
    (0, -1, 1),
    (1, -1, 1)]

heap = [(0, sy, sx)]
dist = [[10**9]*W for _ in range(H)]
while heap:
    cost, y, x = heapq.heappop(heap)
    if y == ey and x == ex:
        print(cost)
        sys.exit()
    for dy, dx, cost1 in d:
        ny, nx, cost2 = dy+y, dx+x, cost1+cost
        if ny<0 or ny>=H or nx<0 or nx>=W: continue
        if arr[ny][nx] == '#': continue
        if dist[ny][nx] > cost2:
            dist[ny][nx] = cost2
            heapq.heappush(heap, (cost2, ny, nx))

print(-1)