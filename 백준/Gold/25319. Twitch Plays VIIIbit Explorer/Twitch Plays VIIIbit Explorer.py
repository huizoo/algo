from collections import defaultdict
import sys
input = sys.stdin.readline


def solve():
    N, M, S = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    dic = defaultdict(list)
    for i in range(N):
        for j in range(M):
            dic[arr[i][j]].append((i, j))
    nick = input().rstrip()

    sy = sx = 0
    ey, ex = N-1, M-1

    need = defaultdict(int)
    for ch in nick:
        need[ch] += 1

    cnt = 1e9
    for ch, v in need.items():
        if ch not in dic:
            cnt = 0
            break
        cnt = min(cnt, len(dic[ch]) // v)

    ans = []
    picked = set()
    for _ in range(cnt):
        temp = []
        sy1, sx1 = sy, sx

        for i in nick:
            for y, x in dic.get(i, []):
                if (y, x) not in picked:
                    picked.add((y, x))
                    if sy1 > y:
                        temp.append('U'*(sy1-y))
                    elif y > sy1:
                        temp.append('D'*(y-sy1))
                    if sx1 > x:
                        temp.append('L'*(sx1-x))
                    elif x > sx1:
                        temp.append('R'*(x-sx1))
                    temp.append('P')
                    sy1, sx1 = y, x
                    break

        ans.extend(temp)
        sy, sx = sy1, sx1

    if sx != ex:
        ans.append('R'*(ex-sx))
    if sy != ey:
        ans.append('D'*(ey-sy))
    
    answer = ''.join(ans)
    print(cnt, len(answer))
    print(answer)


if __name__ == "__main__":
    solve()
