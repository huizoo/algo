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
    Max = max(arr)
    if Max == 0:
        answer.append(0)
        continue
    Set = set(arr2)
    x = 1
    total = arr2[-1]
    while True:
        target = arr2[x]
        if target == 0:
            x += 1
            continue
        if total % target == 0:
            cnt = total // target
            for i in range(2, cnt+1):
                if i*target not in Set:
                    x += 1
                    break
            else:
                answer.append(N-cnt)
                break
        else:
            x += 1

print(*answer, sep='\n')