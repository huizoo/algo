from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr2 = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        arr2[i+1][j+1] = arr2[i+1][j] + arr2[i][j+1] - arr2[i][j] + arr[i][j]

def abc(y1, x1, y2, x2):
    return arr2[y2+1][x2+1] - arr2[y1][x2+1] - arr2[y2+1][x1] + arr2[y1][x1]

cnt = 0

for i in range(N-1):
    for j in range(N-1):
        cnt2 = defaultdict(int)
        for k in range(i, -1, -1):
            for l in range(j, -1, -1):
                cnt2[abc(k, l, i, j)] += 1
        
        for k in range(i+1, N):
            for l in range(j+1, N):
                cnt += cnt2[abc(i+1, j+1, k, l)]

        
        cnt2.clear()

        for k in range(i+1, N):
            for l in range(j, -1, -1):
                cnt2[abc(i+1, l, k, j)] += 1

        for k in range(i, -1, -1):
            for l in range(j+1, N):
                cnt += cnt2[abc(k, j+1, i, l)]
        

print(cnt)