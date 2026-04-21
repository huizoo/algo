def solution(mats, park):
    N = len(park)
    M = len(park[0])
    arr = [[0]*(M+1) for _ in range(N+1)]
    for i, row in enumerate(park):
        for j, el in enumerate(row):
            arr[i+1][j+1] = arr[i+1][j] + arr[i][j+1] - arr[i][j] + (1 if el == "-1" else 0)
    
    Max = -1
    mats.sort()
    for i, row in enumerate(park):
        for j, el in enumerate(row):
            if el == "-1":
                for m in mats:
                    if i+m <= N and j+m <= M and \
                        m**2 == arr[i+m][j+m] - arr[i][j+m] - arr[i+m][j] + arr[i][j]:
                        Max = max(Max, m)
                    else:
                        break

    return Max