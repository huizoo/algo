import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

even = [0]*N
odd = [0]*N
odd[0] = X[0]

for i in range(1, N):
    x = X[i]
    if i%2 == 0:
        even[i] = even[i-1]
        odd[i] = odd[i-1] + x
    else:
        even[i] = even[i-1] + x
        odd[i] = odd[i-1]

evens = even[N-1]
end = X[N-1]

ans = evens
for i in range(N):
    if i%2 == 0:
        ans = max(ans, odd[i]+evens-even[i+1])
    else:
        ans = max(ans, odd[i]+evens-even[i-1]-end)
    
print(ans)
