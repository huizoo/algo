import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(M):
    input()

print('Yes' if M <= N else 'No')
