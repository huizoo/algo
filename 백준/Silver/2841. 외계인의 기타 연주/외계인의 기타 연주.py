import sys
input = sys.stdin.readline

N, P = map(int, input().split())

arr = [[] for _ in range(7)]
arr2 = [0]*7
cnt = 0

def abc(x, y):
    global cnt
    now = arr2[x]    
    if now == 0:
        arr[x].append(y)
        arr2[x] = y
        cnt += 1
    elif now > y:
        while arr[x]:
            last = arr[x][-1]
            if last > y:
                arr[x].pop()
                cnt += 1
                arr2[x] = arr[x][-1] if arr[x] else 0
            elif last < y:
                arr[x].append(y)
                arr2[x] = y
                cnt += 1
                break
            else:
                break
        else:
            arr[x].append(y)
            arr2[x] = y
            cnt += 1
    elif now < y:
        arr[x].append(y)
        arr2[x] = y
        cnt += 1       
    

for _ in range(N):
    l, p = map(int, input().split())
    abc(l, p)

print(cnt)