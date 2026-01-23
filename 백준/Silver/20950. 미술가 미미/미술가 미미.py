import sys
from itertools import combinations
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    R, G, B = map(int, input().split())
    P = min(N, 7)
    
    Min = 1e9
    
    for i in range(2, P+1):
        for rgb in combinations(arr, i):
            r = g = b = 0
            for r2, g2, b2 in rgb:
                r += r2; g += g2; b += b2
            r, g, b = r//i, g//i, b//i

            Min = min(Min, abs(R-r)+abs(G-g)+abs(B-b))

    print(Min)

if __name__ == "__main__":
    solve()