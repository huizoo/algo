import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    T, X, Y = map(int, input().split())
    if X < Y:
        print(T, 2, X, Y)
    elif Y < 4:
        print(T, "NO PATH")
    else:
        print(T, 6, 1, 2, 3, a:= max(4, X-Y+5), X+2, Y+a-2)