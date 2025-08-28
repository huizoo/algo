import sys
input = sys.stdin.readline

N, D = map(int, input().split())

arr = []

for _ in range(N):
    lst = list(map(int, input().split()))
    if lst[1] > D or lst[1]-lst[0]-lst[2] <= 0:
        N -= 1
        continue
    arr.append(lst)

arr.sort()

Max = 0

def dfs(level, Sum, now):
    global Max, visited
    # 끝일때 돌아가.
    if level == N:
        Max = max(Max, Sum)
        return
    
    # 현재 위치에서 지름길을 스킵하냐 스킵하지 않냐 두가지 경우의수 고려해.
    for i in range(2):
        if i == 0:
            dfs(level+1, Sum, now)
        else:
            if arr[level][0] < now:
                continue
            dfs(level+1, Sum+arr[level][1]-arr[level][0]-arr[level][2], arr[level][1])
    

dfs(0, 0, 0)

print(D-Max)