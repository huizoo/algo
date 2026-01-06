import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = [-1]*N

i = 0

while i < N:
    j = i
    while j < N and arr[j] == arr[i]:
        j += 1
    if j < N:
        jj = j + 1
        for k in range(i, j):
            answer[k] = jj

    i = j    

print(*answer)
