import sys
input = sys.stdin.readline

N = int(input())

min_x = min_y = N
max_x = max_y = -1

cnt = 0
for i in range(N):
    row = input().rstrip()
    for j in range(N):
        if row[j] == 'G':
            cnt += 1
            if min_x > j:
                min_x = j
            if max_x < j:
                max_x = j
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
    print(min(N-min_x-1, max_x)+min(N-min_y-1, max_y))

