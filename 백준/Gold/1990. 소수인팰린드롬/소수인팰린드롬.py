import sys
input = sys.stdin.readline
a, b = map(int, input().split())
prime = [0]*(10001)
p = []
for i in range(2, 10001):
    if prime[i] == 0:
        p.append(i)
        for j in range(i**2, 10001, i):
            prime[j] = 1

def abc():
    if 5 <= b:
        yield 5
    if 7 <= b:
        yield 7
    if 11 <= b:
        yield 11

    x = 10
    while True:
        num = str(x)
        pal = int(num + num[-2::-1])
        if pal > b:
            break
        yield pal
        x += 1

def bhc(n):
    if n < 2:
        return 0
    for x in p:
        if x * x > n:
            return True
        if n % x == 0:
            return n == x
    return True

answer = []

for pal in abc():
    if pal < a:
        continue
    if bhc(pal):
        answer.append(str(pal))


answer.append('-1')
print('\n'.join(answer))