import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()), reverse=True)

print(sum(A[i]-i if A[i]-i > 0 else 0 for i in range(N)))