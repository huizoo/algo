from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

q = deque()

for _ in range(N):
    arr = input().split()
    order = arr[0]
    if order == 'push_front':
        q.appendleft(arr[1])
    elif order == 'push_back':
        q.append(arr[1])
    elif order == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

         
       