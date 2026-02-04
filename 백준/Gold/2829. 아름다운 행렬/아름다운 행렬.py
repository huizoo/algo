import sys
input = sys.stdin.readline
N = int(input())
Sum1 = [[0]*(N+2) for _ in range(N+2)]
Sum2 = [[0]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    arr = tuple(map(int, input().split()))
    if i == 1:
        for j in range(1, N+1):
            Sum1[1][j] = arr[j-1]
            Sum2[1][j] = arr[j-1]
    else:
        Sum1[i][N] = arr[N-1] + Sum1[i-1][N-1]
        Sum1[i][1] = arr[0]
        Sum2[i][1] = arr[0] + Sum2[i-1][2]
        Sum2[i][N] = arr[N-1]
        for j in range(2, N):
            Sum1[i][j] = arr[j-1] + Sum1[i-1][j-1]
            Sum2[i][j] = arr[j-1] + Sum2[i-1][j+1]

Max = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(min(i, j)+1):
            a = Sum1[i][j] - Sum1[i-k][j-k]
            b = Sum2[i][j-k+1] - Sum2[i-k][j+1]
            if Max < a-b:
                Max = a-b

print(Max)

