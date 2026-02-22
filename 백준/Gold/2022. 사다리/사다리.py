import sys
import math
input = sys.stdin.readline

x, y, c = map(float, input().split())

lo, hi = 0, min(x, y)

for _ in range(100):
    mid = (lo + hi) / 2
    h1 = math.sqrt(x*x - mid*mid)
    h2 = math.sqrt(y*y - mid*mid)
    cc = (h1*h2) / (h1 + h2)
    
    if cc > c:
        lo = mid
    else:
        hi = mid

print(f"{lo:.3f}")