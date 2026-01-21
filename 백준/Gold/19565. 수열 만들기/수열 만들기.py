import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(1, N+1):
    arr.append(i)
    arr.append(i)
    
    

cnt = N-1
now = N
arr2 = [N]*(N+1)

while True:
    nxt = arr2[now]
    if nxt <= 0:
        break
    elif nxt == now or nxt == now+1:
        if now-1 <= 0: break
        arr2[now] = now-2
        now -= 1
        arr.append(now)
    else:
        arr.append(nxt)
        arr2[now] = nxt-1
        now = nxt

print(len(arr))
print(*arr)