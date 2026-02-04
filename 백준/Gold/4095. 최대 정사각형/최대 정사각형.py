import sys
input = sys.stdin.readline

answer = []
while True:
    N, M = map(int, input().split())
    if N == 0 or M == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = 0
    Sum = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1 and j == 1:
                Sum[1][1] = arr[0][0]
            elif i == 1:
                Sum[1][j] = arr[0][j-1] + Sum[1][j-1]
            elif j == 1:
                Sum[i][1] = arr[i-1][0] + Sum[i-1][1]
            else:
                Sum[i][j] = arr[i-1][j-1] + Sum[i-1][j] + Sum[i][j-1] - Sum[i-1][j-1]
    Max = 0
    for i in range(N, -1, -1):
        for j in range(M, -1, -1):
            for k in range(Max+1, min(i, j)+1):
                if Sum[i][j] - Sum[i-k][j] - Sum[i][j-k] + Sum[i-k][j-k] == k**2:
                    Max = k
                else:
                    break
    
    answer.append(Max)

print(*answer, sep='\n')


