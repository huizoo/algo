import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dic = dict()
for x in arr:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
M = int(input())
answer = []
for x in (map(int, input().split())):
    answer.append(dic.get(x, 0))

print(*answer)
