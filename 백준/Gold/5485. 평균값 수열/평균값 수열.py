import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

start = 2*arr[0]-arr[1]
cnt = 0
for i in range(start, arr[0]+1):
    for j in range(N):
        if arr[j] < i: break
        i = 2*arr[j]-i
    else:
        cnt += 1

print(cnt)
'''
2 5 9
2*2-5 = -1 부터
-1 5 5 13

2*2-4 = 0
0 4 6 12

2*2-3 = 1
1 3 7 11

2*2-2 = 2
2 2 8 10
'''
