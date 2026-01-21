from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = tuple(map(int, input().split()))

dic = defaultdict(int)
dic[0] = 1

Sum = 0
for i in range(N):
    Sum += arr[i]
    Key = Sum - K*(i+1)
    dic[Key] += 1
    
ans = 0
for cnt in dic.values():
    ans += cnt*(cnt-1)//2

print(ans)