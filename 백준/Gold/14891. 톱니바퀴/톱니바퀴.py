import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(4)]
K = int(input())
idx = [[2, 6] for _ in range(3)]

def right(x, d):
    l = idx[x][0]
    r = idx[x][1]
    if arr[x][l] != arr[x+1][r]:
        return 1, (l - d) % 8, (r + d) % 8
    return 0, (l - d) % 8, r

def left(x, d):
    l = idx[x][0]
    r = idx[x][1]
    if arr[x][l] != arr[x+1][r]:
        return 1, (l + d) % 8, (r - d) % 8
    return 0, l, (r - d) % 8

for _ in range(K):
    a, b = map(int, input().split())
    if a == 1:
        ret = [[-1]*3 for _ in range(3)]

        ret[0] = right(0, b)
        if ret[0][0] == 1:
            ret[1] = right(1, -b)
            if ret[1][0] == 1:
                ret[2] = right(2, b)

        for i in range(3):
            if ret[i][0] != -1:
                idx[i][0] = ret[i][1]
                idx[i][1] = ret[i][2]

    elif a == 2:
        ret = [[-1]*3 for _ in range(3)]

        ret[0] = left(0, b)
        ret[1] = right(1, b)
        if ret[1][0] == 1:
            ret[2] = right(2, -b)

        for i in range(3):
            if ret[i][0] != -1:
                idx[i][0] = ret[i][1]
                idx[i][1] = ret[i][2]
        
    elif a == 3:
        ret = [[-1]*3 for _ in range(3)]

        ret[1] = left(1, b)
        if ret[1][0] == 1:
            ret[0] = left(0, -b)
        ret[2] = right(2, b)

        for i in range(3):
            if ret[i][0] != -1:
                idx[i][0] = ret[i][1]
                idx[i][1] = ret[i][2]

    elif a == 4:
        ret = [[-1]*3 for _ in range(3)]

        ret[2] = left(2, b)
        if ret[2][0] == 1:
            ret[1] = left(1, -b)
            if ret[1][0] == 1:
                ret[0] = left(0, b)

        for i in range(3):
            if ret[i][0] != -1:
                idx[i][0] = ret[i][1]
                idx[i][1] = ret[i][2]


Sum = 0
Sum += 1 if arr[0][idx[0][0]-2] == '1' else 0
Sum += 2 if arr[1][idx[0][1]-6] == '1' else 0
Sum += 4 if arr[2][idx[1][1]-6] == '1' else 0
Sum += 8 if arr[3][idx[2][1]-6] == '1' else 0

print(Sum)