import sys
input = sys.stdin.readline
N = int(input())
arr = [0] + list(range(1, N+1))
arr2 = [0] + list(int(input()) for _ in range(N))

total = 0
visited1 = [0]*(N+1)
for idx, value in enumerate(arr):
    if idx == 0: continue
    if visited1[idx] or visited1[value]: continue
    visited2 = set()
    visited2.add(idx)
    cnt = 1
    start = idx
    while arr2[idx] not in visited2:
        idx = arr2[idx]
        visited2.add(idx)
        cnt += 1
    if start == arr2[idx]:
        total += cnt
        for num in visited2:
            visited1[num] = 1

print(total)
for i, v in enumerate(visited1):
    if v == 1:
        print(i)