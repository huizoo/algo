import sys
input = sys.stdin.readline
N = int(input())
zero = 0
pos = []
neg = []
for _ in range(N):
    x = int(input())
    if x < 0:
        neg.append(x)
    elif x > 0:
        pos.append(x)
    else:
        zero += 1

pos.sort()
neg.sort(reverse=True)

Sum = 0
nl = len(neg)
pl = len(pos)
if nl%2 == 0:
    for _ in range(nl//2):
        Sum += neg.pop()*neg.pop()
    for _ in range(pl//2):
        a, b = pos.pop(), pos.pop()
        if a == 1 or b == 1:
            Sum += a+b
        else:
            Sum += a*b
    if pos:
        Sum += pos.pop()
elif zero > 0:
    for _ in range(nl//2):
        Sum += neg.pop()*neg.pop()
    for _ in range(pl//2):
        a, b = pos.pop(), pos.pop()
        if a == 1 or b == 1:
            Sum += a+b
        else:
            Sum += a*b
    if pos:
        Sum += pos[0]
else:
    for _ in range(nl//2):
        Sum += neg.pop()*neg.pop()
    Sum += neg.pop()
    for _ in range(pl//2):
        a, b = pos.pop(), pos.pop()
        if a == 1 or b == 1:
            Sum += a+b
        else:
            Sum += a*b
    if pos:
        Sum += pos.pop()
    
print(Sum)