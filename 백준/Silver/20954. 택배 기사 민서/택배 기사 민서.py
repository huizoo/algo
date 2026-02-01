import sys
input = sys.stdin.readline
T = int(input())
answer = []
for _ in range(T):
    x = int(input())
    if x == 0:
        answer.append(x)
        continue
    if x >= 0:
        answer.append(4*(1 << (x-1).bit_length())-4+x)
    else:
        answer.append(6*(1 << (x+1).bit_length())-4-x)

print(*answer, sep='\n')
