import sys
input = sys.stdin.readline
N, K = map(int, input().split())
Set = set(map(int, input().split()))
Set2 = set(Set)
house = set()

k = 0
l = 1
Sum = 0

while k < K:
    cnt = 0
    ommission = []

    for x in Set:
        cant = 0
        if x-l not in Set2 and x-l not in house:
            house.add(x-l)
            cnt += 1
        else:
            cant += 1
        if x+l not in Set2 and x+l not in house:
            house.add(x+l)
            cnt += 1
        else:
            cant += 1
        if cant == 2:
            ommission.append(x)

    for x in ommission:
        Set.remove(x)

    if k + cnt > K:
        Sum += l*(K-k)
        break
    else:
        Sum += l*cnt
        k += cnt
    l += 1

print(Sum)