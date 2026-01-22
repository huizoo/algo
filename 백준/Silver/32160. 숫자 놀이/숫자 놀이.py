import sys
input = sys.stdin.readline

def solve(N):
    if N%2 == 0:
        arr = []
        arr2 = [N, 1]
        for x in range(2, N-1, 2):
            arr.append((x, x+1))
            arr2.append(1)
        
        l = len(arr2)
        if l%2 != 0:
            arr3 = [N]
            for x in range(1, l, 2):
                arr.append((1, 1))
                arr3.append(0)
        else:
            arr3 = [N-1]
            arr.append((N, 1))
            for x in range(2, l, 2):
                arr.append((1, 1))
                arr3.append(0)

        a = arr3[0]

        print(a)

        for x, y in arr:
            print(x, y)

        for x in range(1, len(arr3)):
            print(a, arr3[x])

    else:
        arr = []
        arr2 = [N]
        arr3 = []
        for x in range(1, N-1, 2):
            arr.append((x, x+1))
            arr2.append(1)
        
        l = len(arr2)
        if l%2 != 0:
            arr3 = [N]
            for x in range(1, l, 2):
                arr.append((1, 1))
                arr3.append(0)
        else:
            arr3 = [N-1]
            arr.append((N, 1))
            for x in range(2, l, 2):
                arr.append((1, 1))
                arr3.append(0)

        a = arr3[0]

        print(a)

        for x, y in arr:
            print(x, y)

        for x in range(1, len(arr3)):
            print(a, arr3[x])

solve(int(input()))