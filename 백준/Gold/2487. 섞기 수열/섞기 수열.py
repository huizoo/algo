import sys
input = sys.stdin.readline
N = int(input())
arr = tuple(map(int, input().split()))

prime = [0]*20001
for i in range(2, 20001):
    prime[i] += 1
    for j in range(i*i, 20001, i):
        prime[j] += 1

visited = [0]*N
Set = set()
for i in range(N):
    x = arr[i]-1
    if visited[x]: continue
    visited[x] = 1
    cnt = 1
    while x != i:
        x = arr[x]-1
        visited[x] = 1
        cnt += 1
    Set.add(cnt)


Max = max(Set)
lst = sorted(Set)
l = len(lst)
ans = 1
for i in range(2, Max+1):
    if prime[i] == 1:
        temp = 0
        for j in range(l):
            temp1 = lst[j]
            temp2 = 0
            while not temp1%i:
                temp2 += 1
                temp1 //= i
            lst[j] = temp1
            if temp < temp2:
                temp = temp2
        if temp:
            ans *= i**temp

print(ans)
