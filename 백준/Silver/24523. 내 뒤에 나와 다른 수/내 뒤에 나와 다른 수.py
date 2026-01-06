import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = [0]*N
answer[N-1] = -1
Min = N-1
Min2 = N
for i in range(N-2, -1, -1):
    if arr[i] == arr[Min]:
        if Min2 == N:
            answer[i] = -1
        else:
            answer[i] = Min2 + 1
        Min = i
    else:
        answer[i] = Min + 1
        Min2 = Min
        Min = i

print(*answer)
