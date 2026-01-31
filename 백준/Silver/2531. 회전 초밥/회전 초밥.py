import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr2 = arr+arr
Max = 0
for i in range(k):
    while i < N:
        if Max == k+1:
            break 
        Set = set()
        for j in range(i, i+k):
            if arr2[j] != c:
                Set.add(arr2[j])
        cnt = len(Set)+1
        if Max < cnt:
            Max = cnt
        i += k
    
print(Max)