import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [0, 0]

def dfs(level, time, size):
    if time == M or level >= N :
        return size
    return max(dfs(level+1, time+1, size+arr[level+1]), dfs(level+2, time+1, size//2+arr[level+2]))

print(dfs(0, 0, 1))