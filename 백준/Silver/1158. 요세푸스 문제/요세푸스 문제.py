from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
cnt = 0
answer = []
while q:
    now = q.popleft()
    cnt += 1
    if cnt == K:
        answer.append(now)
        cnt = 0
    else:
        q.append(now)

print('<', end='')
print(*answer, sep=', ', end='')
print('>', end='')