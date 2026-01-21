import sys
input = sys.stdin.readline
S = input().rstrip()

now = S[0]

cnt = 0
for x in S:
    if now >= x:
        cnt += 1
    now = x

print(cnt)