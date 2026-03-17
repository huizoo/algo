import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    Max = now = -1000
    for v in map(int, input().split()):
        now = max(v, now+v)
        Max = max(Max, now)
    print(Max)