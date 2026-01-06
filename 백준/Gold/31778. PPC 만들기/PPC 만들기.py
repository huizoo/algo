import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(input().rstrip())

l = 0
r = n-1

while l < r and k > 0:
    while l < r and S[l] == 'P':
        l += 1
    while l < r and S[r] == 'C' :
        r -= 1
    # S[l] == 'C' and S[r] == 'P' and l < r 일 때 교환
    if l < r:
        S[l], S[r] = S[r], S[l]
    k -= 1
    l += 1
    r -= 1

p = 0
answer = 0

for ch in S:
    if ch == 'P':
        p += 1
    else:
        answer += p*(p-1)//2

print(answer)