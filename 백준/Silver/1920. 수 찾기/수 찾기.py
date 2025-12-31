import sys
input = sys.stdin.readline

N = int(input())
Set = set(map(int, input().split()))
M = int(input())
arr = tuple(map(int, input().split()))
for ch in arr:
    if ch in Set:
        print(1)
    else:
        print(0)