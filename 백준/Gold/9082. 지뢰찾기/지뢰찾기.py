import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = input().rstrip()
    arr2 = input().rstrip()
    mine = [0 if arr2[i] == '#' else 1 for i in range(N)]
    if N == 1:
        print(1)
        continue
    x = arr[0]
    if x == '1':
        if mine[1] == 0:
            mine[0] = 1
            mine[1] = -1
    elif x == '2':
        mine[0] = 1
        mine[1] = 1
    else:
        mine[0] = -1
        mine[1] = -1

    for i in range(1, N-1):
        now = arr[i]
        if now == '0':
            mine[i-1] = -1
            mine[i] = -1
            mine[i+1] = -1
        elif now == '1':
            if mine[i+1] == 1:
                mine[i] = -1
                mine[i-1] = -1
            elif mine[i] == 1:
                mine[i+1] = -1
                mine[i-1] = -1
            else:
                if mine[i-1] == -1:
                    if mine[i] == -1:
                        mine[i+1] = 1
                    else:
                        mine[i] = 1
                        mine[i+1] = -1
                else:
                    mine[i-1] = 1
                    mine[i] = -1
                    mine[i+1] = -1

        elif now == '2':
            if mine[i+1] == 1:
                if mine[i] == 1:
                    mine[i-1] = -1
                elif mine[i-1] == 1:
                    mine[i] = -1
            elif mine[i] == 1:
                if mine[i-1] == -1:
                    mine[i+1] = 1
                else:
                    mine[i-1] = 1
                    mine[i+1] = -1
            elif mine[i-1] == -1:
                mine[i] = 1
                mine[i+1] = 1
            else:
                mine[i-1] = 1
                if mine[i] == -1:
                    mine[i+1] = 1
                else:
                    mine[i] = 1
                    mine[i+1] = -1
        else:
            mine[i-1] = 1
            mine[i] = 1
            mine[i+1] = 1

    if N > 1:
        if arr[-1] == '1':
            if mine[-2] == 0:
                mine[-1] = 1
        elif arr[-1] == '2':
            mine[-2] = 1
            mine[-1] = 1

    print(mine.count(1))    
