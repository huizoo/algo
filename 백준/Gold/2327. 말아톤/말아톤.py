import sys
input = sys.stdin.readline
H, N = map(int, input().split())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1], reverse=True)
dp = 1
mask = (1<<H+1)-1
check = 1<<H
for h, s in arr:
    dp |= (dp<<h)
    dp &= mask
    
    if dp&check:
        print(s)
        break
