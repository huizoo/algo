import sys
input = sys.stdin.readline
N, X = map(int, input().split())
'''
0: 1 => 2-1
1: 3 => 4-1
2: 3*2+1 = 7 => 8-1
3: (3*2+1)*2+1 = 15 => 16-1
4: ((3*2+1)*2+1)*2+1 = 31 => 32-1
'''

'''
1: BPPPB
2: B BPPPB P BPPPB B
3: B BBPPPBPBPPPBB P BBPPPBPBPPPBB B
4: B BBBPPPBPBPPPBBPBBPPPBPBPPPBBB P BBBPPPBPBPPPBBPBBPPPBPBPPPBBB B
'''
cnt = [1]*(N+1)
pat = [1]*(N+1)
for i in range(1, N+1):
    cnt[i] = cnt[i-1]*2+3
    pat[i] = pat[i-1]*2+1

def abc(n, x):
    if x == 0:
        return 0
    if n == 0:
        return 1 if x >= 1 else 0
    
    if x == 1:
        return 0
    elif x <= 1+cnt[n-1]:
        return abc(n-1, x-1)
    elif x == 2+cnt[n-1]:
        return pat[n-1]+1
    elif x <= 2+2*cnt[n-1]:
        return pat[n-1]+1+abc(n-1, x-(2+cnt[n-1]))
    else:
        return pat[n]
    

print(abc(N, X))