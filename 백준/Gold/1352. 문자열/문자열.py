import sys
input = sys.stdin.readline

N = int(input())

d = []

def dfs(idx, s):
    if s == N:
        return True
    if s > N:
        return False

    diff = N-s
    for x in range(diff, idx - 1, -1):
        if x - 1 > s:
            continue
        d.append(x)
        if dfs(x+1, s+x):
            return True
        d.pop()
    return False

if not dfs(1, 0):
    print(-1)
else:
    m = len(d)
    s = ['?'] * N

    for i, value in enumerate(d):
        s[value-1] = chr(ord('A')+i)

    arr = []
    for i, value in enumerate(d):
        ch = chr(ord('A')+i)
        arr.append(ch*(value-1))
    arr = ''.join(arr)

    idx = 0
    for i in range(N):
        if s[i] == '?':
            s[i] = arr[idx]
            idx += 1

    print(''.join(s))