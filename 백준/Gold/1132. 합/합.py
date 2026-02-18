import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*2 for _ in range(10)]

for _ in range(N):
    st = input().rstrip()
    for i in range(1, len(st)+1):
        arr[ord(st[-i])-65][0] += 10**(i-1)
    
    arr[ord(st[0])-65][1] = 1


arr.sort(reverse=True)
flag = 0
for i in range(10):
    if arr[i][0] == 0:
        flag = 1
        break

if flag == 0:
    for i in range(9, -1, -1):
        if not arr[i][0] or arr[i][1]: continue
        arr.append(arr.pop(i))
        break

print(sum(arr[i][0]*(9-i) for i in range(10)))
    