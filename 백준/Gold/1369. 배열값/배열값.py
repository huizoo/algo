import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp2 = [[0]*N for _ in range(N)]
dp5 = [[0]*N for _ in range(N)]
INF = 1<<31
for i in range(N):
    for j in range(N):
        x = arr[i][j]
        
        if x == 0:
            c2 = c5 = INF
        else:
            c2 = c5 = 0
            while x%2 == 0:
                c2 += 1
                x //= 2
            while x%5 == 0:
                c5 += 1
                x //= 5
        
        if i == 0:
            if j == 0:
                dp2[i][j] = c2
                dp5[i][j] = c5
            else:
                dp2[i][j] = dp2[i][j-1] + c2
                dp5[i][j] = dp5[i][j-1] + c5
        elif j == 0:
            dp2[i][j] = dp2[i-1][j] + c2
            dp5[i][j] = dp5[i-1][j] + c5
        else:
            dp2[i][j] = min(dp2[i-1][j], dp2[i][j-1]) + c2
            dp5[i][j] = min(dp5[i-1][j], dp5[i][j-1]) + c5


two = dp2[N-1][N-1]
five = dp5[N-1][N-1]     
if two >= INF or five >= INF:
    print(1)
else:
    print(min(two, five))
