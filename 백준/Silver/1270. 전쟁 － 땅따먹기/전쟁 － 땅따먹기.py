from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    T, *arr = map(int, input().split())
    cand = None
    cnt = 0
    for x in arr:
        if cnt == 0:
            cand = x
            cnt += 1
        elif cand == x:
            cnt += 1
        else:
            cnt -= 1
    
    if arr.count(cand) > T//2:
        print(cand)
    else:
        print('SYJKGW')