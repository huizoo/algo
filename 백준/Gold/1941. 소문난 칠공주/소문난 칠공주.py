import sys
input = sys.stdin.readline

def main():
    arr = [input().rstrip() for _ in range(5)]
    ans = 0
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def bhc(y, x):
        cnt = 1
        q = [(y, x)]
        visited2 = [[0]*5 for _ in range(5)]
        visited2[y][x] = 1
        while q:
            yy, xx = q.pop()
            for dy, dx in d:
                ny, nx = dy+yy, dx+xx
                if 0<=ny<5 and 0<=nx<5 and visited[ny][nx] and not visited2[ny][nx]:
                    visited2[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))
        
        return 1 if cnt == 7 else 0
    
    def dfs(y, x, Ycnt, Scnt, remain):
        nonlocal ans
        if Ycnt>=4:
            return
        if Ycnt+Scnt == 7:
            if bhc(y, x-1):
                ans += 1
            return
        if x == 5:
            y, x = y+1, 0
        if y == 5:
            return
        if Ycnt+Scnt+remain < 7:
            return
        visited[y][x] = 1
        if arr[y][x] == 'S':
            dfs(y, x+1, Ycnt, Scnt+1, remain-1)
        else:
            dfs(y, x+1, Ycnt+1, Scnt, remain-1)  
        visited[y][x] = 0

        dfs(y, x+1, Ycnt, Scnt, remain-1)  

    visited = [[0]*5 for _ in range(5)]
    dfs(0, 0, 0, 0, 25)
    print(ans)

if __name__ == "__main__":
    main()