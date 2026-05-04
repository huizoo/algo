def get_dot_count(r, pos):
    cnt = 0
    if pos == 'out':
        for x in range(1, r+1):
            cnt += int((r**2-x**2)**0.5) + 1
    elif pos == 'in':
        for x in range(1, r):
            cnt += int(n) + 1 if (n := (r**2-x**2)**0.5) % 1 != 0 else int(n)
        
    return 4 * cnt


def solution(r1, r2):    
    return get_dot_count(r2, 'out') - get_dot_count(r1, 'in')