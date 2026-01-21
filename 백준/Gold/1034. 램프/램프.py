import sys
input = sys.stdin.readline

N, M = map(int, input().split())


arr = []
arr2 = [set() for _ in range(M+1)]

for i in range(N):
    row = input().rstrip()
    arr.append(row)
    cnt = 0
    for x in row:
        if x == '0':
            cnt += 1
    arr2[cnt].add(row)

K = int(input())
Max = 0
if K % 2 == 0:
    for i in range(min(M-(M%2), K), -1, -2):
        for row in arr2[i]:
            cnt = arr.count(row)
            if Max < cnt:
                Max = cnt
else:
    for i in range(min(M-((M+1)%2), K), 0, -2):
        for row in arr2[i]:
            cnt = arr.count(row)
            if Max < cnt:
                Max = cnt

print(Max)