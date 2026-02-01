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
        y = 2**(x-1).bit_length()
        answer.append(y*4-4+x)
    else:
        y = 2**(x+1).bit_length()
        answer.append(y*6-4-x)

print(*answer, sep='\n')
