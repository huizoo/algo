import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

freq = [0]*11
freq[A[0]] += 1

ans = 1

Min = Max = A[0]
l, r = 0, 1
while r < N:
    x = A[r]
    freq[x] += 1
    if Max < x:
        Max = x
        while Max - Min > 2:
            freq[A[l]] -= 1
            l += 1
            for i in range(1, 11):
                if freq[i]:
                    Min = i
                    break
    elif x < Min:
        Min = x
        while Max - Min > 2:
            freq[A[l]] -= 1
            l += 1
            for i in range(10, -1, -1):
                if freq[i]:
                    Max = i
                    break

    ans = max(ans, r-l+1)
    r += 1

print(ans)