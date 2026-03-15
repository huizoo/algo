import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, 9):
    l = 0
    for r, v in enumerate(A):
        if N-l <= ans:
            break
        if i <= v <= i+2:
            ans = max(ans, r-l+1)
        else:
            l = r+1

print(ans)