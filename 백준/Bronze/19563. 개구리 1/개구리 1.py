import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = c-abs(b)-abs(a)
print('YES' if d >= 0 and d%2==0 else 'NO')