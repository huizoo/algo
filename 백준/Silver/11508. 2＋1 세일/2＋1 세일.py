import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
print(sum(arr) - sum(arr[i] for i in range(2, N, 3)))