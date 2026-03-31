import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
op = 0
ans = []
for l in range(N):
    if arr[l] != l+1:
        for r in range(l, N):
            if arr[r] == l+1:
                for x in range((r-l)//2+1):
                    arr[l+x], arr[r-x] = arr[r-x], arr[l+x]
                ans.append((l+1, r+1))
                op += 1
                break

print(op)
for row in ans:
    print(*row)