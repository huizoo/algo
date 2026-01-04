import sys
input = sys.stdin.readline

M = 1000000007

N = int(input())
S = input().rstrip()

w = wh = whe = whee = 0

for x in S:
    if x == 'W':
        w += 1
    elif x == 'H':
        wh += w
    elif x == 'E':
        whee = (whee*2 + whe) % M
        whe = (whe + wh) % M

print(whee % M)