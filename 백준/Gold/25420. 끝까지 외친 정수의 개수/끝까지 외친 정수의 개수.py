import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Set = set(map(int, input().split()))

arr = [0]*(N+1)

for i in range(N, -1, -1):
    if i in Set: continue
    flag = 0    
    for j in range(i+1, i+K+1):
        if j > N: break
        if j in Set: continue
        if arr[j]:
            flag = 1
            break
    arr[i] = 1-flag

i = 0
cnt = 0
while i < N:
    flag = 0
    cango = 0
    for j in range(min(i+K, N), i, -1):
        if j in Set: continue
        if arr[j]:
            flag = 1
            cnt += 1
            i = j
            break
        cango = j
    if flag == 0:
        if cango:
            cnt += 1
            i = cango
        else:
            break

print(cnt)