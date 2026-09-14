num2alpha = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

def transform(num, q):
    rev_base = ''
    
    if num == 0:
        return '0'
    
    while num > 0:
        num, mod = divmod(num, q)
        if mod > 9:
            rev_base += num2alpha[mod]
        else:
            rev_base += str(mod)
            
    return rev_base[::-1] 

def solution(n, t, m, p):
    st = ''

    i = 0
    while len(st) < t*m:
        st += transform(i, n)
        i += 1
    
    return ''.join(st[i] for i in range(p-1, t*m, m))