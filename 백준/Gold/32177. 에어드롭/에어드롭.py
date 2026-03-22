from collections import deque
import sys
input = sys.stdin.readline

# 휴대폰 버전 차이 T 이하 & 유클리드 거리로 최대 K 거리까지
N, K, T = map(int, input().split())
X, Y, V = map(int, input().split())
KK = K*K
cango = deque()
cand = []
ans = set()
visited = [0]*(N)
for i in range(N):
    x, y, v, p = map(int, input().split())
    if (X-x)**2 + (Y-y)**2 <= KK:
        if p == 0:
            if -T <= V-v <= T:
                cango.append((x, y, v, p))
                visited[i] = 1
            else:
                cand.append((i, x, y, v, p))
        elif -T <= V-v <= T:
            cango.append((x, y, v, p))
            visited[i] = 1
            ans.add(i+1)
        else:
            cand.append((i, x, y, v, p))
    else:
        cand.append((i, x, y, v, p))

while cango:
    x, y, v, p = cango.popleft()
    for i, x2, y2, v2, p2 in cand:
        if visited[i] == 1: continue
        if (x-x2)**2 + (y-y2)**2 <= KK:
            if p2 == 0:
                if -T <= v-v2 <= T:
                    cango.append((x2, y2, v2, p2))
                    visited[i] = 1
            elif -T <= v-v2 <= T:
                cango.append((x2, y2, v2, p2))
                visited[i] = 1
                ans.add(i+1)
                
if ans:
    print(*sorted(ans))
else:
    print(0)