import sys
input = sys.stdin.readline

Set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
answer = []
while True:
    x = input().rstrip()
    if x[0] == '#':
        break
    cnt = 0
    for i in x:
        if i in Set:
            cnt += 1
    
    answer.append(cnt)

print(*answer, sep='\n')