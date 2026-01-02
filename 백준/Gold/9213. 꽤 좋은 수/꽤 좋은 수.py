import sys
input = sys.stdin.readline


Max = 1000000
arr = [0]*(Max+1)

for i in range(1, Max//2 + 1):
    for j in range(i*2, Max+1, i):
        arr[j] += i

t = 1
while 1:    
    start, stop, badness = map(int, input().split())
    if start == 0 and stop == 0 and badness == 0: break
    answer = 0

    for i in range(start, stop+1):
        if -badness <= arr[i]-i <= badness:
            answer += 1
        
    print(f'Test {t}: {answer}')
    t += 1