import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
dic = dict()
prefix = [0]*(N)
prefix[0] = arr[0]
dic.update({prefix[0] : 1})
if prefix[0] == K:
    cnt += 1
for i in range(1, N):
    now = prefix[i] = prefix[i-1] + arr[i]
    if now == K:
        cnt += 1
    cnt += dic.get(now-K, 0)
    if dic.get(now):
        dic[now] += 1
    else:
        dic[now] = 1

print(cnt)