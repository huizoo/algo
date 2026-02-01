import sys, heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
heap = [(1, 0, 0, 0)]
for i in range(K+1):
    visited[i][0][0] = 1
while heap:
    cnt, k, y, x = heapq.heappop(heap)
    if y == N-1 and x == M-1:
        print(cnt)
        sys.exit()
    for dy, dx in d:
        ny, nx = dy+y, dx+x
        if 0<=ny<N and 0<=nx<M:
            if arr[ny][nx] == '0':
                if visited[k][ny][nx]: continue
                for i in range(k, K+1):
                    visited[i][ny][nx] = 1
                heapq.heappush(heap, (cnt+1, k, ny, nx))
            elif k < K:
                if visited[k+1][ny][nx]: continue
                for i in range(k+1, K+1):
                    visited[i][ny][nx] = 1
                heapq.heappush(heap, (cnt+1, k+1, ny, nx))
                
print(-1)