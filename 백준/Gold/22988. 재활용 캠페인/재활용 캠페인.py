import sys
input = sys.stdin.readline

N, X = map(int, input().split())
C = sorted(map(int, input().split()))
lo = 0
hi = N-1
cnt = 0
cnt2 = 0
while hi >= 0 and C[hi] == X:
    cnt += 1
    hi -= 1

if hi < 0:
    print(cnt)
    sys.exit()

while lo < hi:
    if 2*(C[lo]+C[hi]) >= X:
        cnt += 1
        lo += 1
        hi -= 1
    else:
        lo += 1
        cnt2 += 1

if lo == hi:
    cnt2 += 1

print(cnt+cnt2//3)
        