import sys
from functools import lru_cache
input = sys.stdin.readline

N, K = map(int, input().split())

dic = dict()

@lru_cache(None)
def abc(pos, a, b, k):
    if k > K:
        return False
    if pos == N:
        return k == K

    if abc(pos + 1, a + 1, b, k):
        dic[(pos, a, b, k)] = 'A'
        return True

    if abc(pos+1, a, b + 1, k + a):
        dic[(pos, a, b, k)] = 'B'
        return True

    if abc(pos+1, a, b, k + a + b):
        dic[(pos, a, b, k)] = 'C'
        return True

    return False


if not abc(0, 0, 0, 0):
    print(-1)
    sys.exit()

pos = a = b = k = 0
ans = []
for _ in range(N):
    ch = dic[(pos, a, b, k)]
    ans.append(ch)
    if ch == 'A':
        a += 1
    elif ch == 'B':
        k += a; b += 1
    else:
        k += a + b
    pos += 1

print(''.join(ans))