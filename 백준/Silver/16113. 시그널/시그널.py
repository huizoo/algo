import sys
input = sys.stdin.readline
N = int(input())
st = input().rstrip()
x = N//5
i = 0
ans = []
while i < x:
    if st[i] == '.':
        i += 1
        continue
    if st[i+x] == '#':
        if i+2 > x:
            ans.append(1)
            i += 2
            continue
        # 0, 1, 4, 5, 6, 8, 9
        if st[i+1] == '#':
            # 0, 5, 6, 8, 9
            if st[i+1+2*x] == '#':
                # 5, 6, 8, 9
                if st[i+3*x] == '#':
                    # 6, 8
                    if st[i+2+x] == '#':
                        # 8
                        ans.append(8)
                        i += 4
                    else:
                        # 6
                        ans.append(6)
                        i += 4
                elif st[i+2+x] == '#':
                    # 9
                    ans.append(9)
                    i += 4
                else:
                    # 5
                    ans.append(5)
                    i += 4
            else:
                # 0
                ans.append(0)
                i += 4
        elif st[i+1+2*x] == '#':
            # 4
            ans.append(4)
            i += 4
        else:
            # 1
            ans.append(1)
            i += 2
    elif st[i+1+2*x] == '#':
        # 2, 3
        if st[i+3*x] == '#':
            # 2
            ans.append(2)
            i += 4
        else:
            # 3
            ans.append(3)
            i += 4
    else:
        # 7
        ans.append(7)
        i += 4

print(*ans, sep='')
