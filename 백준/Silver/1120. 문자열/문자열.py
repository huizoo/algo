import sys
input = sys.stdin.readline
A, B = map(str, input().split())
a, b = len(A), len(B)
Min = b
for i in range(b-a+1):
    diff = 0
    for j in range(a):
       if A[j] == B[i+j]: continue
       diff += 1
    
    if Min > diff:
        Min = diff

print(Min)