import sys
input = sys.stdin.readline

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

S = [0]*5001
ans = [0]*N

for i, a in enumerate(A):
    cnt = (sum(S[1:a])+1)%MOD
    ans[i] = cnt
    S[a] = (S[a]+cnt)%MOD
    
print(*ans)
