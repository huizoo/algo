import sys
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())
if N <= C:
    print(N)
    sys.exit()

dic = dict()
for x in map(int, input().split()):
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

cnt = 0
for key, value in dic.items():
    cnt += min(value, C)

print(min(R*C, cnt))
