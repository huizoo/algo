N = int(input())
arr = list(map(int, input().split()))
arr2 = [-1 for i in range(N)]
# 1에 적힌 숫자가 1의 인덱스번호

for i in range(N):
    idx = arr[i]
    while idx<N:
        cnt = arr2[:idx].count(-1)
        if arr2[idx] == -1 and arr[i] == cnt:
            arr2[idx] = i+1
            break
        else:
            idx += 1

print(*arr2)