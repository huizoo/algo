import sys
input = sys.stdin.readline

def abc(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

N = int(input())
arr = [tuple(map(int, input().split())) for i in range(N)]

Min = 1e9

for i in range(N):
    d1 = 1e9
    d2 = 1e9
    now = arr[i]
    for j in range(N):
        if i == j: continue
        dist = abc(now, arr[j])
        if dist < d1:
            d2 = d1
            d1 = dist
        elif dist < d2:
            d2 = dist
    
    Min = min(Min, d1+d2)

print(Min)