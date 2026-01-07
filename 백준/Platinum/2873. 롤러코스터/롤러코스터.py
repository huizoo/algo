import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

if R % 2 == 1:
    for i in range(R):
        if i == R-1:
            print('R'*(C-1), sep='')
        elif i % 2 == 0:
            print('R'*(C-1), 'D', sep='', end='')
        else:
            print('L'*(C-1), 'D', sep='', end='')
elif C % 2 == 1:
    for i in range(C):
        if i == C-1:
            print('D'*(R-1), sep='')
        elif i % 2 == 0:
            print('D'*(R-1), 'R', sep='', end='')
        else:
            print('U'*(R-1), 'R', sep='', end='')
else:
    Min_y = Min_x = -1
    Min = 10**3
    for i in range(R):
        for j in range(C):
            if (i+j)%2 == 0: continue
            if Min > arr[i][j]:
                Min = arr[i][j]
                Min_y, Min_x = i, j
    flag = 0
    for i in range(0, R, 2):
        if i <= Min_y <= i+1:
            flag = 1
            P = []
            y, x = i, 0
            while x < C-1:
                if x == Min_x:
                    P.append('R')
                elif y == i:
                    P.append('DR')
                    y = i+1
                else:
                    P.append('UR')
                    y = i
                x += 1

            if y == i:
                P.append('D')
                y = i+1
            if not (y == R-1 and x == C-1):
                P.append('D')

            print(*P, sep='', end='')
        elif flag == 0:
            print('R'*(C-1), 'D', 'L'*(C-1), 'D', sep='', end='')
        elif i == R-2:
            print('L'*(C-1), 'D', 'R'*(C-1), sep='', end='')
        else:
            print('L'*(C-1), 'D', 'R'*(C-1), 'D', sep='', end='')
