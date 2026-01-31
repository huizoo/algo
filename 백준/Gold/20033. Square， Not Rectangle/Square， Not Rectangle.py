import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

left = [-1]*N
right = [N]*N
stack = []

for i in range(N):
    while stack and H[stack[-1]] > H[i]:
        right[stack.pop()] = i
    stack.append(i)

stack.clear()

for i in range(N-1, -1, -1):
    while stack and H[stack[-1]] > H[i]:
        left[stack.pop()] = i
    stack.append(i)

Max = 0
for i in range(N):
    h = H[i]
    w = right[i] - left[i] - 1
    hw = min(h, w)
    if Max < hw:
        Max = hw

print(Max)