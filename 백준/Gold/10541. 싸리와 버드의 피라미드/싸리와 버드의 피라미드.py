from array import array
import sys
input = sys.stdin.readline

N = int(input())
st = input().rstrip()
M = len(st)
A, Z = ord('A'), ord('Z')
arr = [array('I', [0]*(Z+1)) for _ in range(M)]
for i, x in enumerate(st):
    arr[i][ord(x)] = 1
    if i == 0: continue
    for j in range(A, Z+1):
        arr[i][j] += arr[i-1][j]

K = int(input())
ans = []
for _ in range(K):
    a, c = input().split()
    a = int(a)
    C = ord(c)
    
    S = a*(a-1)//2
    total = arr[-1][C]
    if a%M == 0:
        ans.append((a//M)*total)
    else:
        sm = S%M
        sam = (sm+a)%M
        if sam-sm > 0:
            ans.append((a//M)*total + arr[sam-1][C] - (0 if sm == 0 else arr[sm-1][C]))
        else:
            ans.append((a//M)*total + (0 if sm == 0 else total-arr[sm-1][C]) + (0 if sam == 0 else arr[sam-1][C]))

print(*ans, sep='\n')