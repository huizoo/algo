from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

maxq = deque()
minq = deque()

l = ans = 0

for r, v in enumerate(A):
    while maxq and maxq[-1] < v:
        maxq.pop()
    maxq.append(v)

    while minq and minq[-1] > v:
        minq.pop()
    minq.append(v)

    while maxq[0] - minq[0] > 2:
        if maxq[0] == A[l]:
            maxq.popleft()
        if minq[0] == A[l]:
            minq.popleft()
        l += 1
    
    ans = max(ans, r-l+1)

print(ans)