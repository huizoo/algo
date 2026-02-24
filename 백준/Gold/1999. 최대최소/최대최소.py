from collections import defaultdict
import sys
input = sys.stdin.readline
N, B, K = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(N))
M = N-B+1
Max = [[0]*M for _ in range(M)]
Min = [[0]*M for _ in range(M)]

for i in range(M):
    dic = defaultdict(int)
    for y in range(B):
        for x in range(B):
            dic[arr[i+y][x]] += 1
    
    Max[i][0] = max(dic)
    Min[i][0] = min(dic)

    for j in range(1, M):
        for k in range(B):
            l = arr[i+k][j-1]
            r = arr[i+k][B+j-1]
            if dic[l] == 1:
                dic.pop(l)
            else:
                dic[l] -= 1
            dic[r] += 1

        Max[i][j] = max(dic)
        Min[i][j] = min(dic)
    
for _ in range(K):
    i, j = map(int, input().split())
    print(Max[i-1][j-1] - Min[i-1][j-1])