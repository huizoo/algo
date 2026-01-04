import sys
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    odd = even = 0
    for num in arr:
        if num % 2 == 1:
            odd += 1
        else:
            even += 1

    if odd != even:
        if max(odd, even) % 2 == 1:
            answer.append('amsminn') # 채완
        else:
            answer.append('heeda0528') # 희원
    else:
        answer.append('heeda0528') # 희원

print(*answer, sep='\n')