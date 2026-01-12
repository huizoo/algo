import sys
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    n, m = map(int, input().split())
    answer.append(n.bit_length()+m)

print(*answer, sep='\n')