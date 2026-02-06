import sys
input = sys.stdin.readline

arr = [0]*10000
arr[0] = 1
arr[1] = 2
arr[2] = 3
arr[3] = 4
arr[4] = 5
arr[5] = 2
arr[6] = 3
used = [10000, 1, 2, 2, 1, 1]
i = 7
j = 1
k = 2
while i <= 10000:
    check_3 = set()
    for l in range(1, j):
        check_3.add(l)
    for l in range(k, 6*k, k):
        for k2 in range(l, l+j):
            check_3.add(k2)
    check_3.add(6*k-1)
    temp = i-6*j
    for l in range(6*k):
        if i + l >= 10000: break
        if l in check_3:
            c1, c2, c3 = arr[i+l-1], arr[temp], arr[temp+1]
            Min = 10000
            ii = -1
            for idx, cnt in enumerate(used):
                if idx == c1 or idx == c2 or idx == c3: continue
                if Min > cnt:
                    Min = cnt
                    ii = idx
            arr[i+l] = ii
            used[ii] += 1
            temp += 1
        else:
            c1, c2 = arr[i+l-1], arr[temp]
            Min = 10000
            ii = -1
            for idx, cnt in enumerate(used):
                if idx == c1 or idx == c2: continue
                if Min > cnt:
                    Min = cnt
                    ii = idx
            arr[i+l] = ii
            used[ii] += 1
    i += 6*k
    j += 1
    k += 1


answer = []
c = int(input())
for _ in range(c):
    n = int(input())
    answer.append(arr[n-1])

print(*answer, sep='\n')