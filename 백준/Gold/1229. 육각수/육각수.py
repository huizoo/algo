import sys
input = sys.stdin.readline

N = int(input())

'''
1 -> 6
2 -> 12 + 3
3 -> 18 + 7 + 3
4 -> 24 + 11 + 7 + 3 
5 -> 30 + 15 + 11 + 7 + 3 
'''
hexa = []
i = 1
while True:
    h = 6*(i-1) + 3*(i-2) + 2*(i-3)*(i-2)
    if h > N:
        break
    hexa.append(h)
    i += 1

H = set(hexa)

if N in H:
    print(1)
    sys.exit()

for a in hexa:
    if N - a in H:
        print(2)
        sys.exit()

for a in hexa:
    for b in hexa:
        if a + b > N:
            break
        if N - a - b in H:
            print(3)
            sys.exit()

if N > 1791:
    print(4)
    sys.exit()


dp = [1e9] * (N + 1)
dp[0] = 0

for x in range(1, N + 1):
    for h in hexa:
        if h > x:
            break
        dp[x] = min(dp[x], dp[x - h] + 1)

print(dp[N])