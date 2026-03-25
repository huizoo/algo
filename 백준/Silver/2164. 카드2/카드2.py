from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([i for i in range(1, N+1)])

while q:
    x = q.popleft()
    if q:
        q.append(q.popleft())
    else:
        print(x)
        break