import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list()
a = set()
b = set()
c = set()
for _ in range(N):
    x, y, z = map(int, input().split())
    a.add(x)
    b.add(y)
    c.add(z)
    arr.append((x, y, z))


answer = 1e9
A = sorted(a)
B = sorted(b)
C = sorted(c)
for i in A:
    for j in B:
        if i+j >= answer: break
        for k in C:
            if i+j+k >= answer: break
            cnt = 0
            for ii, jj, kk in arr:
                if i >= ii and j >= jj and k >= kk:
                    cnt += 1
                    if cnt >= K:
                        answer = i+j+k
                        break

print(answer)