import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

events = []

for s, t in arr:
    events.append((s, 1))
    events.append((t, -1))

events.sort()

cnt = 0
Max = 0

for time, value in events:
    cnt += value
    if cnt > Max:
        Max = cnt

print(Max)