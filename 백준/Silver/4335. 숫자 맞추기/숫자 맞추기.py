import sys
input = sys.stdin.readline

lo = 0; hi = 11
while True:
    num = int(input())
    if num == 0:
        break
    a = input().rstrip()
    if a == 'too high':
        if num < hi:
            hi = num
    elif a == 'too low':
        if lo < num:
            lo = num
    else:
        if lo < num < hi:
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        lo = 0; hi = 11