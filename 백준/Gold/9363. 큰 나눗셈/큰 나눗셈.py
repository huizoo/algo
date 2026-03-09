import sys
input = sys.stdin.readline

Max = 1000000
arr = list(range(Max+1))

for i in range(2, int(Max**0.5)+1):
    if arr[i] == i:
        for j in range(i*i, Max+1, i):
            if arr[j] == j:
                arr[j] = i

def abc(x, k):
    while x > 1:
        p = arr[x]
        cnt[p] += k
        x //= p

def main():
    T = int(input())
    for t in range(1, T+1):
        N, M = map(int, input().split())

        global cnt
        cnt = [0]*(Max+1)
        for a in map(int, input().split()):
            abc(a, 1)

        for b in map(int, input().split()):
            abc(b, -1)
        
        X = Y = 1
        for i, v in enumerate(cnt):
            if v > 0:
                X *= i**v
            elif v < 0:
                Y *= i**(-v)
        
        print(f"Case #{t}: {X} / {Y}")

if __name__ == "__main__":
    main()
