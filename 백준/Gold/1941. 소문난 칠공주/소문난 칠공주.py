import sys
input = sys.stdin.readline

def main():
    arr = [input().rstrip() for _ in range(5)]
    ans = 0
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    def update():
        mask = 0
        for i in range(5):
            for j in range(5):
                if visited[i][j]:
                    mask |= 1<<(i*5+j)
        if mask not in seen:
            seen.add(mask)
            return 1
        return 0

    def dfs(Ycnt, Scnt):
        nonlocal ans
        if Ycnt == 4:
            return
        if Ycnt+Scnt == 7:
            ans += update()
            return
        for y, x in list(cands):
            lst = []
            removed = (y, x)

            cands.remove((y, x))
            visited[y][x] = 1

            for dy, dx in d:
                ny, nx = dy+y, dx+x
                if 0<=ny<5 and 0<=nx<5 and not visited[ny][nx]:
                    if (ny, nx) not in cands:
                        cands.add((ny, nx))
                        lst.append((ny, nx))
        
            if arr[y][x] == 'S':
                dfs(Ycnt, Scnt+1)
            else:
                dfs(Ycnt+1, Scnt)
        
            visited[y][x] = 0
            for i in lst:
                cands.remove(i)
            cands.add(removed)        

    visited = [[0]*5 for _ in range(5)]
    cands = set()
    seen = set()
    for i in range(5):
        for j in range(5):
            visited[i][j] = 1
            cands.clear()
            for di, dj in d:
                ni, nj = di+i, dj+j
                if 0<=ni<5 and 0<=nj<5 and not visited[ni][nj]:
                    cands.add((ni, nj))

            if arr[i][j] == 'S':
                dfs(0, 1)
            else:
                dfs(1, 0)
            

    print(ans)

if __name__ == "__main__":
    main()