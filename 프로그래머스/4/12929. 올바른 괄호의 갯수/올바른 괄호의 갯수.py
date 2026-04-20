def solution(n):
    N = [0]*15
    N[0] = 1; N[1] = 1; N[2] = 2; N[3] = 5;
    for i in range(4, 15):
        N[i] = sum(N[j]*N[i-1-j] for j in range(i))
    return N[n]

