import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = [0]*257

Min = 1e9
Max = 0

for row in arr:
    for height in row:
        cnt[height] += 1
        if Max < height:
            Max = height
        if Min > height:
            Min = height

if Min == Max:
    print(0, Min)
    sys.exit()

time = 1e9
Max_height = 0

for height1 in range(Max, Min-1, -1):
    time2 = 0
    remain = B
    flag = 0
    for height2 in range(Max, Min-1, -1):
        gap = height1 - height2
        if gap > 0:
            if remain - gap*cnt[height2] < 0:
                flag = 1
                break
            remain -= gap*cnt[height2]
            time2 += gap*cnt[height2]
        elif gap < 0:
            remain += -gap*cnt[height2]
            time2 += -gap*2*cnt[height2]

    if flag == 0 and time2 < time:
        time = time2
        Max_height = height1

print(time, Max_height)

