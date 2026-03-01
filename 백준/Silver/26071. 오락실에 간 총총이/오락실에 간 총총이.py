import sys
input = sys.stdin.readline
N = int(input())

min_x, min_y = N, N
max_x, max_y = -1, -1
cnt = 0

for i in range(N):
    cnt2 = 0
    for j, v in enumerate(input().rstrip()):
        if v == 'G':
            cnt2 += 1
            if min_x > j:
                min_x = j
            if max_x < j:
                max_x = j
    if cnt2:
        cnt += cnt2
        if min_y > i:
            min_y = i
        if max_y < i:
            max_y = i

if cnt == 1:
    print(0)
elif min_x == max_x:
    print(min(N-min_y-1, max_y))
elif min_y == max_y:
    print(min(N-min_x-1, max_x))
else:
    print(min(N-min_y-1, max_y)+min(N-min_x-1, max_x))

            
    



