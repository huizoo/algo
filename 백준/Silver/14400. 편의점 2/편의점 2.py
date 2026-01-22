import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = tuple(zip(*[tuple(map(int, input().split())) for _ in range(N)]))
    arr1, arr2 = sorted(arr[0]), sorted(arr[1])
    Sum = 0
    mid1, mid2 = arr1[N//2], arr2[N//2]
    
    for i in range(N):
        Sum += abs(arr1[i] - mid1) + abs(arr2[i] - mid2)
    print(Sum)

solve()

