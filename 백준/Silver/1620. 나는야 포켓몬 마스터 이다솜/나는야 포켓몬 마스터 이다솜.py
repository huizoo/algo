import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [None]*N
dic = dict()
for i in range(N):
    name = input().rstrip()
    dic[name] = i+1
    arr[i] = name
answer = []
for _ in range(M):
    x = input().rstrip()
    if x.isdigit():
        answer.append(arr[int(x)-1])
    else:
        answer.append(dic[x])

print(*answer, sep='\n')