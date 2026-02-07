import sys
input = sys.stdin.readline
answer = []
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr2 = [0]*(N+1)
    arr2[1] = arr[0]
    for i in range(2, N+1):
        arr2[i] = arr2[i-1]+arr[i-1]


    x = 1
    while True:
        target = arr2[x]
        if target != 0 and arr2[-1] > target and arr2[-1] // target == 1:
            answer.append(N-1)
            break
        flag = 0
        cut = 0
        Sum = 0
        for i in range(1, N+1):
            if arr2[i]-arr2[cut] == target:
                Sum += i-cut-1
                cut = i
                flag = 0
            elif arr2[i]-arr2[cut] < target:
                flag = 1
            else:
                flag = 1
                break
        if flag:
            x += 1
        else:
            answer.append(Sum)
            break

print(*answer, sep='\n')