from math import comb

def solution(n):
    return comb(2*n, n) // (n+1)
