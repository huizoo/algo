from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

visited = [[K+1]*M for _ in range(N)]
visited[0][0] = 0
q = deque([(1, 0, 1, 0, 0)])
while q:
    cnt, k, flag, y, x = q.popleft()
    if y == N-1 and x == M-1:
        print(cnt)
        sys.exit()
    for dy, dx in d:
        ny, nx = dy+y, dx+x
        if 0<=ny<N and 0<=nx<M:
            if arr[ny][nx] == '0':
                if visited[ny][nx] <= k: continue
                visited[ny][nx] = k
                q.append((cnt+1, k, flag^1, ny, nx))
            elif k < K:
                if visited[ny][nx] <= k+1: continue
                if flag:
                    visited[ny][nx] = k+1
                    q.append((cnt+1, k+1, flag^1, ny, nx))
                else:
                    q.append((cnt+1, k, flag^1, y, x))

print(-1)