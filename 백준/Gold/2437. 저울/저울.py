import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

Max = 0
for w in arr:
    if w > Max + 1:
        break
    Max += w

print(Max+1)

