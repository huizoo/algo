import sys, heapq
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

M, N = map(int, input().split())
arr = [input().strip() for _ in range(N)]

dp = [[21e8]*M for _ in range(N)]
heap = []
heapq.heappush(heap, (0, 0, 0))
while heap:
    cnt, y, x = heapq.heappop(heap)
    if y == N-1 and x == M-1:
        break
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=N or nx>=M: continue
        if arr[ny][nx] == '1':
            cnt2 = cnt + 1
            if dp[ny][nx] > cnt2:
                dp[ny][nx] = cnt2
                heapq.heappush(heap, (cnt2, ny, nx))
        elif dp[ny][nx] > cnt:
                dp[ny][nx] = cnt
                heapq.heappush(heap, (cnt, ny, nx))
            
if N == 1 and M == 1:
    print(0)
else:
    print(dp[N-1][M-1])