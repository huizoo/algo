import sys
input = sys.stdin.readline
arr = [None]*91
W = input().rstrip()
used = [0]*91
idx = 65
for x in W:
    num = ord(x)
    if used[num]: continue
    used[num] = 1
    arr[idx] = x
    idx += 1


for i in range(65, 91):
    if not used[i]:
        arr[idx] = chr(i)
        idx += 1

S = input().rstrip()
for ch in S:
    print(arr[ord(ch)], end='')