import sys
input = sys.stdin.readline

N, K = map(int, input().split())
R, C = map(int, input().split())
flag = 0
d = [-1, 0, 1]
lst = []
for y in d:
    for x in d:
        if y == 0 and x == 0: continue
        if 0 < R+y <= N and 0 < C+x <= N:
            lst.append((R+y, C+x))


flag = 0
flag2 = [0]*len(lst)

for _ in range(K):
    y, x = map(int, input().split())
    if y == R or x == C or R+C == y+x or R-C == y-x:
        flag = 1
    for i in range(len(lst)):
        yy, xx = lst[i]
        if y == yy or x == xx or yy+xx == y+x or yy-xx == y-x:
            flag2[i] = 1


if flag == 0:
    if flag2.count(0) == 0:
        print('STALEMATE')
    else:
        print('NONE')
elif flag2.count(0) == 0:
    print('CHECKMATE')
else:
    print('CHECK')
