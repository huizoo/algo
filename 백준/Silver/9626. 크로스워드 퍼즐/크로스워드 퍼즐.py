import sys
input = sys.stdin.readline

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

st = [input().rstrip() for _ in range(M)]
l = len(st[0])
col = L+l+R

for i in range(U):
    row = ''
    for j in range(col):
        if (i+j)%2 == 0:
            row += '#'
        else:
            row += '.'
    print(row)

for i in range(M):
    row = ''
    for j in range(L):
        if (U+i+j)%2 == 0:
            row += '#'
        else:
            row += '.'
    row += st[i]
    for j in range(R):
        if (U+L+l+i+j)%2 == 0:
            row += '#'
        else:
            row += '.'
    print(row)
    
for i in range(D):
    row = ''
    for j in range(col):
        if (U+M+i+j)%2 == 0:
            row += '#'
        else:
            row += '.'
    print(row)