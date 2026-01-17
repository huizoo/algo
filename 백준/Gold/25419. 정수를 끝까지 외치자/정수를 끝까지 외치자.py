import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Set = set(map(int, input().split()))

# 1은 지는 위치, 0은 이기는 위치
arr = [0]*(N+1)

for i in range(N, -1, -1):
    if i in Set: continue
    flag = 0
    for j in range(i+1, i+K+1):
        if j > N: break
        if j in Set: continue
        if arr[j]:
            flag=1
            break
    arr[i] = 1-flag

print(1-arr[0])