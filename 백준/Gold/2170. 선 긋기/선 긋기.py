import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

st, ed = arr[0]
ans = 0

for i in range(1, N):
    a, b = arr[i]
    if a <= ed:
        if b > ed:
            ed = b
    else:
        ans += ed - st
        st, ed = a, b

print(ans + ed - st)
