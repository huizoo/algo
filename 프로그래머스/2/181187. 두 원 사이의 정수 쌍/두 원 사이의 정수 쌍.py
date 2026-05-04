from math import isqrt

def get_dot_count(r, pos):
    cnt = 0
    if pos == 'out':
        for x in range(1, r+1):
            cnt += isqrt(r**2-x**2) + 1
    elif pos == 'in':
        for x in range(1, r):
            y_square = r**2-x**2
            y = isqrt(y_square)
            cnt += y if y**2 == y_square else y + 1
        
    return 4 * cnt


def solution(r1, r2):    
    return get_dot_count(r2, 'out') - get_dot_count(r1, 'in')