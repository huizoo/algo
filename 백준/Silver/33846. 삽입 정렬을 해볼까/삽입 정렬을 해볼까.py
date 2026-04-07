import sys
input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))
a2 = sorted(a[:t])
print(*a2, *a[t:])