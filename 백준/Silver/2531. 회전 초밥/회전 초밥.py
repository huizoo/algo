import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

cnt = [0]*(d+1)
kind = 0
for i in range(k):
    now = arr[i]
    if cnt[now] == 0:
        kind += 1
    cnt[now] += 1

ans = 0
for i in range(N):
    ans = max(ans, kind + (0 if cnt[c] else 1))

    left = arr[i]
    cnt[left] -= 1
    if cnt[left] == 0:
        kind -= 1
    
    right = arr[(i+k) % N]
    if cnt[right] == 0:
        kind += 1
    cnt[right] += 1

print(ans)