import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    R, G, B = map(int, input().split())
    P = min(N, 7)
    
    Min = 1e9
    def dfs(idx, cnt, Sr, Sg, Sb):
        nonlocal Min
        if cnt >= 2:
            Min = min(Min, (abs(R-Sr//cnt)+abs(G-Sg//cnt)+abs(B-Sb//cnt)))
        if cnt == P:
            return
        
        for i in range(idx+1, N):
            r, g, b = arr[i]
            dfs(i, cnt+1, Sr+r, Sg+g, Sb+b)

    for i in range(N):
        dfs(i, 1, *arr[i])

    print(Min)
    



if __name__ == "__main__":
    solve()