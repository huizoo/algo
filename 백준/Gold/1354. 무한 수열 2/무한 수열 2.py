import sys
from functools import lru_cache
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, P, Q, X, Y = map(int, input().split())

@lru_cache(None)
def abc(n):
    if n <= 0:
        return 1
    return abc(n//P-X) + abc(n//Q-Y)

print(abc(N))