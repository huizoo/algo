from collections import defaultdict
import sys
input = sys.stdin.readline

h, v = map(int, input().split())
Y = tuple(map(int, input().split()))
X = tuple(map(int, input().split()))

dic1 = defaultdict(int)
for idx, value in enumerate(Y):
    for idx2 in range(idx+1, h):
        dic1[value-Y[idx2]] += 1

cnt = 0
for idx, value in enumerate(X):
    for idx2 in range(idx+1, v):
        cnt += dic1[value-X[idx2]]

print(cnt)