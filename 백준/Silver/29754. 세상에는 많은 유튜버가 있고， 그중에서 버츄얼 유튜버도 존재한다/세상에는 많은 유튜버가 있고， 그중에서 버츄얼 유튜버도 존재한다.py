import sys
input = sys.stdin.readline
N, M = map(int, input().split())
real = []
dic = dict()
arr = [input().split() for _ in range(N)]
Max = M//7
for name, day, start, end in arr:
    hours = int(end[:2])-int(start[:2])
    minutes = int(end[3:])-int(start[3:])
    week = (int(day) - 1)//7
    if minutes < 0:
        hours -= 1
        minutes += 60
    if name in dic:
        if dic[name][week] is None:
            dic[name][week] = [hours, minutes, 1]
        else:    
            dic[name][week][0] += hours
            dic[name][week][1] += minutes
            dic[name][week][2] += 1
    else:
        dic[name] = [None]*Max
        dic[name][week] = [hours, minutes, 1]

for key, value in dic.items():
    flag = 0
    for x in value:
        if x is None:
            flag = 1
        elif x[0]+x[1]//60 < 60 or x[2] < 5:
            flag = 1
    if flag: continue
    else:
        real.append(key)
if real:
    print(*sorted(real), sep='\n')
else:
    print(-1)

