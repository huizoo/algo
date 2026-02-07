import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
if N == 1:
    print(arr[0])
    sys.exit()
x = 0
X = [0]*N
Y = [0]*N
def inorder(i, level):
    global x
    if i >= N:
        return
    inorder(2*i+1, level+1)
    X[i] = x
    Y[i] = level
    x += 1
    inorder(2*i+2, level+1)
    return

inorder(0, 0)

Max = N.bit_length()
arr2 = [[] for _ in range(Max)]
for i in range(N):
    arr2[Y[i]].append((X[i], arr[i]))

INF = -10**18
ans = INF
for y1 in range(Max):
    temp = [0]*N
    can = [0]*N
    for y2 in range(y1, Max):
        for x, num in arr2[y2]:
            temp[x] = num
            can[x] = 1
        
        now = best = INF
        for i in range(N):
            if can[i] == 0: continue
            # now = max(temp[i], now+temp[i])
            # best = max(best, now)
            if now < 0:
                now = temp[i]
            else:
                now += temp[i]
            if best < now:
                best = now

        # ans = max(ans, best)
        if ans < best:
            ans = best

print(ans)