import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
arr2 = [set() for _ in range(M+1)]

for i in range(N):
    row = input().rstrip()
    arr.append(row)
    arr2[row.count('0')].add(row)

K = int(input())
Max = 0
for i in range(M+1):
    if i <= K and (K - i) % 2 == 0:
        for row in arr2[i]:
            Max = max(Max, arr.count(row))

print(Max)