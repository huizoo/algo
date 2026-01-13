import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

Max = 0
for w in arr:
    if Max+1 >= w:
        Max += w
    else:
        break

print(Max+1)

