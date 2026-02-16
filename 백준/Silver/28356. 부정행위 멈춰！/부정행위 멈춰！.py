import sys
input = sys.stdin.readline
N, M = map(int, input().split())
m = M//2
arr1 = [1, 2]*m
arr2 = [3, 4]*m
if M % 2 == 1:
    arr1.append(1)
    arr2.append(3)

if N == 1:
    if M == 1:
        print(1)
        print(1)
    else:
        print(2)
        print(*arr1)
elif M == 1:
    print(2)
    print(*[1, 2]*(N//2), sep='\n')
    if N % 2 == 1:
        print(1)
else:
    print(4)
    for i in range(N):
        if i % 2 == 0:
            print(*arr1)
        else:
            print(*arr2)
