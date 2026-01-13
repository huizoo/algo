import sys
input = sys.stdin.readline

N = -int(input())
if N == 0:
    print(0)
    sys.exit()

l = N.bit_length()
answer = []
while N != 0:
    if N%-2 == -1:
        answer.append(1)
    else:
        answer.append(0)
    N//=-2

print(*answer[::-1], sep='')
    
