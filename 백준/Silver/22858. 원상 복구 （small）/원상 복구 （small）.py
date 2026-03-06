import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))

P = [0]*(N+1)

for i in range(1, N+1):
    s = i
    for _ in range(K):
        s = D[s]
    P[s] = S[i]

print(*P[1:])