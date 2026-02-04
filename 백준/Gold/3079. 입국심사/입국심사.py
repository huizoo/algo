import sys
input = sys.stdin.readline
N, M = map(int, input().split())
T = sorted(int(input()) for _ in range(N))
def abc(x):
    Sum = 0
    for t in T:
        Sum += x//t
    if Sum >= M:
        return True
    else:
        return False
    
lo = 0
hi = 2*M*sum(T)//N**2
while lo < hi:
    mid = (lo+hi)//2
    if abc(mid):
        hi = mid
    else:
        lo = mid+1

print(lo)