from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = defaultdict(int)
arr = [set() for _ in range(51)]

for i in range(N):
    row = input().rstrip()
    dic[row] += 1
    cnt = 0
    for x in row:
        if x == '0':
            cnt += 1
    arr[cnt].add(row)

K = int(input())
Max = 0
if K % 2 == 0:
    for i in range(min(50, K), -1, -2):
        for row in arr[i]:
            Max = max(dic[row], Max)
else:
    for i in range(min(K, 49), 0, -2):
        for row in arr[i]:
            Max = max(dic[row], Max)

print(Max)