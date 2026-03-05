import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    a, b = input().rstrip().split('.')
    arr.append((a, b))

arr.sort()    
ex = set(input().rstrip() for _ in range(M))

pre = None
ans = []
ans2 = []
answer = []
for a, b in arr:
    if pre != a:
        for x in ans2:
            answer.append(pre+'.'+x)
        ans2 = []
        for x in ans:
            answer.append(pre+'.'+x)
        ans = []
        pre = a
    if b in ex:
        ans2.append(b)
    else:
        ans.append(b)

for x in ans2:
    answer.append(pre+'.'+x)
for x in ans:
    answer.append(pre+'.'+x)

print('\n'.join(answer))
