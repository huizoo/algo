import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
Max, Max_idx = 0, -1
Max2 = 0
def abc():
    global Max, Max_idx, Max2
    Max, Max_idx = 0, -1
    Max2 = 0
    for i in range(K):
        now = arr[i]
        if Max == 0:
            Max = now
            Max_idx = i
        elif Max2 == 0:
            if Max < now:
                Max2 = Max
                Max = now
                Max_idx = i
            else:
                Max2 = now
        elif Max < now:
            Max2 = Max
            Max = now
            Max_idx = i
        elif Max2 < now:
            Max2 = now

for _ in range(N-1):
    abc()
    row = list(map(int, input().split()))
    for j in range(K):
        if j != Max_idx:
            arr[j] = row[j]+Max
        else:
            arr[j] = row[j]+Max2
    

print(max(arr))