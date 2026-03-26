from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = input().split()
    q = deque([arr[0]])
    for i in range(1, N):
        x = arr[i]
        if q[0] < x:
            q.append(x)
        else:
            q.appendleft(x)

    print(*q, sep='')