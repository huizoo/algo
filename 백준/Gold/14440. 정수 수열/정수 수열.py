import sys
input = sys.stdin.readline

x, y, a0, a1, n = map(int, input().split())

def abc(lst1, lst2):
    return [
        [(lst1[0][0]*lst2[0][0] + lst1[0][1]*lst2[1][0]) % 100,
         (lst1[0][0]*lst2[0][1] + lst1[0][1]*lst2[1][1]) % 100],
        [(lst1[1][0]*lst2[0][0] + lst1[1][1]*lst2[1][0]) % 100,
         (lst1[1][0]*lst2[0][1] + lst1[1][1]*lst2[1][1]) % 100]
    ]

def bhc(lst, n):
    lst0 = [[1, 0], [0, 1]]

    while n > 0:
        if n & 1:
            lst0 = abc(lst0, lst)
        lst = abc(lst, lst)
        n //= 2

    return lst0

if n == 0:
    print(f"{a0:02d}")
elif n == 1:
    print(f"{a1:02d}")
else:
    arr = [[x, y], [1, 0]]
    arr2 = bhc(arr, n-1)

    print(f"{(arr2[0][0]*a1 + arr2[0][1]*a0) % 100:02d}")