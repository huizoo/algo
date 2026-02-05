import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(10)]

visited = [[0]*10 for _ in range(10)]
used = [0]*6
Min = 100

def find():
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1 and not visited[i][j]:
                return i, j
    return -1, -1

def abc(y, x, k):
    for i in range(y, y+k):
        for j in range(x, x+k):
            if not arr[i][j] or visited[i][j]:
                return False
    return True

def bhc(y, x, k):
    for i in range(y, y+k):
        for j in range(x, x+k):
            visited[i][j] = 1

def bbq(y, x, k):
    for i in range(y, y+k):
        for j in range(x, x+k):
            visited[i][j] = 0

def dfs(cnt):
    global Min
    if cnt >= Min:
        return
    y, x = find()
    if y == -1:
        if Min > cnt:
            Min = cnt
        return

    for k in range(5, 0, -1):
        if used[k] == 5: continue
        if y+k > 10 or x+k > 10: continue
        if abc(y, x, k):
            used[k] += 1
            bhc(y, x, k)
            dfs(cnt+1)
            bbq(y, x, k)
            used[k] -= 1


dfs(0)

print(Min if Min != 100 else -1)