import sys
input = sys.stdin.readline

def main():
    arr = [input().rstrip() for _ in range(5)]
    arr2 = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'Y':
                arr2[i][j] = 1
    ans = 0
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    def dfs(level, Ycnt, mask):
        nonlocal ans
        if Ycnt == 4:
            return
        if level == 7:
            ans += 0 if mask in seen else 1
            seen.add(mask)
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
        
            dfs(level+1, Ycnt+arr2[y][x], mask | 1<<(5*y+x))
        
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

            dfs(1, arr2[i][j], 1<<(5*i+j))
            

    print(ans)

if __name__ == "__main__":
    main()