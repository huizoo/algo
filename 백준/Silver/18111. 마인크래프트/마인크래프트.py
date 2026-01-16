import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

cnt = [0]*257

for i in range(N):
    for h in map(int, input().split()):
        cnt[h] += 1

below = [0]*257
above = [0]*257
now1 = now2 = 0
for i in range(1, 257):
    now1 += cnt[i-1]
    below[i] = below[i-1] + now1
    j = 257-i
    now2 += cnt[j]
    above[j-1] = above[j] + now2


time = float('inf')
height = 0

for h, (b, a) in enumerate(zip(below, above)):
    if B+a-b < 0: continue
    t = 2*a+b
    if t <= time:
        time = t
        height = h

print(time, height)
