import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

Max = 0


for i in range(N):
    #left
    ratio1 = ratio2 = 21e8
    cnt1 = cnt2 = 0
    for j in range(i-1, -1, -1):
        h = arr[i]-arr[j]
        ratio3 = h/(i-j)
        if ratio1 == 21e8:
            ratio1 = ratio3
            cnt1 += 1
        elif ratio1 > ratio3:
            ratio1 = ratio3
            cnt1 += 1
        else: continue

    #right
    for j in range(i+1, N):
        h = arr[i]-arr[j]
        ratio4 = h/(j-i)
        if ratio2 == 21e8:
            ratio2 = ratio4
            cnt2 += 1
        elif ratio2 > ratio4:
            ratio2 = ratio4
            cnt2 += 1
        else: continue

    Max = max(Max, cnt1+cnt2)

print(Max)