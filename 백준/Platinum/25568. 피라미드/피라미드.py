import sys
input = sys.stdin.readline
N = int(input())
top = int(input())
Min = [0]*2

def abc(c):
    ans = 0

    x = min(c[0][1], c[1][0])
    ans += x
    c[0][1] -= x
    c[1][0] -= x

    x = min(c[0][2], c[2][0])
    ans += x
    c[0][2] -= x
    c[2][0] -= x

    x = min(c[1][2], c[2][1])
    ans += x
    c[1][2] -= x
    c[2][1] -= x

    ans += 2*(c[0][1]+c[0][2])

    return ans

for i in range(1, N):
    arr = tuple(map(int, input().split()))
    c0 = [[0]*3 for _ in range(3)]
    c1 = [[0]*3 for _ in range(3)]
    cnt = [0]*3
    ideal = [0]*3
    for j in range(i+1):
        now = arr[j]
        ideal_now0 = ((i+j)%3+top)%3
        ideal_now1 = ((i+(i-j))%3+top)%3
        cnt[now] += 1
        ideal[ideal_now0] += 1
        if now != ideal_now0:
            c0[now][ideal_now0] += 1
        if now != ideal_now1:
            c1[now][ideal_now1] += 1
    
    if cnt == ideal:
        Min[0] += abc([row[:] for row in c0])
        Min[1] += abc([row[:] for row in c1])
    else:
        print(-1)
        sys.exit()

print(min(Min))