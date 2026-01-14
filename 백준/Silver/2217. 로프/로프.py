import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

Max = 0

for i in range(N):
    can = arr[i]*(i+1)
    if can > Max:
        Max = can

print(Max)
    