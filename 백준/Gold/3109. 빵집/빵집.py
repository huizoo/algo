import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]

visited = [[0]*C for _ in range(R)]

def abc(i):
    stack = [(i, 0)]
    visited[i][0] = 1

    while stack:
        i, j = stack[-1]

        if j == C-1:
            return 1

        moved = 0

        for ni in [i-1, i, i+1]:
            if 0 <= ni < R and arr[ni][j+1] == '.' and not visited[ni][j+1]:
                visited[ni][j+1] = 1
                stack.append((ni, j+1))
                moved = 1
                break

        if not moved:
            stack.pop()

    return 0


cnt = 0
for i in range(R):
    cnt += abc(i)

print(cnt)
