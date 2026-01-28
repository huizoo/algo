import sys
input = sys.stdin.readline

def abc(x):
    Sum = 0
    while x: 
        Sum += (x%10)**2
        x //= 10
    return Sum

while True:
    a, b = map(int, input().split())
    if a == 0:
        break
    arr = [None]*20
    arr[0] = a
    arr2 = [None]*20
    arr2[0] = b
    for i in range(1, 20):
        a = abc(a)
        b = abc(b)
        arr[i] = a
        arr2[i] = b
    Min = 41
    for i in range(20):
        x = arr[i]
        for j in range(20):
            if x == arr2[j]:
                Min = min(Min, i+j+2)
    
    print(arr[0], arr2[0], Min if Min != 41 else 0)
