import sys
input = sys.stdin.readline

MOD = int(1e9+7)

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

answer = 0
e = [[0]*(M+1) for _ in range(N+1)]
es = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        now = arr[i-1][j-1]

        e[i][j] = e[i-1][j] + e[i][j-1] - e[i-1][j-1] + (now == 'E')
        es[i][j] = es[i-1][j] + es[i][j-1] - es[i-1][j-1] + (e[i][j] if now == 'S' else 0)

        if now == 'M':
            answer = (answer + es[i][j]) % MOD

print(answer % MOD)