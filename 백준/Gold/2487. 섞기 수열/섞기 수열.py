import sys
input = sys.stdin.readline
N = int(input())
arr = tuple(map(int, input().split()))

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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

ans = 1
for num in Set:
    ans = lcm(ans, num)

print(ans)