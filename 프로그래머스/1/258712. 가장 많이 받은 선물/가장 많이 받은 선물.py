def solution(friends, gifts):
    num = {friend: i for i, friend in enumerate(friends)}
    N = len(friends)
    arr = [[0]*N for _ in range(N)]
    for gift in gifts:
        f1, f2 = gift.split()
        arr[num[f1]][num[f2]] += 1
    
    arr2 = list(zip(*arr))
    
    nxt = [0]*N
    Sum = [sum(arr[i])-sum(arr2[i]) for i in range(N)]
    for i, row in enumerate(arr):
        for j in range(i+1, N):
            c1, c2 = arr[i][j], arr[j][i]
            if c1 > c2:
                nxt[i] += 1
            elif c2 > c1:
                nxt[j] += 1
            else:
                g1, g2 = Sum[i], Sum[j]
                if g1 > g2:
                    nxt[i] += 1
                elif g2 > g1:
                    nxt[j] += 1
        
    return max(nxt)