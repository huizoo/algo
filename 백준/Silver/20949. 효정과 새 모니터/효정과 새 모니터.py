import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(1, N+1):
    W, H = map(int, input().split())
    arr.append((-W**2-H**2, i))

arr.sort()
print(*[row[1] for row in arr], sep='\n')