import sys
input = sys.stdin.readline
t = 1
while True:
    st = input().rstrip()
    if st[0] == '-':
        break
    ans = 0
    op = 0
    for ch in st:
        if ch == '{':
            op += 1
        elif op:
            op -= 1
        else:
            op += 1
            ans += 1
    ans += op//2

    print(f'{t}. {ans}')
    t += 1