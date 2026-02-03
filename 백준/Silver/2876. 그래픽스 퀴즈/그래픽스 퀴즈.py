import sys
input = sys.stdin.readline
N = int(input())
cnt = [0]*6
Max = [0]*6
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(1, 6):
        if i == a:
            cnt[i] += 1
            if Max[i] < cnt[i]:
                Max[i] = cnt[i]
        elif i == b:
            cnt[i] += 1
            if Max[i] < cnt[i]:
                Max[i] = cnt[i]
        else:
            cnt[i] = 0

grade = cnt = 0
for idx, value in enumerate(Max):
    if cnt < value:
        cnt = value
        grade = idx

print(cnt, grade)