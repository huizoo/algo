import sys
input = sys.stdin.readline

st = input().rstrip()
arr = [0]*26
a = ord('a')
for x in st:
    arr[ord(x)-a] += 1

print(*arr, sep='\n')