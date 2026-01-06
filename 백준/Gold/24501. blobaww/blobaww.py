import sys
input = sys.stdin.readline

MOD = int(1e9+7)

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

answer = 0
m = [[0]*(M+1) for _ in range(N+1)]
sm = [[0]*(M+1) for _ in range(N+1)]
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        m[i][j] = m[i+1][j] + m[i][j+1] - m[i+1][j+1] + (arr[i][j] == 'M')
        sm[i][j] = sm[i+1][j] + sm[i][j+1] - sm[i+1][j+1]
        if arr[i][j] == 'S':
            sm[i][j] += m[i][j]
        if arr[i][j] == 'E':
            answer = (answer + sm[i][j]) % MOD

print(answer % MOD)