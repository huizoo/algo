import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)])

arr2 = []
i = 0
while i < N:
    sl, sr = arr[i]
    for j in range(i+1, N):
        nl, nr = arr[j]
        if sl <= nl <= sr :
            if sr < nr:
                sr = nr
        else:
            i = j
            break
    else:
        i = N
    arr2.append((sl, sr))

l, r = arr2[0]
jump = last = r
nl, nr = l, r

flag = 0
for i in range(1, len(arr2)):
    l1, r1 = arr2[i]
    cango = 2*r-l
    if cango < l1:
        if l == nl and r == nr: break
        l, r = max(l, nl), max(r, nr)
    elif cango <= r1:
        l, r = l1, r1 
    elif cango < 2*r1-l1:
        l, r = l1, r1
    else:
        nl, nr = l1, r1

print(max(r, nr))