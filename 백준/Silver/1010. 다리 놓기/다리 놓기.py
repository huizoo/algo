from math import comb
import sys
input = sys.stdin.readline
answer = []
T = int(input())
for _ in range(T):
    ans = 0
    N, M = map(int, input().split())
    answer.append(comb(M, N))

print(*answer, sep='\n')
