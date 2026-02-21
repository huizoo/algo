import sys
input = sys.stdin.readline

st = input().rstrip()
ch = input().rstrip()
l = len(st)

dic = dict()
for idx, s in enumerate(st):
    dic[s] = idx+1

cnt = 0
for idx, c in enumerate(ch[::-1]):
    cnt += pow(pow(l, idx, 900528)*dic[c], 1, 900528)

print(cnt%900528)