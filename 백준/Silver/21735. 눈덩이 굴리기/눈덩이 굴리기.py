import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int,input().split())) + [0, 0]

arr2 = [0]*(N+3)
for i in range(1, N+3):
    arr2[i] = arr2[i-1] + arr[i]

Max = 0

def dfs(level, time, size):
    global Max
    if time == M or level >= N:
        Max = max(Max, size)
        return

    x = M - time
    y = min(N, level + 2*x)

    z = arr2[y] - arr2[level]

    if size + z <= Max:
        return

    dfs(level+1, time+1, size + arr[level+1])
    dfs(level+2, time+1, size//2 + arr[level+2])

dfs(0, 0, 1)
print(Max)