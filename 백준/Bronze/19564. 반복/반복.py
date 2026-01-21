import sys
input = sys.stdin.readline
S = input().rstrip()

now = ord(S[0])

cnt = 0
for x in S:
    nxt = ord(x)
    if now >= nxt:
        cnt += 1
    now = nxt

print(cnt)