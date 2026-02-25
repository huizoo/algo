import sys
input = sys.stdin.readline
N = int(input())
I = [(1<<i)-1 for i in range(11)]
J = [0]*11
J[1] = 1
for j in range(2, 11):
    J[j] = J[j-1]*2+3
arr = [[' ']*J[N] for _ in range(I[N])]
def abc(n, i1, i2, j1, j2):
    if n == 0:
        return
    ii = I[n-1]
    if n%2 == 0:
        for j in range(j1, j2):
            arr[i1][j] = '*'
        for j in range(1, (j2-j1-1)//2+1):
            arr[i1+j][j1+j] = '*'
            arr[i1+j][j2-j-1] = '*'
            pass
        abc(n-1, (i1+i2)>>1, i1+1, j1+ii+1, j2-ii-1)
    else:
        for j in range(j1, j2):
            arr[i1][j] = '*'
        for j in range(1, (j2-j1-1)//2+1):
            arr[i1-j][j1+j] = '*'
            arr[i1-j][j2-j-1] = '*'
            pass
        abc(n-1, (i1+i2)>>1, i1, j1+ii+1, j2-ii-1)
        pass
    
    
if N%2 == 0:
    abc(N, 0, I[N], 0, J[N])
    jjj = J[N]
    for idx, row in enumerate(arr):
        print(*row[:J[N]-idx], sep='')
else:
    abc(N, I[N]-1, 0, 0, J[N])
    jjjj = J[N]//2+1
    for idx, row in enumerate(arr):
        print(*row[:jjjj+idx], sep='')