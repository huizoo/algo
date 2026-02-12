import sys
input = sys.stdin.readline

st = input().rstrip()

S = K = value = 0

dic = {0: (-1, 0)}
ans = -1

for idx, ch in enumerate(st):
    if ch == 'S':
        S += 1
    elif ch == 'K':
        K += 1

    value = K-2*S

    if value in dic:
        idx1, S1 = dic[value]
        if S - S1 > 0:
            ans = max(ans, idx - idx1)
    else:
        dic[value] = (idx, S)

print(ans)
