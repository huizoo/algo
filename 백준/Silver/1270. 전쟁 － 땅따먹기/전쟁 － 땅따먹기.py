from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    T, *arr = map(int, input().split())
    dic = defaultdict(int)
    for x in arr:
        dic[x] += 1
    
    key = value = 0

    for k, v in dic.items():
        if value < v:
            key, value = k, v
    
    if value > T//2:
        print(key)
    else:
        print("SYJKGW")

    