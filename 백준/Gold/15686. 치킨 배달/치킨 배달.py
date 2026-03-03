import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
chicken = []
house = []
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            house.append((i, j))
        elif v == 2:
            chicken.append((i, j))

cl = len(chicken)
hl = len(house)
arr2 = [[0]*(hl) for _ in range(cl)]
for i, (ci, cj) in enumerate(chicken):
    for j, (hi, hj) in enumerate(house):
        arr2[i][j] = abs(ci-hi) + abs(cj-hj)

Min = [10**9]*hl
Min2 = 10**9
def abc(level, idx, Sum):
    global Min2, Min
    if level == M:
        if Min2 > Sum:
            Min2 = Sum
        return
    
    for i in range(idx, cl):
        temp = Min[:]
        S = 0
        for j in range(hl):
            if Min[j] > arr2[i][j]:
                Min[j] = arr2[i][j]
                S += Min[j] - (0 if temp[j] == 10**9 else temp[j])
    
        abc(level+1, i+1, Sum+S)
        Min = temp[:]
    
abc(0, 0, 0)

print(Min2)