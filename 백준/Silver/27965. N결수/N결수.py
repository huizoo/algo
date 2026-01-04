import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ans = 0

for i in range(1, N):
    ans = (ans + i) % K
    l = len(str(i + 1))
    ans = (ans * pow(10, l, K)) % K

ans = (ans + N) % K

print(ans)
