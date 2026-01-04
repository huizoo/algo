import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ans = 0
l = 10
for i in range(1, N+1):
    if i == l:
        l *= 10
    
    ans = (ans * (l % K) + i) % K

print(ans)
