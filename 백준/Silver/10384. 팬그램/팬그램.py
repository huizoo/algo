import sys
input = sys.stdin.readline
for t in range(1, int(input())+1):
    st = input().rstrip()
    l = ord('A'); r = ord('Z')
    cnt = [0]*(r+1)
    for ch in st:
        x = ord(ch.upper())
        if l <= x <= r:
            cnt[x] += 1
    
    n = min(cnt[l:])
    if n == 0:
        print(f'Case {t}: Not a pangram')
    elif n == 1:
        print(f'Case {t}: Pangram!')
    elif n == 2:
        print(f'Case {t}: Double pangram!!')
    else:
        print(f'Case {t}: Triple pangram!!!')

