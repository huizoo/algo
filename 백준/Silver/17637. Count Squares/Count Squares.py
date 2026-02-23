from collections import defaultdict
import sys
input = sys.stdin.readline

h, v = map(int, input().split())
Y = list(map(int, input().split()))
X = list(map(int, input().split()))

dic1 = defaultdict(int)
for i in range(h):
    for j in range(i+1, h):
        dic1[Y[j]-Y[i]] += 1

dic2 = defaultdict(int)
for i in range(v):
    for j in range(i+1, v):
        dic2[X[j]-X[i]] += 1

cnt = 0
for key, value in dic1.items():
    for key2, value2 in dic2.items():
        if key == key2:
            cnt += value*value2

print(cnt)