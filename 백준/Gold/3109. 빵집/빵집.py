import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]

visited = [[0]*C for _ in range(R)]

def dfs(i, j):
    if j == C-1:
        return 1
    flag = 0
    for ni in [i-1, i, i+1]:
        if 0<=ni<R and arr[ni][j+1] == '.' and not visited[ni][j+1]:
            visited[ni][j+1] = 1
            flag = dfs(ni, j+1)
            if flag:
                break
    return flag

cnt = 0
for i in range(R):
    cnt += dfs(i, 0)

print(cnt)