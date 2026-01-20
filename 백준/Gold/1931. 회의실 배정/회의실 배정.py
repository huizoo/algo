import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

start = end = 0
cnt = 0
for s, e in arr:
    if end <= s:
        start, end = s, e
        cnt += 1

print(cnt)