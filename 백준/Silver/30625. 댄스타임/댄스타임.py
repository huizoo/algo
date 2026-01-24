import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = M-1
mod = 10**9+7
dance = [0]*2
for i  in range(1, N+1):
    a, b = map(int, input().split())
    dance[b]+=1

d1, d2 = dance
if m == 0 and d2 == 0:
    print(1)
    sys.exit()
Sum = ((m**d2) + d1*(m**(d2+1)) + d2*(m**(d2-1)))%mod
print(Sum)
