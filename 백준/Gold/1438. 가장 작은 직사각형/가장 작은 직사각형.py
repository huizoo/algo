from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
n = N//2
Min = 1<<31
dic = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    dic[x].append(y)

X = sorted(dic.keys())
l = len(X)
for i in range(l):
    x1 = X[i]
    for j in range(i, l):
        x2 = X[j]
        cand = []
        for k in range(i, j+1):
            cand.extend(dic[X[k]])
        
        cand.sort()

        for k in range(len(cand)-n+1):
            S = (x2-x1+2)*(cand[k+n-1]-cand[k]+2)
            if Min > S:
                Min = S

print(Min)