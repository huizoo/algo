from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
ans = [i for i in range(1, N+1, 2)]

q = deque(list(range(2, N+1, 2)))
if N%2 == 1 and N != 1:
    q.append(q.popleft())
while q:
    ans.append(q.popleft())
    try:
        q.append(q.popleft())
    except:
        break
print(' '.join(map(str, ans)))