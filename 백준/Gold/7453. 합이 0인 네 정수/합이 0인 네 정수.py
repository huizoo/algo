import sys
input = sys.stdin.readline
N = int(input())
A = []; B = []; C = []; D = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

AB = [a+b for a in A for b in B]
CD = [c+d for c in C for d in D]
        
AB.sort(); CD.sort()

ans = 0
i = 0
nn = N*N
j = nn-1

while i < nn and j >= 0:
    s = AB[i] + CD[j]
    if s == 0:
        cnt1 = cnt2 = 1
        ab = AB[i]; cd = CD[j]
        i += 1; j -= 1
        while i < nn and AB[i] == ab:
            i += 1
            cnt1 += 1
        while j >= 0 and CD[j] == cd:
            j -= 1
            cnt2 += 1
        
        ans += cnt1*cnt2
    elif s < 0:
        i += 1
    else:
        j -= 1


print(ans)