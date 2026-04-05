import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N
for i in range(N):
    for j, v in enumerate(input().rstrip()):
        if v == 'T':
            arr[i] |= 1<<j

Min = N*N
for mask in range(1<<N):
    total = 0
    for x in arr:
        cnt = (x^mask).bit_count()
        total += min(cnt, N-cnt)
        if total >= Min:
            break
    Min = min(Min, total)

print(Min)