import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
prefix = 0
dic = {0: 1}

for x in arr:
    prefix += x
    cnt += dic.get(prefix - K, 0)
    dic[prefix] = dic.get(prefix, 0) + 1

print(cnt)