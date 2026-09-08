def solution(n, bans):
    chr_to_ord = {chr(i): i-96 for i in range(97, 123)}
    ord_to_chr = {i-96: chr(i) for i in range(97, 123)}
    
    answer = ''
    bans.sort(key=lambda x: (len(x), x))
    
    def get_ban_order(ban):
        num = 0
        l = len(ban)
        for i in range(l):
            num += chr_to_ord[ban[i]]*(26**(l-i-1))
        return num
    
    for ban in bans:
        if get_ban_order(ban) > n:
            break
        else:
            n += 1
    
    while n > 0:
        if n % 26 == 0:
            answer += ord_to_chr[26]
            n = n // 26 - 1
        else:
            answer += ord_to_chr[n % 26]
            n //= 26
    
    return answer[::-1]


