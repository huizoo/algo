import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

cnt = 0
for _ in range(2):
    if A >= X:
        A -= X
        cnt += X
        X = 0
    else:
        Y += (X - A) // 3
        cnt += A
        X -= A
        A = 0

    if B >= Y:
        B -= Y
        cnt += Y
        Y = 0
    else:
        Z += (Y - B) // 3
        cnt += B
        Y -= B
        B = 0

    if C >= Z:
        C -= Z
        cnt += Z
        Z = 0
    else:
        cnt += C
        X += (Z - C) // 3
        Z -= C
        C = 0

print(cnt)
